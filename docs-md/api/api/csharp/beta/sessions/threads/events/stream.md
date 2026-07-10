# Stream Session Thread Events

Copy page



C#

# Stream Session Thread Events

[BetaManagedAgentsStreamSessionThreadEvents](api/beta/sessions/threads.md) Beta.Sessions.Threads.Events.StreamStreaming(EventStreamParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

Stream Session Thread Events

##### ParametersExpand Collapse



EventStreamParams parameters

required string sessionID

Path param: Path parameter session\_id

required string threadID

Path param: Path parameter thread\_id



IReadOnlyList<[AnthropicBeta](api/beta.md)> betas

Header param: Optional header to specify the beta version(s) you want to use.

"message-batches-2024-09-24"MessageBatches2024\_09\_24

"prompt-caching-2024-07-31"PromptCaching2024\_07\_31

"computer-use-2024-10-22"ComputerUse2024\_10\_22

"computer-use-2025-01-24"ComputerUse2025\_01\_24

"pdfs-2024-09-25"Pdfs2024\_09\_25

"token-counting-2024-11-01"TokenCounting2024\_11\_01

"token-efficient-tools-2025-02-19"TokenEfficientTools2025\_02\_19

"output-128k-2025-02-19"Output128k2025\_02\_19

"files-api-2025-04-14"FilesApi2025\_04\_14

"mcp-client-2025-04-04"McpClient2025\_04\_04

"mcp-client-2025-11-20"McpClient2025\_11\_20

"dev-full-thinking-2025-05-14"DevFullThinking2025\_05\_14

"interleaved-thinking-2025-05-14"InterleavedThinking2025\_05\_14

"code-execution-2025-05-22"CodeExecution2025\_05\_22

"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025\_04\_11

"context-1m-2025-08-07"Context1m2025\_08\_07

"context-management-2025-06-27"ContextManagement2025\_06\_27

"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025\_08\_26

"skills-2025-10-02"Skills2025\_10\_02

"fast-mode-2026-02-01"FastMode2026\_02\_01

"output-300k-2026-03-24"Output300k2026\_03\_24

"user-profiles-2026-03-24"UserProfiles2026\_03\_24

"advisor-tool-2026-03-01"AdvisorTool2026\_03\_01

"managed-agents-2026-04-01"ManagedAgents2026\_04\_01

"cache-diagnosis-2026-04-07"CacheDiagnosis2026\_04\_07

"thinking-token-count-2026-05-13"ThinkingTokenCount2026\_05\_13

"server-side-fallback-2026-06-01"ServerSideFallback2026\_06\_01

"fallback-credit-2026-06-01"FallbackCredit2026\_06\_01

"agent-memory-2026-07-22"AgentMemory2026\_07\_22

##### ReturnsExpand Collapse



class BetaManagedAgentsStreamSessionThreadEvents: A class that can be one of several variants.union 

Server-sent event in a single thread's stream.



class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

required string ID

Unique identifier for this event.



required IReadOnlyList<Content> Content

Array of content blocks comprising the user message.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

required string ID

Unique identifier for this event.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

required string ID

Unique identifier for this event.



required Result Result

UserToolConfirmationResult enum

One of the following:

"allow"Allow

"deny"Deny

required string ToolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

string? DenyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.



class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

required string ID

Unique identifier for this event.

required string CustomToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type



IReadOnlyList<Content> Content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



required [BetaManagedAgentsSearchResultCitations](api/beta/sessions/events.md) Citations

Citation settings for a search result.

required Boolean Enabled

Whether citations are enabled for this search result.



required IReadOnlyList<[BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md)> Content

Array of text content blocks from the search result.

required string Text

The text content.

required Type Type

required string Source

The URL source of the search result.

required string Title

The title of the search result.

required Type Type

Boolean? IsError

Whether the tool execution resulted in an error.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.



class BetaManagedAgentsAgentCustomToolUseEvent:

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string Name

Name of the custom tool being called.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

string? SessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.



class BetaManagedAgentsAgentMessageEvent:

An agent response event in the session conversation.

required string ID

Unique identifier for this event.



required IReadOnlyList<[BetaManagedAgentsTextBlock](api/beta/sessions/events.md)> Content

Array of text blocks comprising the agent response.

required string Text

The text content.

required Type Type

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsAgentThinkingEvent:

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsAgentMcpToolUseEvent:

Event emitted when the agent invokes a tool provided by an MCP server.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string McpServerName

Name of the MCP server providing the tool.

required string Name

Name of the MCP tool being used.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



EvaluatedPermission EvaluatedPermission

AgentEvaluatedPermission enum

One of the following:

"allow"Allow

"ask"Ask

"deny"Deny

string? SessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



class BetaManagedAgentsAgentMcpToolResultEvent:

Event representing the result of an MCP tool execution.

required string ID

Unique identifier for this event.

required string McpToolUseID

The id of the `agent.mcp_tool_use` event this result corresponds to.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



IReadOnlyList<Content> Content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



required [BetaManagedAgentsSearchResultCitations](api/beta/sessions/events.md) Citations

Citation settings for a search result.

required Boolean Enabled

Whether citations are enabled for this search result.



required IReadOnlyList<[BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md)> Content

Array of text content blocks from the search result.

required string Text

The text content.

required Type Type

required string Source

The URL source of the search result.

required string Title

The title of the search result.

required Type Type

Boolean? IsError

Whether the tool execution resulted in an error.



class BetaManagedAgentsAgentToolUseEvent:

Event emitted when the agent invokes a built-in agent tool.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string Name

Name of the agent tool being used.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



EvaluatedPermission EvaluatedPermission

AgentEvaluatedPermission enum

One of the following:

"allow"Allow

"ask"Ask

"deny"Deny

string? SessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



class BetaManagedAgentsAgentToolResultEvent:

Event representing the result of an agent tool execution.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string ToolUseID

The id of the `agent.tool_use` event this result corresponds to.

required Type Type



IReadOnlyList<Content> Content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



required [BetaManagedAgentsSearchResultCitations](api/beta/sessions/events.md) Citations

Citation settings for a search result.

required Boolean Enabled

Whether citations are enabled for this search result.



required IReadOnlyList<[BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md)> Content

Array of text content blocks from the search result.

required string Text

The text content.

required Type Type

required string Source

The URL source of the search result.

required string Title

The title of the search result.

required Type Type

Boolean? IsError

Whether the tool execution resulted in an error.



class BetaManagedAgentsAgentThreadMessageReceivedEvent:

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

required string ID

Unique identifier for this event.



required IReadOnlyList<Content> Content

Message content blocks.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required string FromSessionThreadID

Public `sthr_` ID of the thread that sent the message.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

string? FromAgentName

Name of the callable agent this message came from. Absent when received from the primary agent.



class BetaManagedAgentsAgentThreadMessageSentEvent:

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

required string ID

Unique identifier for this event.



required IReadOnlyList<Content> Content

Message content blocks.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string ToSessionThreadID

Public `sthr_` ID of the thread the message was sent to.

required Type Type

string? ToAgentName

Name of the callable agent this message was sent to. Absent when sent to the primary agent.



class BetaManagedAgentsAgentThreadContextCompactedEvent:

Indicates that context compaction (summarization) occurred during the session.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsSessionErrorEvent:

An error event indicating a problem occurred during session execution.

required string ID

Unique identifier for this event.



required Error Error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

One of the following:



class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

required string Message

Human-readable error description.



required RetryStatus RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type



class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

required string Message

Human-readable error description.



required RetryStatus RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type



class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

required string Message

Human-readable error description.



required RetryStatus RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type



class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

required string Message

Human-readable error description.



required RetryStatus RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type



class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

required string McpServerName

Name of the MCP server that failed to connect.

required string Message

Human-readable error description.



required RetryStatus RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type



class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

required string McpServerName

Name of the MCP server that failed authentication.

required string Message

Human-readable error description.



required RetryStatus RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type



class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

required string Message

Human-readable error description.



required RetryStatus RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type



class BetaManagedAgentsCredentialHostUnreachableError:

An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

required string CredentialID

ID of the affected credential.

required string Message

Human-readable error description.



required RetryStatus RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

required string VaultID

ID of the vault containing the affected credential.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsSessionStatusRescheduledEvent:

Indicates the session is recovering from an error state and is rescheduled for execution.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsSessionStatusRunningEvent:

Indicates the session is actively running and the agent is working.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsSessionStatusIdleEvent:

Indicates the agent has paused and is awaiting user input.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format



required StopReason StopReason

The agent completed its turn naturally and is ready for the next user message.

One of the following:



class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

required Type Type



class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

required IReadOnlyList<string> EventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

required Type Type



class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

required Type Type

required Type Type



class BetaManagedAgentsSessionStatusTerminatedEvent:

Indicates the session has terminated, either due to an error or completion.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsSessionThreadCreatedEvent:

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

required string ID

Unique identifier for this event.

required string AgentName

Name of the callable agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public `sthr_` ID of the newly created thread.

required Type Type



class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:

Emitted when an outcome evaluation cycle begins.

required string ID

Unique identifier for this event.

required Int Iteration

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

required string OutcomeID

The `outc_` ID of the outcome being evaluated.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

required string ID

Unique identifier for this event.

required string Explanation

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

required Int Iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

required string OutcomeEvaluationStartID

The id of the corresponding `span.outcome_evaluation_start` event.

required string OutcomeID

The `outc_` ID of the outcome being evaluated.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string Result

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

required Type Type



required [BetaManagedAgentsSpanModelUsage](api/beta/sessions/events.md) Usage

Token usage for a single model request.

required Int CacheCreationInputTokens

Tokens used to create prompt cache in this request.

required Int CacheReadInputTokens

Tokens read from prompt cache in this request.

required Int InputTokens

Input tokens consumed by this request.

required Int OutputTokens

Output tokens generated by this request.



Speed? Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"Standard

"fast"Fast



class BetaManagedAgentsSpanModelRequestStartEvent:

Emitted when a model request is initiated by the agent.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsSpanModelRequestEndEvent:

Emitted when a model request completes.

required string ID

Unique identifier for this event.

required Boolean? IsError

Whether the model request resulted in an error.

required string ModelRequestStartID

The id of the corresponding `span.model_request_start` event.



required [BetaManagedAgentsSpanModelUsage](api/beta/sessions/events.md) ModelUsage

Token usage for a single model request.

required Int CacheCreationInputTokens

Tokens used to create prompt cache in this request.

required Int CacheReadInputTokens

Tokens read from prompt cache in this request.

required Int InputTokens

Input tokens consumed by this request.

required Int OutputTokens

Output tokens generated by this request.



Speed? Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"Standard

"fast"Fast

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

required string ID

Unique identifier for this event.

required Int Iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

required string OutcomeID

The `outc_` ID of the outcome being evaluated.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsUserDefineOutcomeEvent:

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

required string ID

Unique identifier for this event.

required string Description

What the agent should produce. Copied from the input event.

required Int? MaxIterations

Evaluate-then-revise cycles before giving up. Default 3, max 20.

required string OutcomeID

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format



required Rubric Rubric

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubric:

Rubric referenced by a file uploaded via the Files API.

required string FileID

ID of the rubric file.

required Type Type



class BetaManagedAgentsTextRubric:

Rubric content provided inline as text.

required string Content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

required Type Type

required Type Type



class BetaManagedAgentsSessionDeletedEvent:

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsSessionThreadStatusRunningEvent:

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

required string ID

Unique identifier for this event.

required string AgentName

Name of the agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public sthr\_ ID of the thread that started running.

required Type Type



class BetaManagedAgentsSessionThreadStatusIdleEvent:

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

required string ID

Unique identifier for this event.

required string AgentName

Name of the agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public sthr\_ ID of the thread that went idle.



required StopReason StopReason

The agent completed its turn naturally and is ready for the next user message.

One of the following:



class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

required Type Type



class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

required IReadOnlyList<string> EventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

required Type Type



class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

required Type Type

required Type Type



class BetaManagedAgentsSessionThreadStatusTerminatedEvent:

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

required string ID

Unique identifier for this event.

required string AgentName

Name of the agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public sthr\_ ID of the thread that terminated.

required Type Type



class BetaManagedAgentsUserToolResultEvent:

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

required string ID

Unique identifier for this event.

required string ToolUseID

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type



IReadOnlyList<Content> Content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



required [BetaManagedAgentsSearchResultCitations](api/beta/sessions/events.md) Citations

Citation settings for a search result.

required Boolean Enabled

Whether citations are enabled for this search result.



required IReadOnlyList<[BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md)> Content

Array of text content blocks from the search result.

required string Text

The text content.

required Type Type

required string Source

The URL source of the search result.

required string Title

The title of the search result.

required Type Type

Boolean? IsError

Whether the tool execution resulted in an error.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.



class BetaManagedAgentsSessionThreadStatusRescheduledEvent:

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

required string ID

Unique identifier for this event.

required string AgentName

Name of the agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public sthr\_ ID of the thread that is retrying.

required Type Type



class BetaManagedAgentsSessionUpdatedEvent:

Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



[BetaManagedAgentsSessionAgent](api/beta/sessions.md)? Agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

required string ID

required string? Description



required IReadOnlyList<[BetaManagedAgentsMcpServerUrlDefinition](api/beta/agents.md)> McpServers

required string Name

required Type Type

required string Url



required [BetaManagedAgentsModelConfig](api/beta/agents.md) Model

Model identifier and configuration.



required [BetaManagedAgentsModel](api/beta/agents.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"ClaudeSonnet5

High-performance model for coding and agents

"claude-fable-5"ClaudeFable5

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"ClaudeOpus4\_8

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"ClaudeOpus4\_7

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding



Speed Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"Standard

"fast"Fast



required [BetaManagedAgentsSessionMultiagentCoordinator](api/beta/sessions.md)? Multiagent

Resolved coordinator topology with full agent definitions for each roster member.



required IReadOnlyList<[BetaManagedAgentsSessionThreadAgent](api/beta/agents.md)> Agents

Full `agent` definitions the coordinator may spawn as session threads.

required string ID

required string? Description



required IReadOnlyList<[BetaManagedAgentsMcpServerUrlDefinition](api/beta/agents.md)> McpServers

required string Name

required Type Type

required string Url



required [BetaManagedAgentsModelConfig](api/beta/agents.md) Model

Model identifier and configuration.



required [BetaManagedAgentsModel](api/beta/agents.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"ClaudeSonnet5

High-performance model for coding and agents

"claude-fable-5"ClaudeFable5

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"ClaudeOpus4\_8

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"ClaudeOpus4\_7

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding



Speed Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"Standard

"fast"Fast

required string Name



required IReadOnlyList<Skill> Skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

required string SkillID

required Type Type

required string Version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

required string SkillID

required Type Type

required string Version

required string? System



required IReadOnlyList<Tool> Tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



required IReadOnlyList<[BetaManagedAgentsAgentToolConfig](api/beta/agents.md)> Configs

required Boolean Enabled



required Name Name

Built-in agent tool identifier.

One of the following:

"bash"Bash

"edit"Edit

"read"Read

"write"Write

"glob"Glob

"grep"Grep

"web\_fetch"WebFetch

"web\_search"WebSearch



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) DefaultConfig

Resolved default configuration for agent tools.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required Type Type



class BetaManagedAgentsMcpToolset:



required IReadOnlyList<[BetaManagedAgentsMcpToolConfig](api/beta/agents.md)> Configs

required Boolean Enabled

required string Name



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsMcpToolsetDefaultConfig](api/beta/agents.md) DefaultConfig

Resolved default configuration for all tools from an MCP server.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required string McpServerName

required Type Type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

required string Description



required [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) InputSchema

JSON Schema for custom tool input parameters.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required

required string Name

required Type Type

required Type Type

required Int Version

required Type Type

required string Name



required IReadOnlyList<Skill> Skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

required string SkillID

required Type Type

required string Version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

required string SkillID

required Type Type

required string Version

required string? System



required IReadOnlyList<Tool> Tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



required IReadOnlyList<[BetaManagedAgentsAgentToolConfig](api/beta/agents.md)> Configs

required Boolean Enabled



required Name Name

Built-in agent tool identifier.

One of the following:

"bash"Bash

"edit"Edit

"read"Read

"write"Write

"glob"Glob

"grep"Grep

"web\_fetch"WebFetch

"web\_search"WebSearch



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) DefaultConfig

