# Update Session

Copy page

SDK language

CLI

# Update Session

$ ant beta:sessions update

POST/v1/sessions/{session\_id}

Update Session

##### ParametersExpand Collapse

--session-id: string

Path param: Path parameter session\_id

--agent: optional object { mcp\_servers, tools } 

Body param: Mid-session agent configuration update. Only `tools` and `mcp_servers` are updatable. Full replacement: the provided array becomes the new value. To preserve existing entries, GET the session, modify the array, and POST it back.

--metadata: optional map[string]

Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve.

--title: optional string

Body param: Human-readable session title.

--vault-id: optional array of string

Body param: Vault IDs (`vlt_*`) to attach to the session. Not yet supported; requests setting this field are rejected. Reserved for future use.

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



beta\_managed\_agents\_session: object { id, agent, archived\_at, 13 more } 

A Managed Agents `session`.

id: string



agent: object { id, description, mcp\_servers, 8 more } 

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

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



multiagent: object { agents, type } 

Resolved coordinator topology with full agent definitions for each roster member.



agents: array of [BetaManagedAgentsSessionThreadAgent](api/beta.md) { id, description, mcp\_servers, 7 more } 

Full `agent` definitions the coordinator may spawn as session threads.

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

version: number

archived\_at: string

A timestamp in RFC 3339 format

created\_at: string

A timestamp in RFC 3339 format

environment\_id: string

metadata: map[string]



outcome\_evaluations: array of [BetaManagedAgentsOutcomeEvaluationResource](api/beta.md) { completed\_at, description, explanation, 4 more } 

Per-outcome evaluation state. One entry per define\_outcome event sent to the session.

completed\_at: string

A timestamp in RFC 3339 format

description: string

What the agent should produce.

explanation: string

Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs\_revision (intermediate), what's missing; for failed, why unrecoverable.

iteration: number

0-indexed revision cycle the outcome is currently on.

outcome\_id: string

Server-generated outc\_ ID for this outcome.

result: string

Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.



type: "outcome\_evaluation"

"outcome\_evaluation"



resources: array of [BetaManagedAgentsSessionResource](api/beta.md)



beta\_managed\_agents\_github\_repository\_resource: object { id, created\_at, mount\_path, 4 more } 

id: string

created\_at: string

A timestamp in RFC 3339 format

mount\_path: string



type: "github\_repository"

"github\_repository"

updated\_at: string

A timestamp in RFC 3339 format

url: string



checkout: optional [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  or [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type } 



beta\_managed\_agents\_branch\_checkout: object { name, type } 

name: string

Branch name to check out.



type: "branch"

"branch"



beta\_managed\_agents\_commit\_checkout: object { sha, type } 

sha: string

Full commit SHA to check out.



type: "commit"

"commit"



beta\_managed\_agents\_file\_resource: object { id, created\_at, file\_id, 3 more } 

id: string

created\_at: string

A timestamp in RFC 3339 format

file\_id: string

mount\_path: string



type: "file"

"file"

updated\_at: string

A timestamp in RFC 3339 format



beta\_managed\_agents\_memory\_store\_resource: object { memory\_store\_id, type, access, 4 more } 

A memory store attached to an agent session.

memory\_store\_id: string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.



type: "memory\_store"

"memory\_store"



access: optional "read\_write" or "read\_only"

Access mode for an attached memory store.

"read\_write"

"read\_only"

description: optional string

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

instructions: optional string

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

mount\_path: optional string

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

name: optional string

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.



stats: object { active\_seconds, duration\_seconds } 

Timing statistics for a session.

active\_seconds: optional number

Cumulative time in seconds the session spent in running status. Excludes idle time.

duration\_seconds: optional number

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.



status: "rescheduling" or "running" or "idle" or "terminated"

SessionStatus enum

"rescheduling"

"running"

"idle"

"terminated"

title: string



type: "session"

"session"

updated\_at: string

A timestamp in RFC 3339 format



usage: object { cache\_creation, cache\_read\_input\_tokens, input\_tokens, output\_tokens } 

Cumulative token usage for a session across all turns.



cache\_creation: optional object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

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

vault\_ids: array of string

Vault IDs attached to the session at creation. Empty when no vaults were supplied.

deployment\_id: optional string

Deployment ID when the session was created from a deployment reference. Null otherwise.

Update Session

CLI

```shiki
ant beta:sessions update \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```

Response 200



```shiki
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "description": "A general-purpose starter agent.",
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
    "multiagent": {
      "agents": [
        {
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
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "metadata": {},
  "outcome_evaluations": [
    {
      "completed_at": "2026-03-15T10:02:31Z",
      "description": "Produce a 2-page summary as summary.md",
      "explanation": "All five sections present with inline citations.",
      "iteration": 0,
      "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
      "result": "satisfied",
      "type": "outcome_evaluation"
    }
  ],
  "resources": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0
  },
  "status": "idle",
  "title": "Order #1234 inquiry",
  "type": "session",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  },
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "deployment_id": "deployment_id"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "description": "A general-purpose starter agent.",
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
    "multiagent": {
      "agents": [
        {
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
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "metadata": {},
  "outcome_evaluations": [
    {
      "completed_at": "2026-03-15T10:02:31Z",
      "description": "Produce a 2-page summary as summary.md",
      "explanation": "All five sections present with inline citations.",
      "iteration": 0,
      "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
      "result": "satisfied",
      "type": "outcome_evaluation"
    }
  ],
  "resources": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0
  },
  "status": "idle",
  "title": "Order #1234 inquiry",
  "type": "session",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  },
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "deployment_id": "deployment_id"
}
```

---

*Copyright © Anthropic. All rights reserved.*
