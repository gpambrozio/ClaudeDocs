# Agents

Copy page



CLI

# Agents

##### [Create Agent](api/beta/agents/create.md)

$ ant beta:agents create

POST/v1/agents

##### [List Agents](api/beta/agents/list.md)

$ ant beta:agents list

GET/v1/agents

##### [Get Agent](api/beta/agents/retrieve.md)

$ ant beta:agents retrieve

GET/v1/agents/{agent\_id}

##### [Update Agent](api/beta/agents/update.md)

$ ant beta:agents update

POST/v1/agents/{agent\_id}

##### [Archive Agent](api/beta/agents/archive.md)

$ ant beta:agents archive

POST/v1/agents/{agent\_id}/archive

##### ModelsExpand Collapse



beta\_managed\_agents\_agent: object { id, archived\_at, created\_at, 12 more } 

A Managed Agents `agent`.

id: string

archived\_at: string

A timestamp in RFC 3339 format

created\_at: string

A timestamp in RFC 3339 format

description: string



mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta.md) { name, type, url } 

name: string



type: "url"

"url"

url: string

metadata: map[string]

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

Resolved coordinator topology with a concrete agent roster.



agents: array of [BetaManagedAgentsAgentReference](api/beta.md) { id, type, version } 

Agents the coordinator may spawn as session threads, each resolved to a specific version.

id: string



type: "agent"

"agent"

version: number



type: "coordinator"

"coordinator"

name: string



skills: array of [BetaManagedAgentsAnthropicSkill](api/beta.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta.md) { skill\_id, type, version } 

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

tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta.md) { description, input\_schema, name, type } 



beta\_managed\_agents\_agent\_toolset20260401: object { configs, default\_config, type } 



configs: array of [BetaManagedAgentsAgentToolConfig](api/beta.md) { enabled, name, permission\_policy } 

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

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

configs: array of [BetaManagedAgentsMCPToolConfig](api/beta.md) { enabled, name, permission\_policy } 

enabled: boolean

name: string



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

updated\_at: string

A timestamp in RFC 3339 format

version: number

The agent's current version. Starts at 1 and increments when the agent is modified.



beta\_managed\_agents\_agent\_reference: object { id, type, version } 

A resolved agent reference with a concrete version.

id: string



type: "agent"

"agent"

version: number



beta\_managed\_agents\_agent\_tool\_config: object { enabled, name, permission\_policy } 

Configuration for a specific agent tool.

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

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

beta\_managed\_agents\_agent\_tool\_config\_params: object { name, enabled, permission\_policy } 

Configuration override for a specific tool within a toolset.

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

permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

beta\_managed\_agents\_agent\_toolset\_default\_config: object { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

beta\_managed\_agents\_agent\_toolset\_default\_config\_params: object { enabled, permission\_policy } 

Default configuration for all tools in a toolset.

enabled: optional boolean

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.



permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

beta\_managed\_agents\_agent\_toolset20260401: object { configs, default\_config, type } 



configs: array of [BetaManagedAgentsAgentToolConfig](api/beta.md) { enabled, name, permission\_policy } 

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

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

beta\_managed\_agents\_agent\_toolset20260401\_bash\_input: object { command, restart, timeout\_ms } 

Input payload for the `bash` tool of the
`agent_toolset_20260401` toolset. All fields are optional;
a normal invocation supplies `command`, while `restart=true`
(with no `command`) reboots the runner-side bash session.

command: optional string

Shell command to execute. Omit only when `restart` is true.

restart: optional boolean

When true, restart the persistent bash session instead of
running a command. Subsequent calls without `restart` will
run against the fresh session.

timeout\_ms: optional number

Per-call timeout in milliseconds. Defaults to the
runner-wide tool timeout when omitted or zero.



beta\_managed\_agents\_agent\_toolset20260401\_edit\_input: object { file\_path, new\_string, old\_string, replace\_all } 

Input payload for the `edit` tool. Performs a string
replacement in the named file; by default `old_string` must
occur exactly once.

file\_path: string

Path of the file to edit.

new\_string: string

Replacement text.

old\_string: string

Substring to find and replace.

replace\_all: optional boolean

When true, replace every occurrence of `old_string`
instead of requiring a unique match.



beta\_managed\_agents\_agent\_toolset20260401\_glob\_input: object { pattern, path } 

Input payload for the `glob` tool. Returns paths matching a
doublestar glob pattern, newest first.

pattern: string

Doublestar glob pattern (e.g. `**/*.go`). Absolute patterns
are only permitted when the runner is configured to allow
them.

path: optional string

Optional directory root to search under. Defaults to the
runner's working directory.



beta\_managed\_agents\_agent\_toolset20260401\_grep\_input: object { pattern, path } 

Input payload for the `grep` tool. Searches file contents for
a regular expression, returning matching lines.

pattern: string

Regular expression to search for.

path: optional string

Optional directory root to search under. Defaults to the
runner's working directory.



beta\_managed\_agents\_agent\_toolset20260401\_params: object { type, configs, default\_config } 

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.



type: "agent\_toolset\_20260401"

"agent\_toolset\_20260401"



configs: optional array of [BetaManagedAgentsAgentToolConfigParams](api/beta.md) { name, enabled, permission\_policy } 

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

permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

beta\_managed\_agents\_agent\_toolset20260401\_read\_input: object { file\_path, view\_range } 

Input payload for the `read` tool. Reads file contents
relative to the runner's working directory (or absolute when
the runner permits).

file\_path: string

Path of the file to read.

view\_range: optional array of number

