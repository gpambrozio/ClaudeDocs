# Archive Agent

Copy page



C#

# Archive Agent

[BetaManagedAgentsAgent](api/beta/agents.md) Beta.Agents.Archive(AgentArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/agents/{agent\_id}/archive

Archive Agent

##### ParametersExpand Collapse



AgentArchiveParams parameters

required string agentID

Path parameter agent\_id



IReadOnlyList<[AnthropicBeta](api/beta.md)> betas

Optional header to specify the beta version(s) you want to use.

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

class BetaManagedAgentsAgent:

A Managed Agents `agent`.

required string ID

required DateTimeOffset? ArchivedAt

A timestamp in RFC 3339 format

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string? Description



required IReadOnlyList<[BetaManagedAgentsMcpServerUrlDefinition](api/beta/agents.md)> McpServers

required string Name

required Type Type

required string Url

required IReadOnlyDictionary<string, string> Metadata



required [BetaManagedAgentsModelConfig](api/beta/agents.md) Model

Model identifier and configuration.



required [BetaManagedAgentsModel](api/beta/agents.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"ClaudeSonnet5

High-performance model for coding and agents

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

required [BetaManagedAgentsMultiagent](api/beta/sessions.md)? Multiagent

Resolved coordinator topology with a concrete agent roster.



required IReadOnlyList<[BetaManagedAgentsAgentReference](api/beta/agents.md)> Agents

Agents the coordinator may spawn as session threads, each resolved to a specific version.

required string ID

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

required IReadOnlyList<[BetaManagedAgentsAgentToolConfig](api/beta/agents.md)> Configs

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

required [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md) DefaultConfig

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

required IReadOnlyList<[BetaManagedAgentsMcpToolConfig](api/beta/agents.md)> Configs

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

required [BetaManagedAgentsMcpToolsetDefaultConfig](api/beta/agents.md) DefaultConfig

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

required [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md) InputSchema

JSON Schema for custom tool input parameters.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required

required string Name

required Type Type

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required Int Version

The agent's current version. Starts at 1 and increments when the agent is modified.

Archive Agent

C#

```shiki
AgentArchiveParams parameters = new()
{
    AgentID = "agent_011CZkYpogX7uDKUyvBTophP"
};

var betaManagedAgentsAgent = await client.Beta.Agents.Archive(parameters);

Console.WriteLine(betaManagedAgentsAgent);
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
