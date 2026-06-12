# List Session Thread Events

Copy page

SDK language

Go

# List Session Thread Events

client.Beta.Sessions.Threads.Events.List(ctx, threadID, params) (\*PageCursor[[BetaManagedAgentsSessionEventUnion](api/beta.md)], error)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

List Session Thread Events

##### ParametersExpand Collapse

threadID string



params BetaSessionThreadEventListParams

SessionID param.Field[string]

Path param: Path parameter session\_id

Limit param.Field[int64]Optional

Query param: Query parameter for limit

Page param.Field[string]Optional

Query param: Query parameter for page



Betas param.Field[[]AnthropicBeta]Optional

Header param: Optional header to specify the beta version(s) you want to use.

string



type AnthropicBeta string

One of the following:

const AnthropicBetaMessageBatches2024\_09\_24 AnthropicBeta = "message-batches-2024-09-24"

const AnthropicBetaPromptCaching2024\_07\_31 AnthropicBeta = "prompt-caching-2024-07-31"

const AnthropicBetaComputerUse2024\_10\_22 AnthropicBeta = "computer-use-2024-10-22"

const AnthropicBetaComputerUse2025\_01\_24 AnthropicBeta = "computer-use-2025-01-24"

const AnthropicBetaPDFs2024\_09\_25 AnthropicBeta = "pdfs-2024-09-25"

const AnthropicBetaTokenCounting2024\_11\_01 AnthropicBeta = "token-counting-2024-11-01"

const AnthropicBetaTokenEfficientTools2025\_02\_19 AnthropicBeta = "token-efficient-tools-2025-02-19"

const AnthropicBetaOutput128k2025\_02\_19 AnthropicBeta = "output-128k-2025-02-19"

const AnthropicBetaFilesAPI2025\_04\_14 AnthropicBeta = "files-api-2025-04-14"

const AnthropicBetaMCPClient2025\_04\_04 AnthropicBeta = "mcp-client-2025-04-04"

const AnthropicBetaMCPClient2025\_11\_20 AnthropicBeta = "mcp-client-2025-11-20"

const AnthropicBetaDevFullThinking2025\_05\_14 AnthropicBeta = "dev-full-thinking-2025-05-14"

const AnthropicBetaInterleavedThinking2025\_05\_14 AnthropicBeta = "interleaved-thinking-2025-05-14"

const AnthropicBetaCodeExecution2025\_05\_22 AnthropicBeta = "code-execution-2025-05-22"

const AnthropicBetaExtendedCacheTTL2025\_04\_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"

const AnthropicBetaContext1m2025\_08\_07 AnthropicBeta = "context-1m-2025-08-07"

const AnthropicBetaContextManagement2025\_06\_27 AnthropicBeta = "context-management-2025-06-27"

const AnthropicBetaModelContextWindowExceeded2025\_08\_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"

const AnthropicBetaSkills2025\_10\_02 AnthropicBeta = "skills-2025-10-02"

const AnthropicBetaFastMode2026\_02\_01 AnthropicBeta = "fast-mode-2026-02-01"

const AnthropicBetaOutput300k2026\_03\_24 AnthropicBeta = "output-300k-2026-03-24"

const AnthropicBetaUserProfiles2026\_03\_24 AnthropicBeta = "user-profiles-2026-03-24"

const AnthropicBetaAdvisorTool2026\_03\_01 AnthropicBeta = "advisor-tool-2026-03-01"

const AnthropicBetaManagedAgents2026\_04\_01 AnthropicBeta = "managed-agents-2026-04-01"

const AnthropicBetaCacheDiagnosis2026\_04\_07 AnthropicBeta = "cache-diagnosis-2026-04-07"

const AnthropicBetaThinkingTokenCount2026\_05\_13 AnthropicBeta = "thinking-token-count-2026-05-13"

const AnthropicBetaServerSideFallback2026\_06\_01 AnthropicBeta = "server-side-fallback-2026-06-01"

const AnthropicBetaFallbackCredit2026\_06\_01 AnthropicBeta = "fallback-credit-2026-06-01"

##### ReturnsExpand Collapse



type BetaManagedAgentsSessionEventUnion interface{…}

Union type for all event types in a session.

One of the following:



type BetaManagedAgentsUserMessageEvent struct{…}

A user message event in the session conversation.

ID string

Unique identifier for this event.



Content []BetaManagedAgentsUserMessageEventContentUnion

Array of content blocks comprising the user message.

One of the following:



type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType



type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.



Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

One of the following:



type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType



type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.



type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType



type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

One of the following:



type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType



type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType



type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.



type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringOptional

Additional context about the document for the model.

Title stringOptional

The title of the document.

Type BetaManagedAgentsUserMessageEventType

ProcessedAt TimeOptional

A timestamp in RFC 3339 format



type BetaManagedAgentsUserInterruptEvent struct{…}

An interrupt event that pauses agent execution and returns control to the user.

ID string

Unique identifier for this event.

Type BetaManagedAgentsUserInterruptEventType

ProcessedAt TimeOptional

A timestamp in RFC 3339 format

SessionThreadID stringOptional

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



type BetaManagedAgentsUserToolConfirmationEvent struct{…}

A tool confirmation event that approves or denies a pending tool execution.

ID string

Unique identifier for this event.



Result BetaManagedAgentsUserToolConfirmationEventResult

UserToolConfirmationResult enum

One of the following:

const BetaManagedAgentsUserToolConfirmationEventResultAllow BetaManagedAgentsUserToolConfirmationEventResult = "allow"

const BetaManagedAgentsUserToolConfirmationEventResultDeny BetaManagedAgentsUserToolConfirmationEventResult = "deny"

ToolUseID string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserToolConfirmationEventType

DenyMessage stringOptional

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

ProcessedAt TimeOptional

A timestamp in RFC 3339 format

SessionThreadID stringOptional

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.



type BetaManagedAgentsUserCustomToolResultEvent struct{…}

Event sent by the client providing the result of a custom tool execution.

ID string

Unique identifier for this event.

CustomToolUseID string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserCustomToolResultEventType



Content []BetaManagedAgentsUserCustomToolResultEventContentUnionOptional

The result content returned by the tool.

One of the following:



type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType



type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.



Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

One of the following:



type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType



type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.



type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType



type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

One of the following:



type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType



type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType



type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.



type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringOptional

Additional context about the document for the model.

Title stringOptional

The title of the document.



type BetaManagedAgentsSearchResultBlock struct{…}

A block containing a web search result.



Citations [BetaManagedAgentsSearchResultCitations](api/beta.md)

Citation settings for a search result.

Enabled bool

Whether citations are enabled for this search result.



Content [][BetaManagedAgentsSearchResultContent](api/beta.md)

Array of text content blocks from the search result.

Text string

The text content.

Type BetaManagedAgentsSearchResultContentType

Source string

The URL source of the search result.

Title string

The title of the search result.

Type BetaManagedAgentsSearchResultBlockType

IsError boolOptional

Whether the tool execution resulted in an error.

ProcessedAt TimeOptional

A timestamp in RFC 3339 format

SessionThreadID stringOptional

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.



type BetaManagedAgentsAgentCustomToolUseEvent struct{…}

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

ID string

Unique identifier for this event.

Input map[string, any]

Input parameters for the tool call.

Name string

Name of the custom tool being called.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentCustomToolUseEventType

SessionThreadID stringOptional

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.



type BetaManagedAgentsAgentMessageEvent struct{…}

An agent response event in the session conversation.

ID string

Unique identifier for this event.



Content [][BetaManagedAgentsTextBlock](api/beta.md)

Array of text blocks comprising the agent response.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentMessageEventType



type BetaManagedAgentsAgentThinkingEvent struct{…}

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentThinkingEventType



type BetaManagedAgentsAgentMCPToolUseEvent struct{…}

Event emitted when the agent invokes a tool provided by an MCP server.

ID string

Unique identifier for this event.

Input map[string, any]

Input parameters for the tool call.

MCPServerName string

Name of the MCP server providing the tool.

Name string

Name of the MCP tool being used.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentMCPToolUseEventType



EvaluatedPermission BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionOptional

AgentEvaluatedPermission enum

One of the following:

const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "allow"

const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "ask"

const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "deny"

SessionThreadID stringOptional

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



type BetaManagedAgentsAgentMCPToolResultEvent struct{…}

Event representing the result of an MCP tool execution.

ID string

Unique identifier for this event.

MCPToolUseID string

The id of the `agent.mcp_tool_use` event this result corresponds to.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentMCPToolResultEventType



Content []BetaManagedAgentsAgentMCPToolResultEventContentUnionOptional

The result content returned by the tool.

One of the following:



type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType



type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.



Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

One of the following:



type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType



type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.



type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType



type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

One of the following:



type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType



type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType



type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.



type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringOptional

Additional context about the document for the model.

Title stringOptional

The title of the document.



type BetaManagedAgentsSearchResultBlock struct{…}

A block containing a web search result.



Citations [BetaManagedAgentsSearchResultCitations](api/beta.md)