Resolved default configuration for agent tools.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required Type Type



class BetaManagedAgentsMcpToolset:



required IReadOnlyList<[BetaManagedAgentsMcpToolConfig](api/beta/agents.md)> Configs

required Boolean Enabled

required string Name



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsMcpToolsetDefaultConfig](api/beta/agents.md) DefaultConfig

Resolved default configuration for all tools from an MCP server.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required string McpServerName

required Type Type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

required string Description



required [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) InputSchema

JSON Schema for custom tool input parameters.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required

required string Name

required Type Type

required Type Type

required Int Version

IReadOnlyDictionary<string, string> Metadata

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

string? Title

The session's new title. Present only when the update changed it.



class BetaManagedAgentsStartEvent:

Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event\_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model\_request\_end closes the preview. Only sent on stream connections that opt in via event\_deltas; never appears in event history.



required [BetaManagedAgentsStartEventPreview](api/beta/sessions.md) Event

The previewed event's type and id. The event type determines which delta types the preview's event\_delta events carry: agent.message events stream content\_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

One of the following:



class BetaManagedAgentsAgentMessagePreview:

required string ID

The id the buffered agent.message will carry if it is emitted. Matches the event\_id on this preview's event\_delta events.

required Type Type



class BetaManagedAgentsAgentThinkingPreview:

