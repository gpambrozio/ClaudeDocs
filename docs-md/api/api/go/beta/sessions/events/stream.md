# Stream Events

Copy page

Go

# Stream Events

client.Beta.Sessions.Events.Stream(ctx, sessionID, query) (\*[BetaManagedAgentsStreamSessionEventsUnion](api/beta.md), error)

GET/v1/sessions/{session\_id}/events/stream

Stream Events

##### ParametersExpand Collapse

sessionID string

query BetaSessionEventStreamParams

Betas param.Field[[]AnthropicBeta]optional

Optional header to specify the beta version(s) you want to use.

string

type AnthropicBeta string

Accepts one of the following:

const AnthropicBetaMessageBatches2024\_09\_24 AnthropicBeta = "message-batches-2024-09-24"

const AnthropicBetaPromptCaching2024\_07\_31 AnthropicBeta = "prompt-caching-2024-07-31"

const AnthropicBetaComputerUse2024\_10\_22 AnthropicBeta = "computer-use-2024-10-22"

const AnthropicBetaComputerUse2025\_01\_24 AnthropicBeta = "computer-use-2025-01-24"

const AnthropicBetaPDFs2024\_09\_25 AnthropicBeta = "pdfs-2024-09-25"

const AnthropicBetaTokenCounting2024\_11\_01 AnthropicBeta = "token-counting-2024-11-01"

const AnthropicBetaTokenEfficientTools2025\_02\_19 AnthropicBeta = "token-efficient-tools-2025-02-19"

const AnthropicBetaOutput128k2025\_02\_19 AnthropicBeta = "output-128k-2025-02-19"

const AnthropicBetaFilesAPI2025\_04\_14 AnthropicBeta = "files-api-2025-04-14"

const AnthropicBetaMCPClient2025\_04\_04 AnthropicBeta = "mcp-client-2025-04-04"

const AnthropicBetaMCPClient2025\_11\_20 AnthropicBeta = "mcp-client-2025-11-20"

const AnthropicBetaDevFullThinking2025\_05\_14 AnthropicBeta = "dev-full-thinking-2025-05-14"

const AnthropicBetaInterleavedThinking2025\_05\_14 AnthropicBeta = "interleaved-thinking-2025-05-14"

const AnthropicBetaCodeExecution2025\_05\_22 AnthropicBeta = "code-execution-2025-05-22"

const AnthropicBetaExtendedCacheTTL2025\_04\_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"

const AnthropicBetaContext1m2025\_08\_07 AnthropicBeta = "context-1m-2025-08-07"

const AnthropicBetaContextManagement2025\_06\_27 AnthropicBeta = "context-management-2025-06-27"

const AnthropicBetaModelContextWindowExceeded2025\_08\_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"

const AnthropicBetaSkills2025\_10\_02 AnthropicBeta = "skills-2025-10-02"

const AnthropicBetaFastMode2026\_02\_01 AnthropicBeta = "fast-mode-2026-02-01"

const AnthropicBetaOutput300k2026\_03\_24 AnthropicBeta = "output-300k-2026-03-24"

const AnthropicBetaUserProfiles2026\_03\_24 AnthropicBeta = "user-profiles-2026-03-24"

const AnthropicBetaAdvisorTool2026\_03\_01 AnthropicBeta = "advisor-tool-2026-03-01"

const AnthropicBetaManagedAgents2026\_04\_01 AnthropicBeta = "managed-agents-2026-04-01"

##### ReturnsExpand Collapse

type BetaManagedAgentsStreamSessionEventsUnion interface{…}

Server-sent event in the session stream.

Accepts one of the following:

type BetaManagedAgentsUserMessageEvent struct{…}

A user message event in the session conversation.

ID string

Unique identifier for this event.

Content []BetaManagedAgentsUserMessageEventContentUnion

Array of content blocks comprising the user message.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

Type BetaManagedAgentsUserMessageEventType

ProcessedAt Timeoptional

A timestamp in RFC 3339 format

type BetaManagedAgentsUserInterruptEvent struct{…}

An interrupt event that pauses agent execution and returns control to the user.

ID string

Unique identifier for this event.

Type BetaManagedAgentsUserInterruptEventType

ProcessedAt Timeoptional

A timestamp in RFC 3339 format

