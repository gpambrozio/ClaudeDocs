# Sessions

Copy page

SDK language

PHP

# Sessions

##### [Create Session](api/beta/sessions/create.md)

$client->beta->sessions->create([Agent](api/beta/sessions/create.md) agent, string environmentID, ?array<string,string> metadata, ?list<Resource> resources, ?string title, ?list<string> vaultIDs, ?list<AnthropicBeta> betas): [BetaManagedAgentsSession](api/beta.md)

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

$client->beta->sessions->list(?string agentID, ?int agentVersion, ?\Datetime createdAtGt, ?\Datetime createdAtGte, ?\Datetime createdAtLt, ?\Datetime createdAtLte, ?string deploymentID, ?bool includeArchived, ?int limit, ?string memoryStoreID, ?[Order](api/beta/sessions/list.md) order, ?string page, ?list<Status> statuses, ?list<AnthropicBeta> betas): PageCursor<[BetaManagedAgentsSession](api/beta.md)>

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

$client->beta->sessions->retrieve(string sessionID, ?list<AnthropicBeta> betas): [BetaManagedAgentsSession](api/beta.md)

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

$client->beta->sessions->update(string sessionID, ?[BetaManagedAgentsSessionAgentUpdate](api/beta.md) agent, ?array<string,string> metadata, ?string title, ?list<string> vaultIDs, ?list<AnthropicBeta> betas): [BetaManagedAgentsSession](api/beta.md)

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

$client->beta->sessions->delete(string sessionID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeletedSession](api/beta.md)

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

$client->beta->sessions->archive(string sessionID, ?list<AnthropicBeta> betas): [BetaManagedAgentsSession](api/beta.md)

POST/v1/sessions/{session\_id}/archive

##### ModelsExpand Collapse



[BetaManagedAgentsAgentParams](api/beta.md)

string id

The `agent` ID.

Type type

?int version

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.



[BetaManagedAgentsBranchCheckout](api/beta.md)

string name

Branch name to check out.

Type type



[BetaManagedAgentsCacheCreationUsage](api/beta.md)

?int ephemeral1hInputTokens

Tokens used to create 1-hour ephemeral cache entries.

?int ephemeral5mInputTokens

Tokens used to create 5-minute ephemeral cache entries.



[BetaManagedAgentsCommitCheckout](api/beta.md)

string sha

Full commit SHA to check out.

Type type



[BetaManagedAgentsDeletedSession](api/beta.md)

string id

Type type



[BetaManagedAgentsFileResourceParams](api/beta.md)

string fileID

ID of a previously uploaded file.

Type type

?string mountPath

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.



[BetaManagedAgentsGitHubRepositoryResourceParams](api/beta.md)

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

[BetaManagedAgentsMemoryStoreResourceParam](api/beta.md)

string memoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type type

?Access access

Access mode for an attached memory store.

?string instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.



[BetaManagedAgentsMultiagent](api/beta.md)

list<[BetaManagedAgentsAgentReference](api/beta.md)> agents

Agents the coordinator may spawn as session threads, each resolved to a specific version.

Type type



[BetaManagedAgentsMultiagentParams](api/beta.md)

list<[BetaManagedAgentsMultiagentRosterEntryParams](api/beta.md)> agents

Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

Type type



[BetaManagedAgentsMultiagentRosterEntryParams](api/beta.md)

One of the following:

string



[BetaManagedAgentsAgentParams](api/beta.md)

string id

The `agent` ID.

Type type

?int version

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.



[BetaManagedAgentsMultiagentSelfParams](api/beta.md)

Type type



[BetaManagedAgentsOutcomeEvaluationResource](api/beta.md)

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

[BetaManagedAgentsSession](api/beta.md)

string id

[BetaManagedAgentsSessionAgent](api/beta.md) agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

?\Datetime archivedAt

A timestamp in RFC 3339 format

\Datetime createdAt

A timestamp in RFC 3339 format

string environmentID

array<string,string> metadata