Citation settings for a search result.

Enabled bool

Whether citations are enabled for this search result.



Content [][BetaManagedAgentsSearchResultContent](api/beta.md)

Array of text content blocks from the search result.

Text string

The text content.

Type BetaManagedAgentsSearchResultContentType

Source string

The URL source of the search result.

Title string

The title of the search result.

Type BetaManagedAgentsSearchResultBlockType

IsError boolOptional

Whether the tool execution resulted in an error.



type BetaManagedAgentsAgentToolUseEvent struct{…}

Event emitted when the agent invokes a built-in agent tool.

ID string

Unique identifier for this event.

Input map[string, any]

Input parameters for the tool call.

Name string

Name of the agent tool being used.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentToolUseEventType



EvaluatedPermission BetaManagedAgentsAgentToolUseEventEvaluatedPermissionOptional

AgentEvaluatedPermission enum

One of the following:

const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "allow"

const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "ask"

const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "deny"

SessionThreadID stringOptional

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



type BetaManagedAgentsAgentToolResultEvent struct{…}

Event representing the result of an agent tool execution.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

ToolUseID string

The id of the `agent.tool_use` event this result corresponds to.

Type BetaManagedAgentsAgentToolResultEventType



Content []BetaManagedAgentsAgentToolResultEventContentUnionOptional

The result content returned by the tool.

One of the following:



type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType



type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.



Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

One of the following:



type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType



type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.



type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType



type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

One of the following:



type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType



type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType



type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.



type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringOptional

Additional context about the document for the model.

Title stringOptional

The title of the document.



type BetaManagedAgentsSearchResultBlock struct{…}

A block containing a web search result.



Citations [BetaManagedAgentsSearchResultCitations](api/beta.md)

Citation settings for a search result.

Enabled bool

Whether citations are enabled for this search result.



Content [][BetaManagedAgentsSearchResultContent](api/beta.md)

Array of text content blocks from the search result.

Text string

The text content.

Type BetaManagedAgentsSearchResultContentType

Source string

The URL source of the search result.

Title string

The title of the search result.

Type BetaManagedAgentsSearchResultBlockType

IsError boolOptional

Whether the tool execution resulted in an error.



type BetaManagedAgentsAgentThreadMessageReceivedEvent struct{…}

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

ID string

Unique identifier for this event.



Content []BetaManagedAgentsAgentThreadMessageReceivedEventContentUnion

Message content blocks.

One of the following:



type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType



type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.



Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

One of the following:



type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType



type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.



type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType



type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

One of the following:



type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType



type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType



type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.



type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringOptional

Additional context about the document for the model.

Title stringOptional

The title of the document.

FromSessionThreadID string

Public `sthr_` ID of the thread that sent the message.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentThreadMessageReceivedEventType

FromAgentName stringOptional

Name of the callable agent this message came from. Absent when received from the primary agent.



type BetaManagedAgentsAgentThreadMessageSentEvent struct{…}

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

ID string

Unique identifier for this event.



Content []BetaManagedAgentsAgentThreadMessageSentEventContentUnion

Message content blocks.

One of the following:



type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType



type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.



Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

One of the following:



type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType



type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.



type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType



type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

One of the following:



type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType



type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType



type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.



type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringOptional

Additional context about the document for the model.

Title stringOptional

The title of the document.

ProcessedAt Time

A timestamp in RFC 3339 format

ToSessionThreadID string

Public `sthr_` ID of the thread the message was sent to.

Type BetaManagedAgentsAgentThreadMessageSentEventType

ToAgentName stringOptional

Name of the callable agent this message was sent to. Absent when sent to the primary agent.



type BetaManagedAgentsAgentThreadContextCompactedEvent struct{…}

Indicates that context compaction (summarization) occurred during the session.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentThreadContextCompactedEventType



type BetaManagedAgentsSessionErrorEvent struct{…}

An error event indicating a problem occurred during session execution.

ID string

Unique identifier for this event.



Error BetaManagedAgentsSessionErrorEventErrorUnion

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

One of the following:



type BetaManagedAgentsUnknownError struct{…}

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Message string

Human-readable error description.



RetryStatus BetaManagedAgentsUnknownErrorRetryStatusUnion

What the client should do next in response to this error.

One of the following:



type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType



type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType



type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsUnknownErrorType



type BetaManagedAgentsModelOverloadedError struct{…}

The model is currently overloaded. Emitted after automatic retries are exhausted.

Message string

Human-readable error description.



