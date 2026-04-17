# Agents

Copy page

Java

# Agents

##### [Create Agent](api/beta/agents/create.md)

[BetaManagedAgentsAgent](api/beta.md) beta().agents().create(AgentCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/agents

##### [List Agents](api/beta/agents/list.md)

AgentListPage beta().agents().list(AgentListParamsparams = AgentListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/agents

##### [Get Agent](api/beta/agents/retrieve.md)

[BetaManagedAgentsAgent](api/beta.md) beta().agents().retrieve(AgentRetrieveParamsparams = AgentRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/agents/{agent\_id}

##### [Update Agent](api/beta/agents/update.md)

[BetaManagedAgentsAgent](api/beta.md) beta().agents().update(AgentUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/agents/{agent\_id}

##### [Archive Agent](api/beta/agents/archive.md)

[BetaManagedAgentsAgent](api/beta.md) beta().agents().archive(AgentArchiveParamsparams = AgentArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/agents/{agent\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsAgent:

A Managed Agents `agent`.

String id

Optional<LocalDateTime> archivedAt

A timestamp in RFC 3339 format

LocalDateTime createdAt

A timestamp in RFC 3339 format

Optional<String> description

List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> mcpServers

String name

Type type

String url

Metadata metadata

[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.

BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

String name

List<Skill> skills

Accepts one of the following:

class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version

class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system

List<Tool> tools

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401:

List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled

Name name

Built-in agent tool identifier.

Accepts one of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type

class BetaManagedAgentsMcpToolset:

List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type

class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description

[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

Optional<Properties> properties

JSON Schema properties defining the tool's input parameters.

Optional<List<String>> required

List of required property names.

Optional<Type> type

Must be 'object' for tool input schemas.

String name

Type type

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

long version

The agent's current version. Starts at 1 and increments when the agent is modified.

class BetaManagedAgentsAgentToolConfig:

Configuration for a specific agent tool.

boolean enabled

Name name

Built-in agent tool identifier.

Accepts one of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

class BetaManagedAgentsAgentToolConfigParams:

Configuration override for a specific tool within a toolset.

Name name

Built-in agent tool identifier.

Accepts one of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")

Optional<Boolean> enabled

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.

Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

class BetaManagedAgentsAgentToolsetDefaultConfig:

Resolved default configuration for agent tools.

boolean enabled

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

class BetaManagedAgentsAgentToolsetDefaultConfigParams:

Default configuration for all tools in a toolset.

Optional<Boolean> enabled

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

class BetaManagedAgentsAgentToolset20260401:

List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled

Name name

Built-in agent tool identifier.

Accepts one of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type

class BetaManagedAgentsAgentToolset20260401Params:

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

Type type

Optional<List<[BetaManagedAgentsAgentToolConfigParams](api/beta.md)>> configs

Per-tool configuration overrides.

Name name

Built-in agent tool identifier.

Accepts one of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")

Optional<Boolean> enabled

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.

Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Optional<[BetaManagedAgentsAgentToolsetDefaultConfigParams](api/beta.md)> defaultConfig

Default configuration for all tools in a toolset.

Optional<Boolean> enabled

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version

class BetaManagedAgentsAnthropicSkillParams:

An Anthropic-managed skill.

String skillId

Identifier of the Anthropic skill (e.g., "xlsx").

Type type

Optional<String> version

Version to pin. Defaults to latest if omitted.

class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

class BetaManagedAgentsCustomSkillParams:

A user-created custom skill.

String skillId

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

Type type

Optional<String> version

Version to pin. Defaults to latest if omitted.

class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description

[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

Optional<Properties> properties

JSON Schema properties defining the tool's input parameters.

Optional<List<String>> required

List of required property names.

Optional<Type> type

Must be 'object' for tool input schemas.

String name

Type type

class BetaManagedAgentsCustomToolInputSchema:

JSON Schema for custom tool input parameters.

Optional<Properties> properties

JSON Schema properties defining the tool's input parameters.

Optional<List<String>> required

List of required property names.

Optional<Type> type

Must be 'object' for tool input schemas.

class BetaManagedAgentsCustomToolParams:

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

String description

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

Optional<Properties> properties

JSON Schema properties defining the tool's input parameters.

Optional<List<String>> required

List of required property names.

Optional<Type> type

Must be 'object' for tool input schemas.

String name

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

Type type

class BetaManagedAgentsMcpServerUrlDefinition:

URL-based MCP server connection as returned in API responses.

String name

Type type

String url

class BetaManagedAgentsMcpToolConfig:

Resolved configuration for a specific MCP tool.

boolean enabled

String name

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

class BetaManagedAgentsMcpToolConfigParams:

Configuration override for a specific MCP tool.

String name

Name of the MCP tool to configure. 1-128 characters.

Optional<Boolean> enabled

Whether this tool is enabled. Overrides the `default_config` setting.

Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

class BetaManagedAgentsMcpToolset:

List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type

class BetaManagedAgentsMcpToolsetDefaultConfig:

Resolved default configuration for all tools from an MCP server.

boolean enabled

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

class BetaManagedAgentsMcpToolsetDefaultConfigParams:

Default configuration for all tools from an MCP server.

Optional<Boolean> enabled

Whether tools are enabled by default. Defaults to true if not specified.

Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

class BetaManagedAgentsMcpToolsetParams:

Configuration for tools from an MCP server defined in `mcp_servers`.

String mcpServerName

Name of the MCP server. Must match a server name from the mcp\_servers array. 1-255 characters.

Type type

Optional<List<[BetaManagedAgentsMcpToolConfigParams](api/beta.md)>> configs

Per-tool configuration overrides.

String name

Name of the MCP tool to configure. 1-128 characters.

Optional<Boolean> enabled

Whether this tool is enabled. Overrides the `default_config` setting.

Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Optional<[BetaManagedAgentsMcpToolsetDefaultConfigParams](api/beta.md)> defaultConfig

Default configuration for all tools from an MCP server.

Optional<Boolean> enabled

Whether tools are enabled by default. Defaults to true if not specified.

Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

enum BetaManagedAgentsModel:

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

class BetaManagedAgentsModelConfig:

Model identifier and configuration.

BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

class BetaManagedAgentsModelConfigParams:

An object that defines additional configuration control over model use

BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

class BetaManagedAgentsSkillParams: A class that can be one of several variants.union

Skill to load in the session container.

class BetaManagedAgentsAnthropicSkillParams:

An Anthropic-managed skill.

String skillId

Identifier of the Anthropic skill (e.g., "xlsx").

Type type

Optional<String> version

Version to pin. Defaults to latest if omitted.

class BetaManagedAgentsCustomSkillParams:

A user-created custom skill.

String skillId

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

Type type

Optional<String> version

Version to pin. Defaults to latest if omitted.

class BetaManagedAgentsUrlMcpServerParams:

URL-based MCP server connection.

String name

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

Type type

String url

Endpoint URL for the MCP server.

#### AgentsVersions

##### [List Agent Versions](api/beta/agents/versions/list.md)

VersionListPage beta().agents().versions().list(VersionListParamsparams = VersionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/agents/{agent\_id}/versions

---

*Copyright © Anthropic. All rights reserved.*