required string ID

The id the buffered agent.thinking will carry if it is emitted. Start-only — no event\_delta events follow.

required Type Type

required Type Type



class BetaManagedAgentsDeltaEvent:

An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event\_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model\_request\_end closes the preview. Only sent on stream connections that opt in via event\_deltas; never appears in event history.



required [BetaManagedAgentsDeltaContent](api/beta/sessions.md) Delta

One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content\_delta fragments, each a partial element of the content array.



required [BetaManagedAgentsTextBlock](api/beta/sessions/events.md) Content

Regular text content.

required string Text

The text content.

required Type Type

required Type Type

Long Index

Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

required string EventID

The id of the event being previewed. Matches event.id on the corresponding event\_start and the buffered event that reconciles the preview.

required Type Type



class BetaManagedAgentsSystemMessageEvent:

A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

required string ID

Unique identifier for this event.



required IReadOnlyList<[BetaManagedAgentsSystemContentBlock](api/beta/sessions.md)> Content

System content blocks. Text-only.

required string Text

The text content.

required Type Type

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsStreamSessionThreadEvents: A class that can be one of several variants.union 

Server-sent event in a single thread's stream.



class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

required string ID

Unique identifier for this event.



required IReadOnlyList<Content> Content

Array of content blocks comprising the user message.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

