# List Session Thread Events

Copy page



PHP

# List Session Thread Events

$client->beta->sessions->threads->events->list(string threadID, string sessionID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsSessionEvent](api/beta.md)>

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

List Session Thread Events

##### ParametersExpand Collapse

sessionID: string

threadID: string

limit?:optional int

Query parameter for limit

page?:optional string

Query parameter for page

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



[ManagedAgentsSessionEvent](api/beta.md)

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

List Session Thread Events

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->sessions->threads->events->list(
  'sthr_011CZkZVWa6oIjw0rgXZpnBt',
  sessionID: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  limit: 0,
  page: 'page',
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
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
