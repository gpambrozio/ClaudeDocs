# Threads

Copy page



PHP

# Threads

##### [List Session Threads](api/beta/sessions/threads/list.md)

$client->beta->sessions->threads->list(string sessionID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsSessionThread](api/beta.md)>

GET/v1/sessions/{session\_id}/threads

##### [Get Session Thread](api/beta/sessions/threads/retrieve.md)

$client->beta->sessions->threads->retrieve(string threadID, string sessionID, ?list<AnthropicBeta> betas): [ManagedAgentsSessionThread](api/beta.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}

##### [Archive Session Thread](api/beta/sessions/threads/archive.md)

$client->beta->sessions->threads->archive(string threadID, string sessionID, ?list<AnthropicBeta> betas): [ManagedAgentsSessionThread](api/beta.md)

POST/v1/sessions/{session\_id}/threads/{thread\_id}/archive

##### ModelsExpand Collapse



[ManagedAgentsSessionThread](api/beta.md)

string id

Unique identifier for this thread.

[BetaManagedAgentsSessionThreadAgent](api/beta.md) agent

Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

?\Datetime archivedAt

A timestamp in RFC 3339 format

\Datetime createdAt

A timestamp in RFC 3339 format

?string parentThreadID

Parent thread that spawned this thread. Null for the primary thread.

string sessionID

The session this thread belongs to.

?[ManagedAgentsSessionThreadStats](api/beta.md) stats

Timing statistics for a session thread.

[ManagedAgentsSessionThreadStatus](api/beta.md) status

SessionThreadStatus enum

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

?[ManagedAgentsSessionThreadUsage](api/beta.md) usage

Cumulative token usage for a session thread across all turns.



[ManagedAgentsSessionThreadStats](api/beta.md)

?float activeSeconds

Cumulative time in seconds the thread spent actively running. Excludes idle time.

?float durationSeconds

Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

?float startupSeconds

Time in seconds for the thread to begin running. Zero for child threads, which start immediately.



[ManagedAgentsSessionThreadStatus](api/beta.md)

One of the following:

"running"

"idle"

"rescheduling"

"terminated"



[ManagedAgentsSessionThreadUsage](api/beta.md)

?[BetaManagedAgentsCacheCreationUsage](api/beta.md) cacheCreation

Prompt-cache creation token usage broken down by cache lifetime.

?int cacheReadInputTokens

Total tokens read from prompt cache.

?int inputTokens

Total input tokens consumed across all turns.

?int outputTokens

Total output tokens generated across all turns.



[ManagedAgentsStreamSessionThreadEvents](api/beta.md)

One of the following:



[ManagedAgentsUserMessageEvent](api/beta.md)

string id

Unique identifier for this event.

list<Content> content

Array of content blocks comprising the user message.

Type type

?\Datetime processedAt

A timestamp in RFC 3339 format



[ManagedAgentsUserInterruptEvent](api/beta.md)

string id

Unique identifier for this event.

Type type

?\Datetime processedAt

A timestamp in RFC 3339 format

?string sessionThreadID

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



[ManagedAgentsUserToolConfirmationEvent](api/beta.md)

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

[ManagedAgentsUserCustomToolResultEvent](api/beta.md)

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

[ManagedAgentsAgentCustomToolUseEvent](api/beta.md)

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

[ManagedAgentsAgentMessageEvent](api/beta.md)

string id

Unique identifier for this event.

list<[ManagedAgentsTextBlock](api/beta.md)> content

Array of text blocks comprising the agent response.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsAgentThinkingEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsAgentMCPToolUseEvent](api/beta.md)

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

[ManagedAgentsAgentMCPToolResultEvent](api/beta.md)

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

[ManagedAgentsAgentToolUseEvent](api/beta.md)

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

[ManagedAgentsAgentToolResultEvent](api/beta.md)

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

[ManagedAgentsAgentThreadMessageReceivedEvent](api/beta.md)

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

[ManagedAgentsAgentThreadMessageSentEvent](api/beta.md)

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

[ManagedAgentsAgentThreadContextCompactedEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSessionErrorEvent](api/beta.md)

string id

Unique identifier for this event.

Error error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSessionStatusRescheduledEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSessionStatusRunningEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSessionStatusIdleEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

Type type



[ManagedAgentsSessionStatusTerminatedEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSessionThreadCreatedEvent](api/beta.md)

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

[ManagedAgentsSpanOutcomeEvaluationStartEvent](api/beta.md)

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

[ManagedAgentsSpanOutcomeEvaluationEndEvent](api/beta.md)

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

[ManagedAgentsSpanModelUsage](api/beta.md) usage

Token usage for a single model request.



[ManagedAgentsSpanModelRequestStartEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSpanModelRequestEndEvent](api/beta.md)

string id

Unique identifier for this event.

?bool isError

Whether the model request resulted in an error.

string modelRequestStartID

The id of the corresponding `span.model_request_start` event.

[ManagedAgentsSpanModelUsage](api/beta.md) modelUsage

Token usage for a single model request.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSpanOutcomeEvaluationOngoingEvent](api/beta.md)

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

[ManagedAgentsUserDefineOutcomeEvent](api/beta.md)

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

[ManagedAgentsSessionDeletedEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSessionThreadStatusRunningEvent](api/beta.md)

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

[ManagedAgentsSessionThreadStatusIdleEvent](api/beta.md)

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

[ManagedAgentsSessionThreadStatusTerminatedEvent](api/beta.md)

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

[BetaManagedAgentsUserToolResultEvent](api/beta.md)

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

[ManagedAgentsSessionThreadStatusRescheduledEvent](api/beta.md)

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

[BetaManagedAgentsSessionUpdatedEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

?[BetaManagedAgentsSessionAgent](api/beta.md) agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

?array<string,string> metadata

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

?string title

The session's new title. Present only when the update changed it.



[BetaManagedAgentsSystemMessageEvent](api/beta.md)

string id

Unique identifier for this event.

list<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks. Text-only.

Type type

?\Datetime processedAt

A timestamp in RFC 3339 format

#### ThreadsEvents

##### [List Session Thread Events](api/beta/sessions/threads/events/list.md)

$client->beta->sessions->threads->events->list(string threadID, string sessionID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsSessionEvent](api/beta.md)>

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/beta/sessions/threads/events/stream.md)

$client->beta->sessions->threads->events->stream(string threadID, string sessionID, ?list<AnthropicBeta> betas): [ManagedAgentsStreamSessionThreadEvents](api/beta.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

---

*Copyright © Anthropic. All rights reserved.*
