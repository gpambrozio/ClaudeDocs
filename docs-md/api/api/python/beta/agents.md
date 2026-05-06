# Agents

Copy page

Python

# Agents

##### [Create Agent](api/beta/agents/create.md)

beta.agents.create(AgentCreateParams\*\*kwargs)  -> [BetaManagedAgentsAgent](api/beta.md)

POST/v1/agents

##### [List Agents](api/beta/agents/list.md)

beta.agents.list(AgentListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsAgent](api/beta.md)]

GET/v1/agents

##### [Get Agent](api/beta/agents/retrieve.md)

beta.agents.retrieve(stragent\_id, AgentRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsAgent](api/beta.md)

GET/v1/agents/{agent\_id}

##### [Update Agent](api/beta/agents/update.md)

beta.agents.update(stragent\_id, AgentUpdateParams\*\*kwargs)  -> [BetaManagedAgentsAgent](api/beta.md)

POST/v1/agents/{agent\_id}

##### [Archive Agent](api/beta/agents/archive.md)

beta.agents.archive(stragent\_id, AgentArchiveParams\*\*kwargs)  -> [BetaManagedAgentsAgent](api/beta.md)

POST/v1/agents/{agent\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsAgent: …

A Managed Agents `agent`.

id: str

archived\_at: Optional[datetime]

A timestamp in RFC 3339 format

created\_at: datetime

A timestamp in RFC 3339 format

description: Optional[str]

mcp\_servers: List[[BetaManagedAgentsMCPServerURLDefinition](api/beta.md)]

name: str

type: Literal["url"]

url: str

metadata: Dict[str, str]

model: [BetaManagedAgentsModelConfig](api/beta.md)

Model identifier and configuration.

id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

Literal["claude-opus-4-7", "claude-opus-4-6", "claude-sonnet-4-6", 6 more]

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

Accepts one of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

str

speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"

"fast"

multiagent: Optional[BetaManagedAgentsMultiagent]

Resolved coordinator topology with a concrete agent roster.

agents: List[[BetaManagedAgentsAgentReference](api/beta.md)]

Agents the coordinator may spawn as session threads, each resolved to a specific version.

id: str

type: Literal["agent"]

version: int

type: Literal["coordinator"]

name: str

skills: List[Skill]

Accepts one of the following:

class BetaManagedAgentsAnthropicSkill: …

A resolved Anthropic-managed skill.

skill\_id: str

type: Literal["anthropic"]

version: str

class BetaManagedAgentsCustomSkill: …

A resolved user-created custom skill.

skill\_id: str

type: Literal["custom"]

version: str

system: Optional[str]

tools: List[Tool]

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401: …

configs: List[[BetaManagedAgentsAgentToolConfig](api/beta.md)]

enabled: bool

name: Literal["bash", "edit", "read", 5 more]

Built-in agent tool identifier.

Accepts one of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

permission\_policy: PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md)

Resolved default configuration for agent tools.

enabled: bool

permission\_policy: PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

type: Literal["agent\_toolset\_20260401"]

class BetaManagedAgentsMCPToolset: …

configs: List[[BetaManagedAgentsMCPToolConfig](api/beta.md)]

enabled: bool

name: str

permission\_policy: PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md)

Resolved default configuration for all tools from an MCP server.

enabled: bool

permission\_policy: PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

mcp\_server\_name: str

type: Literal["mcp\_toolset"]

class BetaManagedAgentsCustomTool: …

A custom tool as returned in API responses.

description: str

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md)

JSON Schema for custom tool input parameters.

properties: Optional[Dict[str, object]]

JSON Schema properties defining the tool's input parameters.

required: Optional[List[str]]

List of required property names.

type: Optional[Literal["object"]]

Must be 'object' for tool input schemas.

name: str

type: Literal["custom"]

type: Literal["agent"]

updated\_at: datetime

A timestamp in RFC 3339 format

version: int

The agent's current version. Starts at 1 and increments when the agent is modified.

class BetaManagedAgentsAgentReference: …

A resolved agent reference with a concrete version.

id: str

type: Literal["agent"]

version: int

class BetaManagedAgentsAgentToolConfig: …

Configuration for a specific agent tool.

enabled: bool

name: Literal["bash", "edit", "read", 5 more]

Built-in agent tool identifier.

Accepts one of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

permission\_policy: PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

class BetaManagedAgentsAgentToolConfigParams: …