required string ID

Unique identifier for this event.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

required string ID

Unique identifier for this event.



required Result Result

UserToolConfirmationResult enum

One of the following:

"allow"Allow

"deny"Deny

required string ToolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

string? DenyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.



class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

required string ID

Unique identifier for this event.

required string CustomToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type



IReadOnlyList<Content> Content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



required [BetaManagedAgentsSearchResultCitations](api/beta/sessions/events.md) Citations

Citation settings for a search result.

required Boolean Enabled

Whether citations are enabled for this search result.



required IReadOnlyList<[BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md)> Content

Array of text content blocks from the search result.

required string Text

The text content.

required Type Type

required string Source

The URL source of the search result.

required string Title

The title of the search result.

required Type Type

Boolean? IsError

Whether the tool execution resulted in an error.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.



class BetaManagedAgentsAgentCustomToolUseEvent:

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string Name

Name of the custom tool being called.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

string? SessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.



class BetaManagedAgentsAgentMessageEvent:

An agent response event in the session conversation.

required string ID

Unique identifier for this event.



required IReadOnlyList<[BetaManagedAgentsTextBlock](api/beta/sessions/events.md)> Content

Array of text blocks comprising the agent response.

required string Text

The text content.

required Type Type

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsAgentThinkingEvent:

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsAgentMcpToolUseEvent:

Event emitted when the agent invokes a tool provided by an MCP server.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string McpServerName

Name of the MCP server providing the tool.

required string Name

Name of the MCP tool being used.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



EvaluatedPermission EvaluatedPermission

AgentEvaluatedPermission enum

One of the following:

"allow"Allow

"ask"Ask

"deny"Deny

string? SessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



class BetaManagedAgentsAgentMcpToolResultEvent:

Event representing the result of an MCP tool execution.

required string ID

Unique identifier for this event.

required string McpToolUseID

The id of the `agent.mcp_tool_use` event this result corresponds to.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



IReadOnlyList<Content> Content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



required [BetaManagedAgentsSearchResultCitations](api/beta/sessions/events.md) Citations

Citation settings for a search result.

required Boolean Enabled

Whether citations are enabled for this search result.



required IReadOnlyList<[BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md)> Content

Array of text content blocks from the search result.

required string Text

The text content.

required Type Type

required string Source

The URL source of the search result.

required string Title

The title of the search result.

required Type Type

Boolean? IsError

Whether the tool execution resulted in an error.



class BetaManagedAgentsAgentToolUseEvent:

Event emitted when the agent invokes a built-in agent tool.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string Name

Name of the agent tool being used.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



EvaluatedPermission EvaluatedPermission

AgentEvaluatedPermission enum

One of the following:

"allow"Allow

"ask"Ask

"deny"Deny

string? SessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



class BetaManagedAgentsAgentToolResultEvent:

Event representing the result of an agent tool execution.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string ToolUseID

The id of the `agent.tool_use` event this result corresponds to.

required Type Type



IReadOnlyList<Content> Content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



required [BetaManagedAgentsSearchResultCitations](api/beta/sessions/events.md) Citations