SessionThreadID stringoptional

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

type BetaManagedAgentsUserToolConfirmationEvent struct{…}

A tool confirmation event that approves or denies a pending tool execution.

ID string

Unique identifier for this event.

Result BetaManagedAgentsUserToolConfirmationEventResult

UserToolConfirmationResult enum

Accepts one of the following:

const BetaManagedAgentsUserToolConfirmationEventResultAllow BetaManagedAgentsUserToolConfirmationEventResult = "allow"

const BetaManagedAgentsUserToolConfirmationEventResultDeny BetaManagedAgentsUserToolConfirmationEventResult = "deny"

ToolUseID string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserToolConfirmationEventType

DenyMessage stringoptional

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

ProcessedAt Timeoptional

A timestamp in RFC 3339 format

SessionThreadID stringoptional

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

type BetaManagedAgentsUserCustomToolResultEvent struct{…}

Event sent by the client providing the result of a custom tool execution.

ID string

Unique identifier for this event.

CustomToolUseID string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserCustomToolResultEventType

Content []BetaManagedAgentsUserCustomToolResultEventContentUnionoptional

The result content returned by the tool.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

IsError booloptional

Whether the tool execution resulted in an error.

ProcessedAt Timeoptional

A timestamp in RFC 3339 format

SessionThreadID stringoptional

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

type BetaManagedAgentsAgentCustomToolUseEvent struct{…}

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

ID string

Unique identifier for this event.

Input map[string, any]

Input parameters for the tool call.

Name string

Name of the custom tool being called.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentCustomToolUseEventType

SessionThreadID stringoptional

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

type BetaManagedAgentsAgentMessageEvent struct{…}

An agent response event in the session conversation.

ID string

Unique identifier for this event.

Content [][BetaManagedAgentsTextBlock](api/beta.md)

Array of text blocks comprising the agent response.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentMessageEventType

type BetaManagedAgentsAgentThinkingEvent struct{…}

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentThinkingEventType

type BetaManagedAgentsAgentMCPToolUseEvent struct{…}

Event emitted when the agent invokes a tool provided by an MCP server.

ID string

Unique identifier for this event.

Input map[string, any]

Input parameters for the tool call.

MCPServerName string

Name of the MCP server providing the tool.

Name string

Name of the MCP tool being used.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentMCPToolUseEventType

EvaluatedPermission BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionoptional

AgentEvaluatedPermission enum

Accepts one of the following:

const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "allow"

const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "ask"

const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "deny"

SessionThreadID stringoptional

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

type BetaManagedAgentsAgentMCPToolResultEvent struct{…}

Event representing the result of an MCP tool execution.

ID string

Unique identifier for this event.

MCPToolUseID string

The id of the `agent.mcp_tool_use` event this result corresponds to.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentMCPToolResultEventType

Content []BetaManagedAgentsAgentMCPToolResultEventContentUnionoptional

The result content returned by the tool.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

IsError booloptional

Whether the tool execution resulted in an error.

type BetaManagedAgentsAgentToolUseEvent struct{…}

Event emitted when the agent invokes a built-in agent tool.

ID string

Unique identifier for this event.

Input map[string, any]

Input parameters for the tool call.

Name string

Name of the agent tool being used.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentToolUseEventType

EvaluatedPermission BetaManagedAgentsAgentToolUseEventEvaluatedPermissionoptional

AgentEvaluatedPermission enum

Accepts one of the following:

const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "allow"

const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "ask"

const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "deny"

SessionThreadID stringoptional

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

type BetaManagedAgentsAgentToolResultEvent struct{…}

Event representing the result of an agent tool execution.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

ToolUseID string

The id of the `agent.tool_use` event this result corresponds to.

Type BetaManagedAgentsAgentToolResultEventType

Content []BetaManagedAgentsAgentToolResultEventContentUnionoptional

The result content returned by the tool.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

IsError booloptional

Whether the tool execution resulted in an error.

type BetaManagedAgentsAgentThreadMessageReceivedEvent struct{…}

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

ID string

Unique identifier for this event.

Content []BetaManagedAgentsAgentThreadMessageReceivedEventContentUnion

Message content blocks.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

FromSessionThreadID string

Public `sthr_` ID of the thread that sent the message.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentThreadMessageReceivedEventType

FromAgentName stringoptional

Name of the callable agent this message came from. Absent when received from the primary agent.

type BetaManagedAgentsAgentThreadMessageSentEvent struct{…}

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

ID string

Unique identifier for this event.

Content []BetaManagedAgentsAgentThreadMessageSentEventContentUnion

Message content blocks.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

ProcessedAt Time

A timestamp in RFC 3339 format

ToSessionThreadID string

Public `sthr_` ID of the thread the message was sent to.

Type BetaManagedAgentsAgentThreadMessageSentEventType

ToAgentName stringoptional

Name of the callable agent this message was sent to. Absent when sent to the primary agent.

type BetaManagedAgentsAgentThreadContextCompactedEvent struct{…}

Indicates that context compaction (summarization) occurred during the session.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentThreadContextCompactedEventType

type BetaManagedAgentsSessionErrorEvent struct{…}

An error event indicating a problem occurred during session execution.

ID string

Unique identifier for this event.

Error BetaManagedAgentsSessionErrorEventErrorUnion

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

type BetaManagedAgentsUnknownError struct{…}

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsUnknownErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsUnknownErrorType

type BetaManagedAgentsModelOverloadedError struct{…}

The model is currently overloaded. Emitted after automatic retries are exhausted.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsModelOverloadedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsModelOverloadedErrorType

type BetaManagedAgentsModelRateLimitedError struct{…}

The model request was rate-limited.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsModelRateLimitedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsModelRateLimitedErrorType

type BetaManagedAgentsModelRequestFailedError struct{…}

A model request failed for a reason other than overload or rate-limiting.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsModelRequestFailedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsModelRequestFailedErrorType

type BetaManagedAgentsMCPConnectionFailedError struct{…}

Failed to connect to an MCP server.

MCPServerName string

Name of the MCP server that failed to connect.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsMCPConnectionFailedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsMCPConnectionFailedErrorType

type BetaManagedAgentsMCPAuthenticationFailedError struct{…}

Authentication to an MCP server failed.

MCPServerName string

Name of the MCP server that failed authentication.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsMCPAuthenticationFailedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsMCPAuthenticationFailedErrorType

type BetaManagedAgentsBillingError struct{…}

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsBillingErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsBillingErrorType

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionErrorEventType

type BetaManagedAgentsSessionStatusRescheduledEvent struct{…}

Indicates the session is recovering from an error state and is rescheduled for execution.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionStatusRescheduledEventType

type BetaManagedAgentsSessionStatusRunningEvent struct{…}

Indicates the session is actively running and the agent is working.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionStatusRunningEventType

type BetaManagedAgentsSessionStatusIdleEvent struct{…}

Indicates the agent has paused and is awaiting user input.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

StopReason BetaManagedAgentsSessionStatusIdleEventStopReasonUnion

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

type BetaManagedAgentsSessionEndTurn struct{…}

The agent completed its turn naturally and is ready for the next user message.

Type BetaManagedAgentsSessionEndTurnType

type BetaManagedAgentsSessionRequiresAction struct{…}

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

EventIDs []string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type BetaManagedAgentsSessionRequiresActionType

type BetaManagedAgentsSessionRetriesExhausted struct{…}

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type BetaManagedAgentsSessionRetriesExhaustedType

Type BetaManagedAgentsSessionStatusIdleEventType

type BetaManagedAgentsSessionStatusTerminatedEvent struct{…}

Indicates the session has terminated, either due to an error or completion.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionStatusTerminatedEventType

type BetaManagedAgentsSessionThreadCreatedEvent struct{…}

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

ID string

Unique identifier for this event.

AgentName string

Name of the callable agent the thread runs.

ProcessedAt Time

A timestamp in RFC 3339 format

SessionThreadID string

Public `sthr_` ID of the newly created thread.

Type BetaManagedAgentsSessionThreadCreatedEventType

type BetaManagedAgentsSpanOutcomeEvaluationStartEvent struct{…}

Emitted when an outcome evaluation cycle begins.

ID string

Unique identifier for this event.

Iteration int64

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

OutcomeID string

The `outc_` ID of the outcome being evaluated.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSpanOutcomeEvaluationStartEventType

type BetaManagedAgentsSpanOutcomeEvaluationEndEvent struct{…}

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

ID string

Unique identifier for this event.

Explanation string

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

Iteration int64

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

OutcomeEvaluationStartID string

The id of the corresponding `span.outcome_evaluation_start` event.

OutcomeID string

The `outc_` ID of the outcome being evaluated.

ProcessedAt Time

A timestamp in RFC 3339 format

Result string

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

Type BetaManagedAgentsSpanOutcomeEvaluationEndEventType

Usage [BetaManagedAgentsSpanModelUsage](api/beta.md)

Token usage for a single model request.

CacheCreationInputTokens int64

Tokens used to create prompt cache in this request.

CacheReadInputTokens int64

Tokens read from prompt cache in this request.

InputTokens int64

Input tokens consumed by this request.

OutputTokens int64

Output tokens generated by this request.

Speed BetaManagedAgentsSpanModelUsageSpeedoptional

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

const BetaManagedAgentsSpanModelUsageSpeedStandard BetaManagedAgentsSpanModelUsageSpeed = "standard"

const BetaManagedAgentsSpanModelUsageSpeedFast BetaManagedAgentsSpanModelUsageSpeed = "fast"

type BetaManagedAgentsSpanModelRequestStartEvent struct{…}

Emitted when a model request is initiated by the agent.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSpanModelRequestStartEventType

type BetaManagedAgentsSpanModelRequestEndEvent struct{…}

Emitted when a model request completes.

ID string

Unique identifier for this event.

IsError bool

Whether the model request resulted in an error.

ModelRequestStartID string

The id of the corresponding `span.model_request_start` event.

ModelUsage [BetaManagedAgentsSpanModelUsage](api/beta.md)

Token usage for a single model request.

CacheCreationInputTokens int64

Tokens used to create prompt cache in this request.

CacheReadInputTokens int64

Tokens read from prompt cache in this request.

InputTokens int64

Input tokens consumed by this request.

OutputTokens int64

Output tokens generated by this request.

Speed BetaManagedAgentsSpanModelUsageSpeedoptional

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

const BetaManagedAgentsSpanModelUsageSpeedStandard BetaManagedAgentsSpanModelUsageSpeed = "standard"

const BetaManagedAgentsSpanModelUsageSpeedFast BetaManagedAgentsSpanModelUsageSpeed = "fast"

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSpanModelRequestEndEventType

type BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent struct{…}

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

ID string

Unique identifier for this event.

Iteration int64

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

OutcomeID string

The `outc_` ID of the outcome being evaluated.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSpanOutcomeEvaluationOngoingEventType

type BetaManagedAgentsUserDefineOutcomeEvent struct{…}

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

ID string

Unique identifier for this event.

Description string

What the agent should produce. Copied from the input event.

MaxIterations int64

Evaluate-then-revise cycles before giving up. Default 3, max 20.

OutcomeID string

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

ProcessedAt Time

A timestamp in RFC 3339 format

Rubric BetaManagedAgentsUserDefineOutcomeEventRubricUnion

Rubric for grading the quality of an outcome.

Accepts one of the following:

type BetaManagedAgentsFileRubric struct{…}

Rubric referenced by a file uploaded via the Files API.

FileID string

ID of the rubric file.

Type BetaManagedAgentsFileRubricType

type BetaManagedAgentsTextRubric struct{…}

Rubric content provided inline as text.

Content string

Rubric content. Plain text or markdown — the grader treats it as freeform text.

Type BetaManagedAgentsTextRubricType

Type BetaManagedAgentsUserDefineOutcomeEventType

type BetaManagedAgentsSessionDeletedEvent struct{…}

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionDeletedEventType

type BetaManagedAgentsSessionThreadStatusRunningEvent struct{…}

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

ID string

Unique identifier for this event.

AgentName string

Name of the agent the thread runs.

ProcessedAt Time

A timestamp in RFC 3339 format

SessionThreadID string

Public sthr\_ ID of the thread that started running.

Type BetaManagedAgentsSessionThreadStatusRunningEventType

type BetaManagedAgentsSessionThreadStatusIdleEvent struct{…}

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

ID string

Unique identifier for this event.

AgentName string

Name of the agent the thread runs.

ProcessedAt Time

