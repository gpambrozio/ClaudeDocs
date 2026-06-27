# Sessions

Copy page



CLI

# Sessions

##### [Create Session](api/beta/sessions/create.md)

$ ant beta:sessions create

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

$ ant beta:sessions list

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

$ ant beta:sessions retrieve

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

$ ant beta:sessions update

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

$ ant beta:sessions delete

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

$ ant beta:sessions archive

POST/v1/sessions/{session\_id}/archive

##### ModelsExpand Collapse



beta\_managed\_agents\_agent\_params: object { id, type, version } 

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: string

The `agent` ID.



type: "agent"

"agent"

version: optional number

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.



beta\_managed\_agents\_branch\_checkout: object { name, type } 

name: string

Branch name to check out.



type: "branch"

"branch"



beta\_managed\_agents\_cache\_creation\_usage: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: optional number

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: optional number

Tokens used to create 5-minute ephemeral cache entries.



beta\_managed\_agents\_commit\_checkout: object { sha, type } 

sha: string

Full commit SHA to check out.



type: "commit"

"commit"



beta\_managed\_agents\_deleted\_session: object { id, type } 

Confirmation that a `session` has been permanently deleted.

id: string



type: "session\_deleted"

"session\_deleted"



beta\_managed\_agents\_file\_resource\_params: object { file\_id, type, mount\_path } 

Mount a file uploaded via the Files API into the session.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"

mount\_path: optional string

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.



beta\_managed\_agents\_github\_repository\_resource\_params: object { authorization\_token, type, url, 2 more } 

Mount a GitHub repository into the session's container.

authorization\_token: string

GitHub authorization token used to clone the repository.



type: "github\_repository"

"github\_repository"

url: string

Github URL of the repository



checkout: optional [BetaManagedAgentsBranchCheckout](api/beta/sessions.md) { name, type }  or [BetaManagedAgentsCommitCheckout](api/beta/sessions.md) { sha, type } 

Branch or commit to check out. Defaults to the repository's default branch.



beta\_managed\_agents\_branch\_checkout: object { name, type } 

name: string

Branch name to check out.



type: "branch"

"branch"



beta\_managed\_agents\_commit\_checkout: object { sha, type } 

sha: string

Full commit SHA to check out.



type: "commit"

"commit"

mount\_path: optional string

Mount path in the container. Defaults to `/workspace/<repo-name>`.



beta\_managed\_agents\_memory\_store\_resource\_param: object { memory\_store\_id, type, access, instructions } 

Parameters for attaching a memory store to an agent session.

memory\_store\_id: string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.



type: "memory\_store"

"memory\_store"



access: optional "read\_write" or "read\_only"

Access mode for an attached memory store.

"read\_write"

"read\_only"

instructions: optional string

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.



beta\_managed\_agents\_multiagent: object { agents, type } 

Resolved coordinator topology with a concrete agent roster.



agents: array of [BetaManagedAgentsAgentReference](api/beta/agents.md) { id, type, version } 

Agents the coordinator may spawn as session threads, each resolved to a specific version.

id: string



type: "agent"

"agent"

version: number



type: "coordinator"

"coordinator"



beta\_managed\_agents\_multiagent\_params: object { agents, type } 

A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.



agents: array of [BetaManagedAgentsMultiagentRosterEntryParams](api/beta/sessions.md)

Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

union\_member\_0: string



beta\_managed\_agents\_agent\_params: object { id, type, version } 

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: string

The `agent` ID.



type: "agent"

"agent"

version: optional number

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.



beta\_managed\_agents\_multiagent\_self\_params: object { type } 

Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.



type: "self"

"self"



type: "coordinator"

"coordinator"



beta\_managed\_agents\_multiagent\_roster\_entry\_params: string or [BetaManagedAgentsAgentParams](api/beta/sessions.md) { id, type, version }  or [BetaManagedAgentsMultiagentSelfParams](api/beta/agents.md) { type } 

An entry in a multiagent roster: an agent ID string, a versioned agent reference, or `self`.

union\_member\_0: string



