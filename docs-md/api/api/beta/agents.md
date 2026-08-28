# Agents

Copy page



cURL

# Agents

##### [Create Agent](api/http/beta/agents/create.md)

POST/v1/agents

##### [List Agents](api/http/beta/agents/list.md)

GET/v1/agents

##### [Get Agent](api/http/beta/agents/retrieve.md)

GET/v1/agents/{agent\_id}

##### [Update Agent](api/http/beta/agents/update.md)

POST/v1/agents/{agent\_id}

##### [Archive Agent](api/http/beta/agents/archive.md)

POST/v1/agents/{agent\_id}/archive

##### Models



BetaManagedAgentsAdvisor object{ model, type }

Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

model: string

The advisor model id.

type: "advisor"



BetaManagedAgentsAgent object{ id, archived\_at, created\_at, 12 more }

A Managed Agents `agent`.



BetaManagedAgentsAgentReference object{ id, type, version }

A resolved agent reference with a concrete version.

id: string

type: "agent"



version: number

formatint32



BetaManagedAgentsAgentToolConfig = [BetaManagedAgentsBashToolConfig](api/http/beta/agents.md) { enabled, name, permission\_policy, type } or [BetaManagedAgentsEditToolConfig](api/http/beta/agents.md) { enabled, name, permission\_policy, type } or [BetaManagedAgentsReadToolConfig](api/http/beta/agents.md) { enabled, name, permission\_policy, type } or 5 more

Configuration for a specific agent tool.

One of the following:



BetaManagedAgentsAgentToolConfigParams = [BetaManagedAgentsBashToolConfigParams](api/http/beta/agents.md) { name, enabled, permission\_policy, type } or [BetaManagedAgentsEditToolConfigParams](api/http/beta/agents.md) { name, enabled, permission\_policy, type } or [BetaManagedAgentsReadToolConfigParams](api/http/beta/agents.md) { name, enabled, permission\_policy, type } or 5 more

Configuration override for a specific tool within a toolset.

One of the following:



BetaManagedAgentsAgentToolsetDefaultConfig object{ enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/http/beta/agents.md) { type } or [BetaManagedAgentsAlwaysAskPolicy](api/http/beta/agents.md) { type }

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object{ type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object{ type }

Tool calls require user confirmation before execution.

type: "always\_ask"



BetaManagedAgentsAgentToolsetDefaultConfigParams object{ enabled, permission\_policy }

Default configuration for all tools in a toolset.

enabled: optional boolean or null

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.



permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/http/beta/agents.md) { type } or [BetaManagedAgentsAlwaysAskPolicy](api/http/beta/agents.md) { type } or null

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object{ type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object{ type }

Tool calls require user confirmation before execution.

type: "always\_ask"



BetaManagedAgentsAgentToolset20260401 object{ configs, default\_config, type }



BetaManagedAgentsAgentToolset20260401BashInput object{ command, restart, timeout\_ms }

Input payload for the `bash` tool of the
`agent_toolset_20260401` toolset. All fields are optional;
a normal invocation supplies `command`, while `restart=true`
(with no `command`) reboots the runner-side bash session.

command: optional string

Shell command to execute. Omit only when `restart` is true.

restart: optional boolean

When true, restart the persistent bash session instead of
running a command. Subsequent calls without `restart` will
run against the fresh session.



timeout\_ms: optional number

Per-call timeout in milliseconds. Defaults to the
runner-wide tool timeout when omitted or zero.

minimum0



BetaManagedAgentsAgentToolset20260401EditInput object{ file\_path, new\_string, old\_string, replace\_all }

Input payload for the `edit` tool. Performs a string
replacement in the named file; by default `old_string` must
occur exactly once.

file\_path: string

Path of the file to edit.

new\_string: string

Replacement text.

old\_string: string

Substring to find and replace.

replace\_all: optional boolean

When true, replace every occurrence of `old_string`
instead of requiring a unique match.



BetaManagedAgentsAgentToolset20260401GlobInput object{ pattern, path }

Input payload for the `glob` tool. Returns paths matching a
doublestar glob pattern, newest first.

pattern: string

Doublestar glob pattern (e.g. `**/*.go`). Absolute patterns
are only permitted when the runner is configured to allow
them.

path: optional string

Optional directory root to search under. Defaults to the
runner's working directory.



BetaManagedAgentsAgentToolset20260401GrepInput object{ pattern, path }

Input payload for the `grep` tool. Searches file contents for
a regular expression, returning matching lines.

pattern: string

Regular expression to search for.

path: optional string

Optional directory root to search under. Defaults to the
runner's working directory.



BetaManagedAgentsAgentToolset20260401Params object{ type, configs, default\_config }

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.



BetaManagedAgentsAgentToolset20260401ReadInput object{ file\_path, view\_range }

Input payload for the `read` tool. Reads file contents
relative to the runner's working directory (or absolute when
the runner permits).