A timestamp in RFC 3339 format

SessionThreadID string

Public sthr\_ ID of the thread that went idle.

StopReason BetaManagedAgentsSessionThreadStatusIdleEventStopReasonUnion

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

type BetaManagedAgentsSessionEndTurn struct{…}

The agent completed its turn naturally and is ready for the next user message.

Type BetaManagedAgentsSessionEndTurnType

type BetaManagedAgentsSessionRequiresAction struct{…}

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

EventIDs []string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type BetaManagedAgentsSessionRequiresActionType

type BetaManagedAgentsSessionRetriesExhausted struct{…}

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type BetaManagedAgentsSessionRetriesExhaustedType

Type BetaManagedAgentsSessionThreadStatusIdleEventType

type BetaManagedAgentsSessionThreadStatusTerminatedEvent struct{…}

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

ID string

Unique identifier for this event.

AgentName string

Name of the agent the thread runs.

ProcessedAt Time

A timestamp in RFC 3339 format

SessionThreadID string

Public sthr\_ ID of the thread that terminated.

Type BetaManagedAgentsSessionThreadStatusTerminatedEventType

type BetaManagedAgentsSessionThreadStatusRescheduledEvent struct{…}

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

ID string

Unique identifier for this event.

AgentName string

Name of the agent the thread runs.

ProcessedAt Time

A timestamp in RFC 3339 format

SessionThreadID string

Public sthr\_ ID of the thread that is retrying.

Type BetaManagedAgentsSessionThreadStatusRescheduledEventType

type BetaManagedAgentsStreamSessionEventsUnion interface{…}

Server-sent event in the session stream.

Accepts one of the following:

type BetaManagedAgentsUserMessageEvent struct{…}

A user message event in the session conversation.

ID string

Unique identifier for this event.

Content []BetaManagedAgentsUserMessageEventContentUnion

Array of content blocks comprising the user message.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

Type BetaManagedAgentsUserMessageEventType

ProcessedAt Timeoptional

A timestamp in RFC 3339 format

type BetaManagedAgentsUserInterruptEvent struct{…}

An interrupt event that pauses agent execution and returns control to the user.

ID string

Unique identifier for this event.

Type BetaManagedAgentsUserInterruptEventType

ProcessedAt Timeoptional

A timestamp in RFC 3339 format

SessionThreadID stringoptional

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

type BetaManagedAgentsUserToolConfirmationEvent struct{…}

A tool confirmation event that approves or denies a pending tool execution.

ID string

Unique identifier for this event.

Result BetaManagedAgentsUserToolConfirmationEventResult

UserToolConfirmationResult enum

Accepts one of the following:

const BetaManagedAgentsUserToolConfirmationEventResultAllow BetaManagedAgentsUserToolConfirmationEventResult = "allow"

const BetaManagedAgentsUserToolConfirmationEventResultDeny BetaManagedAgentsUserToolConfirmationEventResult = "deny"

ToolUseID string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserToolConfirmationEventType

DenyMessage stringoptional

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

ProcessedAt Timeoptional

A timestamp in RFC 3339 format

SessionThreadID stringoptional

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

type BetaManagedAgentsUserCustomToolResultEvent struct{…}

Event sent by the client providing the result of a custom tool execution.

ID string

Unique identifier for this event.

CustomToolUseID string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserCustomToolResultEventType

Content []BetaManagedAgentsUserCustomToolResultEventContentUnionoptional

The result content returned by the tool.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

IsError booloptional

Whether the tool execution resulted in an error.

ProcessedAt Timeoptional

A timestamp in RFC 3339 format

SessionThreadID stringoptional

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

type BetaManagedAgentsAgentCustomToolUseEvent struct{…}

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

ID string

Unique identifier for this event.

Input map[string, any]

Input parameters for the tool call.

Name string

Name of the custom tool being called.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentCustomToolUseEventType

SessionThreadID stringoptional

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

type BetaManagedAgentsAgentMessageEvent struct{…}

An agent response event in the session conversation.

ID string

Unique identifier for this event.

Content [][BetaManagedAgentsTextBlock](api/beta.md)

Array of text blocks comprising the agent response.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentMessageEventType

type BetaManagedAgentsAgentThinkingEvent struct{…}

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentThinkingEventType

type BetaManagedAgentsAgentMCPToolUseEvent struct{…}

Event emitted when the agent invokes a tool provided by an MCP server.

ID string

Unique identifier for this event.

Input map[string, any]

Input parameters for the tool call.

MCPServerName string

Name of the MCP server providing the tool.

Name string

Name of the MCP tool being used.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentMCPToolUseEventType

EvaluatedPermission BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionoptional

AgentEvaluatedPermission enum

Accepts one of the following:

const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "allow"

const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "ask"

const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "deny"

SessionThreadID stringoptional

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

type BetaManagedAgentsAgentMCPToolResultEvent struct{…}

Event representing the result of an MCP tool execution.

ID string

Unique identifier for this event.

MCPToolUseID string

The id of the `agent.mcp_tool_use` event this result corresponds to.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentMCPToolResultEventType

Content []BetaManagedAgentsAgentMCPToolResultEventContentUnionoptional

The result content returned by the tool.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

IsError booloptional

Whether the tool execution resulted in an error.

type BetaManagedAgentsAgentToolUseEvent struct{…}

Event emitted when the agent invokes a built-in agent tool.

ID string

Unique identifier for this event.

Input map[string, any]

Input parameters for the tool call.

Name string

Name of the agent tool being used.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentToolUseEventType

EvaluatedPermission BetaManagedAgentsAgentToolUseEventEvaluatedPermissionoptional

AgentEvaluatedPermission enum

Accepts one of the following:

const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "allow"

const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "ask"

const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "deny"

SessionThreadID stringoptional

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

type BetaManagedAgentsAgentToolResultEvent struct{…}

Event representing the result of an agent tool execution.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

ToolUseID string

The id of the `agent.tool_use` event this result corresponds to.

Type BetaManagedAgentsAgentToolResultEventType

Content []BetaManagedAgentsAgentToolResultEventContentUnionoptional

The result content returned by the tool.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

IsError booloptional

Whether the tool execution resulted in an error.

type BetaManagedAgentsAgentThreadMessageReceivedEvent struct{…}

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

ID string

Unique identifier for this event.

Content []BetaManagedAgentsAgentThreadMessageReceivedEventContentUnion

Message content blocks.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

FromSessionThreadID string

Public `sthr_` ID of the thread that sent the message.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentThreadMessageReceivedEventType

FromAgentName stringoptional

Name of the callable agent this message came from. Absent when received from the primary agent.

type BetaManagedAgentsAgentThreadMessageSentEvent struct{…}

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

ID string

Unique identifier for this event.

Content []BetaManagedAgentsAgentThreadMessageSentEventContentUnion

Message content blocks.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

ProcessedAt Time

A timestamp in RFC 3339 format

ToSessionThreadID string

Public `sthr_` ID of the thread the message was sent to.

Type BetaManagedAgentsAgentThreadMessageSentEventType

ToAgentName stringoptional

Name of the callable agent this message was sent to. Absent when sent to the primary agent.

type BetaManagedAgentsAgentThreadContextCompactedEvent struct{…}

Indicates that context compaction (summarization) occurred during the session.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentThreadContextCompactedEventType

type BetaManagedAgentsSessionErrorEvent struct{…}

An error event indicating a problem occurred during session execution.

ID string

Unique identifier for this event.

Error BetaManagedAgentsSessionErrorEventErrorUnion

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

type BetaManagedAgentsUnknownError struct{…}

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsUnknownErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsUnknownErrorType

type BetaManagedAgentsModelOverloadedError struct{…}

The model is currently overloaded. Emitted after automatic retries are exhausted.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsModelOverloadedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsModelOverloadedErrorType

type BetaManagedAgentsModelRateLimitedError struct{…}

The model request was rate-limited.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsModelRateLimitedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsModelRateLimitedErrorType

type BetaManagedAgentsModelRequestFailedError struct{…}

A model request failed for a reason other than overload or rate-limiting.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsModelRequestFailedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsModelRequestFailedErrorType

type BetaManagedAgentsMCPConnectionFailedError struct{…}

Failed to connect to an MCP server.

MCPServerName string

Name of the MCP server that failed to connect.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsMCPConnectionFailedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsMCPConnectionFailedErrorType

type BetaManagedAgentsMCPAuthenticationFailedError struct{…}

Authentication to an MCP server failed.

MCPServerName string

Name of the MCP server that failed authentication.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsMCPAuthenticationFailedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsMCPAuthenticationFailedErrorType

type BetaManagedAgentsBillingError struct{…}

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsBillingErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsBillingErrorType

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionErrorEventType

type BetaManagedAgentsSessionStatusRescheduledEvent struct{…}

Indicates the session is recovering from an error state and is rescheduled for execution.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionStatusRescheduledEventType

type BetaManagedAgentsSessionStatusRunningEvent struct{…}

Indicates the session is actively running and the agent is working.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionStatusRunningEventType

type BetaManagedAgentsSessionStatusIdleEvent struct{…}

Indicates the agent has paused and is awaiting user input.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

StopReason BetaManagedAgentsSessionStatusIdleEventStopReasonUnion

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

type BetaManagedAgentsSessionEndTurn struct{…}

The agent completed its turn naturally and is ready for the next user message.

Type BetaManagedAgentsSessionEndTurnType

type BetaManagedAgentsSessionRequiresAction struct{…}

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

EventIDs []string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type BetaManagedAgentsSessionRequiresActionType

type BetaManagedAgentsSessionRetriesExhausted struct{…}

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type BetaManagedAgentsSessionRetriesExhaustedType

Type BetaManagedAgentsSessionStatusIdleEventType

type BetaManagedAgentsSessionStatusTerminatedEvent struct{…}

Indicates the session has terminated, either due to an error or completion.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionStatusTerminatedEventType

type BetaManagedAgentsSessionThreadCreatedEvent struct{…}

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

ID string

Unique identifier for this event.

AgentName string

Name of the callable agent the thread runs.

ProcessedAt Time

A timestamp in RFC 3339 format

SessionThreadID string

Public `sthr_` ID of the newly created thread.

Type BetaManagedAgentsSessionThreadCreatedEventType

type BetaManagedAgentsSpanOutcomeEvaluationStartEvent struct{…}

Emitted when an outcome evaluation cycle begins.

ID string

Unique identifier for this event.

Iteration int64

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

OutcomeID string

The `outc_` ID of the outcome being evaluated.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSpanOutcomeEvaluationStartEventType

type BetaManagedAgentsSpanOutcomeEvaluationEndEvent struct{…}

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

ID string

Unique identifier for this event.

Explanation string

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

Iteration int64

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

OutcomeEvaluationStartID string

The id of the corresponding `span.outcome_evaluation_start` event.

OutcomeID string

The `outc_` ID of the outcome being evaluated.

ProcessedAt Time

A timestamp in RFC 3339 format

Result string

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

Type BetaManagedAgentsSpanOutcomeEvaluationEndEventType

Usage [BetaManagedAgentsSpanModelUsage](api/beta.md)

Token usage for a single model request.

CacheCreationInputTokens int64

Tokens used to create prompt cache in this request.

CacheReadInputTokens int64

Tokens read from prompt cache in this request.

InputTokens int64

Input tokens consumed by this request.

OutputTokens int64

Output tokens generated by this request.

Speed BetaManagedAgentsSpanModelUsageSpeedoptional

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

const BetaManagedAgentsSpanModelUsageSpeedStandard BetaManagedAgentsSpanModelUsageSpeed = "standard"

const BetaManagedAgentsSpanModelUsageSpeedFast BetaManagedAgentsSpanModelUsageSpeed = "fast"

type BetaManagedAgentsSpanModelRequestStartEvent struct{…}

Emitted when a model request is initiated by the agent.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSpanModelRequestStartEventType

type BetaManagedAgentsSpanModelRequestEndEvent struct{…}

Emitted when a model request completes.

ID string

Unique identifier for this event.

IsError bool

Whether the model request resulted in an error.

ModelRequestStartID string

The id of the corresponding `span.model_request_start` event.

ModelUsage [BetaManagedAgentsSpanModelUsage](api/beta.md)

Token usage for a single model request.

CacheCreationInputTokens int64

Tokens used to create prompt cache in this request.

CacheReadInputTokens int64

Tokens read from prompt cache in this request.

InputTokens int64

Input tokens consumed by this request.

OutputTokens int64

