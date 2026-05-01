# List Agents

Copy page

Ruby

# List Agents

beta.agents.list(\*\*kwargs) -> PageCursor<[BetaManagedAgentsAgent](api/beta.md) { id, archived\_at, created\_at, 11 more } >

GET/v1/agents

List Agents

##### ParametersExpand Collapse

created\_at\_gte: Time

Return agents created at or after this time (inclusive).

created\_at\_lte: Time

Return agents created at or before this time (inclusive).

include\_archived: bool

Include archived agents in results. Defaults to false.

limit: Integer

Maximum results per page. Default 20, maximum 100.

page: String

Opaque pagination cursor from a previous response.

betas: Array[[AnthropicBeta](api/beta.md)]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

String

:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 20 more

Accepts one of the following:

:"message-batches-2024-09-24"

:"prompt-caching-2024-07-31"

:"computer-use-2024-10-22"

:"computer-use-2025-01-24"

:"pdfs-2024-09-25"

:"token-counting-2024-11-01"

:"token-efficient-tools-2025-02-19"

:"output-128k-2025-02-19"

:"files-api-2025-04-14"

:"mcp-client-2025-04-04"

:"mcp-client-2025-11-20"

:"dev-full-thinking-2025-05-14"

:"interleaved-thinking-2025-05-14"

:"code-execution-2025-05-22"

:"extended-cache-ttl-2025-04-11"

:"context-1m-2025-08-07"

:"context-management-2025-06-27"

:"model-context-window-exceeded-2025-08-26"

:"skills-2025-10-02"

:"fast-mode-2026-02-01"

:"output-300k-2026-03-24"

:"user-profiles-2026-03-24"

:"advisor-tool-2026-03-01"

##### ReturnsExpand Collapse

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

List Agents

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.agents.list

puts(page)
```

Response 200

```shiki
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200

```shiki
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
