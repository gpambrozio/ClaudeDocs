# Sessions

Copy page



C#

# Sessions

##### [Create Session](api/beta/sessions/create.md)

[BetaManagedAgentsSession](api/beta/sessions.md) Beta.Sessions.Create(SessionCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

[SessionListPageResponse](api/beta/sessions.md) Beta.Sessions.List(SessionListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

[BetaManagedAgentsSession](api/beta/sessions.md) Beta.Sessions.Retrieve(SessionRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

[BetaManagedAgentsSession](api/beta/sessions.md) Beta.Sessions.Update(SessionUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

[BetaManagedAgentsDeletedSession](api/beta/sessions.md) Beta.Sessions.Delete(SessionDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

[BetaManagedAgentsSession](api/beta/sessions.md) Beta.Sessions.Archive(SessionArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}/archive

##### ModelsExpand Collapse



class BetaManagedAgentsAgentParams:

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

required string ID

The `agent` ID.

required Type Type

Int Version

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.



class BetaManagedAgentsBranchCheckout:

required string Name

Branch name to check out.

required Type Type



class BetaManagedAgentsCacheCreationUsage:

Prompt-cache creation token usage broken down by cache lifetime.

Int Ephemeral1hInputTokens

Tokens used to create 1-hour ephemeral cache entries.

Int Ephemeral5mInputTokens

Tokens used to create 5-minute ephemeral cache entries.



class BetaManagedAgentsCommitCheckout:

required string Sha

Full commit SHA to check out.

required Type Type



class BetaManagedAgentsDeletedSession:

Confirmation that a `session` has been permanently deleted.

required string ID

required Type Type



class BetaManagedAgentsFileResourceParams:

Mount a file uploaded via the Files API into the session.

required string FileID

ID of a previously uploaded file.

required Type Type

string? MountPath

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.



class BetaManagedAgentsGitHubRepositoryResourceParams:

Mount a GitHub repository into the session's container.

required string AuthorizationToken

GitHub authorization token used to clone the repository.

required Type Type

required string Url

Github URL of the repository



Checkout? Checkout

Branch or commit to check out. Defaults to the repository's default branch.

One of the following:



class BetaManagedAgentsBranchCheckout:

required string Name

Branch name to check out.

required Type Type



class BetaManagedAgentsCommitCheckout:

required string Sha

Full commit SHA to check out.

required Type Type

string? MountPath

Mount path in the container. Defaults to `/workspace/<repo-name>`.



class BetaManagedAgentsMemoryStoreResourceParam:

Parameters for attaching a memory store to an agent session.

required string MemoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

required Type Type



Access? Access

Access mode for an attached memory store.

One of the following:

"read\_write"ReadWrite

"read\_only"ReadOnly

string? Instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.



class BetaManagedAgentsMultiagent:

Resolved coordinator topology with a concrete agent roster.



required IReadOnlyList<[BetaManagedAgentsAgentReference](api/beta/agents.md)> Agents

Agents the coordinator may spawn as session threads, each resolved to a specific version.

required string ID

required Type Type

required Int Version

required Type Type



class BetaManagedAgentsMultiagentParams:

A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.



required IReadOnlyList<[BetaManagedAgentsMultiagentRosterEntryParams](api/beta/sessions.md)> Agents

Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

One of the following:

string



class BetaManagedAgentsAgentParams:

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

required string ID

The `agent` ID.

required Type Type

Int Version

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.



class BetaManagedAgentsMultiagentSelfParams:

Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

required Type Type

required Type Type



class BetaManagedAgentsMultiagentRosterEntryParams: A class that can be one of several variants.union 

An entry in a multiagent roster: an agent ID string, a versioned agent reference, or `self`.

string



class BetaManagedAgentsAgentParams:

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

required string ID

The `agent` ID.

required Type Type

Int Version

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.



class BetaManagedAgentsMultiagentSelfParams:

Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

required Type Type



class BetaManagedAgentsOutcomeEvaluationResource:

Evaluation state for a single outcome defined via a define\_outcome event.

required DateTimeOffset? CompletedAt

A timestamp in RFC 3339 format

required string Description

What the agent should produce.

required string? Explanation

Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs\_revision (intermediate), what's missing; for failed, why unrecoverable.

required Int Iteration

0-indexed revision cycle the outcome is currently on.

required string OutcomeID

Server-generated outc\_ ID for this outcome.

required string Result

Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

required Type Type



class BetaManagedAgentsSession:

A Managed Agents `session`.

required string ID



required [BetaManagedAgentsSessionAgent](api/beta/sessions.md) Agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

required string ID

required string? Description



required IReadOnlyList<[BetaManagedAgentsMcpServerUrlDefinition](api/beta/agents.md)> McpServers

required string Name

required Type Type

required string Url



required [BetaManagedAgentsModelConfig](api/beta/agents.md) Model

Model identifier and configuration.



required [BetaManagedAgentsModel](api/beta/agents.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-fable-5"ClaudeFable5

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"ClaudeOpus4\_8

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"ClaudeOpus4\_7

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding



Speed Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"Standard

"fast"Fast



required [BetaManagedAgentsSessionMultiagentCoordinator](api/beta/sessions.md)? Multiagent

Resolved coordinator topology with full agent definitions for each roster member.



required IReadOnlyList<[BetaManagedAgentsSessionThreadAgent](api/beta/agents.md)> Agents

Full `agent` definitions the coordinator may spawn as session threads.

required string ID

required string? Description



required IReadOnlyList<[BetaManagedAgentsMcpServerUrlDefinition](api/beta/agents.md)> McpServers

required string Name

required Type Type

required string Url



required [BetaManagedAgentsModelConfig](api/beta/agents.md) Model

Model identifier and configuration.



required [BetaManagedAgentsModel](api/beta/agents.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-fable-5"ClaudeFable5

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"ClaudeOpus4\_8

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"ClaudeOpus4\_7

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding



Speed Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"Standard

"fast"Fast

required string Name



required IReadOnlyList<Skill> Skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

required string SkillID

required Type Type

required string Version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

required string SkillID

required Type Type

required string Version

required string? System



required IReadOnlyList<Tool> Tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



required IReadOnlyList<[BetaManagedAgentsAgentToolConfig](api/beta/agents.md)> Configs

required Boolean Enabled



required Name Name

Built-in agent tool identifier.

One of the following:

"bash"Bash

"edit"Edit

"read"Read

"write"Write

"glob"Glob

"grep"Grep

"web\_fetch"WebFetch

"web\_search"WebSearch



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) DefaultConfig

Resolved default configuration for agent tools.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required Type Type



class BetaManagedAgentsMcpToolset:



required IReadOnlyList<[BetaManagedAgentsMcpToolConfig](api/beta/agents.md)> Configs

required Boolean Enabled

required string Name



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsMcpToolsetDefaultConfig](api/beta/agents.md) DefaultConfig

Resolved default configuration for all tools from an MCP server.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required string McpServerName

required Type Type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

required string Description



required [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) InputSchema

JSON Schema for custom tool input parameters.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required

required string Name

required Type Type

required Type Type

required Int Version

required Type Type

required string Name



required IReadOnlyList<Skill> Skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

required string SkillID

required Type Type

required string Version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

required string SkillID

required Type Type

required string Version

required string? System



required IReadOnlyList<Tool> Tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



required IReadOnlyList<[BetaManagedAgentsAgentToolConfig](api/beta/agents.md)> Configs

required Boolean Enabled



required Name Name

Built-in agent tool identifier.

One of the following:

"bash"Bash

"edit"Edit

"read"Read

"write"Write

"glob"Glob

"grep"Grep

"web\_fetch"WebFetch

"web\_search"WebSearch



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) DefaultConfig

Resolved default configuration for agent tools.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required Type Type



class BetaManagedAgentsMcpToolset:



required IReadOnlyList<[BetaManagedAgentsMcpToolConfig](api/beta/agents.md)> Configs

required Boolean Enabled

required string Name



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsMcpToolsetDefaultConfig](api/beta/agents.md) DefaultConfig

Resolved default configuration for all tools from an MCP server.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required string McpServerName

required Type Type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

required string Description



required [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) InputSchema

JSON Schema for custom tool input parameters.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required

required string Name

required Type Type

required Type Type

required Int Version

required DateTimeOffset? ArchivedAt

A timestamp in RFC 3339 format

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string EnvironmentID

required IReadOnlyDictionary<string, string> Metadata



required IReadOnlyList<[BetaManagedAgentsOutcomeEvaluationResource](api/beta/sessions.md)> OutcomeEvaluations

Per-outcome evaluation state. One entry per define\_outcome event sent to the session.

required DateTimeOffset? CompletedAt

A timestamp in RFC 3339 format

required string Description

What the agent should produce.

required string? Explanation

Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs\_revision (intermediate), what's missing; for failed, why unrecoverable.

required Int Iteration

0-indexed revision cycle the outcome is currently on.

required string OutcomeID

Server-generated outc\_ ID for this outcome.

required string Result

Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

required Type Type



required IReadOnlyList<[BetaManagedAgentsSessionResource](api/beta/sessions/resources.md)> Resources

One of the following:



class BetaManagedAgentsGitHubRepositoryResource:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string MountPath

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required string Url



Checkout? Checkout

One of the following:



class BetaManagedAgentsBranchCheckout:

required string Name

Branch name to check out.

required Type Type



class BetaManagedAgentsCommitCheckout:

required string Sha

Full commit SHA to check out.

required Type Type



class BetaManagedAgentsFileResource:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string FileID

required string MountPath

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsMemoryStoreResource:

A memory store attached to an agent session.

required string MemoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

required Type Type



Access? Access

Access mode for an attached memory store.

One of the following:

"read\_write"ReadWrite

"read\_only"ReadOnly

string Description

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

string? Instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

string? MountPath

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

string? Name

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.



required [BetaManagedAgentsSessionStats](api/beta/sessions.md) Stats

Timing statistics for a session.

Double ActiveSeconds

Cumulative time in seconds the session spent in running status. Excludes idle time.

Double DurationSeconds

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.



required Status Status

SessionStatus enum

One of the following:

"rescheduling"Rescheduling

"running"Running

"idle"Idle

"terminated"Terminated

required string? Title

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format



required [BetaManagedAgentsSessionUsage](api/beta/sessions.md) Usage

Cumulative token usage for a session across all turns.



[BetaManagedAgentsCacheCreationUsage](api/beta/sessions.md) CacheCreation

Prompt-cache creation token usage broken down by cache lifetime.

Int Ephemeral1hInputTokens

Tokens used to create 1-hour ephemeral cache entries.

Int Ephemeral5mInputTokens

Tokens used to create 5-minute ephemeral cache entries.

Int CacheReadInputTokens

Total tokens read from prompt cache.

Int InputTokens

Total input tokens consumed across all turns.

Int OutputTokens

Total output tokens generated across all turns.

required IReadOnlyList<string> VaultIds

Vault IDs attached to the session at creation. Empty when no vaults were supplied.

string? DeploymentID

Deployment ID when the session was created from a deployment reference. Null otherwise.



class BetaManagedAgentsSessionAgent:

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

required string ID

required string? Description



required IReadOnlyList<[BetaManagedAgentsMcpServerUrlDefinition](api/beta/agents.md)> McpServers

required string Name

required Type Type

required string Url



required [BetaManagedAgentsModelConfig](api/beta/agents.md) Model

Model identifier and configuration.



required [BetaManagedAgentsModel](api/beta/agents.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-fable-5"ClaudeFable5

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"ClaudeOpus4\_8

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"ClaudeOpus4\_7

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding



Speed Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"Standard

"fast"Fast



required [BetaManagedAgentsSessionMultiagentCoordinator](api/beta/sessions.md)? Multiagent

Resolved coordinator topology with full agent definitions for each roster member.



required IReadOnlyList<[BetaManagedAgentsSessionThreadAgent](api/beta/agents.md)> Agents

Full `agent` definitions the coordinator may spawn as session threads.

required string ID

required string? Description



required IReadOnlyList<[BetaManagedAgentsMcpServerUrlDefinition](api/beta/agents.md)> McpServers

required string Name

required Type Type

required string Url



required [BetaManagedAgentsModelConfig](api/beta/agents.md) Model

Model identifier and configuration.



required [BetaManagedAgentsModel](api/beta/agents.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-fable-5"ClaudeFable5

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"ClaudeOpus4\_8

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"ClaudeOpus4\_7

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding



Speed Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"Standard

"fast"Fast

required string Name



required IReadOnlyList<Skill> Skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

required string SkillID

required Type Type

required string Version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

required string SkillID

required Type Type

required string Version

required string? System



required IReadOnlyList<Tool> Tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



required IReadOnlyList<[BetaManagedAgentsAgentToolConfig](api/beta/agents.md)> Configs

required Boolean Enabled



required Name Name

Built-in agent tool identifier.

One of the following:

"bash"Bash

"edit"Edit

"read"Read

"write"Write

"glob"Glob

"grep"Grep

"web\_fetch"WebFetch

"web\_search"WebSearch



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) DefaultConfig

Resolved default configuration for agent tools.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required Type Type



class BetaManagedAgentsMcpToolset:



required IReadOnlyList<[BetaManagedAgentsMcpToolConfig](api/beta/agents.md)> Configs

required Boolean Enabled

required string Name



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsMcpToolsetDefaultConfig](api/beta/agents.md) DefaultConfig

Resolved default configuration for all tools from an MCP server.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required string McpServerName

required Type Type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

required string Description



required [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) InputSchema

JSON Schema for custom tool input parameters.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required

required string Name

required Type Type

required Type Type

required Int Version

required Type Type

required string Name



required IReadOnlyList<Skill> Skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

required string SkillID

required Type Type

required string Version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

required string SkillID

required Type Type

required string Version

required string? System



required IReadOnlyList<Tool> Tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



required IReadOnlyList<[BetaManagedAgentsAgentToolConfig](api/beta/agents.md)> Configs

required Boolean Enabled



required Name Name

Built-in agent tool identifier.

One of the following:

"bash"Bash

"edit"Edit

"read"Read

"write"Write

"glob"Glob

"grep"Grep

"web\_fetch"WebFetch

"web\_search"WebSearch



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) DefaultConfig

Resolved default configuration for agent tools.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required Type Type



class BetaManagedAgentsMcpToolset:



required IReadOnlyList<[BetaManagedAgentsMcpToolConfig](api/beta/agents.md)> Configs

required Boolean Enabled

required string Name



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsMcpToolsetDefaultConfig](api/beta/agents.md) DefaultConfig

Resolved default configuration for all tools from an MCP server.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required string McpServerName

required Type Type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

required string Description



required [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) InputSchema

JSON Schema for custom tool input parameters.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required

required string Name

required Type Type

required Type Type

required Int Version



class BetaManagedAgentsSessionAgentUpdate:

Mid-session agent configuration update. Only `tools` and `mcp_servers` are updatable. Full replacement: the provided array becomes the new value. To preserve existing entries, GET the session, modify the array, and POST it back.



IReadOnlyList<[BetaManagedAgentsUrlMcpServerParams](api/beta/agents.md)> McpServers

Replacement MCP server list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

required string Name

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

required Type Type

required string Url

Endpoint URL for the MCP server.



IReadOnlyList<Tool> Tools

Replacement tool list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

One of the following:



class BetaManagedAgentsAgentToolset20260401Params:

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

required Type Type



IReadOnlyList<[BetaManagedAgentsAgentToolConfigParams](api/beta/agents.md)> Configs

Per-tool configuration overrides.



required Name Name

Built-in agent tool identifier.

One of the following:

"bash"Bash

"edit"Edit

"read"Read

"write"Write

"glob"Glob

"grep"Grep

"web\_fetch"WebFetch

"web\_search"WebSearch

Boolean? Enabled

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.



PermissionPolicy? PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



[BetaManagedAgentsAgentToolsetDefaultConfigParams](api/beta/agents.md)? DefaultConfig

Default configuration for all tools in a toolset.

Boolean? Enabled

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.



PermissionPolicy? PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



class BetaManagedAgentsMcpToolsetParams:

Configuration for tools from an MCP server defined in `mcp_servers`.

required string McpServerName

Name of the MCP server. Must match a server name from the mcp\_servers array. 1-255 characters.

required Type Type



IReadOnlyList<[BetaManagedAgentsMcpToolConfigParams](api/beta/agents.md)> Configs

Per-tool configuration overrides.

required string Name

Name of the MCP tool to configure. 1-128 characters.

Boolean? Enabled

Whether this tool is enabled. Overrides the `default_config` setting.



PermissionPolicy? PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



[BetaManagedAgentsMcpToolsetDefaultConfigParams](api/beta/agents.md)? DefaultConfig

Default configuration for all tools from an MCP server.

Boolean? Enabled

Whether tools are enabled by default. Defaults to true if not specified.



PermissionPolicy? PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



class BetaManagedAgentsCustomToolParams:

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

required string Description

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.



required [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) InputSchema

JSON Schema for custom tool input parameters.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required

required string Name

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

required Type Type



class BetaManagedAgentsSessionMultiagentCoordinator:

Resolved coordinator topology with full agent definitions for each roster member.



required IReadOnlyList<[BetaManagedAgentsSessionThreadAgent](api/beta/agents.md)> Agents

Full `agent` definitions the coordinator may spawn as session threads.

required string ID

required string? Description



required IReadOnlyList<[BetaManagedAgentsMcpServerUrlDefinition](api/beta/agents.md)> McpServers

required string Name

required Type Type

required string Url



required [BetaManagedAgentsModelConfig](api/beta/agents.md) Model

Model identifier and configuration.



required [BetaManagedAgentsModel](api/beta/agents.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-fable-5"ClaudeFable5

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"ClaudeOpus4\_8

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"ClaudeOpus4\_7

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding



Speed Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"Standard

"fast"Fast

required string Name



required IReadOnlyList<Skill> Skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

required string SkillID

required Type Type

required string Version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

required string SkillID

required Type Type

required string Version

required string? System



required IReadOnlyList<Tool> Tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



required IReadOnlyList<[BetaManagedAgentsAgentToolConfig](api/beta/agents.md)> Configs

required Boolean Enabled



required Name Name

Built-in agent tool identifier.

One of the following:

"bash"Bash

"edit"Edit

"read"Read

"write"Write

"glob"Glob

"grep"Grep

"web\_fetch"WebFetch

"web\_search"WebSearch



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) DefaultConfig

Resolved default configuration for agent tools.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required Type Type



class BetaManagedAgentsMcpToolset:



required IReadOnlyList<[BetaManagedAgentsMcpToolConfig](api/beta/agents.md)> Configs

required Boolean Enabled

required string Name



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsMcpToolsetDefaultConfig](api/beta/agents.md) DefaultConfig

