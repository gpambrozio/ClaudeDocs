# Sessions

Copy page



cURL

# Sessions

##### [Create Session](api/beta/sessions/create.md)

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

POST/v1/sessions/{session\_id}/archive

##### ModelsExpand Collapse



BetaManagedAgentsAgentMessagePreview object { id, type } 

id: string

The id the buffered agent.message will carry if it is emitted. Matches the event\_id on this preview's event\_delta events.

type: "agent.message"



BetaManagedAgentsAgentParams object { id, type, version } 

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: string

The `agent` ID.

type: "agent"

version: optional number

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.



BetaManagedAgentsAgentThinkingPreview object { id, type } 

id: string

The id the buffered agent.thinking will carry if it is emitted. Start-only — no event\_delta events follow.

type: "agent.thinking"



BetaManagedAgentsAgentWithOverridesParams object { id, type, mcp\_servers, 5 more } 

Reference to an `agent` plus optional configuration overrides. Each provided field replaces the agent's value for the caller's use; the agent resource is unchanged.

id: string

The `agent` ID.

type: "agent\_with\_overrides"



mcp\_servers: optional array of [BetaManagedAgentsURLMCPServerParams](api/beta/agents.md) { name, type, url } 

Replacement MCP server list. Full replacement: the provided array becomes the MCP servers. Send an empty array to clear; omit to preserve the agent's servers.

name: string

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

type: "url"

url: string

Endpoint URL for the MCP server.



model: optional [BetaManagedAgentsModel](api/beta/agents.md) or [BetaManagedAgentsModelConfigParams](api/beta/agents.md) { id, speed } 

Replacement model. Accepts the model string, e.g. `claude-opus-4-6`, or a `model_config` object. Omit to use the agent's model.

One of the following:



BetaManagedAgentsModel = "claude-sonnet-5" or "claude-fable-5" or "claude-opus-4-8" or 9 more or string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-opus-4-8" or 9 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"

High-performance model for coding and agents

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

string



BetaManagedAgentsModelConfigParams object { id, speed } 

An object that defines additional configuration control over model use



id: [BetaManagedAgentsModel](api/beta/agents.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-opus-4-8" or 9 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"

High-performance model for coding and agents

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

string



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"



skills: optional array of [BetaManagedAgentsSkillParams](api/beta/agents.md)

Replacement skill list. Full replacement: the provided array becomes the skills. Send an empty array to clear; omit to preserve the agent's skills.

One of the following:



BetaManagedAgentsAnthropicSkillParams object { skill\_id, type, version } 

An Anthropic-managed skill.

skill\_id: string

Identifier of the Anthropic skill (e.g., "xlsx").

type: "anthropic"

version: optional string

Version to pin. Defaults to latest if omitted.



BetaManagedAgentsCustomSkillParams object { skill\_id, type, version } 

A user-created custom skill.

skill\_id: string

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

type: "custom"

version: optional string

Version to pin. Defaults to latest if omitted.

system: optional string

Replacement system prompt. Up to 100,000 characters. Set to null to clear the agent's system prompt; omit to preserve it.



tools: optional array of [BetaManagedAgentsAgentToolset20260401Params](api/beta/agents.md) { type, configs, default\_config }  or [BetaManagedAgentsMCPToolsetParams](api/beta/agents.md) { mcp\_server\_name, type, configs, default\_config }  or [BetaManagedAgentsCustomToolParams](api/beta/agents.md) { description, input\_schema, name, type } 

Replacement tool list. Full replacement: the provided array becomes the tool configuration. Send an empty array to clear; omit to preserve the agent's tools.

One of the following:



BetaManagedAgentsAgentToolset20260401Params object { type, configs, default\_config } 

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

type: "agent\_toolset\_20260401"



configs: optional array of [BetaManagedAgentsAgentToolConfigParams](api/beta/agents.md) { name, enabled, permission\_policy } 

Per-tool configuration overrides.



name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

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

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"



default\_config: optional [BetaManagedAgentsAgentToolsetDefaultConfigParams](api/beta/agents.md) { enabled, permission\_policy } 

Default configuration for all tools in a toolset.

enabled: optional boolean

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.



permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"



BetaManagedAgentsMCPToolsetParams object { mcp\_server\_name, type, configs, default\_config } 

Configuration for tools from an MCP server defined in `mcp_servers`.

mcp\_server\_name: string

Name of the MCP server. Must match a server name from the mcp\_servers array. 1-255 characters.

type: "mcp\_toolset"

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

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"



default\_config: optional [BetaManagedAgentsMCPToolsetDefaultConfigParams](api/beta/agents.md) { enabled, permission\_policy } 

Default configuration for all tools from an MCP server.

enabled: optional boolean

Whether tools are enabled by default. Defaults to true if not specified.



permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"



BetaManagedAgentsCustomToolParams object { description, input\_schema, name, type } 

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

description: string

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) { type, properties, required } 

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