RetryStatus BetaManagedAgentsModelOverloadedErrorRetryStatusUnion

What the client should do next in response to this error.

One of the following:



type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType



type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType



type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsModelOverloadedErrorType



type BetaManagedAgentsModelRateLimitedError struct{…}

The model request was rate-limited.

Message string

Human-readable error description.



RetryStatus BetaManagedAgentsModelRateLimitedErrorRetryStatusUnion

What the client should do next in response to this error.

One of the following:



type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType



type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType



type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsModelRateLimitedErrorType



type BetaManagedAgentsModelRequestFailedError struct{…}

A model request failed for a reason other than overload or rate-limiting.

Message string

Human-readable error description.



RetryStatus BetaManagedAgentsModelRequestFailedErrorRetryStatusUnion

What the client should do next in response to this error.

One of the following:



type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType



type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType



type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsModelRequestFailedErrorType



type BetaManagedAgentsMCPConnectionFailedError struct{…}

Failed to connect to an MCP server.

MCPServerName string

Name of the MCP server that failed to connect.

Message string

Human-readable error description.



RetryStatus BetaManagedAgentsMCPConnectionFailedErrorRetryStatusUnion

What the client should do next in response to this error.

One of the following:



type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType



type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType



type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsMCPConnectionFailedErrorType



type BetaManagedAgentsMCPAuthenticationFailedError struct{…}

Authentication to an MCP server failed.

MCPServerName string

Name of the MCP server that failed authentication.

Message string

Human-readable error description.



RetryStatus BetaManagedAgentsMCPAuthenticationFailedErrorRetryStatusUnion

What the client should do next in response to this error.

One of the following:



type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType



type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType



type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsMCPAuthenticationFailedErrorType



type BetaManagedAgentsBillingError struct{…}

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

Message string

Human-readable error description.



RetryStatus BetaManagedAgentsBillingErrorRetryStatusUnion

What the client should do next in response to this error.

One of the following:



type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType



type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType



type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsBillingErrorType



type BetaManagedAgentsCredentialHostUnreachableError struct{…}

An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

CredentialID string

ID of the affected credential.

Message string

Human-readable error description.



RetryStatus BetaManagedAgentsCredentialHostUnreachableErrorRetryStatusUnion

What the client should do next in response to this error.

One of the following:



type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType



type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType



type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsCredentialHostUnreachableErrorType

VaultID string

ID of the vault containing the affected credential.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionErrorEventType



type BetaManagedAgentsSessionStatusRescheduledEvent struct{…}

Indicates the session is recovering from an error state and is rescheduled for execution.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionStatusRescheduledEventType



type BetaManagedAgentsSessionStatusRunningEvent struct{…}

Indicates the session is actively running and the agent is working.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionStatusRunningEventType



type BetaManagedAgentsSessionStatusIdleEvent struct{…}

Indicates the agent has paused and is awaiting user input.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format



StopReason BetaManagedAgentsSessionStatusIdleEventStopReasonUnion

The agent completed its turn naturally and is ready for the next user message.

One of the following:



type BetaManagedAgentsSessionEndTurn struct{…}

The agent completed its turn naturally and is ready for the next user message.

Type BetaManagedAgentsSessionEndTurnType



type BetaManagedAgentsSessionRequiresAction struct{…}

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

EventIDs []string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type BetaManagedAgentsSessionRequiresActionType



type BetaManagedAgentsSessionRetriesExhausted struct{…}

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type BetaManagedAgentsSessionRetriesExhaustedType

Type BetaManagedAgentsSessionStatusIdleEventType



type BetaManagedAgentsSessionStatusTerminatedEvent struct{…}

Indicates the session has terminated, either due to an error or completion.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionStatusTerminatedEventType



type BetaManagedAgentsSessionThreadCreatedEvent struct{…}

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

ID string

Unique identifier for this event.

AgentName string

Name of the callable agent the thread runs.

ProcessedAt Time

A timestamp in RFC 3339 format

SessionThreadID string

Public `sthr_` ID of the newly created thread.

Type BetaManagedAgentsSessionThreadCreatedEventType



type BetaManagedAgentsSpanOutcomeEvaluationStartEvent struct{…}

Emitted when an outcome evaluation cycle begins.

ID string

Unique identifier for this event.

Iteration int64

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

OutcomeID string

The `outc_` ID of the outcome being evaluated.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSpanOutcomeEvaluationStartEventType



type BetaManagedAgentsSpanOutcomeEvaluationEndEvent struct{…}

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

ID string

Unique identifier for this event.

Explanation string

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

Iteration int64

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