beta\_managed\_agents\_agent\_params: object { id, type, version } 

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: string

The `agent` ID.



type: "agent"

"agent"

version: optional number

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.



beta\_managed\_agents\_multiagent\_self\_params: object { type } 

Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.



type: "self"

"self"



beta\_managed\_agents\_outcome\_evaluation\_resource: object { completed\_at, description, explanation, 4 more } 

Evaluation state for a single outcome defined via a define\_outcome event.

completed\_at: string

A timestamp in RFC 3339 format

description: string

What the agent should produce.

explanation: string

Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs\_revision (intermediate), what's missing; for failed, why unrecoverable.

iteration: number

0-indexed revision cycle the outcome is currently on.

outcome\_id: string

Server-generated outc\_ ID for this outcome.

result: string

Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.



type: "outcome\_evaluation"

"outcome\_evaluation"



beta\_managed\_agents\_session: object { id, agent, archived\_at, 13 more } 

A Managed Agents `session`.

id: string



agent: object { id, description, mcp\_servers, 8 more } 

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: string

description: string



mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md) { name, type, url } 

name: string



type: "url"

"url"

url: string



model: object { id, speed } 

Model identifier and configuration.



id: "claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more or string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

"standard"

"fast"



multiagent: object { agents, type } 

Resolved coordinator topology with full agent definitions for each roster member.



agents: array of [BetaManagedAgentsSessionThreadAgent](api/beta/agents.md) { id, description, mcp\_servers, 7 more } 

Full `agent` definitions the coordinator may spawn as session threads.

id: string

description: string



mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md) { name, type, url } 

name: string



type: "url"

"url"

url: string



model: object { id, speed } 

Model identifier and configuration.



id: "claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more or string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

"standard"

"fast"

name: string



skills: array of [BetaManagedAgentsAnthropicSkill](api/beta/agents.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta/agents.md) { skill\_id, type, version } 



