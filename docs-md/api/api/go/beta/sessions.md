# Sessions

Copy page



Go

# Sessions

##### [Create Session](api/beta/sessions/create.md)

client.Beta.Sessions.New(ctx, params) (\*[BetaManagedAgentsSession](api/beta.md), error)

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

client.Beta.Sessions.List(ctx, params) (\*PageCursor[[BetaManagedAgentsSession](api/beta.md)], error)

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

client.Beta.Sessions.Get(ctx, sessionID, query) (\*[BetaManagedAgentsSession](api/beta.md), error)

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

client.Beta.Sessions.Update(ctx, sessionID, params) (\*[BetaManagedAgentsSession](api/beta.md), error)

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

client.Beta.Sessions.Delete(ctx, sessionID, body) (\*[BetaManagedAgentsDeletedSession](api/beta.md), error)

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

client.Beta.Sessions.Archive(ctx, sessionID, body) (\*[BetaManagedAgentsSession](api/beta.md), error)

POST/v1/sessions/{session\_id}/archive

##### ModelsExpand Collapse



type BetaManagedAgentsAgentParamsResp struct{…}

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

ID string

The `agent` ID.

Type BetaManagedAgentsAgentParamsType

Version int64Optional

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.



type BetaManagedAgentsBranchCheckout struct{…}

Name string

Branch name to check out.

Type BetaManagedAgentsBranchCheckoutType



type BetaManagedAgentsCacheCreationUsage struct{…}

Prompt-cache creation token usage broken down by cache lifetime.

Ephemeral1hInputTokens int64Optional

Tokens used to create 1-hour ephemeral cache entries.

Ephemeral5mInputTokens int64Optional

Tokens used to create 5-minute ephemeral cache entries.



type BetaManagedAgentsCommitCheckout struct{…}

Sha string

Full commit SHA to check out.

Type BetaManagedAgentsCommitCheckoutType



type BetaManagedAgentsDeletedSession struct{…}

Confirmation that a `session` has been permanently deleted.

ID string

Type BetaManagedAgentsDeletedSessionType



type BetaManagedAgentsFileResourceParamsResp struct{…}

Mount a file uploaded via the Files API into the session.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileResourceParamsType

MountPath stringOptional

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.



type BetaManagedAgentsGitHubRepositoryResourceParamsResp struct{…}

Mount a GitHub repository into the session's container.

AuthorizationToken string

GitHub authorization token used to clone the repository.

Type BetaManagedAgentsGitHubRepositoryResourceParamsType

URL string

Github URL of the repository



Checkout BetaManagedAgentsGitHubRepositoryResourceParamsCheckoutUnionRespOptional

Branch or commit to check out. Defaults to the repository's default branch.

One of the following:



type BetaManagedAgentsBranchCheckout struct{…}

Name string

Branch name to check out.

Type BetaManagedAgentsBranchCheckoutType



type BetaManagedAgentsCommitCheckout struct{…}

Sha string

Full commit SHA to check out.

Type BetaManagedAgentsCommitCheckoutType

MountPath stringOptional

Mount path in the container. Defaults to `/workspace/<repo-name>`.



type BetaManagedAgentsMemoryStoreResourceParamResp struct{…}

Parameters for attaching a memory store to an agent session.

MemoryStoreID string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type BetaManagedAgentsMemoryStoreResourceParamType



Access BetaManagedAgentsMemoryStoreResourceParamAccessOptional

Access mode for an attached memory store.

One of the following:

const BetaManagedAgentsMemoryStoreResourceParamAccessReadWrite BetaManagedAgentsMemoryStoreResourceParamAccess = "read\_write"

const BetaManagedAgentsMemoryStoreResourceParamAccessReadOnly BetaManagedAgentsMemoryStoreResourceParamAccess = "read\_only"

Instructions stringOptional

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.



type BetaManagedAgentsMultiagent struct{…}

Resolved coordinator topology with a concrete agent roster.



Agents [][BetaManagedAgentsAgentReference](api/beta.md)

Agents the coordinator may spawn as session threads, each resolved to a specific version.

ID string

Type BetaManagedAgentsAgentReferenceType

Version int64

Type BetaManagedAgentsMultiagentType



type BetaManagedAgentsMultiagentParamsResp struct{…}

A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.