file\_path: string

Path of the file to read.



view\_range: optional array of number

Optional `[start_line, end_line]` 1-indexed inclusive
range. When omitted the entire file is returned.
`end_line` of 0 or negative means "to end of file".

minItems2

maxItems2



BetaManagedAgentsAgentToolset20260401WriteInput object{ content, file\_path }

Input payload for the `write` tool. Writes (overwriting) the
entire file contents.

content: string

Full file contents to write.

file\_path: string

Path of the file to write.



BetaManagedAgentsAlwaysAllowPolicy object{ type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object{ type }

Tool calls require user confirmation before execution.

type: "always\_ask"



BetaManagedAgentsAnthropicSkill object{ skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string



BetaManagedAgentsAnthropicSkillParams object{ skill\_id, type, version }

An Anthropic-managed skill.



skill\_id: string

Identifier of the Anthropic skill (e.g., "xlsx").

minLength1

maxLength64

type: "anthropic"



version: optional string or null

Version to pin. Defaults to latest if omitted.

minLength1

maxLength64



BetaManagedAgentsBashToolConfig object{ enabled, name, permission\_policy, type }

Configuration for the bash tool.



BetaManagedAgentsBashToolConfigParams object{ name, enabled, permission\_policy, type }

Configuration override for the bash tool.



BetaManagedAgentsCustomSkill object{ skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string



BetaManagedAgentsCustomSkillParams object{ skill\_id, type, version }

A user-created custom skill.



skill\_id: string

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

minLength1

maxLength64

type: "custom"



version: optional string or null

Version to pin. Defaults to latest if omitted.

minLength1

maxLength64



BetaManagedAgentsCustomTool object{ description, input\_schema, name, type }

A custom tool as returned in API responses.

description: string



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/http/beta/agents.md) { type, properties, required }

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown] or null

required: optional array of string or null

name: string

type: "custom"



BetaManagedAgentsCustomToolInputSchema object{ type, properties, required }

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown] or null

required: optional array of string or null



BetaManagedAgentsCustomToolParams object{ description, input\_schema, name, type }

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.



description: string

Description of what the tool does, shown to the agent to help it decide when to use the tool.

minLength1



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/http/beta/agents.md) { type, properties, required }

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown] or null

required: optional array of string or null



name: string

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

minLength1

maxLength128

type: "custom"



BetaManagedAgentsEditToolConfig object{ enabled, name, permission\_policy, type }

Configuration for the edit tool.



BetaManagedAgentsEditToolConfigParams object{ name, enabled, permission\_policy, type }

Configuration override for the edit tool.



BetaManagedAgentsEffortHigh object{ type }

High effort. Favors reasoning depth.

type: "high"



BetaManagedAgentsEffortLow object{ type }

Low effort. Favors latency over reasoning depth.

type: "low"



BetaManagedAgentsEffortMax object{ type }

Maximum effort. Favors reasoning depth over latency.

type: "max"



BetaManagedAgentsEffortMedium object{ type }

Medium effort. Balances latency and reasoning depth.

type: "medium"



BetaManagedAgentsEffortXhigh object{ type }

Extra-high effort. Not all models accept this level.

type: "xhigh"



BetaManagedAgentsGlobToolConfig object{ enabled, name, permission\_policy, type }

Configuration for the glob tool.



BetaManagedAgentsGlobToolConfigParams object{ name, enabled, permission\_policy, type }

Configuration override for the glob tool.



BetaManagedAgentsGrepToolConfig object{ enabled, name, permission\_policy, type }

Configuration for the grep tool.



BetaManagedAgentsGrepToolConfigParams object{ name, enabled, permission\_policy, type }

Configuration override for the grep tool.



BetaManagedAgentsMCPServerURLDefinition object{ name, type, url }

URL-based MCP server connection as returned in API responses.

name: string

type: "url"

url: string



BetaManagedAgentsMCPToolConfig object{ enabled, name, permission\_policy }

Resolved configuration for a specific MCP tool.

enabled: boolean

