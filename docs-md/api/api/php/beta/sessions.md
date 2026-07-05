# Sessions

Copy page



PHP

# Sessions

##### [Create Session](api/beta/sessions/create.md)

$client->beta->sessions->create([Agent](api/beta/sessions/create.md) agent, string environmentID, ?array<string,string> metadata, ?list<Resource> resources, ?string title, ?list<string> vaultIDs, ?list<AnthropicBeta> betas): [BetaManagedAgentsSession](api/beta/sessions.md)

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

$client->beta->sessions->list(?string agentID, ?int agentVersion, ?\Datetime createdAtGt, ?\Datetime createdAtGte, ?\Datetime createdAtLt, ?\Datetime createdAtLte, ?string deploymentID, ?bool includeArchived, ?int limit, ?string memoryStoreID, ?[Order](api/beta/sessions/list.md) order, ?string page, ?list<Status> statuses, ?list<AnthropicBeta> betas): BidirectionalPageCursor<[BetaManagedAgentsSession](api/beta/sessions.md)>

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

$client->beta->sessions->retrieve(string sessionID, ?list<AnthropicBeta> betas): [BetaManagedAgentsSession](api/beta/sessions.md)

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

$client->beta->sessions->update(string sessionID, ?[BetaManagedAgentsSessionAgentUpdate](api/beta/sessions.md) agent, ?array<string,string> metadata, ?string title, ?list<string> vaultIDs, ?list<AnthropicBeta> betas): [BetaManagedAgentsSession](api/beta/sessions.md)

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

$client->beta->sessions->delete(string sessionID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeletedSession](api/beta/sessions.md)

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

$client->beta->sessions->archive(string sessionID, ?list<AnthropicBeta> betas): [BetaManagedAgentsSession](api/beta/sessions.md)

POST/v1/sessions/{session\_id}/archive

##### ModelsExpand Collapse



[BetaManagedAgentsAgentMessagePreview](api/beta/sessions.md)

string id

The id the buffered agent.message will carry if it is emitted. Matches the event\_id on this preview's event\_delta events.

Type type



[BetaManagedAgentsAgentParams](api/beta/sessions.md)

string id

The `agent` ID.

Type type

?int version

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.



[BetaManagedAgentsAgentThinkingPreview](api/beta/sessions.md)

string id

The id the buffered agent.thinking will carry if it is emitted. Start-only — no event\_delta events follow.

Type type



[BetaManagedAgentsAgentWithOverridesParams](api/beta/sessions.md)

string id

The `agent` ID.

Type type

?list<[BetaManagedAgentsURLMCPServerParams](api/beta/agents.md)> mcpServers

Replacement MCP server list. Full replacement: the provided array becomes the MCP servers. Send an empty array to clear; omit to preserve the agent's servers.

?Model model

Replacement model. Accepts the model string, e.g. `claude-opus-4-6`, or a `model_config` object. Omit to use the agent's model.

?list<[BetaManagedAgentsSkillParams](api/beta/agents.md)> skills

Replacement skill list. Full replacement: the provided array becomes the skills. Send an empty array to clear; omit to preserve the agent's skills.

?string system

Replacement system prompt. Up to 100,000 characters. Set to null to clear the agent's system prompt; omit to preserve it.

?list<Tool> tools

Replacement tool list. Full replacement: the provided array becomes the tool configuration. Send an empty array to clear; omit to preserve the agent's tools.

?int version

The specific `agent` version to use. Omit to use the latest version.



[BetaManagedAgentsBranchCheckout](api/beta/sessions.md)

string name

Branch name to check out.

Type type



[BetaManagedAgentsCacheCreationUsage](api/beta/sessions.md)

?int ephemeral1hInputTokens

Tokens used to create 1-hour ephemeral cache entries.

?int ephemeral5mInputTokens

Tokens used to create 5-minute ephemeral cache entries.



[BetaManagedAgentsCommitCheckout](api/beta/sessions.md)

string sha

Full commit SHA to check out.

Type type



[BetaManagedAgentsDeletedSession](api/beta/sessions.md)

string id

Type type



[BetaManagedAgentsDeltaContent](api/beta/sessions.md)

[ManagedAgentsTextBlock](api/beta/sessions/events.md) content

Regular text content.

Type type

?int index

Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.



[BetaManagedAgentsDeltaEvent](api/beta/sessions.md)

[BetaManagedAgentsDeltaContent](api/beta/sessions.md) delta

One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content\_delta fragments, each a partial element of the content array.

string eventID