Agents [][BetaManagedAgentsMultiagentRosterEntryParamsUnionResp](api/beta.md)

Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

One of the following:

string



type BetaManagedAgentsAgentParamsResp struct{…}

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

ID string

The `agent` ID.

Type BetaManagedAgentsAgentParamsType

Version int64Optional

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.



type BetaManagedAgentsMultiagentSelfParamsResp struct{…}

Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

Type BetaManagedAgentsMultiagentSelfParamsType

Type BetaManagedAgentsMultiagentParamsType



type BetaManagedAgentsMultiagentRosterEntryParamsUnionResp interface{…}

An entry in a multiagent roster: an agent ID string, a versioned agent reference, or `self`.

One of the following:

string



type BetaManagedAgentsAgentParamsResp struct{…}

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

ID string

The `agent` ID.

Type BetaManagedAgentsAgentParamsType

Version int64Optional

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.



type BetaManagedAgentsMultiagentSelfParamsResp struct{…}

Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

Type BetaManagedAgentsMultiagentSelfParamsType



type BetaManagedAgentsOutcomeEvaluationResource struct{…}

Evaluation state for a single outcome defined via a define\_outcome event.

CompletedAt Time

A timestamp in RFC 3339 format

Description string

What the agent should produce.

Explanation string

Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs\_revision (intermediate), what's missing; for failed, why unrecoverable.

Iteration int64

0-indexed revision cycle the outcome is currently on.

OutcomeID string

Server-generated outc\_ ID for this outcome.

Result string

Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

Type BetaManagedAgentsOutcomeEvaluationResourceType



type BetaManagedAgentsSession struct{…}

A Managed Agents `session`.

ID string



Agent [BetaManagedAgentsSessionAgent](api/beta.md)

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

ArchivedAt Time

A timestamp in RFC 3339 format

CreatedAt Time

A timestamp in RFC 3339 format

EnvironmentID string

Metadata map[string, string]



OutcomeEvaluations [][BetaManagedAgentsOutcomeEvaluationResource](api/beta.md)

Per-outcome evaluation state. One entry per define\_outcome event sent to the session.

CompletedAt Time

A timestamp in RFC 3339 format

Description string

What the agent should produce.

Explanation string

Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs\_revision (intermediate), what's missing; for failed, why unrecoverable.

Iteration int64

0-indexed revision cycle the outcome is currently on.

OutcomeID string

Server-generated outc\_ ID for this outcome.

Result string

Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

Type BetaManagedAgentsOutcomeEvaluationResourceType



Resources [][BetaManagedAgentsSessionResourceUnion](api/beta.md)

One of the following:



type BetaManagedAgentsGitHubRepositoryResource struct{…}

ID string

CreatedAt Time

A timestamp in RFC 3339 format

MountPath string

Type BetaManagedAgentsGitHubRepositoryResourceType

UpdatedAt Time

A timestamp in RFC 3339 format

URL string



Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnionOptional

One of the following:



type BetaManagedAgentsBranchCheckout struct{…}

Name string

Branch name to check out.

Type BetaManagedAgentsBranchCheckoutType



type BetaManagedAgentsCommitCheckout struct{…}

Sha string

Full commit SHA to check out.

Type BetaManagedAgentsCommitCheckoutType



type BetaManagedAgentsFileResource struct{…}

ID string

CreatedAt Time

A timestamp in RFC 3339 format

FileID string

MountPath string

Type BetaManagedAgentsFileResourceType

UpdatedAt Time

A timestamp in RFC 3339 format



type BetaManagedAgentsMemoryStoreResource struct{…}

A memory store attached to an agent session.

MemoryStoreID string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type BetaManagedAgentsMemoryStoreResourceType



Access BetaManagedAgentsMemoryStoreResourceAccessOptional

Access mode for an attached memory store.

One of the following:

const BetaManagedAgentsMemoryStoreResourceAccessReadWrite BetaManagedAgentsMemoryStoreResourceAccess = "read\_write"

const BetaManagedAgentsMemoryStoreResourceAccessReadOnly BetaManagedAgentsMemoryStoreResourceAccess = "read\_only"

Description stringOptional

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

Instructions stringOptional

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

MountPath stringOptional

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

Name stringOptional

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.



Stats [BetaManagedAgentsSessionStats](api/beta.md)

