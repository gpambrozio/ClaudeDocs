# Agents

Copy page



Go

# Agents

##### [Create Agent](api/beta/agents/create.md)

client.Beta.Agents.New(ctx, params) (\*[BetaManagedAgentsAgent](api/beta.md), error)

POST/v1/agents

##### [List Agents](api/beta/agents/list.md)

client.Beta.Agents.List(ctx, params) (\*PageCursor[[BetaManagedAgentsAgent](api/beta.md)], error)

GET/v1/agents

##### [Get Agent](api/beta/agents/retrieve.md)

client.Beta.Agents.Get(ctx, agentID, params) (\*[BetaManagedAgentsAgent](api/beta.md), error)

GET/v1/agents/{agent\_id}

##### [Update Agent](api/beta/agents/update.md)

client.Beta.Agents.Update(ctx, agentID, params) (\*[BetaManagedAgentsAgent](api/beta.md), error)

POST/v1/agents/{agent\_id}

##### [Archive Agent](api/beta/agents/archive.md)

client.Beta.Agents.Archive(ctx, agentID, body) (\*[BetaManagedAgentsAgent](api/beta.md), error)

POST/v1/agents/{agent\_id}/archive

##### ModelsExpand Collapse



type BetaManagedAgentsAgent struct{…}

A Managed Agents `agent`.

ID string

ArchivedAt Time

A timestamp in RFC 3339 format

CreatedAt Time

A timestamp in RFC 3339 format

Description string



MCPServers [][BetaManagedAgentsMCPServerURLDefinition](api/beta.md)

Name string

Type BetaManagedAgentsMCPServerURLDefinitionType

URL string

Metadata map[string, string]

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

Multiagent [BetaManagedAgentsMultiagent](api/beta.md)

Resolved coordinator topology with a concrete agent roster.



Agents [][BetaManagedAgentsAgentReference](api/beta.md)

Agents the coordinator may spawn as session threads, each resolved to a specific version.

ID string

Type BetaManagedAgentsAgentReferenceType

Version int64

Type BetaManagedAgentsMultiagentType

Name string



Skills []BetaManagedAgentsAgentSkillUnion

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

Tools []BetaManagedAgentsAgentToolUnion

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

Type BetaManagedAgentsAgentType

UpdatedAt Time

A timestamp in RFC 3339 format

Version int64

The agent's current version. Starts at 1 and increments when the agent is modified.



type BetaManagedAgentsAgentReference struct{…}

A resolved agent reference with a concrete version.

ID string

Type BetaManagedAgentsAgentReferenceType

Version int64



type BetaManagedAgentsAgentToolConfig struct{…}

Configuration for a specific agent tool.

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

type BetaManagedAgentsAgentToolConfigParamsResp struct{…}

Configuration override for a specific tool within a toolset.

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

type BetaManagedAgentsAgentToolsetDefaultConfig struct{…}

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



type BetaManagedAgentsAgentToolsetDefaultConfigParamsResp struct{…}

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

type BetaManagedAgentsAgentToolset20260401BashInput struct{…}

Input payload for the `bash` tool of the
`agent_toolset_20260401` toolset. All fields are optional;
a normal invocation supplies `command`, while `restart=true`
(with no `command`) reboots the runner-side bash session.

Command stringOptional

Shell command to execute. Omit only when `restart` is true.

Restart boolOptional

When true, restart the persistent bash session instead of
running a command. Subsequent calls without `restart` will
run against the fresh session.

TimeoutMs int64Optional

Per-call timeout in milliseconds. Defaults to the
runner-wide tool timeout when omitted or zero.



type BetaManagedAgentsAgentToolset20260401EditInput struct{…}

Input payload for the `edit` tool. Performs a string
replacement in the named file; by default `old_string` must
occur exactly once.

FilePath string

Path of the file to edit.

NewString string

Replacement text.

OldString string

Substring to find and replace.

ReplaceAll boolOptional

When true, replace every occurrence of `old_string`
instead of requiring a unique match.



type BetaManagedAgentsAgentToolset20260401GlobInput struct{…}

Input payload for the `glob` tool. Returns paths matching a
doublestar glob pattern, newest first.

Pattern string

Doublestar glob pattern (e.g. `**/*.go`). Absolute patterns
are only permitted when the runner is configured to allow
them.

Path stringOptional

Optional directory root to search under. Defaults to the
runner's working directory.



type BetaManagedAgentsAgentToolset20260401GrepInput struct{…}

Input payload for the `grep` tool. Searches file contents for
a regular expression, returning matching lines.

Pattern string

Regular expression to search for.

Path stringOptional

Optional directory root to search under. Defaults to the
runner's working directory.

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

type BetaManagedAgentsAgentToolset20260401ReadInput struct{…}

Input payload for the `read` tool. Reads file contents
relative to the runner's working directory (or absolute when
the runner permits).