Resolved default configuration for all tools from an MCP server.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required string McpServerName

required Type Type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

required string Description



required [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) InputSchema

JSON Schema for custom tool input parameters.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required

required string Name

required Type Type

required Type Type

required Int Version

required Type Type



class BetaManagedAgentsSessionStats:

Timing statistics for a session.

Double ActiveSeconds

Cumulative time in seconds the session spent in running status. Excludes idle time.

Double DurationSeconds

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.



class BetaManagedAgentsSessionUpdatedEvent:

Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type



[BetaManagedAgentsSessionAgent](api/beta/sessions.md)? Agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

required string ID

required string? Description



required IReadOnlyList<[BetaManagedAgentsMcpServerUrlDefinition](api/beta/agents.md)> McpServers

required string Name

required Type Type

required string Url



required [BetaManagedAgentsModelConfig](api/beta/agents.md) Model

Model identifier and configuration.



required [BetaManagedAgentsModel](api/beta/agents.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-fable-5"ClaudeFable5

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"ClaudeOpus4\_8

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"ClaudeOpus4\_7

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding



Speed Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"Standard

"fast"Fast



required [BetaManagedAgentsSessionMultiagentCoordinator](api/beta/sessions.md)? Multiagent

Resolved coordinator topology with full agent definitions for each roster member.



required IReadOnlyList<[BetaManagedAgentsSessionThreadAgent](api/beta/agents.md)> Agents

Full `agent` definitions the coordinator may spawn as session threads.

required string ID

required string? Description



required IReadOnlyList<[BetaManagedAgentsMcpServerUrlDefinition](api/beta/agents.md)> McpServers

required string Name

required Type Type

required string Url



required [BetaManagedAgentsModelConfig](api/beta/agents.md) Model

Model identifier and configuration.



required [BetaManagedAgentsModel](api/beta/agents.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-fable-5"ClaudeFable5

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"ClaudeOpus4\_8

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"ClaudeOpus4\_7

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding



Speed Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"Standard

"fast"Fast

required string Name



required IReadOnlyList<Skill> Skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

required string SkillID

required Type Type

required string Version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

required string SkillID

required Type Type

required string Version

required string? System



required IReadOnlyList<Tool> Tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



required IReadOnlyList<[BetaManagedAgentsAgentToolConfig](api/beta/agents.md)> Configs

required Boolean Enabled



required Name Name

Built-in agent tool identifier.

One of the following:

"bash"Bash

"edit"Edit

"read"Read

"write"Write

"glob"Glob

"grep"Grep

"web\_fetch"WebFetch

"web\_search"WebSearch



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) DefaultConfig

Resolved default configuration for agent tools.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required Type Type



class BetaManagedAgentsMcpToolset:



required IReadOnlyList<[BetaManagedAgentsMcpToolConfig](api/beta/agents.md)> Configs

required Boolean Enabled

required string Name



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsMcpToolsetDefaultConfig](api/beta/agents.md) DefaultConfig

