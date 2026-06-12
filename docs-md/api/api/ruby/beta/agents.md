# Agents

Copy page

SDK language

Ruby

# Agents

##### [Create Agent](api/beta/agents/create.md)

beta.agents.create(\*\*kwargs) -> [BetaManagedAgentsAgent](api/beta.md) { id, archived\_at, created\_at, 12 more }

POST/v1/agents

##### [List Agents](api/beta/agents/list.md)

beta.agents.list(\*\*kwargs) -> PageCursor<[BetaManagedAgentsAgent](api/beta.md) { id, archived\_at, created\_at, 12 more } >

GET/v1/agents

##### [Get Agent](api/beta/agents/retrieve.md)

beta.agents.retrieve(agent\_id, \*\*kwargs) -> [BetaManagedAgentsAgent](api/beta.md) { id, archived\_at, created\_at, 12 more }

GET/v1/agents/{agent\_id}

##### [Update Agent](api/beta/agents/update.md)

beta.agents.update(agent\_id, \*\*kwargs) -> [BetaManagedAgentsAgent](api/beta.md) { id, archived\_at, created\_at, 12 more }

POST/v1/agents/{agent\_id}

##### [Archive Agent](api/beta/agents/archive.md)

beta.agents.archive(agent\_id, \*\*kwargs) -> [BetaManagedAgentsAgent](api/beta.md) { id, archived\_at, created\_at, 12 more }

POST/v1/agents/{agent\_id}/archive

##### ModelsExpand Collapse



class BetaManagedAgentsAgent { id, archived\_at, created\_at, 12 more } 

A Managed Agents `agent`.

id: String

archived\_at: Time

A timestamp in RFC 3339 format

created\_at: Time

A timestamp in RFC 3339 format

description: String



mcp\_servers: Array[[BetaManagedAgentsMCPServerURLDefinition](api/beta.md) { name, type, url } ]

name: String

type: :url

url: String

metadata: Hash[Symbol, String]



model: [BetaManagedAgentsModelConfig](api/beta.md) { id, speed } 

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



BetaManagedAgentsModel = :"claude-fable-5" | :"claude-opus-4-8" | :"claude-opus-4-7" | 8 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

String = String



speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

:standard

:fast



multiagent: [BetaManagedAgentsMultiagent](api/beta.md) { agents, type } 

Resolved coordinator topology with a concrete agent roster.



agents: Array[[BetaManagedAgentsAgentReference](api/beta.md) { id, type, version } ]

Agents the coordinator may spawn as session threads, each resolved to a specific version.

id: String

type: :agent

version: Integer

type: :coordinator

name: String



skills: Array[[BetaManagedAgentsAnthropicSkill](api/beta.md) { skill\_id, type, version }  | [BetaManagedAgentsCustomSkill](api/beta.md) { skill\_id, type, version } ]

One of the following:



class BetaManagedAgentsAnthropicSkill { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: String

type: :anthropic

version: String



class BetaManagedAgentsCustomSkill { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: String

type: :custom

version: String

system\_: String



tools: Array[[BetaManagedAgentsAgentToolset20260401](api/beta.md) { configs, default\_config, type }  | [BetaManagedAgentsMCPToolset](api/beta.md) { configs, default\_config, mcp\_server\_name, type }  | [BetaManagedAgentsCustomTool](api/beta.md) { description, input\_schema, name, type } ]

One of the following:



class BetaManagedAgentsAgentToolset20260401 { configs, default\_config, type } 



configs: Array[[BetaManagedAgentsAgentToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool



name: :bash | :edit | :read | 5 more

Built-in agent tool identifier.

One of the following:

:bash

:edit

:read

:write

:glob

:grep

:web\_fetch

:web\_search



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: bool



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask

type: :agent\_toolset\_20260401



class BetaManagedAgentsMCPToolset { configs, default\_config, mcp\_server\_name, type } 



configs: Array[[BetaManagedAgentsMCPToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool

name: String



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: bool



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask

mcp\_server\_name: String

type: :mcp\_toolset



class BetaManagedAgentsCustomTool { description, input\_schema, name, type } 

A custom tool as returned in API responses.

description: String



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md) { type, properties, required } 

JSON Schema for custom tool input parameters.

type: :object

properties: Hash[Symbol, untyped]

required: Array[String]

name: String

type: :custom

type: :agent

updated\_at: Time

A timestamp in RFC 3339 format

version: Integer

The agent's current version. Starts at 1 and increments when the agent is modified.



class BetaManagedAgentsAgentReference { id, type, version } 

A resolved agent reference with a concrete version.

id: String

type: :agent

version: Integer



class BetaManagedAgentsAgentToolConfig { enabled, name, permission\_policy } 

Configuration for a specific agent tool.

enabled: bool



name: :bash | :edit | :read | 5 more

Built-in agent tool identifier.

One of the following:

:bash

:edit

:read

:write

:glob

:grep

:web\_fetch

:web\_search



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask



class BetaManagedAgentsAgentToolConfigParams { name, enabled, permission\_policy } 

Configuration override for a specific tool within a toolset.



name: :bash | :edit | :read | 5 more

Built-in agent tool identifier.

One of the following:

:bash

:edit

:read

:write

:glob

:grep

:web\_fetch

:web\_search

enabled: bool

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask



class BetaManagedAgentsAgentToolsetDefaultConfig { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: bool



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask



class BetaManagedAgentsAgentToolsetDefaultConfigParams { enabled, permission\_policy } 

Default configuration for all tools in a toolset.

enabled: bool

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask



class BetaManagedAgentsAgentToolset20260401 { configs, default\_config, type } 



configs: Array[[BetaManagedAgentsAgentToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool



name: :bash | :edit | :read | 5 more

Built-in agent tool identifier.

One of the following:

:bash

:edit

:read

:write

:glob

:grep

:web\_fetch

:web\_search



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: bool



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask

type: :agent\_toolset\_20260401



class BetaManagedAgentsAgentToolset20260401BashInput { command, restart, timeout\_ms } 

Input payload for the `bash` tool of the
`agent_toolset_20260401` toolset. All fields are optional;
a normal invocation supplies `command`, while `restart=true`
(with no `command`) reboots the runner-side bash session.

command: String

Shell command to execute. Omit only when `restart` is true.

restart: bool

When true, restart the persistent bash session instead of
running a command. Subsequent calls without `restart` will
run against the fresh session.

timeout\_ms: Integer

Per-call timeout in milliseconds. Defaults to the
runner-wide tool timeout when omitted or zero.



class BetaManagedAgentsAgentToolset20260401EditInput { file\_path, new\_string, old\_string, replace\_all } 

Input payload for the `edit` tool. Performs a string
replacement in the named file; by default `old_string` must
occur exactly once.

file\_path: String

Path of the file to edit.

new\_string: String

Replacement text.

old\_string: String

Substring to find and replace.

replace\_all: bool

When true, replace every occurrence of `old_string`
instead of requiring a unique match.



class BetaManagedAgentsAgentToolset20260401GlobInput { pattern, path } 

Input payload for the `glob` tool. Returns paths matching a
doublestar glob pattern, newest first.

pattern: String

Doublestar glob pattern (e.g. `**/*.go`). Absolute patterns
are only permitted when the runner is configured to allow
them.

path: String

Optional directory root to search under. Defaults to the
runner's working directory.



class BetaManagedAgentsAgentToolset20260401GrepInput { pattern, path } 

Input payload for the `grep` tool. Searches file contents for
a regular expression, returning matching lines.

pattern: String

Regular expression to search for.

path: String

Optional directory root to search under. Defaults to the
runner's working directory.



class BetaManagedAgentsAgentToolset20260401Params { type, configs, default\_config } 

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

type: :agent\_toolset\_20260401



configs: Array[[BetaManagedAgentsAgentToolConfigParams](api/beta.md) { name, enabled, permission\_policy } ]

Per-tool configuration overrides.



name: :bash | :edit | :read | 5 more

Built-in agent tool identifier.

One of the following:

:bash

:edit

:read

:write

:glob

:grep

:web\_fetch

:web\_search

enabled: bool

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfigParams](api/beta.md) { enabled, permission\_policy } 

Default configuration for all tools in a toolset.

enabled: bool

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask



class BetaManagedAgentsAgentToolset20260401ReadInput { file\_path, view\_range } 

Input payload for the `read` tool. Reads file contents
relative to the runner's working directory (or absolute when
the runner permits).

file\_path: String

Path of the file to read.

view\_range: Array[Integer]

Optional `[start_line, end_line]` 1-indexed inclusive
range. When omitted the entire file is returned.
`end_line` of 0 or negative means "to end of file".



class BetaManagedAgentsAgentToolset20260401WriteInput { content, file\_path } 

Input payload for the `write` tool. Writes (overwriting) the
entire file contents.

content: String

Full file contents to write.

file\_path: String

Path of the file to write.



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask



class BetaManagedAgentsAnthropicSkill { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: String

type: :anthropic

version: String



class BetaManagedAgentsAnthropicSkillParams { skill\_id, type, version } 

An Anthropic-managed skill.

skill\_id: String

Identifier of the Anthropic skill (e.g., "xlsx").

type: :anthropic

version: String

Version to pin. Defaults to latest if omitted.



class BetaManagedAgentsCustomSkill { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: String

type: :custom

version: String



class BetaManagedAgentsCustomSkillParams { skill\_id, type, version } 

A user-created custom skill.

skill\_id: String

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

type: :custom

version: String

Version to pin. Defaults to latest if omitted.



class BetaManagedAgentsCustomTool { description, input\_schema, name, type } 

A custom tool as returned in API responses.

description: String



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md) { type, properties, required } 

JSON Schema for custom tool input parameters.

type: :object

properties: Hash[Symbol, untyped]

required: Array[String]

name: String

type: :custom



class BetaManagedAgentsCustomToolInputSchema { type, properties, required } 

JSON Schema for custom tool input parameters.

type: :object

properties: Hash[Symbol, untyped]

required: Array[String]



class BetaManagedAgentsCustomToolParams { description, input\_schema, name, type } 

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

description: String

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md) { type, properties, required } 

JSON Schema for custom tool input parameters.

type: :object

properties: Hash[Symbol, untyped]

required: Array[String]

name: String

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

type: :custom



class BetaManagedAgentsMCPServerURLDefinition { name, type, url } 

URL-based MCP server connection as returned in API responses.

name: String

type: :url

url: String



class BetaManagedAgentsMCPToolConfig { enabled, name, permission\_policy } 

Resolved configuration for a specific MCP tool.

enabled: bool

name: String



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask



class BetaManagedAgentsMCPToolConfigParams { name, enabled, permission\_policy } 

Configuration override for a specific MCP tool.

name: String

Name of the MCP tool to configure. 1-128 characters.

enabled: bool

Whether this tool is enabled. Overrides the `default_config` setting.



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask



class BetaManagedAgentsMCPToolset { configs, default\_config, mcp\_server\_name, type } 



configs: Array[[BetaManagedAgentsMCPToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool

name: String



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: bool



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask

mcp\_server\_name: String

type: :mcp\_toolset



class BetaManagedAgentsMCPToolsetDefaultConfig { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: bool



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask



class BetaManagedAgentsMCPToolsetDefaultConfigParams { enabled, permission\_policy } 

Default configuration for all tools from an MCP server.

enabled: bool

Whether tools are enabled by default. Defaults to true if not specified.



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask



class BetaManagedAgentsMCPToolsetParams { mcp\_server\_name, type, configs, default\_config } 

Configuration for tools from an MCP server defined in `mcp_servers`.

mcp\_server\_name: String

Name of the MCP server. Must match a server name from the mcp\_servers array. 1-255 characters.

type: :mcp\_toolset



configs: Array[[BetaManagedAgentsMCPToolConfigParams](api/beta.md) { name, enabled, permission\_policy } ]

Per-tool configuration overrides.

name: String

Name of the MCP tool to configure. 1-128 characters.

enabled: bool

Whether this tool is enabled. Overrides the `default_config` setting.



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfigParams](api/beta.md) { enabled, permission\_policy } 

Default configuration for all tools from an MCP server.

enabled: bool

Whether tools are enabled by default. Defaults to true if not specified.



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask



BetaManagedAgentsModel = :"claude-fable-5" | :"claude-opus-4-8" | :"claude-opus-4-7" | 8 more | String

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



BetaManagedAgentsModel = :"claude-fable-5" | :"claude-opus-4-8" | :"claude-opus-4-7" | 8 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

String = String



class BetaManagedAgentsModelConfig { id, speed } 

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



BetaManagedAgentsModel = :"claude-fable-5" | :"claude-opus-4-8" | :"claude-opus-4-7" | 8 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

String = String



speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

:standard

:fast



class BetaManagedAgentsModelConfigParams { id, speed } 

An object that defines additional configuration control over model use



id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



BetaManagedAgentsModel = :"claude-fable-5" | :"claude-opus-4-8" | :"claude-opus-4-7" | 8 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

String = String



speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

:standard

:fast



class BetaManagedAgentsMultiagentCoordinator { agents, type } 

Resolved coordinator topology with a concrete agent roster.



agents: Array[[BetaManagedAgentsAgentReference](api/beta.md) { id, type, version } ]

Agents the coordinator may spawn as session threads, each resolved to a specific version.

id: String

type: :agent

version: Integer

type: :coordinator



class BetaManagedAgentsMultiagentCoordinatorParams { agents, type } 

A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.



agents: Array[[BetaManagedAgentsMultiagentRosterEntryParams](api/beta.md)]

Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

One of the following:

String = String



class BetaManagedAgentsAgentParams { id, type, version } 

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: String

The `agent` ID.

type: :agent

version: Integer

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.



class BetaManagedAgentsMultiagentSelfParams { type } 

Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

type: :self

type: :coordinator



class BetaManagedAgentsMultiagentSelfParams { type } 

Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

type: :self



class BetaManagedAgentsSessionThreadAgent { id, description, mcp\_servers, 7 more } 

Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

id: String

description: String



mcp\_servers: Array[[BetaManagedAgentsMCPServerURLDefinition](api/beta.md) { name, type, url } ]

name: String

type: :url

url: String



model: [BetaManagedAgentsModelConfig](api/beta.md) { id, speed } 

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



BetaManagedAgentsModel = :"claude-fable-5" | :"claude-opus-4-8" | :"claude-opus-4-7" | 8 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

String = String



speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

:standard

:fast

name: String



skills: Array[[BetaManagedAgentsAnthropicSkill](api/beta.md) { skill\_id, type, version }  | [BetaManagedAgentsCustomSkill](api/beta.md) { skill\_id, type, version } ]

One of the following:



class BetaManagedAgentsAnthropicSkill { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: String

type: :anthropic

version: String



class BetaManagedAgentsCustomSkill { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: String

type: :custom

version: String

system\_: String



tools: Array[[BetaManagedAgentsAgentToolset20260401](api/beta.md) { configs, default\_config, type }  | [BetaManagedAgentsMCPToolset](api/beta.md) { configs, default\_config, mcp\_server\_name, type }  | [BetaManagedAgentsCustomTool](api/beta.md) { description, input\_schema, name, type } ]

One of the following:



class BetaManagedAgentsAgentToolset20260401 { configs, default\_config, type } 



configs: Array[[BetaManagedAgentsAgentToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool



name: :bash | :edit | :read | 5 more

Built-in agent tool identifier.

One of the following:

:bash

:edit

:read

:write

:glob

:grep

:web\_fetch

:web\_search



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: bool



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask

type: :agent\_toolset\_20260401



class BetaManagedAgentsMCPToolset { configs, default\_config, mcp\_server\_name, type } 



configs: Array[[BetaManagedAgentsMCPToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool

name: String



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: bool



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy { type } 

Tool calls are automatically approved without user confirmation.

type: :always\_allow



class BetaManagedAgentsAlwaysAskPolicy { type } 

Tool calls require user confirmation before execution.

type: :always\_ask

mcp\_server\_name: String

type: :mcp\_toolset



class BetaManagedAgentsCustomTool { description, input\_schema, name, type } 

A custom tool as returned in API responses.

description: String



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md) { type, properties, required } 

JSON Schema for custom tool input parameters.

type: :object

properties: Hash[Symbol, untyped]

required: Array[String]

name: String

type: :custom

type: :agent

version: Integer



BetaManagedAgentsSkillParams = [BetaManagedAgentsAnthropicSkillParams](api/beta.md) { skill\_id, type, version }  | [BetaManagedAgentsCustomSkillParams](api/beta.md) { skill\_id, type, version } 

Skill to load in the session container.

One of the following:



class BetaManagedAgentsAnthropicSkillParams { skill\_id, type, version } 

An Anthropic-managed skill.

skill\_id: String

Identifier of the Anthropic skill (e.g., "xlsx").

type: :anthropic

version: String

Version to pin. Defaults to latest if omitted.



class BetaManagedAgentsCustomSkillParams { skill\_id, type, version } 

A user-created custom skill.

skill\_id: String

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

type: :custom

version: String

Version to pin. Defaults to latest if omitted.



class BetaManagedAgentsURLMCPServerParams { name, type, url } 

URL-based MCP server connection.

name: String

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

type: :url

url: String

Endpoint URL for the MCP server.

#### AgentsVersions

##### [List Agent Versions](api/beta/agents/versions/list.md)

beta.agents.versions.list(agent\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsAgent](api/beta.md) { id, archived\_at, created\_at, 12 more } >

GET/v1/agents/{agent\_id}/versions

---

*Copyright © Anthropic. All rights reserved.*