FilePath string

Path of the file to read.

ViewRange []int64Optional

Optional `[start_line, end_line]` 1-indexed inclusive
range. When omitted the entire file is returned.
`end_line` of 0 or negative means "to end of file".



type BetaManagedAgentsAgentToolset20260401WriteInput struct{…}

Input payload for the `write` tool. Writes (overwriting) the
entire file contents.

Content string

Full file contents to write.

FilePath string

Path of the file to write.



type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType



type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType



type BetaManagedAgentsAnthropicSkill struct{…}

A resolved Anthropic-managed skill.

SkillID string

Type BetaManagedAgentsAnthropicSkillType

Version string



type BetaManagedAgentsAnthropicSkillParamsResp struct{…}

An Anthropic-managed skill.

SkillID string

Identifier of the Anthropic skill (e.g., "xlsx").

Type BetaManagedAgentsAnthropicSkillParamsType

Version stringOptional

Version to pin. Defaults to latest if omitted.



type BetaManagedAgentsCustomSkill struct{…}

A resolved user-created custom skill.

SkillID string

Type BetaManagedAgentsCustomSkillType

Version string



type BetaManagedAgentsCustomSkillParamsResp struct{…}

A user-created custom skill.

SkillID string

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

Type BetaManagedAgentsCustomSkillParamsType

Version stringOptional

Version to pin. Defaults to latest if omitted.

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



type BetaManagedAgentsCustomToolInputSchema struct{…}

JSON Schema for custom tool input parameters.

Type Object

Properties map[string, any]Optional

Required []stringOptional

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

type BetaManagedAgentsMCPServerURLDefinition struct{…}

URL-based MCP server connection as returned in API responses.

Name string

Type BetaManagedAgentsMCPServerURLDefinitionType

URL string



type BetaManagedAgentsMCPToolConfig struct{…}

Resolved configuration for a specific MCP tool.

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

type BetaManagedAgentsMCPToolConfigParamsResp struct{…}

Configuration override for a specific MCP tool.

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

type BetaManagedAgentsMCPToolsetDefaultConfig struct{…}

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



type BetaManagedAgentsMCPToolsetDefaultConfigParamsResp struct{…}

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

type BetaManagedAgentsModel interface{…}

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

type BetaManagedAgentsModelConfig struct{…}

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

type BetaManagedAgentsModelConfigParamsResp struct{…}

An object that defines additional configuration control over model use

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

Speed BetaManagedAgentsModelConfigParamsSpeedOptional

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

const BetaManagedAgentsModelConfigParamsSpeedStandard BetaManagedAgentsModelConfigParamsSpeed = "standard"

const BetaManagedAgentsModelConfigParamsSpeedFast BetaManagedAgentsModelConfigParamsSpeed = "fast"



type BetaManagedAgentsMultiagentCoordinator struct{…}

Resolved coordinator topology with a concrete agent roster.



Agents [][BetaManagedAgentsAgentReference](api/beta.md)

Agents the coordinator may spawn as session threads, each resolved to a specific version.

ID string

Type BetaManagedAgentsAgentReferenceType

Version int64

Type BetaManagedAgentsMultiagentCoordinatorType



type BetaManagedAgentsMultiagentCoordinatorParamsResp struct{…}

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

Type BetaManagedAgentsMultiagentCoordinatorParamsType



type BetaManagedAgentsMultiagentSelfParamsResp struct{…}

Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

Type BetaManagedAgentsMultiagentSelfParamsType



type BetaManagedAgentsSessionThreadAgent struct{…}

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



type BetaManagedAgentsSkillParamsUnionResp interface{…}

Skill to load in the session container.

One of the following:



type BetaManagedAgentsAnthropicSkillParamsResp struct{…}

An Anthropic-managed skill.

SkillID string

Identifier of the Anthropic skill (e.g., "xlsx").

Type BetaManagedAgentsAnthropicSkillParamsType

Version stringOptional

Version to pin. Defaults to latest if omitted.



type BetaManagedAgentsCustomSkillParamsResp struct{…}

A user-created custom skill.

SkillID string

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

Type BetaManagedAgentsCustomSkillParamsType

Version stringOptional

Version to pin. Defaults to latest if omitted.



type BetaManagedAgentsURLMCPServerParamsResp struct{…}

URL-based MCP server connection.

Name string

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

Type BetaManagedAgentsURLMCPServerParamsType

URL string

Endpoint URL for the MCP server.

#### AgentsVersions

##### [List Agent Versions](api/beta/agents/versions/list.md)

client.Beta.Agents.Versions.List(ctx, agentID, params) (\*PageCursor[[BetaManagedAgentsAgent](api/beta.md)], error)

GET/v1/agents/{agent\_id}/versions

---

*Copyright © Anthropic. All rights reserved.*