OutcomeEvaluationStartID string

The id of the corresponding `span.outcome_evaluation_start` event.

OutcomeID string

The `outc_` ID of the outcome being evaluated.

ProcessedAt Time

A timestamp in RFC 3339 format

Result string

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

Type BetaManagedAgentsSpanOutcomeEvaluationEndEventType



Usage [BetaManagedAgentsSpanModelUsage](api/beta.md)

Token usage for a single model request.

CacheCreationInputTokens int64

Tokens used to create prompt cache in this request.

CacheReadInputTokens int64

Tokens read from prompt cache in this request.

InputTokens int64

Input tokens consumed by this request.

OutputTokens int64

Output tokens generated by this request.



Speed BetaManagedAgentsSpanModelUsageSpeedOptional

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

const BetaManagedAgentsSpanModelUsageSpeedStandard BetaManagedAgentsSpanModelUsageSpeed = "standard"

const BetaManagedAgentsSpanModelUsageSpeedFast BetaManagedAgentsSpanModelUsageSpeed = "fast"



type BetaManagedAgentsSpanModelRequestStartEvent struct{…}

Emitted when a model request is initiated by the agent.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSpanModelRequestStartEventType



type BetaManagedAgentsSpanModelRequestEndEvent struct{…}

Emitted when a model request completes.

ID string

Unique identifier for this event.

IsError bool

Whether the model request resulted in an error.

ModelRequestStartID string

The id of the corresponding `span.model_request_start` event.



ModelUsage [BetaManagedAgentsSpanModelUsage](api/beta.md)

Token usage for a single model request.

CacheCreationInputTokens int64

Tokens used to create prompt cache in this request.

CacheReadInputTokens int64

Tokens read from prompt cache in this request.

InputTokens int64

Input tokens consumed by this request.

OutputTokens int64

Output tokens generated by this request.



Speed BetaManagedAgentsSpanModelUsageSpeedOptional

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

const BetaManagedAgentsSpanModelUsageSpeedStandard BetaManagedAgentsSpanModelUsageSpeed = "standard"

const BetaManagedAgentsSpanModelUsageSpeedFast BetaManagedAgentsSpanModelUsageSpeed = "fast"

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSpanModelRequestEndEventType



type BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent struct{…}

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

ID string

Unique identifier for this event.

Iteration int64

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

OutcomeID string

The `outc_` ID of the outcome being evaluated.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSpanOutcomeEvaluationOngoingEventType



type BetaManagedAgentsUserDefineOutcomeEvent struct{…}

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

ID string

Unique identifier for this event.

Description string

What the agent should produce. Copied from the input event.

MaxIterations int64

Evaluate-then-revise cycles before giving up. Default 3, max 20.

OutcomeID string

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

ProcessedAt Time

A timestamp in RFC 3339 format



Rubric BetaManagedAgentsUserDefineOutcomeEventRubricUnion

Rubric for grading the quality of an outcome.

One of the following:



type BetaManagedAgentsFileRubric struct{…}

Rubric referenced by a file uploaded via the Files API.

FileID string

ID of the rubric file.

Type BetaManagedAgentsFileRubricType



type BetaManagedAgentsTextRubric struct{…}

Rubric content provided inline as text.

Content string

Rubric content. Plain text or markdown — the grader treats it as freeform text.

Type BetaManagedAgentsTextRubricType

Type BetaManagedAgentsUserDefineOutcomeEventType



type BetaManagedAgentsSessionDeletedEvent struct{…}

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionDeletedEventType



type BetaManagedAgentsSessionThreadStatusRunningEvent struct{…}

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

ID string

Unique identifier for this event.

AgentName string

Name of the agent the thread runs.

ProcessedAt Time

A timestamp in RFC 3339 format

SessionThreadID string

Public sthr\_ ID of the thread that started running.

Type BetaManagedAgentsSessionThreadStatusRunningEventType



type BetaManagedAgentsSessionThreadStatusIdleEvent struct{…}

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

ID string

Unique identifier for this event.

AgentName string

Name of the agent the thread runs.

ProcessedAt Time

A timestamp in RFC 3339 format

SessionThreadID string

Public sthr\_ ID of the thread that went idle.



StopReason BetaManagedAgentsSessionThreadStatusIdleEventStopReasonUnion

The agent completed its turn naturally and is ready for the next user message.

One of the following:



type BetaManagedAgentsSessionEndTurn struct{…}

The agent completed its turn naturally and is ready for the next user message.

Type BetaManagedAgentsSessionEndTurnType



type BetaManagedAgentsSessionRequiresAction struct{…}

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