Citation settings for a search result.

required Boolean Enabled

Whether citations are enabled for this search result.



required IReadOnlyList<[BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md)> Content

Array of text content blocks from the search result.

required string Text

The text content.

required Type Type

required string Source

The URL source of the search result.

required string Title

The title of the search result.

required Type Type

Boolean? IsError

Whether the tool execution resulted in an error.



class BetaManagedAgentsAgentThreadMessageReceivedEvent:

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

required string ID

Unique identifier for this event.



required IReadOnlyList<Content> Content

Message content blocks.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required string FromSessionThreadID

Public `sthr_` ID of the thread that sent the message.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

string? FromAgentName

Name of the callable agent this message came from. Absent when received from the primary agent.



class BetaManagedAgentsAgentThreadMessageSentEvent:

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

required string ID

Unique identifier for this event.



required IReadOnlyList<Content> Content

Message content blocks.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string ToSessionThreadID

Public `sthr_` ID of the thread the message was sent to.

required Type Type

string? ToAgentName

Name of the callable agent this message was sent to. Absent when sent to the primary agent.



class BetaManagedAgentsAgentThreadContextCompactedEvent:

Indicates that context compaction (summarization) occurred during the session.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsSessionErrorEvent:

An error event indicating a problem occurred during session execution.

required string ID

Unique identifier for this event.



required Error Error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

One of the following:



class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

required string Message

Human-readable error description.



required RetryStatus RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type



class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

required string Message

Human-readable error description.



required RetryStatus RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type



class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

required string Message

Human-readable error description.



required RetryStatus RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type



class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

required string Message

Human-readable error description.



required RetryStatus RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type



class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

required string McpServerName

Name of the MCP server that failed to connect.

required string Message

Human-readable error description.



required RetryStatus RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type



class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

required string McpServerName

Name of the MCP server that failed authentication.

required string Message

Human-readable error description.



required RetryStatus RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type



class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

required string Message

Human-readable error description.



required RetryStatus RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type



class BetaManagedAgentsCredentialHostUnreachableError:

An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

required string CredentialID

ID of the affected credential.

required string Message

Human-readable error description.



required RetryStatus RetryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

required string VaultID

ID of the vault containing the affected credential.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsSessionStatusRescheduledEvent:

Indicates the session is recovering from an error state and is rescheduled for execution.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsSessionStatusRunningEvent:

Indicates the session is actively running and the agent is working.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsSessionStatusIdleEvent:

Indicates the agent has paused and is awaiting user input.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format



required StopReason StopReason

The agent completed its turn naturally and is ready for the next user message.

One of the following:



class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

required Type Type



class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

required IReadOnlyList<string> EventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

required Type Type



class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

required Type Type

required Type Type



class BetaManagedAgentsSessionStatusTerminatedEvent:

Indicates the session has terminated, either due to an error or completion.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsSessionThreadCreatedEvent:

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

required string ID

Unique identifier for this event.

required string AgentName

Name of the callable agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public `sthr_` ID of the newly created thread.

required Type Type



class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:

Emitted when an outcome evaluation cycle begins.

required string ID

Unique identifier for this event.

required Int Iteration

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

required string OutcomeID

The `outc_` ID of the outcome being evaluated.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

required string ID

Unique identifier for this event.

required string Explanation

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

required Int Iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

required string OutcomeEvaluationStartID

The id of the corresponding `span.outcome_evaluation_start` event.

required string OutcomeID

The `outc_` ID of the outcome being evaluated.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string Result

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

required Type Type



required [BetaManagedAgentsSpanModelUsage](api/beta/sessions/events.md) Usage

Token usage for a single model request.

required Int CacheCreationInputTokens

Tokens used to create prompt cache in this request.

required Int CacheReadInputTokens

Tokens read from prompt cache in this request.

required Int InputTokens

Input tokens consumed by this request.

required Int OutputTokens

Output tokens generated by this request.



Speed? Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"Standard

"fast"Fast



class BetaManagedAgentsSpanModelRequestStartEvent:

Emitted when a model request is initiated by the agent.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsSpanModelRequestEndEvent:

Emitted when a model request completes.

required string ID

Unique identifier for this event.

required Boolean? IsError

Whether the model request resulted in an error.

required string ModelRequestStartID

The id of the corresponding `span.model_request_start` event.



required [BetaManagedAgentsSpanModelUsage](api/beta/sessions/events.md) ModelUsage

Token usage for a single model request.

required Int CacheCreationInputTokens

