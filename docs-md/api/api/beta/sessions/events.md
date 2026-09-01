# Events

Copy page



cURL

# Events

##### [List Events](api/http/beta/sessions/events/list.md)

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/http/beta/sessions/events/send.md)

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/http/beta/sessions/events/stream.md)

GET/v1/sessions/{session\_id}/events/stream

##### Models



BetaManagedAgentsAgentCustomToolUseEvent object{ id, input, name, 3 more }

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

name: string

Name of the custom tool being called.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "agent.custom\_tool\_use"

session\_thread\_id: optional string or null

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.



BetaManagedAgentsAgentMCPToolResultEvent object{ id, mcp\_tool\_use\_id, processed\_at, 3 more }

Event representing the result of an MCP tool execution.



BetaManagedAgentsAgentMCPToolUseEvent object{ id, input, mcp\_server\_name, 5 more }

Event emitted when the agent invokes a tool provided by an MCP server.



BetaManagedAgentsAgentMessageEvent object{ id, content, processed\_at, type }

An agent response event in the session conversation.



BetaManagedAgentsAgentThinkingEvent object{ id, processed\_at, type }

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: string

Unique identifier for this event.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "agent.thinking"



BetaManagedAgentsAgentThreadContextCompactedEvent object{ id, processed\_at, type }

Indicates that context compaction (summarization) occurred during the session.

id: string

Unique identifier for this event.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "agent.thread\_context\_compacted"



BetaManagedAgentsAgentThreadMessageReceivedEvent object{ id, content, from\_session\_thread\_id, 3 more }

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.



BetaManagedAgentsAgentThreadMessageSentEvent object{ id, content, processed\_at, 3 more }

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.



BetaManagedAgentsAgentToolResultEvent object{ id, processed\_at, tool\_use\_id, 3 more }

Event representing the result of an agent tool execution.



BetaManagedAgentsAgentToolUseEvent object{ id, input, name, 4 more }

Event emitted when the agent invokes a built-in agent tool.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

name: string

Name of the agent tool being used.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "agent.tool\_use"



evaluated\_permission: optional "allow" or "ask" or "deny"

AgentEvaluatedPermission enum

One of the following:

"allow"

"ask"

"deny"

session\_thread\_id: optional string or null

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



BetaManagedAgentsBase64DocumentSource object{ data, media\_type, type }

Base64-encoded document data.



data: string

Base64-encoded document data.

minLength1



media\_type: string

MIME type of the document (e.g., "application/pdf").

minLength1

type: "base64"



BetaManagedAgentsBase64ImageSource object{ data, media\_type, type }

Base64-encoded image data.



data: string

Base64-encoded image data.

minLength1



media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

minLength1

type: "base64"