EventIDs []string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type BetaManagedAgentsSessionRequiresActionType



type BetaManagedAgentsSessionRetriesExhausted struct{…}

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type BetaManagedAgentsSessionRetriesExhaustedType

Type BetaManagedAgentsSessionThreadStatusIdleEventType



type BetaManagedAgentsSessionThreadStatusTerminatedEvent struct{…}

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

ID string

Unique identifier for this event.

AgentName string

Name of the agent the thread runs.

ProcessedAt Time

A timestamp in RFC 3339 format

SessionThreadID string

Public sthr\_ ID of the thread that terminated.

Type BetaManagedAgentsSessionThreadStatusTerminatedEventType



type BetaManagedAgentsUserToolResultEvent struct{…}

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

ID string

Unique identifier for this event.

ToolUseID string

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserToolResultEventType



Content []BetaManagedAgentsUserToolResultEventContentUnionOptional

The result content returned by the tool.

One of the following:



type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType



type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.



Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

One of the following:



type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType



type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.



type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType



type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

One of the following:



type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType



type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType



type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.



type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringOptional

Additional context about the document for the model.

Title stringOptional

The title of the document.



type BetaManagedAgentsSearchResultBlock struct{…}

A block containing a web search result.



Citations [BetaManagedAgentsSearchResultCitations](api/beta.md)

Citation settings for a search result.

Enabled bool

Whether citations are enabled for this search result.



Content [][BetaManagedAgentsSearchResultContent](api/beta.md)

Array of text content blocks from the search result.

Text string

The text content.

Type BetaManagedAgentsSearchResultContentType

Source string

The URL source of the search result.

Title string

The title of the search result.

Type BetaManagedAgentsSearchResultBlockType

IsError boolOptional

Whether the tool execution resulted in an error.

ProcessedAt TimeOptional

A timestamp in RFC 3339 format

SessionThreadID stringOptional

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.



type BetaManagedAgentsSessionThreadStatusRescheduledEvent struct{…}

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

ID string

Unique identifier for this event.

AgentName string

Name of the agent the thread runs.

ProcessedAt Time

A timestamp in RFC 3339 format

SessionThreadID string

Public sthr\_ ID of the thread that is retrying.

Type BetaManagedAgentsSessionThreadStatusRescheduledEventType



type BetaManagedAgentsSessionUpdatedEvent struct{…}

Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionUpdatedEventType



Agent [BetaManagedAgentsSessionAgent](api/beta.md)Optional

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

ID string

Description string



MCPServers [][BetaManagedAgentsMCPServerURLDefinition](api/beta.md)

Name string

Type BetaManagedAgentsMCPServerURLDefinitionType

URL string



Model [BetaManagedAgentsModelConfig](api/beta.md)

Model identifier and configuration.



ID BetaManagedAgentsModel

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



type BetaManagedAgentsModel string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

const BetaManagedAgentsModelClaudeOpus4\_8 BetaManagedAgentsModel = "claude-opus-4-8"

Frontier intelligence for long-running agents and coding

const BetaManagedAgentsModelClaudeOpus4\_7 BetaManagedAgentsModel = "claude-opus-4-7"

Frontier intelligence for long-running agents and coding

const BetaManagedAgentsModelClaudeOpus4\_6 BetaManagedAgentsModel = "claude-opus-4-6"

Most intelligent model for building agents and coding

const BetaManagedAgentsModelClaudeSonnet4\_6 BetaManagedAgentsModel = "claude-sonnet-4-6"

Best combination of speed and intelligence

const BetaManagedAgentsModelClaudeHaiku4\_5 BetaManagedAgentsModel = "claude-haiku-4-5"

Fastest model with near-frontier intelligence

const BetaManagedAgentsModelClaudeHaiku4\_5\_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

const BetaManagedAgentsModelClaudeOpus4\_5 BetaManagedAgentsModel = "claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

const BetaManagedAgentsModelClaudeOpus4\_5\_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

const BetaManagedAgentsModelClaudeSonnet4\_5 BetaManagedAgentsModel = "claude-sonnet-4-5"

High-performance model for agents and coding

const BetaManagedAgentsModelClaudeSonnet4\_5\_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"

High-performance model for agents and coding

string



Speed BetaManagedAgentsModelConfigSpeedOptional

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"

const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"



Multiagent [BetaManagedAgentsSessionMultiagentCoordinator](api/beta.md)

Resolved coordinator topology with full agent definitions for each roster member.



Agents [][BetaManagedAgentsSessionThreadAgent](api/beta.md)

