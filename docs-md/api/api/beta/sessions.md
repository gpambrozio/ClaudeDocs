# Sessions

Copy page



cURL

# Sessions

##### [Create Session](api/http/beta/sessions/create.md)

POST/v1/sessions

##### [List Sessions](api/http/beta/sessions/list.md)

GET/v1/sessions

##### [Get Session](api/http/beta/sessions/retrieve.md)

GET/v1/sessions/{session\_id}

##### [Update Session](api/http/beta/sessions/update.md)

POST/v1/sessions/{session\_id}

##### [Delete Session](api/http/beta/sessions/delete.md)

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/http/beta/sessions/archive.md)

POST/v1/sessions/{session\_id}/archive

##### Models



BetaManagedAgentsAdvisorParams object{ model, type }

Platform advisor roster entry: a model the session's primary thread may consult mid-turn. At most one per roster; the entry occupies the roster name `anthropic.advisor`.



model: string

A Claude model id. The model must be permitted as an advisor for this agent's model — see the sessions/threads/advisor spec.

minLength1

maxLength256

type: "advisor"



BetaManagedAgentsAgentMessagePreview object{ id, type }

id: string

The id the buffered agent.message will carry if it is emitted. Matches the event\_id on this preview's event\_delta events.

type: "agent.message"



BetaManagedAgentsAgentParams object{ id, type, version }

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version



id: string

The `agent` ID.

minLength1

maxLength128

type: "agent"



version: optional number

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

formatint32



BetaManagedAgentsAgentThinkingPreview object{ id, type }

id: string

The id the buffered agent.thinking will carry if it is emitted. Start-only — no event\_delta events follow.

type: "agent.thinking"



BetaManagedAgentsAgentWithOverridesParams object{ id, type, mcp\_servers, 5 more }

Reference to an `agent` plus optional configuration overrides. Each provided field replaces the agent's value for the caller's use; the agent resource is unchanged.



BetaManagedAgentsBranchCheckout object{ name, type }



name: string

Branch name to check out.

minLength1

maxLength255

type: "branch"



BetaManagedAgentsBudgetLimit object{ max\_list\_cost, type }

A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.



max\_list\_cost: [BetaMonetaryAmount](api/http/beta.md) { amount, currency }

A monetary amount in a specific currency.

amount: string

Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

currency: [BetaCurrency](api/http/beta.md)

Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

type: "limit"



