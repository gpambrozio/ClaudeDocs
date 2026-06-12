# List Sessions

Copy page

SDK language

Ruby

# List Sessions

beta.sessions.list(\*\*kwargs) -> PageCursor<[BetaManagedAgentsSession](api/beta.md) { id, agent, archived\_at, 13 more } >

GET/v1/sessions

List Sessions

##### ParametersExpand Collapse

agent\_id: String

Filter sessions created with this agent ID.

agent\_version: Integer

Filter by agent version. Only applies when agent\_id is also set.

created\_at\_gt: Time

Return sessions created after this time (exclusive).

created\_at\_gte: Time

Return sessions created at or after this time (inclusive).

created\_at\_lt: Time

Return sessions created before this time (exclusive).

created\_at\_lte: Time

Return sessions created at or before this time (inclusive).

deployment\_id: String

Filter sessions created by this deployment ID.

include\_archived: bool

When true, includes archived sessions. Default: false (exclude archived).

limit: Integer

Maximum number of results to return.

memory\_store\_id: String

Filter sessions whose resources contain a memory\_store with this memory store ID.



order: :asc | :desc

Sort direction for results, ordered by created\_at. Defaults to desc (newest first).

One of the following:

:asc

:desc

page: String

Opaque pagination cursor from a previous response.



statuses: Array[:rescheduling | :running | :idle | :terminated]

Filter by session status. Repeat the parameter to match any of multiple statuses.

One of the following:

:rescheduling

:running

:idle

:terminated

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

class BetaManagedAgentsSession { id, agent, archived\_at, 13 more } 

A Managed Agents `session`.

id: String



agent: [BetaManagedAgentsSessionAgent](api/beta.md) { id, description, mcp\_servers, 8 more } 

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: String

description: String



mcp\_servers: Array[[BetaManagedAgentsMCPServerURLDefinition](api/beta.md) { name, type, url } ]

name: String

type: :url

url: String



model: [BetaManagedAgentsModelConfig](api/beta.md) { id, speed } 

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta.md)

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

multiagent: [BetaManagedAgentsSessionMultiagentCoordinator](api/beta.md) { agents, type } 

Resolved coordinator topology with full agent definitions for each roster member.



agents: Array[[BetaManagedAgentsSessionThreadAgent](api/beta.md) { id, description, mcp\_servers, 7 more } ]

Full `agent` definitions the coordinator may spawn as session threads.

id: String

description: String



mcp\_servers: Array[[BetaManagedAgentsMCPServerURLDefinition](api/beta.md) { name, type, url } ]

name: String

type: :url

url: String



model: [BetaManagedAgentsModelConfig](api/beta.md) { id, speed } 

Model identifier and configuration.



id: [BetaManagedAgentsModel](api/beta.md)

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



skills: Array[[BetaManagedAgentsAnthropicSkill](api/beta.md) { skill\_id, type, version }  | [BetaManagedAgentsCustomSkill](api/beta.md) { skill\_id, type, version } ]

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

tools: Array[[BetaManagedAgentsAgentToolset20260401](api/beta.md) { configs, default\_config, type }  | [BetaManagedAgentsMCPToolset](api/beta.md) { configs, default\_config, mcp\_server\_name, type }  | [BetaManagedAgentsCustomTool](api/beta.md) { description, input\_schema, name, type } ]

One of the following:



class BetaManagedAgentsAgentToolset20260401 { configs, default\_config, type } 



configs: Array[[BetaManagedAgentsAgentToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

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

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: bool



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

configs: Array[[BetaManagedAgentsMCPToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool

name: String



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: bool



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md) { type, properties, required } 

JSON Schema for custom tool input parameters.

type: :object

properties: Hash[Symbol, untyped]

required: Array[String]

name: String

type: :custom

type: :agent

version: Integer

type: :coordinator

name: String



skills: Array[[BetaManagedAgentsAnthropicSkill](api/beta.md) { skill\_id, type, version }  | [BetaManagedAgentsCustomSkill](api/beta.md) { skill\_id, type, version } ]

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

tools: Array[[BetaManagedAgentsAgentToolset20260401](api/beta.md) { configs, default\_config, type }  | [BetaManagedAgentsMCPToolset](api/beta.md) { configs, default\_config, mcp\_server\_name, type }  | [BetaManagedAgentsCustomTool](api/beta.md) { description, input\_schema, name, type } ]

One of the following:



class BetaManagedAgentsAgentToolset20260401 { configs, default\_config, type } 



configs: Array[[BetaManagedAgentsAgentToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

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

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy } 

Resolved default configuration for agent tools.

enabled: bool



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

configs: Array[[BetaManagedAgentsMCPToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool

name: String



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy } 

Resolved default configuration for all tools from an MCP server.

enabled: bool



permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type } 

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

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md) { type, properties, required } 

JSON Schema for custom tool input parameters.

type: :object

properties: Hash[Symbol, untyped]

required: Array[String]

name: String

type: :custom

type: :agent

version: Integer

archived\_at: Time

A timestamp in RFC 3339 format

created\_at: Time

A timestamp in RFC 3339 format

environment\_id: String

metadata: Hash[Symbol, String]



outcome\_evaluations: Array[[BetaManagedAgentsOutcomeEvaluationResource](api/beta.md) { completed\_at, description, explanation, 4 more } ]

Per-outcome evaluation state. One entry per define\_outcome event sent to the session.

completed\_at: Time

A timestamp in RFC 3339 format

description: String

What the agent should produce.

explanation: String

Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs\_revision (intermediate), what's missing; for failed, why unrecoverable.

iteration: Integer

0-indexed revision cycle the outcome is currently on.

outcome\_id: String

Server-generated outc\_ ID for this outcome.

result: String

Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

type: :outcome\_evaluation



resources: Array[[BetaManagedAgentsSessionResource](api/beta.md)]

One of the following:



class BetaManagedAgentsGitHubRepositoryResource { id, created\_at, mount\_path, 4 more } 

id: String

created\_at: Time

A timestamp in RFC 3339 format

mount\_path: String

type: :github\_repository

updated\_at: Time

A timestamp in RFC 3339 format

url: String



checkout: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type } 

One of the following:



class BetaManagedAgentsBranchCheckout { name, type } 

name: String

Branch name to check out.

type: :branch



class BetaManagedAgentsCommitCheckout { sha, type } 

sha: String

Full commit SHA to check out.

type: :commit



class BetaManagedAgentsFileResource { id, created\_at, file\_id, 3 more } 

id: String

created\_at: Time

A timestamp in RFC 3339 format

file\_id: String

mount\_path: String

type: :file

updated\_at: Time

A timestamp in RFC 3339 format



class BetaManagedAgentsMemoryStoreResource { memory\_store\_id, type, access, 4 more } 

A memory store attached to an agent session.

memory\_store\_id: String

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: :memory\_store



access: :read\_write | :read\_only

Access mode for an attached memory store.

One of the following:

:read\_write

:read\_only

description: String

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

instructions: String

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

mount\_path: String

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

name: String

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.



stats: [BetaManagedAgentsSessionStats](api/beta.md) { active\_seconds, duration\_seconds } 

Timing statistics for a session.

active\_seconds: Float

Cumulative time in seconds the session spent in running status. Excludes idle time.

duration\_seconds: Float

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.



status: :rescheduling | :running | :idle | :terminated

SessionStatus enum

One of the following:

:rescheduling

:running

:idle

:terminated

title: String

type: :session

updated\_at: Time

A timestamp in RFC 3339 format



usage: [BetaManagedAgentsSessionUsage](api/beta.md) { cache\_creation, cache\_read\_input\_tokens, input\_tokens, output\_tokens } 

Cumulative token usage for a session across all turns.



cache\_creation: [BetaManagedAgentsCacheCreationUsage](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: Integer

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: Integer

Tokens used to create 5-minute ephemeral cache entries.

cache\_read\_input\_tokens: Integer

Total tokens read from prompt cache.

input\_tokens: Integer

Total input tokens consumed across all turns.

output\_tokens: Integer

Total output tokens generated across all turns.

vault\_ids: Array[String]

Vault IDs attached to the session at creation. Empty when no vaults were supplied.

deployment\_id: String

Deployment ID when the session was created from a deployment reference. Null otherwise.

List Sessions

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.sessions.list

puts(page)
```

Response 200



```shiki
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

---

*Copyright © Anthropic. All rights reserved.*