Optional `[start_line, end_line]` 1-indexed inclusive
range. When omitted the entire file is returned.
`end_line` of 0 or negative means "to end of file".



beta\_managed\_agents\_agent\_toolset20260401\_write\_input: object { content, file\_path } 

Input payload for the `write` tool. Writes (overwriting) the
entire file contents.

content: string

Full file contents to write.

file\_path: string

Path of the file to write.

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

beta\_managed\_agents\_anthropic\_skill: object { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: string



type: "anthropic"

"anthropic"

version: string



beta\_managed\_agents\_anthropic\_skill\_params: object { skill\_id, type, version } 

An Anthropic-managed skill.

skill\_id: string

Identifier of the Anthropic skill (e.g., "xlsx").



type: "anthropic"

"anthropic"

version: optional string

Version to pin. Defaults to latest if omitted.



beta\_managed\_agents\_custom\_skill: object { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: string



type: "custom"

"custom"

version: string



beta\_managed\_agents\_custom\_skill\_params: object { skill\_id, type, version } 

A user-created custom skill.

skill\_id: string

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").



type: "custom"

"custom"

version: optional string

Version to pin. Defaults to latest if omitted.

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

beta\_managed\_agents\_custom\_tool\_input\_schema: object { type, properties, required } 

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown]

required: optional array of string

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

beta\_managed\_agents\_mcp\_server\_url\_definition: object { name, type, url } 

URL-based MCP server connection as returned in API responses.

name: string



type: "url"

"url"

url: string



beta\_managed\_agents\_mcp\_tool\_config: object { enabled, name, permission\_policy } 

Resolved configuration for a specific MCP tool.

enabled: boolean

name: string



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

beta\_managed\_agents\_mcp\_tool\_config\_params: object { name, enabled, permission\_policy } 

Configuration override for a specific MCP tool.

name: string

Name of the MCP tool to configure. 1-128 characters.

enabled: optional boolean

Whether this tool is enabled. Overrides the `default_config` setting.



permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

beta\_managed\_agents\_mcp\_toolset: object { configs, default\_config, mcp\_server\_name, type } 



configs: array of [BetaManagedAgentsMCPToolConfig](api/beta.md) { enabled, name, permission\_policy } 

enabled: boolean

name: string



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

beta\_managed\_agents\_mcp\_toolset\_default\_config: object { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

beta\_managed\_agents\_mcp\_toolset\_default\_config\_params: object { enabled, permission\_policy } 

Default configuration for all tools from an MCP server.

enabled: optional boolean

Whether tools are enabled by default. Defaults to true if not specified.



permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

configs: optional array of [BetaManagedAgentsMCPToolConfigParams](api/beta.md) { name, enabled, permission\_policy } 

Per-tool configuration overrides.

name: string

Name of the MCP tool to configure. 1-128 characters.

enabled: optional boolean

Whether this tool is enabled. Overrides the `default_config` setting.



permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

beta\_managed\_agents\_model\_config: object { id, speed } 

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

beta\_managed\_agents\_model\_config\_params: object { id, speed } 

An object that defines additional configuration control over model use

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

beta\_managed\_agents\_multiagent\_coordinator: object { agents, type } 

Resolved coordinator topology with a concrete agent roster.



agents: array of [BetaManagedAgentsAgentReference](api/beta.md) { id, type, version } 

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

beta\_managed\_agents\_multiagent\_coordinator\_params: object { agents, type } 

A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.



agents: array of [BetaManagedAgentsMultiagentRosterEntryParams](api/beta.md)

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

beta\_managed\_agents\_multiagent\_self\_params: object { type } 

Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.



type: "self"

"self"



beta\_managed\_agents\_session\_thread\_agent: object { id, description, mcp\_servers, 7 more } 

Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

id: string

description: string



mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta.md) { name, type, url } 

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

skills: array of [BetaManagedAgentsAnthropicSkill](api/beta.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta.md) { skill\_id, type, version } 

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

tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta.md) { description, input\_schema, name, type } 



beta\_managed\_agents\_agent\_toolset20260401: object { configs, default\_config, type } 



configs: array of [BetaManagedAgentsAgentToolConfig](api/beta.md) { enabled, name, permission\_policy } 

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

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

configs: array of [BetaManagedAgentsMCPToolConfig](api/beta.md) { enabled, name, permission\_policy } 

enabled: boolean

name: string



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

beta\_managed\_agents\_skill\_params: [BetaManagedAgentsAnthropicSkillParams](api/beta.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkillParams](api/beta.md) { skill\_id, type, version } 

Skill to load in the session container.



beta\_managed\_agents\_anthropic\_skill\_params: object { skill\_id, type, version } 

An Anthropic-managed skill.

skill\_id: string

Identifier of the Anthropic skill (e.g., "xlsx").



type: "anthropic"

"anthropic"

version: optional string

Version to pin. Defaults to latest if omitted.



beta\_managed\_agents\_custom\_skill\_params: object { skill\_id, type, version } 

A user-created custom skill.

skill\_id: string

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").



type: "custom"

"custom"

version: optional string

Version to pin. Defaults to latest if omitted.



beta\_managed\_agents\_url\_mcp\_server\_params: object { name, type, url } 

URL-based MCP server connection.

name: string

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.



type: "url"

"url"

url: string

Endpoint URL for the MCP server.

#### AgentsVersions

##### [List Agent Versions](api/beta/agents/versions/list.md)

$ ant beta:agents:versions list

GET/v1/agents/{agent\_id}/versions

---

*Copyright © Anthropic. All rights reserved.*