BetaManagedAgentsCacheCreationUsage object{ ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Prompt-cache creation token usage broken down by cache lifetime.



ephemeral\_1h\_input\_tokens: optional number

Tokens used to create 1-hour ephemeral cache entries.

formatint32



ephemeral\_5m\_input\_tokens: optional number

Tokens used to create 5-minute ephemeral cache entries.

formatint32



BetaManagedAgentsCommitCheckout object{ sha, type }



sha: string

Full commit SHA to check out.

minLength7

maxLength64

type: "commit"



BetaManagedAgentsDeletedSession object{ id, type }

Confirmation that a `session` has been permanently deleted.

id: string

type: "session\_deleted"



BetaManagedAgentsDeltaContent object{ content, type, index }



content: [BetaManagedAgentsTextBlock](api/http/beta/sessions/events.md) { text, type }

Regular text content.



text: string

The text content.

minLength1

type: "text"

type: "content\_delta"



index: optional number

Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

formatuint32



BetaManagedAgentsDeltaEvent object{ delta, event\_id, type }

An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event\_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model\_request\_end closes the preview. Only sent on stream connections that opt in via event\_deltas; never appears in event history.



BetaManagedAgentsDeltaType = "agent.message" or "agent.thinking"

EventDeltaType enum

One of the following:

"agent.message"

"agent.thinking"



BetaManagedAgentsFileResourceParams object{ file\_id, type, mount\_path }

Mount a file uploaded via the Files API into the session.



file\_id: string

ID of a previously uploaded file.

minLength1

maxLength128

type: "file"



mount\_path: optional string or null

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

minLength1

maxLength4096



BetaManagedAgentsGitHubRepositoryResourceParams object{ authorization\_token, type, url, 2 more }

Mount a GitHub repository into the session's container.



BetaManagedAgentsMemoryStoreResourceParam object{ memory\_store\_id, type, access, instructions }

Parameters for attaching a memory store to an agent session.

memory\_store\_id: string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: "memory\_store"



access: optional "read\_write" or "read\_only" or null

Access mode for an attached memory store.

One of the following:

"read\_write"

"read\_only"



instructions: optional string or null

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

maxLength4096



BetaManagedAgentsMultiagent object{ agents, type }

Resolved coordinator topology with a concrete agent roster.



BetaManagedAgentsMultiagentParams object{ agents, type }

A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.



BetaManagedAgentsMultiagentRosterEntryParams = string or [BetaManagedAgentsAgentParams](api/http/beta/sessions.md) { id, type, version } or [BetaManagedAgentsMultiagentSelfParams](api/http/beta/agents.md) { type } or [BetaManagedAgentsAdvisorParams](api/http/beta/sessions.md) { model, type }

An entry in a multiagent roster: an agent ID string, a versioned agent reference, or `self`.

One of the following:



BetaManagedAgentsOutcomeEvaluationResource object{ completed\_at, description, explanation, 4 more }

Evaluation state for a single outcome defined via a define\_outcome event.



completed\_at: string or null

A timestamp in RFC 3339 format

formatdate-time

description: string

What the agent should produce.

explanation: string or null

Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs\_revision (intermediate), what's missing; for failed, why unrecoverable.



iteration: number

0-indexed revision cycle the outcome is currently on.

formatint32

outcome\_id: string

Server-generated outc\_ ID for this outcome.

result: string

Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

type: "outcome\_evaluation"



BetaManagedAgentsServerToolUsage object{ web\_fetch\_requests, web\_search\_requests }

Cumulative count of server-executed tool invocations, broken down by tool.



web\_fetch\_requests: optional number

Number of server-executed web fetch requests.

formatint32



web\_search\_requests: optional number

Number of server-executed web search requests.

formatint32



BetaManagedAgentsSession object{ id, agent, archived\_at, 14 more }

A Managed Agents `session`.



BetaManagedAgentsSessionAgent object{ id, description, mcp\_servers, 8 more }

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.



BetaManagedAgentsSessionAgentUpdate object{ mcp\_servers, tools }

Mid-session agent configuration update. Only `tools` and `mcp_servers` are updatable. Full replacement: the provided array becomes the new value. To preserve existing entries, GET the session, modify the array, and POST it back.



BetaManagedAgentsSessionMultiagentCoordinator object{ agents, type }

Resolved coordinator topology with full agent definitions for each roster member.



BetaManagedAgentsSessionStats object{ active\_seconds, duration\_seconds }

Timing statistics for a session.



active\_seconds: optional number

Cumulative time in seconds the session spent in running status. Excludes idle time.

formatdouble



duration\_seconds: optional number

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

formatdouble



BetaManagedAgentsSessionUpdatedEvent object{ id, processed\_at, type, 4 more }

Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.



BetaManagedAgentsSessionUsage object{ active\_seconds, cache\_creation, cache\_read\_input\_tokens, 4 more }

Cumulative token usage for a session across all turns.



BetaManagedAgentsSessionUsageEvent object{ id, processed\_at, type, 2 more }

Periodic snapshot of the session's cumulative usage and tracked list cost.



BetaManagedAgentsStartEvent object{ event, type }

Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event\_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model\_request\_end closes the preview. Only sent on stream connections that opt in via event\_deltas; never appears in event history.



event: [BetaManagedAgentsStartEventPreview](api/http/beta/sessions.md)

The previewed event's type and id. The event type determines which delta types the preview's event\_delta events carry: agent.message events stream content\_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

One of the following:



BetaManagedAgentsAgentMessagePreview object{ id, type }

id: string

The id the buffered agent.message will carry if it is emitted. Matches the event\_id on this preview's event\_delta events.

type: "agent.message"



BetaManagedAgentsAgentThinkingPreview object{ id, type }

id: string

The id the buffered agent.thinking will carry if it is emitted. Start-only — no event\_delta events follow.

type: "agent.thinking"

type: "event\_start"



BetaManagedAgentsStartEventPreview = [BetaManagedAgentsAgentMessagePreview](api/http/beta/sessions.md) { id, type } or [BetaManagedAgentsAgentThinkingPreview](api/http/beta/sessions.md) { id, type }

One of the following:



BetaManagedAgentsAgentMessagePreview object{ id, type }

id: string

The id the buffered agent.message will carry if it is emitted. Matches the event\_id on this preview's event\_delta events.

type: "agent.message"



BetaManagedAgentsAgentThinkingPreview object{ id, type }

id: string

The id the buffered agent.thinking will carry if it is emitted. Start-only — no event\_delta events follow.

type: "agent.thinking"



BetaManagedAgentsSystemContentBlock object{ text, type }

Regular text content.



text: string

The text content.

minLength1

type: "text"

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

BetaManagedAgentsUserToolResultEvent object{ id, tool\_use\_id, type, 4 more }

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

#### Sessions[Events](api/http/beta/sessions/events.md)

##### [List Events](api/http/beta/sessions/events/list.md)

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/http/beta/sessions/events/send.md)

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/http/beta/sessions/events/stream.md)

GET/v1/sessions/{session\_id}/events/stream

#### Sessions[Resources](api/http/beta/sessions/resources.md)

##### [Add Session Resource](api/http/beta/sessions/resources/add.md)

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/http/beta/sessions/resources/list.md)

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/http/beta/sessions/resources/retrieve.md)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/http/beta/sessions/resources/update.md)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/http/beta/sessions/resources/delete.md)

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

#### Sessions[Threads](api/http/beta/sessions/threads.md)

##### [List Session Threads](api/http/beta/sessions/threads/list.md)

GET/v1/sessions/{session\_id}/threads

##### [Get Session Thread](api/http/beta/sessions/threads/retrieve.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}

##### [Archive Session Thread](api/http/beta/sessions/threads/archive.md)

POST/v1/sessions/{session\_id}/threads/{thread\_id}/archive

#### SessionsThreads[Events](api/http/beta/sessions/threads/events.md)

##### [List Session Thread Events](api/http/beta/sessions/threads/events/list.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/http/beta/sessions/threads/events/stream.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

---

*Copyright © Anthropic. All rights reserved.*
