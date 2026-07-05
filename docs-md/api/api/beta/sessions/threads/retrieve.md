# Get Session Thread

Copy page



cURL

# Get Session Thread

GET/v1/sessions/{session\_id}/threads/{thread\_id}

Get Session Thread

##### Path ParametersExpand Collapse

session\_id: string

thread\_id: string

##### Header ParametersExpand Collapse



"anthropic-beta": optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

One of the following:

string



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more

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

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"fallback-credit-2026-06-01"

##### ReturnsExpand Collapse



BetaManagedAgentsSessionThread object { id, agent, archived\_at, 8 more } 

An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

id: string

Unique identifier for this thread.



agent: [BetaManagedAgentsSessionThreadAgent](api/beta/agents.md) { id, description, mcp\_servers, 7 more } 

Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

id: string

description: string



mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md) { name, type, url } 

name: string

type: "url"

url: string



model: [BetaManagedAgentsModelConfig](api/beta/agents.md) { id, speed } 

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta/agents.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-opus-4-8" or 9 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"

High-performance model for coding and agents

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

string



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"

name: string



skills: array of [BetaManagedAgentsAnthropicSkill](api/beta/agents.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta/agents.md) { skill\_id, type, version } 

One of the following:



BetaManagedAgentsAnthropicSkill object { skill\_id, type, version } 

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string



BetaManagedAgentsCustomSkill object { skill\_id, type, version } 

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string



tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta/agents.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta/agents.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta/agents.md) { description, input\_schema, name, type } 

One of the following:



BetaManagedAgentsAgentToolset20260401 object { configs, default\_config, type } 



configs: array of [BetaManagedAgentsAgentToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean



name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

One of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"



default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"



BetaManagedAgentsMCPToolset object { configs, default\_config, mcp\_server\_name, type } 



configs: array of [BetaManagedAgentsMCPToolConfig](api/beta/agents.md) { enabled, name, permission\_policy } 

enabled: boolean

name: string



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"



default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta/agents.md) { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: boolean



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta/agents.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta/agents.md) { type } 

Permission policy for tool execution.

One of the following:



BetaManagedAgentsAlwaysAllowPolicy object { type } 

Tool calls are automatically approved without user confirmation.

type: "always\_allow"



BetaManagedAgentsAlwaysAskPolicy object { type } 

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"



BetaManagedAgentsCustomTool object { description, input\_schema, name, type } 

A custom tool as returned in API responses.

description: string



input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) { type, properties, required } 

JSON Schema for custom tool input parameters.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string

type: "custom"

type: "agent"

version: number

archived\_at: string

A timestamp in RFC 3339 format

created\_at: string

A timestamp in RFC 3339 format

parent\_thread\_id: string

Parent thread that spawned this thread. Null for the primary thread.

session\_id: string

The session this thread belongs to.



stats: [BetaManagedAgentsSessionThreadStats](api/beta/sessions/threads.md) { active\_seconds, duration\_seconds, startup\_seconds } 

Timing statistics for a session thread.

active\_seconds: optional number

Cumulative time in seconds the thread spent actively running. Excludes idle time.

duration\_seconds: optional number

Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

startup\_seconds: optional number

Time in seconds for the thread to begin running. Zero for child threads, which start immediately.



status: [BetaManagedAgentsSessionThreadStatus](api/beta/sessions/threads.md)

SessionThreadStatus enum

One of the following:

"running"

"idle"

"rescheduling"

"terminated"

type: "session\_thread"

updated\_at: string

A timestamp in RFC 3339 format



usage: [BetaManagedAgentsSessionThreadUsage](api/beta/sessions/threads.md) { cache\_creation, cache\_read\_input\_tokens, input\_tokens, output\_tokens } 

Cumulative token usage for a session thread across all turns.



cache\_creation: optional [BetaManagedAgentsCacheCreationUsage](api/beta/sessions.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: optional number

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: optional number

Tokens used to create 5-minute ephemeral cache entries.

cache\_read\_input\_tokens: optional number

Total tokens read from prompt cache.

input\_tokens: optional number

Total input tokens consumed across all turns.

output\_tokens: optional number

Total output tokens generated across all turns.

Get Session Thread

cURL

```shiki
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/threads/$THREAD_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```shiki
{
  "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "description": "A focused research subagent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-sonnet-4-6",
      "speed": "standard"
    },
    "name": "Researcher",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      }
    ],
    "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
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
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "parent_thread_id": null,
  "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0,
    "startup_seconds": 0
  },
  "status": "idle",
  "type": "session_thread",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "description": "A focused research subagent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-sonnet-4-6",
      "speed": "standard"
    },
    "name": "Researcher",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      }
    ],
    "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
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
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "parent_thread_id": null,
  "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0,
    "startup_seconds": 0
  },
  "status": "idle",
  "type": "session_thread",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

---

*Copyright © Anthropic. All rights reserved.*