type: "custom"

version: optional number

The specific `agent` version to use. Omit to use the latest version.



BetaManagedAgentsBranchCheckout object { name, type } 

name: string

Branch name to check out.

type: "branch"



BetaManagedAgentsCacheCreationUsage object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: optional number

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: optional number

Tokens used to create 5-minute ephemeral cache entries.



BetaManagedAgentsCommitCheckout object { sha, type } 

sha: string

Full commit SHA to check out.

type: "commit"



BetaManagedAgentsDeletedSession object { id, type } 

Confirmation that a `session` has been permanently deleted.

id: string

type: "session\_deleted"



BetaManagedAgentsDeltaContent object { content, type, index } 



content: [BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type } 

Regular text content.

text: string

The text content.

type: "text"

type: "content\_delta"

index: optional number

Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.



BetaManagedAgentsDeltaEvent object { delta, event\_id, type } 

An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event\_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model\_request\_end closes the preview. Only sent on stream connections that opt in via event\_deltas; never appears in event history.



delta: [BetaManagedAgentsDeltaContent](api/beta/sessions.md) { content, type, index } 

One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content\_delta fragments, each a partial element of the content array.



content: [BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type } 

Regular text content.

text: string

The text content.

type: "text"

type: "content\_delta"

index: optional number

Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

event\_id: string

The id of the event being previewed. Matches event.id on the corresponding event\_start and the buffered event that reconciles the preview.

type: "event\_delta"



BetaManagedAgentsDeltaType = "agent.message" or "agent.thinking"

EventDeltaType enum

One of the following:

"agent.message"

"agent.thinking"



BetaManagedAgentsFileResourceParams object { file\_id, type, mount\_path } 

Mount a file uploaded via the Files API into the session.

file\_id: string

ID of a previously uploaded file.

type: "file"

mount\_path: optional string

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.



BetaManagedAgentsGitHubRepositoryResourceParams object { authorization\_token, type, url, 2 more } 

Mount a GitHub repository into the session's container.

authorization\_token: string

GitHub authorization token used to clone the repository.

type: "github\_repository"

url: string

Github URL of the repository



checkout: optional [BetaManagedAgentsBranchCheckout](api/beta/sessions.md) { name, type }  or [BetaManagedAgentsCommitCheckout](api/beta/sessions.md) { sha, type } 

Branch or commit to check out. Defaults to the repository's default branch.

One of the following:



BetaManagedAgentsBranchCheckout object { name, type } 

name: string

Branch name to check out.

type: "branch"



BetaManagedAgentsCommitCheckout object { sha, type } 

sha: string

Full commit SHA to check out.

type: "commit"

mount\_path: optional string

Mount path in the container. Defaults to `/workspace/<repo-name>`.



BetaManagedAgentsMemoryStoreResourceParam object { memory\_store\_id, type, access, instructions } 

Parameters for attaching a memory store to an agent session.

memory\_store\_id: string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: "memory\_store"



access: optional "read\_write" or "read\_only"

Access mode for an attached memory store.

One of the following:

"read\_write"

"read\_only"

instructions: optional string

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.



BetaManagedAgentsMultiagent object { agents, type } 

Resolved coordinator topology with a concrete agent roster.



agents: array of [BetaManagedAgentsAgentReference](api/beta/agents.md) { id, type, version } 

Agents the coordinator may spawn as session threads, each resolved to a specific version.

id: string

type: "agent"

version: number

type: "coordinator"



BetaManagedAgentsMultiagentParams object { agents, type } 

A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.



agents: array of [BetaManagedAgentsMultiagentRosterEntryParams](api/beta/sessions.md)

Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

One of the following:

string



BetaManagedAgentsAgentParams object { id, type, version } 

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: string

