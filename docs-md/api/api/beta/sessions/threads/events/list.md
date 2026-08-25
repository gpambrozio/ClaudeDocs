# List Session Thread Events

Copy page



cURL

# List Session Thread Events

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

List Session Thread Events

##### Path parameters

session\_id: string

thread\_id: string

##### Query parameters



limit: optional number

Query parameter for limit

formatint32

page: optional string

Query parameter for page

##### Headers



"anthropic-beta": optional array of [AnthropicBeta](api/http/beta.md)

Optional header to specify the beta version(s) you want to use.

One of the following:

string



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 31 more

One of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"user-profiles-2026-08-18"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"dreaming-2026-04-21"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"server-side-fallback-2026-07-01"

"fallback-credit-2026-06-01"

"fallback-credit-2026-07-01"

"agent-memory-2026-07-22"

"mid-conversation-tool-changes-2026-07-01"

##### Returns



data: optional array of [BetaManagedAgentsSessionEvent](api/http/beta/sessions/events.md)

Events for the thread, ordered by `processed_at`.

One of the following:



BetaManagedAgentsUserMessageEvent object{ id, content, type, processed\_at }

A user message event in the session conversation.



BetaManagedAgentsUserInterruptEvent object{ id, type, processed\_at, session\_thread\_id }

An interrupt event that pauses agent execution and returns control to the user.

id: string

Unique identifier for this event.

type: "user.interrupt"



processed\_at: optional string or null

A timestamp in RFC 3339 format

formatdate-time

session\_thread\_id: optional string or null

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



BetaManagedAgentsUserToolConfirmationEvent object{ id, result, tool\_use\_id, 4 more }

A tool confirmation event that approves or denies a pending tool execution.



BetaManagedAgentsUserCustomToolResultEvent object{ id, custom\_tool\_use\_id, type, 4 more }

Event sent by the client providing the result of a custom tool execution.



BetaManagedAgentsAgentCustomToolUseEvent object{ id, input, name, 3 more }

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

name: string

Name of the custom tool being called.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "agent.custom\_tool\_use"

session\_thread\_id: optional string or null

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.



BetaManagedAgentsAgentMessageEvent object{ id, content, processed\_at, type }

An agent response event in the session conversation.



BetaManagedAgentsAgentThinkingEvent object{ id, processed\_at, type }

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: string

Unique identifier for this event.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "agent.thinking"



BetaManagedAgentsAgentMCPToolUseEvent object{ id, input, mcp\_server\_name, 5 more }

Event emitted when the agent invokes a tool provided by an MCP server.



BetaManagedAgentsAgentMCPToolResultEvent object{ id, mcp\_tool\_use\_id, processed\_at, 3 more }

Event representing the result of an MCP tool execution.



BetaManagedAgentsAgentToolUseEvent object{ id, input, name, 4 more }

Event emitted when the agent invokes a built-in agent tool.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

name: string

Name of the agent tool being used.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "agent.tool\_use"



evaluated\_permission: optional "allow" or "ask" or "deny"

AgentEvaluatedPermission enum

One of the following:

"allow"

"ask"

"deny"

session\_thread\_id: optional string or null

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



BetaManagedAgentsAgentToolResultEvent object{ id, processed\_at, tool\_use\_id, 3 more }

Event representing the result of an agent tool execution.



BetaManagedAgentsAgentThreadMessageReceivedEvent object{ id, content, from\_session\_thread\_id, 3 more }

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.



BetaManagedAgentsAgentThreadMessageSentEvent object{ id, content, processed\_at, 3 more }

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.



BetaManagedAgentsAgentThreadContextCompactedEvent object{ id, processed\_at, type }

Indicates that context compaction (summarization) occurred during the session.

id: string

Unique identifier for this event.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "agent.thread\_context\_compacted"



BetaManagedAgentsSessionErrorEvent object{ id, error, processed\_at, type }

An error event indicating a problem occurred during session execution.



BetaManagedAgentsSessionStatusRescheduledEvent object{ id, processed\_at, type }

Indicates the session is recovering from an error state and is rescheduled for execution.

id: string

Unique identifier for this event.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "session.status\_rescheduled"



BetaManagedAgentsSessionStatusRunningEvent object{ id, processed\_at, type }