Resolved default configuration for all tools from an MCP server.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required string McpServerName

required Type Type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

required string Description



required [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) InputSchema

JSON Schema for custom tool input parameters.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required

required string Name

required Type Type

required Type Type

required Int Version

required Type Type

required string Name



required IReadOnlyList<Skill> Skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

required string SkillID

required Type Type

required string Version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

required string SkillID

required Type Type

required string Version

required string? System



required IReadOnlyList<Tool> Tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



required IReadOnlyList<[BetaManagedAgentsAgentToolConfig](api/beta/agents.md)> Configs

required Boolean Enabled



required Name Name

Built-in agent tool identifier.

One of the following:

"bash"Bash

"edit"Edit

"read"Read

"write"Write

"glob"Glob

"grep"Grep

"web\_fetch"WebFetch

"web\_search"WebSearch



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) DefaultConfig

Resolved default configuration for agent tools.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required Type Type



class BetaManagedAgentsMcpToolset:



required IReadOnlyList<[BetaManagedAgentsMcpToolConfig](api/beta/agents.md)> Configs

required Boolean Enabled

required string Name



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsMcpToolsetDefaultConfig](api/beta/agents.md) DefaultConfig

Resolved default configuration for all tools from an MCP server.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required string McpServerName

required Type Type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

required string Description