Timing statistics for a session.

ActiveSeconds float64Optional

Cumulative time in seconds the session spent in running status. Excludes idle time.

DurationSeconds float64Optional

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.



Status BetaManagedAgentsSessionStatus

SessionStatus enum

One of the following:

const BetaManagedAgentsSessionStatusRescheduling BetaManagedAgentsSessionStatus = "rescheduling"

const BetaManagedAgentsSessionStatusRunning BetaManagedAgentsSessionStatus = "running"

const BetaManagedAgentsSessionStatusIdle BetaManagedAgentsSessionStatus = "idle"

const BetaManagedAgentsSessionStatusTerminated BetaManagedAgentsSessionStatus = "terminated"

Title string

Type BetaManagedAgentsSessionType

UpdatedAt Time

A timestamp in RFC 3339 format



Usage [BetaManagedAgentsSessionUsage](api/beta.md)

Cumulative token usage for a session across all turns.



CacheCreation [BetaManagedAgentsCacheCreationUsage](api/beta.md)Optional

Prompt-cache creation token usage broken down by cache lifetime.

Ephemeral1hInputTokens int64Optional

Tokens used to create 1-hour ephemeral cache entries.

Ephemeral5mInputTokens int64Optional

Tokens used to create 5-minute ephemeral cache entries.

CacheReadInputTokens int64Optional

Total tokens read from prompt cache.

InputTokens int64Optional

Total input tokens consumed across all turns.

OutputTokens int64Optional

Total output tokens generated across all turns.

VaultIDs []string

Vault IDs attached to the session at creation. Empty when no vaults were supplied.

DeploymentID stringOptional

Deployment ID when the session was created from a deployment reference. Null otherwise.



type BetaManagedAgentsSessionAgent struct{…}

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



type BetaManagedAgentsSessionAgentUpdate struct{…}

Mid-session agent configuration update. Only `tools` and `mcp_servers` are updatable. Full replacement: the provided array becomes the new value. To preserve existing entries, GET the session, modify the array, and POST it back.



MCPServers [][BetaManagedAgentsURLMCPServerParamsResp](api/beta.md)Optional

Replacement MCP server list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

Name string

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

Type BetaManagedAgentsURLMCPServerParamsType

URL string

Endpoint URL for the MCP server.



Tools []BetaManagedAgentsSessionAgentUpdateToolUnionOptional

Replacement tool list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

One of the following:



type BetaManagedAgentsAgentToolset20260401ParamsResp struct{…}

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

Type BetaManagedAgentsAgentToolset20260401ParamsType



Configs [][BetaManagedAgentsAgentToolConfigParamsResp](api/beta.md)Optional

Per-tool configuration overrides.



Name BetaManagedAgentsAgentToolConfigParamsName

Built-in agent tool identifier.

One of the following:

const BetaManagedAgentsAgentToolConfigParamsNameBash BetaManagedAgentsAgentToolConfigParamsName = "bash"

const BetaManagedAgentsAgentToolConfigParamsNameEdit BetaManagedAgentsAgentToolConfigParamsName = "edit"

const BetaManagedAgentsAgentToolConfigParamsNameRead BetaManagedAgentsAgentToolConfigParamsName = "read"

const BetaManagedAgentsAgentToolConfigParamsNameWrite BetaManagedAgentsAgentToolConfigParamsName = "write"

const BetaManagedAgentsAgentToolConfigParamsNameGlob BetaManagedAgentsAgentToolConfigParamsName = "glob"

const BetaManagedAgentsAgentToolConfigParamsNameGrep BetaManagedAgentsAgentToolConfigParamsName = "grep"

const BetaManagedAgentsAgentToolConfigParamsNameWebFetch BetaManagedAgentsAgentToolConfigParamsName = "web\_fetch"

const BetaManagedAgentsAgentToolConfigParamsNameWebSearch BetaManagedAgentsAgentToolConfigParamsName = "web\_search"

Enabled boolOptional

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.



PermissionPolicy BetaManagedAgentsAgentToolConfigParamsPermissionPolicyUnionRespOptional

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

DefaultConfig [BetaManagedAgentsAgentToolsetDefaultConfigParamsResp](api/beta.md)Optional

Default configuration for all tools in a toolset.

Enabled boolOptional

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.



PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigParamsPermissionPolicyUnionRespOptional

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

type BetaManagedAgentsMCPToolsetParamsResp struct{…}

Configuration for tools from an MCP server defined in `mcp_servers`.

MCPServerName string

Name of the MCP server. Must match a server name from the mcp\_servers array. 1-255 characters.

Type BetaManagedAgentsMCPToolsetParamsType



Configs [][BetaManagedAgentsMCPToolConfigParamsResp](api/beta.md)Optional

Per-tool configuration overrides.

Name string

Name of the MCP tool to configure. 1-128 characters.

Enabled boolOptional

Whether this tool is enabled. Overrides the `default_config` setting.



PermissionPolicy BetaManagedAgentsMCPToolConfigParamsPermissionPolicyUnionRespOptional

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

DefaultConfig [BetaManagedAgentsMCPToolsetDefaultConfigParamsResp](api/beta.md)Optional

Default configuration for all tools from an MCP server.

Enabled boolOptional

Whether tools are enabled by default. Defaults to true if not specified.



PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigParamsPermissionPolicyUnionRespOptional

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

type BetaManagedAgentsCustomToolParamsResp struct{…}

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

Description string

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.



InputSchema [BetaManagedAgentsCustomToolInputSchema](api/beta.md)

JSON Schema for custom tool input parameters.

Type Object

Properties map[string, any]Optional

Required []stringOptional

Name string

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

Type BetaManagedAgentsCustomToolParamsType



type BetaManagedAgentsSessionMultiagentCoordinator struct{…}

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



type BetaManagedAgentsSessionStats struct{…}

Timing statistics for a session.

ActiveSeconds float64Optional

Cumulative time in seconds the session spent in running status. Excludes idle time.

DurationSeconds float64Optional

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

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

type BetaManagedAgentsSessionUsage struct{…}

Cumulative token usage for a session across all turns.



CacheCreation [BetaManagedAgentsCacheCreationUsage](api/beta.md)Optional

Prompt-cache creation token usage broken down by cache lifetime.

Ephemeral1hInputTokens int64Optional

Tokens used to create 1-hour ephemeral cache entries.

Ephemeral5mInputTokens int64Optional

Tokens used to create 5-minute ephemeral cache entries.

CacheReadInputTokens int64Optional

Total tokens read from prompt cache.

InputTokens int64Optional

Total input tokens consumed across all turns.

OutputTokens int64Optional

Total output tokens generated across all turns.



type BetaManagedAgentsSystemContentBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsSystemContentBlockType

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

#### SessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

client.Beta.Sessions.Events.List(ctx, sessionID, params) (\*PageCursor[[BetaManagedAgentsSessionEventUnion](api/beta.md)], error)

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

client.Beta.Sessions.Events.Send(ctx, sessionID, params) (\*[BetaManagedAgentsSendSessionEvents](api/beta.md), error)

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

client.Beta.Sessions.Events.Stream(ctx, sessionID, query) (\*[BetaManagedAgentsStreamSessionEventsUnion](api/beta.md), error)

GET/v1/sessions/{session\_id}/events/stream

##### ModelsExpand Collapse

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

type BetaManagedAgentsAgentThreadContextCompactedEvent struct{…}

Indicates that context compaction (summarization) occurred during the session.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentThreadContextCompactedEventType

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

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType



type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

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

type BetaManagedAgentsEventParamsUnionResp interface{…}

Union type for event parameters that can be sent to a session.

One of the following:



type BetaManagedAgentsUserMessageEventParamsResp struct{…}

Parameters for sending a user message to the session.



Content []BetaManagedAgentsUserMessageEventParamsContentUnionResp

Array of content blocks for the user message.

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

Type BetaManagedAgentsUserMessageEventParamsType



type BetaManagedAgentsUserInterruptEventParamsResp struct{…}

Parameters for sending an interrupt to pause the agent.

Type BetaManagedAgentsUserInterruptEventParamsType

SessionThreadID stringOptional

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



type BetaManagedAgentsUserToolConfirmationEventParamsResp struct{…}

Parameters for confirming or denying a tool execution request.



Result BetaManagedAgentsUserToolConfirmationEventParamsResult

UserToolConfirmationResult enum

One of the following:

const BetaManagedAgentsUserToolConfirmationEventParamsResultAllow BetaManagedAgentsUserToolConfirmationEventParamsResult = "allow"

const BetaManagedAgentsUserToolConfirmationEventParamsResultDeny BetaManagedAgentsUserToolConfirmationEventParamsResult = "deny"

ToolUseID string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserToolConfirmationEventParamsType

DenyMessage stringOptional

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.



type BetaManagedAgentsUserCustomToolResultEventParamsResp struct{…}

Parameters for providing the result of a custom tool execution.

CustomToolUseID string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserCustomToolResultEventParamsType



Content []BetaManagedAgentsUserCustomToolResultEventParamsContentUnionRespOptional

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

type BetaManagedAgentsUserDefineOutcomeEventParamsResp struct{…}

Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

Description string

What the agent should produce. This is the task specification.



Rubric BetaManagedAgentsUserDefineOutcomeEventParamsRubricUnionResp

Rubric for grading the quality of an outcome.

One of the following:



type BetaManagedAgentsFileRubricParamsResp struct{…}

Rubric referenced by a file uploaded via the Files API.

FileID string

ID of the rubric file.

Type BetaManagedAgentsFileRubricParamsType



type BetaManagedAgentsTextRubricParamsResp struct{…}

Rubric content provided inline as text.

Content string

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

Type BetaManagedAgentsTextRubricParamsType

Type BetaManagedAgentsUserDefineOutcomeEventParamsType

MaxIterations int64Optional

Eval→revision cycles before giving up. Default 3, max 20.



type BetaManagedAgentsUserToolResultEventParamsResp struct{…}

Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

ToolUseID string

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserToolResultEventParamsType



Content []BetaManagedAgentsUserToolResultEventParamsContentUnionRespOptional

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

type BetaManagedAgentsSystemMessageEventParamsResp struct{…}

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.



Content [][BetaManagedAgentsSystemContentBlock](api/beta.md)

System content blocks to append. Text-only.

Text string

The text content.

Type BetaManagedAgentsSystemContentBlockType

Type BetaManagedAgentsSystemMessageEventParamsType



type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType



type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType



type BetaManagedAgentsFileRubric struct{…}

Rubric referenced by a file uploaded via the Files API.

FileID string

ID of the rubric file.

Type BetaManagedAgentsFileRubricType



type BetaManagedAgentsFileRubricParamsResp struct{…}

Rubric referenced by a file uploaded via the Files API.

FileID string

ID of the rubric file.

Type BetaManagedAgentsFileRubricParamsType

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

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType



type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType



type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType



type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

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



type BetaManagedAgentsSearchResultCitations struct{…}

Citation settings for a search result.

Enabled bool

Whether citations are enabled for this search result.



type BetaManagedAgentsSearchResultContent struct{…}

Text content within a search result.

Text string

The text content.

Type BetaManagedAgentsSearchResultContentType



type BetaManagedAgentsSendSessionEvents struct{…}

Events that were successfully sent to the session.



Data []BetaManagedAgentsSendSessionEventsDataUnionOptional

Sent events

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



type BetaManagedAgentsSessionDeletedEvent struct{…}

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionDeletedEventType



type BetaManagedAgentsSessionEndTurn struct{…}

The agent completed its turn naturally and is ready for the next user message.

Type BetaManagedAgentsSessionEndTurnType

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

type BetaManagedAgentsSpanModelRequestStartEvent struct{…}

Emitted when a model request is initiated by the agent.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSpanModelRequestStartEventType



type BetaManagedAgentsSpanModelUsage struct{…}

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

type BetaManagedAgentsStreamSessionEventsUnion interface{…}

Server-sent event in the session stream.

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



type BetaManagedAgentsSystemMessageEventParamsResp struct{…}

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.



Content [][BetaManagedAgentsSystemContentBlock](api/beta.md)

System content blocks to append. Text-only.

Text string

The text content.

Type BetaManagedAgentsSystemContentBlockType

Type BetaManagedAgentsSystemMessageEventParamsType



type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType



type BetaManagedAgentsTextRubric struct{…}

Rubric content provided inline as text.

Content string

Rubric content. Plain text or markdown — the grader treats it as freeform text.

Type BetaManagedAgentsTextRubricType



