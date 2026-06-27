# Create Agent

Copy page



Ruby

# Create Agent

beta.agents.create(\*\*kwargs) -> [BetaManagedAgentsAgent](api/beta/agents.md) { id, archived\_at, created\_at, 12 more }

POST/v1/agents

Create Agent

##### ParametersExpand Collapse



model: [BetaManagedAgentsModel](api/beta/agents.md) | [BetaManagedAgentsModelConfigParams](api/beta/agents.md) { id, speed } 

Model identifier. Accepts the [model string](about-claude/models/overview.md), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control

One of the following:

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

class BetaManagedAgentsModelConfigParams { id, speed } 

An object that defines additional configuration control over model use



id: [BetaManagedAgentsModel](api/beta/agents.md)

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

Human-readable name for the agent.

description: String

Description of what the agent does.



mcp\_servers: Array[[BetaManagedAgentsURLMCPServerParams](api/beta/agents.md) { name, type, url } ]

MCP servers this agent connects to. Maximum 20. Names must be unique within the array. Every server must be referenced by an `mcp_toolset` in `tools`; unreferenced servers are rejected. See the [MCP connector guide](managed-agents/mcp-connector.md).

name: String

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

type: :url

url: String

Endpoint URL for the MCP server.

metadata: Hash[Symbol, String]

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.



multiagent: [BetaManagedAgentsMultiagentParams](api/beta/sessions.md) { agents, type } 

A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.



agents: Array[[BetaManagedAgentsMultiagentRosterEntryParams](api/beta/sessions.md)]

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

skills: Array[[BetaManagedAgentsSkillParams](api/beta/agents.md)]

Skills available to the agent.

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

system\_: String

System prompt for the agent.



tools: Array[[BetaManagedAgentsAgentToolset20260401Params](api/beta/agents.md) { type, configs, default\_config }  | [BetaManagedAgentsMCPToolsetParams](api/beta/agents.md) { mcp\_server\_name, type, configs, default\_config }  | [BetaManagedAgentsCustomToolParams](api/beta/agents.md) { description, input\_schema, name, type } ]

Tool configurations available to the agent. Maximum of 128 tools across all toolsets allowed.

One of the following:



class BetaManagedAgentsAgentToolset20260401Params { type, configs, default\_config } 

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

type: :agent\_toolset\_20260401



configs: Array[[BetaManagedAgentsAgentToolConfigParams](api/beta/agents.md) { name, enabled, permission\_policy } ]

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

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

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

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfigParams](api/beta/agents.md) { enabled, permission\_policy } 

Default configuration for all tools in a toolset.

enabled: bool

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

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

configs: Array[[BetaManagedAgentsMCPToolConfigParams](api/beta/agents.md) { name, enabled, permission\_policy } ]

Per-tool configuration overrides.

name: String

Name of the MCP tool to configure. 1-128 characters.

enabled: bool

Whether this tool is enabled. Overrides the `default_config` setting.



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

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

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfigParams](api/beta/agents.md) { enabled, permission\_policy } 

Default configuration for all tools from an MCP server.

enabled: bool

Whether tools are enabled by default. Defaults to true if not specified.



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

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

class BetaManagedAgentsCustomToolParams { description, input\_schema, name, type } 

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

description: String

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) { type, properties, required } 

JSON Schema for custom tool input parameters.

type: :object

properties: Hash[Symbol, untyped]

required: Array[String]

name: String

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

type: :custom



betas: Array[[AnthropicBeta](api/beta.md)]

Optional header to specify the beta version(s) you want to use.

One of the following:

String = String



AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 25 more

One of the following:

:"message-batches-2024-09-24"

:"prompt-caching-2024-07-31"

:"computer-use-2024-10-22"

:"computer-use-2025-01-24"

:"pdfs-2024-09-25"

:"token-counting-2024-11-01"

:"token-efficient-tools-2025-02-19"

:"output-128k-2025-02-19"

:"files-api-2025-04-14"

:"mcp-client-2025-04-04"

:"mcp-client-2025-11-20"

:"dev-full-thinking-2025-05-14"

:"interleaved-thinking-2025-05-14"

:"code-execution-2025-05-22"

:"extended-cache-ttl-2025-04-11"

:"context-1m-2025-08-07"

:"context-management-2025-06-27"

:"model-context-window-exceeded-2025-08-26"

:"skills-2025-10-02"

:"fast-mode-2026-02-01"

:"output-300k-2026-03-24"

:"user-profiles-2026-03-24"

:"advisor-tool-2026-03-01"

:"managed-agents-2026-04-01"

:"cache-diagnosis-2026-04-07"