Tokens used to create prompt cache in this request.

required Int CacheReadInputTokens

Tokens read from prompt cache in this request.

required Int InputTokens

Input tokens consumed by this request.

required Int OutputTokens

Output tokens generated by this request.



Speed? Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"Standard

"fast"Fast

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

required string ID

Unique identifier for this event.

required Int Iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

required string OutcomeID

The `outc_` ID of the outcome being evaluated.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsUserDefineOutcomeEvent:

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

required string ID

Unique identifier for this event.

required string Description

What the agent should produce. Copied from the input event.

required Int? MaxIterations

Evaluate-then-revise cycles before giving up. Default 3, max 20.

required string OutcomeID

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format



required Rubric Rubric

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubric:

Rubric referenced by a file uploaded via the Files API.

required string FileID

ID of the rubric file.

required Type Type



class BetaManagedAgentsTextRubric:

Rubric content provided inline as text.

required string Content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

required Type Type

required Type Type



class BetaManagedAgentsSessionDeletedEvent:

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsSessionThreadStatusRunningEvent:

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

required string ID

Unique identifier for this event.

required string AgentName

Name of the agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public sthr\_ ID of the thread that started running.

required Type Type



class BetaManagedAgentsSessionThreadStatusIdleEvent:

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

required string ID

Unique identifier for this event.

required string AgentName

Name of the agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public sthr\_ ID of the thread that went idle.



required StopReason StopReason

The agent completed its turn naturally and is ready for the next user message.

One of the following:



class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

required Type Type



class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

required IReadOnlyList<string> EventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

required Type Type



class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

required Type Type

required Type Type



class BetaManagedAgentsSessionThreadStatusTerminatedEvent:

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

required string ID

Unique identifier for this event.

required string AgentName

Name of the agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public sthr\_ ID of the thread that terminated.

required Type Type



class BetaManagedAgentsUserToolResultEvent:

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

required string ID

Unique identifier for this event.

required string ToolUseID

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type



IReadOnlyList<Content> Content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



required [BetaManagedAgentsSearchResultCitations](api/beta/sessions/events.md) Citations

Citation settings for a search result.

required Boolean Enabled

Whether citations are enabled for this search result.



required IReadOnlyList<[BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md)> Content

Array of text content blocks from the search result.

required string Text

The text content.

required Type Type

required string Source

The URL source of the search result.

required string Title

The title of the search result.

required Type Type

Boolean? IsError

Whether the tool execution resulted in an error.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.



class BetaManagedAgentsSessionThreadStatusRescheduledEvent:

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

required string ID

Unique identifier for this event.

required string AgentName

Name of the agent the thread runs.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string SessionThreadID

Public sthr\_ ID of the thread that is retrying.

required Type Type



class BetaManagedAgentsSessionUpdatedEvent:

Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



[BetaManagedAgentsSessionAgent](api/beta/sessions.md)? Agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

required string ID

required string? Description



required IReadOnlyList<[BetaManagedAgentsMcpServerUrlDefinition](api/beta/agents.md)> McpServers

required string Name

required Type Type

required string Url



required [BetaManagedAgentsModelConfig](api/beta/agents.md) Model

Model identifier and configuration.



required [BetaManagedAgentsModel](api/beta/agents.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"ClaudeSonnet5

High-performance model for coding and agents

"claude-fable-5"ClaudeFable5

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"ClaudeOpus4\_8

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"ClaudeOpus4\_7

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding



Speed Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"Standard

"fast"Fast



required [BetaManagedAgentsSessionMultiagentCoordinator](api/beta/sessions.md)? Multiagent

Resolved coordinator topology with full agent definitions for each roster member.



required IReadOnlyList<[BetaManagedAgentsSessionThreadAgent](api/beta/agents.md)> Agents

Full `agent` definitions the coordinator may spawn as session threads.

required string ID

required string? Description



required IReadOnlyList<[BetaManagedAgentsMcpServerUrlDefinition](api/beta/agents.md)> McpServers

required string Name

required Type Type

required string Url



required [BetaManagedAgentsModelConfig](api/beta/agents.md) Model

Model identifier and configuration.



required [BetaManagedAgentsModel](api/beta/agents.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"ClaudeSonnet5

High-performance model for coding and agents

"claude-fable-5"ClaudeFable5

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"ClaudeOpus4\_8

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"ClaudeOpus4\_7

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding



Speed Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"Standard

"fast"Fast

required string Name



required IReadOnlyList<Skill> Skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

required string SkillID

required Type Type

required string Version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

required string SkillID

required Type Type

required string Version

required string? System



required IReadOnlyList<Tool> Tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



required IReadOnlyList<[BetaManagedAgentsAgentToolConfig](api/beta/agents.md)> Configs

required Boolean Enabled



required Name Name

Built-in agent tool identifier.

One of the following:

"bash"Bash

"edit"Edit

"read"Read

"write"Write

"glob"Glob

"grep"Grep

"web\_fetch"WebFetch

"web\_search"WebSearch



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) DefaultConfig

Resolved default configuration for agent tools.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required Type Type



class BetaManagedAgentsMcpToolset:



required IReadOnlyList<[BetaManagedAgentsMcpToolConfig](api/beta/agents.md)> Configs

required Boolean Enabled

required string Name



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsMcpToolsetDefaultConfig](api/beta/agents.md) DefaultConfig

