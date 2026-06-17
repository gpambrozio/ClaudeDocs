# Sessions

Copy page



Java

# Sessions

##### [Create Session](api/beta/sessions/create.md)

[BetaManagedAgentsSession](api/beta.md) beta().sessions().create(SessionCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

SessionListPage beta().sessions().list(SessionListParamsparams = SessionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

[BetaManagedAgentsSession](api/beta.md) beta().sessions().retrieve(SessionRetrieveParamsparams = SessionRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

[BetaManagedAgentsSession](api/beta.md) beta().sessions().update(SessionUpdateParamsparams = SessionUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

[BetaManagedAgentsDeletedSession](api/beta.md) beta().sessions().delete(SessionDeleteParamsparams = SessionDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

[BetaManagedAgentsSession](api/beta.md) beta().sessions().archive(SessionArchiveParamsparams = SessionArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/sessions/{session\_id}/archive

##### ModelsExpand Collapse



class BetaManagedAgentsAgentParams:

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

String id

The `agent` ID.

Type type

Optional<Long> version

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.



class BetaManagedAgentsBranchCheckout:

String name

Branch name to check out.

Type type



class BetaManagedAgentsCacheCreationUsage:

Prompt-cache creation token usage broken down by cache lifetime.

Optional<Long> ephemeral1hInputTokens

Tokens used to create 1-hour ephemeral cache entries.

Optional<Long> ephemeral5mInputTokens

Tokens used to create 5-minute ephemeral cache entries.



class BetaManagedAgentsCommitCheckout:

String sha

Full commit SHA to check out.

Type type



class BetaManagedAgentsDeletedSession:

Confirmation that a `session` has been permanently deleted.

String id

Type type



class BetaManagedAgentsFileResourceParams:

Mount a file uploaded via the Files API into the session.

String fileId

ID of a previously uploaded file.

Type type

Optional<String> mountPath

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.



class BetaManagedAgentsGitHubRepositoryResourceParams:

Mount a GitHub repository into the session's container.

String authorizationToken

GitHub authorization token used to clone the repository.

Type type

String url

Github URL of the repository



Optional<Checkout> checkout

Branch or commit to check out. Defaults to the repository's default branch.

One of the following:



class BetaManagedAgentsBranchCheckout:

String name

Branch name to check out.

Type type



class BetaManagedAgentsCommitCheckout:

String sha

Full commit SHA to check out.

Type type

Optional<String> mountPath

Mount path in the container. Defaults to `/workspace/<repo-name>`.



class BetaManagedAgentsMemoryStoreResourceParam:

Parameters for attaching a memory store to an agent session.

String memoryStoreId

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type type



Optional<Access> access

Access mode for an attached memory store.

One of the following:

READ\_WRITE("read\_write")

READ\_ONLY("read\_only")

Optional<String> instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.



class BetaManagedAgentsMultiagent:

Resolved coordinator topology with a concrete agent roster.



List<[BetaManagedAgentsAgentReference](api/beta.md)> agents

Agents the coordinator may spawn as session threads, each resolved to a specific version.

String id

Type type

long version

Type type



class BetaManagedAgentsMultiagentParams:

A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.



List<[BetaManagedAgentsMultiagentRosterEntryParams](api/beta.md)> agents

Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

One of the following:

String



class BetaManagedAgentsAgentParams:

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

String id

The `agent` ID.

Type type

Optional<Long> version

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.



class BetaManagedAgentsMultiagentSelfParams:

Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

Type type

Type type



class BetaManagedAgentsMultiagentRosterEntryParams: A class that can be one of several variants.union 

An entry in a multiagent roster: an agent ID string, a versioned agent reference, or `self`.

String



class BetaManagedAgentsAgentParams:

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

String id

The `agent` ID.

Type type

Optional<Long> version

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.



class BetaManagedAgentsMultiagentSelfParams:

Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

Type type



class BetaManagedAgentsOutcomeEvaluationResource:

Evaluation state for a single outcome defined via a define\_outcome event.

Optional<LocalDateTime> completedAt

A timestamp in RFC 3339 format

String description

What the agent should produce.

Optional<String> explanation

Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs\_revision (intermediate), what's missing; for failed, why unrecoverable.

long iteration

0-indexed revision cycle the outcome is currently on.

String outcomeId

Server-generated outc\_ ID for this outcome.

String result

Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

Type type



class BetaManagedAgentsSession:

A Managed Agents `session`.

String id



[BetaManagedAgentsSessionAgent](api/beta.md) agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

String id

Optional<String> description



List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> mcpServers

String name

Type type

String url



[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.



BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")



Optional<[BetaManagedAgentsSessionMultiagentCoordinator](api/beta.md)> multiagent

Resolved coordinator topology with full agent definitions for each roster member.



List<[BetaManagedAgentsSessionThreadAgent](api/beta.md)> agents

Full `agent` definitions the coordinator may spawn as session threads.

String id

Optional<String> description



List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> mcpServers

String name

Type type

String url



[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.



BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")

String name



List<Skill> skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system



List<Tool> tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled



Name name

Built-in agent tool identifier.

One of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type



class BetaManagedAgentsMcpToolset:



List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description



[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required

String name

Type type

Type type

long version

Type type

String name



List<Skill> skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system



List<Tool> tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled



Name name

Built-in agent tool identifier.

One of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type



class BetaManagedAgentsMcpToolset:



List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description



[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required

String name

Type type

Type type

long version

Optional<LocalDateTime> archivedAt

A timestamp in RFC 3339 format

LocalDateTime createdAt

A timestamp in RFC 3339 format

String environmentId

Metadata metadata



List<[BetaManagedAgentsOutcomeEvaluationResource](api/beta.md)> outcomeEvaluations

Per-outcome evaluation state. One entry per define\_outcome event sent to the session.

Optional<LocalDateTime> completedAt

A timestamp in RFC 3339 format

String description

What the agent should produce.

Optional<String> explanation

Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs\_revision (intermediate), what's missing; for failed, why unrecoverable.

long iteration

0-indexed revision cycle the outcome is currently on.

String outcomeId

Server-generated outc\_ ID for this outcome.

String result

Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

Type type



List<[BetaManagedAgentsSessionResource](api/beta.md)> resources

One of the following:



class BetaManagedAgentsGitHubRepositoryResource:

String id

LocalDateTime createdAt

A timestamp in RFC 3339 format

String mountPath

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

String url



Optional<Checkout> checkout

One of the following:



class BetaManagedAgentsBranchCheckout:

String name

Branch name to check out.

Type type



class BetaManagedAgentsCommitCheckout:

String sha

Full commit SHA to check out.

Type type



class BetaManagedAgentsFileResource:

String id

LocalDateTime createdAt

A timestamp in RFC 3339 format

String fileId

String mountPath

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsMemoryStoreResource:

A memory store attached to an agent session.

String memoryStoreId

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type type



Optional<Access> access

Access mode for an attached memory store.

One of the following:

READ\_WRITE("read\_write")

READ\_ONLY("read\_only")

Optional<String> description

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

Optional<String> instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

Optional<String> mountPath

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

Optional<String> name

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.



[BetaManagedAgentsSessionStats](api/beta.md) stats

Timing statistics for a session.

Optional<Double> activeSeconds

Cumulative time in seconds the session spent in running status. Excludes idle time.

Optional<Double> durationSeconds

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.



Status status

SessionStatus enum

One of the following:

RESCHEDULING("rescheduling")

RUNNING("running")

IDLE("idle")

TERMINATED("terminated")

Optional<String> title

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format



[BetaManagedAgentsSessionUsage](api/beta.md) usage

Cumulative token usage for a session across all turns.



Optional<[BetaManagedAgentsCacheCreationUsage](api/beta.md)> cacheCreation

Prompt-cache creation token usage broken down by cache lifetime.

Optional<Long> ephemeral1hInputTokens

Tokens used to create 1-hour ephemeral cache entries.

Optional<Long> ephemeral5mInputTokens

Tokens used to create 5-minute ephemeral cache entries.

Optional<Long> cacheReadInputTokens

Total tokens read from prompt cache.

Optional<Long> inputTokens

Total input tokens consumed across all turns.

Optional<Long> outputTokens

Total output tokens generated across all turns.

List<String> vaultIds

Vault IDs attached to the session at creation. Empty when no vaults were supplied.

Optional<String> deploymentId

Deployment ID when the session was created from a deployment reference. Null otherwise.



class BetaManagedAgentsSessionAgent:

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

String id

Optional<String> description



List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> mcpServers

String name

Type type

String url



[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.



BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")



Optional<[BetaManagedAgentsSessionMultiagentCoordinator](api/beta.md)> multiagent

Resolved coordinator topology with full agent definitions for each roster member.



List<[BetaManagedAgentsSessionThreadAgent](api/beta.md)> agents

Full `agent` definitions the coordinator may spawn as session threads.

String id

Optional<String> description



List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> mcpServers

String name

Type type

String url



[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.



BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")

String name



List<Skill> skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system



List<Tool> tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled



Name name

Built-in agent tool identifier.

One of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type



class BetaManagedAgentsMcpToolset:



List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description



[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required

String name

Type type

Type type

long version

Type type

String name



List<Skill> skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system



List<Tool> tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled



Name name

Built-in agent tool identifier.

One of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type



class BetaManagedAgentsMcpToolset:



List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description



[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required

String name

Type type

Type type

long version



class BetaManagedAgentsSessionAgentUpdate:

Mid-session agent configuration update. Only `tools` and `mcp_servers` are updatable. Full replacement: the provided array becomes the new value. To preserve existing entries, GET the session, modify the array, and POST it back.



Optional<List<[BetaManagedAgentsUrlMcpServerParams](api/beta.md)>> mcpServers

Replacement MCP server list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

String name

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

Type type

String url

Endpoint URL for the MCP server.



Optional<List<Tool>> tools

Replacement tool list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

One of the following:



class BetaManagedAgentsAgentToolset20260401Params:

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

Type type



Optional<List<[BetaManagedAgentsAgentToolConfigParams](api/beta.md)>> configs

Per-tool configuration overrides.



Name name

Built-in agent tool identifier.

One of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")

Optional<Boolean> enabled

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.



Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



Optional<[BetaManagedAgentsAgentToolsetDefaultConfigParams](api/beta.md)> defaultConfig

Default configuration for all tools in a toolset.

Optional<Boolean> enabled

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.



Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



class BetaManagedAgentsMcpToolsetParams:

Configuration for tools from an MCP server defined in `mcp_servers`.

String mcpServerName

Name of the MCP server. Must match a server name from the mcp\_servers array. 1-255 characters.

Type type



Optional<List<[BetaManagedAgentsMcpToolConfigParams](api/beta.md)>> configs

Per-tool configuration overrides.

String name

Name of the MCP tool to configure. 1-128 characters.

Optional<Boolean> enabled

Whether this tool is enabled. Overrides the `default_config` setting.



Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



Optional<[BetaManagedAgentsMcpToolsetDefaultConfigParams](api/beta.md)> defaultConfig

Default configuration for all tools from an MCP server.

Optional<Boolean> enabled

Whether tools are enabled by default. Defaults to true if not specified.



Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



class BetaManagedAgentsCustomToolParams:

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

String description

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.



[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required

String name

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

Type type



class BetaManagedAgentsSessionMultiagentCoordinator:

Resolved coordinator topology with full agent definitions for each roster member.



List<[BetaManagedAgentsSessionThreadAgent](api/beta.md)> agents

Full `agent` definitions the coordinator may spawn as session threads.

String id

Optional<String> description



List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> mcpServers

String name

Type type

String url



[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.



BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")

String name



List<Skill> skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system



List<Tool> tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled



Name name

Built-in agent tool identifier.

One of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type



class BetaManagedAgentsMcpToolset:



List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description



[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required

String name

Type type

Type type

long version

Type type



class BetaManagedAgentsSessionStats:

Timing statistics for a session.

Optional<Double> activeSeconds

Cumulative time in seconds the session spent in running status. Excludes idle time.

Optional<Double> durationSeconds

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.



class BetaManagedAgentsSessionUpdatedEvent:

Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



Optional<[BetaManagedAgentsSessionAgent](api/beta.md)> agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

String id

Optional<String> description



List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> mcpServers

String name

Type type

String url



[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.



BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")



Optional<[BetaManagedAgentsSessionMultiagentCoordinator](api/beta.md)> multiagent

Resolved coordinator topology with full agent definitions for each roster member.



List<[BetaManagedAgentsSessionThreadAgent](api/beta.md)> agents

Full `agent` definitions the coordinator may spawn as session threads.

String id

Optional<String> description



List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> mcpServers

String name

Type type

String url



[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.



BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")

String name



List<Skill> skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system



List<Tool> tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled



Name name

Built-in agent tool identifier.

One of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type



class BetaManagedAgentsMcpToolset:



List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description



[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required

String name

Type type

Type type

long version

Type type

String name



List<Skill> skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system



List<Tool> tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled



Name name

Built-in agent tool identifier.

One of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type



class BetaManagedAgentsMcpToolset:



List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description



[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required

String name

Type type

Type type

long version

Optional<Metadata> metadata

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

Optional<String> title

The session's new title. Present only when the update changed it.



class BetaManagedAgentsSessionUsage:

Cumulative token usage for a session across all turns.



Optional<[BetaManagedAgentsCacheCreationUsage](api/beta.md)> cacheCreation

Prompt-cache creation token usage broken down by cache lifetime.

Optional<Long> ephemeral1hInputTokens

Tokens used to create 1-hour ephemeral cache entries.

Optional<Long> ephemeral5mInputTokens

Tokens used to create 5-minute ephemeral cache entries.

Optional<Long> cacheReadInputTokens

Total tokens read from prompt cache.

Optional<Long> inputTokens

Total input tokens consumed across all turns.

Optional<Long> outputTokens

Total output tokens generated across all turns.



class BetaManagedAgentsSystemContentBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsSystemMessageEvent:

A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

String id

Unique identifier for this event.



List<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks. Text-only.

String text

The text content.

Type type

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsUserToolResultEvent:

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

String id

Unique identifier for this event.

String toolUseId

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

#### SessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

EventListPage beta().sessions().events().list(EventListParamsparams = EventListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

[BetaManagedAgentsSendSessionEvents](api/beta.md) beta().sessions().events().send(EventSendParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

[BetaManagedAgentsStreamSessionEvents](api/beta.md) beta().sessions().events().streamStreaming(EventStreamParamsparams = EventStreamParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}/events/stream

##### ModelsExpand Collapse



class BetaManagedAgentsAgentCustomToolUseEvent:

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String name

Name of the custom tool being called.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

Optional<String> sessionThreadId

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.



class BetaManagedAgentsAgentMcpToolResultEvent:

Event representing the result of an MCP tool execution.

String id

Unique identifier for this event.

String mcpToolUseId

The id of the `agent.mcp_tool_use` event this result corresponds to.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.



class BetaManagedAgentsAgentMcpToolUseEvent:

Event emitted when the agent invokes a tool provided by an MCP server.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String mcpServerName

Name of the MCP server providing the tool.

String name

Name of the MCP tool being used.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



Optional<EvaluatedPermission> evaluatedPermission

AgentEvaluatedPermission enum

One of the following:

ALLOW("allow")

ASK("ask")

DENY("deny")

Optional<String> sessionThreadId

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



class BetaManagedAgentsAgentMessageEvent:

An agent response event in the session conversation.

String id

Unique identifier for this event.



List<[BetaManagedAgentsTextBlock](api/beta.md)> content

Array of text blocks comprising the agent response.

String text

The text content.

Type type

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsAgentThinkingEvent:

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsAgentThreadContextCompactedEvent:

Indicates that context compaction (summarization) occurred during the session.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsAgentThreadMessageReceivedEvent:

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

String id

Unique identifier for this event.



List<Content> content

Message content blocks.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

String fromSessionThreadId

Public `sthr_` ID of the thread that sent the message.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

Optional<String> fromAgentName

Name of the callable agent this message came from. Absent when received from the primary agent.



class BetaManagedAgentsAgentThreadMessageSentEvent:

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

String id

Unique identifier for this event.



List<Content> content

Message content blocks.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String toSessionThreadId

Public `sthr_` ID of the thread the message was sent to.

Type type

Optional<String> toAgentName

Name of the callable agent this message was sent to. Absent when sent to the primary agent.



class BetaManagedAgentsAgentToolResultEvent:

Event representing the result of an agent tool execution.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String toolUseId

The id of the `agent.tool_use` event this result corresponds to.

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.



class BetaManagedAgentsAgentToolUseEvent:

Event emitted when the agent invokes a built-in agent tool.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String name

Name of the agent tool being used.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



Optional<EvaluatedPermission> evaluatedPermission

AgentEvaluatedPermission enum

One of the following:

ALLOW("allow")

ASK("ask")

DENY("deny")

Optional<String> sessionThreadId

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsCredentialHostUnreachableError:

An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

String credentialId

ID of the affected credential.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

String vaultId

ID of the vault containing the affected credential.



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsEventParams: A class that can be one of several variants.union 

Union type for event parameters that can be sent to a session.



class BetaManagedAgentsUserMessageEventParams:

Parameters for sending a user message to the session.



List<Content> content

Array of content blocks for the user message.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Type type



class BetaManagedAgentsUserInterruptEventParams:

Parameters for sending an interrupt to pause the agent.

Type type

Optional<String> sessionThreadId

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



class BetaManagedAgentsUserToolConfirmationEventParams:

Parameters for confirming or denying a tool execution request.



Result result

UserToolConfirmationResult enum

One of the following:

ALLOW("allow")

DENY("deny")

String toolUseId

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

Optional<String> denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.



class BetaManagedAgentsUserCustomToolResultEventParams:

Parameters for providing the result of a custom tool execution.

String customToolUseId

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.



class BetaManagedAgentsUserDefineOutcomeEventParams:

Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

String description

What the agent should produce. This is the task specification.



Rubric rubric

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubricParams:

Rubric referenced by a file uploaded via the Files API.

String fileId

ID of the rubric file.

Type type



class BetaManagedAgentsTextRubricParams:

Rubric content provided inline as text.

String content

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

Type type

Type type

Optional<Long> maxIterations

Eval→revision cycles before giving up. Default 3, max 20.



class BetaManagedAgentsUserToolResultEventParams:

Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

String toolUseId

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.



class BetaManagedAgentsSystemMessageEventParams:

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.



List<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks to append. Text-only.

String text

The text content.

Type type

Type type



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type



class BetaManagedAgentsFileRubric:

Rubric referenced by a file uploaded via the Files API.

String fileId

ID of the rubric file.

Type type



class BetaManagedAgentsFileRubricParams:

Rubric referenced by a file uploaded via the Files API.

String fileId

ID of the rubric file.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

String mcpServerName

Name of the MCP server that failed authentication.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

String mcpServerName

Name of the MCP server that failed to connect.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type



class BetaManagedAgentsSearchResultCitations:

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



class BetaManagedAgentsSearchResultContent:

Text content within a search result.

String text

The text content.

Type type



class BetaManagedAgentsSendSessionEvents:

Events that were successfully sent to the session.



Optional<List<Data>> data

Sent events

One of the following:



class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

String id

Unique identifier for this event.



List<Content> content

Array of content blocks comprising the user message.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

String id

Unique identifier for this event.

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

String id

Unique identifier for this event.



Result result

UserToolConfirmationResult enum

One of the following:

ALLOW("allow")

DENY("deny")

String toolUseId

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

Optional<String> denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.



class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

String id

Unique identifier for this event.

String customToolUseId

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.



class BetaManagedAgentsUserDefineOutcomeEvent:

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

String id

Unique identifier for this event.

String description

What the agent should produce. Copied from the input event.

Optional<Long> maxIterations

Evaluate-then-revise cycles before giving up. Default 3, max 20.

String outcomeId

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

LocalDateTime processedAt

A timestamp in RFC 3339 format



Rubric rubric

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubric:

Rubric referenced by a file uploaded via the Files API.

String fileId

ID of the rubric file.

Type type



class BetaManagedAgentsTextRubric:

Rubric content provided inline as text.

String content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

Type type

Type type



class BetaManagedAgentsUserToolResultEvent:

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

String id

Unique identifier for this event.

String toolUseId

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.



class BetaManagedAgentsSystemMessageEvent:

A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

String id

Unique identifier for this event.



List<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks. Text-only.

String text

The text content.

Type type

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsSessionDeletedEvent:

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

Type type



class BetaManagedAgentsSessionErrorEvent:

An error event indicating a problem occurred during session execution.

String id

Unique identifier for this event.



Error error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

One of the following:



class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

String mcpServerName

Name of the MCP server that failed to connect.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

String mcpServerName

Name of the MCP server that failed authentication.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsCredentialHostUnreachableError:

An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

String credentialId

ID of the affected credential.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

String vaultId

ID of the vault containing the affected credential.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionEvent: A class that can be one of several variants.union 

Union type for all event types in a session.



class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

String id

Unique identifier for this event.



List<Content> content

Array of content blocks comprising the user message.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

String id

Unique identifier for this event.

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

String id

Unique identifier for this event.



Result result

UserToolConfirmationResult enum

One of the following:

ALLOW("allow")

DENY("deny")

String toolUseId

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

Optional<String> denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.



class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

String id

Unique identifier for this event.

String customToolUseId

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.



class BetaManagedAgentsAgentCustomToolUseEvent:

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String name

Name of the custom tool being called.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

Optional<String> sessionThreadId

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.



class BetaManagedAgentsAgentMessageEvent:

An agent response event in the session conversation.

String id

Unique identifier for this event.



List<[BetaManagedAgentsTextBlock](api/beta.md)> content

Array of text blocks comprising the agent response.

String text

The text content.

Type type

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsAgentThinkingEvent:

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsAgentMcpToolUseEvent:

Event emitted when the agent invokes a tool provided by an MCP server.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String mcpServerName

Name of the MCP server providing the tool.

String name

Name of the MCP tool being used.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



Optional<EvaluatedPermission> evaluatedPermission

AgentEvaluatedPermission enum

One of the following:

ALLOW("allow")

ASK("ask")

DENY("deny")

Optional<String> sessionThreadId

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



class BetaManagedAgentsAgentMcpToolResultEvent:

Event representing the result of an MCP tool execution.

String id

Unique identifier for this event.

String mcpToolUseId

The id of the `agent.mcp_tool_use` event this result corresponds to.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.



class BetaManagedAgentsAgentToolUseEvent:

Event emitted when the agent invokes a built-in agent tool.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String name

Name of the agent tool being used.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



Optional<EvaluatedPermission> evaluatedPermission

AgentEvaluatedPermission enum

One of the following:

ALLOW("allow")

ASK("ask")

DENY("deny")

Optional<String> sessionThreadId

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



class BetaManagedAgentsAgentToolResultEvent:

Event representing the result of an agent tool execution.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String toolUseId

The id of the `agent.tool_use` event this result corresponds to.

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.



class BetaManagedAgentsAgentThreadMessageReceivedEvent:

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

String id

Unique identifier for this event.



List<Content> content

Message content blocks.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

String fromSessionThreadId

Public `sthr_` ID of the thread that sent the message.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

Optional<String> fromAgentName

Name of the callable agent this message came from. Absent when received from the primary agent.



class BetaManagedAgentsAgentThreadMessageSentEvent:

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

String id

Unique identifier for this event.



List<Content> content

Message content blocks.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String toSessionThreadId

Public `sthr_` ID of the thread the message was sent to.

Type type

Optional<String> toAgentName

Name of the callable agent this message was sent to. Absent when sent to the primary agent.



class BetaManagedAgentsAgentThreadContextCompactedEvent:

Indicates that context compaction (summarization) occurred during the session.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionErrorEvent:

An error event indicating a problem occurred during session execution.

String id

Unique identifier for this event.



Error error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

One of the following:



class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

String mcpServerName

Name of the MCP server that failed to connect.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

String mcpServerName

Name of the MCP server that failed authentication.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsCredentialHostUnreachableError:

An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

String credentialId

ID of the affected credential.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

String vaultId

ID of the vault containing the affected credential.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionStatusRescheduledEvent:

Indicates the session is recovering from an error state and is rescheduled for execution.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionStatusRunningEvent:

Indicates the session is actively running and the agent is working.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionStatusIdleEvent:

Indicates the agent has paused and is awaiting user input.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format



StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

One of the following:



class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

Type type



class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

List<String> eventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type type



class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type type

Type type



class BetaManagedAgentsSessionStatusTerminatedEvent:

Indicates the session has terminated, either due to an error or completion.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionThreadCreatedEvent:

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

String id

Unique identifier for this event.

String agentName

Name of the callable agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public `sthr_` ID of the newly created thread.

Type type



class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:

Emitted when an outcome evaluation cycle begins.

String id

Unique identifier for this event.

long iteration

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

String outcomeId

The `outc_` ID of the outcome being evaluated.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

String id

Unique identifier for this event.

String explanation

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

long iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

String outcomeEvaluationStartId

The id of the corresponding `span.outcome_evaluation_start` event.

String outcomeId

The `outc_` ID of the outcome being evaluated.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String result

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

Type type



[BetaManagedAgentsSpanModelUsage](api/beta.md) usage

Token usage for a single model request.

long cacheCreationInputTokens

Tokens used to create prompt cache in this request.

long cacheReadInputTokens

Tokens read from prompt cache in this request.

long inputTokens

Input tokens consumed by this request.

long outputTokens

Output tokens generated by this request.



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")



class BetaManagedAgentsSpanModelRequestStartEvent:

Emitted when a model request is initiated by the agent.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSpanModelRequestEndEvent:

Emitted when a model request completes.

String id

Unique identifier for this event.

Optional<Boolean> isError

Whether the model request resulted in an error.

String modelRequestStartId

The id of the corresponding `span.model_request_start` event.



[BetaManagedAgentsSpanModelUsage](api/beta.md) modelUsage

Token usage for a single model request.

long cacheCreationInputTokens

Tokens used to create prompt cache in this request.

long cacheReadInputTokens

Tokens read from prompt cache in this request.

long inputTokens

Input tokens consumed by this request.

long outputTokens

Output tokens generated by this request.



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

String id

Unique identifier for this event.

long iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

String outcomeId

The `outc_` ID of the outcome being evaluated.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsUserDefineOutcomeEvent:

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

String id

Unique identifier for this event.

String description

What the agent should produce. Copied from the input event.

Optional<Long> maxIterations

Evaluate-then-revise cycles before giving up. Default 3, max 20.

String outcomeId

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

LocalDateTime processedAt

A timestamp in RFC 3339 format



Rubric rubric

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubric:

Rubric referenced by a file uploaded via the Files API.

String fileId

ID of the rubric file.

Type type



class BetaManagedAgentsTextRubric:

Rubric content provided inline as text.

String content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

Type type

Type type



class BetaManagedAgentsSessionDeletedEvent:

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionThreadStatusRunningEvent:

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

String id

Unique identifier for this event.

String agentName

Name of the agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public sthr\_ ID of the thread that started running.

Type type



class BetaManagedAgentsSessionThreadStatusIdleEvent:

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

String id

Unique identifier for this event.

String agentName

Name of the agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public sthr\_ ID of the thread that went idle.



StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

One of the following:



class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

Type type



class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

List<String> eventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type type



class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type type

Type type



class BetaManagedAgentsSessionThreadStatusTerminatedEvent:

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

String id

Unique identifier for this event.

String agentName

Name of the agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public sthr\_ ID of the thread that terminated.

Type type



class BetaManagedAgentsUserToolResultEvent:

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

String id

Unique identifier for this event.

String toolUseId

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.



class BetaManagedAgentsSessionThreadStatusRescheduledEvent:

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

String id

Unique identifier for this event.

String agentName

Name of the agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public sthr\_ ID of the thread that is retrying.

Type type



class BetaManagedAgentsSessionUpdatedEvent:

Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



Optional<[BetaManagedAgentsSessionAgent](api/beta.md)> agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

String id

Optional<String> description



List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> mcpServers

String name

Type type

String url



[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.



BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")



Optional<[BetaManagedAgentsSessionMultiagentCoordinator](api/beta.md)> multiagent

Resolved coordinator topology with full agent definitions for each roster member.



List<[BetaManagedAgentsSessionThreadAgent](api/beta.md)> agents

Full `agent` definitions the coordinator may spawn as session threads.

String id

Optional<String> description



List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> mcpServers

String name

Type type

String url



[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.



BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")

String name



List<Skill> skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system



List<Tool> tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled



Name name

Built-in agent tool identifier.

One of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type



class BetaManagedAgentsMcpToolset:



List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description



[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required

String name

Type type

Type type

long version

Type type

String name



List<Skill> skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system



List<Tool> tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled



Name name

Built-in agent tool identifier.

One of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type



class BetaManagedAgentsMcpToolset:



List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description



[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required

String name

Type type

Type type

long version

Optional<Metadata> metadata

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

Optional<String> title

The session's new title. Present only when the update changed it.



class BetaManagedAgentsSystemMessageEvent:

A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

String id

Unique identifier for this event.



List<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks. Text-only.

String text

The text content.

Type type

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

List<String> eventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type type



class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type type



class BetaManagedAgentsSessionStatusIdleEvent:

Indicates the agent has paused and is awaiting user input.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format



StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

One of the following:



class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

Type type



class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

List<String> eventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type type



class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type type

Type type



class BetaManagedAgentsSessionStatusRescheduledEvent:

Indicates the session is recovering from an error state and is rescheduled for execution.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionStatusRunningEvent:

Indicates the session is actively running and the agent is working.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionStatusTerminatedEvent:

Indicates the session has terminated, either due to an error or completion.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionThreadCreatedEvent:

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

String id

Unique identifier for this event.

String agentName

Name of the callable agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public `sthr_` ID of the newly created thread.

Type type



class BetaManagedAgentsSessionThreadStatusIdleEvent:

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

String id

Unique identifier for this event.

String agentName

Name of the agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public sthr\_ ID of the thread that went idle.



StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

One of the following:



class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

Type type



class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

List<String> eventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type type



class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type type

Type type



class BetaManagedAgentsSessionThreadStatusRescheduledEvent:

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

String id

Unique identifier for this event.

String agentName

Name of the agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public sthr\_ ID of the thread that is retrying.

Type type



class BetaManagedAgentsSessionThreadStatusRunningEvent:

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

String id

Unique identifier for this event.

String agentName

Name of the agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public sthr\_ ID of the thread that started running.

Type type



class BetaManagedAgentsSessionThreadStatusTerminatedEvent:

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

String id

Unique identifier for this event.

String agentName

Name of the agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public sthr\_ ID of the thread that terminated.

Type type



class BetaManagedAgentsSpanModelRequestEndEvent:

Emitted when a model request completes.

String id

Unique identifier for this event.

Optional<Boolean> isError

Whether the model request resulted in an error.

String modelRequestStartId

The id of the corresponding `span.model_request_start` event.



[BetaManagedAgentsSpanModelUsage](api/beta.md) modelUsage

Token usage for a single model request.

long cacheCreationInputTokens

Tokens used to create prompt cache in this request.

long cacheReadInputTokens

Tokens read from prompt cache in this request.

long inputTokens

Input tokens consumed by this request.

long outputTokens

Output tokens generated by this request.



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSpanModelRequestStartEvent:

Emitted when a model request is initiated by the agent.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSpanModelUsage:

Token usage for a single model request.

long cacheCreationInputTokens

Tokens used to create prompt cache in this request.

long cacheReadInputTokens

Tokens read from prompt cache in this request.

long inputTokens

Input tokens consumed by this request.

long outputTokens

Output tokens generated by this request.



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")



class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

String id

Unique identifier for this event.

String explanation

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

long iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

String outcomeEvaluationStartId

The id of the corresponding `span.outcome_evaluation_start` event.

String outcomeId

The `outc_` ID of the outcome being evaluated.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String result

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

Type type



[BetaManagedAgentsSpanModelUsage](api/beta.md) usage

Token usage for a single model request.

long cacheCreationInputTokens

Tokens used to create prompt cache in this request.

long cacheReadInputTokens

Tokens read from prompt cache in this request.

long inputTokens

Input tokens consumed by this request.

long outputTokens

Output tokens generated by this request.



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")



class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

String id

Unique identifier for this event.

long iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

String outcomeId

The `outc_` ID of the outcome being evaluated.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:

Emitted when an outcome evaluation cycle begins.

String id

Unique identifier for this event.

long iteration

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

String outcomeId

The `outc_` ID of the outcome being evaluated.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsStreamSessionEvents: A class that can be one of several variants.union 

Server-sent event in the session stream.



class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

String id

Unique identifier for this event.



List<Content> content

Array of content blocks comprising the user message.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

String id

Unique identifier for this event.

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

String id

Unique identifier for this event.



Result result

UserToolConfirmationResult enum

One of the following:

ALLOW("allow")

DENY("deny")

String toolUseId

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

Optional<String> denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.



class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

String id

Unique identifier for this event.

String customToolUseId

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.



class BetaManagedAgentsAgentCustomToolUseEvent:

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String name

Name of the custom tool being called.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

Optional<String> sessionThreadId

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.



class BetaManagedAgentsAgentMessageEvent:

An agent response event in the session conversation.

String id

Unique identifier for this event.



List<[BetaManagedAgentsTextBlock](api/beta.md)> content

Array of text blocks comprising the agent response.

String text

The text content.

Type type

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsAgentThinkingEvent:

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsAgentMcpToolUseEvent:

Event emitted when the agent invokes a tool provided by an MCP server.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String mcpServerName

Name of the MCP server providing the tool.

String name

Name of the MCP tool being used.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



Optional<EvaluatedPermission> evaluatedPermission

AgentEvaluatedPermission enum

One of the following:

ALLOW("allow")

ASK("ask")

DENY("deny")

Optional<String> sessionThreadId

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



class BetaManagedAgentsAgentMcpToolResultEvent:

Event representing the result of an MCP tool execution.

String id

Unique identifier for this event.

String mcpToolUseId

The id of the `agent.mcp_tool_use` event this result corresponds to.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.



class BetaManagedAgentsAgentToolUseEvent:

Event emitted when the agent invokes a built-in agent tool.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String name

Name of the agent tool being used.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



Optional<EvaluatedPermission> evaluatedPermission

AgentEvaluatedPermission enum

One of the following:

ALLOW("allow")

ASK("ask")

DENY("deny")

Optional<String> sessionThreadId

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



class BetaManagedAgentsAgentToolResultEvent:

Event representing the result of an agent tool execution.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String toolUseId

The id of the `agent.tool_use` event this result corresponds to.

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.



class BetaManagedAgentsAgentThreadMessageReceivedEvent:

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

String id

Unique identifier for this event.



List<Content> content

Message content blocks.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

String fromSessionThreadId

Public `sthr_` ID of the thread that sent the message.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

Optional<String> fromAgentName

Name of the callable agent this message came from. Absent when received from the primary agent.



class BetaManagedAgentsAgentThreadMessageSentEvent:

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

String id

Unique identifier for this event.



List<Content> content

Message content blocks.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String toSessionThreadId

Public `sthr_` ID of the thread the message was sent to.

Type type

Optional<String> toAgentName

Name of the callable agent this message was sent to. Absent when sent to the primary agent.



class BetaManagedAgentsAgentThreadContextCompactedEvent:

Indicates that context compaction (summarization) occurred during the session.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionErrorEvent:

An error event indicating a problem occurred during session execution.

String id

Unique identifier for this event.



Error error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

One of the following:



class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

String mcpServerName

Name of the MCP server that failed to connect.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

String mcpServerName

Name of the MCP server that failed authentication.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsCredentialHostUnreachableError:

An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

String credentialId

ID of the affected credential.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

String vaultId

ID of the vault containing the affected credential.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionStatusRescheduledEvent:

Indicates the session is recovering from an error state and is rescheduled for execution.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionStatusRunningEvent:

Indicates the session is actively running and the agent is working.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionStatusIdleEvent:

Indicates the agent has paused and is awaiting user input.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format



StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

One of the following:



class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

Type type



class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

List<String> eventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type type



class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type type

Type type



class BetaManagedAgentsSessionStatusTerminatedEvent:

Indicates the session has terminated, either due to an error or completion.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionThreadCreatedEvent:

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

String id

Unique identifier for this event.

String agentName

Name of the callable agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public `sthr_` ID of the newly created thread.

Type type



class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:

Emitted when an outcome evaluation cycle begins.

String id

Unique identifier for this event.

long iteration

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

String outcomeId

The `outc_` ID of the outcome being evaluated.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

String id

Unique identifier for this event.

String explanation

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

long iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

String outcomeEvaluationStartId

The id of the corresponding `span.outcome_evaluation_start` event.

String outcomeId

The `outc_` ID of the outcome being evaluated.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String result

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

Type type



[BetaManagedAgentsSpanModelUsage](api/beta.md) usage

Token usage for a single model request.

long cacheCreationInputTokens

Tokens used to create prompt cache in this request.

long cacheReadInputTokens

Tokens read from prompt cache in this request.

long inputTokens

Input tokens consumed by this request.

long outputTokens

Output tokens generated by this request.



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")



class BetaManagedAgentsSpanModelRequestStartEvent:

Emitted when a model request is initiated by the agent.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSpanModelRequestEndEvent:

Emitted when a model request completes.

String id

Unique identifier for this event.

Optional<Boolean> isError

Whether the model request resulted in an error.

String modelRequestStartId

The id of the corresponding `span.model_request_start` event.



[BetaManagedAgentsSpanModelUsage](api/beta.md) modelUsage

Token usage for a single model request.

long cacheCreationInputTokens

Tokens used to create prompt cache in this request.

long cacheReadInputTokens

Tokens read from prompt cache in this request.

long inputTokens

Input tokens consumed by this request.

long outputTokens

Output tokens generated by this request.



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

String id

Unique identifier for this event.

long iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

String outcomeId

The `outc_` ID of the outcome being evaluated.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsUserDefineOutcomeEvent:

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

String id

Unique identifier for this event.

String description

What the agent should produce. Copied from the input event.

Optional<Long> maxIterations

Evaluate-then-revise cycles before giving up. Default 3, max 20.

String outcomeId

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

LocalDateTime processedAt

A timestamp in RFC 3339 format



Rubric rubric

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubric:

Rubric referenced by a file uploaded via the Files API.

String fileId

ID of the rubric file.

Type type



class BetaManagedAgentsTextRubric:

Rubric content provided inline as text.

String content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

Type type

Type type



class BetaManagedAgentsSessionDeletedEvent:

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionThreadStatusRunningEvent:

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

String id

Unique identifier for this event.

String agentName

Name of the agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public sthr\_ ID of the thread that started running.

Type type



class BetaManagedAgentsSessionThreadStatusIdleEvent:

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

String id

Unique identifier for this event.

String agentName

Name of the agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public sthr\_ ID of the thread that went idle.



StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

One of the following:



class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

Type type



class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

List<String> eventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type type



class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type type

Type type



class BetaManagedAgentsSessionThreadStatusTerminatedEvent:

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

String id

Unique identifier for this event.

String agentName

Name of the agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public sthr\_ ID of the thread that terminated.

Type type



class BetaManagedAgentsUserToolResultEvent:

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

String id

Unique identifier for this event.

String toolUseId

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.



class BetaManagedAgentsSessionThreadStatusRescheduledEvent:

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

String id

Unique identifier for this event.

String agentName

Name of the agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public sthr\_ ID of the thread that is retrying.

Type type



class BetaManagedAgentsSessionUpdatedEvent:

Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



Optional<[BetaManagedAgentsSessionAgent](api/beta.md)> agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

String id

Optional<String> description



List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> mcpServers

String name

Type type

String url



[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.



BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")



Optional<[BetaManagedAgentsSessionMultiagentCoordinator](api/beta.md)> multiagent

Resolved coordinator topology with full agent definitions for each roster member.



List<[BetaManagedAgentsSessionThreadAgent](api/beta.md)> agents

Full `agent` definitions the coordinator may spawn as session threads.

String id

Optional<String> description



List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> mcpServers

String name

Type type

String url



[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.



BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")

String name



List<Skill> skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system



List<Tool> tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled



Name name

Built-in agent tool identifier.

One of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type



class BetaManagedAgentsMcpToolset:



List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description



[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required

String name

Type type

Type type

long version

Type type

String name



List<Skill> skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system



List<Tool> tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled



Name name

Built-in agent tool identifier.

One of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type



class BetaManagedAgentsMcpToolset:



List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description



[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required

String name

Type type

Type type

long version

Optional<Metadata> metadata

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

Optional<String> title

The session's new title. Present only when the update changed it.



class BetaManagedAgentsSystemMessageEvent:

A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

String id

Unique identifier for this event.



List<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks. Text-only.

String text

The text content.

Type type

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsSystemMessageEventParams:

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.



List<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks to append. Text-only.

String text

The text content.

Type type

Type type



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsTextRubric:

Rubric content provided inline as text.

String content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

Type type



class BetaManagedAgentsTextRubricParams:

Rubric content provided inline as text.

String content

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

Type type



class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

String id

Unique identifier for this event.

String customToolUseId

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.



class BetaManagedAgentsUserCustomToolResultEventParams:

Parameters for providing the result of a custom tool execution.

String customToolUseId

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.



class BetaManagedAgentsUserDefineOutcomeEvent:

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

String id

Unique identifier for this event.

String description

What the agent should produce. Copied from the input event.

Optional<Long> maxIterations

Evaluate-then-revise cycles before giving up. Default 3, max 20.

String outcomeId

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

LocalDateTime processedAt

A timestamp in RFC 3339 format



Rubric rubric

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubric:

Rubric referenced by a file uploaded via the Files API.

String fileId

ID of the rubric file.

Type type



class BetaManagedAgentsTextRubric:

Rubric content provided inline as text.

String content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

Type type

Type type



class BetaManagedAgentsUserDefineOutcomeEventParams:

Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

String description

What the agent should produce. This is the task specification.



Rubric rubric

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubricParams:

Rubric referenced by a file uploaded via the Files API.

String fileId

ID of the rubric file.

Type type



class BetaManagedAgentsTextRubricParams:

Rubric content provided inline as text.

String content

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

Type type

Type type

Optional<Long> maxIterations

Eval→revision cycles before giving up. Default 3, max 20.



class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

String id

Unique identifier for this event.

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



class BetaManagedAgentsUserInterruptEventParams:

Parameters for sending an interrupt to pause the agent.

Type type

Optional<String> sessionThreadId

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

String id

Unique identifier for this event.



List<Content> content

Array of content blocks comprising the user message.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsUserMessageEventParams:

Parameters for sending a user message to the session.



List<Content> content

Array of content blocks for the user message.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Type type



class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

String id

Unique identifier for this event.



Result result

UserToolConfirmationResult enum

One of the following:

ALLOW("allow")

DENY("deny")

String toolUseId

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

Optional<String> denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.



class BetaManagedAgentsUserToolConfirmationEventParams:

Parameters for confirming or denying a tool execution request.



Result result

UserToolConfirmationResult enum

One of the following:

ALLOW("allow")

DENY("deny")

String toolUseId

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

Optional<String> denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.



class BetaManagedAgentsUserToolResultEventParams:

Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

String toolUseId

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.

#### SessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

[BetaManagedAgentsFileResource](api/beta.md) beta().sessions().resources().add(ResourceAddParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

ResourceListPage beta().sessions().resources().list(ResourceListParamsparams = ResourceListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

[ResourceRetrieveResponse](api/beta.md) beta().sessions().resources().retrieve(ResourceRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

[ResourceUpdateResponse](api/beta.md) beta().sessions().resources().update(ResourceUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

[BetaManagedAgentsDeleteSessionResource](api/beta.md) beta().sessions().resources().delete(ResourceDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

##### ModelsExpand Collapse



class BetaManagedAgentsDeleteSessionResource:

Confirmation of resource deletion.

String id

Type type



class BetaManagedAgentsFileResource:

String id

LocalDateTime createdAt

A timestamp in RFC 3339 format

String fileId

String mountPath

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsGitHubRepositoryResource:

String id

LocalDateTime createdAt

A timestamp in RFC 3339 format

String mountPath

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

String url



Optional<Checkout> checkout

One of the following:



class BetaManagedAgentsBranchCheckout:

String name

Branch name to check out.

Type type



class BetaManagedAgentsCommitCheckout:

String sha

Full commit SHA to check out.

Type type



class BetaManagedAgentsMemoryStoreResource:

A memory store attached to an agent session.

String memoryStoreId

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type type



Optional<Access> access

Access mode for an attached memory store.

One of the following:

READ\_WRITE("read\_write")

READ\_ONLY("read\_only")

Optional<String> description

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

Optional<String> instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

Optional<String> mountPath

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

Optional<String> name

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.



class BetaManagedAgentsSessionResource: A class that can be one of several variants.union 

A memory store attached to an agent session.



class BetaManagedAgentsGitHubRepositoryResource:

String id

LocalDateTime createdAt

A timestamp in RFC 3339 format

String mountPath

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

String url



Optional<Checkout> checkout

One of the following:



class BetaManagedAgentsBranchCheckout:

String name

Branch name to check out.

Type type



class BetaManagedAgentsCommitCheckout:

String sha

Full commit SHA to check out.

Type type



class BetaManagedAgentsFileResource:

String id

LocalDateTime createdAt

A timestamp in RFC 3339 format

String fileId

String mountPath

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsMemoryStoreResource:

A memory store attached to an agent session.

String memoryStoreId

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type type



Optional<Access> access

Access mode for an attached memory store.

One of the following:

READ\_WRITE("read\_write")

READ\_ONLY("read\_only")

Optional<String> description

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

Optional<String> instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

Optional<String> mountPath

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

Optional<String> name

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### SessionsThreads

##### [List Session Threads](api/beta/sessions/threads/list.md)

ThreadListPage beta().sessions().threads().list(ThreadListParamsparams = ThreadListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}/threads

##### [Get Session Thread](api/beta/sessions/threads/retrieve.md)

[BetaManagedAgentsSessionThread](api/beta.md) beta().sessions().threads().retrieve(ThreadRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}/threads/{thread\_id}

##### [Archive Session Thread](api/beta/sessions/threads/archive.md)

[BetaManagedAgentsSessionThread](api/beta.md) beta().sessions().threads().archive(ThreadArchiveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/sessions/{session\_id}/threads/{thread\_id}/archive

##### ModelsExpand Collapse



class BetaManagedAgentsSessionThread:

An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

String id

Unique identifier for this thread.



[BetaManagedAgentsSessionThreadAgent](api/beta.md) agent

Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

String id

Optional<String> description



List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> mcpServers

String name

Type type

String url



[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.



BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")

String name



List<Skill> skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system



List<Tool> tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled



Name name

Built-in agent tool identifier.

One of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type



class BetaManagedAgentsMcpToolset:



List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description



[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required

String name

Type type

Type type

long version

Optional<LocalDateTime> archivedAt

A timestamp in RFC 3339 format

LocalDateTime createdAt

A timestamp in RFC 3339 format

Optional<String> parentThreadId

Parent thread that spawned this thread. Null for the primary thread.

String sessionId

The session this thread belongs to.



Optional<[BetaManagedAgentsSessionThreadStats](api/beta.md)> stats

Timing statistics for a session thread.

Optional<Double> activeSeconds

Cumulative time in seconds the thread spent actively running. Excludes idle time.

Optional<Double> durationSeconds

Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

Optional<Double> startupSeconds

Time in seconds for the thread to begin running. Zero for child threads, which start immediately.



[BetaManagedAgentsSessionThreadStatus](api/beta.md) status

SessionThreadStatus enum

One of the following:

RUNNING("running")

IDLE("idle")

RESCHEDULING("rescheduling")

TERMINATED("terminated")

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format



Optional<[BetaManagedAgentsSessionThreadUsage](api/beta.md)> usage

Cumulative token usage for a session thread across all turns.



Optional<[BetaManagedAgentsCacheCreationUsage](api/beta.md)> cacheCreation

Prompt-cache creation token usage broken down by cache lifetime.

Optional<Long> ephemeral1hInputTokens

Tokens used to create 1-hour ephemeral cache entries.

Optional<Long> ephemeral5mInputTokens

Tokens used to create 5-minute ephemeral cache entries.

Optional<Long> cacheReadInputTokens

Total tokens read from prompt cache.

Optional<Long> inputTokens

Total input tokens consumed across all turns.

Optional<Long> outputTokens

Total output tokens generated across all turns.



class BetaManagedAgentsSessionThreadStats:

Timing statistics for a session thread.

Optional<Double> activeSeconds

Cumulative time in seconds the thread spent actively running. Excludes idle time.

Optional<Double> durationSeconds

Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

Optional<Double> startupSeconds

Time in seconds for the thread to begin running. Zero for child threads, which start immediately.



enum BetaManagedAgentsSessionThreadStatus:

SessionThreadStatus enum

RUNNING("running")

IDLE("idle")

RESCHEDULING("rescheduling")

TERMINATED("terminated")



class BetaManagedAgentsSessionThreadUsage:

Cumulative token usage for a session thread across all turns.



Optional<[BetaManagedAgentsCacheCreationUsage](api/beta.md)> cacheCreation

Prompt-cache creation token usage broken down by cache lifetime.

Optional<Long> ephemeral1hInputTokens

Tokens used to create 1-hour ephemeral cache entries.

Optional<Long> ephemeral5mInputTokens

Tokens used to create 5-minute ephemeral cache entries.

Optional<Long> cacheReadInputTokens

Total tokens read from prompt cache.

Optional<Long> inputTokens

Total input tokens consumed across all turns.

Optional<Long> outputTokens

Total output tokens generated across all turns.



class BetaManagedAgentsStreamSessionThreadEvents: A class that can be one of several variants.union 

Server-sent event in a single thread's stream.



class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

String id

Unique identifier for this event.



List<Content> content

Array of content blocks comprising the user message.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

String id

Unique identifier for this event.

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

String id

Unique identifier for this event.



Result result

UserToolConfirmationResult enum

One of the following:

ALLOW("allow")

DENY("deny")

String toolUseId

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

Optional<String> denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.



class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

String id

Unique identifier for this event.

String customToolUseId

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.



class BetaManagedAgentsAgentCustomToolUseEvent:

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String name

Name of the custom tool being called.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

Optional<String> sessionThreadId

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.



class BetaManagedAgentsAgentMessageEvent:

An agent response event in the session conversation.

String id

Unique identifier for this event.



List<[BetaManagedAgentsTextBlock](api/beta.md)> content

Array of text blocks comprising the agent response.

String text

The text content.

Type type

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsAgentThinkingEvent:

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsAgentMcpToolUseEvent:

Event emitted when the agent invokes a tool provided by an MCP server.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String mcpServerName

Name of the MCP server providing the tool.

String name

Name of the MCP tool being used.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



Optional<EvaluatedPermission> evaluatedPermission

AgentEvaluatedPermission enum

One of the following:

ALLOW("allow")

ASK("ask")

DENY("deny")

Optional<String> sessionThreadId

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



class BetaManagedAgentsAgentMcpToolResultEvent:

Event representing the result of an MCP tool execution.

String id

Unique identifier for this event.

String mcpToolUseId

The id of the `agent.mcp_tool_use` event this result corresponds to.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.



class BetaManagedAgentsAgentToolUseEvent:

Event emitted when the agent invokes a built-in agent tool.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String name

Name of the agent tool being used.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



Optional<EvaluatedPermission> evaluatedPermission

AgentEvaluatedPermission enum

One of the following:

ALLOW("allow")

ASK("ask")

DENY("deny")

Optional<String> sessionThreadId

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.



class BetaManagedAgentsAgentToolResultEvent:

Event representing the result of an agent tool execution.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String toolUseId

The id of the `agent.tool_use` event this result corresponds to.

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.



class BetaManagedAgentsAgentThreadMessageReceivedEvent:

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

String id

Unique identifier for this event.



List<Content> content

Message content blocks.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

String fromSessionThreadId

Public `sthr_` ID of the thread that sent the message.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

Optional<String> fromAgentName

Name of the callable agent this message came from. Absent when received from the primary agent.



class BetaManagedAgentsAgentThreadMessageSentEvent:

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

String id

Unique identifier for this event.



List<Content> content

Message content blocks.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String toSessionThreadId

Public `sthr_` ID of the thread the message was sent to.

Type type

Optional<String> toAgentName

Name of the callable agent this message was sent to. Absent when sent to the primary agent.



class BetaManagedAgentsAgentThreadContextCompactedEvent:

Indicates that context compaction (summarization) occurred during the session.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionErrorEvent:

An error event indicating a problem occurred during session execution.

String id

Unique identifier for this event.



Error error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

One of the following:



class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

String mcpServerName

Name of the MCP server that failed to connect.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

String mcpServerName

Name of the MCP server that failed authentication.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type



class BetaManagedAgentsCredentialHostUnreachableError:

An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

String credentialId

ID of the affected credential.

String message

Human-readable error description.



RetryStatus retryStatus

What the client should do next in response to this error.

One of the following:



class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type



class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type



class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

String vaultId

ID of the vault containing the affected credential.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionStatusRescheduledEvent:

Indicates the session is recovering from an error state and is rescheduled for execution.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionStatusRunningEvent:

Indicates the session is actively running and the agent is working.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionStatusIdleEvent:

Indicates the agent has paused and is awaiting user input.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format



StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

One of the following:



class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

Type type



class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

List<String> eventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type type



class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type type

Type type



class BetaManagedAgentsSessionStatusTerminatedEvent:

Indicates the session has terminated, either due to an error or completion.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionThreadCreatedEvent:

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

String id

Unique identifier for this event.

String agentName

Name of the callable agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public `sthr_` ID of the newly created thread.

Type type



class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:

Emitted when an outcome evaluation cycle begins.

String id

Unique identifier for this event.

long iteration

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

String outcomeId

The `outc_` ID of the outcome being evaluated.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

String id

Unique identifier for this event.

String explanation

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

long iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

String outcomeEvaluationStartId

The id of the corresponding `span.outcome_evaluation_start` event.

String outcomeId

The `outc_` ID of the outcome being evaluated.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String result

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

Type type



[BetaManagedAgentsSpanModelUsage](api/beta.md) usage

Token usage for a single model request.

long cacheCreationInputTokens

Tokens used to create prompt cache in this request.

long cacheReadInputTokens

Tokens read from prompt cache in this request.

long inputTokens

Input tokens consumed by this request.

long outputTokens

Output tokens generated by this request.



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")



class BetaManagedAgentsSpanModelRequestStartEvent:

Emitted when a model request is initiated by the agent.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSpanModelRequestEndEvent:

Emitted when a model request completes.

String id

Unique identifier for this event.

Optional<Boolean> isError

Whether the model request resulted in an error.

String modelRequestStartId

The id of the corresponding `span.model_request_start` event.



[BetaManagedAgentsSpanModelUsage](api/beta.md) modelUsage

Token usage for a single model request.

long cacheCreationInputTokens

Tokens used to create prompt cache in this request.

long cacheReadInputTokens

Tokens read from prompt cache in this request.

long inputTokens

Input tokens consumed by this request.

long outputTokens

Output tokens generated by this request.



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

String id

Unique identifier for this event.

long iteration

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

String outcomeId

The `outc_` ID of the outcome being evaluated.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsUserDefineOutcomeEvent:

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

String id

Unique identifier for this event.

String description

What the agent should produce. Copied from the input event.

Optional<Long> maxIterations

Evaluate-then-revise cycles before giving up. Default 3, max 20.

String outcomeId

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

LocalDateTime processedAt

A timestamp in RFC 3339 format



Rubric rubric

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubric:

Rubric referenced by a file uploaded via the Files API.

String fileId

ID of the rubric file.

Type type



class BetaManagedAgentsTextRubric:

Rubric content provided inline as text.

String content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

Type type

Type type



class BetaManagedAgentsSessionDeletedEvent:

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSessionThreadStatusRunningEvent:

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

String id

Unique identifier for this event.

String agentName

Name of the agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public sthr\_ ID of the thread that started running.

Type type



class BetaManagedAgentsSessionThreadStatusIdleEvent:

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

String id

Unique identifier for this event.

String agentName

Name of the agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public sthr\_ ID of the thread that went idle.



StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

One of the following:



class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

Type type



class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

List<String> eventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type type



class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type type

Type type



class BetaManagedAgentsSessionThreadStatusTerminatedEvent:

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

String id

Unique identifier for this event.

String agentName

Name of the agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public sthr\_ ID of the thread that terminated.

Type type



class BetaManagedAgentsUserToolResultEvent:

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

String id

Unique identifier for this event.

String toolUseId

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type



Optional<List<Content>> content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



Source source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



[BetaManagedAgentsSearchResultCitations](api/beta.md) citations

Citation settings for a search result.

boolean enabled

Whether citations are enabled for this search result.



List<[BetaManagedAgentsSearchResultContent](api/beta.md)> content

Array of text content blocks from the search result.

String text

The text content.

Type type

String source

The URL source of the search result.

String title

The title of the search result.

Type type

Optional<Boolean> isError

Whether the tool execution resulted in an error.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

Optional<String> sessionThreadId

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.



class BetaManagedAgentsSessionThreadStatusRescheduledEvent:

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

String id

Unique identifier for this event.

String agentName

Name of the agent the thread runs.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String sessionThreadId

Public sthr\_ ID of the thread that is retrying.

Type type



class BetaManagedAgentsSessionUpdatedEvent:

Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type



Optional<[BetaManagedAgentsSessionAgent](api/beta.md)> agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

String id

Optional<String> description



List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> mcpServers

String name

Type type

String url



[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.



BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")



Optional<[BetaManagedAgentsSessionMultiagentCoordinator](api/beta.md)> multiagent

Resolved coordinator topology with full agent definitions for each roster member.



List<[BetaManagedAgentsSessionThreadAgent](api/beta.md)> agents

Full `agent` definitions the coordinator may spawn as session threads.

String id

Optional<String> description



List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> mcpServers

String name

Type type

String url



[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.



BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding



Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

STANDARD("standard")

FAST("fast")

String name



List<Skill> skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system



List<Tool> tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled



Name name

Built-in agent tool identifier.

One of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type



class BetaManagedAgentsMcpToolset:



List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description



[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required

String name

Type type

Type type

long version

Type type

String name



List<Skill> skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system



List<Tool> tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled



Name name

Built-in agent tool identifier.

One of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type



class BetaManagedAgentsMcpToolset:



List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type



[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled



PermissionPolicy permissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description



[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required

String name

Type type

Type type

long version

Optional<Metadata> metadata

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

Optional<String> title

The session's new title. Present only when the update changed it.



class BetaManagedAgentsSystemMessageEvent:

A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

String id

Unique identifier for this event.



List<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks. Text-only.

String text

The text content.

Type type

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

#### SessionsThreadsEvents

##### [List Session Thread Events](api/beta/sessions/threads/events/list.md)

EventListPage beta().sessions().threads().events().list(EventListParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/beta/sessions/threads/events/stream.md)

[BetaManagedAgentsStreamSessionThreadEvents](api/beta.md) beta().sessions().threads().events().streamStreaming(EventStreamParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

---

*Copyright © Anthropic. All rights reserved.*