required [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) InputSchema

JSON Schema for custom tool input parameters.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required

required string Name

required Type Type

required Type Type

required Int Version

IReadOnlyDictionary<string, string> Metadata

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

string? Title

The session's new title. Present only when the update changed it.



class BetaManagedAgentsSessionUsage:

Cumulative token usage for a session across all turns.



[BetaManagedAgentsCacheCreationUsage](api/beta/sessions.md) CacheCreation

Prompt-cache creation token usage broken down by cache lifetime.

Int Ephemeral1hInputTokens

Tokens used to create 1-hour ephemeral cache entries.

Int Ephemeral5mInputTokens

Tokens used to create 5-minute ephemeral cache entries.

Int CacheReadInputTokens

Total tokens read from prompt cache.

Int InputTokens

Total input tokens consumed across all turns.

Int OutputTokens

Total output tokens generated across all turns.



class BetaManagedAgentsSystemContentBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsSystemMessageEvent:

A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

required string ID

Unique identifier for this event.



required IReadOnlyList<[BetaManagedAgentsSystemContentBlock](api/beta/sessions.md)> Content

System content blocks. Text-only.

required string Text

The text content.

required Type Type

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsUserToolResultEvent:

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

required string ID

Unique identifier for this event.

required string ToolUseID

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type



