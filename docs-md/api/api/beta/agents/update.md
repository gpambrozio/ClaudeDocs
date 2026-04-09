# Update Agent

Copy page

cURL

# Update Agent

POST/v1/agents/{agent\_id}

Update Agent

##### Path ParametersExpand Collapse

agent\_id: string

##### Header ParametersExpand Collapse

"anthropic-beta": optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

UnionMember0 = string

UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 18 more

Accepts one of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

##### Body ParametersJSONExpand Collapse

version: number

The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. The request fails if this does not match the server's current version.

description: optional string

Description. Up to 2048 characters. Omit to preserve; send empty string or null to clear.

mcp\_servers: optional array of [BetaManagedAgentsURLMCPServerParams](api/beta.md) { name, type, url }

MCP servers. Full replacement. Omit to preserve; send empty array or null to clear. Names must be unique. Maximum 20.

name: string

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

type: "url"

url: string

Endpoint URL for the MCP server.

metadata: optional map[string]

Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

model: optional [BetaManagedAgentsModel](api/beta.md) or [BetaManagedAgentsModelConfigParams](api/beta.md) { id, speed }

Model identifier. Accepts the [model string](about-claude/models/overview.md), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control. Omit to preserve. Cannot be cleared.

Accepts one of the following:

BetaManagedAgentsModel = "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-haiku-4-5" or 5 more or string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-haiku-4-5" or 5 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

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

UnionMember1 = string

BetaManagedAgentsModelConfigParams = object { id, speed }

An object that defines additional configuration control over model use

id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-haiku-4-5" or 5 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

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

UnionMember1 = string

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"

"fast"

name: optional string

Human-readable name. 1-256 characters. Omit to preserve. Cannot be cleared.

skills: optional array of [BetaManagedAgentsSkillParams](api/beta.md)

Skills. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 20.

Accepts one of the following:

BetaManagedAgentsAnthropicSkillParams = object { skill\_id, type, version }

An Anthropic-managed skill.

skill\_id: string

Identifier of the Anthropic skill (e.g., "xlsx").

type: "anthropic"

version: optional string

Version to pin. Defaults to latest if omitted.

BetaManagedAgentsCustomSkillParams = object { skill\_id, type, version }

A user-created custom skill.

skill\_id: string

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

type: "custom"

version: optional string

Version to pin. Defaults to latest if omitted.

system: optional string

System prompt. Up to 100,000 characters. Omit to preserve; send empty string or null to clear.

tools: optional array of [BetaManagedAgentsAgentToolset20260401Params](api/beta.md) { type, configs, default\_config }  or [BetaManagedAgentsMCPToolsetParams](api/beta.md) { mcp\_server\_name, type, configs, default\_config }  or [BetaManagedAgentsCustomToolParams](api/beta.md) { description, input\_schema, name, type }

Tool configurations available to the agent. Full replacement. Omit to preserve; send empty array or null to clear. Maximum of 128 tools across all toolsets allowed.

Accepts one of the following:

BetaManagedAgentsAgentToolset20260401Params = object { type, configs, default\_config }

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

type: "agent\_toolset\_20260401"

configs: optional array of [BetaManagedAgentsAgentToolConfigParams](api/beta.md) { name, enabled, permission\_policy }

Per-tool configuration overrides.

name: "bash" or "edit" or "read" or 5 more

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

enabled: optional boolean

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.

permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

BetaManagedAgentsAlwaysAllowPolicy = object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy = object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: optional [BetaManagedAgentsAgentToolsetDefaultConfigParams](api/beta.md) { enabled, permission\_policy }

Default configuration for all tools in a toolset.

enabled: optional boolean

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

BetaManagedAgentsAlwaysAllowPolicy = object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy = object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

BetaManagedAgentsMCPToolsetParams = object { mcp\_server\_name, type, configs, default\_config }

Configuration for tools from an MCP server defined in `mcp_servers`.

mcp\_server\_name: string

Name of the MCP server. Must match a server name from the mcp\_servers array. 1-255 characters.

type: "mcp\_toolset"

configs: optional array of [BetaManagedAgentsMCPToolConfigParams](api/beta.md) { name, enabled, permission\_policy }

Per-tool configuration overrides.

name: string

Name of the MCP tool to configure. 1-128 characters.

enabled: optional boolean

Whether this tool is enabled. Overrides the `default_config` setting.

permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

BetaManagedAgentsAlwaysAllowPolicy = object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy = object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: optional [BetaManagedAgentsMCPToolsetDefaultConfigParams](api/beta.md) { enabled, permission\_policy }

Default configuration for all tools from an MCP server.

enabled: optional boolean

Whether tools are enabled by default. Defaults to true if not specified.

permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

BetaManagedAgentsAlwaysAllowPolicy = object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy = object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

BetaManagedAgentsCustomToolParams = object { description, input\_schema, name, type }

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

description: string

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: optional map[unknown]

JSON Schema properties defining the tool's input parameters.

required: optional array of string

List of required property names.

type: optional "object"

Must be 'object' for tool input schemas.

name: string

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

type: "custom"

##### ReturnsExpand Collapse

BetaManagedAgentsAgent = object { id, archived\_at, created\_at, 11 more }

A Managed Agents `agent`.

id: string

archived\_at: string

A timestamp in RFC 3339 format

created\_at: string

A timestamp in RFC 3339 format

description: string

mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta.md) { name, type, url }

name: string

type: "url"

url: string

metadata: map[string]

model: [BetaManagedAgentsModelConfig](api/beta.md) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-haiku-4-5" or 5 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

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

UnionMember1 = string

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"

"fast"

name: string

skills: array of [BetaManagedAgentsAnthropicSkill](api/beta.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta.md) { skill\_id, type, version }

Accepts one of the following:

BetaManagedAgentsAnthropicSkill = object { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string

BetaManagedAgentsCustomSkill = object { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string

tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta.md) { description, input\_schema, name, type }

Accepts one of the following:

BetaManagedAgentsAgentToolset20260401 = object { configs, default\_config, type }

configs: array of [BetaManagedAgentsAgentToolConfig](api/beta.md) { enabled, name, permission\_policy }

enabled: boolean

name: "bash" or "edit" or "read" or 5 more

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

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

BetaManagedAgentsAlwaysAllowPolicy = object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy = object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

BetaManagedAgentsAlwaysAllowPolicy = object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy = object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"

BetaManagedAgentsMCPToolset = object { configs, default\_config, mcp\_server\_name, type }

configs: array of [BetaManagedAgentsMCPToolConfig](api/beta.md) { enabled, name, permission\_policy }

enabled: boolean

name: string

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

BetaManagedAgentsAlwaysAllowPolicy = object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy = object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

BetaManagedAgentsAlwaysAllowPolicy = object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy = object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"

BetaManagedAgentsCustomTool = object { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: string

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: optional map[unknown]

JSON Schema properties defining the tool's input parameters.

required: optional array of string

List of required property names.

type: optional "object"

Must be 'object' for tool input schemas.

name: string

type: "custom"

type: "agent"

updated\_at: string

A timestamp in RFC 3339 format

version: number

The agent's current version. Starts at 1 and increments when the agent is modified.

Update Agent

cURL

```shiki
curl https://api.anthropic.com/v1/agents/$AGENT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "version": 1
        }'
```

Response 200

```shiki
{
  "id": "agent_011CZkYpogX7uDKUyvBTophP",
  "archived_at": "2019-12-27T18:11:19.117Z",
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

```shiki
{
  "id": "agent_011CZkYpogX7uDKUyvBTophP",
  "archived_at": "2019-12-27T18:11:19.117Z",
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
