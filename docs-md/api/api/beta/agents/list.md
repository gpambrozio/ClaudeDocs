# List Agents

Copy page



cURL

# List Agents

GET/v1/agents

List Agents

##### Query parameters



"created\_at[gte]": optional string

Return agents created at or after this time (inclusive).

formatdate-time



"created\_at[lte]": optional string

Return agents created at or before this time (inclusive).

formatdate-time

include\_archived: optional boolean

Include archived agents in results. Defaults to false.



limit: optional number

Maximum results per page. Default 20, maximum 100.

formatint32

page: optional string

Opaque pagination cursor from a previous response.

##### Headers



"anthropic-beta": optional array of [AnthropicBeta](api/http/beta.md)

Optional header to specify the beta version(s) you want to use.

One of the following:

string



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 31 more

One of the following:

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

"user-profiles-2026-03-24"

"user-profiles-2026-08-18"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"dreaming-2026-04-21"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"server-side-fallback-2026-07-01"

"fallback-credit-2026-06-01"

"fallback-credit-2026-07-01"

"agent-memory-2026-07-22"

"mid-conversation-tool-changes-2026-07-01"

##### Returns



data: array of [BetaManagedAgentsAgent](api/http/beta/agents.md) { id, archived\_at, created\_at, 12 more }

List of agents.

id: string



archived\_at: string or null

A timestamp in RFC 3339 format

formatdate-time



created\_at: string

A timestamp in RFC 3339 format

formatdate-time

description: string or null



mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/http/beta/agents.md) { name, type, url }

name: string

type: "url"

url: string

metadata: map[string]



model: [BetaManagedAgentsModelConfig](api/http/beta/agents.md) { id, effort, inference\_geo, speed }

Model identifier and configuration.



multiagent: [BetaManagedAgentsMultiagent](api/http/beta/sessions.md) { agents, type } or null

Resolved coordinator topology with a concrete agent roster.

name: string



skills: array of [BetaManagedAgentsAnthropicSkill](api/http/beta/agents.md) { skill\_id, type, version } or [BetaManagedAgentsCustomSkill](api/http/beta/agents.md) { skill\_id, type, version }

One of the following:



BetaManagedAgentsAnthropicSkill object{ skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string



BetaManagedAgentsCustomSkill object{ skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string or null



tools: array of [BetaManagedAgentsAgentToolset20260401](api/http/beta/agents.md) { configs, default\_config, type } or [BetaManagedAgentsMCPToolset](api/http/beta/agents.md) { configs, default\_config, mcp\_server\_name, type } or [BetaManagedAgentsCustomTool](api/http/beta/agents.md) { description, input\_schema, name, type }

One of the following:



BetaManagedAgentsAgentToolset20260401 object{ configs, default\_config, type }



BetaManagedAgentsMCPToolset object{ configs, default\_config, mcp\_server\_name, type }

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

type: "agent"



updated\_at: string

A timestamp in RFC 3339 format

formatdate-time



version: number

The agent's current version. Starts at 1 and increments when the agent is modified.

formatint32

next\_page: optional string or null

Opaque cursor for the next page. Null when no more results.

### List Agents

cURL



```shiki
curl https://api.anthropic.com/v1/agents \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



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
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



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
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