Configuration override for a specific tool within a toolset.

name: Literal["bash", "edit", "read", 5 more]

Built-in agent tool identifier.

Accepts one of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

enabled: Optional[bool]

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.

permission\_policy: Optional[PermissionPolicy]

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

class BetaManagedAgentsAgentToolsetDefaultConfig: …

Resolved default configuration for agent tools.

enabled: bool

permission\_policy: PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

class BetaManagedAgentsAgentToolsetDefaultConfigParams: …

Default configuration for all tools in a toolset.

enabled: Optional[bool]

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

permission\_policy: Optional[PermissionPolicy]

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

class BetaManagedAgentsAgentToolset20260401: …

configs: List[[BetaManagedAgentsAgentToolConfig](api/beta.md)]

enabled: bool

name: Literal["bash", "edit", "read", 5 more]

Built-in agent tool identifier.

Accepts one of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

permission\_policy: PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md)

Resolved default configuration for agent tools.

enabled: bool

permission\_policy: PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

type: Literal["agent\_toolset\_20260401"]

class BetaManagedAgentsAgentToolset20260401Params: …

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

type: Literal["agent\_toolset\_20260401"]

configs: Optional[List[[BetaManagedAgentsAgentToolConfigParams](api/beta.md)]]

Per-tool configuration overrides.

name: Literal["bash", "edit", "read", 5 more]

Built-in agent tool identifier.

Accepts one of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

enabled: Optional[bool]

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.

permission\_policy: Optional[PermissionPolicy]

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

default\_config: Optional[BetaManagedAgentsAgentToolsetDefaultConfigParams]

Default configuration for all tools in a toolset.

enabled: Optional[bool]

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

permission\_policy: Optional[PermissionPolicy]

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

class BetaManagedAgentsAnthropicSkill: …

A resolved Anthropic-managed skill.

skill\_id: str

type: Literal["anthropic"]

version: str

class BetaManagedAgentsAnthropicSkillParams: …

An Anthropic-managed skill.

skill\_id: str

Identifier of the Anthropic skill (e.g., "xlsx").

type: Literal["anthropic"]

version: Optional[str]

Version to pin. Defaults to latest if omitted.

class BetaManagedAgentsCustomSkill: …

A resolved user-created custom skill.

skill\_id: str

type: Literal["custom"]

version: str

class BetaManagedAgentsCustomSkillParams: …

A user-created custom skill.

skill\_id: str

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

type: Literal["custom"]

version: Optional[str]

Version to pin. Defaults to latest if omitted.

class BetaManagedAgentsCustomTool: …

A custom tool as returned in API responses.

description: str

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md)

JSON Schema for custom tool input parameters.

properties: Optional[Dict[str, object]]

JSON Schema properties defining the tool's input parameters.

required: Optional[List[str]]

List of required property names.

type: Optional[Literal["object"]]

Must be 'object' for tool input schemas.

name: str

type: Literal["custom"]

class BetaManagedAgentsCustomToolInputSchema: …

JSON Schema for custom tool input parameters.

properties: Optional[Dict[str, object]]

JSON Schema properties defining the tool's input parameters.

required: Optional[List[str]]

List of required property names.

type: Optional[Literal["object"]]

Must be 'object' for tool input schemas.

class BetaManagedAgentsCustomToolParams: …

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

description: str

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md)

JSON Schema for custom tool input parameters.

properties: Optional[Dict[str, object]]

JSON Schema properties defining the tool's input parameters.

required: Optional[List[str]]

List of required property names.

type: Optional[Literal["object"]]

Must be 'object' for tool input schemas.

name: str

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

type: Literal["custom"]

class BetaManagedAgentsMCPServerURLDefinition: …

URL-based MCP server connection as returned in API responses.

name: str

type: Literal["url"]

url: str

class BetaManagedAgentsMCPToolConfig: …

Resolved configuration for a specific MCP tool.

enabled: bool

name: str

permission\_policy: PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

class BetaManagedAgentsMCPToolConfigParams: …

Configuration override for a specific MCP tool.

name: str

Name of the MCP tool to configure. 1-128 characters.

enabled: Optional[bool]

Whether this tool is enabled. Overrides the `default_config` setting.

permission\_policy: Optional[PermissionPolicy]

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

class BetaManagedAgentsMCPToolset: …

configs: List[[BetaManagedAgentsMCPToolConfig](api/beta.md)]

