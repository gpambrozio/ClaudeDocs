# Update Agent

Copy page

CLI

# Update Agent

$ ant beta:agents update

POST/v1/agents/{agent\_id}

Update Agent

##### ParametersExpand Collapse

--agent-id: string

Path param: Path parameter agent\_id

--version: number

Body param: The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. The request fails if this does not match the server's current version.

--description: optional string

Body param: Description. Up to 2048 characters. Omit to preserve; send empty string or null to clear.

--mcp-server: optional array of [BetaManagedAgentsURLMCPServerParams](api/beta.md) { name, type, url }

Body param: MCP servers. Full replacement. Omit to preserve; send empty array or null to clear. Names must be unique. Maximum 20.

--metadata: optional map[string]

Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

--model: optional [BetaManagedAgentsModelConfigParams](api/beta.md) { id, speed }

Body param: Model identifier. Accepts the [model string](about-claude/models/overview.md), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control. Omit to preserve. Cannot be cleared.

--name: optional string

Body param: Human-readable name. 1-256 characters. Omit to preserve. Cannot be cleared.

--skill: optional array of [BetaManagedAgentsSkillParams](api/beta.md)

Body param: Skills. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 20.

--system: optional string

Body param: System prompt. Up to 100,000 characters. Omit to preserve; send empty string or null to clear.

--tool: optional array of [BetaManagedAgentsAgentToolset20260401Params](api/beta.md) { type, configs, default\_config }  or [BetaManagedAgentsMCPToolsetParams](api/beta.md) { mcp\_server\_name, type, configs, default\_config }  or [BetaManagedAgentsCustomToolParams](api/beta.md) { description, input\_schema, name, type }

Body param: Tool configurations available to the agent. Full replacement. Omit to preserve; send empty array or null to clear. Maximum of 128 tools across all toolsets allowed.

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

beta\_managed\_agents\_agent: object { id, archived\_at, created\_at, 11 more }

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

"url"

url: string

metadata: map[string]

model: object { id, speed }

Model identifier and configuration.

id: "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-haiku-4-5" or 5 more or string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

"standard"

"fast"

name: string

skills: array of [BetaManagedAgentsAnthropicSkill](api/beta.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta.md) { skill\_id, type, version }

beta\_managed\_agents\_anthropic\_skill: object { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

"anthropic"

version: string

beta\_managed\_agents\_custom\_skill: object { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: string

type: "custom"

"custom"

version: string

system: string

tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta.md) { description, input\_schema, name, type }

beta\_managed\_agents\_agent\_toolset20260401: object { configs, default\_config, type }

configs: array of [BetaManagedAgentsAgentToolConfig](api/beta.md) { enabled, name, permission\_policy }

enabled: boolean

name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

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

beta\_managed\_agents\_always\_allow\_policy: object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

"always\_allow"

beta\_managed\_agents\_always\_ask\_policy: object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

"always\_ask"

default\_config: object { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

beta\_managed\_agents\_always\_allow\_policy: object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

"always\_allow"

beta\_managed\_agents\_always\_ask\_policy: object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

"always\_ask"

type: "agent\_toolset\_20260401"

"agent\_toolset\_20260401"

beta\_managed\_agents\_mcp\_toolset: object { configs, default\_config, mcp\_server\_name, type }

configs: array of [BetaManagedAgentsMCPToolConfig](api/beta.md) { enabled, name, permission\_policy }

enabled: boolean

name: string

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

beta\_managed\_agents\_always\_allow\_policy: object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

"always\_allow"

beta\_managed\_agents\_always\_ask\_policy: object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

"always\_ask"

default\_config: object { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

beta\_managed\_agents\_always\_allow\_policy: object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

"always\_allow"

beta\_managed\_agents\_always\_ask\_policy: object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

"always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"

"mcp\_toolset"

beta\_managed\_agents\_custom\_tool: object { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: string

input\_schema: object { properties, required, type }

JSON Schema for custom tool input parameters.

properties: optional map[unknown]

JSON Schema properties defining the tool's input parameters.

required: optional array of string

List of required property names.

type: optional "object"

Must be 'object' for tool input schemas.

"object"

name: string

type: "custom"

"custom"

type: "agent"

"agent"

updated\_at: string

A timestamp in RFC 3339 format

version: number

The agent's current version. Starts at 1 and increments when the agent is modified.

Update Agent

CLI

```shiki
ant beta:agents update \
  --api-key my-anthropic-api-key \
  --agent-id agent_011CZkYpogX7uDKUyvBTophP \
  --version 1
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