Full `agent` definitions the coordinator may spawn as session threads.

ID string

Description string



MCPServers [][BetaManagedAgentsMCPServerURLDefinition](api/beta.md)

Name string

Type BetaManagedAgentsMCPServerURLDefinitionType

URL string



Model [BetaManagedAgentsModelConfig](api/beta.md)

Model identifier and configuration.



ID BetaManagedAgentsModel

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



type BetaManagedAgentsModel string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

const BetaManagedAgentsModelClaudeOpus4\_8 BetaManagedAgentsModel = "claude-opus-4-8"

Frontier intelligence for long-running agents and coding

const BetaManagedAgentsModelClaudeOpus4\_7 BetaManagedAgentsModel = "claude-opus-4-7"

Frontier intelligence for long-running agents and coding

const BetaManagedAgentsModelClaudeOpus4\_6 BetaManagedAgentsModel = "claude-opus-4-6"

Most intelligent model for building agents and coding

const BetaManagedAgentsModelClaudeSonnet4\_6 BetaManagedAgentsModel = "claude-sonnet-4-6"

Best combination of speed and intelligence

const BetaManagedAgentsModelClaudeHaiku4\_5 BetaManagedAgentsModel = "claude-haiku-4-5"

Fastest model with near-frontier intelligence

const BetaManagedAgentsModelClaudeHaiku4\_5\_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

const BetaManagedAgentsModelClaudeOpus4\_5 BetaManagedAgentsModel = "claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

const BetaManagedAgentsModelClaudeOpus4\_5\_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

const BetaManagedAgentsModelClaudeSonnet4\_5 BetaManagedAgentsModel = "claude-sonnet-4-5"

High-performance model for agents and coding

const BetaManagedAgentsModelClaudeSonnet4\_5\_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"

High-performance model for agents and coding

string



Speed BetaManagedAgentsModelConfigSpeedOptional

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"

const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"

Name string



Skills []BetaManagedAgentsSessionThreadAgentSkillUnion

One of the following:



type BetaManagedAgentsAnthropicSkill struct{…}

A resolved Anthropic-managed skill.

SkillID string

Type BetaManagedAgentsAnthropicSkillType

Version string



type BetaManagedAgentsCustomSkill struct{…}

A resolved user-created custom skill.

SkillID string

Type BetaManagedAgentsCustomSkillType

Version string

System string



Tools []BetaManagedAgentsSessionThreadAgentToolUnion

One of the following:



type BetaManagedAgentsAgentToolset20260401 struct{…}



Configs [][BetaManagedAgentsAgentToolConfig](api/beta.md)

Enabled bool



Name BetaManagedAgentsAgentToolConfigName

Built-in agent tool identifier.

One of the following:

const BetaManagedAgentsAgentToolConfigNameBash BetaManagedAgentsAgentToolConfigName = "bash"

const BetaManagedAgentsAgentToolConfigNameEdit BetaManagedAgentsAgentToolConfigName = "edit"

const BetaManagedAgentsAgentToolConfigNameRead BetaManagedAgentsAgentToolConfigName = "read"

const BetaManagedAgentsAgentToolConfigNameWrite BetaManagedAgentsAgentToolConfigName = "write"

const BetaManagedAgentsAgentToolConfigNameGlob BetaManagedAgentsAgentToolConfigName = "glob"

const BetaManagedAgentsAgentToolConfigNameGrep BetaManagedAgentsAgentToolConfigName = "grep"

const BetaManagedAgentsAgentToolConfigNameWebFetch BetaManagedAgentsAgentToolConfigName = "web\_fetch"

const BetaManagedAgentsAgentToolConfigNameWebSearch BetaManagedAgentsAgentToolConfigName = "web\_search"



PermissionPolicy BetaManagedAgentsAgentToolConfigPermissionPolicyUnion

Permission policy for tool execution.

One of the following:



type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType



type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType



DefaultConfig [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md)

Resolved default configuration for agent tools.

Enabled bool



PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion

Permission policy for tool execution.

One of the following:



type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType



type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType

Type BetaManagedAgentsAgentToolset20260401Type



type BetaManagedAgentsMCPToolset struct{…}



Configs [][BetaManagedAgentsMCPToolConfig](api/beta.md)

Enabled bool

Name string



PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion

Permission policy for tool execution.

One of the following:



type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType



type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType



DefaultConfig [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md)

Resolved default configuration for all tools from an MCP server.

Enabled bool



PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion

Permission policy for tool execution.

One of the following:



type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType



type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType

MCPServerName string