enabled: bool

name: str

permission\_policy: PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md)

Resolved default configuration for all tools from an MCP server.

enabled: bool

permission\_policy: PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

mcp\_server\_name: str

type: Literal["mcp\_toolset"]

class BetaManagedAgentsMCPToolsetDefaultConfig: …

Resolved default configuration for all tools from an MCP server.

enabled: bool

permission\_policy: PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

class BetaManagedAgentsMCPToolsetDefaultConfigParams: …

Default configuration for all tools from an MCP server.

enabled: Optional[bool]

Whether tools are enabled by default. Defaults to true if not specified.

permission\_policy: Optional[PermissionPolicy]

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

class BetaManagedAgentsMCPToolsetParams: …

Configuration for tools from an MCP server defined in `mcp_servers`.

mcp\_server\_name: str

Name of the MCP server. Must match a server name from the mcp\_servers array. 1-255 characters.

type: Literal["mcp\_toolset"]

configs: Optional[List[[BetaManagedAgentsMCPToolConfigParams](api/beta.md)]]

Per-tool configuration overrides.

name: str

Name of the MCP tool to configure. 1-128 characters.

enabled: Optional[bool]

Whether this tool is enabled. Overrides the `default_config` setting.

permission\_policy: Optional[PermissionPolicy]

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

default\_config: Optional[BetaManagedAgentsMCPToolsetDefaultConfigParams]

Default configuration for all tools from an MCP server.

enabled: Optional[bool]

Whether tools are enabled by default. Defaults to true if not specified.

permission\_policy: Optional[PermissionPolicy]

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

Union[Literal["claude-opus-4-7", "claude-opus-4-6", "claude-sonnet-4-6", 6 more], str]

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

Literal["claude-opus-4-7", "claude-opus-4-6", "claude-sonnet-4-6", 6 more]

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

Accepts one of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

str

class BetaManagedAgentsModelConfig: …

Model identifier and configuration.

id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

Literal["claude-opus-4-7", "claude-opus-4-6", "claude-sonnet-4-6", 6 more]

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

Accepts one of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

str

speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"

"fast"

class BetaManagedAgentsModelConfigParams: …

An object that defines additional configuration control over model use

id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

Literal["claude-opus-4-7", "claude-opus-4-6", "claude-sonnet-4-6", 6 more]

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

Accepts one of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

str

speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"

"fast"

class BetaManagedAgentsMultiagentCoordinator: …

Resolved coordinator topology with a concrete agent roster.

agents: List[[BetaManagedAgentsAgentReference](api/beta.md)]

Agents the coordinator may spawn as session threads, each resolved to a specific version.

id: str

type: Literal["agent"]

version: int

type: Literal["coordinator"]

class BetaManagedAgentsMultiagentCoordinatorParams: …

A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

agents: List[[BetaManagedAgentsMultiagentRosterEntryParams](api/beta.md)]

Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

Accepts one of the following:

str

class BetaManagedAgentsAgentParams: …

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: str

The `agent` ID.

type: Literal["agent"]

version: Optional[int]

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

class BetaManagedAgentsMultiagentSelfParams: …

Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

type: Literal["self"]

type: Literal["coordinator"]

class BetaManagedAgentsMultiagentSelfParams: …

Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

type: Literal["self"]

[BetaManagedAgentsSkillParams](api/beta.md)

Skill to load in the session container.

Accepts one of the following:

class BetaManagedAgentsAnthropicSkillParams: …

An Anthropic-managed skill.

skill\_id: str

Identifier of the Anthropic skill (e.g., "xlsx").

type: Literal["anthropic"]

version: Optional[str]

Version to pin. Defaults to latest if omitted.

class BetaManagedAgentsCustomSkillParams: …

A user-created custom skill.

skill\_id: str

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

type: Literal["custom"]

version: Optional[str]

Version to pin. Defaults to latest if omitted.

class BetaManagedAgentsURLMCPServerParams: …

URL-based MCP server connection.

name: str

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

type: Literal["url"]

url: str

Endpoint URL for the MCP server.

#### AgentsVersions

##### [List Agent Versions](api/beta/agents/versions/list.md)

beta.agents.versions.list(stragent\_id, VersionListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsAgent](api/beta.md)]

GET/v1/agents/{agent\_id}/versions

---

*Copyright © Anthropic. All rights reserved.*
