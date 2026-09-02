# Create Agent

Copy page



cURL

# Create Agent

POST/v1/agents

Create Agent

##### Headers



"anthropic-beta": optional array of [AnthropicBeta](api/http/beta.md)

Optional header to specify the beta version(s) you want to use.

One of the following:

string



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 41 more

One of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"user-profiles-2026-08-18"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"dreaming-2026-04-21"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"server-side-fallback-2026-07-01"

"fallback-credit-2026-06-01"

"fallback-credit-2026-07-01"

"agent-memory-2026-07-22"

"mid-conversation-tool-changes-2026-07-01"

"compact-2026-01-12"

"computer-use-2025-11-24"

"mcp-tunnels-2026-06-22"

"structured-outputs-2025-11-13"

"task-budgets-2026-03-13"

"thinking-display-updates-2026-08-18"

"ce-user-management-2026-07-13"

"mid-conversation-output-config-2026-07-01"

"thinking-binding-controls-2026-08-01"

"mid-conversation-system-clear-at-2026-08-21"

##### Body



model: [BetaManagedAgentsModel](api/http/beta/agents.md) or [BetaManagedAgentsModelConfigParams](api/http/beta/agents.md) { id, effort, inference\_geo, speed }

Model identifier. Accepts the [model string](about-claude/models/overview.md), e.g. `claude-opus-5`, or a `model_config` object for additional configuration control

One of the following:



BetaManagedAgentsModel = "claude-fable-5-1" or "claude-sonnet-5" or "claude-fable-5" or 11 more or string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



BetaManagedAgentsModelConfigParams object{ id, effort, inference\_geo, speed }

An object that defines additional configuration control over model use



name: string

Human-readable name for the agent.

minLength1

maxLength256



description: optional string or null

Description of what the agent does.

maxLength2048



mcp\_servers: optional array of [BetaManagedAgentsURLMCPServerParams](api/http/beta/agents.md) { name, type, url }

MCP servers this agent connects to. Maximum 20. Names must be unique within the array. Every server must be referenced by an `mcp_toolset` in `tools`; unreferenced servers are rejected. See the [MCP connector guide](managed-agents/mcp-connector.md).



name: string

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

minLength1

maxLength255

type: "url"



url: string

Endpoint URL for the MCP server.

maxLength2048

metadata: optional map[string]

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.



multiagent: optional [BetaManagedAgentsMultiagentParams](api/http/beta/sessions.md) { agents, type } or null

A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.



skills: optional array of [BetaManagedAgentsSkillParams](api/http/beta/agents.md)

Skills available to the agent.

One of the following:



BetaManagedAgentsAnthropicSkillParams object{ skill\_id, type, version }

An Anthropic-managed skill.



skill\_id: string

Identifier of the Anthropic skill (e.g., "xlsx").

minLength1

maxLength64

type: "anthropic"



version: optional string or null

Version to pin. Defaults to latest if omitted.

minLength1

maxLength64



BetaManagedAgentsCustomSkillParams object{ skill\_id, type, version }

A user-created custom skill.



skill\_id: string

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

minLength1

maxLength64

type: "custom"



version: optional string or null

Version to pin. Defaults to latest if omitted.

minLength1

maxLength64



system: optional string or null

System prompt for the agent.

maxLength100000



tools: optional array of [BetaManagedAgentsAgentToolset20260401Params](api/http/beta/agents.md) { type, configs, default\_config } or [BetaManagedAgentsMCPToolsetParams](api/http/beta/agents.md) { mcp\_server\_name, type, configs, default\_config } or [BetaManagedAgentsCustomToolParams](api/http/beta/agents.md) { description, input\_schema, name, type }

Tool configurations available to the agent. Maximum of 128 tools across all toolsets allowed.

One of the following:



BetaManagedAgentsAgentToolset20260401Params object{ type, configs, default\_config }

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.



BetaManagedAgentsMCPToolsetParams object{ mcp\_server\_name, type, configs, default\_config }

Configuration for tools from an MCP server defined in `mcp_servers`.



BetaManagedAgentsCustomToolParams object{ description, input\_schema, name, type }

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.



description: string

Description of what the tool does, shown to the agent to help it decide when to use the tool.

minLength1



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/http/beta/agents.md) { type, properties, required }

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown] or null

required: optional array of string or null



name: string

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

minLength1

maxLength128

type: "custom"

##### Returns



BetaManagedAgentsAgent object{ id, archived\_at, created\_at, 12 more }

A Managed Agents `agent`.

Create Agent

cURL

```shiki
curl https://api.anthropic.com/v1/agents \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "model": "claude-opus-5",
          "name": "My First Agent",
          "description": "A general-purpose starter agent.",
          "metadata": {
            "foo": "bar"
          },
          "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user'\''s task end to end.",
          "tools": [
            {
              "type": "agent_toolset_20260401"
            }
          ]
        }'
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
    "id": "claude-opus-5",
    "effort": {
      "type": "low"
    },
    "inference_geo": "inference_geo",
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
          },
          "type": "bash"
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
    "id": "claude-opus-5",
    "effort": {
      "type": "low"
    },
    "inference_geo": "inference_geo",
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
          },
          "type": "bash"
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