Type BetaManagedAgentsMCPToolsetType



type BetaManagedAgentsCustomTool struct{…}

A custom tool as returned in API responses.

Description string



InputSchema [BetaManagedAgentsCustomToolInputSchema](api/beta.md)

JSON Schema for custom tool input parameters.

Type Object

Properties map[string, any]Optional

Required []stringOptional

Name string

Type BetaManagedAgentsCustomToolType

Type BetaManagedAgentsSessionThreadAgentType

Version int64

Type BetaManagedAgentsSessionMultiagentCoordinatorType

Name string



Skills []BetaManagedAgentsSessionAgentSkillUnion

One of the following:



type BetaManagedAgentsAnthropicSkill struct{…}

A resolved Anthropic-managed skill.

SkillID string

Type BetaManagedAgentsAnthropicSkillType

Version string



type BetaManagedAgentsCustomSkill struct{…}

A resolved user-created custom skill.

SkillID string

Type BetaManagedAgentsCustomSkillType

Version string

System string



Tools []BetaManagedAgentsSessionAgentToolUnion

One of the following:



type BetaManagedAgentsAgentToolset20260401 struct{…}



Configs [][BetaManagedAgentsAgentToolConfig](api/beta.md)

Enabled bool



Name BetaManagedAgentsAgentToolConfigName

Built-in agent tool identifier.

One of the following:

const BetaManagedAgentsAgentToolConfigNameBash BetaManagedAgentsAgentToolConfigName = "bash"

const BetaManagedAgentsAgentToolConfigNameEdit BetaManagedAgentsAgentToolConfigName = "edit"

const BetaManagedAgentsAgentToolConfigNameRead BetaManagedAgentsAgentToolConfigName = "read"

const BetaManagedAgentsAgentToolConfigNameWrite BetaManagedAgentsAgentToolConfigName = "write"

const BetaManagedAgentsAgentToolConfigNameGlob BetaManagedAgentsAgentToolConfigName = "glob"

const BetaManagedAgentsAgentToolConfigNameGrep BetaManagedAgentsAgentToolConfigName = "grep"

const BetaManagedAgentsAgentToolConfigNameWebFetch BetaManagedAgentsAgentToolConfigName = "web\_fetch"

const BetaManagedAgentsAgentToolConfigNameWebSearch BetaManagedAgentsAgentToolConfigName = "web\_search"



PermissionPolicy BetaManagedAgentsAgentToolConfigPermissionPolicyUnion

Permission policy for tool execution.

One of the following:



type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType



type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType



DefaultConfig [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md)

Resolved default configuration for agent tools.

Enabled bool



PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion

Permission policy for tool execution.

One of the following:



type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType



type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType

Type BetaManagedAgentsAgentToolset20260401Type



type BetaManagedAgentsMCPToolset struct{…}



Configs [][BetaManagedAgentsMCPToolConfig](api/beta.md)

Enabled bool

Name string



PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion

Permission policy for tool execution.

One of the following:



type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType



type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType



DefaultConfig [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md)

Resolved default configuration for all tools from an MCP server.

Enabled bool



PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion

Permission policy for tool execution.

One of the following:



type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType



type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType

MCPServerName string

Type BetaManagedAgentsMCPToolsetType



type BetaManagedAgentsCustomTool struct{…}

A custom tool as returned in API responses.

Description string



InputSchema [BetaManagedAgentsCustomToolInputSchema](api/beta.md)

JSON Schema for custom tool input parameters.

Type Object

Properties map[string, any]Optional

Required []stringOptional

Name string

Type BetaManagedAgentsCustomToolType

Type BetaManagedAgentsSessionAgentType

Version int64

Metadata map[string, string]Optional

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

Title stringOptional

The session's new title. Present only when the update changed it.



type BetaManagedAgentsSystemMessageEvent struct{…}

A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

ID string

Unique identifier for this event.



Content [][BetaManagedAgentsSystemContentBlock](api/beta.md)

System content blocks. Text-only.

Text string

The text content.

Type BetaManagedAgentsSystemContentBlockType

Type BetaManagedAgentsSystemMessageEventType

ProcessedAt TimeOptional

A timestamp in RFC 3339 format

List Session Thread Events

Go

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
  page, err := client.Beta.Sessions.Threads.Events.List(
    context.TODO(),
    "sthr_011CZkZVWa6oIjw0rgXZpnBt",
    anthropic.BetaSessionThreadEventListParams{
      SessionID: "sesn_011CZkZAtmR3yMPDzynEDxu7",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
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
  ],
  "next_page": "next_page"
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
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