type BetaManagedAgentsTextRubricParamsResp struct{…}

Rubric content provided inline as text.

Content string

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

Type BetaManagedAgentsTextRubricParamsType

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

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.



type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

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

type BetaManagedAgentsUserCustomToolResultEventParamsResp struct{…}

Parameters for providing the result of a custom tool execution.

CustomToolUseID string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserCustomToolResultEventParamsType



Content []BetaManagedAgentsUserCustomToolResultEventParamsContentUnionRespOptional

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

type BetaManagedAgentsUserDefineOutcomeEventParamsResp struct{…}

Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

Description string

What the agent should produce. This is the task specification.



Rubric BetaManagedAgentsUserDefineOutcomeEventParamsRubricUnionResp

Rubric for grading the quality of an outcome.

One of the following:



type BetaManagedAgentsFileRubricParamsResp struct{…}

Rubric referenced by a file uploaded via the Files API.

FileID string

ID of the rubric file.

Type BetaManagedAgentsFileRubricParamsType



type BetaManagedAgentsTextRubricParamsResp struct{…}

Rubric content provided inline as text.

Content string

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

Type BetaManagedAgentsTextRubricParamsType

Type BetaManagedAgentsUserDefineOutcomeEventParamsType

MaxIterations int64Optional

Eval→revision cycles before giving up. Default 3, max 20.

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

type BetaManagedAgentsUserInterruptEventParamsResp struct{…}

Parameters for sending an interrupt to pause the agent.

Type BetaManagedAgentsUserInterruptEventParamsType

SessionThreadID stringOptional

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

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

type BetaManagedAgentsUserMessageEventParamsResp struct{…}

Parameters for sending a user message to the session.



Content []BetaManagedAgentsUserMessageEventParamsContentUnionResp

Array of content blocks for the user message.

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

Type BetaManagedAgentsUserMessageEventParamsType

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

type BetaManagedAgentsUserToolConfirmationEventParamsResp struct{…}

Parameters for confirming or denying a tool execution request.



Result BetaManagedAgentsUserToolConfirmationEventParamsResult

UserToolConfirmationResult enum

One of the following:

const BetaManagedAgentsUserToolConfirmationEventParamsResultAllow BetaManagedAgentsUserToolConfirmationEventParamsResult = "allow"

const BetaManagedAgentsUserToolConfirmationEventParamsResultDeny BetaManagedAgentsUserToolConfirmationEventParamsResult = "deny"

ToolUseID string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserToolConfirmationEventParamsType

DenyMessage stringOptional

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.



type BetaManagedAgentsUserToolResultEventParamsResp struct{…}

Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

ToolUseID string

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserToolResultEventParamsType



Content []BetaManagedAgentsUserToolResultEventParamsContentUnionRespOptional

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

#### SessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

client.Beta.Sessions.Resources.Add(ctx, sessionID, params) (\*[BetaManagedAgentsFileResource](api/beta.md), error)

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

client.Beta.Sessions.Resources.List(ctx, sessionID, params) (\*PageCursor[[BetaManagedAgentsSessionResourceUnion](api/beta.md)], error)

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

client.Beta.Sessions.Resources.Get(ctx, resourceID, params) (\*[BetaSessionResourceGetResponseUnion](api/beta.md), error)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

client.Beta.Sessions.Resources.Update(ctx, resourceID, params) (\*[BetaSessionResourceUpdateResponseUnion](api/beta.md), error)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

client.Beta.Sessions.Resources.Delete(ctx, resourceID, params) (\*[BetaManagedAgentsDeleteSessionResource](api/beta.md), error)

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

##### ModelsExpand Collapse



type BetaManagedAgentsDeleteSessionResource struct{…}

Confirmation of resource deletion.

ID string

Type BetaManagedAgentsDeleteSessionResourceType



type BetaManagedAgentsFileResource struct{…}

ID string

CreatedAt Time

A timestamp in RFC 3339 format

FileID string

MountPath string

Type BetaManagedAgentsFileResourceType

UpdatedAt Time

A timestamp in RFC 3339 format



type BetaManagedAgentsGitHubRepositoryResource struct{…}

ID string

CreatedAt Time

A timestamp in RFC 3339 format

MountPath string

Type BetaManagedAgentsGitHubRepositoryResourceType

UpdatedAt Time