The id of the event being previewed. Matches event.id on the corresponding event\_start and the buffered event that reconciles the preview.

Type type



[BetaManagedAgentsDeltaType](api/beta/sessions.md)

One of the following:

"agent.message"

"agent.thinking"



[BetaManagedAgentsFileResourceParams](api/beta/sessions.md)

string fileID

ID of a previously uploaded file.

Type type

?string mountPath

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.



[BetaManagedAgentsGitHubRepositoryResourceParams](api/beta/sessions.md)

string authorizationToken

GitHub authorization token used to clone the repository.

Type type

string url

Github URL of the repository

?Checkout checkout

Branch or commit to check out. Defaults to the repository's default branch.

?string mountPath

Mount path in the container. Defaults to `/workspace/<repo-name>`.



[BetaManagedAgentsMemoryStoreResourceParam](api/beta/sessions.md)

string memoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type type

?Access access

Access mode for an attached memory store.

?string instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.



[BetaManagedAgentsMultiagent](api/beta/sessions.md)

list<[BetaManagedAgentsAgentReference](api/beta/agents.md)> agents

Agents the coordinator may spawn as session threads, each resolved to a specific version.

Type type



[BetaManagedAgentsMultiagentParams](api/beta/sessions.md)

list<[BetaManagedAgentsMultiagentRosterEntryParams](api/beta/sessions.md)> agents

Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

Type type



[BetaManagedAgentsMultiagentRosterEntryParams](api/beta/sessions.md)

One of the following:

string



[BetaManagedAgentsAgentParams](api/beta/sessions.md)

string id

The `agent` ID.

Type type

?int version

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.



[BetaManagedAgentsMultiagentSelfParams](api/beta/agents.md)

Type type



[BetaManagedAgentsOutcomeEvaluationResource](api/beta/sessions.md)

?\Datetime completedAt

A timestamp in RFC 3339 format

string description

What the agent should produce.

?string explanation

Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs\_revision (intermediate), what's missing; for failed, why unrecoverable.

int iteration

0-indexed revision cycle the outcome is currently on.

string outcomeID

Server-generated outc\_ ID for this outcome.

string result

Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

Type type



[BetaManagedAgentsSession](api/beta/sessions.md)

string id

[BetaManagedAgentsSessionAgent](api/beta/sessions.md) agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

?\Datetime archivedAt

A timestamp in RFC 3339 format

\Datetime createdAt

A timestamp in RFC 3339 format

string environmentID

array<string,string> metadata

list<[BetaManagedAgentsOutcomeEvaluationResource](api/beta/sessions.md)> outcomeEvaluations

Per-outcome evaluation state. One entry per define\_outcome event sent to the session.

list<[ManagedAgentsSessionResource](api/beta/sessions/resources.md)> resources

[BetaManagedAgentsSessionStats](api/beta/sessions.md) stats

Timing statistics for a session.

Status status

SessionStatus enum

?string title

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

[BetaManagedAgentsSessionUsage](api/beta/sessions.md) usage

Cumulative token usage for a session across all turns.

list<string> vaultIDs

Vault IDs attached to the session at creation. Empty when no vaults were supplied.

?string deploymentID

Deployment ID when the session was created from a deployment reference. Null otherwise.



[BetaManagedAgentsSessionAgent](api/beta/sessions.md)

string id

?string description

list<[BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md)> mcpServers

[BetaManagedAgentsModelConfig](api/beta/agents.md) model

Model identifier and configuration.

?[BetaManagedAgentsSessionMultiagentCoordinator](api/beta/sessions.md) multiagent

Resolved coordinator topology with full agent definitions for each roster member.

string name

list<Skill> skills

?string system

list<Tool> tools

Type type

int version



[BetaManagedAgentsSessionAgentUpdate](api/beta/sessions.md)

?list<[BetaManagedAgentsURLMCPServerParams](api/beta/agents.md)> mcpServers

Replacement MCP server list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

?list<Tool> tools

Replacement tool list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.



[BetaManagedAgentsSessionMultiagentCoordinator](api/beta/sessions.md)

list<[BetaManagedAgentsSessionThreadAgent](api/beta/agents.md)> agents

Full `agent` definitions the coordinator may spawn as session threads.

Type type



[BetaManagedAgentsSessionStats](api/beta/sessions.md)

?float activeSeconds

Cumulative time in seconds the session spent in running status. Excludes idle time.

?float durationSeconds

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

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

[BetaManagedAgentsSessionUsage](api/beta/sessions.md)

?[BetaManagedAgentsCacheCreationUsage](api/beta/sessions.md) cacheCreation