Resolved default configuration for all tools from an MCP server.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required string McpServerName

required Type Type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

required string Description



required [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) InputSchema

JSON Schema for custom tool input parameters.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required

required string Name

required Type Type

required Type Type

required Int Version

required Type Type

required string Name



required IReadOnlyList<Skill> Skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

required string SkillID

required Type Type

required string Version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

required string SkillID

required Type Type

required string Version

required string? System



required IReadOnlyList<Tool> Tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



required IReadOnlyList<[BetaManagedAgentsAgentToolConfig](api/beta/agents.md)> Configs

required Boolean Enabled



required Name Name

Built-in agent tool identifier.

One of the following:

"bash"Bash

"edit"Edit

"read"Read

"write"Write

"glob"Glob

"grep"Grep

"web\_fetch"WebFetch

"web\_search"WebSearch



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) DefaultConfig

Resolved default configuration for agent tools.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required Type Type



class BetaManagedAgentsMcpToolset:



required IReadOnlyList<[BetaManagedAgentsMcpToolConfig](api/beta/agents.md)> Configs

required Boolean Enabled

required string Name



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsMcpToolsetDefaultConfig](api/beta/agents.md) DefaultConfig

Resolved default configuration for all tools from an MCP server.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required string McpServerName

required Type Type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

required string Description



required [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) InputSchema

JSON Schema for custom tool input parameters.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required

required string Name

required Type Type

required Type Type

required Int Version

IReadOnlyDictionary<string, string> Metadata

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

string? Title

The session's new title. Present only when the update changed it.



class BetaManagedAgentsStartEvent:

Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event\_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model\_request\_end closes the preview. Only sent on stream connections that opt in via event\_deltas; never appears in event history.



required [BetaManagedAgentsStartEventPreview](api/beta/sessions.md) Event

The previewed event's type and id. The event type determines which delta types the preview's event\_delta events carry: agent.message events stream content\_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

One of the following:



class BetaManagedAgentsAgentMessagePreview:

required string ID

The id the buffered agent.message will carry if it is emitted. Matches the event\_id on this preview's event\_delta events.

required Type Type



class BetaManagedAgentsAgentThinkingPreview:

required string ID

The id the buffered agent.thinking will carry if it is emitted. Start-only — no event\_delta events follow.

required Type Type

required Type Type



class BetaManagedAgentsDeltaEvent:

An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event\_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model\_request\_end closes the preview. Only sent on stream connections that opt in via event\_deltas; never appears in event history.



required [BetaManagedAgentsDeltaContent](api/beta/sessions.md) Delta

One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content\_delta fragments, each a partial element of the content array.



required [BetaManagedAgentsTextBlock](api/beta/sessions/events.md) Content

Regular text content.

required string Text

The text content.

required Type Type

required Type Type

Long Index

Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

required string EventID

The id of the event being previewed. Matches event.id on the corresponding event\_start and the buffered event that reconciles the preview.

required Type Type



class BetaManagedAgentsSystemMessageEvent:

A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

required string ID

Unique identifier for this event.



required IReadOnlyList<[BetaManagedAgentsSystemContentBlock](api/beta/sessions.md)> Content

System content blocks. Text-only.

required string Text

The text content.

required Type Type

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

Stream Session Thread Events

C#

```shiki
EventStreamParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ThreadID = "sthr_011CZkZVWa6oIjw0rgXZpnBt",
};

await foreach (var betaManagedAgentsStreamSessionThreadEvents in client.Beta.Sessions.Threads.Events.StreamStreaming(parameters))
{
    Console.WriteLine(betaManagedAgentsStreamSessionThreadEvents);
}
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
