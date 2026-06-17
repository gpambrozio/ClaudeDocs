# Agents

Copy page



PHP

# Agents

##### [Create Agent](api/beta/agents/create.md)

$client->beta->agents->create([Model](api/beta/agents/create.md) model, string name, ?string description, ?list<[BetaManagedAgentsURLMCPServerParams](api/beta.md)> mcpServers, ?array<string,string> metadata, ?[BetaManagedAgentsMultiagentParams](api/beta.md) multiagent, ?list<[BetaManagedAgentsSkillParams](api/beta.md)> skills, ?string system, ?list<Tool> tools, ?list<AnthropicBeta> betas): [BetaManagedAgentsAgent](api/beta.md)

POST/v1/agents

##### [List Agents](api/beta/agents/list.md)

$client->beta->agents->list(?\Datetime createdAtGte, ?\Datetime createdAtLte, ?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[BetaManagedAgentsAgent](api/beta.md)>

GET/v1/agents

##### [Get Agent](api/beta/agents/retrieve.md)

$client->beta->agents->retrieve(string agentID, ?int version, ?list<AnthropicBeta> betas): [BetaManagedAgentsAgent](api/beta.md)

GET/v1/agents/{agent\_id}

##### [Update Agent](api/beta/agents/update.md)

$client->beta->agents->update(string agentID, int version, ?string description, ?list<[BetaManagedAgentsURLMCPServerParams](api/beta.md)> mcpServers, ?array<string,string> metadata, ?[Model](api/beta/agents/update.md) model, ?[BetaManagedAgentsMultiagentParams](api/beta.md) multiagent, ?string name, ?list<[BetaManagedAgentsSkillParams](api/beta.md)> skills, ?string system, ?list<Tool> tools, ?list<AnthropicBeta> betas): [BetaManagedAgentsAgent](api/beta.md)

POST/v1/agents/{agent\_id}

##### [Archive Agent](api/beta/agents/archive.md)

$client->beta->agents->archive(string agentID, ?list<AnthropicBeta> betas): [BetaManagedAgentsAgent](api/beta.md)

POST/v1/agents/{agent\_id}/archive

##### ModelsExpand Collapse



[BetaManagedAgentsAgent](api/beta.md)

string id

?\Datetime archivedAt

A timestamp in RFC 3339 format

\Datetime createdAt

A timestamp in RFC 3339 format

?string description

list<[BetaManagedAgentsMCPServerURLDefinition](api/beta.md)> mcpServers

array<string,string> metadata

[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.

?[BetaManagedAgentsMultiagent](api/beta.md) multiagent

Resolved coordinator topology with a concrete agent roster.

string name

list<Skill> skills

?string system

list<Tool> tools

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

int version

The agent's current version. Starts at 1 and increments when the agent is modified.



[BetaManagedAgentsAgentReference](api/beta.md)

string id

Type type

int version



[BetaManagedAgentsAgentToolConfig](api/beta.md)

bool enabled

Name name

Built-in agent tool identifier.

PermissionPolicy permissionPolicy

Permission policy for tool execution.



[BetaManagedAgentsAgentToolConfigParams](api/beta.md)

Name name

Built-in agent tool identifier.

?bool enabled

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.

?PermissionPolicy permissionPolicy

Permission policy for tool execution.



[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md)

bool enabled

PermissionPolicy permissionPolicy

Permission policy for tool execution.



[BetaManagedAgentsAgentToolsetDefaultConfigParams](api/beta.md)

?bool enabled

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

?PermissionPolicy permissionPolicy

Permission policy for tool execution.



[BetaManagedAgentsAgentToolset20260401](api/beta.md)

list<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

Type type



[BetaManagedAgentsAgentToolset20260401BashInput](api/beta.md)

?string command

Shell command to execute. Omit only when `restart` is true.

?bool restart

When true, restart the persistent bash session instead of
running a command. Subsequent calls without `restart` will
run against the fresh session.

?int timeoutMs

Per-call timeout in milliseconds. Defaults to the
runner-wide tool timeout when omitted or zero.



[BetaManagedAgentsAgentToolset20260401EditInput](api/beta.md)

string filePath

Path of the file to edit.

string newString

Replacement text.

string oldString

Substring to find and replace.

?bool replaceAll

When true, replace every occurrence of `old_string`
instead of requiring a unique match.



[BetaManagedAgentsAgentToolset20260401GlobInput](api/beta.md)

string pattern

Doublestar glob pattern (e.g. `**/*.go`). Absolute patterns
are only permitted when the runner is configured to allow
them.

?string path

Optional directory root to search under. Defaults to the
runner's working directory.



[BetaManagedAgentsAgentToolset20260401GrepInput](api/beta.md)

string pattern

Regular expression to search for.

?string path

Optional directory root to search under. Defaults to the
runner's working directory.



[BetaManagedAgentsAgentToolset20260401Params](api/beta.md)

Type type

?list<[BetaManagedAgentsAgentToolConfigParams](api/beta.md)> configs

Per-tool configuration overrides.

?[BetaManagedAgentsAgentToolsetDefaultConfigParams](api/beta.md) defaultConfig

Default configuration for all tools in a toolset.



[BetaManagedAgentsAgentToolset20260401ReadInput](api/beta.md)

string filePath

Path of the file to read.

?list<int> viewRange

Optional `[start_line, end_line]` 1-indexed inclusive
range. When omitted the entire file is returned.
`end_line` of 0 or negative means "to end of file".



[BetaManagedAgentsAgentToolset20260401WriteInput](api/beta.md)

string content

Full file contents to write.

string filePath

Path of the file to write.



[BetaManagedAgentsAlwaysAllowPolicy](api/beta.md)

Type type



[BetaManagedAgentsAlwaysAskPolicy](api/beta.md)

Type type



[BetaManagedAgentsAnthropicSkill](api/beta.md)

string skillID

Type type

string version



[BetaManagedAgentsAnthropicSkillParams](api/beta.md)

string skillID

Identifier of the Anthropic skill (e.g., "xlsx").

Type type

?string version

Version to pin. Defaults to latest if omitted.



[BetaManagedAgentsCustomSkill](api/beta.md)

string skillID

Type type

string version



[BetaManagedAgentsCustomSkillParams](api/beta.md)

string skillID

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

Type type

?string version

Version to pin. Defaults to latest if omitted.



[BetaManagedAgentsCustomTool](api/beta.md)

string description

[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

string name

Type type



[BetaManagedAgentsCustomToolInputSchema](api/beta.md)

"object" type

?array<string,mixed> properties

?list<string> required



[BetaManagedAgentsCustomToolParams](api/beta.md)

string description

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

string name

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

Type type



[BetaManagedAgentsMCPServerURLDefinition](api/beta.md)

string name

Type type

string url



[BetaManagedAgentsMCPToolConfig](api/beta.md)

bool enabled

string name

PermissionPolicy permissionPolicy

Permission policy for tool execution.



[BetaManagedAgentsMCPToolConfigParams](api/beta.md)

string name

Name of the MCP tool to configure. 1-128 characters.

?bool enabled

Whether this tool is enabled. Overrides the `default_config` setting.

?PermissionPolicy permissionPolicy

Permission policy for tool execution.



[BetaManagedAgentsMCPToolset](api/beta.md)

list<[BetaManagedAgentsMCPToolConfig](api/beta.md)> configs

[BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

string mcpServerName

Type type



[BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md)

bool enabled

PermissionPolicy permissionPolicy

Permission policy for tool execution.



[BetaManagedAgentsMCPToolsetDefaultConfigParams](api/beta.md)

?bool enabled

Whether tools are enabled by default. Defaults to true if not specified.

?PermissionPolicy permissionPolicy

Permission policy for tool execution.



[BetaManagedAgentsMCPToolsetParams](api/beta.md)

string mcpServerName

Name of the MCP server. Must match a server name from the mcp\_servers array. 1-255 characters.

Type type

?list<[BetaManagedAgentsMCPToolConfigParams](api/beta.md)> configs

Per-tool configuration overrides.

?[BetaManagedAgentsMCPToolsetDefaultConfigParams](api/beta.md) defaultConfig

Default configuration for all tools from an MCP server.



BetaManagedAgentsModel

One of the following:

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

[BetaManagedAgentsModelConfig](api/beta.md)



BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

?Speed speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.



[BetaManagedAgentsModelConfigParams](api/beta.md)



BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

?Speed speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.



[BetaManagedAgentsMultiagentCoordinator](api/beta.md)

list<[BetaManagedAgentsAgentReference](api/beta.md)> agents

Agents the coordinator may spawn as session threads, each resolved to a specific version.

Type type



[BetaManagedAgentsMultiagentCoordinatorParams](api/beta.md)

list<[BetaManagedAgentsMultiagentRosterEntryParams](api/beta.md)> agents

Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

Type type



[BetaManagedAgentsMultiagentSelfParams](api/beta.md)

Type type



[BetaManagedAgentsSessionThreadAgent](api/beta.md)

string id

?string description

list<[BetaManagedAgentsMCPServerURLDefinition](api/beta.md)> mcpServers

[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.

string name

list<Skill> skills

?string system

list<Tool> tools

Type type

int version



[BetaManagedAgentsSkillParams](api/beta.md)

One of the following:



[BetaManagedAgentsAnthropicSkillParams](api/beta.md)

string skillID

Identifier of the Anthropic skill (e.g., "xlsx").

Type type

?string version

Version to pin. Defaults to latest if omitted.



[BetaManagedAgentsCustomSkillParams](api/beta.md)

string skillID

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

Type type

?string version

Version to pin. Defaults to latest if omitted.



[BetaManagedAgentsURLMCPServerParams](api/beta.md)

string name

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

Type type

string url

Endpoint URL for the MCP server.

#### AgentsVersions

##### [List Agent Versions](api/beta/agents/versions/list.md)

$client->beta->agents->versions->list(string agentID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[BetaManagedAgentsAgent](api/beta.md)>

GET/v1/agents/{agent\_id}/versions

---

*Copyright © Anthropic. All rights reserved.*
