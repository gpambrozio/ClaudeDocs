# Stream Session Thread Events

Copy page



Java

# Stream Session Thread Events

[BetaManagedAgentsStreamSessionThreadEvents](api/beta.md) beta().sessions().threads().events().streamStreaming(EventStreamParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

Stream Session Thread Events

##### ParametersExpand Collapse



EventStreamParams params

String sessionId

Optional<String> threadId



Optional<List<AnthropicBeta>> betas

Optional header to specify the beta version(s) you want to use.

MESSAGE\_BATCHES\_2024\_09\_24("message-batches-2024-09-24")

PROMPT\_CACHING\_2024\_07\_31("prompt-caching-2024-07-31")

COMPUTER\_USE\_2024\_10\_22("computer-use-2024-10-22")

COMPUTER\_USE\_2025\_01\_24("computer-use-2025-01-24")

PDFS\_2024\_09\_25("pdfs-2024-09-25")

TOKEN\_COUNTING\_2024\_11\_01("token-counting-2024-11-01")

TOKEN\_EFFICIENT\_TOOLS\_2025\_02\_19("token-efficient-tools-2025-02-19")

OUTPUT\_128K\_2025\_02\_19("output-128k-2025-02-19")

FILES\_API\_2025\_04\_14("files-api-2025-04-14")

MCP\_CLIENT\_2025\_04\_04("mcp-client-2025-04-04")

MCP\_CLIENT\_2025\_11\_20("mcp-client-2025-11-20")

DEV\_FULL\_THINKING\_2025\_05\_14("dev-full-thinking-2025-05-14")

INTERLEAVED\_THINKING\_2025\_05\_14("interleaved-thinking-2025-05-14")

CODE\_EXECUTION\_2025\_05\_22("code-execution-2025-05-22")

EXTENDED\_CACHE\_TTL\_2025\_04\_11("extended-cache-ttl-2025-04-11")

CONTEXT\_1M\_2025\_08\_07("context-1m-2025-08-07")

CONTEXT\_MANAGEMENT\_2025\_06\_27("context-management-2025-06-27")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED\_2025\_08\_26("model-context-window-exceeded-2025-08-26")

SKILLS\_2025\_10\_02("skills-2025-10-02")

FAST\_MODE\_2026\_02\_01("fast-mode-2026-02-01")

OUTPUT\_300K\_2026\_03\_24("output-300k-2026-03-24")

USER\_PROFILES\_2026\_03\_24("user-profiles-2026-03-24")

ADVISOR\_TOOL\_2026\_03\_01("advisor-tool-2026-03-01")

MANAGED\_AGENTS\_2026\_04\_01("managed-agents-2026-04-01")

CACHE\_DIAGNOSIS\_2026\_04\_07("cache-diagnosis-2026-04-07")

THINKING\_TOKEN\_COUNT\_2026\_05\_13("thinking-token-count-2026-05-13")

SERVER\_SIDE\_FALLBACK\_2026\_06\_01("server-side-fallback-2026-06-01")

FALLBACK\_CREDIT\_2026\_06\_01("fallback-credit-2026-06-01")

##### ReturnsExpand Collapse



class BetaManagedAgentsStreamSessionThreadEvents: A class that can be one of several variants.union 

Server-sent event in a single thread's stream.



class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

String id

Unique identifier for this event.



List<Content> content

Array of content blocks comprising the user message.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

String id

Unique identifier for this event.

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

String id

Unique identifier for this event.



Result result

UserToolConfirmationResult enum

One of the following:

ALLOW("allow")

DENY("deny")

String toolUseId

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

Optional<String> denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.



class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

String id

Unique identifier for this event.

String customToolUseId

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.



class BetaManagedAgentsAgentCustomToolUseEvent:

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String name

Name of the custom tool being called.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

Optional<String> sessionThreadId

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.



class BetaManagedAgentsAgentMessageEvent:

An agent response event in the session conversation.

String id

Unique identifier for this event.



List<[BetaManagedAgentsTextBlock](api/beta.md)> content

Array of text blocks comprising the agent response.

String text

The text content.

Type type

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsAgentThinkingEvent:

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsAgentMcpToolUseEvent:

Event emitted when the agent invokes a tool provided by an MCP server.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String mcpServerName

Name of the MCP server providing the tool.

String name

Name of the MCP tool being used.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



Optional<EvaluatedPermission> evaluatedPermission

AgentEvaluatedPermission enum

One of the following:

ALLOW("allow")

ASK("ask")

DENY("deny")

Optional<String> sessionThreadId

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



class BetaManagedAgentsAgentMcpToolResultEvent:

Event representing the result of an MCP tool execution.

String id

Unique identifier for this event.

String mcpToolUseId

The id of the `agent.mcp_tool_use` event this result corresponds to.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.



class BetaManagedAgentsAgentToolUseEvent:

Event emitted when the agent invokes a built-in agent tool.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String name

Name of the agent tool being used.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



Optional<EvaluatedPermission> evaluatedPermission

AgentEvaluatedPermission enum

One of the following:

ALLOW("allow")

ASK("ask")

DENY("deny")

Optional<String> sessionThreadId

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



class BetaManagedAgentsAgentToolResultEvent:

Event representing the result of an agent tool execution.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String toolUseId

The id of the `agent.tool_use` event this result corresponds to.

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.



class BetaManagedAgentsAgentThreadMessageReceivedEvent:

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

String id

Unique identifier for this event.



List<Content> content

Message content blocks.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

String fromSessionThreadId

Public `sthr_` ID of the thread that sent the message.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

Optional<String> fromAgentName

Name of the callable agent this message came from. Absent when received from the primary agent.



class BetaManagedAgentsAgentThreadMessageSentEvent:

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

String id

Unique identifier for this event.



List<Content> content

Message content blocks.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String toSessionThreadId

Public `sthr_` ID of the thread the message was sent to.

Type type

Optional<String> toAgentName

Name of the callable agent this message was sent to. Absent when sent to the primary agent.



class BetaManagedAgentsAgentThreadContextCompactedEvent:

Indicates that context compaction (summarization) occurred during the session.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionErrorEvent:

An error event indicating a problem occurred during session execution.

String id

Unique identifier for this event.



Error error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

One of the following:



class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

String mcpServerName

Name of the MCP server that failed to connect.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

String mcpServerName

Name of the MCP server that failed authentication.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsCredentialHostUnreachableError:

An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

String credentialId

ID of the affected credential.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

String vaultId

ID of the vault containing the affected credential.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionStatusRescheduledEvent:

Indicates the session is recovering from an error state and is rescheduled for execution.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionStatusRunningEvent:

Indicates the session is actively running and the agent is working.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionStatusIdleEvent:

Indicates the agent has paused and is awaiting user input.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format



StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

One of the following:



class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

Type type



class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

List<String> eventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type type



class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type type

Type type



class BetaManagedAgentsSessionStatusTerminatedEvent:

Indicates the session has terminated, either due to an error or completion.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionThreadCreatedEvent:

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

String id

Unique identifier for this event.

String agentName

Name of the callable agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public `sthr_` ID of the newly created thread.

Type type



class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:

Emitted when an outcome evaluation cycle begins.

String id

Unique identifier for this event.

long iteration

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

String outcomeId

The `outc_` ID of the outcome being evaluated.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

String id

Unique identifier for this event.

String explanation

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

long iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

String outcomeEvaluationStartId

The id of the corresponding `span.outcome_evaluation_start` event.

String outcomeId

The `outc_` ID of the outcome being evaluated.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String result

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

Type type



[BetaManagedAgentsSpanModelUsage](api/beta.md) usage

Token usage for a single model request.

long cacheCreationInputTokens

Tokens used to create prompt cache in this request.

long cacheReadInputTokens

Tokens read from prompt cache in this request.

long inputTokens

Input tokens consumed by this request.

long outputTokens

Output tokens generated by this request.



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")



class BetaManagedAgentsSpanModelRequestStartEvent:

Emitted when a model request is initiated by the agent.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSpanModelRequestEndEvent:

Emitted when a model request completes.

String id

Unique identifier for this event.

Optional<Boolean> isError

Whether the model request resulted in an error.

String modelRequestStartId

The id of the corresponding `span.model_request_start` event.



[BetaManagedAgentsSpanModelUsage](api/beta.md) modelUsage

Token usage for a single model request.

long cacheCreationInputTokens

Tokens used to create prompt cache in this request.

long cacheReadInputTokens

Tokens read from prompt cache in this request.

long inputTokens

Input tokens consumed by this request.

long outputTokens

Output tokens generated by this request.



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

String id

Unique identifier for this event.

long iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

String outcomeId

The `outc_` ID of the outcome being evaluated.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsUserDefineOutcomeEvent:

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

String id

Unique identifier for this event.

String description

What the agent should produce. Copied from the input event.

Optional<Long> maxIterations

Evaluate-then-revise cycles before giving up. Default 3, max 20.

String outcomeId

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

LocalDateTime processedAt

A timestamp in RFC 3339 format



Rubric rubric

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubric:

Rubric referenced by a file uploaded via the Files API.

String fileId

ID of the rubric file.

Type type



class BetaManagedAgentsTextRubric:

Rubric content provided inline as text.

String content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

Type type

Type type



class BetaManagedAgentsSessionDeletedEvent:

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionThreadStatusRunningEvent:

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

String id

Unique identifier for this event.

String agentName

Name of the agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public sthr\_ ID of the thread that started running.

Type type



class BetaManagedAgentsSessionThreadStatusIdleEvent:

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

String id

Unique identifier for this event.

String agentName

Name of the agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public sthr\_ ID of the thread that went idle.



StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

One of the following:



class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

Type type



class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

List<String> eventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type type



class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type type

Type type



class BetaManagedAgentsSessionThreadStatusTerminatedEvent:

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

String id

Unique identifier for this event.

String agentName

Name of the agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public sthr\_ ID of the thread that terminated.

Type type



class BetaManagedAgentsUserToolResultEvent:

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

String id

Unique identifier for this event.

String toolUseId

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.



class BetaManagedAgentsSessionThreadStatusRescheduledEvent:

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

String id

Unique identifier for this event.

String agentName

Name of the agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public sthr\_ ID of the thread that is retrying.

Type type



class BetaManagedAgentsSessionUpdatedEvent:

Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



Optional<[BetaManagedAgentsSessionAgent](api/beta.md)> agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

String id

Optional<String> description



List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> mcpServers

String name

Type type

String url



[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.



BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")



Optional<[BetaManagedAgentsSessionMultiagentCoordinator](api/beta.md)> multiagent

Resolved coordinator topology with full agent definitions for each roster member.



List<[BetaManagedAgentsSessionThreadAgent](api/beta.md)> agents

Full `agent` definitions the coordinator may spawn as session threads.

String id

Optional<String> description



List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> mcpServers

String name

Type type

String url



[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.



BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")

String name



List<Skill> skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system



List<Tool> tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled



Name name

Built-in agent tool identifier.

One of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type



class BetaManagedAgentsMcpToolset:



List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description



[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required

String name

Type type

Type type

long version

Type type

String name



List<Skill> skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system



List<Tool> tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled



Name name

Built-in agent tool identifier.

One of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type



class BetaManagedAgentsMcpToolset:



List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description



[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required

String name

Type type

Type type

long version

Optional<Metadata> metadata

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

Optional<String> title

The session's new title. Present only when the update changed it.



class BetaManagedAgentsSystemMessageEvent:

A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

String id

Unique identifier for this event.



List<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks. Text-only.

String text

The text content.

Type type

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsStreamSessionThreadEvents: A class that can be one of several variants.union 

Server-sent event in a single thread's stream.



class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

String id

Unique identifier for this event.



List<Content> content

Array of content blocks comprising the user message.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

String id

Unique identifier for this event.

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

String id

Unique identifier for this event.



Result result

UserToolConfirmationResult enum

One of the following:

ALLOW("allow")

DENY("deny")

String toolUseId

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

Optional<String> denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.



class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

String id

Unique identifier for this event.

String customToolUseId

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.



class BetaManagedAgentsAgentCustomToolUseEvent:

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String name

Name of the custom tool being called.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

Optional<String> sessionThreadId

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.



class BetaManagedAgentsAgentMessageEvent:

An agent response event in the session conversation.

String id

Unique identifier for this event.



List<[BetaManagedAgentsTextBlock](api/beta.md)> content

Array of text blocks comprising the agent response.

String text

The text content.

Type type

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsAgentThinkingEvent:

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsAgentMcpToolUseEvent:

Event emitted when the agent invokes a tool provided by an MCP server.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String mcpServerName

Name of the MCP server providing the tool.

String name

Name of the MCP tool being used.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



Optional<EvaluatedPermission> evaluatedPermission

AgentEvaluatedPermission enum

One of the following:

ALLOW("allow")

ASK("ask")

DENY("deny")

Optional<String> sessionThreadId

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



class BetaManagedAgentsAgentMcpToolResultEvent:

Event representing the result of an MCP tool execution.

String id

Unique identifier for this event.

String mcpToolUseId

The id of the `agent.mcp_tool_use` event this result corresponds to.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.



class BetaManagedAgentsAgentToolUseEvent:

Event emitted when the agent invokes a built-in agent tool.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String name

Name of the agent tool being used.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



Optional<EvaluatedPermission> evaluatedPermission

AgentEvaluatedPermission enum

One of the following:

ALLOW("allow")

ASK("ask")

DENY("deny")

Optional<String> sessionThreadId

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



class BetaManagedAgentsAgentToolResultEvent:

Event representing the result of an agent tool execution.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String toolUseId

The id of the `agent.tool_use` event this result corresponds to.

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.



class BetaManagedAgentsAgentThreadMessageReceivedEvent:

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

String id

Unique identifier for this event.



List<Content> content

Message content blocks.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

String fromSessionThreadId

Public `sthr_` ID of the thread that sent the message.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

Optional<String> fromAgentName

Name of the callable agent this message came from. Absent when received from the primary agent.



class BetaManagedAgentsAgentThreadMessageSentEvent:

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

String id

Unique identifier for this event.



List<Content> content

Message content blocks.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String toSessionThreadId

Public `sthr_` ID of the thread the message was sent to.

Type type

Optional<String> toAgentName

Name of the callable agent this message was sent to. Absent when sent to the primary agent.



class BetaManagedAgentsAgentThreadContextCompactedEvent:

Indicates that context compaction (summarization) occurred during the session.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionErrorEvent:

An error event indicating a problem occurred during session execution.

String id

Unique identifier for this event.



Error error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

One of the following:



class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

String mcpServerName

Name of the MCP server that failed to connect.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

String mcpServerName

Name of the MCP server that failed authentication.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsCredentialHostUnreachableError:

An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

String credentialId

ID of the affected credential.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

String vaultId

ID of the vault containing the affected credential.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionStatusRescheduledEvent:

Indicates the session is recovering from an error state and is rescheduled for execution.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionStatusRunningEvent:

Indicates the session is actively running and the agent is working.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionStatusIdleEvent:

Indicates the agent has paused and is awaiting user input.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format



StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

One of the following:



class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

Type type



class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

List<String> eventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type type



class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type type

Type type



class BetaManagedAgentsSessionStatusTerminatedEvent:

Indicates the session has terminated, either due to an error or completion.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionThreadCreatedEvent:

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

String id

Unique identifier for this event.

String agentName

Name of the callable agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public `sthr_` ID of the newly created thread.

Type type



class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:

Emitted when an outcome evaluation cycle begins.

String id

Unique identifier for this event.

long iteration

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

String outcomeId

The `outc_` ID of the outcome being evaluated.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

String id

Unique identifier for this event.

String explanation

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

long iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

String outcomeEvaluationStartId

The id of the corresponding `span.outcome_evaluation_start` event.

String outcomeId

The `outc_` ID of the outcome being evaluated.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String result

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

Type type



[BetaManagedAgentsSpanModelUsage](api/beta.md) usage

Token usage for a single model request.

long cacheCreationInputTokens

Tokens used to create prompt cache in this request.

long cacheReadInputTokens

Tokens read from prompt cache in this request.

long inputTokens

Input tokens consumed by this request.

long outputTokens

Output tokens generated by this request.



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")



class BetaManagedAgentsSpanModelRequestStartEvent:

Emitted when a model request is initiated by the agent.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSpanModelRequestEndEvent:

Emitted when a model request completes.

String id

Unique identifier for this event.

Optional<Boolean> isError

Whether the model request resulted in an error.

String modelRequestStartId

The id of the corresponding `span.model_request_start` event.



[BetaManagedAgentsSpanModelUsage](api/beta.md) modelUsage

Token usage for a single model request.

long cacheCreationInputTokens

Tokens used to create prompt cache in this request.

long cacheReadInputTokens

Tokens read from prompt cache in this request.

long inputTokens

Input tokens consumed by this request.

long outputTokens

Output tokens generated by this request.



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

String id

Unique identifier for this event.

long iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

String outcomeId

The `outc_` ID of the outcome being evaluated.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsUserDefineOutcomeEvent:

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

String id

Unique identifier for this event.

String description

What the agent should produce. Copied from the input event.

Optional<Long> maxIterations

Evaluate-then-revise cycles before giving up. Default 3, max 20.

String outcomeId

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

LocalDateTime processedAt

A timestamp in RFC 3339 format



Rubric rubric

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubric:

Rubric referenced by a file uploaded via the Files API.

String fileId

ID of the rubric file.

Type type



class BetaManagedAgentsTextRubric:

Rubric content provided inline as text.

String content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

Type type

Type type



class BetaManagedAgentsSessionDeletedEvent:

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionThreadStatusRunningEvent:

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

String id

Unique identifier for this event.

String agentName

Name of the agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public sthr\_ ID of the thread that started running.

Type type



class BetaManagedAgentsSessionThreadStatusIdleEvent:

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

String id

Unique identifier for this event.

String agentName

Name of the agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public sthr\_ ID of the thread that went idle.



StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

One of the following:



class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

Type type



class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

List<String> eventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type type



class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type type

Type type



class BetaManagedAgentsSessionThreadStatusTerminatedEvent:

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

String id

Unique identifier for this event.

String agentName

Name of the agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public sthr\_ ID of the thread that terminated.

Type type



class BetaManagedAgentsUserToolResultEvent:

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

String id

Unique identifier for this event.

String toolUseId

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.



class BetaManagedAgentsSessionThreadStatusRescheduledEvent:

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

String id

Unique identifier for this event.

String agentName

Name of the agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public sthr\_ ID of the thread that is retrying.

Type type



class BetaManagedAgentsSessionUpdatedEvent:

Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



Optional<[BetaManagedAgentsSessionAgent](api/beta.md)> agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

String id

Optional<String> description



List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> mcpServers

String name

Type type

String url



[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.



BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")



Optional<[BetaManagedAgentsSessionMultiagentCoordinator](api/beta.md)> multiagent

Resolved coordinator topology with full agent definitions for each roster member.



List<[BetaManagedAgentsSessionThreadAgent](api/beta.md)> agents

Full `agent` definitions the coordinator may spawn as session threads.

String id

Optional<String> description



List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> mcpServers

String name

Type type

String url



[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.



BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")

String name



List<Skill> skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system



List<Tool> tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled



Name name

Built-in agent tool identifier.

One of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type



class BetaManagedAgentsMcpToolset:



List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description



[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required

String name

Type type

Type type

long version

Type type

String name



List<Skill> skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system



List<Tool> tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled



Name name

Built-in agent tool identifier.

One of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type



class BetaManagedAgentsMcpToolset:



List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description



[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required

String name

Type type

Type type

long version

Optional<Metadata> metadata

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

Optional<String> title

The session's new title. Present only when the update changed it.



class BetaManagedAgentsSystemMessageEvent:

A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

String id

Unique identifier for this event.



List<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks. Text-only.

String text

The text content.

Type type

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Stream Session Thread Events

Java

```shiki
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.http.StreamResponse;
import com.anthropic.models.beta.sessions.threads.BetaManagedAgentsStreamSessionThreadEvents;
import com.anthropic.models.beta.sessions.threads.events.EventStreamParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        EventStreamParams params = EventStreamParams.builder()
            .sessionId("sesn_011CZkZAtmR3yMPDzynEDxu7")
            .threadId("sthr_011CZkZVWa6oIjw0rgXZpnBt")
            .build();
        StreamResponse<BetaManagedAgentsStreamSessionThreadEvents> betaManagedAgentsStreamSessionThreadEvents = client.beta().sessions().threads().events().streamStreaming(params);
    }
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