IReadOnlyList<Content> Content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



required [BetaManagedAgentsSearchResultCitations](api/beta/sessions/events.md) Citations

Citation settings for a search result.

required Boolean Enabled

Whether citations are enabled for this search result.



required IReadOnlyList<[BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md)> Content

Array of text content blocks from the search result.

required string Text

The text content.

required Type Type

required string Source

The URL source of the search result.

required string Title

The title of the search result.

required Type Type

Boolean? IsError

Whether the tool execution resulted in an error.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

#### SessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

[EventListPageResponse](api/beta/sessions/events.md) Beta.Sessions.Events.List(EventListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

[BetaManagedAgentsSendSessionEvents](api/beta/sessions/events.md) Beta.Sessions.Events.Send(EventSendParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

[BetaManagedAgentsStreamSessionEvents](api/beta/sessions/events.md) Beta.Sessions.Events.StreamStreaming(EventStreamParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/events/stream

#### SessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

[BetaManagedAgentsFileResource](api/beta/sessions/resources.md) Beta.Sessions.Resources.Add(ResourceAddParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

[ResourceListPageResponse](api/beta/sessions/resources.md) Beta.Sessions.Resources.List(ResourceListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

[ResourceRetrieveResponse](api/beta/sessions/resources.md) Beta.Sessions.Resources.Retrieve(ResourceRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

[ResourceUpdateResponse](api/beta/sessions/resources.md) Beta.Sessions.Resources.Update(ResourceUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

[BetaManagedAgentsDeleteSessionResource](api/beta/sessions/resources.md) Beta.Sessions.Resources.Delete(ResourceDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

#### SessionsThreads

##### [List Session Threads](api/beta/sessions/threads/list.md)

[ThreadListPageResponse](api/beta/sessions/threads.md) Beta.Sessions.Threads.List(ThreadListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/threads

##### [Get Session Thread](api/beta/sessions/threads/retrieve.md)

[BetaManagedAgentsSessionThread](api/beta/sessions/threads.md) Beta.Sessions.Threads.Retrieve(ThreadRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/threads/{thread\_id}

##### [Archive Session Thread](api/beta/sessions/threads/archive.md)

[BetaManagedAgentsSessionThread](api/beta/sessions/threads.md) Beta.Sessions.Threads.Archive(ThreadArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}/threads/{thread\_id}/archive

#### SessionsThreadsEvents

##### [List Session Thread Events](api/beta/sessions/threads/events/list.md)

[EventListPageResponse](api/beta/sessions/threads/events.md) Beta.Sessions.Threads.Events.List(EventListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/beta/sessions/threads/events/stream.md)

[BetaManagedAgentsStreamSessionThreadEvents](api/beta/sessions/threads.md) Beta.Sessions.Threads.Events.StreamStreaming(EventStreamParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

---

*Copyright © Anthropic. All rights reserved.*
