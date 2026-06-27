# Events

Copy page



PHP

# Events

##### [List Events](api/beta/sessions/events/list.md)

$client->beta->sessions->events->list(string sessionID, ?\Datetime createdAtGt, ?\Datetime createdAtGte, ?\Datetime createdAtLt, ?\Datetime createdAtLte, ?int limit, ?[Order](api/beta/sessions/events/list.md) order, ?string page, ?list<string> types, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsSessionEvent](api/beta/sessions/events.md)>

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

$client->beta->sessions->events->send(string sessionID, list<[ManagedAgentsEventParams](api/beta/sessions/events.md)> events, ?list<AnthropicBeta> betas): [ManagedAgentsSendSessionEvents](api/beta/sessions/events.md)

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

$client->beta->sessions->events->stream(string sessionID, ?list<AnthropicBeta> betas): [ManagedAgentsStreamSessionEvents](api/beta/sessions/events.md)

GET/v1/sessions/{session\_id}/events/stream

##### ModelsExpand Collapse



[ManagedAgentsAgentCustomToolUseEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

array<string,mixed> input

Input parameters for the tool call.

string name

Name of the custom tool being called.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?string sessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.



[ManagedAgentsAgentMCPToolResultEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string mcpToolUseID

The id of the `agent.mcp_tool_use` event this result corresponds to.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.



[ManagedAgentsAgentMCPToolUseEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

array<string,mixed> input

Input parameters for the tool call.

string mcpServerName

Name of the MCP server providing the tool.

string name

Name of the MCP tool being used.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?EvaluatedPermission evaluatedPermission

AgentEvaluatedPermission enum

?string sessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



[ManagedAgentsAgentMessageEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

list<[ManagedAgentsTextBlock](api/beta/sessions/events.md)> content

Array of text blocks comprising the agent response.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsAgentThinkingEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsAgentThreadContextCompactedEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsAgentThreadMessageReceivedEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

list<Content> content

Message content blocks.

string fromSessionThreadID

Public `sthr_` ID of the thread that sent the message.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?string fromAgentName

Name of the callable agent this message came from. Absent when received from the primary agent.



[ManagedAgentsAgentThreadMessageSentEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

list<Content> content

Message content blocks.

\Datetime processedAt

A timestamp in RFC 3339 format

string toSessionThreadID

Public `sthr_` ID of the thread the message was sent to.

Type type

?string toAgentName

Name of the callable agent this message was sent to. Absent when sent to the primary agent.



[ManagedAgentsAgentToolResultEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

string toolUseID

The id of the `agent.tool_use` event this result corresponds to.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.



[ManagedAgentsAgentToolUseEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

array<string,mixed> input

Input parameters for the tool call.

string name

Name of the agent tool being used.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?EvaluatedPermission evaluatedPermission

AgentEvaluatedPermission enum

?string sessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



[ManagedAgentsBase64DocumentSource](api/beta/sessions/events.md)

string data

Base64-encoded document data.

string mediaType

MIME type of the document (e.g., "application/pdf").

Type type



[ManagedAgentsBase64ImageSource](api/beta/sessions/events.md)

string data

Base64-encoded image data.

string mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



[ManagedAgentsBillingError](api/beta/sessions/events.md)

string message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Type type



[ManagedAgentsCredentialHostUnreachableError](api/beta/sessions/events.md)

string credentialID

ID of the affected credential.

string message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Type type

string vaultID

ID of the vault containing the affected credential.



[ManagedAgentsDocumentBlock](api/beta/sessions/events.md)

Source source

Union type for document source variants.

Type type

?string context

Additional context about the document for the model.

?string title

The title of the document.



[ManagedAgentsEventParams](api/beta/sessions/events.md)

One of the following:



[ManagedAgentsUserMessageEventParams](api/beta/sessions/events.md)

list<Content> content

Array of content blocks for the user message.

Type type



[ManagedAgentsUserInterruptEventParams](api/beta/sessions/events.md)

Type type

?string sessionThreadID

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



[ManagedAgentsUserToolConfirmationEventParams](api/beta/sessions/events.md)

Result result

UserToolConfirmationResult enum

string toolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?string denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.



[ManagedAgentsUserCustomToolResultEventParams](api/beta/sessions/events.md)

string customToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.



[ManagedAgentsUserDefineOutcomeEventParams](api/beta/sessions/events.md)

string description

What the agent should produce. This is the task specification.

Rubric rubric

Rubric for grading the quality of an outcome.

Type type

?int maxIterations

Eval→revision cycles before giving up. Default 3, max 20.



[ManagedAgentsUserToolResultEventParams](api/beta/sessions/events.md)

string toolUseID

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.



[ManagedAgentsSystemMessageEventParams](api/beta/sessions/events.md)

list<[BetaManagedAgentsSystemContentBlock](api/beta/sessions.md)> content

System content blocks to append. Text-only.

Type type



[ManagedAgentsFileDocumentSource](api/beta/sessions/events.md)

string fileID

ID of a previously uploaded file.

Type type



[ManagedAgentsFileImageSource](api/beta/sessions/events.md)

string fileID

ID of a previously uploaded file.

Type type



[ManagedAgentsFileRubric](api/beta/sessions/events.md)

string fileID

ID of the rubric file.

Type type



[ManagedAgentsFileRubricParams](api/beta/sessions/events.md)

string fileID

ID of the rubric file.

Type type



[ManagedAgentsImageBlock](api/beta/sessions/events.md)

Source source

Union type for image source variants.

Type type



[ManagedAgentsMCPAuthenticationFailedError](api/beta/sessions/events.md)

string mcpServerName

Name of the MCP server that failed authentication.

string message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Type type



[ManagedAgentsMCPConnectionFailedError](api/beta/sessions/events.md)

string mcpServerName

Name of the MCP server that failed to connect.

string message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Type type



[ManagedAgentsModelOverloadedError](api/beta/sessions/events.md)

string message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Type type



[ManagedAgentsModelRateLimitedError](api/beta/sessions/events.md)

string message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Type type



[ManagedAgentsModelRequestFailedError](api/beta/sessions/events.md)

string message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Type type



[ManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md)

string data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



[ManagedAgentsRetryStatusExhausted](api/beta/sessions/events.md)

Type type



[ManagedAgentsRetryStatusRetrying](api/beta/sessions/events.md)

Type type



[ManagedAgentsRetryStatusTerminal](api/beta/sessions/events.md)

Type type



[ManagedAgentsSearchResultBlock](api/beta/sessions/events.md)

[ManagedAgentsSearchResultCitations](api/beta/sessions/events.md) citations

Citation settings for a search result.

list<[ManagedAgentsSearchResultContent](api/beta/sessions/events.md)> content

Array of text content blocks from the search result.

string source

The URL source of the search result.

string title

The title of the search result.

Type type



[ManagedAgentsSearchResultCitations](api/beta/sessions/events.md)

bool enabled

Whether citations are enabled for this search result.



[ManagedAgentsSearchResultContent](api/beta/sessions/events.md)

string text

The text content.

Type type



[ManagedAgentsSendSessionEvents](api/beta/sessions/events.md)

?list<Data> data

Sent events



[ManagedAgentsSessionDeletedEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSessionEndTurn](api/beta/sessions/events.md)

Type type



[ManagedAgentsSessionErrorEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

Error error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSessionEvent](api/beta/sessions/events.md)

One of the following:



[ManagedAgentsUserMessageEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

list<Content> content

Array of content blocks comprising the user message.

Type type

?\Datetime processedAt

A timestamp in RFC 3339 format



[ManagedAgentsUserInterruptEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

Type type

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



[ManagedAgentsUserToolConfirmationEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

Result result

UserToolConfirmationResult enum

string toolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?string denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.



[ManagedAgentsUserCustomToolResultEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string customToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.



[ManagedAgentsAgentCustomToolUseEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

array<string,mixed> input

Input parameters for the tool call.

string name

Name of the custom tool being called.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?string sessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.



[ManagedAgentsAgentMessageEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

list<[ManagedAgentsTextBlock](api/beta/sessions/events.md)> content

Array of text blocks comprising the agent response.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsAgentThinkingEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsAgentMCPToolUseEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

array<string,mixed> input

Input parameters for the tool call.

string mcpServerName

Name of the MCP server providing the tool.

string name

Name of the MCP tool being used.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?EvaluatedPermission evaluatedPermission

AgentEvaluatedPermission enum

?string sessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



[ManagedAgentsAgentMCPToolResultEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string mcpToolUseID

The id of the `agent.mcp_tool_use` event this result corresponds to.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.



[ManagedAgentsAgentToolUseEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

array<string,mixed> input

Input parameters for the tool call.

string name

Name of the agent tool being used.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?EvaluatedPermission evaluatedPermission

AgentEvaluatedPermission enum

?string sessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



[ManagedAgentsAgentToolResultEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

string toolUseID

The id of the `agent.tool_use` event this result corresponds to.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.



[ManagedAgentsAgentThreadMessageReceivedEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

list<Content> content

Message content blocks.

string fromSessionThreadID

Public `sthr_` ID of the thread that sent the message.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?string fromAgentName

Name of the callable agent this message came from. Absent when received from the primary agent.



[ManagedAgentsAgentThreadMessageSentEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

list<Content> content

Message content blocks.

\Datetime processedAt

A timestamp in RFC 3339 format

string toSessionThreadID

Public `sthr_` ID of the thread the message was sent to.

Type type

?string toAgentName

Name of the callable agent this message was sent to. Absent when sent to the primary agent.



[ManagedAgentsAgentThreadContextCompactedEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSessionErrorEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

Error error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSessionStatusRescheduledEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSessionStatusRunningEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSessionStatusIdleEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

Type type



[ManagedAgentsSessionStatusTerminatedEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSessionThreadCreatedEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string agentName

Name of the callable agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public `sthr_` ID of the newly created thread.

Type type



[ManagedAgentsSpanOutcomeEvaluationStartEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

int iteration

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

string outcomeID

The `outc_` ID of the outcome being evaluated.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSpanOutcomeEvaluationEndEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string explanation

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

int iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

string outcomeEvaluationStartID

The id of the corresponding `span.outcome_evaluation_start` event.

string outcomeID

The `outc_` ID of the outcome being evaluated.

\Datetime processedAt

A timestamp in RFC 3339 format

string result

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

Type type

[ManagedAgentsSpanModelUsage](api/beta/sessions/events.md) usage

Token usage for a single model request.



[ManagedAgentsSpanModelRequestStartEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSpanModelRequestEndEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

?bool isError

Whether the model request resulted in an error.

string modelRequestStartID

The id of the corresponding `span.model_request_start` event.

[ManagedAgentsSpanModelUsage](api/beta/sessions/events.md) modelUsage

Token usage for a single model request.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSpanOutcomeEvaluationOngoingEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

int iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

string outcomeID

The `outc_` ID of the outcome being evaluated.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsUserDefineOutcomeEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string description

What the agent should produce. Copied from the input event.

?int maxIterations

Evaluate-then-revise cycles before giving up. Default 3, max 20.

string outcomeID

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

\Datetime processedAt

A timestamp in RFC 3339 format

Rubric rubric

Rubric for grading the quality of an outcome.

Type type



[ManagedAgentsSessionDeletedEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSessionThreadStatusRunningEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that started running.

Type type



[ManagedAgentsSessionThreadStatusIdleEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that went idle.

StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

Type type



[ManagedAgentsSessionThreadStatusTerminatedEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that terminated.

Type type



[BetaManagedAgentsUserToolResultEvent](api/beta/sessions.md)

string id

Unique identifier for this event.

string toolUseID

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.



[ManagedAgentsSessionThreadStatusRescheduledEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that is retrying.

Type type



[BetaManagedAgentsSessionUpdatedEvent](api/beta/sessions.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?[BetaManagedAgentsSessionAgent](api/beta/sessions.md) agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

?array<string,string> metadata

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

?string title

The session's new title. Present only when the update changed it.



[BetaManagedAgentsSystemMessageEvent](api/beta/sessions.md)

string id

Unique identifier for this event.

list<[BetaManagedAgentsSystemContentBlock](api/beta/sessions.md)> content

System content blocks. Text-only.

Type type

?\Datetime processedAt

A timestamp in RFC 3339 format



[ManagedAgentsSessionRequiresAction](api/beta/sessions/events.md)

list<string> eventIDs

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type type



[ManagedAgentsSessionRetriesExhausted](api/beta/sessions/events.md)

Type type



[ManagedAgentsSessionStatusIdleEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

Type type



[ManagedAgentsSessionStatusRescheduledEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSessionStatusRunningEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSessionStatusTerminatedEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSessionThreadCreatedEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string agentName

Name of the callable agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public `sthr_` ID of the newly created thread.

Type type



[ManagedAgentsSessionThreadStatusIdleEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that went idle.

StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

Type type



[ManagedAgentsSessionThreadStatusRescheduledEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that is retrying.

Type type



[ManagedAgentsSessionThreadStatusRunningEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that started running.

Type type



[ManagedAgentsSessionThreadStatusTerminatedEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that terminated.

Type type



[ManagedAgentsSpanModelRequestEndEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

?bool isError

Whether the model request resulted in an error.

string modelRequestStartID

The id of the corresponding `span.model_request_start` event.

[ManagedAgentsSpanModelUsage](api/beta/sessions/events.md) modelUsage

Token usage for a single model request.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSpanModelRequestStartEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSpanModelUsage](api/beta/sessions/events.md)

int cacheCreationInputTokens

Tokens used to create prompt cache in this request.

int cacheReadInputTokens

Tokens read from prompt cache in this request.

int inputTokens

Input tokens consumed by this request.

int outputTokens

Output tokens generated by this request.

?Speed speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.



[ManagedAgentsSpanOutcomeEvaluationEndEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string explanation

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

int iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

string outcomeEvaluationStartID

The id of the corresponding `span.outcome_evaluation_start` event.

string outcomeID

The `outc_` ID of the outcome being evaluated.

\Datetime processedAt

A timestamp in RFC 3339 format

string result

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

Type type

[ManagedAgentsSpanModelUsage](api/beta/sessions/events.md) usage

Token usage for a single model request.



[ManagedAgentsSpanOutcomeEvaluationOngoingEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

int iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

string outcomeID

The `outc_` ID of the outcome being evaluated.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSpanOutcomeEvaluationStartEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

int iteration

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

string outcomeID

The `outc_` ID of the outcome being evaluated.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsStreamSessionEvents](api/beta/sessions/events.md)

One of the following:



[ManagedAgentsUserMessageEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

list<Content> content

Array of content blocks comprising the user message.

Type type

?\Datetime processedAt

A timestamp in RFC 3339 format



[ManagedAgentsUserInterruptEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

Type type

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



[ManagedAgentsUserToolConfirmationEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

Result result

UserToolConfirmationResult enum

string toolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?string denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.



[ManagedAgentsUserCustomToolResultEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string customToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.



[ManagedAgentsAgentCustomToolUseEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

array<string,mixed> input

Input parameters for the tool call.

string name

Name of the custom tool being called.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?string sessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.



[ManagedAgentsAgentMessageEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

list<[ManagedAgentsTextBlock](api/beta/sessions/events.md)> content

Array of text blocks comprising the agent response.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsAgentThinkingEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsAgentMCPToolUseEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

array<string,mixed> input

Input parameters for the tool call.

string mcpServerName

Name of the MCP server providing the tool.

string name

Name of the MCP tool being used.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?EvaluatedPermission evaluatedPermission

AgentEvaluatedPermission enum

?string sessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



[ManagedAgentsAgentMCPToolResultEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string mcpToolUseID

The id of the `agent.mcp_tool_use` event this result corresponds to.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.



[ManagedAgentsAgentToolUseEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

array<string,mixed> input

Input parameters for the tool call.

string name

Name of the agent tool being used.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?EvaluatedPermission evaluatedPermission

AgentEvaluatedPermission enum

?string sessionThreadID

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



[ManagedAgentsAgentToolResultEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

string toolUseID

The id of the `agent.tool_use` event this result corresponds to.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.



[ManagedAgentsAgentThreadMessageReceivedEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

list<Content> content

Message content blocks.

string fromSessionThreadID

Public `sthr_` ID of the thread that sent the message.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?string fromAgentName

Name of the callable agent this message came from. Absent when received from the primary agent.



[ManagedAgentsAgentThreadMessageSentEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

list<Content> content

Message content blocks.

\Datetime processedAt

A timestamp in RFC 3339 format

string toSessionThreadID

Public `sthr_` ID of the thread the message was sent to.

Type type

?string toAgentName

Name of the callable agent this message was sent to. Absent when sent to the primary agent.



[ManagedAgentsAgentThreadContextCompactedEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSessionErrorEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

Error error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSessionStatusRescheduledEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSessionStatusRunningEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSessionStatusIdleEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

Type type



[ManagedAgentsSessionStatusTerminatedEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSessionThreadCreatedEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string agentName

Name of the callable agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public `sthr_` ID of the newly created thread.

Type type



[ManagedAgentsSpanOutcomeEvaluationStartEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

int iteration

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

string outcomeID

The `outc_` ID of the outcome being evaluated.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSpanOutcomeEvaluationEndEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string explanation

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

int iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

string outcomeEvaluationStartID

The id of the corresponding `span.outcome_evaluation_start` event.

string outcomeID

The `outc_` ID of the outcome being evaluated.

\Datetime processedAt

A timestamp in RFC 3339 format

string result

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

Type type

[ManagedAgentsSpanModelUsage](api/beta/sessions/events.md) usage

Token usage for a single model request.



[ManagedAgentsSpanModelRequestStartEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSpanModelRequestEndEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

?bool isError

Whether the model request resulted in an error.

string modelRequestStartID

The id of the corresponding `span.model_request_start` event.

[ManagedAgentsSpanModelUsage](api/beta/sessions/events.md) modelUsage

Token usage for a single model request.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSpanOutcomeEvaluationOngoingEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

int iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

string outcomeID

The `outc_` ID of the outcome being evaluated.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsUserDefineOutcomeEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string description

What the agent should produce. Copied from the input event.

?int maxIterations

Evaluate-then-revise cycles before giving up. Default 3, max 20.

string outcomeID

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

\Datetime processedAt

A timestamp in RFC 3339 format

Rubric rubric

Rubric for grading the quality of an outcome.

Type type



[ManagedAgentsSessionDeletedEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSessionThreadStatusRunningEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that started running.

Type type



[ManagedAgentsSessionThreadStatusIdleEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that went idle.

StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

Type type



[ManagedAgentsSessionThreadStatusTerminatedEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that terminated.

Type type



[BetaManagedAgentsUserToolResultEvent](api/beta/sessions.md)

string id

Unique identifier for this event.

string toolUseID

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.



[ManagedAgentsSessionThreadStatusRescheduledEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string agentName

Name of the agent the thread runs.

\Datetime processedAt

A timestamp in RFC 3339 format

string sessionThreadID

Public sthr\_ ID of the thread that is retrying.

Type type



[BetaManagedAgentsSessionUpdatedEvent](api/beta/sessions.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?[BetaManagedAgentsSessionAgent](api/beta/sessions.md) agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

?array<string,string> metadata

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

?string title

The session's new title. Present only when the update changed it.



[BetaManagedAgentsSystemMessageEvent](api/beta/sessions.md)

string id

Unique identifier for this event.

list<[BetaManagedAgentsSystemContentBlock](api/beta/sessions.md)> content

System content blocks. Text-only.

Type type

?\Datetime processedAt

A timestamp in RFC 3339 format



[ManagedAgentsSystemMessageEventParams](api/beta/sessions/events.md)

list<[BetaManagedAgentsSystemContentBlock](api/beta/sessions.md)> content

System content blocks to append. Text-only.

Type type



[ManagedAgentsTextBlock](api/beta/sessions/events.md)

string text

The text content.

Type type



[ManagedAgentsTextRubric](api/beta/sessions/events.md)

string content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

Type type



[ManagedAgentsTextRubricParams](api/beta/sessions/events.md)

string content

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

Type type



[ManagedAgentsUnknownError](api/beta/sessions/events.md)

string message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Type type



[ManagedAgentsURLDocumentSource](api/beta/sessions/events.md)

Type type

string url

URL of the document to fetch.



[ManagedAgentsURLImageSource](api/beta/sessions/events.md)

Type type

string url

URL of the image to fetch.



[ManagedAgentsUserCustomToolResultEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string customToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.



[ManagedAgentsUserCustomToolResultEventParams](api/beta/sessions/events.md)

string customToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.



[ManagedAgentsUserDefineOutcomeEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

string description

What the agent should produce. Copied from the input event.

?int maxIterations

Evaluate-then-revise cycles before giving up. Default 3, max 20.

string outcomeID

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

\Datetime processedAt

A timestamp in RFC 3339 format

Rubric rubric

Rubric for grading the quality of an outcome.

Type type



[ManagedAgentsUserDefineOutcomeEventParams](api/beta/sessions/events.md)

string description

What the agent should produce. This is the task specification.

Rubric rubric

Rubric for grading the quality of an outcome.

Type type

?int maxIterations

Eval→revision cycles before giving up. Default 3, max 20.



[ManagedAgentsUserInterruptEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

Type type

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



[ManagedAgentsUserInterruptEventParams](api/beta/sessions/events.md)

Type type

?string sessionThreadID

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



[ManagedAgentsUserMessageEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

list<Content> content

Array of content blocks comprising the user message.

Type type

?\Datetime processedAt

A timestamp in RFC 3339 format



[ManagedAgentsUserMessageEventParams](api/beta/sessions/events.md)

list<Content> content

Array of content blocks for the user message.

Type type



[ManagedAgentsUserToolConfirmationEvent](api/beta/sessions/events.md)

string id

Unique identifier for this event.

Result result

UserToolConfirmationResult enum

string toolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?string denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.



[ManagedAgentsUserToolConfirmationEventParams](api/beta/sessions/events.md)

Result result

UserToolConfirmationResult enum

string toolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?string denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.



[ManagedAgentsUserToolResultEventParams](api/beta/sessions/events.md)

string toolUseID

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

---

*Copyright © Anthropic. All rights reserved.*
