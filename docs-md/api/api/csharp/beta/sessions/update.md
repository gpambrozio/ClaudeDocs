# Update Session

Copy page

SDK language

C#

# Update Session

[BetaManagedAgentsSession](api/beta.md) Beta.Sessions.Update(SessionUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}

Update Session

##### ParametersExpand Collapse



SessionUpdateParams parameters

required string sessionID

Path param: Path parameter session\_id

[BetaManagedAgentsSessionAgentUpdate](api/beta.md) agent

Body param: Mid-session agent configuration update. Only `tools` and `mcp_servers` are updatable. Full replacement: the provided array becomes the new value. To preserve existing entries, GET the session, modify the array, and POST it back.

IReadOnlyDictionary<string, string>? metadata

Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve.

string? title

Body param: Human-readable session title.

IReadOnlyList<string> vaultIds

Body param: Vault IDs (`vlt_*`) to attach to the session. Not yet supported; requests setting this field are rejected. Reserved for future use.



IReadOnlyList<[AnthropicBeta](api/beta.md)> betas

Header param: Optional header to specify the beta version(s) you want to use.

"message-batches-2024-09-24"MessageBatches2024\_09\_24

"prompt-caching-2024-07-31"PromptCaching2024\_07\_31

"computer-use-2024-10-22"ComputerUse2024\_10\_22

"computer-use-2025-01-24"ComputerUse2025\_01\_24

"pdfs-2024-09-25"Pdfs2024\_09\_25

"token-counting-2024-11-01"TokenCounting2024\_11\_01

"token-efficient-tools-2025-02-19"TokenEfficientTools2025\_02\_19

"output-128k-2025-02-19"Output128k2025\_02\_19

"files-api-2025-04-14"FilesApi2025\_04\_14

"mcp-client-2025-04-04"McpClient2025\_04\_04

"mcp-client-2025-11-20"McpClient2025\_11\_20

"dev-full-thinking-2025-05-14"DevFullThinking2025\_05\_14

"interleaved-thinking-2025-05-14"InterleavedThinking2025\_05\_14

"code-execution-2025-05-22"CodeExecution2025\_05\_22

"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025\_04\_11

"context-1m-2025-08-07"Context1m2025\_08\_07

"context-management-2025-06-27"ContextManagement2025\_06\_27

"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025\_08\_26

"skills-2025-10-02"Skills2025\_10\_02

"fast-mode-2026-02-01"FastMode2026\_02\_01

"output-300k-2026-03-24"Output300k2026\_03\_24

"user-profiles-2026-03-24"UserProfiles2026\_03\_24

"advisor-tool-2026-03-01"AdvisorTool2026\_03\_01

"managed-agents-2026-04-01"ManagedAgents2026\_04\_01

"cache-diagnosis-2026-04-07"CacheDiagnosis2026\_04\_07

"thinking-token-count-2026-05-13"ThinkingTokenCount2026\_05\_13

"server-side-fallback-2026-06-01"ServerSideFallback2026\_06\_01

"fallback-credit-2026-06-01"FallbackCredit2026\_06\_01

##### ReturnsExpand Collapse



class BetaManagedAgentsSession:

A Managed Agents `session`.

required string ID



required [BetaManagedAgentsSessionAgent](api/beta.md) Agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

required string ID

required string? Description



required IReadOnlyList<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> McpServers

required string Name

required Type Type

required string Url



required [BetaManagedAgentsModelConfig](api/beta.md) Model

Model identifier and configuration.



required [BetaManagedAgentsModel](api/beta.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-fable-5"ClaudeFable5

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"ClaudeOpus4\_8

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"ClaudeOpus4\_7

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding



Speed Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"Standard

"fast"Fast



required [BetaManagedAgentsSessionMultiagentCoordinator](api/beta.md)? Multiagent

Resolved coordinator topology with full agent definitions for each roster member.



required IReadOnlyList<[BetaManagedAgentsSessionThreadAgent](api/beta.md)> Agents

Full `agent` definitions the coordinator may spawn as session threads.

required string ID

required string? Description



required IReadOnlyList<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> McpServers

required string Name

required Type Type

required string Url



required [BetaManagedAgentsModelConfig](api/beta.md) Model

Model identifier and configuration.



required [BetaManagedAgentsModel](api/beta.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-fable-5"ClaudeFable5

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-opus-4-8"ClaudeOpus4\_8

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"ClaudeOpus4\_7

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding



Speed Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"Standard

"fast"Fast

required string Name



required IReadOnlyList<Skill> Skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

required string SkillID

required Type Type

required string Version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

required string SkillID

required Type Type

required string Version

required string? System



required IReadOnlyList<Tool> Tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



required IReadOnlyList<[BetaManagedAgentsAgentToolConfig](api/beta.md)> Configs

required Boolean Enabled



required Name Name

Built-in agent tool identifier.

One of the following:

"bash"Bash

"edit"Edit

"read"Read

"write"Write

"glob"Glob

"grep"Grep

"web\_fetch"WebFetch

"web\_search"WebSearch



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) DefaultConfig

Resolved default configuration for agent tools.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required Type Type



class BetaManagedAgentsMcpToolset:



required IReadOnlyList<[BetaManagedAgentsMcpToolConfig](api/beta.md)> Configs

required Boolean Enabled

required string Name



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) DefaultConfig

