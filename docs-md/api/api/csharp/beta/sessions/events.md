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

class BetaManagedAgentsSessionDeletedEvent:

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

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

class BetaManagedAgentsSessionDeletedEvent:

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

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

class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

required string ID

Unique identifier for this event.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEventParams:

Parameters for sending an interrupt to pause the agent.

required Type Type

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