A timestamp in RFC 3339 format

URL string



Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnionOptional

One of the following:



type BetaManagedAgentsBranchCheckout struct{…}

Name string

Branch name to check out.

Type BetaManagedAgentsBranchCheckoutType



type BetaManagedAgentsCommitCheckout struct{…}

Sha string

Full commit SHA to check out.

Type BetaManagedAgentsCommitCheckoutType



type BetaManagedAgentsMemoryStoreResource struct{…}

A memory store attached to an agent session.

MemoryStoreID string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type BetaManagedAgentsMemoryStoreResourceType



Access BetaManagedAgentsMemoryStoreResourceAccessOptional

Access mode for an attached memory store.

One of the following:

const BetaManagedAgentsMemoryStoreResourceAccessReadWrite BetaManagedAgentsMemoryStoreResourceAccess = "read\_write"

const BetaManagedAgentsMemoryStoreResourceAccessReadOnly BetaManagedAgentsMemoryStoreResourceAccess = "read\_only"

Description stringOptional

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

Instructions stringOptional

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

MountPath stringOptional

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

Name stringOptional

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.



type BetaManagedAgentsSessionResourceUnion interface{…}

A memory store attached to an agent session.

One of the following:



type BetaManagedAgentsGitHubRepositoryResource struct{…}

ID string

CreatedAt Time

A timestamp in RFC 3339 format

MountPath string

Type BetaManagedAgentsGitHubRepositoryResourceType

UpdatedAt Time

A timestamp in RFC 3339 format

URL string



Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnionOptional

One of the following:



type BetaManagedAgentsBranchCheckout struct{…}

Name string

Branch name to check out.

Type BetaManagedAgentsBranchCheckoutType



type BetaManagedAgentsCommitCheckout struct{…}

Sha string

Full commit SHA to check out.

Type BetaManagedAgentsCommitCheckoutType



type BetaManagedAgentsFileResource struct{…}

ID string

CreatedAt Time

A timestamp in RFC 3339 format

FileID string

MountPath string

Type BetaManagedAgentsFileResourceType

UpdatedAt Time

A timestamp in RFC 3339 format



type BetaManagedAgentsMemoryStoreResource struct{…}

A memory store attached to an agent session.

MemoryStoreID string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type BetaManagedAgentsMemoryStoreResourceType



Access BetaManagedAgentsMemoryStoreResourceAccessOptional

Access mode for an attached memory store.

One of the following:

const BetaManagedAgentsMemoryStoreResourceAccessReadWrite BetaManagedAgentsMemoryStoreResourceAccess = "read\_write"

const BetaManagedAgentsMemoryStoreResourceAccessReadOnly BetaManagedAgentsMemoryStoreResourceAccess = "read\_only"

Description stringOptional

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

Instructions stringOptional

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

MountPath stringOptional

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

Name stringOptional

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### SessionsThreads

##### [List Session Threads](api/beta/sessions/threads/list.md)

client.Beta.Sessions.Threads.List(ctx, sessionID, params) (\*PageCursor[[BetaManagedAgentsSessionThread](api/beta.md)], error)

GET/v1/sessions/{session\_id}/threads

##### [Get Session Thread](api/beta/sessions/threads/retrieve.md)

client.Beta.Sessions.Threads.Get(ctx, threadID, params) (\*[BetaManagedAgentsSessionThread](api/beta.md), error)

GET/v1/sessions/{session\_id}/threads/{thread\_id}

##### [Archive Session Thread](api/beta/sessions/threads/archive.md)

client.Beta.Sessions.Threads.Archive(ctx, threadID, params) (\*[BetaManagedAgentsSessionThread](api/beta.md), error)

POST/v1/sessions/{session\_id}/threads/{thread\_id}/archive

##### ModelsExpand Collapse



type BetaManagedAgentsSessionThread struct{…}

An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

ID string

Unique identifier for this thread.



Agent [BetaManagedAgentsSessionThreadAgent](api/beta.md)

Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

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

ArchivedAt Time

A timestamp in RFC 3339 format

CreatedAt Time

A timestamp in RFC 3339 format

ParentThreadID string

Parent thread that spawned this thread. Null for the primary thread.

SessionID string

The session this thread belongs to.



Stats [BetaManagedAgentsSessionThreadStats](api/beta.md)

