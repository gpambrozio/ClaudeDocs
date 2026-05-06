# Sessions

Copy page

Ruby

# Sessions

##### [Create Session](api/beta/sessions/create.md)

beta.sessions.create(\*\*kwargs) -> [BetaManagedAgentsSession](api/beta.md) { id, agent, archived\_at, 12 more }

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

beta.sessions.list(\*\*kwargs) -> PageCursor<[BetaManagedAgentsSession](api/beta.md) { id, agent, archived\_at, 12 more } >

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

beta.sessions.retrieve(session\_id, \*\*kwargs) -> [BetaManagedAgentsSession](api/beta.md) { id, agent, archived\_at, 12 more }

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

beta.sessions.update(session\_id, \*\*kwargs) -> [BetaManagedAgentsSession](api/beta.md) { id, agent, archived\_at, 12 more }

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

beta.sessions.delete(session\_id, \*\*kwargs) -> [BetaManagedAgentsDeletedSession](api/beta.md) { id, type }

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

beta.sessions.archive(session\_id, \*\*kwargs) -> [BetaManagedAgentsSession](api/beta.md) { id, agent, archived\_at, 12 more }

POST/v1/sessions/{session\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsAgentParams { id, type, version }

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: String

The `agent` ID.

type: :agent

version: Integer

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

class BetaManagedAgentsBranchCheckout { name, type }

name: String

Branch name to check out.

type: :branch

class BetaManagedAgentsCacheCreationUsage { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: Integer

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: Integer

Tokens used to create 5-minute ephemeral cache entries.

class BetaManagedAgentsCommitCheckout { sha, type }

sha: String

Full commit SHA to check out.

type: :commit

class BetaManagedAgentsDeletedSession { id, type }

Confirmation that a `session` has been permanently deleted.

id: String

type: :session\_deleted

class BetaManagedAgentsFileResourceParams { file\_id, type, mount\_path }

Mount a file uploaded via the Files API into the session.

file\_id: String

ID of a previously uploaded file.

type: :file

mount\_path: String

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

class BetaManagedAgentsGitHubRepositoryResourceParams { authorization\_token, type, url, 2 more }

Mount a GitHub repository into the session's container.

authorization\_token: String

GitHub authorization token used to clone the repository.

type: :github\_repository

url: String

Github URL of the repository

checkout: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }

Branch or commit to check out. Defaults to the repository's default branch.

Accepts one of the following:

class BetaManagedAgentsBranchCheckout { name, type }

name: String

Branch name to check out.

type: :branch

class BetaManagedAgentsCommitCheckout { sha, type }

sha: String

Full commit SHA to check out.

type: :commit

mount\_path: String

Mount path in the container. Defaults to `/workspace/<repo-name>`.

class BetaManagedAgentsMemoryStoreResourceParam { memory\_store\_id, type, access, instructions }

Parameters for attaching a memory store to an agent session.

memory\_store\_id: String

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: :memory\_store

access: :read\_write | :read\_only

Access mode for an attached memory store.

Accepts one of the following:

:read\_write

:read\_only

instructions: String

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

class BetaManagedAgentsMultiagent { agents, type }

Resolved coordinator topology with a concrete agent roster.

agents: Array[[BetaManagedAgentsAgentReference](api/beta.md) { id, type, version } ]

Agents the coordinator may spawn as session threads, each resolved to a specific version.

id: String

type: :agent

version: Integer

type: :coordinator

class BetaManagedAgentsMultiagentParams { agents, type }

A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

agents: Array[[BetaManagedAgentsMultiagentRosterEntryParams](api/beta.md)]

Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

Accepts one of the following:

String

class BetaManagedAgentsAgentParams { id, type, version }

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: String

The `agent` ID.

type: :agent

version: Integer

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

class BetaManagedAgentsMultiagentSelfParams { type }

Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

type: :self

type: :coordinator

BetaManagedAgentsMultiagentRosterEntryParams = String | [BetaManagedAgentsAgentParams](api/beta.md) { id, type, version }  | [BetaManagedAgentsMultiagentSelfParams](api/beta.md) { type }

An entry in a multiagent roster: an agent ID string, a versioned agent reference, or `self`.

Accepts one of the following:

String

class BetaManagedAgentsAgentParams { id, type, version }

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: String

The `agent` ID.

type: :agent

version: Integer

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

class BetaManagedAgentsMultiagentSelfParams { type }

Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

type: :self

class BetaManagedAgentsOutcomeEvaluationResource { completed\_at, description, explanation, 4 more }

Evaluation state for a single outcome defined via a define\_outcome event.

completed\_at: Time

A timestamp in RFC 3339 format

description: String

What the agent should produce.

explanation: String

Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs\_revision (intermediate), what's missing; for failed, why unrecoverable.

iteration: Integer

0-indexed revision cycle the outcome is currently on.

outcome\_id: String

Server-generated outc\_ ID for this outcome.

result: String

Current evaluation state. 'pending' before the agent begins work; 'running' while producing or revising; 'evaluating' while the grader scores; 'satisfied'/'max\_iterations\_reached'/'failed'/'interrupted' are terminal.

type: :outcome\_evaluation

class BetaManagedAgentsSession { id, agent, archived\_at, 12 more }

A Managed Agents `session`.

id: String

agent: [BetaManagedAgentsSessionAgent](api/beta.md) { id, description, mcp\_servers, 8 more }

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: String

description: String

mcp\_servers: Array[[BetaManagedAgentsMCPServerURLDefinition](api/beta.md) { name, type, url } ]

name: String

type: :url

url: String

model: [BetaManagedAgentsModelConfig](api/beta.md) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

String

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

multiagent: [BetaManagedAgentsSessionMultiagentCoordinator](api/beta.md) { agents, type }

Resolved coordinator topology with full agent definitions for each roster member.

agents: Array[[BetaManagedAgentsSessionThreadAgent](api/beta.md) { id, description, mcp\_servers, 7 more } ]

Full `agent` definitions the coordinator may spawn as session threads.

id: String

description: String

mcp\_servers: Array[[BetaManagedAgentsMCPServerURLDefinition](api/beta.md) { name, type, url } ]

name: String

type: :url

url: String

model: [BetaManagedAgentsModelConfig](api/beta.md) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

String

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

name: String

skills: Array[[BetaManagedAgentsAnthropicSkill](api/beta.md) { skill\_id, type, version }  | [BetaManagedAgentsCustomSkill](api/beta.md) { skill\_id, type, version } ]

Accepts one of the following:

class BetaManagedAgentsAnthropicSkill { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: String

type: :anthropic

version: String

class BetaManagedAgentsCustomSkill { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: String

type: :custom

version: String

system\_: String

tools: Array[[BetaManagedAgentsAgentToolset20260401](api/beta.md) { configs, default\_config, type }  | [BetaManagedAgentsMCPToolset](api/beta.md) { configs, default\_config, mcp\_server\_name, type }  | [BetaManagedAgentsCustomTool](api/beta.md) { description, input\_schema, name, type } ]

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401 { configs, default\_config, type }

configs: Array[[BetaManagedAgentsAgentToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool

name: :bash | :edit | :read | 5 more

Built-in agent tool identifier.

Accepts one of the following:

:bash

:edit

:read

:write

:glob

:grep

:web\_fetch

:web\_search

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: bool

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

type: :agent\_toolset\_20260401

class BetaManagedAgentsMCPToolset { configs, default\_config, mcp\_server\_name, type }

configs: Array[[BetaManagedAgentsMCPToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool

name: String

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: bool

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

mcp\_server\_name: String

type: :mcp\_toolset

class BetaManagedAgentsCustomTool { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: String

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: Hash[Symbol, untyped]

JSON Schema properties defining the tool's input parameters.

required: Array[String]

List of required property names.

type: :object

Must be 'object' for tool input schemas.

name: String

type: :custom

type: :agent

version: Integer

type: :coordinator

name: String

skills: Array[[BetaManagedAgentsAnthropicSkill](api/beta.md) { skill\_id, type, version }  | [BetaManagedAgentsCustomSkill](api/beta.md) { skill\_id, type, version } ]

Accepts one of the following:

class BetaManagedAgentsAnthropicSkill { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: String

type: :anthropic

version: String

class BetaManagedAgentsCustomSkill { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: String

type: :custom

version: String

system\_: String

tools: Array[[BetaManagedAgentsAgentToolset20260401](api/beta.md) { configs, default\_config, type }  | [BetaManagedAgentsMCPToolset](api/beta.md) { configs, default\_config, mcp\_server\_name, type }  | [BetaManagedAgentsCustomTool](api/beta.md) { description, input\_schema, name, type } ]

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401 { configs, default\_config, type }

configs: Array[[BetaManagedAgentsAgentToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool

name: :bash | :edit | :read | 5 more

Built-in agent tool identifier.

Accepts one of the following:

:bash

:edit

:read

:write

:glob

:grep

:web\_fetch

:web\_search

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: bool

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

type: :agent\_toolset\_20260401

class BetaManagedAgentsMCPToolset { configs, default\_config, mcp\_server\_name, type }

configs: Array[[BetaManagedAgentsMCPToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool

name: String

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: bool

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

mcp\_server\_name: String

type: :mcp\_toolset

class BetaManagedAgentsCustomTool { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: String

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: Hash[Symbol, untyped]

JSON Schema properties defining the tool's input parameters.

required: Array[String]

List of required property names.

type: :object

Must be 'object' for tool input schemas.

name: String

type: :custom

type: :agent

version: Integer

archived\_at: Time

A timestamp in RFC 3339 format

created\_at: Time

A timestamp in RFC 3339 format

environment\_id: String

metadata: Hash[Symbol, String]

outcome\_evaluations: Array[[BetaManagedAgentsOutcomeEvaluationResource](api/beta.md) { completed\_at, description, explanation, 4 more } ]

Per-outcome evaluation state. One entry per define\_outcome event sent to the session.

completed\_at: Time

A timestamp in RFC 3339 format

description: String

What the agent should produce.

explanation: String

Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs\_revision (intermediate), what's missing; for failed, why unrecoverable.

iteration: Integer

0-indexed revision cycle the outcome is currently on.

outcome\_id: String

Server-generated outc\_ ID for this outcome.

result: String

Current evaluation state. 'pending' before the agent begins work; 'running' while producing or revising; 'evaluating' while the grader scores; 'satisfied'/'max\_iterations\_reached'/'failed'/'interrupted' are terminal.

type: :outcome\_evaluation

resources: Array[[BetaManagedAgentsSessionResource](api/beta.md)]

Accepts one of the following:

class BetaManagedAgentsGitHubRepositoryResource { id, created\_at, mount\_path, 4 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

mount\_path: String

type: :github\_repository

updated\_at: Time

A timestamp in RFC 3339 format

url: String

checkout: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }

Accepts one of the following:

class BetaManagedAgentsBranchCheckout { name, type }

name: String

Branch name to check out.

type: :branch

class BetaManagedAgentsCommitCheckout { sha, type }

sha: String

Full commit SHA to check out.

type: :commit

class BetaManagedAgentsFileResource { id, created\_at, file\_id, 3 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

file\_id: String

mount\_path: String

type: :file

updated\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsMemoryStoreResource { memory\_store\_id, type, access, 4 more }

A memory store attached to an agent session.

memory\_store\_id: String

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: :memory\_store

access: :read\_write | :read\_only

Access mode for an attached memory store.

Accepts one of the following:

:read\_write

:read\_only

description: String

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

instructions: String

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

mount\_path: String

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

name: String

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

stats: [BetaManagedAgentsSessionStats](api/beta.md) { active\_seconds, duration\_seconds }

Timing statistics for a session.

active\_seconds: Float

Cumulative time in seconds the session spent in running status. Excludes idle time.

duration\_seconds: Float

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

status: :rescheduling | :running | :idle | :terminated

SessionStatus enum

Accepts one of the following:

:rescheduling

:running

:idle

:terminated

title: String

type: :session

updated\_at: Time

A timestamp in RFC 3339 format

usage: [BetaManagedAgentsSessionUsage](api/beta.md) { cache\_creation, cache\_read\_input\_tokens, input\_tokens, output\_tokens }

Cumulative token usage for a session across all turns.

cache\_creation: [BetaManagedAgentsCacheCreationUsage](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: Integer

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: Integer

Tokens used to create 5-minute ephemeral cache entries.

cache\_read\_input\_tokens: Integer

Total tokens read from prompt cache.

input\_tokens: Integer

Total input tokens consumed across all turns.

output\_tokens: Integer

Total output tokens generated across all turns.

vault\_ids: Array[String]

Vault IDs attached to the session at creation. Empty when no vaults were supplied.

class BetaManagedAgentsSessionAgent { id, description, mcp\_servers, 8 more }

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: String

description: String

mcp\_servers: Array[[BetaManagedAgentsMCPServerURLDefinition](api/beta.md) { name, type, url } ]

name: String

type: :url

url: String

model: [BetaManagedAgentsModelConfig](api/beta.md) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

String

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

multiagent: [BetaManagedAgentsSessionMultiagentCoordinator](api/beta.md) { agents, type }

Resolved coordinator topology with full agent definitions for each roster member.

agents: Array[[BetaManagedAgentsSessionThreadAgent](api/beta.md) { id, description, mcp\_servers, 7 more } ]

Full `agent` definitions the coordinator may spawn as session threads.

id: String

description: String

mcp\_servers: Array[[BetaManagedAgentsMCPServerURLDefinition](api/beta.md) { name, type, url } ]

name: String

type: :url

url: String

model: [BetaManagedAgentsModelConfig](api/beta.md) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

String

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

name: String

skills: Array[[BetaManagedAgentsAnthropicSkill](api/beta.md) { skill\_id, type, version }  | [BetaManagedAgentsCustomSkill](api/beta.md) { skill\_id, type, version } ]

Accepts one of the following:

class BetaManagedAgentsAnthropicSkill { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: String

type: :anthropic

version: String

class BetaManagedAgentsCustomSkill { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: String

type: :custom

version: String

system\_: String

tools: Array[[BetaManagedAgentsAgentToolset20260401](api/beta.md) { configs, default\_config, type }  | [BetaManagedAgentsMCPToolset](api/beta.md) { configs, default\_config, mcp\_server\_name, type }  | [BetaManagedAgentsCustomTool](api/beta.md) { description, input\_schema, name, type } ]

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401 { configs, default\_config, type }

configs: Array[[BetaManagedAgentsAgentToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool

name: :bash | :edit | :read | 5 more

Built-in agent tool identifier.

Accepts one of the following:

:bash

:edit

:read

:write

:glob

:grep

:web\_fetch

:web\_search

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: bool

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

type: :agent\_toolset\_20260401

class BetaManagedAgentsMCPToolset { configs, default\_config, mcp\_server\_name, type }

configs: Array[[BetaManagedAgentsMCPToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool

name: String

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: bool

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

mcp\_server\_name: String

type: :mcp\_toolset

class BetaManagedAgentsCustomTool { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: String

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: Hash[Symbol, untyped]

JSON Schema properties defining the tool's input parameters.

required: Array[String]

List of required property names.

type: :object

Must be 'object' for tool input schemas.

name: String

type: :custom

type: :agent

version: Integer

type: :coordinator

name: String

skills: Array[[BetaManagedAgentsAnthropicSkill](api/beta.md) { skill\_id, type, version }  | [BetaManagedAgentsCustomSkill](api/beta.md) { skill\_id, type, version } ]

Accepts one of the following:

class BetaManagedAgentsAnthropicSkill { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: String

type: :anthropic

version: String

class BetaManagedAgentsCustomSkill { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: String

type: :custom

version: String

system\_: String

tools: Array[[BetaManagedAgentsAgentToolset20260401](api/beta.md) { configs, default\_config, type }  | [BetaManagedAgentsMCPToolset](api/beta.md) { configs, default\_config, mcp\_server\_name, type }  | [BetaManagedAgentsCustomTool](api/beta.md) { description, input\_schema, name, type } ]

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401 { configs, default\_config, type }

configs: Array[[BetaManagedAgentsAgentToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool

name: :bash | :edit | :read | 5 more

Built-in agent tool identifier.

Accepts one of the following:

:bash

:edit

:read

:write

:glob

:grep

:web\_fetch

:web\_search

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: bool

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

type: :agent\_toolset\_20260401

class BetaManagedAgentsMCPToolset { configs, default\_config, mcp\_server\_name, type }

configs: Array[[BetaManagedAgentsMCPToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool

name: String

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: bool

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

mcp\_server\_name: String

type: :mcp\_toolset

class BetaManagedAgentsCustomTool { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: String

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: Hash[Symbol, untyped]

JSON Schema properties defining the tool's input parameters.

required: Array[String]

List of required property names.

type: :object

Must be 'object' for tool input schemas.

name: String

type: :custom

type: :agent

version: Integer

class BetaManagedAgentsSessionMultiagentCoordinator { agents, type }

Resolved coordinator topology with full agent definitions for each roster member.

agents: Array[[BetaManagedAgentsSessionThreadAgent](api/beta.md) { id, description, mcp\_servers, 7 more } ]

Full `agent` definitions the coordinator may spawn as session threads.

id: String

description: String

mcp\_servers: Array[[BetaManagedAgentsMCPServerURLDefinition](api/beta.md) { name, type, url } ]

name: String

type: :url

url: String

model: [BetaManagedAgentsModelConfig](api/beta.md) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

String

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

name: String

skills: Array[[BetaManagedAgentsAnthropicSkill](api/beta.md) { skill\_id, type, version }  | [BetaManagedAgentsCustomSkill](api/beta.md) { skill\_id, type, version } ]

Accepts one of the following:

class BetaManagedAgentsAnthropicSkill { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: String

type: :anthropic

version: String

class BetaManagedAgentsCustomSkill { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: String

type: :custom

version: String

system\_: String

tools: Array[[BetaManagedAgentsAgentToolset20260401](api/beta.md) { configs, default\_config, type }  | [BetaManagedAgentsMCPToolset](api/beta.md) { configs, default\_config, mcp\_server\_name, type }  | [BetaManagedAgentsCustomTool](api/beta.md) { description, input\_schema, name, type } ]

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401 { configs, default\_config, type }

configs: Array[[BetaManagedAgentsAgentToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool

name: :bash | :edit | :read | 5 more

Built-in agent tool identifier.

Accepts one of the following:

:bash

:edit

:read

:write

:glob

:grep

:web\_fetch

:web\_search

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: bool

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

type: :agent\_toolset\_20260401

class BetaManagedAgentsMCPToolset { configs, default\_config, mcp\_server\_name, type }

configs: Array[[BetaManagedAgentsMCPToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool

name: String

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: bool

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

mcp\_server\_name: String

type: :mcp\_toolset

class BetaManagedAgentsCustomTool { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: String

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: Hash[Symbol, untyped]

JSON Schema properties defining the tool's input parameters.

required: Array[String]

List of required property names.

type: :object

Must be 'object' for tool input schemas.

name: String

type: :custom

type: :agent

version: Integer

type: :coordinator

class BetaManagedAgentsSessionStats { active\_seconds, duration\_seconds }

Timing statistics for a session.

active\_seconds: Float

Cumulative time in seconds the session spent in running status. Excludes idle time.

duration\_seconds: Float

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

class BetaManagedAgentsSessionUsage { cache\_creation, cache\_read\_input\_tokens, input\_tokens, output\_tokens }

Cumulative token usage for a session across all turns.

cache\_creation: [BetaManagedAgentsCacheCreationUsage](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: Integer

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: Integer

Tokens used to create 5-minute ephemeral cache entries.

cache\_read\_input\_tokens: Integer

Total tokens read from prompt cache.

input\_tokens: Integer

Total input tokens consumed across all turns.

output\_tokens: Integer

Total output tokens generated across all turns.

#### SessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

beta.sessions.events.list(session\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsSessionEvent](api/beta.md)>

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

beta.sessions.events.send\_(session\_id, \*\*kwargs) -> [BetaManagedAgentsSendSessionEvents](api/beta.md) { data }

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

beta.sessions.events.stream(session\_id, \*\*kwargs) -> [BetaManagedAgentsStreamSessionEvents](api/beta.md)

GET/v1/sessions/{session\_id}/events/stream

##### ModelsExpand Collapse

class BetaManagedAgentsAgentCustomToolUseEvent { id, input, name, 3 more }

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

name: String

Name of the custom tool being called.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.custom\_tool\_use"

session\_thread\_id: String

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

class BetaManagedAgentsAgentMCPToolResultEvent { id, mcp\_tool\_use\_id, processed\_at, 3 more }

Event representing the result of an MCP tool execution.

id: String

Unique identifier for this event.

mcp\_tool\_use\_id: String

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.mcp\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentMCPToolUseEvent { id, input, mcp\_server\_name, 5 more }

Event emitted when the agent invokes a tool provided by an MCP server.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

mcp\_server\_name: String

Name of the MCP server providing the tool.

name: String

Name of the MCP tool being used.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.mcp\_tool\_use"

evaluated\_permission: :allow | :ask | :deny

AgentEvaluatedPermission enum

Accepts one of the following:

:allow

:ask

:deny

session\_thread\_id: String

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

class BetaManagedAgentsAgentMessageEvent { id, content, processed\_at, type }

An agent response event in the session conversation.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type } ]

Array of text blocks comprising the agent response.

text: String

The text content.

type: :text

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.message"

class BetaManagedAgentsAgentThinkingEvent { id, processed\_at, type }

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thinking"

class BetaManagedAgentsAgentThreadContextCompactedEvent { id, processed\_at, type }

Indicates that context compaction (summarization) occurred during the session.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thread\_context\_compacted"

class BetaManagedAgentsAgentThreadMessageReceivedEvent { id, content, from\_session\_thread\_id, 3 more }

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Message content blocks.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

from\_session\_thread\_id: String

Public `sthr_` ID of the thread that sent the message.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thread\_message\_received"

from\_agent\_name: String

Name of the callable agent this message came from. Absent when received from the primary agent.

class BetaManagedAgentsAgentThreadMessageSentEvent { id, content, processed\_at, 3 more }

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Message content blocks.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

processed\_at: Time

A timestamp in RFC 3339 format

to\_session\_thread\_id: String

Public `sthr_` ID of the thread the message was sent to.

type: :"agent.thread\_message\_sent"

to\_agent\_name: String

Name of the callable agent this message was sent to. Absent when sent to the primary agent.

class BetaManagedAgentsAgentToolResultEvent { id, processed\_at, tool\_use\_id, 3 more }

Event representing the result of an agent tool execution.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

tool\_use\_id: String

The id of the `agent.tool_use` event this result corresponds to.

type: :"agent.tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent { id, input, name, 4 more }

Event emitted when the agent invokes a built-in agent tool.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

name: String

Name of the agent tool being used.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.tool\_use"

evaluated\_permission: :allow | :ask | :deny

AgentEvaluatedPermission enum

Accepts one of the following:

:allow

:ask

:deny

session\_thread\_id: String

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsBillingError { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :billing\_error

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

BetaManagedAgentsEventParams = [BetaManagedAgentsUserMessageEventParams](api/beta.md) { content, type }  | [BetaManagedAgentsUserInterruptEventParams](api/beta.md) { type, session\_thread\_id }  | [BetaManagedAgentsUserToolConfirmationEventParams](api/beta.md) { result, tool\_use\_id, type, deny\_message }  | 2 more

Union type for event parameters that can be sent to a session.

Accepts one of the following:

class BetaManagedAgentsUserMessageEventParams { content, type }

Parameters for sending a user message to the session.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Array of content blocks for the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

type: :"user.message"

class BetaManagedAgentsUserInterruptEventParams { type, session\_thread\_id }

Parameters for sending an interrupt to pause the agent.

type: :"user.interrupt"

session\_thread\_id: String

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

class BetaManagedAgentsUserToolConfirmationEventParams { result, tool\_use\_id, type, deny\_message }

Parameters for confirming or denying a tool execution request.

result: :allow | :deny

UserToolConfirmationResult enum

Accepts one of the following:

:allow

:deny

tool\_use\_id: String

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.tool\_confirmation"

deny\_message: String

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

class BetaManagedAgentsUserCustomToolResultEventParams { custom\_tool\_use\_id, type, content, is\_error }

Parameters for providing the result of a custom tool execution.

custom\_tool\_use\_id: String

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.custom\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsUserDefineOutcomeEventParams { description, rubric, type, max\_iterations }

Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

description: String

What the agent should produce. This is the task specification.

rubric: [BetaManagedAgentsFileRubricParams](api/beta.md) { file\_id, type }  | [BetaManagedAgentsTextRubricParams](api/beta.md) { content, type }

Rubric for grading the quality of an outcome.

Accepts one of the following:

class BetaManagedAgentsFileRubricParams { file\_id, type }

Rubric referenced by a file uploaded via the Files API.

file\_id: String

ID of the rubric file.

type: :file

class BetaManagedAgentsTextRubricParams { content, type }

Rubric content provided inline as text.

content: String

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

type: :text

type: :"user.define\_outcome"

max\_iterations: Integer

Eval→revision cycles before giving up. Default 3, max 20.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

class BetaManagedAgentsFileRubric { file\_id, type }

Rubric referenced by a file uploaded via the Files API.

file\_id: String

ID of the rubric file.

type: :file

class BetaManagedAgentsFileRubricParams { file\_id, type }

Rubric referenced by a file uploaded via the Files API.

file\_id: String

ID of the rubric file.

type: :file

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsMCPAuthenticationFailedError { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: String

Name of the MCP server that failed authentication.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_authentication\_failed\_error

class BetaManagedAgentsMCPConnectionFailedError { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: String

Name of the MCP server that failed to connect.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_connection\_failed\_error

class BetaManagedAgentsModelOverloadedError { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_overloaded\_error

class BetaManagedAgentsModelRateLimitedError { message, retry\_status, type }

The model request was rate-limited.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_rate\_limited\_error

class BetaManagedAgentsModelRequestFailedError { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_request\_failed\_error

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

class BetaManagedAgentsSendSessionEvents { data }

Events that were successfully sent to the session.

data: Array[[BetaManagedAgentsUserMessageEvent](api/beta.md) { id, content, type, processed\_at }  | [BetaManagedAgentsUserInterruptEvent](api/beta.md) { id, type, processed\_at, session\_thread\_id }  | [BetaManagedAgentsUserToolConfirmationEvent](api/beta.md) { id, result, tool\_use\_id, 4 more }  | 2 more]

Sent events

Accepts one of the following:

class BetaManagedAgentsUserMessageEvent { id, content, type, processed\_at }

A user message event in the session conversation.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

type: :"user.message"

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent { id, type, processed\_at, session\_thread\_id }

An interrupt event that pauses agent execution and returns control to the user.

id: String

Unique identifier for this event.

type: :"user.interrupt"

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

class BetaManagedAgentsUserToolConfirmationEvent { id, result, tool\_use\_id, 4 more }

A tool confirmation event that approves or denies a pending tool execution.

id: String

Unique identifier for this event.

result: :allow | :deny

UserToolConfirmationResult enum

Accepts one of the following:

:allow

:deny

tool\_use\_id: String

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.tool\_confirmation"

deny\_message: String

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

class BetaManagedAgentsUserCustomToolResultEvent { id, custom\_tool\_use\_id, type, 4 more }

Event sent by the client providing the result of a custom tool execution.

id: String

Unique identifier for this event.

custom\_tool\_use\_id: String

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.custom\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

class BetaManagedAgentsUserDefineOutcomeEvent { id, description, max\_iterations, 4 more }

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

id: String

Unique identifier for this event.

description: String

What the agent should produce. Copied from the input event.

max\_iterations: Integer

Evaluate-then-revise cycles before giving up. Default 3, max 20.

outcome\_id: String

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

processed\_at: Time

A timestamp in RFC 3339 format

rubric: [BetaManagedAgentsFileRubric](api/beta.md) { file\_id, type }  | [BetaManagedAgentsTextRubric](api/beta.md) { content, type }

Rubric for grading the quality of an outcome.

Accepts one of the following:

class BetaManagedAgentsFileRubric { file\_id, type }

Rubric referenced by a file uploaded via the Files API.

file\_id: String

ID of the rubric file.

type: :file

class BetaManagedAgentsTextRubric { content, type }

Rubric content provided inline as text.

content: String

Rubric content. Plain text or markdown — the grader treats it as freeform text.

type: :text

type: :"user.define\_outcome"

class BetaManagedAgentsSessionDeletedEvent { id, processed\_at, type }

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.deleted"

class BetaManagedAgentsSessionEndTurn { type }

The agent completed its turn naturally and is ready for the next user message.

type: :end\_turn

class BetaManagedAgentsSessionErrorEvent { id, error, processed\_at, type }

An error event indicating a problem occurred during session execution.

id: String

Unique identifier for this event.

error: [BetaManagedAgentsUnknownError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelOverloadedError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelRateLimitedError](api/beta.md) { message, retry\_status, type }  | 4 more

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :unknown\_error

class BetaManagedAgentsModelOverloadedError { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_overloaded\_error

class BetaManagedAgentsModelRateLimitedError { message, retry\_status, type }

The model request was rate-limited.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_rate\_limited\_error

class BetaManagedAgentsModelRequestFailedError { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_request\_failed\_error

class BetaManagedAgentsMCPConnectionFailedError { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: String

Name of the MCP server that failed to connect.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_connection\_failed\_error

class BetaManagedAgentsMCPAuthenticationFailedError { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: String

Name of the MCP server that failed authentication.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_authentication\_failed\_error

class BetaManagedAgentsBillingError { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :billing\_error

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.error"

BetaManagedAgentsSessionEvent = [BetaManagedAgentsUserMessageEvent](api/beta.md) { id, content, type, processed\_at }  | [BetaManagedAgentsUserInterruptEvent](api/beta.md) { id, type, processed\_at, session\_thread\_id }  | [BetaManagedAgentsUserToolConfirmationEvent](api/beta.md) { id, result, tool\_use\_id, 4 more }  | 28 more

Union type for all event types in a session.

Accepts one of the following:

class BetaManagedAgentsUserMessageEvent { id, content, type, processed\_at }

A user message event in the session conversation.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

type: :"user.message"

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent { id, type, processed\_at, session\_thread\_id }

An interrupt event that pauses agent execution and returns control to the user.

id: String

Unique identifier for this event.

type: :"user.interrupt"

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

class BetaManagedAgentsUserToolConfirmationEvent { id, result, tool\_use\_id, 4 more }

A tool confirmation event that approves or denies a pending tool execution.

id: String

Unique identifier for this event.

result: :allow | :deny

UserToolConfirmationResult enum

Accepts one of the following:

:allow

:deny

tool\_use\_id: String

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.tool\_confirmation"

deny\_message: String

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

class BetaManagedAgentsUserCustomToolResultEvent { id, custom\_tool\_use\_id, type, 4 more }

Event sent by the client providing the result of a custom tool execution.

id: String

Unique identifier for this event.

custom\_tool\_use\_id: String

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.custom\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

class BetaManagedAgentsAgentCustomToolUseEvent { id, input, name, 3 more }

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

name: String

Name of the custom tool being called.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.custom\_tool\_use"

session\_thread\_id: String

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

class BetaManagedAgentsAgentMessageEvent { id, content, processed\_at, type }

An agent response event in the session conversation.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type } ]

Array of text blocks comprising the agent response.

text: String

The text content.

type: :text

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.message"

class BetaManagedAgentsAgentThinkingEvent { id, processed\_at, type }

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thinking"

class BetaManagedAgentsAgentMCPToolUseEvent { id, input, mcp\_server\_name, 5 more }

Event emitted when the agent invokes a tool provided by an MCP server.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

mcp\_server\_name: String

Name of the MCP server providing the tool.

name: String

Name of the MCP tool being used.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.mcp\_tool\_use"

evaluated\_permission: :allow | :ask | :deny

AgentEvaluatedPermission enum

Accepts one of the following:

:allow

:ask

:deny

session\_thread\_id: String

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

class BetaManagedAgentsAgentMCPToolResultEvent { id, mcp\_tool\_use\_id, processed\_at, 3 more }

Event representing the result of an MCP tool execution.

id: String

Unique identifier for this event.

mcp\_tool\_use\_id: String

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.mcp\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent { id, input, name, 4 more }

Event emitted when the agent invokes a built-in agent tool.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

name: String

Name of the agent tool being used.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.tool\_use"

evaluated\_permission: :allow | :ask | :deny

AgentEvaluatedPermission enum

Accepts one of the following:

:allow

:ask

:deny

session\_thread\_id: String

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

class BetaManagedAgentsAgentToolResultEvent { id, processed\_at, tool\_use\_id, 3 more }

Event representing the result of an agent tool execution.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

tool\_use\_id: String

The id of the `agent.tool_use` event this result corresponds to.

type: :"agent.tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentThreadMessageReceivedEvent { id, content, from\_session\_thread\_id, 3 more }

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Message content blocks.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

from\_session\_thread\_id: String

Public `sthr_` ID of the thread that sent the message.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thread\_message\_received"

from\_agent\_name: String

Name of the callable agent this message came from. Absent when received from the primary agent.

class BetaManagedAgentsAgentThreadMessageSentEvent { id, content, processed\_at, 3 more }

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Message content blocks.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

processed\_at: Time

A timestamp in RFC 3339 format

to\_session\_thread\_id: String

Public `sthr_` ID of the thread the message was sent to.

type: :"agent.thread\_message\_sent"

to\_agent\_name: String

Name of the callable agent this message was sent to. Absent when sent to the primary agent.

class BetaManagedAgentsAgentThreadContextCompactedEvent { id, processed\_at, type }

Indicates that context compaction (summarization) occurred during the session.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thread\_context\_compacted"

class BetaManagedAgentsSessionErrorEvent { id, error, processed\_at, type }

An error event indicating a problem occurred during session execution.

id: String

Unique identifier for this event.

error: [BetaManagedAgentsUnknownError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelOverloadedError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelRateLimitedError](api/beta.md) { message, retry\_status, type }  | 4 more

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :unknown\_error

class BetaManagedAgentsModelOverloadedError { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_overloaded\_error

class BetaManagedAgentsModelRateLimitedError { message, retry\_status, type }

The model request was rate-limited.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_rate\_limited\_error

class BetaManagedAgentsModelRequestFailedError { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_request\_failed\_error

class BetaManagedAgentsMCPConnectionFailedError { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: String

Name of the MCP server that failed to connect.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_connection\_failed\_error

class BetaManagedAgentsMCPAuthenticationFailedError { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: String

Name of the MCP server that failed authentication.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_authentication\_failed\_error

class BetaManagedAgentsBillingError { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :billing\_error

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.error"

class BetaManagedAgentsSessionStatusRescheduledEvent { id, processed\_at, type }

Indicates the session is recovering from an error state and is rescheduled for execution.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_rescheduled"

class BetaManagedAgentsSessionStatusRunningEvent { id, processed\_at, type }

Indicates the session is actively running and the agent is working.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_running"

class BetaManagedAgentsSessionStatusIdleEvent { id, processed\_at, stop\_reason, type }

Indicates the agent has paused and is awaiting user input.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta.md) { type }  | [BetaManagedAgentsSessionRequiresAction](api/beta.md) { event\_ids, type }  | [BetaManagedAgentsSessionRetriesExhausted](api/beta.md) { type }

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn { type }

The agent completed its turn naturally and is ready for the next user message.

type: :end\_turn

class BetaManagedAgentsSessionRequiresAction { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: Array[String]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: :requires\_action

class BetaManagedAgentsSessionRetriesExhausted { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: :retries\_exhausted

type: :"session.status\_idle"

class BetaManagedAgentsSessionStatusTerminatedEvent { id, processed\_at, type }

Indicates the session has terminated, either due to an error or completion.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_terminated"

class BetaManagedAgentsSessionThreadCreatedEvent { id, agent\_name, processed\_at, 2 more }

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

id: String

Unique identifier for this event.

agent\_name: String

Name of the callable agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public `sthr_` ID of the newly created thread.

type: :"session.thread\_created"

class BetaManagedAgentsSpanOutcomeEvaluationStartEvent { id, iteration, outcome\_id, 2 more }

Emitted when an outcome evaluation cycle begins.

id: String

Unique identifier for this event.

iteration: Integer

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

outcome\_id: String

The `outc_` ID of the outcome being evaluated.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.outcome\_evaluation\_start"

class BetaManagedAgentsSpanOutcomeEvaluationEndEvent { id, explanation, iteration, 6 more }

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

id: String

Unique identifier for this event.

explanation: String

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

iteration: Integer

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_evaluation\_start\_id: String

The id of the corresponding `span.outcome_evaluation_start` event.

outcome\_id: String

The `outc_` ID of the outcome being evaluated.

processed\_at: Time

A timestamp in RFC 3339 format

result: String

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

type: :"span.outcome\_evaluation\_end"

usage: [BetaManagedAgentsSpanModelUsage](api/beta.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: Integer

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: Integer

Tokens read from prompt cache in this request.

input\_tokens: Integer

Input tokens consumed by this request.

output\_tokens: Integer

Output tokens generated by this request.

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

class BetaManagedAgentsSpanModelRequestStartEvent { id, processed\_at, type }

Emitted when a model request is initiated by the agent.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.model\_request\_start"

class BetaManagedAgentsSpanModelRequestEndEvent { id, is\_error, model\_request\_start\_id, 3 more }

Emitted when a model request completes.

id: String

Unique identifier for this event.

is\_error: bool

Whether the model request resulted in an error.

model\_request\_start\_id: String

The id of the corresponding `span.model_request_start` event.

model\_usage: [BetaManagedAgentsSpanModelUsage](api/beta.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: Integer

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: Integer

Tokens read from prompt cache in this request.

input\_tokens: Integer

Input tokens consumed by this request.

output\_tokens: Integer

Output tokens generated by this request.

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.model\_request\_end"

class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent { id, iteration, outcome\_id, 2 more }

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

id: String

Unique identifier for this event.

iteration: Integer

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_id: String

The `outc_` ID of the outcome being evaluated.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.outcome\_evaluation\_ongoing"

class BetaManagedAgentsUserDefineOutcomeEvent { id, description, max\_iterations, 4 more }

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

id: String

Unique identifier for this event.

description: String

What the agent should produce. Copied from the input event.

max\_iterations: Integer

Evaluate-then-revise cycles before giving up. Default 3, max 20.

outcome\_id: String

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

processed\_at: Time

A timestamp in RFC 3339 format

rubric: [BetaManagedAgentsFileRubric](api/beta.md) { file\_id, type }  | [BetaManagedAgentsTextRubric](api/beta.md) { content, type }

Rubric for grading the quality of an outcome.

Accepts one of the following:

class BetaManagedAgentsFileRubric { file\_id, type }

Rubric referenced by a file uploaded via the Files API.

file\_id: String

ID of the rubric file.

type: :file

class BetaManagedAgentsTextRubric { content, type }

Rubric content provided inline as text.

content: String

Rubric content. Plain text or markdown — the grader treats it as freeform text.

type: :text

type: :"user.define\_outcome"

class BetaManagedAgentsSessionDeletedEvent { id, processed\_at, type }

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.deleted"

class BetaManagedAgentsSessionThreadStatusRunningEvent { id, agent\_name, processed\_at, 2 more }

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: String

Unique identifier for this event.

agent\_name: String

Name of the agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public sthr\_ ID of the thread that started running.

type: :"session.thread\_status\_running"

class BetaManagedAgentsSessionThreadStatusIdleEvent { id, agent\_name, processed\_at, 3 more }

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: String

Unique identifier for this event.

agent\_name: String

Name of the agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public sthr\_ ID of the thread that went idle.

stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta.md) { type }  | [BetaManagedAgentsSessionRequiresAction](api/beta.md) { event\_ids, type }  | [BetaManagedAgentsSessionRetriesExhausted](api/beta.md) { type }

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn { type }

The agent completed its turn naturally and is ready for the next user message.

type: :end\_turn

class BetaManagedAgentsSessionRequiresAction { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: Array[String]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: :requires\_action

class BetaManagedAgentsSessionRetriesExhausted { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: :retries\_exhausted

type: :"session.thread\_status\_idle"

class BetaManagedAgentsSessionThreadStatusTerminatedEvent { id, agent\_name, processed\_at, 2 more }

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: String

Unique identifier for this event.

agent\_name: String

Name of the agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public sthr\_ ID of the thread that terminated.

type: :"session.thread\_status\_terminated"

class BetaManagedAgentsSessionThreadStatusRescheduledEvent { id, agent\_name, processed\_at, 2 more }

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: String

Unique identifier for this event.

agent\_name: String

Name of the agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public sthr\_ ID of the thread that is retrying.

type: :"session.thread\_status\_rescheduled"

class BetaManagedAgentsSessionRequiresAction { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: Array[String]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: :requires\_action

class BetaManagedAgentsSessionRetriesExhausted { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: :retries\_exhausted

class BetaManagedAgentsSessionStatusIdleEvent { id, processed\_at, stop\_reason, type }

Indicates the agent has paused and is awaiting user input.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta.md) { type }  | [BetaManagedAgentsSessionRequiresAction](api/beta.md) { event\_ids, type }  | [BetaManagedAgentsSessionRetriesExhausted](api/beta.md) { type }

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn { type }

The agent completed its turn naturally and is ready for the next user message.

type: :end\_turn

class BetaManagedAgentsSessionRequiresAction { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: Array[String]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: :requires\_action

class BetaManagedAgentsSessionRetriesExhausted { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: :retries\_exhausted

type: :"session.status\_idle"

class BetaManagedAgentsSessionStatusRescheduledEvent { id, processed\_at, type }

Indicates the session is recovering from an error state and is rescheduled for execution.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_rescheduled"

class BetaManagedAgentsSessionStatusRunningEvent { id, processed\_at, type }

Indicates the session is actively running and the agent is working.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_running"

class BetaManagedAgentsSessionStatusTerminatedEvent { id, processed\_at, type }

Indicates the session has terminated, either due to an error or completion.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_terminated"

class BetaManagedAgentsSessionThreadCreatedEvent { id, agent\_name, processed\_at, 2 more }

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

id: String

Unique identifier for this event.

agent\_name: String

Name of the callable agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public `sthr_` ID of the newly created thread.

type: :"session.thread\_created"

class BetaManagedAgentsSessionThreadStatusIdleEvent { id, agent\_name, processed\_at, 3 more }

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: String

Unique identifier for this event.

agent\_name: String

Name of the agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public sthr\_ ID of the thread that went idle.

stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta.md) { type }  | [BetaManagedAgentsSessionRequiresAction](api/beta.md) { event\_ids, type }  | [BetaManagedAgentsSessionRetriesExhausted](api/beta.md) { type }

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn { type }

The agent completed its turn naturally and is ready for the next user message.

type: :end\_turn

class BetaManagedAgentsSessionRequiresAction { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: Array[String]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: :requires\_action

class BetaManagedAgentsSessionRetriesExhausted { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: :retries\_exhausted

type: :"session.thread\_status\_idle"

class BetaManagedAgentsSessionThreadStatusRescheduledEvent { id, agent\_name, processed\_at, 2 more }

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: String

Unique identifier for this event.

agent\_name: String

Name of the agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public sthr\_ ID of the thread that is retrying.

type: :"session.thread\_status\_rescheduled"

class BetaManagedAgentsSessionThreadStatusRunningEvent { id, agent\_name, processed\_at, 2 more }

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: String

Unique identifier for this event.

agent\_name: String

Name of the agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public sthr\_ ID of the thread that started running.

type: :"session.thread\_status\_running"

class BetaManagedAgentsSessionThreadStatusTerminatedEvent { id, agent\_name, processed\_at, 2 more }

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: String

Unique identifier for this event.

agent\_name: String

Name of the agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public sthr\_ ID of the thread that terminated.

type: :"session.thread\_status\_terminated"

class BetaManagedAgentsSpanModelRequestEndEvent { id, is\_error, model\_request\_start\_id, 3 more }

Emitted when a model request completes.

id: String

Unique identifier for this event.

is\_error: bool

Whether the model request resulted in an error.

model\_request\_start\_id: String

The id of the corresponding `span.model_request_start` event.

model\_usage: [BetaManagedAgentsSpanModelUsage](api/beta.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: Integer

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: Integer

Tokens read from prompt cache in this request.

input\_tokens: Integer

Input tokens consumed by this request.

output\_tokens: Integer

Output tokens generated by this request.

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.model\_request\_end"

class BetaManagedAgentsSpanModelRequestStartEvent { id, processed\_at, type }

Emitted when a model request is initiated by the agent.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.model\_request\_start"

class BetaManagedAgentsSpanModelUsage { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: Integer

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: Integer

Tokens read from prompt cache in this request.

input\_tokens: Integer

Input tokens consumed by this request.

output\_tokens: Integer

Output tokens generated by this request.

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

class BetaManagedAgentsSpanOutcomeEvaluationEndEvent { id, explanation, iteration, 6 more }

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

id: String

Unique identifier for this event.

explanation: String

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

iteration: Integer

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_evaluation\_start\_id: String

The id of the corresponding `span.outcome_evaluation_start` event.

outcome\_id: String

The `outc_` ID of the outcome being evaluated.

processed\_at: Time

A timestamp in RFC 3339 format

result: String

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

type: :"span.outcome\_evaluation\_end"

usage: [BetaManagedAgentsSpanModelUsage](api/beta.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: Integer

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: Integer

Tokens read from prompt cache in this request.

input\_tokens: Integer

Input tokens consumed by this request.

output\_tokens: Integer

Output tokens generated by this request.

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent { id, iteration, outcome\_id, 2 more }

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

id: String

Unique identifier for this event.

iteration: Integer

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_id: String

The `outc_` ID of the outcome being evaluated.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.outcome\_evaluation\_ongoing"

class BetaManagedAgentsSpanOutcomeEvaluationStartEvent { id, iteration, outcome\_id, 2 more }

Emitted when an outcome evaluation cycle begins.

id: String

Unique identifier for this event.

iteration: Integer

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

outcome\_id: String

The `outc_` ID of the outcome being evaluated.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.outcome\_evaluation\_start"

BetaManagedAgentsStreamSessionEvents = [BetaManagedAgentsUserMessageEvent](api/beta.md) { id, content, type, processed\_at }  | [BetaManagedAgentsUserInterruptEvent](api/beta.md) { id, type, processed\_at, session\_thread\_id }  | [BetaManagedAgentsUserToolConfirmationEvent](api/beta.md) { id, result, tool\_use\_id, 4 more }  | 28 more

Server-sent event in the session stream.

Accepts one of the following:

class BetaManagedAgentsUserMessageEvent { id, content, type, processed\_at }

A user message event in the session conversation.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

type: :"user.message"

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent { id, type, processed\_at, session\_thread\_id }

An interrupt event that pauses agent execution and returns control to the user.

id: String

Unique identifier for this event.

type: :"user.interrupt"

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

class BetaManagedAgentsUserToolConfirmationEvent { id, result, tool\_use\_id, 4 more }

A tool confirmation event that approves or denies a pending tool execution.

id: String

Unique identifier for this event.

result: :allow | :deny

UserToolConfirmationResult enum

Accepts one of the following:

:allow

:deny

tool\_use\_id: String

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.tool\_confirmation"

deny\_message: String

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

class BetaManagedAgentsUserCustomToolResultEvent { id, custom\_tool\_use\_id, type, 4 more }

Event sent by the client providing the result of a custom tool execution.

id: String

Unique identifier for this event.

custom\_tool\_use\_id: String

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.custom\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

class BetaManagedAgentsAgentCustomToolUseEvent { id, input, name, 3 more }

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

name: String

Name of the custom tool being called.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.custom\_tool\_use"

session\_thread\_id: String

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

class BetaManagedAgentsAgentMessageEvent { id, content, processed\_at, type }

An agent response event in the session conversation.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type } ]

Array of text blocks comprising the agent response.

text: String

The text content.

type: :text

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.message"

class BetaManagedAgentsAgentThinkingEvent { id, processed\_at, type }

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thinking"

class BetaManagedAgentsAgentMCPToolUseEvent { id, input, mcp\_server\_name, 5 more }

Event emitted when the agent invokes a tool provided by an MCP server.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

mcp\_server\_name: String

Name of the MCP server providing the tool.

name: String

Name of the MCP tool being used.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.mcp\_tool\_use"

evaluated\_permission: :allow | :ask | :deny

AgentEvaluatedPermission enum

Accepts one of the following:

:allow

:ask

:deny

session\_thread\_id: String

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

class BetaManagedAgentsAgentMCPToolResultEvent { id, mcp\_tool\_use\_id, processed\_at, 3 more }

Event representing the result of an MCP tool execution.

id: String

Unique identifier for this event.

mcp\_tool\_use\_id: String

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.mcp\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent { id, input, name, 4 more }

Event emitted when the agent invokes a built-in agent tool.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

name: String

Name of the agent tool being used.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.tool\_use"

evaluated\_permission: :allow | :ask | :deny

AgentEvaluatedPermission enum

Accepts one of the following:

:allow

:ask

:deny

session\_thread\_id: String

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

class BetaManagedAgentsAgentToolResultEvent { id, processed\_at, tool\_use\_id, 3 more }

Event representing the result of an agent tool execution.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

tool\_use\_id: String

The id of the `agent.tool_use` event this result corresponds to.

type: :"agent.tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentThreadMessageReceivedEvent { id, content, from\_session\_thread\_id, 3 more }

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Message content blocks.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

from\_session\_thread\_id: String

Public `sthr_` ID of the thread that sent the message.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thread\_message\_received"

from\_agent\_name: String

Name of the callable agent this message came from. Absent when received from the primary agent.

class BetaManagedAgentsAgentThreadMessageSentEvent { id, content, processed\_at, 3 more }

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Message content blocks.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

processed\_at: Time

A timestamp in RFC 3339 format

to\_session\_thread\_id: String

Public `sthr_` ID of the thread the message was sent to.

type: :"agent.thread\_message\_sent"

to\_agent\_name: String

Name of the callable agent this message was sent to. Absent when sent to the primary agent.

class BetaManagedAgentsAgentThreadContextCompactedEvent { id, processed\_at, type }

Indicates that context compaction (summarization) occurred during the session.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thread\_context\_compacted"

class BetaManagedAgentsSessionErrorEvent { id, error, processed\_at, type }

An error event indicating a problem occurred during session execution.

id: String

Unique identifier for this event.

error: [BetaManagedAgentsUnknownError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelOverloadedError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelRateLimitedError](api/beta.md) { message, retry\_status, type }  | 4 more

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :unknown\_error

class BetaManagedAgentsModelOverloadedError { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_overloaded\_error

class BetaManagedAgentsModelRateLimitedError { message, retry\_status, type }

The model request was rate-limited.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_rate\_limited\_error

class BetaManagedAgentsModelRequestFailedError { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_request\_failed\_error

class BetaManagedAgentsMCPConnectionFailedError { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: String

Name of the MCP server that failed to connect.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_connection\_failed\_error

class BetaManagedAgentsMCPAuthenticationFailedError { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: String

Name of the MCP server that failed authentication.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_authentication\_failed\_error

class BetaManagedAgentsBillingError { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :billing\_error

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.error"

class BetaManagedAgentsSessionStatusRescheduledEvent { id, processed\_at, type }

Indicates the session is recovering from an error state and is rescheduled for execution.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_rescheduled"

class BetaManagedAgentsSessionStatusRunningEvent { id, processed\_at, type }

Indicates the session is actively running and the agent is working.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_running"

class BetaManagedAgentsSessionStatusIdleEvent { id, processed\_at, stop\_reason, type }

Indicates the agent has paused and is awaiting user input.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta.md) { type }  | [BetaManagedAgentsSessionRequiresAction](api/beta.md) { event\_ids, type }  | [BetaManagedAgentsSessionRetriesExhausted](api/beta.md) { type }

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn { type }

The agent completed its turn naturally and is ready for the next user message.

type: :end\_turn

class BetaManagedAgentsSessionRequiresAction { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: Array[String]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: :requires\_action

class BetaManagedAgentsSessionRetriesExhausted { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: :retries\_exhausted

type: :"session.status\_idle"

class BetaManagedAgentsSessionStatusTerminatedEvent { id, processed\_at, type }

Indicates the session has terminated, either due to an error or completion.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_terminated"

class BetaManagedAgentsSessionThreadCreatedEvent { id, agent\_name, processed\_at, 2 more }

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

id: String

Unique identifier for this event.

agent\_name: String

Name of the callable agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public `sthr_` ID of the newly created thread.

type: :"session.thread\_created"

class BetaManagedAgentsSpanOutcomeEvaluationStartEvent { id, iteration, outcome\_id, 2 more }

Emitted when an outcome evaluation cycle begins.

id: String

Unique identifier for this event.

iteration: Integer

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

outcome\_id: String

The `outc_` ID of the outcome being evaluated.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.outcome\_evaluation\_start"

class BetaManagedAgentsSpanOutcomeEvaluationEndEvent { id, explanation, iteration, 6 more }

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

id: String

Unique identifier for this event.

explanation: String

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

iteration: Integer

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_evaluation\_start\_id: String

The id of the corresponding `span.outcome_evaluation_start` event.

outcome\_id: String

The `outc_` ID of the outcome being evaluated.

processed\_at: Time

A timestamp in RFC 3339 format

result: String

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

type: :"span.outcome\_evaluation\_end"

usage: [BetaManagedAgentsSpanModelUsage](api/beta.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: Integer

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: Integer

Tokens read from prompt cache in this request.

input\_tokens: Integer

Input tokens consumed by this request.

output\_tokens: Integer

Output tokens generated by this request.

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

class BetaManagedAgentsSpanModelRequestStartEvent { id, processed\_at, type }

Emitted when a model request is initiated by the agent.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.model\_request\_start"

class BetaManagedAgentsSpanModelRequestEndEvent { id, is\_error, model\_request\_start\_id, 3 more }

Emitted when a model request completes.

id: String

Unique identifier for this event.

is\_error: bool

Whether the model request resulted in an error.

model\_request\_start\_id: String

The id of the corresponding `span.model_request_start` event.

model\_usage: [BetaManagedAgentsSpanModelUsage](api/beta.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: Integer

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: Integer

Tokens read from prompt cache in this request.

input\_tokens: Integer

Input tokens consumed by this request.

output\_tokens: Integer

Output tokens generated by this request.

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.model\_request\_end"

class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent { id, iteration, outcome\_id, 2 more }

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

id: String

Unique identifier for this event.

iteration: Integer

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_id: String

The `outc_` ID of the outcome being evaluated.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.outcome\_evaluation\_ongoing"

class BetaManagedAgentsUserDefineOutcomeEvent { id, description, max\_iterations, 4 more }

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

id: String

Unique identifier for this event.

description: String

What the agent should produce. Copied from the input event.

max\_iterations: Integer

Evaluate-then-revise cycles before giving up. Default 3, max 20.

outcome\_id: String

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

processed\_at: Time

A timestamp in RFC 3339 format

rubric: [BetaManagedAgentsFileRubric](api/beta.md) { file\_id, type }  | [BetaManagedAgentsTextRubric](api/beta.md) { content, type }

Rubric for grading the quality of an outcome.

Accepts one of the following:

class BetaManagedAgentsFileRubric { file\_id, type }

Rubric referenced by a file uploaded via the Files API.

file\_id: String

ID of the rubric file.

type: :file

class BetaManagedAgentsTextRubric { content, type }

Rubric content provided inline as text.

content: String

Rubric content. Plain text or markdown — the grader treats it as freeform text.

type: :text

type: :"user.define\_outcome"

class BetaManagedAgentsSessionDeletedEvent { id, processed\_at, type }

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.deleted"

class BetaManagedAgentsSessionThreadStatusRunningEvent { id, agent\_name, processed\_at, 2 more }

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: String

Unique identifier for this event.

agent\_name: String

Name of the agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public sthr\_ ID of the thread that started running.

type: :"session.thread\_status\_running"

class BetaManagedAgentsSessionThreadStatusIdleEvent { id, agent\_name, processed\_at, 3 more }

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: String

Unique identifier for this event.

agent\_name: String

Name of the agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public sthr\_ ID of the thread that went idle.

stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta.md) { type }  | [BetaManagedAgentsSessionRequiresAction](api/beta.md) { event\_ids, type }  | [BetaManagedAgentsSessionRetriesExhausted](api/beta.md) { type }

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn { type }

The agent completed its turn naturally and is ready for the next user message.

type: :end\_turn

class BetaManagedAgentsSessionRequiresAction { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: Array[String]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: :requires\_action

class BetaManagedAgentsSessionRetriesExhausted { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: :retries\_exhausted

type: :"session.thread\_status\_idle"

class BetaManagedAgentsSessionThreadStatusTerminatedEvent { id, agent\_name, processed\_at, 2 more }

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: String

Unique identifier for this event.

agent\_name: String

Name of the agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public sthr\_ ID of the thread that terminated.

type: :"session.thread\_status\_terminated"

class BetaManagedAgentsSessionThreadStatusRescheduledEvent { id, agent\_name, processed\_at, 2 more }

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: String

Unique identifier for this event.

agent\_name: String

Name of the agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public sthr\_ ID of the thread that is retrying.

type: :"session.thread\_status\_rescheduled"

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsTextRubric { content, type }

Rubric content provided inline as text.

content: String

Rubric content. Plain text or markdown — the grader treats it as freeform text.

type: :text

class BetaManagedAgentsTextRubricParams { content, type }

Rubric content provided inline as text.

content: String

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

type: :text

class BetaManagedAgentsUnknownError { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :unknown\_error

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsUserCustomToolResultEvent { id, custom\_tool\_use\_id, type, 4 more }

Event sent by the client providing the result of a custom tool execution.

id: String

Unique identifier for this event.

custom\_tool\_use\_id: String

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.custom\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

class BetaManagedAgentsUserCustomToolResultEventParams { custom\_tool\_use\_id, type, content, is\_error }

Parameters for providing the result of a custom tool execution.

custom\_tool\_use\_id: String

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.custom\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsUserDefineOutcomeEvent { id, description, max\_iterations, 4 more }

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

id: String

Unique identifier for this event.

description: String

What the agent should produce. Copied from the input event.

max\_iterations: Integer

Evaluate-then-revise cycles before giving up. Default 3, max 20.

outcome\_id: String

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

processed\_at: Time

A timestamp in RFC 3339 format

rubric: [BetaManagedAgentsFileRubric](api/beta.md) { file\_id, type }  | [BetaManagedAgentsTextRubric](api/beta.md) { content, type }

Rubric for grading the quality of an outcome.

Accepts one of the following:

class BetaManagedAgentsFileRubric { file\_id, type }

Rubric referenced by a file uploaded via the Files API.

file\_id: String

ID of the rubric file.

type: :file

class BetaManagedAgentsTextRubric { content, type }

Rubric content provided inline as text.

content: String

Rubric content. Plain text or markdown — the grader treats it as freeform text.

type: :text

type: :"user.define\_outcome"

class BetaManagedAgentsUserDefineOutcomeEventParams { description, rubric, type, max\_iterations }

Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

description: String

What the agent should produce. This is the task specification.

rubric: [BetaManagedAgentsFileRubricParams](api/beta.md) { file\_id, type }  | [BetaManagedAgentsTextRubricParams](api/beta.md) { content, type }

Rubric for grading the quality of an outcome.

Accepts one of the following:

class BetaManagedAgentsFileRubricParams { file\_id, type }

Rubric referenced by a file uploaded via the Files API.

file\_id: String

ID of the rubric file.

type: :file

class BetaManagedAgentsTextRubricParams { content, type }

Rubric content provided inline as text.

content: String

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

type: :text

type: :"user.define\_outcome"

max\_iterations: Integer

Eval→revision cycles before giving up. Default 3, max 20.

class BetaManagedAgentsUserInterruptEvent { id, type, processed\_at, session\_thread\_id }

An interrupt event that pauses agent execution and returns control to the user.

id: String

Unique identifier for this event.

type: :"user.interrupt"

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

class BetaManagedAgentsUserInterruptEventParams { type, session\_thread\_id }

Parameters for sending an interrupt to pause the agent.

type: :"user.interrupt"

session\_thread\_id: String

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

class BetaManagedAgentsUserMessageEvent { id, content, type, processed\_at }

A user message event in the session conversation.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

type: :"user.message"

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserMessageEventParams { content, type }

Parameters for sending a user message to the session.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Array of content blocks for the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

type: :"user.message"

class BetaManagedAgentsUserToolConfirmationEvent { id, result, tool\_use\_id, 4 more }

A tool confirmation event that approves or denies a pending tool execution.

id: String

Unique identifier for this event.

result: :allow | :deny

UserToolConfirmationResult enum

Accepts one of the following:

:allow

:deny

tool\_use\_id: String

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.tool\_confirmation"

deny\_message: String

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

class BetaManagedAgentsUserToolConfirmationEventParams { result, tool\_use\_id, type, deny\_message }

Parameters for confirming or denying a tool execution request.

result: :allow | :deny

UserToolConfirmationResult enum

Accepts one of the following:

:allow

:deny

tool\_use\_id: String

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.tool\_confirmation"

deny\_message: String

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

#### SessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

beta.sessions.resources.add(session\_id, \*\*kwargs) -> [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

beta.sessions.resources.list(session\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsSessionResource](api/beta.md)>

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

beta.sessions.resources.retrieve(resource\_id, \*\*kwargs) -> [ResourceRetrieveResponse](api/beta.md)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

beta.sessions.resources.update(resource\_id, \*\*kwargs) -> [ResourceUpdateResponse](api/beta.md)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

beta.sessions.resources.delete(resource\_id, \*\*kwargs) -> [BetaManagedAgentsDeleteSessionResource](api/beta.md) { id, type }

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

##### ModelsExpand Collapse

class BetaManagedAgentsDeleteSessionResource { id, type }

Confirmation of resource deletion.

id: String

type: :session\_resource\_deleted

class BetaManagedAgentsFileResource { id, created\_at, file\_id, 3 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

file\_id: String

mount\_path: String

type: :file

updated\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsGitHubRepositoryResource { id, created\_at, mount\_path, 4 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

mount\_path: String

type: :github\_repository

updated\_at: Time

A timestamp in RFC 3339 format

url: String

checkout: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }

Accepts one of the following:

class BetaManagedAgentsBranchCheckout { name, type }

name: String

Branch name to check out.

type: :branch

class BetaManagedAgentsCommitCheckout { sha, type }

sha: String

Full commit SHA to check out.

type: :commit

class BetaManagedAgentsMemoryStoreResource { memory\_store\_id, type, access, 4 more }

A memory store attached to an agent session.

memory\_store\_id: String

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: :memory\_store

access: :read\_write | :read\_only

Access mode for an attached memory store.

Accepts one of the following:

:read\_write

:read\_only

description: String

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

instructions: String

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

mount\_path: String

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

name: String

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

BetaManagedAgentsSessionResource = [BetaManagedAgentsGitHubRepositoryResource](api/beta.md) { id, created\_at, mount\_path, 4 more }  | [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }  | [BetaManagedAgentsMemoryStoreResource](api/beta.md) { memory\_store\_id, type, access, 4 more }

A memory store attached to an agent session.

Accepts one of the following:

class BetaManagedAgentsGitHubRepositoryResource { id, created\_at, mount\_path, 4 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

mount\_path: String

type: :github\_repository

updated\_at: Time

A timestamp in RFC 3339 format

url: String

checkout: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }

Accepts one of the following:

class BetaManagedAgentsBranchCheckout { name, type }

name: String

Branch name to check out.

type: :branch

class BetaManagedAgentsCommitCheckout { sha, type }

sha: String

Full commit SHA to check out.

type: :commit

class BetaManagedAgentsFileResource { id, created\_at, file\_id, 3 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

file\_id: String

mount\_path: String

type: :file

updated\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsMemoryStoreResource { memory\_store\_id, type, access, 4 more }

A memory store attached to an agent session.

memory\_store\_id: String

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: :memory\_store

access: :read\_write | :read\_only

Access mode for an attached memory store.

Accepts one of the following:

:read\_write

:read\_only

description: String

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

instructions: String

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

mount\_path: String

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

name: String

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

ResourceRetrieveResponse = [BetaManagedAgentsGitHubRepositoryResource](api/beta.md) { id, created\_at, mount\_path, 4 more }  | [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }  | [BetaManagedAgentsMemoryStoreResource](api/beta.md) { memory\_store\_id, type, access, 4 more }

The requested session resource.

Accepts one of the following:

class BetaManagedAgentsGitHubRepositoryResource { id, created\_at, mount\_path, 4 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

mount\_path: String

type: :github\_repository

updated\_at: Time

A timestamp in RFC 3339 format

url: String

checkout: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }

Accepts one of the following:

class BetaManagedAgentsBranchCheckout { name, type }

name: String

Branch name to check out.

type: :branch

class BetaManagedAgentsCommitCheckout { sha, type }

sha: String

Full commit SHA to check out.

type: :commit

class BetaManagedAgentsFileResource { id, created\_at, file\_id, 3 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

file\_id: String

mount\_path: String

type: :file

updated\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsMemoryStoreResource { memory\_store\_id, type, access, 4 more }

A memory store attached to an agent session.

memory\_store\_id: String

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: :memory\_store

access: :read\_write | :read\_only

Access mode for an attached memory store.

Accepts one of the following:

:read\_write

:read\_only

description: String

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

instructions: String

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

mount\_path: String

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

name: String

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

ResourceUpdateResponse = [BetaManagedAgentsGitHubRepositoryResource](api/beta.md) { id, created\_at, mount\_path, 4 more }  | [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }  | [BetaManagedAgentsMemoryStoreResource](api/beta.md) { memory\_store\_id, type, access, 4 more }

The updated session resource.

Accepts one of the following:

class BetaManagedAgentsGitHubRepositoryResource { id, created\_at, mount\_path, 4 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

mount\_path: String

type: :github\_repository

updated\_at: Time

A timestamp in RFC 3339 format

url: String

checkout: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }

Accepts one of the following:

class BetaManagedAgentsBranchCheckout { name, type }

name: String

Branch name to check out.

type: :branch

class BetaManagedAgentsCommitCheckout { sha, type }

sha: String

Full commit SHA to check out.

type: :commit

class BetaManagedAgentsFileResource { id, created\_at, file\_id, 3 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

file\_id: String

mount\_path: String

type: :file

updated\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsMemoryStoreResource { memory\_store\_id, type, access, 4 more }

A memory store attached to an agent session.

memory\_store\_id: String

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: :memory\_store

access: :read\_write | :read\_only

Access mode for an attached memory store.

Accepts one of the following:

:read\_write

:read\_only

description: String

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

instructions: String

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

mount\_path: String

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

name: String

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### SessionsThreads

##### [List Session Threads](api/beta/sessions/threads/list.md)

beta.sessions.threads.list(session\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsSessionThread](api/beta.md) { id, agent, archived\_at, 8 more } >

GET/v1/sessions/{session\_id}/threads

##### [Get Session Thread](api/beta/sessions/threads/retrieve.md)

beta.sessions.threads.retrieve(thread\_id, \*\*kwargs) -> [BetaManagedAgentsSessionThread](api/beta.md) { id, agent, archived\_at, 8 more }

GET/v1/sessions/{session\_id}/threads/{thread\_id}

##### [Archive Session Thread](api/beta/sessions/threads/archive.md)

beta.sessions.threads.archive(thread\_id, \*\*kwargs) -> [BetaManagedAgentsSessionThread](api/beta.md) { id, agent, archived\_at, 8 more }

POST/v1/sessions/{session\_id}/threads/{thread\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsSessionThread { id, agent, archived\_at, 8 more }

An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

id: String

Unique identifier for this thread.

agent: [BetaManagedAgentsSessionThreadAgent](api/beta.md) { id, description, mcp\_servers, 7 more }

Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

id: String

description: String

mcp\_servers: Array[[BetaManagedAgentsMCPServerURLDefinition](api/beta.md) { name, type, url } ]

name: String

type: :url

url: String

model: [BetaManagedAgentsModelConfig](api/beta.md) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

String

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

name: String

skills: Array[[BetaManagedAgentsAnthropicSkill](api/beta.md) { skill\_id, type, version }  | [BetaManagedAgentsCustomSkill](api/beta.md) { skill\_id, type, version } ]

Accepts one of the following:

class BetaManagedAgentsAnthropicSkill { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: String

type: :anthropic

version: String

class BetaManagedAgentsCustomSkill { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: String

type: :custom

version: String

system\_: String

tools: Array[[BetaManagedAgentsAgentToolset20260401](api/beta.md) { configs, default\_config, type }  | [BetaManagedAgentsMCPToolset](api/beta.md) { configs, default\_config, mcp\_server\_name, type }  | [BetaManagedAgentsCustomTool](api/beta.md) { description, input\_schema, name, type } ]

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401 { configs, default\_config, type }

configs: Array[[BetaManagedAgentsAgentToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool

name: :bash | :edit | :read | 5 more

Built-in agent tool identifier.

Accepts one of the following:

:bash

:edit

:read

:write

:glob

:grep

:web\_fetch

:web\_search

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: bool

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

type: :agent\_toolset\_20260401

class BetaManagedAgentsMCPToolset { configs, default\_config, mcp\_server\_name, type }

configs: Array[[BetaManagedAgentsMCPToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool

name: String

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: bool

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

mcp\_server\_name: String

type: :mcp\_toolset

class BetaManagedAgentsCustomTool { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: String

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: Hash[Symbol, untyped]

JSON Schema properties defining the tool's input parameters.

required: Array[String]

List of required property names.

type: :object

Must be 'object' for tool input schemas.

name: String

type: :custom

type: :agent

version: Integer

archived\_at: Time

A timestamp in RFC 3339 format

created\_at: Time

A timestamp in RFC 3339 format

parent\_thread\_id: String

Parent thread that spawned this thread. Null for the primary thread.

session\_id: String

The session this thread belongs to.

stats: [BetaManagedAgentsSessionThreadStats](api/beta.md) { active\_seconds, duration\_seconds, startup\_seconds }

Timing statistics for a session thread.

active\_seconds: Float

Cumulative time in seconds the thread spent actively running. Excludes idle time.

duration\_seconds: Float

Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

startup\_seconds: Float

Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

status: [BetaManagedAgentsSessionThreadStatus](api/beta.md)

SessionThreadStatus enum

Accepts one of the following:

:running

:idle

:rescheduling

:terminated

type: :session\_thread

updated\_at: Time

A timestamp in RFC 3339 format

usage: [BetaManagedAgentsSessionThreadUsage](api/beta.md) { cache\_creation, cache\_read\_input\_tokens, input\_tokens, output\_tokens }

Cumulative token usage for a session thread across all turns.

cache\_creation: [BetaManagedAgentsCacheCreationUsage](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: Integer

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: Integer

Tokens used to create 5-minute ephemeral cache entries.

cache\_read\_input\_tokens: Integer

Total tokens read from prompt cache.

input\_tokens: Integer

Total input tokens consumed across all turns.

output\_tokens: Integer

Total output tokens generated across all turns.

class BetaManagedAgentsSessionThreadAgent { id, description, mcp\_servers, 7 more }

Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

id: String

description: String

mcp\_servers: Array[[BetaManagedAgentsMCPServerURLDefinition](api/beta.md) { name, type, url } ]

name: String

type: :url

url: String

model: [BetaManagedAgentsModelConfig](api/beta.md) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

String

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

name: String

skills: Array[[BetaManagedAgentsAnthropicSkill](api/beta.md) { skill\_id, type, version }  | [BetaManagedAgentsCustomSkill](api/beta.md) { skill\_id, type, version } ]

Accepts one of the following:

class BetaManagedAgentsAnthropicSkill { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: String

type: :anthropic

version: String

class BetaManagedAgentsCustomSkill { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: String

type: :custom

version: String

system\_: String

tools: Array[[BetaManagedAgentsAgentToolset20260401](api/beta.md) { configs, default\_config, type }  | [BetaManagedAgentsMCPToolset](api/beta.md) { configs, default\_config, mcp\_server\_name, type }  | [BetaManagedAgentsCustomTool](api/beta.md) { description, input\_schema, name, type } ]

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401 { configs, default\_config, type }

configs: Array[[BetaManagedAgentsAgentToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool

name: :bash | :edit | :read | 5 more

Built-in agent tool identifier.

Accepts one of the following:

:bash

:edit

:read

:write

:glob

:grep

:web\_fetch

:web\_search

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: bool

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

type: :agent\_toolset\_20260401

class BetaManagedAgentsMCPToolset { configs, default\_config, mcp\_server\_name, type }

configs: Array[[BetaManagedAgentsMCPToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool

name: String

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: bool

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

mcp\_server\_name: String

type: :mcp\_toolset

class BetaManagedAgentsCustomTool { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: String

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: Hash[Symbol, untyped]

JSON Schema properties defining the tool's input parameters.

required: Array[String]

List of required property names.

type: :object

Must be 'object' for tool input schemas.

name: String

type: :custom

type: :agent

version: Integer

class BetaManagedAgentsSessionThreadStats { active\_seconds, duration\_seconds, startup\_seconds }

Timing statistics for a session thread.

active\_seconds: Float

Cumulative time in seconds the thread spent actively running. Excludes idle time.

duration\_seconds: Float

Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

startup\_seconds: Float

Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

BetaManagedAgentsSessionThreadStatus = :running | :idle | :rescheduling | :terminated

SessionThreadStatus enum

Accepts one of the following:

:running

:idle

:rescheduling

:terminated

class BetaManagedAgentsSessionThreadUsage { cache\_creation, cache\_read\_input\_tokens, input\_tokens, output\_tokens }

Cumulative token usage for a session thread across all turns.

cache\_creation: [BetaManagedAgentsCacheCreationUsage](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: Integer

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: Integer

Tokens used to create 5-minute ephemeral cache entries.

cache\_read\_input\_tokens: Integer

Total tokens read from prompt cache.

input\_tokens: Integer

Total input tokens consumed across all turns.

output\_tokens: Integer

Total output tokens generated across all turns.

BetaManagedAgentsStreamSessionThreadEvents = [BetaManagedAgentsUserMessageEvent](api/beta.md) { id, content, type, processed\_at }  | [BetaManagedAgentsUserInterruptEvent](api/beta.md) { id, type, processed\_at, session\_thread\_id }  | [BetaManagedAgentsUserToolConfirmationEvent](api/beta.md) { id, result, tool\_use\_id, 4 more }  | 28 more

Server-sent event in a single thread's stream.

Accepts one of the following:

class BetaManagedAgentsUserMessageEvent { id, content, type, processed\_at }

A user message event in the session conversation.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

type: :"user.message"

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent { id, type, processed\_at, session\_thread\_id }

An interrupt event that pauses agent execution and returns control to the user.

id: String

Unique identifier for this event.

type: :"user.interrupt"

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

class BetaManagedAgentsUserToolConfirmationEvent { id, result, tool\_use\_id, 4 more }

A tool confirmation event that approves or denies a pending tool execution.

id: String

Unique identifier for this event.

result: :allow | :deny

UserToolConfirmationResult enum

Accepts one of the following:

:allow

:deny

tool\_use\_id: String

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.tool\_confirmation"

deny\_message: String

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

class BetaManagedAgentsUserCustomToolResultEvent { id, custom\_tool\_use\_id, type, 4 more }

Event sent by the client providing the result of a custom tool execution.

id: String

Unique identifier for this event.

custom\_tool\_use\_id: String

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.custom\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

class BetaManagedAgentsAgentCustomToolUseEvent { id, input, name, 3 more }

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

name: String

Name of the custom tool being called.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.custom\_tool\_use"

session\_thread\_id: String

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

class BetaManagedAgentsAgentMessageEvent { id, content, processed\_at, type }

An agent response event in the session conversation.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type } ]

Array of text blocks comprising the agent response.

text: String

The text content.

type: :text

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.message"

class BetaManagedAgentsAgentThinkingEvent { id, processed\_at, type }

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thinking"

class BetaManagedAgentsAgentMCPToolUseEvent { id, input, mcp\_server\_name, 5 more }

Event emitted when the agent invokes a tool provided by an MCP server.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

mcp\_server\_name: String

Name of the MCP server providing the tool.

name: String

Name of the MCP tool being used.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.mcp\_tool\_use"

evaluated\_permission: :allow | :ask | :deny

AgentEvaluatedPermission enum

Accepts one of the following:

:allow

:ask

:deny

session\_thread\_id: String

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

class BetaManagedAgentsAgentMCPToolResultEvent { id, mcp\_tool\_use\_id, processed\_at, 3 more }

Event representing the result of an MCP tool execution.

id: String

Unique identifier for this event.

mcp\_tool\_use\_id: String

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.mcp\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent { id, input, name, 4 more }

Event emitted when the agent invokes a built-in agent tool.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

name: String

Name of the agent tool being used.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.tool\_use"

evaluated\_permission: :allow | :ask | :deny

AgentEvaluatedPermission enum

Accepts one of the following:

:allow

:ask

:deny

session\_thread\_id: String

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

class BetaManagedAgentsAgentToolResultEvent { id, processed\_at, tool\_use\_id, 3 more }

Event representing the result of an agent tool execution.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

tool\_use\_id: String

The id of the `agent.tool_use` event this result corresponds to.

type: :"agent.tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentThreadMessageReceivedEvent { id, content, from\_session\_thread\_id, 3 more }

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Message content blocks.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

from\_session\_thread\_id: String

Public `sthr_` ID of the thread that sent the message.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thread\_message\_received"

from\_agent\_name: String

Name of the callable agent this message came from. Absent when received from the primary agent.

class BetaManagedAgentsAgentThreadMessageSentEvent { id, content, processed\_at, 3 more }

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Message content blocks.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

processed\_at: Time

A timestamp in RFC 3339 format

to\_session\_thread\_id: String

Public `sthr_` ID of the thread the message was sent to.

type: :"agent.thread\_message\_sent"

to\_agent\_name: String

Name of the callable agent this message was sent to. Absent when sent to the primary agent.

class BetaManagedAgentsAgentThreadContextCompactedEvent { id, processed\_at, type }

Indicates that context compaction (summarization) occurred during the session.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thread\_context\_compacted"

class BetaManagedAgentsSessionErrorEvent { id, error, processed\_at, type }

An error event indicating a problem occurred during session execution.

id: String

Unique identifier for this event.

error: [BetaManagedAgentsUnknownError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelOverloadedError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelRateLimitedError](api/beta.md) { message, retry\_status, type }  | 4 more

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :unknown\_error

class BetaManagedAgentsModelOverloadedError { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_overloaded\_error

class BetaManagedAgentsModelRateLimitedError { message, retry\_status, type }

The model request was rate-limited.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_rate\_limited\_error

class BetaManagedAgentsModelRequestFailedError { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_request\_failed\_error

class BetaManagedAgentsMCPConnectionFailedError { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: String

Name of the MCP server that failed to connect.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_connection\_failed\_error

class BetaManagedAgentsMCPAuthenticationFailedError { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: String

Name of the MCP server that failed authentication.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_authentication\_failed\_error

class BetaManagedAgentsBillingError { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :billing\_error

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.error"

class BetaManagedAgentsSessionStatusRescheduledEvent { id, processed\_at, type }

Indicates the session is recovering from an error state and is rescheduled for execution.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_rescheduled"

class BetaManagedAgentsSessionStatusRunningEvent { id, processed\_at, type }

Indicates the session is actively running and the agent is working.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_running"

class BetaManagedAgentsSessionStatusIdleEvent { id, processed\_at, stop\_reason, type }

Indicates the agent has paused and is awaiting user input.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta.md) { type }  | [BetaManagedAgentsSessionRequiresAction](api/beta.md) { event\_ids, type }  | [BetaManagedAgentsSessionRetriesExhausted](api/beta.md) { type }

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn { type }

The agent completed its turn naturally and is ready for the next user message.

type: :end\_turn

class BetaManagedAgentsSessionRequiresAction { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: Array[String]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: :requires\_action

class BetaManagedAgentsSessionRetriesExhausted { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: :retries\_exhausted

type: :"session.status\_idle"

class BetaManagedAgentsSessionStatusTerminatedEvent { id, processed\_at, type }

Indicates the session has terminated, either due to an error or completion.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_terminated"

class BetaManagedAgentsSessionThreadCreatedEvent { id, agent\_name, processed\_at, 2 more }

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

id: String

Unique identifier for this event.

agent\_name: String

Name of the callable agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public `sthr_` ID of the newly created thread.

type: :"session.thread\_created"

class BetaManagedAgentsSpanOutcomeEvaluationStartEvent { id, iteration, outcome\_id, 2 more }

Emitted when an outcome evaluation cycle begins.

id: String

Unique identifier for this event.

iteration: Integer

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

outcome\_id: String

The `outc_` ID of the outcome being evaluated.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.outcome\_evaluation\_start"

class BetaManagedAgentsSpanOutcomeEvaluationEndEvent { id, explanation, iteration, 6 more }

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

id: String

Unique identifier for this event.

explanation: String

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

iteration: Integer

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_evaluation\_start\_id: String

The id of the corresponding `span.outcome_evaluation_start` event.

outcome\_id: String

The `outc_` ID of the outcome being evaluated.

processed\_at: Time

A timestamp in RFC 3339 format

result: String

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

type: :"span.outcome\_evaluation\_end"

usage: [BetaManagedAgentsSpanModelUsage](api/beta.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: Integer

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: Integer

Tokens read from prompt cache in this request.

input\_tokens: Integer

Input tokens consumed by this request.

output\_tokens: Integer

Output tokens generated by this request.

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

class BetaManagedAgentsSpanModelRequestStartEvent { id, processed\_at, type }

Emitted when a model request is initiated by the agent.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.model\_request\_start"

class BetaManagedAgentsSpanModelRequestEndEvent { id, is\_error, model\_request\_start\_id, 3 more }

Emitted when a model request completes.

id: String

Unique identifier for this event.

is\_error: bool

Whether the model request resulted in an error.

model\_request\_start\_id: String

The id of the corresponding `span.model_request_start` event.

model\_usage: [BetaManagedAgentsSpanModelUsage](api/beta.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: Integer

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: Integer

Tokens read from prompt cache in this request.

input\_tokens: Integer

Input tokens consumed by this request.

output\_tokens: Integer

Output tokens generated by this request.

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.model\_request\_end"

class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent { id, iteration, outcome\_id, 2 more }

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

id: String

Unique identifier for this event.

iteration: Integer

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_id: String

The `outc_` ID of the outcome being evaluated.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.outcome\_evaluation\_ongoing"

class BetaManagedAgentsUserDefineOutcomeEvent { id, description, max\_iterations, 4 more }

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

id: String

Unique identifier for this event.

description: String

What the agent should produce. Copied from the input event.

max\_iterations: Integer

Evaluate-then-revise cycles before giving up. Default 3, max 20.

outcome\_id: String

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

processed\_at: Time

A timestamp in RFC 3339 format

rubric: [BetaManagedAgentsFileRubric](api/beta.md) { file\_id, type }  | [BetaManagedAgentsTextRubric](api/beta.md) { content, type }

Rubric for grading the quality of an outcome.

Accepts one of the following:

class BetaManagedAgentsFileRubric { file\_id, type }

Rubric referenced by a file uploaded via the Files API.

file\_id: String

ID of the rubric file.

type: :file

class BetaManagedAgentsTextRubric { content, type }

Rubric content provided inline as text.

content: String

Rubric content. Plain text or markdown — the grader treats it as freeform text.

type: :text

type: :"user.define\_outcome"

class BetaManagedAgentsSessionDeletedEvent { id, processed\_at, type }

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.deleted"

class BetaManagedAgentsSessionThreadStatusRunningEvent { id, agent\_name, processed\_at, 2 more }

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: String

Unique identifier for this event.

agent\_name: String

Name of the agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public sthr\_ ID of the thread that started running.

type: :"session.thread\_status\_running"

class BetaManagedAgentsSessionThreadStatusIdleEvent { id, agent\_name, processed\_at, 3 more }

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: String

Unique identifier for this event.

agent\_name: String

Name of the agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public sthr\_ ID of the thread that went idle.

stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta.md) { type }  | [BetaManagedAgentsSessionRequiresAction](api/beta.md) { event\_ids, type }  | [BetaManagedAgentsSessionRetriesExhausted](api/beta.md) { type }

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn { type }

The agent completed its turn naturally and is ready for the next user message.

type: :end\_turn

class BetaManagedAgentsSessionRequiresAction { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: Array[String]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: :requires\_action

class BetaManagedAgentsSessionRetriesExhausted { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: :retries\_exhausted

type: :"session.thread\_status\_idle"

class BetaManagedAgentsSessionThreadStatusTerminatedEvent { id, agent\_name, processed\_at, 2 more }

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: String

Unique identifier for this event.

agent\_name: String

Name of the agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public sthr\_ ID of the thread that terminated.

type: :"session.thread\_status\_terminated"

class BetaManagedAgentsSessionThreadStatusRescheduledEvent { id, agent\_name, processed\_at, 2 more }

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: String

Unique identifier for this event.

agent\_name: String

Name of the agent the thread runs.

processed\_at: Time

A timestamp in RFC 3339 format

session\_thread\_id: String

Public sthr\_ ID of the thread that is retrying.

type: :"session.thread\_status\_rescheduled"

#### SessionsThreadsEvents

##### [List Session Thread Events](api/beta/sessions/threads/events/list.md)

beta.sessions.threads.events.list(thread\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsSessionEvent](api/beta.md)>

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/beta/sessions/threads/events/stream.md)

beta.sessions.threads.events.stream(thread\_id, \*\*kwargs) -> [BetaManagedAgentsStreamSessionThreadEvents](api/beta.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

---

*Copyright © Anthropic. All rights reserved.*