beta\_managed\_agents\_anthropic\_skill: object { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: string



type: "anthropic"

"anthropic"

version: string



beta\_managed\_agents\_custom\_skill: object { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: string



type: "custom"

"custom"

version: string

system: string



tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta/agents.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta/agents.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta/agents.md) { description, input\_schema, name, type } 



beta\_managed\_agents\_agent\_toolset20260401: object { configs, default\_config, type } 



configs: array of [BetaManagedAgentsAgentToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean



name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



default\_config: object { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



type: "agent\_toolset\_20260401"

"agent\_toolset\_20260401"



beta\_managed\_agents\_mcp\_toolset: object { configs, default\_config, mcp\_server\_name, type } 



configs: array of [BetaManagedAgentsMCPToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean

name: string



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



default\_config: object { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"

mcp\_server\_name: string



type: "mcp\_toolset"

"mcp\_toolset"



beta\_managed\_agents\_custom\_tool: object { description, input\_schema, name, type } 

A custom tool as returned in API responses.

description: string



input\_schema: object { type, properties, required } 

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string



type: "custom"

"custom"



type: "agent"

"agent"

version: number



type: "coordinator"

"coordinator"

name: string



skills: array of [BetaManagedAgentsAnthropicSkill](api/beta/agents.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta/agents.md) { skill\_id, type, version } 



beta\_managed\_agents\_anthropic\_skill: object { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: string



type: "anthropic"

"anthropic"

version: string



beta\_managed\_agents\_custom\_skill: object { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: string



type: "custom"

"custom"

version: string

system: string



tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta/agents.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta/agents.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta/agents.md) { description, input\_schema, name, type } 



beta\_managed\_agents\_agent\_toolset20260401: object { configs, default\_config, type } 



configs: array of [BetaManagedAgentsAgentToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean



name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



default\_config: object { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



type: "agent\_toolset\_20260401"

"agent\_toolset\_20260401"



beta\_managed\_agents\_mcp\_toolset: object { configs, default\_config, mcp\_server\_name, type } 



configs: array of [BetaManagedAgentsMCPToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean

name: string



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



default\_config: object { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"

mcp\_server\_name: string



type: "mcp\_toolset"

"mcp\_toolset"



beta\_managed\_agents\_custom\_tool: object { description, input\_schema, name, type } 

A custom tool as returned in API responses.

description: string



input\_schema: object { type, properties, required } 

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string



type: "custom"

"custom"



type: "agent"

"agent"

version: number

archived\_at: string

A timestamp in RFC 3339 format

created\_at: string

A timestamp in RFC 3339 format

environment\_id: string

metadata: map[string]



outcome\_evaluations: array of [BetaManagedAgentsOutcomeEvaluationResource](api/beta/sessions.md) { completed\_at, description, explanation, 4 more } 

Per-outcome evaluation state. One entry per define\_outcome event sent to the session.

completed\_at: string

A timestamp in RFC 3339 format

description: string

What the agent should produce.

explanation: string

Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs\_revision (intermediate), what's missing; for failed, why unrecoverable.

iteration: number

0-indexed revision cycle the outcome is currently on.

outcome\_id: string

Server-generated outc\_ ID for this outcome.

result: string

Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.



type: "outcome\_evaluation"

"outcome\_evaluation"



resources: array of [BetaManagedAgentsSessionResource](api/beta/sessions/resources.md)



beta\_managed\_agents\_github\_repository\_resource: object { id, created\_at, mount\_path, 4 more } 

id: string

created\_at: string

A timestamp in RFC 3339 format

mount\_path: string



type: "github\_repository"

"github\_repository"

updated\_at: string

A timestamp in RFC 3339 format

url: string



checkout: optional [BetaManagedAgentsBranchCheckout](api/beta/sessions.md) { name, type }  or [BetaManagedAgentsCommitCheckout](api/beta/sessions.md) { sha, type } 



beta\_managed\_agents\_branch\_checkout: object { name, type } 

name: string

Branch name to check out.



type: "branch"

"branch"



beta\_managed\_agents\_commit\_checkout: object { sha, type } 

sha: string

Full commit SHA to check out.



type: "commit"

"commit"



beta\_managed\_agents\_file\_resource: object { id, created\_at, file\_id, 3 more } 

id: string

created\_at: string

A timestamp in RFC 3339 format

file\_id: string

mount\_path: string



type: "file"

"file"

updated\_at: string

A timestamp in RFC 3339 format



beta\_managed\_agents\_memory\_store\_resource: object { memory\_store\_id, type, access, 4 more } 

A memory store attached to an agent session.

memory\_store\_id: string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.



type: "memory\_store"

"memory\_store"



access: optional "read\_write" or "read\_only"

Access mode for an attached memory store.

"read\_write"

"read\_only"

description: optional string

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

instructions: optional string

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

mount\_path: optional string

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

name: optional string

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.



stats: object { active\_seconds, duration\_seconds } 

Timing statistics for a session.

active\_seconds: optional number

Cumulative time in seconds the session spent in running status. Excludes idle time.

duration\_seconds: optional number

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.



status: "rescheduling" or "running" or "idle" or "terminated"

SessionStatus enum

"rescheduling"

"running"

"idle"

"terminated"

title: string



type: "session"

"session"

updated\_at: string

A timestamp in RFC 3339 format



usage: object { cache\_creation, cache\_read\_input\_tokens, input\_tokens, output\_tokens } 

Cumulative token usage for a session across all turns.



cache\_creation: optional object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: optional number

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: optional number

Tokens used to create 5-minute ephemeral cache entries.

cache\_read\_input\_tokens: optional number

Total tokens read from prompt cache.

input\_tokens: optional number

Total input tokens consumed across all turns.

output\_tokens: optional number

Total output tokens generated across all turns.

vault\_ids: array of string

Vault IDs attached to the session at creation. Empty when no vaults were supplied.

deployment\_id: optional string

Deployment ID when the session was created from a deployment reference. Null otherwise.



beta\_managed\_agents\_session\_agent: object { id, description, mcp\_servers, 8 more } 

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: string

description: string



mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md) { name, type, url } 

name: string



type: "url"

"url"

url: string



model: object { id, speed } 

Model identifier and configuration.



id: "claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more or string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

"standard"

"fast"



multiagent: object { agents, type } 

Resolved coordinator topology with full agent definitions for each roster member.



agents: array of [BetaManagedAgentsSessionThreadAgent](api/beta/agents.md) { id, description, mcp\_servers, 7 more } 

Full `agent` definitions the coordinator may spawn as session threads.

id: string

description: string



mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md) { name, type, url } 

name: string



type: "url"

"url"

url: string



model: object { id, speed } 

Model identifier and configuration.



id: "claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more or string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

"standard"

"fast"

name: string



skills: array of [BetaManagedAgentsAnthropicSkill](api/beta/agents.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta/agents.md) { skill\_id, type, version } 



beta\_managed\_agents\_anthropic\_skill: object { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: string



type: "anthropic"

"anthropic"

version: string



beta\_managed\_agents\_custom\_skill: object { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: string



type: "custom"

"custom"

version: string

system: string



tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta/agents.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta/agents.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta/agents.md) { description, input\_schema, name, type } 



beta\_managed\_agents\_agent\_toolset20260401: object { configs, default\_config, type } 



configs: array of [BetaManagedAgentsAgentToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean



name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



default\_config: object { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



type: "agent\_toolset\_20260401"

"agent\_toolset\_20260401"



beta\_managed\_agents\_mcp\_toolset: object { configs, default\_config, mcp\_server\_name, type } 



configs: array of [BetaManagedAgentsMCPToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean

name: string



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



default\_config: object { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"

mcp\_server\_name: string



type: "mcp\_toolset"

"mcp\_toolset"



beta\_managed\_agents\_custom\_tool: object { description, input\_schema, name, type } 

A custom tool as returned in API responses.

description: string



input\_schema: object { type, properties, required } 

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string



type: "custom"

"custom"



type: "agent"

"agent"

version: number



type: "coordinator"

"coordinator"

name: string



skills: array of [BetaManagedAgentsAnthropicSkill](api/beta/agents.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta/agents.md) { skill\_id, type, version } 



beta\_managed\_agents\_anthropic\_skill: object { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: string



type: "anthropic"

"anthropic"

version: string



beta\_managed\_agents\_custom\_skill: object { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: string



type: "custom"

"custom"

version: string

system: string



tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta/agents.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta/agents.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta/agents.md) { description, input\_schema, name, type } 



beta\_managed\_agents\_agent\_toolset20260401: object { configs, default\_config, type } 



configs: array of [BetaManagedAgentsAgentToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean



name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



default\_config: object { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



type: "agent\_toolset\_20260401"

"agent\_toolset\_20260401"



beta\_managed\_agents\_mcp\_toolset: object { configs, default\_config, mcp\_server\_name, type } 



configs: array of [BetaManagedAgentsMCPToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean

name: string



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



default\_config: object { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"

mcp\_server\_name: string



type: "mcp\_toolset"

"mcp\_toolset"



beta\_managed\_agents\_custom\_tool: object { description, input\_schema, name, type } 

A custom tool as returned in API responses.

description: string



input\_schema: object { type, properties, required } 

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string



type: "custom"

"custom"



type: "agent"

"agent"

version: number



beta\_managed\_agents\_session\_agent\_update: object { mcp\_servers, tools } 

Mid-session agent configuration update. Only `tools` and `mcp_servers` are updatable. Full replacement: the provided array becomes the new value. To preserve existing entries, GET the session, modify the array, and POST it back.



mcp\_servers: optional array of [BetaManagedAgentsURLMCPServerParams](api/beta/agents.md) { name, type, url } 

Replacement MCP server list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

name: string

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.



type: "url"

"url"

url: string

Endpoint URL for the MCP server.



tools: optional array of [BetaManagedAgentsAgentToolset20260401Params](api/beta/agents.md) { type, configs, default\_config }  or [BetaManagedAgentsMCPToolsetParams](api/beta/agents.md) { mcp\_server\_name, type, configs, default\_config }  or [BetaManagedAgentsCustomToolParams](api/beta/agents.md) { description, input\_schema, name, type } 

Replacement tool list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.



beta\_managed\_agents\_agent\_toolset20260401\_params: object { type, configs, default\_config } 

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.



type: "agent\_toolset\_20260401"

"agent\_toolset\_20260401"



configs: optional array of [BetaManagedAgentsAgentToolConfigParams](api/beta/agents.md) { name, enabled, permission\_policy } 

Per-tool configuration overrides.



name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

enabled: optional boolean

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.



permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



default\_config: optional object { enabled, permission\_policy } 

Default configuration for all tools in a toolset.

enabled: optional boolean

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.



permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



beta\_managed\_agents\_mcp\_toolset\_params: object { mcp\_server\_name, type, configs, default\_config } 

Configuration for tools from an MCP server defined in `mcp_servers`.

mcp\_server\_name: string

Name of the MCP server. Must match a server name from the mcp\_servers array. 1-255 characters.



type: "mcp\_toolset"

"mcp\_toolset"



configs: optional array of [BetaManagedAgentsMCPToolConfigParams](api/beta/agents.md) { name, enabled, permission\_policy } 

Per-tool configuration overrides.

name: string

Name of the MCP tool to configure. 1-128 characters.

enabled: optional boolean

Whether this tool is enabled. Overrides the `default_config` setting.



permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



default\_config: optional object { enabled, permission\_policy } 

Default configuration for all tools from an MCP server.

enabled: optional boolean

Whether tools are enabled by default. Defaults to true if not specified.



permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



beta\_managed\_agents\_custom\_tool\_params: object { description, input\_schema, name, type } 

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

description: string

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.



input\_schema: object { type, properties, required } 

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.



type: "custom"

"custom"



beta\_managed\_agents\_session\_multiagent\_coordinator: object { agents, type } 

Resolved coordinator topology with full agent definitions for each roster member.



agents: array of [BetaManagedAgentsSessionThreadAgent](api/beta/agents.md) { id, description, mcp\_servers, 7 more } 

Full `agent` definitions the coordinator may spawn as session threads.

id: string

description: string



mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md) { name, type, url } 

name: string



type: "url"

"url"

url: string



model: object { id, speed } 

Model identifier and configuration.



id: "claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more or string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

"standard"

"fast"

name: string



skills: array of [BetaManagedAgentsAnthropicSkill](api/beta/agents.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta/agents.md) { skill\_id, type, version } 



beta\_managed\_agents\_anthropic\_skill: object { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: string



type: "anthropic"

"anthropic"

version: string



beta\_managed\_agents\_custom\_skill: object { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: string



type: "custom"

"custom"

version: string

system: string



tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta/agents.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta/agents.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta/agents.md) { description, input\_schema, name, type } 



beta\_managed\_agents\_agent\_toolset20260401: object { configs, default\_config, type } 



configs: array of [BetaManagedAgentsAgentToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean



name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



default\_config: object { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



type: "agent\_toolset\_20260401"

"agent\_toolset\_20260401"



beta\_managed\_agents\_mcp\_toolset: object { configs, default\_config, mcp\_server\_name, type } 



configs: array of [BetaManagedAgentsMCPToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean

name: string



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



default\_config: object { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"

mcp\_server\_name: string



type: "mcp\_toolset"

"mcp\_toolset"



beta\_managed\_agents\_custom\_tool: object { description, input\_schema, name, type } 

A custom tool as returned in API responses.

description: string



input\_schema: object { type, properties, required } 

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string



type: "custom"

"custom"



type: "agent"

"agent"

version: number



type: "coordinator"

"coordinator"



beta\_managed\_agents\_session\_stats: object { active\_seconds, duration\_seconds } 

Timing statistics for a session.

active\_seconds: optional number

Cumulative time in seconds the session spent in running status. Excludes idle time.

duration\_seconds: optional number

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.



beta\_managed\_agents\_session\_updated\_event: object { id, processed\_at, type, 3 more } 

Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format



type: "session.updated"

"session.updated"



agent: optional object { id, description, mcp\_servers, 8 more } 

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: string

description: string



mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md) { name, type, url } 

name: string



type: "url"

"url"

url: string



model: object { id, speed } 

Model identifier and configuration.



id: "claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more or string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

"standard"

"fast"



multiagent: object { agents, type } 

Resolved coordinator topology with full agent definitions for each roster member.



agents: array of [BetaManagedAgentsSessionThreadAgent](api/beta/agents.md) { id, description, mcp\_servers, 7 more } 

Full `agent` definitions the coordinator may spawn as session threads.

id: string

description: string



mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md) { name, type, url } 

name: string



type: "url"

"url"

url: string



model: object { id, speed } 

Model identifier and configuration.



id: "claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more or string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

"standard"

"fast"

name: string



skills: array of [BetaManagedAgentsAnthropicSkill](api/beta/agents.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta/agents.md) { skill\_id, type, version } 



beta\_managed\_agents\_anthropic\_skill: object { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: string



type: "anthropic"

"anthropic"

version: string



beta\_managed\_agents\_custom\_skill: object { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: string



type: "custom"

"custom"

version: string

system: string



tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta/agents.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta/agents.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta/agents.md) { description, input\_schema, name, type } 



beta\_managed\_agents\_agent\_toolset20260401: object { configs, default\_config, type } 



configs: array of [BetaManagedAgentsAgentToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean



name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



default\_config: object { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



type: "agent\_toolset\_20260401"

"agent\_toolset\_20260401"



beta\_managed\_agents\_mcp\_toolset: object { configs, default\_config, mcp\_server\_name, type } 



configs: array of [BetaManagedAgentsMCPToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean

name: string



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



default\_config: object { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"

mcp\_server\_name: string



type: "mcp\_toolset"

"mcp\_toolset"



beta\_managed\_agents\_custom\_tool: object { description, input\_schema, name, type } 

A custom tool as returned in API responses.

description: string



input\_schema: object { type, properties, required } 

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string



type: "custom"

"custom"



type: "agent"

"agent"

version: number



type: "coordinator"

"coordinator"

name: string



skills: array of [BetaManagedAgentsAnthropicSkill](api/beta/agents.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta/agents.md) { skill\_id, type, version } 



beta\_managed\_agents\_anthropic\_skill: object { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: string



type: "anthropic"

"anthropic"

version: string



beta\_managed\_agents\_custom\_skill: object { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: string



type: "custom"

"custom"

version: string

system: string



tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta/agents.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta/agents.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta/agents.md) { description, input\_schema, name, type } 



beta\_managed\_agents\_agent\_toolset20260401: object { configs, default\_config, type } 



configs: array of [BetaManagedAgentsAgentToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean



name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



default\_config: object { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



type: "agent\_toolset\_20260401"

"agent\_toolset\_20260401"



beta\_managed\_agents\_mcp\_toolset: object { configs, default\_config, mcp\_server\_name, type } 



configs: array of [BetaManagedAgentsMCPToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean

name: string



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"



default\_config: object { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.



beta\_managed\_agents\_always\_allow\_policy: object { type } 

Tool calls are automatically approved without user confirmation.



type: "always\_allow"

"always\_allow"



beta\_managed\_agents\_always\_ask\_policy: object { type } 

Tool calls require user confirmation before execution.



type: "always\_ask"

"always\_ask"

mcp\_server\_name: string



type: "mcp\_toolset"

"mcp\_toolset"



beta\_managed\_agents\_custom\_tool: object { description, input\_schema, name, type } 

A custom tool as returned in API responses.

description: string



input\_schema: object { type, properties, required } 

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string



type: "custom"

"custom"



type: "agent"

"agent"

version: number

metadata: optional map[string]

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

title: optional string

The session's new title. Present only when the update changed it.



beta\_managed\_agents\_session\_usage: object { cache\_creation, cache\_read\_input\_tokens, input\_tokens, output\_tokens } 

Cumulative token usage for a session across all turns.



cache\_creation: optional object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: optional number

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: optional number

Tokens used to create 5-minute ephemeral cache entries.

cache\_read\_input\_tokens: optional number

Total tokens read from prompt cache.

input\_tokens: optional number

Total input tokens consumed across all turns.

output\_tokens: optional number

Total output tokens generated across all turns.



beta\_managed\_agents\_system\_content\_block: object { text, type } 

Regular text content.

text: string

The text content.



type: "text"

"text"



beta\_managed\_agents\_system\_message\_event: object { id, content, type, processed\_at } 

A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

id: string

Unique identifier for this event.



content: array of [BetaManagedAgentsSystemContentBlock](api/beta/sessions.md) { text, type } 

System content blocks. Text-only.

text: string

The text content.



type: "text"

"text"



type: "system.message"

"system.message"

processed\_at: optional string

A timestamp in RFC 3339 format



beta\_managed\_agents\_user\_tool\_result\_event: object { id, tool\_use\_id, type, 4 more } 

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

id: string

Unique identifier for this event.

tool\_use\_id: string

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.



type: "user.tool\_result"

"user.tool\_result"



content: optional array of [BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta/sessions/events.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta/sessions/events.md) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](api/beta/sessions/events.md) { citations, content, source, 2 more } 

The result content returned by the tool.



beta\_managed\_agents\_text\_block: object { text, type } 

Regular text content.

text: string

The text content.



type: "text"

"text"



beta\_managed\_agents\_image\_block: object { source, type } 

Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for image source variants.



beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type } 

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").



type: "base64"

"base64"



beta\_managed\_agents\_url\_image\_source: object { type, url } 

Image referenced by URL.



type: "url"

"url"

url: string

URL of the image to fetch.



beta\_managed\_agents\_file\_image\_source: object { file\_id, type } 

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "image"

"image"



beta\_managed\_agents\_document\_block: object { source, type, context, title } 

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for document source variants.



beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type } 

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").



type: "base64"

"base64"



beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type } 

Plain text document content.

data: string

The plain text content.



media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"



type: "text"

"text"



beta\_managed\_agents\_url\_document\_source: object { type, url } 

Document referenced by URL.



type: "url"

"url"

url: string

URL of the document to fetch.



beta\_managed\_agents\_file\_document\_source: object { file\_id, type } 

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.



type: "file"

"file"



type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.



beta\_managed\_agents\_search\_result\_block: object { citations, content, source, 2 more } 

A block containing a web search result.



citations: object { enabled } 

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.



content: array of [BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md) { text, type } 

Array of text content blocks from the search result.

text: string

The text content.



type: "text"

"text"

source: string

The URL source of the search result.

title: string

The title of the search result.



type: "search\_result"

"search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

#### SessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

$ ant beta:sessions:events list

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

$ ant beta:sessions:events send

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

$ ant beta:sessions:events stream

GET/v1/sessions/{session\_id}/events/stream

#### SessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

$ ant beta:sessions:resources add

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

$ ant beta:sessions:resources list

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

$ ant beta:sessions:resources retrieve

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

$ ant beta:sessions:resources update

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

$ ant beta:sessions:resources delete

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

#### SessionsThreads

##### [List Session Threads](api/beta/sessions/threads/list.md)

$ ant beta:sessions:threads list

GET/v1/sessions/{session\_id}/threads

##### [Get Session Thread](api/beta/sessions/threads/retrieve.md)

$ ant beta:sessions:threads retrieve

GET/v1/sessions/{session\_id}/threads/{thread\_id}

##### [Archive Session Thread](api/beta/sessions/threads/archive.md)

$ ant beta:sessions:threads archive

POST/v1/sessions/{session\_id}/threads/{thread\_id}/archive

#### SessionsThreadsEvents

##### [List Session Thread Events](api/beta/sessions/threads/events/list.md)

$ ant beta:sessions:threads:events list

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/beta/sessions/threads/events/stream.md)

$ ant beta:sessions:threads:events stream

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

---

*Copyright © Anthropic. All rights reserved.*