Prompt-cache creation token usage broken down by cache lifetime.

?int cacheReadInputTokens

Total tokens read from prompt cache.

?int inputTokens

Total input tokens consumed across all turns.

?int outputTokens

Total output tokens generated across all turns.



[BetaManagedAgentsStartEvent](api/beta/sessions.md)

[BetaManagedAgentsStartEventPreview](api/beta/sessions.md) event

The previewed event's type and id. The event type determines which delta types the preview's event\_delta events carry: agent.message events stream content\_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

Type type



[BetaManagedAgentsStartEventPreview](api/beta/sessions.md)

One of the following:



[BetaManagedAgentsAgentMessagePreview](api/beta/sessions.md)

string id

The id the buffered agent.message will carry if it is emitted. Matches the event\_id on this preview's event\_delta events.

Type type



[BetaManagedAgentsAgentThinkingPreview](api/beta/sessions.md)

string id

The id the buffered agent.thinking will carry if it is emitted. Start-only — no event\_delta events follow.

Type type



[BetaManagedAgentsSystemContentBlock](api/beta/sessions.md)

string text

The text content.

Type type

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

#### SessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

$client->beta->sessions->events->list(string sessionID, ?\Datetime createdAtGt, ?\Datetime createdAtGte, ?\Datetime createdAtLt, ?\Datetime createdAtLte, ?int limit, ?[Order](api/beta/sessions/events/list.md) order, ?string page, ?list<string> types, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsSessionEvent](api/beta/sessions/events.md)>

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

$client->beta->sessions->events->send(string sessionID, list<[ManagedAgentsEventParams](api/beta/sessions/events.md)> events, ?list<AnthropicBeta> betas): [ManagedAgentsSendSessionEvents](api/beta/sessions/events.md)

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

$client->beta->sessions->events->stream(string sessionID, ?list<[BetaManagedAgentsDeltaType](api/beta/sessions.md)> eventDeltas, ?list<AnthropicBeta> betas): [ManagedAgentsStreamSessionEvents](api/beta/sessions/events.md)

GET/v1/sessions/{session\_id}/events/stream

#### SessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

$client->beta->sessions->resources->add(string sessionID, string fileID, [Type](api/beta/sessions/resources/add.md) type, ?string mountPath, ?list<AnthropicBeta> betas): [ManagedAgentsFileResource](api/beta/sessions/resources.md)

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

$client->beta->sessions->resources->list(string sessionID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsSessionResource](api/beta/sessions/resources.md)>

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

$client->beta->sessions->resources->retrieve(string resourceID, string sessionID, ?list<AnthropicBeta> betas): [ResourceGetResponse](api/beta/sessions/resources.md)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

$client->beta->sessions->resources->update(string resourceID, string sessionID, string authorizationToken, ?list<AnthropicBeta> betas): [ResourceUpdateResponse](api/beta/sessions/resources.md)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

$client->beta->sessions->resources->delete(string resourceID, string sessionID, ?list<AnthropicBeta> betas): [ManagedAgentsDeleteSessionResource](api/beta/sessions/resources.md)

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

#### SessionsThreads

##### [List Session Threads](api/beta/sessions/threads/list.md)

$client->beta->sessions->threads->list(string sessionID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsSessionThread](api/beta/sessions/threads.md)>

GET/v1/sessions/{session\_id}/threads

##### [Get Session Thread](api/beta/sessions/threads/retrieve.md)

$client->beta->sessions->threads->retrieve(string threadID, string sessionID, ?list<AnthropicBeta> betas): [ManagedAgentsSessionThread](api/beta/sessions/threads.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}

##### [Archive Session Thread](api/beta/sessions/threads/archive.md)

$client->beta->sessions->threads->archive(string threadID, string sessionID, ?list<AnthropicBeta> betas): [ManagedAgentsSessionThread](api/beta/sessions/threads.md)

POST/v1/sessions/{session\_id}/threads/{thread\_id}/archive

#### SessionsThreadsEvents

##### [List Session Thread Events](api/beta/sessions/threads/events/list.md)

$client->beta->sessions->threads->events->list(string threadID, string sessionID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsSessionEvent](api/beta/sessions/events.md)>

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/beta/sessions/threads/events/stream.md)

$client->beta->sessions->threads->events->stream(string threadID, string sessionID, ?list<AnthropicBeta> betas): [ManagedAgentsStreamSessionThreadEvents](api/beta/sessions/threads.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

---

*Copyright © Anthropic. All rights reserved.*
