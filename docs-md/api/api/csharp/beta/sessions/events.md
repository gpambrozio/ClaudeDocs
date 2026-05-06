# Events

Copy page

C#

# Events

##### [List Events](api/beta/sessions/events/list.md)

[EventListPageResponse](api/beta.md) Beta.Sessions.Events.List(EventListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

[BetaManagedAgentsSendSessionEvents](api/beta.md) Beta.Sessions.Events.Send(EventSendParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

[BetaManagedAgentsStreamSessionEvents](api/beta.md) Beta.Sessions.Events.StreamStreaming(EventStreamParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/events/stream

##### ModelsExpand Collapse

class BetaManagedAgentsAgentCustomToolUseEvent:

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string Name

Name of the custom tool being called.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

string? SessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

class BetaManagedAgentsAgentMcpToolResultEvent:

Event representing the result of an MCP tool execution.

required string ID

Unique identifier for this event.

required string McpToolUseID

The id of the `agent.mcp_tool_use` event this result corresponds to.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentMcpToolUseEvent:

Event emitted when the agent invokes a tool provided by an MCP server.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string McpServerName

Name of the MCP server providing the tool.

required string Name

Name of the MCP tool being used.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

EvaluatedPermission EvaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"Allow

"ask"Ask

"deny"Deny

string? SessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

class BetaManagedAgentsAgentMessageEvent:

An agent response event in the session conversation.

required string ID

Unique identifier for this event.

required IReadOnlyList<[BetaManagedAgentsTextBlock](api/beta.md)> Content

Array of text blocks comprising the agent response.

required string Text

The text content.

required Type Type

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentThinkingEvent:

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentThreadContextCompactedEvent:

Indicates that context compaction (summarization) occurred during the session.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentThreadMessageReceivedEvent:

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

required string ID

Unique identifier for this event.

required IReadOnlyList<Content> Content

Message content blocks.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required string FromSessionThreadID

Public `sthr_` ID of the thread that sent the message.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

string? FromAgentName

Name of the callable agent this message came from. Absent when received from the primary agent.

class BetaManagedAgentsAgentThreadMessageSentEvent:

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

required string ID

Unique identifier for this event.

required IReadOnlyList<Content> Content

Message content blocks.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string ToSessionThreadID

Public `sthr_` ID of the thread the message was sent to.

required Type Type

string? ToAgentName

Name of the callable agent this message was sent to. Absent when sent to the primary agent.

class BetaManagedAgentsAgentToolResultEvent:

Event representing the result of an agent tool execution.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string ToolUseID

The id of the `agent.tool_use` event this result corresponds to.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent:

Event emitted when the agent invokes a built-in agent tool.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string Name

Name of the agent tool being used.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

EvaluatedPermission EvaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"Allow

"ask"Ask

"deny"Deny

string? SessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

class BetaManagedAgentsEventParams: A class that can be one of several variants.union

Union type for event parameters that can be sent to a session.

class BetaManagedAgentsUserMessageEventParams:

Parameters for sending a user message to the session.

required IReadOnlyList<Content> Content

Array of content blocks for the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type

class BetaManagedAgentsUserInterruptEventParams:

Parameters for sending an interrupt to pause the agent.

required Type Type

string? SessionThreadID

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

class BetaManagedAgentsUserToolConfirmationEventParams:

Parameters for confirming or denying a tool execution request.

required Result Result

UserToolConfirmationResult enum

Accepts one of the following:

"allow"Allow

"deny"Deny

required string ToolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

string? DenyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

class BetaManagedAgentsUserCustomToolResultEventParams:

Parameters for providing the result of a custom tool execution.

required string CustomToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

class BetaManagedAgentsUserDefineOutcomeEventParams:

Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

required string Description

What the agent should produce. This is the task specification.

required Rubric Rubric

Rubric for grading the quality of an outcome.

Accepts one of the following:

class BetaManagedAgentsFileRubricParams:

Rubric referenced by a file uploaded via the Files API.

required string FileID

ID of the rubric file.

required Type Type

class BetaManagedAgentsTextRubricParams:

Rubric content provided inline as text.

required string Content

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

required Type Type

required Type Type

Int? MaxIterations

Eval→revision cycles before giving up. Default 3, max 20.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

class BetaManagedAgentsFileRubric:

Rubric referenced by a file uploaded via the Files API.

required string FileID

ID of the rubric file.

required Type Type

class BetaManagedAgentsFileRubricParams:

Rubric referenced by a file uploaded via the Files API.

required string FileID

ID of the rubric file.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

required string McpServerName

Name of the MCP server that failed authentication.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

required string McpServerName

Name of the MCP server that failed to connect.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

class BetaManagedAgentsSendSessionEvents:

Events that were successfully sent to the session.

IReadOnlyList<Data> Data

Sent events

Accepts one of the following:

class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

required string ID

Unique identifier for this event.

required IReadOnlyList<Content> Content

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

required string ID

Unique identifier for this event.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

required string ID

Unique identifier for this event.

required Result Result

UserToolConfirmationResult enum

Accepts one of the following:

"allow"Allow

"deny"Deny

required string ToolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

string? DenyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

required string ID

Unique identifier for this event.

required string CustomToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

class BetaManagedAgentsUserDefineOutcomeEvent:

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

required string ID

Unique identifier for this event.

required string Description

What the agent should produce. Copied from the input event.

required Int? MaxIterations

Evaluate-then-revise cycles before giving up. Default 3, max 20.

required string OutcomeID

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Rubric Rubric

Rubric for grading the quality of an outcome.

Accepts one of the following:

class BetaManagedAgentsFileRubric:

Rubric referenced by a file uploaded via the Files API.

required string FileID

ID of the rubric file.

required Type Type

class BetaManagedAgentsTextRubric:

Rubric content provided inline as text.

required string Content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

required Type Type

required Type Type

class BetaManagedAgentsSessionDeletedEvent:

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

required Type Type

class BetaManagedAgentsSessionErrorEvent:

An error event indicating a problem occurred during session execution.

required string ID

Unique identifier for this event.

required Error Error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

required string McpServerName

Name of the MCP server that failed to connect.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

required string McpServerName

Name of the MCP server that failed authentication.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionEvent: A class that can be one of several variants.union

Union type for all event types in a session.

class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

required string ID

Unique identifier for this event.

required IReadOnlyList<Content> Content

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

required string ID

Unique identifier for this event.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

required string ID

Unique identifier for this event.

required Result Result

UserToolConfirmationResult enum

Accepts one of the following:

"allow"Allow

"deny"Deny

required string ToolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

string? DenyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

required string ID

Unique identifier for this event.

required string CustomToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

class BetaManagedAgentsAgentCustomToolUseEvent:

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string Name

Name of the custom tool being called.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

string? SessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

class BetaManagedAgentsAgentMessageEvent:

An agent response event in the session conversation.

required string ID

Unique identifier for this event.

required IReadOnlyList<[BetaManagedAgentsTextBlock](api/beta.md)> Content

Array of text blocks comprising the agent response.

required string Text

The text content.

required Type Type

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentThinkingEvent:

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentMcpToolUseEvent:

Event emitted when the agent invokes a tool provided by an MCP server.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string McpServerName

Name of the MCP server providing the tool.

required string Name

Name of the MCP tool being used.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

EvaluatedPermission EvaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"Allow

"ask"Ask

"deny"Deny

string? SessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

class BetaManagedAgentsAgentMcpToolResultEvent:

Event representing the result of an MCP tool execution.

required string ID

Unique identifier for this event.

required string McpToolUseID

The id of the `agent.mcp_tool_use` event this result corresponds to.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent:

Event emitted when the agent invokes a built-in agent tool.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string Name

Name of the agent tool being used.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

EvaluatedPermission EvaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"Allow

"ask"Ask

"deny"Deny

string? SessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

class BetaManagedAgentsAgentToolResultEvent:

Event representing the result of an agent tool execution.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string ToolUseID

The id of the `agent.tool_use` event this result corresponds to.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentThreadMessageReceivedEvent:

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

required string ID

Unique identifier for this event.

required IReadOnlyList<Content> Content

Message content blocks.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required string FromSessionThreadID

Public `sthr_` ID of the thread that sent the message.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

string? FromAgentName

Name of the callable agent this message came from. Absent when received from the primary agent.

class BetaManagedAgentsAgentThreadMessageSentEvent:

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

required string ID

Unique identifier for this event.

required IReadOnlyList<Content> Content

Message content blocks.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string ToSessionThreadID

Public `sthr_` ID of the thread the message was sent to.

required Type Type

string? ToAgentName

Name of the callable agent this message was sent to. Absent when sent to the primary agent.

class BetaManagedAgentsAgentThreadContextCompactedEvent:

Indicates that context compaction (summarization) occurred during the session.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionErrorEvent:

An error event indicating a problem occurred during session execution.

required string ID

Unique identifier for this event.

required Error Error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

required string McpServerName

Name of the MCP server that failed to connect.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

required string McpServerName

Name of the MCP server that failed authentication.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionStatusRescheduledEvent:

Indicates the session is recovering from an error state and is rescheduled for execution.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionStatusRunningEvent:

Indicates the session is actively running and the agent is working.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionStatusIdleEvent:

Indicates the agent has paused and is awaiting user input.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required StopReason StopReason

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

required Type Type

class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

required IReadOnlyList<string> EventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

required Type Type

class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

required Type Type

required Type Type

class BetaManagedAgentsSessionStatusTerminatedEvent:

Indicates the session has terminated, either due to an error or completion.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionThreadCreatedEvent:

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

required string ID

Unique identifier for this event.

required string AgentName

Name of the callable agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public `sthr_` ID of the newly created thread.

required Type Type

class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:

Emitted when an outcome evaluation cycle begins.

required string ID

Unique identifier for this event.

required Int Iteration

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

required string OutcomeID

The `outc_` ID of the outcome being evaluated.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

required string ID

Unique identifier for this event.

required string Explanation

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

required Int Iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

required string OutcomeEvaluationStartID

The id of the corresponding `span.outcome_evaluation_start` event.

required string OutcomeID

The `outc_` ID of the outcome being evaluated.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string Result

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

required Type Type

required [BetaManagedAgentsSpanModelUsage](api/beta.md) Usage

Token usage for a single model request.

required Int CacheCreationInputTokens

Tokens used to create prompt cache in this request.

required Int CacheReadInputTokens

Tokens read from prompt cache in this request.

required Int InputTokens

Input tokens consumed by this request.

required Int OutputTokens

Output tokens generated by this request.

Speed? Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"Standard

"fast"Fast

class BetaManagedAgentsSpanModelRequestStartEvent:

Emitted when a model request is initiated by the agent.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSpanModelRequestEndEvent:

Emitted when a model request completes.

required string ID

Unique identifier for this event.

required Boolean? IsError

Whether the model request resulted in an error.

required string ModelRequestStartID

The id of the corresponding `span.model_request_start` event.

required [BetaManagedAgentsSpanModelUsage](api/beta.md) ModelUsage

Token usage for a single model request.

required Int CacheCreationInputTokens

Tokens used to create prompt cache in this request.

required Int CacheReadInputTokens

Tokens read from prompt cache in this request.

required Int InputTokens

Input tokens consumed by this request.

required Int OutputTokens

Output tokens generated by this request.

Speed? Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"Standard

"fast"Fast

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

required string ID

Unique identifier for this event.

required Int Iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

required string OutcomeID

The `outc_` ID of the outcome being evaluated.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsUserDefineOutcomeEvent:

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

required string ID

Unique identifier for this event.

required string Description

What the agent should produce. Copied from the input event.

required Int? MaxIterations

Evaluate-then-revise cycles before giving up. Default 3, max 20.

required string OutcomeID

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Rubric Rubric

Rubric for grading the quality of an outcome.

Accepts one of the following:

class BetaManagedAgentsFileRubric:

Rubric referenced by a file uploaded via the Files API.

required string FileID

ID of the rubric file.

required Type Type

class BetaManagedAgentsTextRubric:

Rubric content provided inline as text.

required string Content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

required Type Type

required Type Type

class BetaManagedAgentsSessionDeletedEvent:

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionThreadStatusRunningEvent:

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

required string ID

Unique identifier for this event.

required string AgentName

Name of the agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public sthr\_ ID of the thread that started running.

required Type Type

class BetaManagedAgentsSessionThreadStatusIdleEvent:

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

required string ID

Unique identifier for this event.

required string AgentName

Name of the agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public sthr\_ ID of the thread that went idle.

required StopReason StopReason

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

required Type Type

class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

required IReadOnlyList<string> EventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

required Type Type

class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

required Type Type

required Type Type

class BetaManagedAgentsSessionThreadStatusTerminatedEvent:

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

required string ID

Unique identifier for this event.

required string AgentName

Name of the agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public sthr\_ ID of the thread that terminated.

required Type Type

class BetaManagedAgentsSessionThreadStatusRescheduledEvent:

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

required string ID

Unique identifier for this event.

required string AgentName

Name of the agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public sthr\_ ID of the thread that is retrying.

required Type Type

class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

required IReadOnlyList<string> EventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

required Type Type

class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

required Type Type

class BetaManagedAgentsSessionStatusIdleEvent:

Indicates the agent has paused and is awaiting user input.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required StopReason StopReason

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

required Type Type

class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

required IReadOnlyList<string> EventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

required Type Type

class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

required Type Type

required Type Type

class BetaManagedAgentsSessionStatusRescheduledEvent:

Indicates the session is recovering from an error state and is rescheduled for execution.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionStatusRunningEvent:

Indicates the session is actively running and the agent is working.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionStatusTerminatedEvent:

Indicates the session has terminated, either due to an error or completion.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionThreadCreatedEvent:

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

required string ID

Unique identifier for this event.

required string AgentName

Name of the callable agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public `sthr_` ID of the newly created thread.

required Type Type

class BetaManagedAgentsSessionThreadStatusIdleEvent:

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

required string ID

Unique identifier for this event.

required string AgentName

Name of the agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public sthr\_ ID of the thread that went idle.

required StopReason StopReason

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

required Type Type

class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

required IReadOnlyList<string> EventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

required Type Type

class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

required Type Type

required Type Type

class BetaManagedAgentsSessionThreadStatusRescheduledEvent:

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

required string ID

Unique identifier for this event.

required string AgentName

Name of the agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public sthr\_ ID of the thread that is retrying.

required Type Type

class BetaManagedAgentsSessionThreadStatusRunningEvent:

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

required string ID

Unique identifier for this event.

required string AgentName

Name of the agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public sthr\_ ID of the thread that started running.

required Type Type

class BetaManagedAgentsSessionThreadStatusTerminatedEvent:

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

required string ID

Unique identifier for this event.

required string AgentName

Name of the agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public sthr\_ ID of the thread that terminated.

required Type Type

class BetaManagedAgentsSpanModelRequestEndEvent:

Emitted when a model request completes.

required string ID

Unique identifier for this event.

required Boolean? IsError

Whether the model request resulted in an error.

required string ModelRequestStartID

The id of the corresponding `span.model_request_start` event.

required [BetaManagedAgentsSpanModelUsage](api/beta.md) ModelUsage

Token usage for a single model request.

required Int CacheCreationInputTokens

Tokens used to create prompt cache in this request.

required Int CacheReadInputTokens

Tokens read from prompt cache in this request.

required Int InputTokens

Input tokens consumed by this request.

required Int OutputTokens

Output tokens generated by this request.

Speed? Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"Standard

"fast"Fast

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSpanModelRequestStartEvent:

Emitted when a model request is initiated by the agent.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSpanModelUsage:

Token usage for a single model request.

required Int CacheCreationInputTokens

Tokens used to create prompt cache in this request.

required Int CacheReadInputTokens

Tokens read from prompt cache in this request.

required Int InputTokens

Input tokens consumed by this request.

required Int OutputTokens

Output tokens generated by this request.

Speed? Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"Standard

"fast"Fast

class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

required string ID

Unique identifier for this event.

required string Explanation

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

required Int Iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

required string OutcomeEvaluationStartID

The id of the corresponding `span.outcome_evaluation_start` event.

required string OutcomeID

The `outc_` ID of the outcome being evaluated.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string Result

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

required Type Type

required [BetaManagedAgentsSpanModelUsage](api/beta.md) Usage

Token usage for a single model request.

required Int CacheCreationInputTokens

Tokens used to create prompt cache in this request.

required Int CacheReadInputTokens

Tokens read from prompt cache in this request.

required Int InputTokens

Input tokens consumed by this request.

required Int OutputTokens

Output tokens generated by this request.

Speed? Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"Standard

"fast"Fast

class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

required string ID

Unique identifier for this event.

required Int Iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

required string OutcomeID

The `outc_` ID of the outcome being evaluated.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:

Emitted when an outcome evaluation cycle begins.

required string ID

Unique identifier for this event.

required Int Iteration

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

required string OutcomeID

The `outc_` ID of the outcome being evaluated.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsStreamSessionEvents: A class that can be one of several variants.union

Server-sent event in the session stream.

class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

required string ID

Unique identifier for this event.

required IReadOnlyList<Content> Content

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

required string ID

Unique identifier for this event.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

required string ID

Unique identifier for this event.

required Result Result

UserToolConfirmationResult enum

Accepts one of the following:

"allow"Allow

"deny"Deny

required string ToolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

string? DenyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

required string ID

Unique identifier for this event.

required string CustomToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

class BetaManagedAgentsAgentCustomToolUseEvent:

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string Name

Name of the custom tool being called.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

string? SessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

class BetaManagedAgentsAgentMessageEvent:

An agent response event in the session conversation.

required string ID

Unique identifier for this event.

required IReadOnlyList<[BetaManagedAgentsTextBlock](api/beta.md)> Content

Array of text blocks comprising the agent response.

required string Text

The text content.

required Type Type

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentThinkingEvent:

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentMcpToolUseEvent:

Event emitted when the agent invokes a tool provided by an MCP server.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string McpServerName

Name of the MCP server providing the tool.

required string Name

Name of the MCP tool being used.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

EvaluatedPermission EvaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"Allow

"ask"Ask

"deny"Deny

string? SessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

class BetaManagedAgentsAgentMcpToolResultEvent:

Event representing the result of an MCP tool execution.

required string ID

Unique identifier for this event.

required string McpToolUseID

The id of the `agent.mcp_tool_use` event this result corresponds to.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent:

Event emitted when the agent invokes a built-in agent tool.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string Name

Name of the agent tool being used.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

EvaluatedPermission EvaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"Allow

"ask"Ask

"deny"Deny

string? SessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

class BetaManagedAgentsAgentToolResultEvent:

Event representing the result of an agent tool execution.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string ToolUseID

The id of the `agent.tool_use` event this result corresponds to.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentThreadMessageReceivedEvent:

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

required string ID

Unique identifier for this event.

required IReadOnlyList<Content> Content

Message content blocks.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required string FromSessionThreadID

Public `sthr_` ID of the thread that sent the message.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

string? FromAgentName

Name of the callable agent this message came from. Absent when received from the primary agent.

class BetaManagedAgentsAgentThreadMessageSentEvent:

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

required string ID

Unique identifier for this event.

required IReadOnlyList<Content> Content

Message content blocks.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string ToSessionThreadID

Public `sthr_` ID of the thread the message was sent to.

required Type Type

string? ToAgentName

Name of the callable agent this message was sent to. Absent when sent to the primary agent.

class BetaManagedAgentsAgentThreadContextCompactedEvent:

Indicates that context compaction (summarization) occurred during the session.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionErrorEvent:

An error event indicating a problem occurred during session execution.

required string ID

Unique identifier for this event.

required Error Error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

required string McpServerName

Name of the MCP server that failed to connect.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

required string McpServerName

Name of the MCP server that failed authentication.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionStatusRescheduledEvent:

Indicates the session is recovering from an error state and is rescheduled for execution.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionStatusRunningEvent:

Indicates the session is actively running and the agent is working.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionStatusIdleEvent:

Indicates the agent has paused and is awaiting user input.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required StopReason StopReason

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

required Type Type

class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

required IReadOnlyList<string> EventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

required Type Type

class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

required Type Type

required Type Type

class BetaManagedAgentsSessionStatusTerminatedEvent:

Indicates the session has terminated, either due to an error or completion.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionThreadCreatedEvent:

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

required string ID

Unique identifier for this event.

required string AgentName

Name of the callable agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public `sthr_` ID of the newly created thread.

required Type Type

class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:

Emitted when an outcome evaluation cycle begins.

required string ID

Unique identifier for this event.

required Int Iteration

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

required string OutcomeID

The `outc_` ID of the outcome being evaluated.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

required string ID

Unique identifier for this event.

required string Explanation

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

required Int Iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

required string OutcomeEvaluationStartID

The id of the corresponding `span.outcome_evaluation_start` event.

required string OutcomeID

The `outc_` ID of the outcome being evaluated.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string Result

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

required Type Type

required [BetaManagedAgentsSpanModelUsage](api/beta.md) Usage

Token usage for a single model request.

required Int CacheCreationInputTokens

Tokens used to create prompt cache in this request.

required Int CacheReadInputTokens

Tokens read from prompt cache in this request.

required Int InputTokens

Input tokens consumed by this request.

required Int OutputTokens

Output tokens generated by this request.

Speed? Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"Standard

"fast"Fast

class BetaManagedAgentsSpanModelRequestStartEvent:

Emitted when a model request is initiated by the agent.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSpanModelRequestEndEvent:

Emitted when a model request completes.

required string ID

Unique identifier for this event.

required Boolean? IsError

Whether the model request resulted in an error.

required string ModelRequestStartID

The id of the corresponding `span.model_request_start` event.

required [BetaManagedAgentsSpanModelUsage](api/beta.md) ModelUsage

Token usage for a single model request.

required Int CacheCreationInputTokens

Tokens used to create prompt cache in this request.

required Int CacheReadInputTokens

Tokens read from prompt cache in this request.

required Int InputTokens

Input tokens consumed by this request.

required Int OutputTokens

Output tokens generated by this request.

Speed? Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"Standard

"fast"Fast

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

required string ID

Unique identifier for this event.

required Int Iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

required string OutcomeID

The `outc_` ID of the outcome being evaluated.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsUserDefineOutcomeEvent:

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

required string ID

Unique identifier for this event.

required string Description

What the agent should produce. Copied from the input event.

required Int? MaxIterations

Evaluate-then-revise cycles before giving up. Default 3, max 20.

required string OutcomeID

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Rubric Rubric

Rubric for grading the quality of an outcome.

Accepts one of the following:

class BetaManagedAgentsFileRubric:

Rubric referenced by a file uploaded via the Files API.

required string FileID

ID of the rubric file.

required Type Type

class BetaManagedAgentsTextRubric:

Rubric content provided inline as text.

required string Content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

required Type Type

required Type Type

class BetaManagedAgentsSessionDeletedEvent:

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionThreadStatusRunningEvent:

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

required string ID

Unique identifier for this event.

required string AgentName

Name of the agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public sthr\_ ID of the thread that started running.

required Type Type

class BetaManagedAgentsSessionThreadStatusIdleEvent:

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

required string ID

Unique identifier for this event.

required string AgentName

Name of the agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public sthr\_ ID of the thread that went idle.

required StopReason StopReason

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

required Type Type

class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

required IReadOnlyList<string> EventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

required Type Type

class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

required Type Type

required Type Type

class BetaManagedAgentsSessionThreadStatusTerminatedEvent:

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

required string ID

Unique identifier for this event.

required string AgentName

Name of the agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public sthr\_ ID of the thread that terminated.

required Type Type

class BetaManagedAgentsSessionThreadStatusRescheduledEvent:

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

required string ID

Unique identifier for this event.

required string AgentName

Name of the agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public sthr\_ ID of the thread that is retrying.

required Type Type

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsTextRubric:

Rubric content provided inline as text.

required string Content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

required Type Type

class BetaManagedAgentsTextRubricParams:

Rubric content provided inline as text.

required string Content

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

required Type Type

class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

required string ID

Unique identifier for this event.

required string CustomToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

class BetaManagedAgentsUserCustomToolResultEventParams:

Parameters for providing the result of a custom tool execution.

required string CustomToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

class BetaManagedAgentsUserDefineOutcomeEvent:

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

required string ID

Unique identifier for this event.

required string Description

What the agent should produce. Copied from the input event.

required Int? MaxIterations

Evaluate-then-revise cycles before giving up. Default 3, max 20.

required string OutcomeID

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Rubric Rubric

Rubric for grading the quality of an outcome.

Accepts one of the following:

class BetaManagedAgentsFileRubric:

Rubric referenced by a file uploaded via the Files API.

required string FileID

ID of the rubric file.

required Type Type

class BetaManagedAgentsTextRubric:

Rubric content provided inline as text.

required string Content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

required Type Type

required Type Type

class BetaManagedAgentsUserDefineOutcomeEventParams:

Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

required string Description

What the agent should produce. This is the task specification.

required Rubric Rubric

Rubric for grading the quality of an outcome.

Accepts one of the following:

class BetaManagedAgentsFileRubricParams:

Rubric referenced by a file uploaded via the Files API.

required string FileID

ID of the rubric file.

required Type Type

class BetaManagedAgentsTextRubricParams:

Rubric content provided inline as text.

required string Content

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

required Type Type

required Type Type

Int? MaxIterations

Eval→revision cycles before giving up. Default 3, max 20.

class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

required string ID

Unique identifier for this event.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

class BetaManagedAgentsUserInterruptEventParams:

Parameters for sending an interrupt to pause the agent.

required Type Type

string? SessionThreadID

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

required string ID

Unique identifier for this event.

required IReadOnlyList<Content> Content

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserMessageEventParams:

Parameters for sending a user message to the session.

required IReadOnlyList<Content> Content

Array of content blocks for the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type

class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

required string ID

Unique identifier for this event.

required Result Result

UserToolConfirmationResult enum

Accepts one of the following:

"allow"Allow

"deny"Deny

required string ToolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

string? DenyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

class BetaManagedAgentsUserToolConfirmationEventParams:

Parameters for confirming or denying a tool execution request.

required Result Result

UserToolConfirmationResult enum

Accepts one of the following:

"allow"Allow

"deny"Deny

required string ToolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

string? DenyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

---

*Copyright © Anthropic. All rights reserved.*