Output tokens generated by this request.

Speed BetaManagedAgentsSpanModelUsageSpeedoptional

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

const BetaManagedAgentsSpanModelUsageSpeedStandard BetaManagedAgentsSpanModelUsageSpeed = "standard"

const BetaManagedAgentsSpanModelUsageSpeedFast BetaManagedAgentsSpanModelUsageSpeed = "fast"

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSpanModelRequestEndEventType

type BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent struct{…}

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

ID string

Unique identifier for this event.

Iteration int64

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

OutcomeID string

The `outc_` ID of the outcome being evaluated.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSpanOutcomeEvaluationOngoingEventType

type BetaManagedAgentsUserDefineOutcomeEvent struct{…}

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

ID string

Unique identifier for this event.

Description string

What the agent should produce. Copied from the input event.

MaxIterations int64

Evaluate-then-revise cycles before giving up. Default 3, max 20.

OutcomeID string

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

ProcessedAt Time

A timestamp in RFC 3339 format

Rubric BetaManagedAgentsUserDefineOutcomeEventRubricUnion

Rubric for grading the quality of an outcome.

Accepts one of the following:

type BetaManagedAgentsFileRubric struct{…}

Rubric referenced by a file uploaded via the Files API.

FileID string

ID of the rubric file.

Type BetaManagedAgentsFileRubricType

type BetaManagedAgentsTextRubric struct{…}

Rubric content provided inline as text.

Content string

Rubric content. Plain text or markdown — the grader treats it as freeform text.

Type BetaManagedAgentsTextRubricType

Type BetaManagedAgentsUserDefineOutcomeEventType

type BetaManagedAgentsSessionDeletedEvent struct{…}

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionDeletedEventType

type BetaManagedAgentsSessionThreadStatusRunningEvent struct{…}

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

ID string

Unique identifier for this event.

AgentName string

Name of the agent the thread runs.

ProcessedAt Time

A timestamp in RFC 3339 format

SessionThreadID string

Public sthr\_ ID of the thread that started running.

Type BetaManagedAgentsSessionThreadStatusRunningEventType

type BetaManagedAgentsSessionThreadStatusIdleEvent struct{…}

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

ID string

Unique identifier for this event.

AgentName string

Name of the agent the thread runs.

ProcessedAt Time

A timestamp in RFC 3339 format

SessionThreadID string

Public sthr\_ ID of the thread that went idle.

StopReason BetaManagedAgentsSessionThreadStatusIdleEventStopReasonUnion

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

type BetaManagedAgentsSessionEndTurn struct{…}

The agent completed its turn naturally and is ready for the next user message.

Type BetaManagedAgentsSessionEndTurnType

type BetaManagedAgentsSessionRequiresAction struct{…}

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

EventIDs []string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type BetaManagedAgentsSessionRequiresActionType

type BetaManagedAgentsSessionRetriesExhausted struct{…}

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type BetaManagedAgentsSessionRetriesExhaustedType

Type BetaManagedAgentsSessionThreadStatusIdleEventType

type BetaManagedAgentsSessionThreadStatusTerminatedEvent struct{…}

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

ID string

Unique identifier for this event.

AgentName string

Name of the agent the thread runs.

ProcessedAt Time

A timestamp in RFC 3339 format

SessionThreadID string

Public sthr\_ ID of the thread that terminated.

Type BetaManagedAgentsSessionThreadStatusTerminatedEventType

type BetaManagedAgentsSessionThreadStatusRescheduledEvent struct{…}

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

ID string

Unique identifier for this event.

AgentName string

Name of the agent the thread runs.

ProcessedAt Time

A timestamp in RFC 3339 format

SessionThreadID string

Public sthr\_ ID of the thread that is retrying.

Type BetaManagedAgentsSessionThreadStatusRescheduledEventType

Stream Events

Go

```shiki
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  stream := client.Beta.Sessions.Events.StreamEvents(
    context.TODO(),
    "sesn_011CZkZAtmR3yMPDzynEDxu7",
    anthropic.BetaSessionEventStreamParams{

    },
  )
  for stream.Next() {
  fmt.Printf("%+v\n", stream.Current())
  }
  err := stream.Err()
  if err != nil {
    panic(err.Error())
  }
}
```

Response 200

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