:"thinking-token-count-2026-05-13"

:"server-side-fallback-2026-06-01"

:"fallback-credit-2026-06-01"

##### ReturnsExpand Collapse

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

mcp\_servers: Array[[BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md) { name, type, url } ]

name: String

type: :url

url: String

metadata: Hash[Symbol, String]



model: [BetaManagedAgentsModelConfig](api/beta/agents.md) { id, speed } 

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta/agents.md)

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

multiagent: [BetaManagedAgentsMultiagent](api/beta/sessions.md) { agents, type } 

Resolved coordinator topology with a concrete agent roster.



agents: Array[[BetaManagedAgentsAgentReference](api/beta/agents.md) { id, type, version } ]

Agents the coordinator may spawn as session threads, each resolved to a specific version.

id: String

type: :agent

version: Integer

type: :coordinator

name: String



skills: Array[[BetaManagedAgentsAnthropicSkill](api/beta/agents.md) { skill\_id, type, version }  | [BetaManagedAgentsCustomSkill](api/beta/agents.md) { skill\_id, type, version } ]

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

tools: Array[[BetaManagedAgentsAgentToolset20260401](api/beta/agents.md) { configs, default\_config, type }  | [BetaManagedAgentsMCPToolset](api/beta/agents.md) { configs, default\_config, mcp\_server\_name, type }  | [BetaManagedAgentsCustomTool](api/beta/agents.md) { description, input\_schema, name, type } ]

One of the following:



class BetaManagedAgentsAgentToolset20260401 { configs, default\_config, type } 



configs: Array[[BetaManagedAgentsAgentToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } ]

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

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

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

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: bool



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

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

configs: Array[[BetaManagedAgentsMCPToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } ]

enabled: bool

name: String



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

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

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta/agents.md) { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: bool



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

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

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) { type, properties, required } 

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

Create Agent

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_agent = anthropic.beta.agents.create(model: :"claude-sonnet-4-6", name: "My First Agent")

puts(beta_managed_agents_agent)
```

Response 200



```shiki
{
  "id": "agent_011CZkYpogX7uDKUyvBTophP",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "A general-purpose starter agent.",
  "mcp_servers": [
    {
      "name": "example-mcp",
      "type": "url",
      "url": "https://example-server.modelcontextprotocol.io/sse"
    }
  ],
  "metadata": {
    "foo": "bar"
  },
  "model": {
    "id": "claude-sonnet-4-6",
    "speed": "standard"
  },
  "multiagent": {
    "agents": [
      {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "type": "agent",
        "version": 1
      }
    ],
    "type": "coordinator"
  },
  "name": "My First Agent",
  "skills": [
    {
      "skill_id": "xlsx",
      "type": "anthropic",
      "version": "1"
    },
    {
      "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
      "type": "custom",
      "version": "2"
    }
  ],
  "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
  "tools": [
    {
      "configs": [
        {
          "enabled": true,
          "name": "bash",
          "permission_policy": {
            "type": "always_allow"
          }
        }
      ],
      "default_config": {
        "enabled": true,
        "permission_policy": {
          "type": "always_ask"
        }
      },
      "type": "agent_toolset_20260401"
    }
  ],
  "type": "agent",
  "updated_at": "2026-03-15T10:00:00Z",
  "version": 1
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "agent_011CZkYpogX7uDKUyvBTophP",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "A general-purpose starter agent.",
  "mcp_servers": [
    {
      "name": "example-mcp",
      "type": "url",
      "url": "https://example-server.modelcontextprotocol.io/sse"
    }
  ],
  "metadata": {
    "foo": "bar"
  },
  "model": {
    "id": "claude-sonnet-4-6",
    "speed": "standard"
  },
  "multiagent": {
    "agents": [
      {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "type": "agent",
        "version": 1
      }
    ],
    "type": "coordinator"
  },
  "name": "My First Agent",
  "skills": [
    {
      "skill_id": "xlsx",
      "type": "anthropic",
      "version": "1"
    },
    {
      "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
      "type": "custom",
      "version": "2"
    }
  ],
  "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
  "tools": [
    {
      "configs": [
        {
          "enabled": true,
          "name": "bash",
          "permission_policy": {
            "type": "always_allow"
          }
        }
      ],
      "default_config": {
        "enabled": true,
        "permission_policy": {
          "type": "always_ask"
        }
      },
      "type": "agent_toolset_20260401"
    }
  ],
  "type": "agent",
  "updated_at": "2026-03-15T10:00:00Z",
  "version": 1
}
```

---

*Copyright © Anthropic. All rights reserved.*