BetaManagedAgentsBillingError object{ message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.



BetaManagedAgentsCredentialHostUnreachableError object{ credential\_id, message, retry\_status, 2 more }

An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.



BetaManagedAgentsDocumentBlock object{ source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



BetaManagedAgentsEventParams = [BetaManagedAgentsUserMessageEventParams](api/http/beta/sessions/events.md) { content, type } or [BetaManagedAgentsUserInterruptEventParams](api/http/beta/sessions/events.md) { type, session\_thread\_id } or [BetaManagedAgentsUserToolConfirmationEventParams](api/http/beta/sessions/events.md) { result, tool\_use\_id, type, deny\_message } or 4 more

Union type for event parameters that can be sent to a session.

One of the following:



BetaManagedAgentsFileDocumentSource object{ file\_id, type }

Document referenced by file ID.



file\_id: string

ID of a previously uploaded file.

minLength1

type: "file"



BetaManagedAgentsFileImageSource object{ file\_id, type }

Image referenced by file ID.



file\_id: string

ID of a previously uploaded file.

minLength1

type: "file"



BetaManagedAgentsFileRubric object{ file\_id, type }

Rubric referenced by a file uploaded via the Files API.

file\_id: string

ID of the rubric file.

type: "file"



BetaManagedAgentsFileRubricParams object{ file\_id, type }

Rubric referenced by a file uploaded via the Files API.

file\_id: string

ID of the rubric file.

type: "file"



BetaManagedAgentsImageBlock object{ source, type }

Image content specified directly as base64 data or as a reference via a URL.



BetaManagedAgentsMCPAuthenticationFailedError object{ mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.



BetaManagedAgentsMCPConnectionFailedError object{ mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.



BetaManagedAgentsModelOverloadedError object{ message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.



BetaManagedAgentsModelRateLimitedError object{ message, retry\_status, type }

The model request was rate-limited.



BetaManagedAgentsModelRequestFailedError object{ message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.



BetaManagedAgentsPlainTextDocumentSource object{ data, media\_type, type }

Plain text document content.



data: string

The plain text content.

minLength1

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"



BetaManagedAgentsRedactedBlock object{ type }

Placeholder for content withheld by Anthropic model policy.

type: "redacted"



BetaManagedAgentsRetryStatusExhausted object{ type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"



BetaManagedAgentsRetryStatusRetrying object{ type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"



BetaManagedAgentsRetryStatusTerminal object{ type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"



BetaManagedAgentsSearchResultBlock object{ citations, content, source, 2 more }

A block containing a web search result.



citations: [BetaManagedAgentsSearchResultCitations](api/http/beta/sessions/events.md) { enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.



content: array of [BetaManagedAgentsSearchResultContent](api/http/beta/sessions/events.md) { text, type }

Array of text content blocks from the search result.



text: string

The text content.

minLength1

type: "text"



source: string

The URL source of the search result.

minLength1



title: string

The title of the search result.

minLength1

type: "search\_result"



BetaManagedAgentsSearchResultCitations object{ enabled }

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.



BetaManagedAgentsSearchResultContent object{ text, type }

Text content within a search result.



text: string

The text content.

minLength1

type: "text"



BetaManagedAgentsSendSessionEvents object{ data }

Events that were successfully sent to the session.



BetaManagedAgentsSessionBudgetReached object{ type }

The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

type: "budget\_reached"



BetaManagedAgentsSessionDeletedEvent object{ id, processed\_at, type }

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: string

Unique identifier for this event.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "session.deleted"



BetaManagedAgentsSessionEndTurn object{ type }

The agent completed its turn naturally and is ready for the next user message.

type: "end\_turn"



BetaManagedAgentsSessionErrorEvent object{ id, error, processed\_at, type }

An error event indicating a problem occurred during session execution.



BetaManagedAgentsSessionEvent = [BetaManagedAgentsUserMessageEvent](api/http/beta/sessions/events.md) { id, content, type, processed\_at } or [BetaManagedAgentsUserInterruptEvent](api/http/beta/sessions/events.md) { id, type, processed\_at, session\_thread\_id } or [BetaManagedAgentsUserToolConfirmationEvent](api/http/beta/sessions/events.md) { id, result, tool\_use\_id, 4 more } or 32 more

Union type for all event types in a session.

One of the following:



BetaManagedAgentsSessionRequiresAction object{ event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: array of string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: "requires\_action"



BetaManagedAgentsSessionRetriesExhausted object{ type }

The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

type: "retries\_exhausted"



BetaManagedAgentsSessionStatusIdleEvent object{ id, processed\_at, stop\_reason, type }

Indicates the agent has paused and is awaiting user input.



BetaManagedAgentsSessionStatusRescheduledEvent object{ id, processed\_at, type }

Indicates the session is recovering from an error state and is rescheduled for execution.

id: string

Unique identifier for this event.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "session.status\_rescheduled"



BetaManagedAgentsSessionStatusRunningEvent object{ id, processed\_at, type }

Indicates the session is actively running and the agent is working.

id: string

Unique identifier for this event.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "session.status\_running"



BetaManagedAgentsSessionStatusTerminatedEvent object{ id, processed\_at, type }

Indicates the session has terminated, either due to an error or completion.

id: string

Unique identifier for this event.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "session.status\_terminated"



BetaManagedAgentsSessionThreadCreatedEvent object{ id, agent\_name, processed\_at, 2 more }

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

id: string

Unique identifier for this event.

agent\_name: string

Name of the callable agent the thread runs.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

session\_thread\_id: string

Public `sthr_` ID of the newly created thread.

type: "session.thread\_created"



BetaManagedAgentsSessionThreadStatusIdleEvent object{ id, agent\_name, processed\_at, 3 more }

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.



BetaManagedAgentsSessionThreadStatusRescheduledEvent object{ id, agent\_name, processed\_at, 2 more }

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

session\_thread\_id: string

Public sthr\_ ID of the thread that is retrying.

type: "session.thread\_status\_rescheduled"



BetaManagedAgentsSessionThreadStatusRunningEvent object{ id, agent\_name, processed\_at, 2 more }

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

session\_thread\_id: string

Public sthr\_ ID of the thread that started running.

type: "session.thread\_status\_running"



BetaManagedAgentsSessionThreadStatusTerminatedEvent object{ id, agent\_name, processed\_at, 2 more }

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

session\_thread\_id: string

Public sthr\_ ID of the thread that terminated.

type: "session.thread\_status\_terminated"



BetaManagedAgentsSessionUsageSnapshot object{ active\_seconds, cache\_creation, cache\_read\_input\_tokens, 4 more }

Point-in-time snapshot of a session's cumulative usage.



BetaManagedAgentsSpanModelRequestEndEvent object{ id, is\_error, model\_request\_start\_id, 3 more }

Emitted when a model request completes.



BetaManagedAgentsSpanModelRequestStartEvent object{ id, processed\_at, type }

Emitted when a model request is initiated by the agent.

id: string

Unique identifier for this event.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "span.model\_request\_start"



BetaManagedAgentsSpanModelUsage object{ cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.



cache\_creation\_input\_tokens: number

Tokens used to create prompt cache in this request.

formatint32



cache\_read\_input\_tokens: number

Tokens read from prompt cache in this request.

formatint32



input\_tokens: number

Input tokens consumed by this request.

formatint32



output\_tokens: number

Output tokens generated by this request.

formatint32



speed: optional "standard" or "fast" or null

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"



BetaManagedAgentsSpanOutcomeEvaluationEndEvent object{ id, explanation, iteration, 6 more }

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.



BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent object{ id, iteration, outcome\_id, 2 more }

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

id: string

Unique identifier for this event.



iteration: number

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

formatint32

outcome\_id: string

The `outc_` ID of the outcome being evaluated.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "span.outcome\_evaluation\_ongoing"



BetaManagedAgentsSpanOutcomeEvaluationStartEvent object{ id, iteration, outcome\_id, 2 more }

Emitted when an outcome evaluation cycle begins.

id: string

Unique identifier for this event.



iteration: number

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

formatint32

outcome\_id: string

The `outc_` ID of the outcome being evaluated.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "span.outcome\_evaluation\_start"



BetaManagedAgentsStreamSessionEvents = [BetaManagedAgentsUserMessageEvent](api/http/beta/sessions/events.md) { id, content, type, processed\_at } or [BetaManagedAgentsUserInterruptEvent](api/http/beta/sessions/events.md) { id, type, processed\_at, session\_thread\_id } or [BetaManagedAgentsUserToolConfirmationEvent](api/http/beta/sessions/events.md) { id, result, tool\_use\_id, 4 more } or 34 more

Server-sent event in the session stream.

One of the following:



BetaManagedAgentsSystemMessageEventParams object{ content, type }

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.



content: array of [BetaManagedAgentsSystemContentBlock](api/http/beta/sessions.md) { text, type }

System content blocks to append. Text-only.



text: string

The text content.

minLength1

type: "text"

type: "system.message"



BetaManagedAgentsTextBlock object{ text, type }

Regular text content.



text: string

The text content.

minLength1

type: "text"



BetaManagedAgentsTextRubric object{ content, type }

Rubric content provided inline as text.

content: string

Rubric content. Plain text or markdown — the grader treats it as freeform text.

type: "text"



BetaManagedAgentsTextRubricParams object{ content, type }

Rubric content provided inline as text.



content: string

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

maxLength262144

type: "text"



BetaManagedAgentsUnknownError object{ message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.



BetaManagedAgentsURLDocumentSource object{ type, url }

Document referenced by URL.

type: "url"



url: string

URL of the document to fetch.

minLength1



BetaManagedAgentsURLImageSource object{ type, url }

Image referenced by URL.

type: "url"



url: string

URL of the image to fetch.

minLength1



BetaManagedAgentsUserCustomToolResultEvent object{ id, custom\_tool\_use\_id, type, 4 more }

Event sent by the client providing the result of a custom tool execution.



BetaManagedAgentsUserCustomToolResultEventParams object{ custom\_tool\_use\_id, type, content, is\_error }

Parameters for providing the result of a custom tool execution.



BetaManagedAgentsUserDefineOutcomeEvent object{ id, description, max\_iterations, 4 more }

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.



BetaManagedAgentsUserDefineOutcomeEventParams object{ description, rubric, type, max\_iterations }

Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.



BetaManagedAgentsUserInterruptEvent object{ id, type, processed\_at, session\_thread\_id }

An interrupt event that pauses agent execution and returns control to the user.

id: string

Unique identifier for this event.

type: "user.interrupt"



processed\_at: optional string or null

A timestamp in RFC 3339 format

formatdate-time

session\_thread\_id: optional string or null

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



BetaManagedAgentsUserInterruptEventParams object{ type, session\_thread\_id }

Parameters for sending an interrupt to pause the agent.

type: "user.interrupt"

session\_thread\_id: optional string or null

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



BetaManagedAgentsUserMessageEvent object{ id, content, type, processed\_at }

A user message event in the session conversation.



BetaManagedAgentsUserMessageEventParams object{ content, type }

Parameters for sending a user message to the session.



BetaManagedAgentsUserToolConfirmationEvent object{ id, result, tool\_use\_id, 4 more }

A tool confirmation event that approves or denies a pending tool execution.



BetaManagedAgentsUserToolConfirmationEventParams object{ result, tool\_use\_id, type, deny\_message }

Parameters for confirming or denying a tool execution request.



result: "allow" or "deny"

UserToolConfirmationResult enum

One of the following:

"allow"

"deny"



tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

minLength1

maxLength128

type: "user.tool\_confirmation"



deny\_message: optional string or null

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

maxLength10000



BetaManagedAgentsUserToolResultEventParams object{ tool\_use\_id, type, content, is\_error }

Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

---

*Copyright © Anthropic. All rights reserved.*