list<[BetaManagedAgentsOutcomeEvaluationResource](api/beta.md)> outcomeEvaluations

Per-outcome evaluation state. One entry per define\_outcome event sent to the session.

list<[ManagedAgentsSessionResource](api/beta.md)> resources

[BetaManagedAgentsSessionStats](api/beta.md) stats

Timing statistics for a session.

Status status

SessionStatus enum

?string title

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

[BetaManagedAgentsSessionUsage](api/beta.md) usage

Cumulative token usage for a session across all turns.

list<string> vaultIDs

Vault IDs attached to the session at creation. Empty when no vaults were supplied.

?string deploymentID

Deployment ID when the session was created from a deployment reference. Null otherwise.



[BetaManagedAgentsSessionAgent](api/beta.md)

string id

?string description

list<[BetaManagedAgentsMCPServerURLDefinition](api/beta.md)> mcpServers

[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.

?[BetaManagedAgentsSessionMultiagentCoordinator](api/beta.md) multiagent

Resolved coordinator topology with full agent definitions for each roster member.

string name

list<Skill> skills

?string system

list<Tool> tools

Type type

int version



[BetaManagedAgentsSessionAgentUpdate](api/beta.md)

?list<[BetaManagedAgentsURLMCPServerParams](api/beta.md)> mcpServers

Replacement MCP server list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

?list<Tool> tools

Replacement tool list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.



[BetaManagedAgentsSessionMultiagentCoordinator](api/beta.md)

list<[BetaManagedAgentsSessionThreadAgent](api/beta.md)> agents

Full `agent` definitions the coordinator may spawn as session threads.

Type type



[BetaManagedAgentsSessionStats](api/beta.md)

?float activeSeconds

Cumulative time in seconds the session spent in running status. Excludes idle time.

?float durationSeconds

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

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

[BetaManagedAgentsSessionUsage](api/beta.md)

?[BetaManagedAgentsCacheCreationUsage](api/beta.md) cacheCreation

Prompt-cache creation token usage broken down by cache lifetime.

?int cacheReadInputTokens

Total tokens read from prompt cache.

?int inputTokens

Total input tokens consumed across all turns.

?int outputTokens

Total output tokens generated across all turns.



[BetaManagedAgentsSystemContentBlock](api/beta.md)

string text

The text content.

Type type



[BetaManagedAgentsSystemMessageEvent](api/beta.md)

string id

Unique identifier for this event.

list<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks. Text-only.

Type type

?\Datetime processedAt

A timestamp in RFC 3339 format

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

#### SessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

$client->beta->sessions->events->list(string sessionID, ?\Datetime createdAtGt, ?\Datetime createdAtGte, ?\Datetime createdAtLt, ?\Datetime createdAtLte, ?int limit, ?[Order](api/beta/sessions/events/list.md) order, ?string page, ?list<string> types, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsSessionEvent](api/beta.md)>

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

$client->beta->sessions->events->send(string sessionID, list<[ManagedAgentsEventParams](api/beta.md)> events, ?list<AnthropicBeta> betas): [ManagedAgentsSendSessionEvents](api/beta.md)

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

$client->beta->sessions->events->stream(string sessionID, ?list<AnthropicBeta> betas): [ManagedAgentsStreamSessionEvents](api/beta.md)

GET/v1/sessions/{session\_id}/events/stream

##### ModelsExpand Collapse

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

[ManagedAgentsAgentThreadContextCompactedEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type

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

[ManagedAgentsBase64DocumentSource](api/beta.md)

string data

Base64-encoded document data.

string mediaType

MIME type of the document (e.g., "application/pdf").

Type type



[ManagedAgentsBase64ImageSource](api/beta.md)

string data

Base64-encoded image data.

string mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



[ManagedAgentsBillingError](api/beta.md)

string message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Type type



[ManagedAgentsCredentialHostUnreachableError](api/beta.md)

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

[ManagedAgentsDocumentBlock](api/beta.md)

Source source

Union type for document source variants.

Type type

?string context

Additional context about the document for the model.

?string title

The title of the document.



[ManagedAgentsEventParams](api/beta.md)

One of the following:



[ManagedAgentsUserMessageEventParams](api/beta.md)

list<Content> content

Array of content blocks for the user message.

Type type



[ManagedAgentsUserInterruptEventParams](api/beta.md)

Type type

?string sessionThreadID

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



[ManagedAgentsUserToolConfirmationEventParams](api/beta.md)

Result result

UserToolConfirmationResult enum

string toolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?string denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.



[ManagedAgentsUserCustomToolResultEventParams](api/beta.md)

string customToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.



[ManagedAgentsUserDefineOutcomeEventParams](api/beta.md)

string description

What the agent should produce. This is the task specification.

Rubric rubric

Rubric for grading the quality of an outcome.

Type type

?int maxIterations

Eval→revision cycles before giving up. Default 3, max 20.



[ManagedAgentsUserToolResultEventParams](api/beta.md)

string toolUseID

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.



[ManagedAgentsSystemMessageEventParams](api/beta.md)

list<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks to append. Text-only.

Type type



[ManagedAgentsFileDocumentSource](api/beta.md)

string fileID

ID of a previously uploaded file.

Type type



[ManagedAgentsFileImageSource](api/beta.md)

string fileID

ID of a previously uploaded file.

Type type



[ManagedAgentsFileRubric](api/beta.md)

string fileID

ID of the rubric file.

Type type



[ManagedAgentsFileRubricParams](api/beta.md)

string fileID

ID of the rubric file.

Type type



[ManagedAgentsImageBlock](api/beta.md)

Source source

Union type for image source variants.

Type type



[ManagedAgentsMCPAuthenticationFailedError](api/beta.md)

string mcpServerName

Name of the MCP server that failed authentication.

string message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Type type



[ManagedAgentsMCPConnectionFailedError](api/beta.md)

string mcpServerName

Name of the MCP server that failed to connect.

string message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Type type



[ManagedAgentsModelOverloadedError](api/beta.md)

string message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Type type



[ManagedAgentsModelRateLimitedError](api/beta.md)

string message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Type type



[ManagedAgentsModelRequestFailedError](api/beta.md)

string message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Type type



[ManagedAgentsPlainTextDocumentSource](api/beta.md)

string data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



[ManagedAgentsRetryStatusExhausted](api/beta.md)

Type type



[ManagedAgentsRetryStatusRetrying](api/beta.md)

Type type



[ManagedAgentsRetryStatusTerminal](api/beta.md)

Type type



[ManagedAgentsSearchResultBlock](api/beta.md)

[ManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

list<[ManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

string source

The URL source of the search result.

string title

The title of the search result.

Type type



[ManagedAgentsSearchResultCitations](api/beta.md)

bool enabled

Whether citations are enabled for this search result.



[ManagedAgentsSearchResultContent](api/beta.md)

string text

The text content.

Type type



[ManagedAgentsSendSessionEvents](api/beta.md)

?list<Data> data

Sent events



[ManagedAgentsSessionDeletedEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSessionEndTurn](api/beta.md)

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



[ManagedAgentsSessionRequiresAction](api/beta.md)

list<string> eventIDs

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type type



[ManagedAgentsSessionRetriesExhausted](api/beta.md)

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

[ManagedAgentsSpanModelRequestStartEvent](api/beta.md)

string id

Unique identifier for this event.

\Datetime processedAt

A timestamp in RFC 3339 format

Type type



[ManagedAgentsSpanModelUsage](api/beta.md)

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

[ManagedAgentsStreamSessionEvents](api/beta.md)

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



[ManagedAgentsSystemMessageEventParams](api/beta.md)

list<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks to append. Text-only.

Type type



[ManagedAgentsTextBlock](api/beta.md)

string text

The text content.

Type type



[ManagedAgentsTextRubric](api/beta.md)

string content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

Type type



[ManagedAgentsTextRubricParams](api/beta.md)

string content

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

Type type



[ManagedAgentsUnknownError](api/beta.md)

string message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Type type



[ManagedAgentsURLDocumentSource](api/beta.md)

Type type

string url

URL of the document to fetch.



[ManagedAgentsURLImageSource](api/beta.md)

Type type

string url

URL of the image to fetch.

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

[ManagedAgentsUserCustomToolResultEventParams](api/beta.md)

string customToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

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

[ManagedAgentsUserDefineOutcomeEventParams](api/beta.md)

string description

What the agent should produce. This is the task specification.

Rubric rubric

Rubric for grading the quality of an outcome.

Type type

?int maxIterations

Eval→revision cycles before giving up. Default 3, max 20.

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

[ManagedAgentsUserInterruptEventParams](api/beta.md)

Type type

?string sessionThreadID

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

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

[ManagedAgentsUserMessageEventParams](api/beta.md)

list<Content> content

Array of content blocks for the user message.

Type type

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

[ManagedAgentsUserToolConfirmationEventParams](api/beta.md)

Result result

UserToolConfirmationResult enum

string toolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?string denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.



[ManagedAgentsUserToolResultEventParams](api/beta.md)

string toolUseID

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

?list<Content> content

The result content returned by the tool.

?bool isError

Whether the tool execution resulted in an error.

#### SessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

$client->beta->sessions->resources->add(string sessionID, string fileID, [Type](api/beta/sessions/resources/add.md) type, ?string mountPath, ?list<AnthropicBeta> betas): [ManagedAgentsFileResource](api/beta.md)

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

$client->beta->sessions->resources->list(string sessionID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsSessionResource](api/beta.md)>

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

$client->beta->sessions->resources->retrieve(string resourceID, string sessionID, ?list<AnthropicBeta> betas): [ResourceGetResponse](api/beta.md)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

$client->beta->sessions->resources->update(string resourceID, string sessionID, string authorizationToken, ?list<AnthropicBeta> betas): [ResourceUpdateResponse](api/beta.md)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

$client->beta->sessions->resources->delete(string resourceID, string sessionID, ?list<AnthropicBeta> betas): [ManagedAgentsDeleteSessionResource](api/beta.md)

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

##### ModelsExpand Collapse



[ManagedAgentsDeleteSessionResource](api/beta.md)

string id

Type type



[ManagedAgentsFileResource](api/beta.md)

string id

\Datetime createdAt

A timestamp in RFC 3339 format

string fileID

string mountPath

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format



[ManagedAgentsGitHubRepositoryResource](api/beta.md)

string id

\Datetime createdAt

A timestamp in RFC 3339 format

string mountPath

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

string url

?Checkout checkout



[ManagedAgentsMemoryStoreResource](api/beta.md)

string memoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type type

?Access access

Access mode for an attached memory store.

?string description

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

?string instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

?string mountPath

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

?string name

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.



[ManagedAgentsSessionResource](api/beta.md)

One of the following:



[ManagedAgentsGitHubRepositoryResource](api/beta.md)

string id

\Datetime createdAt

A timestamp in RFC 3339 format

string mountPath

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

string url

?Checkout checkout



[ManagedAgentsFileResource](api/beta.md)

string id

\Datetime createdAt

A timestamp in RFC 3339 format

string fileID

string mountPath

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format



[ManagedAgentsMemoryStoreResource](api/beta.md)

string memoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type type

?Access access

Access mode for an attached memory store.

?string description

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

?string instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

?string mountPath

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

?string name

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### SessionsThreads

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

#### SessionsThreadsEvents

##### [List Session Thread Events](api/beta/sessions/threads/events/list.md)

$client->beta->sessions->threads->events->list(string threadID, string sessionID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsSessionEvent](api/beta.md)>

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/beta/sessions/threads/events/stream.md)

$client->beta->sessions->threads->events->stream(string threadID, string sessionID, ?list<AnthropicBeta> betas): [ManagedAgentsStreamSessionThreadEvents](api/beta.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

---

*Copyright © Anthropic. All rights reserved.*