Timing statistics for a session thread.

ActiveSeconds float64Optional

Cumulative time in seconds the thread spent actively running. Excludes idle time.

DurationSeconds float64Optional

Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

StartupSeconds float64Optional

Time in seconds for the thread to begin running. Zero for child threads, which start immediately.



Status [BetaManagedAgentsSessionThreadStatus](api/beta.md)

SessionThreadStatus enum

One of the following:

const BetaManagedAgentsSessionThreadStatusRunning [BetaManagedAgentsSessionThreadStatus](api/beta.md) = "running"

const BetaManagedAgentsSessionThreadStatusIdle [BetaManagedAgentsSessionThreadStatus](api/beta.md) = "idle"

const BetaManagedAgentsSessionThreadStatusRescheduling [BetaManagedAgentsSessionThreadStatus](api/beta.md) = "rescheduling"

const BetaManagedAgentsSessionThreadStatusTerminated [BetaManagedAgentsSessionThreadStatus](api/beta.md) = "terminated"

Type BetaManagedAgentsSessionThreadType

UpdatedAt Time

A timestamp in RFC 3339 format



Usage [BetaManagedAgentsSessionThreadUsage](api/beta.md)

Cumulative token usage for a session thread across all turns.



CacheCreation [BetaManagedAgentsCacheCreationUsage](api/beta.md)Optional

Prompt-cache creation token usage broken down by cache lifetime.

Ephemeral1hInputTokens int64Optional

Tokens used to create 1-hour ephemeral cache entries.

Ephemeral5mInputTokens int64Optional

Tokens used to create 5-minute ephemeral cache entries.

CacheReadInputTokens int64Optional

Total tokens read from prompt cache.

InputTokens int64Optional

Total input tokens consumed across all turns.

OutputTokens int64Optional

Total output tokens generated across all turns.



type BetaManagedAgentsSessionThreadStats struct{…}

Timing statistics for a session thread.

ActiveSeconds float64Optional

Cumulative time in seconds the thread spent actively running. Excludes idle time.

DurationSeconds float64Optional

Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

StartupSeconds float64Optional

Time in seconds for the thread to begin running. Zero for child threads, which start immediately.



type BetaManagedAgentsSessionThreadStatus string

SessionThreadStatus enum

One of the following:

const BetaManagedAgentsSessionThreadStatusRunning [BetaManagedAgentsSessionThreadStatus](api/beta.md) = "running"

const BetaManagedAgentsSessionThreadStatusIdle [BetaManagedAgentsSessionThreadStatus](api/beta.md) = "idle"

const BetaManagedAgentsSessionThreadStatusRescheduling [BetaManagedAgentsSessionThreadStatus](api/beta.md) = "rescheduling"

const BetaManagedAgentsSessionThreadStatusTerminated [BetaManagedAgentsSessionThreadStatus](api/beta.md) = "terminated"



type BetaManagedAgentsSessionThreadUsage struct{…}

Cumulative token usage for a session thread across all turns.



CacheCreation [BetaManagedAgentsCacheCreationUsage](api/beta.md)Optional

Prompt-cache creation token usage broken down by cache lifetime.

Ephemeral1hInputTokens int64Optional

Tokens used to create 1-hour ephemeral cache entries.

Ephemeral5mInputTokens int64Optional

Tokens used to create 5-minute ephemeral cache entries.

CacheReadInputTokens int64Optional

Total tokens read from prompt cache.

InputTokens int64Optional

Total input tokens consumed across all turns.

OutputTokens int64Optional

Total output tokens generated across all turns.



type BetaManagedAgentsStreamSessionThreadEventsUnion interface{…}

Server-sent event in a single thread's stream.

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

#### SessionsThreadsEvents

##### [List Session Thread Events](api/beta/sessions/threads/events/list.md)

client.Beta.Sessions.Threads.Events.List(ctx, threadID, params) (\*PageCursor[[BetaManagedAgentsSessionEventUnion](api/beta.md)], error)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/beta/sessions/threads/events/stream.md)

client.Beta.Sessions.Threads.Events.Stream(ctx, threadID, params) (\*[BetaManagedAgentsStreamSessionThreadEventsUnion](api/beta.md), error)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

---

*Copyright © Anthropic. All rights reserved.*