name: string



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/http/beta/agents.md) { type } or [BetaManagedAgentsAlwaysAskPolicy](api/http/beta/agents.md) { type }

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object{ type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object{ type }

Tool calls require user confirmation before execution.

type: "always\_ask"



BetaManagedAgentsMCPToolConfigParams object{ name, enabled, permission\_policy }

Configuration override for a specific MCP tool.



BetaManagedAgentsMCPToolset object{ configs, default\_config, mcp\_server\_name, type }



BetaManagedAgentsMCPToolsetDefaultConfig object{ enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/http/beta/agents.md) { type } or [BetaManagedAgentsAlwaysAskPolicy](api/http/beta/agents.md) { type }

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object{ type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object{ type }

Tool calls require user confirmation before execution.

type: "always\_ask"



BetaManagedAgentsMCPToolsetDefaultConfigParams object{ enabled, permission\_policy }

Default configuration for all tools from an MCP server.

enabled: optional boolean or null

Whether tools are enabled by default. Defaults to true if not specified.



permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/http/beta/agents.md) { type } or [BetaManagedAgentsAlwaysAskPolicy](api/http/beta/agents.md) { type } or null

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object{ type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object{ type }

Tool calls require user confirmation before execution.

type: "always\_ask"



BetaManagedAgentsMCPToolsetParams object{ mcp\_server\_name, type, configs, default\_config }

Configuration for tools from an MCP server defined in `mcp_servers`.



BetaManagedAgentsModel = "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



BetaManagedAgentsModelConfig object{ id, effort, inference\_geo, speed }

Model identifier and configuration.



BetaManagedAgentsModelConfigParams object{ id, effort, inference\_geo, speed }

An object that defines additional configuration control over model use



BetaManagedAgentsMultiagentCoordinator object{ agents, type }

Resolved coordinator topology with a concrete agent roster.



BetaManagedAgentsMultiagentCoordinatorParams object{ agents, type }

A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.



BetaManagedAgentsMultiagentSelfParams object{ type }

Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

type: "self"



BetaManagedAgentsReadToolConfig object{ enabled, name, permission\_policy, type }

Configuration for the read tool.



BetaManagedAgentsReadToolConfigParams object{ name, enabled, permission\_policy, type }

Configuration override for the read tool.



BetaManagedAgentsSessionThreadAgent object{ id, description, mcp\_servers, 7 more }

Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.



BetaManagedAgentsSkillParams = [BetaManagedAgentsAnthropicSkillParams](api/http/beta/agents.md) { skill\_id, type, version } or [BetaManagedAgentsCustomSkillParams](api/http/beta/agents.md) { skill\_id, type, version }

Skill to load in the session container.

One of the following:



BetaManagedAgentsURLMCPServerParams object{ name, type, url }

URL-based MCP server connection.



name: string

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

minLength1

maxLength255

type: "url"



url: string

Endpoint URL for the MCP server.

maxLength2048



BetaManagedAgentsUserLocation object{ type, city, country, 2 more }

Approximate user location for search result localization.

type: "approximate"

Location precision. Only "approximate" is supported.



city: optional string or null

City name.

minLength1

maxLength255

country: optional string or null

Two-letter ISO 3166-1 country code, uppercase.



region: optional string or null

Region or state name.

minLength1

maxLength255



timezone: optional string or null

IANA timezone identifier, e.g. "America/Los\_Angeles".

minLength1

maxLength255



BetaManagedAgentsWebFetchToolConfig object{ enabled, name, permission\_policy, 4 more }

Configuration for the web\_fetch tool.



BetaManagedAgentsWebFetchToolConfigParams object{ name, allowed\_domains, blocked\_domains, 4 more }

Configuration override for the web\_fetch tool.



BetaManagedAgentsWebSearchToolConfig object{ enabled, name, permission\_policy, 4 more }

Configuration for the web\_search tool.



BetaManagedAgentsWebSearchToolConfigParams object{ name, allowed\_domains, blocked\_domains, 4 more }

Configuration override for the web\_search tool.



BetaManagedAgentsWriteToolConfig object{ enabled, name, permission\_policy, type }

Configuration for the write tool.



BetaManagedAgentsWriteToolConfigParams object{ name, enabled, permission\_policy, type }

Configuration override for the write tool.

#### Agents[Versions](api/http/beta/agents/versions.md)

##### [List Agent Versions](api/http/beta/agents/versions/list.md)

GET/v1/agents/{agent\_id}/versions

---

*Copyright © Anthropic. All rights reserved.*
