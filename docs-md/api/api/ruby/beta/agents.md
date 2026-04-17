# Agents

Copy page

Ruby

# Agents

##### [Create Agent](api/beta/agents/create.md)

beta.agents.create(\*\*kwargs) -> [BetaManagedAgentsAgent](api/beta.md) { id, archived\_at, created\_at, 11 more }

POST/v1/agents

##### [List Agents](api/beta/agents/list.md)

beta.agents.list(\*\*kwargs) -> PageCursor<[BetaManagedAgentsAgent](api/beta.md) { id, archived\_at, created\_at, 11 more } >

GET/v1/agents

##### [Get Agent](api/beta/agents/retrieve.md)

beta.agents.retrieve(agent\_id, \*\*kwargs) -> [BetaManagedAgentsAgent](api/beta.md) { id, archived\_at, created\_at, 11 more }

GET/v1/agents/{agent\_id}

##### [Update Agent](api/beta/agents/update.md)

beta.agents.update(agent\_id, \*\*kwargs) -> [BetaManagedAgentsAgent](api/beta.md) { id, archived\_at, created\_at, 11 more }

POST/v1/agents/{agent\_id}

##### [Archive Agent](api/beta/agents/archive.md)

beta.agents.archive(agent\_id, \*\*kwargs) -> [BetaManagedAgentsAgent](api/beta.md) { id, archived\_at, created\_at, 11 more }

POST/v1/agents/{agent\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsAgent { id, archived\_at, created\_at, 11 more }

A Managed Agents `agent`.

id: String

archived\_at: Time

A timestamp in RFC 3339 format

created\_at: Time

A timestamp in RFC 3339 format

description: String

mcp\_servers: Array[[BetaManagedAgentsMCPServerURLDefinition](api/beta.md) { name, type, url } ]

name: String

type: :url

url: String

metadata: Hash[Symbol, String]

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

updated\_at: Time

A timestamp in RFC 3339 format

version: Integer

The agent's current version. Starts at 1 and increments when the agent is modified.

class BetaManagedAgentsAgentToolConfig { enabled, name, permission\_policy }

Configuration for a specific agent tool.

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

class BetaManagedAgentsAgentToolConfigParams { name, enabled, permission\_policy }

Configuration override for a specific tool within a toolset.

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

enabled: bool

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

class BetaManagedAgentsAgentToolsetDefaultConfig { enabled, permission\_policy }

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

class BetaManagedAgentsAgentToolsetDefaultConfigParams { enabled, permission\_policy }

Default configuration for all tools in a toolset.

enabled: bool

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

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

class BetaManagedAgentsAgentToolset20260401Params { type, configs, default\_config }

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

type: :agent\_toolset\_20260401

configs: Array[[BetaManagedAgentsAgentToolConfigParams](api/beta.md) { name, enabled, permission\_policy } ]

Per-tool configuration overrides.

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

enabled: bool

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfigParams](api/beta.md) { enabled, permission\_policy }

Default configuration for all tools in a toolset.

enabled: bool

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

class BetaManagedAgentsAnthropicSkill { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: String

type: :anthropic

version: String

class BetaManagedAgentsAnthropicSkillParams { skill\_id, type, version }

An Anthropic-managed skill.

skill\_id: String

Identifier of the Anthropic skill (e.g., "xlsx").

type: :anthropic

version: String

Version to pin. Defaults to latest if omitted.

class BetaManagedAgentsCustomSkill { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: String

type: :custom

version: String

class BetaManagedAgentsCustomSkillParams { skill\_id, type, version }

A user-created custom skill.

skill\_id: String

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

type: :custom

version: String

Version to pin. Defaults to latest if omitted.

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

class BetaManagedAgentsCustomToolInputSchema { properties, required, type }

JSON Schema for custom tool input parameters.

properties: Hash[Symbol, untyped]

JSON Schema properties defining the tool's input parameters.

required: Array[String]

List of required property names.

type: :object

Must be 'object' for tool input schemas.

class BetaManagedAgentsCustomToolParams { description, input\_schema, name, type }

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

description: String

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: Hash[Symbol, untyped]

JSON Schema properties defining the tool's input parameters.

required: Array[String]

List of required property names.

type: :object

Must be 'object' for tool input schemas.

name: String

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

type: :custom

class BetaManagedAgentsMCPServerURLDefinition { name, type, url }

URL-based MCP server connection as returned in API responses.

name: String

type: :url

url: String

class BetaManagedAgentsMCPToolConfig { enabled, name, permission\_policy }

Resolved configuration for a specific MCP tool.

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

class BetaManagedAgentsMCPToolConfigParams { name, enabled, permission\_policy }

Configuration override for a specific MCP tool.

name: String

Name of the MCP tool to configure. 1-128 characters.

enabled: bool

Whether this tool is enabled. Overrides the `default_config` setting.

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

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

class BetaManagedAgentsMCPToolsetDefaultConfig { enabled, permission\_policy }

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

class BetaManagedAgentsMCPToolsetDefaultConfigParams { enabled, permission\_policy }

Default configuration for all tools from an MCP server.

enabled: bool

Whether tools are enabled by default. Defaults to true if not specified.

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

class BetaManagedAgentsMCPToolsetParams { mcp\_server\_name, type, configs, default\_config }

Configuration for tools from an MCP server defined in `mcp_servers`.

mcp\_server\_name: String

Name of the MCP server. Must match a server name from the mcp\_servers array. 1-255 characters.

type: :mcp\_toolset

configs: Array[[BetaManagedAgentsMCPToolConfigParams](api/beta.md) { name, enabled, permission\_policy } ]

Per-tool configuration overrides.

name: String

Name of the MCP tool to configure. 1-128 characters.

enabled: bool

Whether this tool is enabled. Overrides the `default_config` setting.

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfigParams](api/beta.md) { enabled, permission\_policy }

Default configuration for all tools from an MCP server.

enabled: bool

Whether tools are enabled by default. Defaults to true if not specified.

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

BetaManagedAgentsModel = :"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more | String

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

class BetaManagedAgentsModelConfig { id, speed }

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

class BetaManagedAgentsModelConfigParams { id, speed }

An object that defines additional configuration control over model use

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

BetaManagedAgentsSkillParams = [BetaManagedAgentsAnthropicSkillParams](api/beta.md) { skill\_id, type, version }  | [BetaManagedAgentsCustomSkillParams](api/beta.md) { skill\_id, type, version }

Skill to load in the session container.

Accepts one of the following:

class BetaManagedAgentsAnthropicSkillParams { skill\_id, type, version }

An Anthropic-managed skill.

skill\_id: String

Identifier of the Anthropic skill (e.g., "xlsx").

type: :anthropic

version: String

Version to pin. Defaults to latest if omitted.

class BetaManagedAgentsCustomSkillParams { skill\_id, type, version }

A user-created custom skill.

skill\_id: String

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

type: :custom

version: String

Version to pin. Defaults to latest if omitted.

class BetaManagedAgentsURLMCPServerParams { name, type, url }

URL-based MCP server connection.

name: String

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

type: :url

url: String

Endpoint URL for the MCP server.

#### AgentsVersions

##### [List Agent Versions](api/beta/agents/versions/list.md)

beta.agents.versions.list(agent\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsAgent](api/beta.md) { id, archived\_at, created\_at, 11 more } >

GET/v1/agents/{agent\_id}/versions

---

*Copyright © Anthropic. All rights reserved.*
