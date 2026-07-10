# Agents

Copy page



C#

# Agents

##### [Create Agent](api/beta/agents/create.md)

[BetaManagedAgentsAgent](api/beta/agents.md) Beta.Agents.Create(AgentCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/agents

##### [List Agents](api/beta/agents/list.md)

[AgentListPageResponse](api/beta/agents.md) Beta.Agents.List(AgentListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/agents

##### [Get Agent](api/beta/agents/retrieve.md)

[BetaManagedAgentsAgent](api/beta/agents.md) Beta.Agents.Retrieve(AgentRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/agents/{agent\_id}

##### [Update Agent](api/beta/agents/update.md)

[BetaManagedAgentsAgent](api/beta/agents.md) Beta.Agents.Update(AgentUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/agents/{agent\_id}

##### [Archive Agent](api/beta/agents/archive.md)

[BetaManagedAgentsAgent](api/beta/agents.md) Beta.Agents.Archive(AgentArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/agents/{agent\_id}/archive

##### ModelsExpand Collapse



class BetaManagedAgentsAgent:

A Managed Agents `agent`.

required string ID

required DateTimeOffset? ArchivedAt

A timestamp in RFC 3339 format

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string? Description



required IReadOnlyList<[BetaManagedAgentsMcpServerUrlDefinition](api/beta/agents.md)> McpServers

required string Name

required Type Type

required string Url

required IReadOnlyDictionary<string, string> Metadata



required [BetaManagedAgentsModelConfig](api/beta/agents.md) Model

Model identifier and configuration.



required [BetaManagedAgentsModel](api/beta/agents.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"ClaudeSonnet5

High-performance model for coding and agents

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

required [BetaManagedAgentsMultiagent](api/beta/sessions.md)? Multiagent

Resolved coordinator topology with a concrete agent roster.



required IReadOnlyList<[BetaManagedAgentsAgentReference](api/beta/agents.md)> Agents

Agents the coordinator may spawn as session threads, each resolved to a specific version.

required string ID

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

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required Int Version

The agent's current version. Starts at 1 and increments when the agent is modified.



class BetaManagedAgentsAgentReference:

A resolved agent reference with a concrete version.

required string ID

required Type Type

required Int Version



class BetaManagedAgentsAgentToolConfig:

Configuration for a specific agent tool.

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

class BetaManagedAgentsAgentToolConfigParams:

Configuration override for a specific tool within a toolset.

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

class BetaManagedAgentsAgentToolsetDefaultConfig:

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



class BetaManagedAgentsAgentToolsetDefaultConfigParams:

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

class BetaManagedAgentsAgentToolset20260401BashInput:

Input payload for the `bash` tool of the
`agent_toolset_20260401` toolset. All fields are optional;
a normal invocation supplies `command`, while `restart=true`
(with no `command`) reboots the runner-side bash session.

string Command

Shell command to execute. Omit only when `restart` is true.

Boolean Restart

When true, restart the persistent bash session instead of
running a command. Subsequent calls without `restart` will
run against the fresh session.

Long TimeoutMs

Per-call timeout in milliseconds. Defaults to the
runner-wide tool timeout when omitted or zero.



class BetaManagedAgentsAgentToolset20260401EditInput:

Input payload for the `edit` tool. Performs a string
replacement in the named file; by default `old_string` must
occur exactly once.

required string FilePath

Path of the file to edit.

required string NewString

Replacement text.

required string OldString

Substring to find and replace.

Boolean ReplaceAll

When true, replace every occurrence of `old_string`
instead of requiring a unique match.



class BetaManagedAgentsAgentToolset20260401GlobInput:

Input payload for the `glob` tool. Returns paths matching a
doublestar glob pattern, newest first.

required string Pattern

Doublestar glob pattern (e.g. `**/*.go`). Absolute patterns
are only permitted when the runner is configured to allow
them.

string Path

Optional directory root to search under. Defaults to the
runner's working directory.



class BetaManagedAgentsAgentToolset20260401GrepInput:

Input payload for the `grep` tool. Searches file contents for
a regular expression, returning matching lines.

required string Pattern

Regular expression to search for.

string Path

Optional directory root to search under. Defaults to the
runner's working directory.

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

class BetaManagedAgentsAgentToolset20260401ReadInput:

Input payload for the `read` tool. Reads file contents
relative to the runner's working directory (or absolute when
the runner permits).

required string FilePath

Path of the file to read.

IReadOnlyList<Long> ViewRange

Optional `[start_line, end_line]` 1-indexed inclusive
range. When omitted the entire file is returned.
`end_line` of 0 or negative means "to end of file".



class BetaManagedAgentsAgentToolset20260401WriteInput:

Input payload for the `write` tool. Writes (overwriting) the
entire file contents.

required string Content

Full file contents to write.

required string FilePath

Path of the file to write.



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

required string SkillID

required Type Type

required string Version



class BetaManagedAgentsAnthropicSkillParams:

An Anthropic-managed skill.

required string SkillID

Identifier of the Anthropic skill (e.g., "xlsx").

required Type Type

string? Version

Version to pin. Defaults to latest if omitted.



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

required string SkillID

required Type Type

required string Version



class BetaManagedAgentsCustomSkillParams:

A user-created custom skill.

required string SkillID

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

required Type Type

string? Version

Version to pin. Defaults to latest if omitted.

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



class BetaManagedAgentsCustomToolInputSchema:

JSON Schema for custom tool input parameters.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required



class BetaManagedAgentsCustomToolParams:

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

required string Description

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-4096 characters.

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

class BetaManagedAgentsMcpServerUrlDefinition:

URL-based MCP server connection as returned in API responses.

required string Name

required Type Type

required string Url



class BetaManagedAgentsMcpToolConfig:

Resolved configuration for a specific MCP tool.

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

class BetaManagedAgentsMcpToolConfigParams:

Configuration override for a specific MCP tool.

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

class BetaManagedAgentsMcpToolsetDefaultConfig:

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



class BetaManagedAgentsMcpToolsetDefaultConfigParams:

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

class BetaManagedAgentsModelConfig:

Model identifier and configuration.



required [BetaManagedAgentsModel](api/beta/agents.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"ClaudeSonnet5

High-performance model for coding and agents

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

class BetaManagedAgentsModelConfigParams:

An object that defines additional configuration control over model use



required [BetaManagedAgentsModel](api/beta/agents.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"ClaudeSonnet5

High-performance model for coding and agents

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

Speed? Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"Standard

"fast"Fast



class BetaManagedAgentsMultiagentCoordinator:

Resolved coordinator topology with a concrete agent roster.



required IReadOnlyList<[BetaManagedAgentsAgentReference](api/beta/agents.md)> Agents

Agents the coordinator may spawn as session threads, each resolved to a specific version.

required string ID

required Type Type

required Int Version

required Type Type



class BetaManagedAgentsMultiagentCoordinatorParams:

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

class BetaManagedAgentsMultiagentSelfParams:

Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

required Type Type



class BetaManagedAgentsSessionThreadAgent:

Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

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

"claude-sonnet-5"ClaudeSonnet5

High-performance model for coding and agents

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



class BetaManagedAgentsSkillParams: A class that can be one of several variants.union 

Skill to load in the session container.



class BetaManagedAgentsAnthropicSkillParams:

An Anthropic-managed skill.

required string SkillID

Identifier of the Anthropic skill (e.g., "xlsx").

required Type Type

string? Version

Version to pin. Defaults to latest if omitted.



class BetaManagedAgentsCustomSkillParams:

A user-created custom skill.

required string SkillID

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

required Type Type

string? Version

Version to pin. Defaults to latest if omitted.



class BetaManagedAgentsUrlMcpServerParams:

URL-based MCP server connection.

required string Name

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

required Type Type

required string Url

Endpoint URL for the MCP server.

#### AgentsVersions

##### [List Agent Versions](api/beta/agents/versions/list.md)

[VersionListPageResponse](api/beta/agents/versions.md) Beta.Agents.Versions.List(VersionListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/agents/{agent\_id}/versions

---

*Copyright © Anthropic. All rights reserved.*