The `agent` ID.

type: "agent"

version: optional number

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.



BetaManagedAgentsMultiagentSelfParams object { type } 

Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

type: "self"

type: "coordinator"



BetaManagedAgentsMultiagentRosterEntryParams = string or [BetaManagedAgentsAgentParams](api/beta/sessions.md) { id, type, version }  or [BetaManagedAgentsMultiagentSelfParams](api/beta/agents.md) { type } 

An entry in a multiagent roster: an agent ID string, a versioned agent reference, or `self`.

One of the following:

string



BetaManagedAgentsAgentParams object { id, type, version } 

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: string

The `agent` ID.

type: "agent"

version: optional number

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.



BetaManagedAgentsMultiagentSelfParams object { type } 

Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

type: "self"



BetaManagedAgentsOutcomeEvaluationResource object { completed\_at, description, explanation, 4 more } 

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

type: "outcome\_evaluation"



BetaManagedAgentsSession object { id, agent, archived\_at, 13 more } 

A Managed Agents `session`.

id: string



agent: [BetaManagedAgentsSessionAgent](api/beta/sessions.md) { id, description, mcp\_servers, 8 more } 

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: string

description: string



mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md) { name, type, url } 

name: string

type: "url"

url: string



model: [BetaManagedAgentsModelConfig](api/beta/agents.md) { id, speed } 

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta/agents.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-opus-4-8" or 9 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"

High-performance model for coding and agents

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

string



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"



multiagent: [BetaManagedAgentsSessionMultiagentCoordinator](api/beta/sessions.md) { agents, type } 

Resolved coordinator topology with full agent definitions for each roster member.



agents: array of [BetaManagedAgentsSessionThreadAgent](api/beta/agents.md) { id, description, mcp\_servers, 7 more } 

Full `agent` definitions the coordinator may spawn as session threads.

id: string

description: string



mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md) { name, type, url } 

name: string

type: "url"

url: string



model: [BetaManagedAgentsModelConfig](api/beta/agents.md) { id, speed } 

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta/agents.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-opus-4-8" or 9 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"

High-performance model for coding and agents

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

string



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

name: string



skills: array of [BetaManagedAgentsAnthropicSkill](api/beta/agents.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta/agents.md) { skill\_id, type, version } 

One of the following:



BetaManagedAgentsAnthropicSkill object { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string



BetaManagedAgentsCustomSkill object { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string



tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta/agents.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta/agents.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta/agents.md) { description, input\_schema, name, type } 

One of the following:



BetaManagedAgentsAgentToolset20260401 object { configs, default\_config, type } 



configs: array of [BetaManagedAgentsAgentToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean



name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

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

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"



BetaManagedAgentsMCPToolset object { configs, default\_config, mcp\_server\_name, type } 



configs: array of [BetaManagedAgentsMCPToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean

name: string



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta/agents.md) { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"



BetaManagedAgentsCustomTool object { description, input\_schema, name, type } 

A custom tool as returned in API responses.

description: string



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) { type, properties, required } 

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string

type: "custom"

type: "agent"

version: number

type: "coordinator"

name: string



skills: array of [BetaManagedAgentsAnthropicSkill](api/beta/agents.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta/agents.md) { skill\_id, type, version } 

One of the following:



BetaManagedAgentsAnthropicSkill object { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string



BetaManagedAgentsCustomSkill object { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string



tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta/agents.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta/agents.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta/agents.md) { description, input\_schema, name, type } 

One of the following:



BetaManagedAgentsAgentToolset20260401 object { configs, default\_config, type } 



configs: array of [BetaManagedAgentsAgentToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean



name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

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

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"



BetaManagedAgentsMCPToolset object { configs, default\_config, mcp\_server\_name, type } 



configs: array of [BetaManagedAgentsMCPToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean

name: string



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta/agents.md) { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"



BetaManagedAgentsCustomTool object { description, input\_schema, name, type } 

A custom tool as returned in API responses.

description: string



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) { type, properties, required } 

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string

type: "custom"

type: "agent"

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

type: "outcome\_evaluation"



resources: array of [BetaManagedAgentsSessionResource](api/beta/sessions/resources.md)

One of the following:



BetaManagedAgentsGitHubRepositoryResource object { id, created\_at, mount\_path, 4 more } 

id: string

created\_at: string

A timestamp in RFC 3339 format

mount\_path: string

type: "github\_repository"

updated\_at: string

A timestamp in RFC 3339 format

url: string



checkout: optional [BetaManagedAgentsBranchCheckout](api/beta/sessions.md) { name, type }  or [BetaManagedAgentsCommitCheckout](api/beta/sessions.md) { sha, type } 

One of the following:



BetaManagedAgentsBranchCheckout object { name, type } 

name: string

Branch name to check out.

type: "branch"



BetaManagedAgentsCommitCheckout object { sha, type } 

sha: string

Full commit SHA to check out.

type: "commit"



BetaManagedAgentsFileResource object { id, created\_at, file\_id, 3 more } 

id: string

created\_at: string

A timestamp in RFC 3339 format

file\_id: string

mount\_path: string

type: "file"

updated\_at: string

A timestamp in RFC 3339 format



BetaManagedAgentsMemoryStoreResource object { memory\_store\_id, type, access, 4 more } 

A memory store attached to an agent session.

memory\_store\_id: string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: "memory\_store"



access: optional "read\_write" or "read\_only"

Access mode for an attached memory store.

One of the following:

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

stats: [BetaManagedAgentsSessionStats](api/beta/sessions.md) { active\_seconds, duration\_seconds } 

Timing statistics for a session.

active\_seconds: optional number

Cumulative time in seconds the session spent in running status. Excludes idle time.

duration\_seconds: optional number

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.



status: "rescheduling" or "running" or "idle" or "terminated"

SessionStatus enum

One of the following:

"rescheduling"

"running"

"idle"

"terminated"

title: string

type: "session"

updated\_at: string

A timestamp in RFC 3339 format



usage: [BetaManagedAgentsSessionUsage](api/beta/sessions.md) { cache\_creation, cache\_read\_input\_tokens, input\_tokens, output\_tokens } 

Cumulative token usage for a session across all turns.



cache\_creation: optional [BetaManagedAgentsCacheCreationUsage](api/beta/sessions.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

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

BetaManagedAgentsSessionAgent object { id, description, mcp\_servers, 8 more } 

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: string

description: string



mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md) { name, type, url } 

name: string

type: "url"

url: string



model: [BetaManagedAgentsModelConfig](api/beta/agents.md) { id, speed } 

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta/agents.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-opus-4-8" or 9 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"

High-performance model for coding and agents

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

string



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"



multiagent: [BetaManagedAgentsSessionMultiagentCoordinator](api/beta/sessions.md) { agents, type } 

Resolved coordinator topology with full agent definitions for each roster member.



agents: array of [BetaManagedAgentsSessionThreadAgent](api/beta/agents.md) { id, description, mcp\_servers, 7 more } 

Full `agent` definitions the coordinator may spawn as session threads.

id: string

description: string



mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md) { name, type, url } 

name: string

type: "url"

url: string



model: [BetaManagedAgentsModelConfig](api/beta/agents.md) { id, speed } 

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta/agents.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-opus-4-8" or 9 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"

High-performance model for coding and agents

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

string



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

name: string



skills: array of [BetaManagedAgentsAnthropicSkill](api/beta/agents.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta/agents.md) { skill\_id, type, version } 

One of the following:



BetaManagedAgentsAnthropicSkill object { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string



BetaManagedAgentsCustomSkill object { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string



tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta/agents.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta/agents.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta/agents.md) { description, input\_schema, name, type } 

One of the following:



BetaManagedAgentsAgentToolset20260401 object { configs, default\_config, type } 



configs: array of [BetaManagedAgentsAgentToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean



name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

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

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"



BetaManagedAgentsMCPToolset object { configs, default\_config, mcp\_server\_name, type } 



configs: array of [BetaManagedAgentsMCPToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean

name: string



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta/agents.md) { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"



BetaManagedAgentsCustomTool object { description, input\_schema, name, type } 

A custom tool as returned in API responses.

description: string



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) { type, properties, required } 

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string

type: "custom"

type: "agent"

version: number

type: "coordinator"

name: string



skills: array of [BetaManagedAgentsAnthropicSkill](api/beta/agents.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta/agents.md) { skill\_id, type, version } 

One of the following:



BetaManagedAgentsAnthropicSkill object { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string



BetaManagedAgentsCustomSkill object { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string



tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta/agents.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta/agents.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta/agents.md) { description, input\_schema, name, type } 

One of the following:



BetaManagedAgentsAgentToolset20260401 object { configs, default\_config, type } 



configs: array of [BetaManagedAgentsAgentToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean



name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

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

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"



BetaManagedAgentsMCPToolset object { configs, default\_config, mcp\_server\_name, type } 



configs: array of [BetaManagedAgentsMCPToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean

name: string



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta/agents.md) { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"



BetaManagedAgentsCustomTool object { description, input\_schema, name, type } 

A custom tool as returned in API responses.

description: string



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) { type, properties, required } 

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string

type: "custom"

type: "agent"

version: number



BetaManagedAgentsSessionAgentUpdate object { mcp\_servers, tools } 

Mid-session agent configuration update. Only `tools` and `mcp_servers` are updatable. Full replacement: the provided array becomes the new value. To preserve existing entries, GET the session, modify the array, and POST it back.



mcp\_servers: optional array of [BetaManagedAgentsURLMCPServerParams](api/beta/agents.md) { name, type, url } 

Replacement MCP server list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

name: string

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

type: "url"

url: string

Endpoint URL for the MCP server.



tools: optional array of [BetaManagedAgentsAgentToolset20260401Params](api/beta/agents.md) { type, configs, default\_config }  or [BetaManagedAgentsMCPToolsetParams](api/beta/agents.md) { mcp\_server\_name, type, configs, default\_config }  or [BetaManagedAgentsCustomToolParams](api/beta/agents.md) { description, input\_schema, name, type } 

Replacement tool list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

One of the following:



BetaManagedAgentsAgentToolset20260401Params object { type, configs, default\_config } 

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

type: "agent\_toolset\_20260401"



configs: optional array of [BetaManagedAgentsAgentToolConfigParams](api/beta/agents.md) { name, enabled, permission\_policy } 

Per-tool configuration overrides.



name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

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

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"



default\_config: optional [BetaManagedAgentsAgentToolsetDefaultConfigParams](api/beta/agents.md) { enabled, permission\_policy } 

Default configuration for all tools in a toolset.

enabled: optional boolean

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.



permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"



BetaManagedAgentsMCPToolsetParams object { mcp\_server\_name, type, configs, default\_config } 

Configuration for tools from an MCP server defined in `mcp_servers`.

mcp\_server\_name: string

Name of the MCP server. Must match a server name from the mcp\_servers array. 1-255 characters.

type: "mcp\_toolset"

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

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"



default\_config: optional [BetaManagedAgentsMCPToolsetDefaultConfigParams](api/beta/agents.md) { enabled, permission\_policy } 

Default configuration for all tools from an MCP server.

enabled: optional boolean

Whether tools are enabled by default. Defaults to true if not specified.



permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"



BetaManagedAgentsCustomToolParams object { description, input\_schema, name, type } 

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

description: string

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) { type, properties, required } 

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

type: "custom"



BetaManagedAgentsSessionMultiagentCoordinator object { agents, type } 

Resolved coordinator topology with full agent definitions for each roster member.



agents: array of [BetaManagedAgentsSessionThreadAgent](api/beta/agents.md) { id, description, mcp\_servers, 7 more } 

Full `agent` definitions the coordinator may spawn as session threads.

id: string

description: string



mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md) { name, type, url } 

name: string

type: "url"

url: string



model: [BetaManagedAgentsModelConfig](api/beta/agents.md) { id, speed } 

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta/agents.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-opus-4-8" or 9 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"

High-performance model for coding and agents

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

string



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

name: string



skills: array of [BetaManagedAgentsAnthropicSkill](api/beta/agents.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta/agents.md) { skill\_id, type, version } 

One of the following:



BetaManagedAgentsAnthropicSkill object { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string



BetaManagedAgentsCustomSkill object { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string



tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta/agents.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta/agents.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta/agents.md) { description, input\_schema, name, type } 

One of the following:



BetaManagedAgentsAgentToolset20260401 object { configs, default\_config, type } 



configs: array of [BetaManagedAgentsAgentToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean



name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

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

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"



BetaManagedAgentsMCPToolset object { configs, default\_config, mcp\_server\_name, type } 



configs: array of [BetaManagedAgentsMCPToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean

name: string



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta/agents.md) { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"



BetaManagedAgentsCustomTool object { description, input\_schema, name, type } 

A custom tool as returned in API responses.

description: string



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) { type, properties, required } 

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string

type: "custom"

type: "agent"

version: number

type: "coordinator"



BetaManagedAgentsSessionStats object { active\_seconds, duration\_seconds } 

Timing statistics for a session.

active\_seconds: optional number

Cumulative time in seconds the session spent in running status. Excludes idle time.

duration\_seconds: optional number

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.



BetaManagedAgentsSessionUpdatedEvent object { id, processed\_at, type, 3 more } 

Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.updated"



agent: optional [BetaManagedAgentsSessionAgent](api/beta/sessions.md) { id, description, mcp\_servers, 8 more } 

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: string

description: string



mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md) { name, type, url } 

name: string

type: "url"

url: string



model: [BetaManagedAgentsModelConfig](api/beta/agents.md) { id, speed } 

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta/agents.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-opus-4-8" or 9 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"

High-performance model for coding and agents

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

string



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"



multiagent: [BetaManagedAgentsSessionMultiagentCoordinator](api/beta/sessions.md) { agents, type } 

Resolved coordinator topology with full agent definitions for each roster member.



agents: array of [BetaManagedAgentsSessionThreadAgent](api/beta/agents.md) { id, description, mcp\_servers, 7 more } 

Full `agent` definitions the coordinator may spawn as session threads.

id: string

description: string



mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md) { name, type, url } 

name: string

type: "url"

url: string



model: [BetaManagedAgentsModelConfig](api/beta/agents.md) { id, speed } 

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta/agents.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-opus-4-8" or 9 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"

High-performance model for coding and agents

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

string



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

name: string



skills: array of [BetaManagedAgentsAnthropicSkill](api/beta/agents.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta/agents.md) { skill\_id, type, version } 

One of the following:



BetaManagedAgentsAnthropicSkill object { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string



BetaManagedAgentsCustomSkill object { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string



tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta/agents.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta/agents.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta/agents.md) { description, input\_schema, name, type } 

One of the following:



BetaManagedAgentsAgentToolset20260401 object { configs, default\_config, type } 



configs: array of [BetaManagedAgentsAgentToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean



name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

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

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"



BetaManagedAgentsMCPToolset object { configs, default\_config, mcp\_server\_name, type } 



configs: array of [BetaManagedAgentsMCPToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean

name: string



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta/agents.md) { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"



BetaManagedAgentsCustomTool object { description, input\_schema, name, type } 

A custom tool as returned in API responses.

description: string



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) { type, properties, required } 

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string

type: "custom"

type: "agent"

version: number

type: "coordinator"

name: string



skills: array of [BetaManagedAgentsAnthropicSkill](api/beta/agents.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta/agents.md) { skill\_id, type, version } 

One of the following:



BetaManagedAgentsAnthropicSkill object { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string



BetaManagedAgentsCustomSkill object { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string



tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta/agents.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta/agents.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta/agents.md) { description, input\_schema, name, type } 

One of the following:



BetaManagedAgentsAgentToolset20260401 object { configs, default\_config, type } 



configs: array of [BetaManagedAgentsAgentToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean



name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

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

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"



BetaManagedAgentsMCPToolset object { configs, default\_config, mcp\_server\_name, type } 



configs: array of [BetaManagedAgentsMCPToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean

name: string



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta/agents.md) { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"



BetaManagedAgentsCustomTool object { description, input\_schema, name, type } 

A custom tool as returned in API responses.

description: string



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) { type, properties, required } 

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string

type: "custom"

type: "agent"

version: number

metadata: optional map[string]

The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

title: optional string

The session's new title. Present only when the update changed it.



BetaManagedAgentsSessionUsage object { cache\_creation, cache\_read\_input\_tokens, input\_tokens, output\_tokens } 

Cumulative token usage for a session across all turns.



cache\_creation: optional [BetaManagedAgentsCacheCreationUsage](api/beta/sessions.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

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

BetaManagedAgentsStartEvent object { event, type } 

Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event\_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model\_request\_end closes the preview. Only sent on stream connections that opt in via event\_deltas; never appears in event history.



event: [BetaManagedAgentsStartEventPreview](api/beta/sessions.md)

The previewed event's type and id. The event type determines which delta types the preview's event\_delta events carry: agent.message events stream content\_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

One of the following:



BetaManagedAgentsAgentMessagePreview object { id, type } 

id: string

The id the buffered agent.message will carry if it is emitted. Matches the event\_id on this preview's event\_delta events.

type: "agent.message"



BetaManagedAgentsAgentThinkingPreview object { id, type } 

id: string

The id the buffered agent.thinking will carry if it is emitted. Start-only — no event\_delta events follow.

type: "agent.thinking"

type: "event\_start"



BetaManagedAgentsStartEventPreview = [BetaManagedAgentsAgentMessagePreview](api/beta/sessions.md) { id, type }  or [BetaManagedAgentsAgentThinkingPreview](api/beta/sessions.md) { id, type } 

One of the following:



BetaManagedAgentsAgentMessagePreview object { id, type } 

id: string

The id the buffered agent.message will carry if it is emitted. Matches the event\_id on this preview's event\_delta events.

type: "agent.message"



BetaManagedAgentsAgentThinkingPreview object { id, type } 

id: string

The id the buffered agent.thinking will carry if it is emitted. Start-only — no event\_delta events follow.

type: "agent.thinking"



BetaManagedAgentsSystemContentBlock object { text, type } 

Regular text content.

text: string

The text content.

type: "text"



BetaManagedAgentsSystemMessageEvent object { id, content, type, processed\_at } 

A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

id: string

Unique identifier for this event.



content: array of [BetaManagedAgentsSystemContentBlock](api/beta/sessions.md) { text, type } 

System content blocks. Text-only.

text: string

The text content.

type: "text"

type: "system.message"

processed\_at: optional string

A timestamp in RFC 3339 format



BetaManagedAgentsUserToolResultEvent object { id, tool\_use\_id, type, 4 more } 

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

id: string

Unique identifier for this event.

tool\_use\_id: string

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.tool\_result"



content: optional array of [BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta/sessions/events.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta/sessions/events.md) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](api/beta/sessions/events.md) { citations, content, source, 2 more } 

The result content returned by the tool.

One of the following:



BetaManagedAgentsTextBlock object { text, type } 

Regular text content.

text: string

The text content.

type: "text"



BetaManagedAgentsImageBlock object { source, type } 

Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for image source variants.

One of the following:



BetaManagedAgentsBase64ImageSource object { data, media\_type, type } 

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"



BetaManagedAgentsURLImageSource object { type, url } 

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.



BetaManagedAgentsFileImageSource object { file\_id, type } 

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"



BetaManagedAgentsDocumentBlock object { source, type, context, title } 

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta/sessions/events.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for document source variants.

One of the following:



BetaManagedAgentsBase64DocumentSource object { data, media\_type, type } 

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"



BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type } 

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"



BetaManagedAgentsURLDocumentSource object { type, url } 

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.



BetaManagedAgentsFileDocumentSource object { file\_id, type } 

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.



BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more } 

A block containing a web search result.



citations: [BetaManagedAgentsSearchResultCitations](api/beta/sessions/events.md) { enabled } 

Citation settings for a search result.

enabled: boolean

Whether citations are enabled for this search result.



content: array of [BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md) { text, type } 

Array of text content blocks from the search result.

text: string

The text content.

type: "text"

source: string

The URL source of the search result.

title: string

The title of the search result.

type: "search\_result"

is\_error: optional boolean

Whether the tool execution resulted in an error.

processed\_at: optional string

A timestamp in RFC 3339 format

session\_thread\_id: optional string

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

#### SessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

GET/v1/sessions/{session\_id}/events/stream

#### SessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

#### SessionsThreads

##### [List Session Threads](api/beta/sessions/threads/list.md)

GET/v1/sessions/{session\_id}/threads

##### [Get Session Thread](api/beta/sessions/threads/retrieve.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}

##### [Archive Session Thread](api/beta/sessions/threads/archive.md)

POST/v1/sessions/{session\_id}/threads/{thread\_id}/archive

#### SessionsThreadsEvents

##### [List Session Thread Events](api/beta/sessions/threads/events/list.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/beta/sessions/threads/events/stream.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

---

*Copyright © Anthropic. All rights reserved.*