Resolved default configuration for all tools from an MCP server.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required string McpServerName

required Type Type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

required string Description



required [BetaManagedAgentsCustomToolInputSchema](api/beta.md) InputSchema

JSON Schema for custom tool input parameters.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required

required string Name

required Type Type

required Type Type

required Int Version

required Type Type

required string Name



required IReadOnlyList<Skill> Skills

One of the following:



class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

required string SkillID

required Type Type

required string Version



class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

required string SkillID

required Type Type

required string Version

required string? System



required IReadOnlyList<Tool> Tools

One of the following:



class BetaManagedAgentsAgentToolset20260401:



required IReadOnlyList<[BetaManagedAgentsAgentToolConfig](api/beta.md)> Configs

required Boolean Enabled



required Name Name

Built-in agent tool identifier.

One of the following:

"bash"Bash

"edit"Edit

"read"Read

"write"Write

"glob"Glob

"grep"Grep

"web\_fetch"WebFetch

"web\_search"WebSearch



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) DefaultConfig

Resolved default configuration for agent tools.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required Type Type



class BetaManagedAgentsMcpToolset:



required IReadOnlyList<[BetaManagedAgentsMcpToolConfig](api/beta.md)> Configs

required Boolean Enabled

required string Name



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type



required [BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) DefaultConfig

Resolved default configuration for all tools from an MCP server.

required Boolean Enabled



required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

One of the following:



class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type



class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required string McpServerName

required Type Type



class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

required string Description



required [BetaManagedAgentsCustomToolInputSchema](api/beta.md) InputSchema

JSON Schema for custom tool input parameters.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required

required string Name

required Type Type

required Type Type

required Int Version

required DateTimeOffset? ArchivedAt

A timestamp in RFC 3339 format

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string EnvironmentID

required IReadOnlyDictionary<string, string> Metadata



required IReadOnlyList<[BetaManagedAgentsOutcomeEvaluationResource](api/beta.md)> OutcomeEvaluations

Per-outcome evaluation state. One entry per define\_outcome event sent to the session.

required DateTimeOffset? CompletedAt

A timestamp in RFC 3339 format

required string Description

What the agent should produce.

required string? Explanation

Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs\_revision (intermediate), what's missing; for failed, why unrecoverable.

required Int Iteration

0-indexed revision cycle the outcome is currently on.

required string OutcomeID

Server-generated outc\_ ID for this outcome.

required string Result

Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

required Type Type



required IReadOnlyList<[BetaManagedAgentsSessionResource](api/beta.md)> Resources

One of the following:



class BetaManagedAgentsGitHubRepositoryResource:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string MountPath

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required string Url



Checkout? Checkout

One of the following:



class BetaManagedAgentsBranchCheckout:

required string Name

Branch name to check out.

required Type Type



class BetaManagedAgentsCommitCheckout:

required string Sha

Full commit SHA to check out.

required Type Type



class BetaManagedAgentsFileResource:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string FileID

required string MountPath

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsMemoryStoreResource:

A memory store attached to an agent session.

required string MemoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

required Type Type



Access? Access

Access mode for an attached memory store.

One of the following:

"read\_write"ReadWrite

"read\_only"ReadOnly

string Description

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

string? Instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

string? MountPath

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

string? Name

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.



required [BetaManagedAgentsSessionStats](api/beta.md) Stats

Timing statistics for a session.

Double ActiveSeconds

Cumulative time in seconds the session spent in running status. Excludes idle time.

Double DurationSeconds

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.



required Status Status

SessionStatus enum

One of the following:

"rescheduling"Rescheduling

"running"Running

"idle"Idle

"terminated"Terminated

required string? Title

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format



required [BetaManagedAgentsSessionUsage](api/beta.md) Usage

Cumulative token usage for a session across all turns.



[BetaManagedAgentsCacheCreationUsage](api/beta.md) CacheCreation

Prompt-cache creation token usage broken down by cache lifetime.

Int Ephemeral1hInputTokens

Tokens used to create 1-hour ephemeral cache entries.

Int Ephemeral5mInputTokens

Tokens used to create 5-minute ephemeral cache entries.

Int CacheReadInputTokens

Total tokens read from prompt cache.

Int InputTokens

Total input tokens consumed across all turns.

Int OutputTokens

Total output tokens generated across all turns.

required IReadOnlyList<string> VaultIds

Vault IDs attached to the session at creation. Empty when no vaults were supplied.

string? DeploymentID

Deployment ID when the session was created from a deployment reference. Null otherwise.

Update Session

C#

```shiki
SessionUpdateParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7"
};

var betaManagedAgentsSession = await client.Beta.Sessions.Update(parameters);

Console.WriteLine(betaManagedAgentsSession);
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