Indicates the session is actively running and the agent is working.

id: string

Unique identifier for this event.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "session.status\_running"



BetaManagedAgentsSessionStatusIdleEvent object{ id, processed\_at, stop\_reason, type }

Indicates the agent has paused and is awaiting user input.



BetaManagedAgentsSessionStatusTerminatedEvent object{ id, processed\_at, type }

Indicates the session has terminated, either due to an error or completion.

id: string

Unique identifier for this event.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "session.status\_terminated"



BetaManagedAgentsSessionThreadCreatedEvent object{ id, agent\_name, processed\_at, 2 more }

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

id: string

Unique identifier for this event.

agent\_name: string

Name of the callable agent the thread runs.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

session\_thread\_id: string

Public `sthr_` ID of the newly created thread.

type: "session.thread\_created"



BetaManagedAgentsSpanOutcomeEvaluationStartEvent object{ id, iteration, outcome\_id, 2 more }

Emitted when an outcome evaluation cycle begins.

id: string

Unique identifier for this event.



iteration: number

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

formatint32

outcome\_id: string

The `outc_` ID of the outcome being evaluated.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "span.outcome\_evaluation\_start"



BetaManagedAgentsSpanOutcomeEvaluationEndEvent object{ id, explanation, iteration, 6 more }

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.



BetaManagedAgentsSpanModelRequestStartEvent object{ id, processed\_at, type }

Emitted when a model request is initiated by the agent.

id: string

Unique identifier for this event.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "span.model\_request\_start"



BetaManagedAgentsSpanModelRequestEndEvent object{ id, is\_error, model\_request\_start\_id, 3 more }

Emitted when a model request completes.



BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent object{ id, iteration, outcome\_id, 2 more }

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

id: string

Unique identifier for this event.



iteration: number

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

formatint32

outcome\_id: string

The `outc_` ID of the outcome being evaluated.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "span.outcome\_evaluation\_ongoing"



BetaManagedAgentsUserDefineOutcomeEvent object{ id, description, max\_iterations, 4 more }

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.



BetaManagedAgentsSessionDeletedEvent object{ id, processed\_at, type }

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: string

Unique identifier for this event.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "session.deleted"



BetaManagedAgentsSessionThreadStatusRunningEvent object{ id, agent\_name, processed\_at, 2 more }

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

session\_thread\_id: string

Public sthr\_ ID of the thread that started running.

type: "session.thread\_status\_running"



BetaManagedAgentsSessionThreadStatusIdleEvent object{ id, agent\_name, processed\_at, 3 more }

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.



BetaManagedAgentsSessionThreadStatusTerminatedEvent object{ id, agent\_name, processed\_at, 2 more }

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

session\_thread\_id: string

Public sthr\_ ID of the thread that terminated.

type: "session.thread\_status\_terminated"



BetaManagedAgentsUserToolResultEvent object{ id, tool\_use\_id, type, 4 more }

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.



BetaManagedAgentsSessionThreadStatusRescheduledEvent object{ id, agent\_name, processed\_at, 2 more }

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: string

Unique identifier for this event.

agent\_name: string

Name of the agent the thread runs.



processed\_at: string

A timestamp in RFC 3339 format

formatdate-time

session\_thread\_id: string

Public sthr\_ ID of the thread that is retrying.

type: "session.thread\_status\_rescheduled"



BetaManagedAgentsSessionUpdatedEvent object{ id, processed\_at, type, 4 more }

Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.



BetaManagedAgentsSystemMessageEvent object{ id, content, type, processed\_at }

A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

id: string

Unique identifier for this event.



content: array of [BetaManagedAgentsSystemContentBlock](api/http/beta/sessions.md) { text, type }

System content blocks. Text-only.



text: string

The text content.

minLength1

type: "text"

type: "system.message"



processed\_at: optional string or null

A timestamp in RFC 3339 format

formatdate-time



BetaManagedAgentsSessionUsageEvent object{ id, processed\_at, type, 2 more }

Periodic snapshot of the session's cumulative usage and tracked list cost.

next\_page: optional string or null

Opaque cursor for the next page. Null when no more results.

### List Session Thread Events

cURL



```shiki
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/threads/$THREAD_ID/events \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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
