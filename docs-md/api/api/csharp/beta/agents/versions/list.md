# List Agent Versions

Copy page

C#

# List Agent Versions

[VersionListPageResponse](api/beta.md) Beta.Agents.Versions.List(VersionListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/agents/{agent\_id}/versions

List Agent Versions

##### ParametersExpand Collapse

VersionListParams parameters

required string agentID

Path param: Path parameter agent\_id

Int limit

Query param: Maximum results per page. Default 20, maximum 100.

string page

Query param: Opaque pagination cursor.

IReadOnlyList<[AnthropicBeta](api/beta.md)> betas

Header param: Optional header to specify the beta version(s) you want to use.

"message-batches-2024-09-24"MessageBatches2024\_09\_24

"prompt-caching-2024-07-31"PromptCaching2024\_07\_31

"computer-use-2024-10-22"ComputerUse2024\_10\_22

"computer-use-2025-01-24"ComputerUse2025\_01\_24

"pdfs-2024-09-25"Pdfs2024\_09\_25

"token-counting-2024-11-01"TokenCounting2024\_11\_01

"token-efficient-tools-2025-02-19"TokenEfficientTools2025\_02\_19

"output-128k-2025-02-19"Output128k2025\_02\_19

"files-api-2025-04-14"FilesApi2025\_04\_14

"mcp-client-2025-04-04"McpClient2025\_04\_04

"mcp-client-2025-11-20"McpClient2025\_11\_20

"dev-full-thinking-2025-05-14"DevFullThinking2025\_05\_14

"interleaved-thinking-2025-05-14"InterleavedThinking2025\_05\_14

"code-execution-2025-05-22"CodeExecution2025\_05\_22

"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025\_04\_11

"context-1m-2025-08-07"Context1m2025\_08\_07

"context-management-2025-06-27"ContextManagement2025\_06\_27

"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025\_08\_26

"skills-2025-10-02"Skills2025\_10\_02

"fast-mode-2026-02-01"FastMode2026\_02\_01

"output-300k-2026-03-24"Output300k2026\_03\_24

##### ReturnsExpand Collapse

class VersionListPageResponse:

Paginated list of agent versions.

IReadOnlyList<[BetaManagedAgentsAgent](api/beta.md)> Data

Agent versions.

required string ID

required DateTimeOffset? ArchivedAt

A timestamp in RFC 3339 format

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string? Description

required IReadOnlyList<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> McpServers

required string Name

required Type Type

required string Url

required IReadOnlyDictionary<string, string> Metadata

required [BetaManagedAgentsModelConfig](api/beta.md) Model

Model identifier and configuration.

required [BetaManagedAgentsModel](api/beta.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding

Speed Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"Standard

"fast"Fast

required string Name

required IReadOnlyList<Skill> Skills

Accepts one of the following:

class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

required string SkillID

required Type Type

required string Version

class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

required string SkillID

required Type Type

required string Version

required string? System

required IReadOnlyList<Tool> Tools

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401:

required IReadOnlyList<[BetaManagedAgentsAgentToolConfig](api/beta.md)> Configs

required Boolean Enabled

required Name Name

Built-in agent tool identifier.

Accepts one of the following:

"bash"Bash

"edit"Edit

"read"Read

"write"Write

"glob"Glob

"grep"Grep

"web\_fetch"WebFetch

"web\_search"WebSearch

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) DefaultConfig

Resolved default configuration for agent tools.

required Boolean Enabled

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required Type Type

class BetaManagedAgentsMcpToolset:

required IReadOnlyList<[BetaManagedAgentsMcpToolConfig](api/beta.md)> Configs

required Boolean Enabled

required string Name

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required [BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) DefaultConfig

Resolved default configuration for all tools from an MCP server.

required Boolean Enabled

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required string McpServerName

required Type Type

class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

required string Description

required [BetaManagedAgentsCustomToolInputSchema](api/beta.md) InputSchema

JSON Schema for custom tool input parameters.

IReadOnlyDictionary<string, JsonElement>? Properties

JSON Schema properties defining the tool's input parameters.

IReadOnlyList<string> Required

List of required property names.

Type Type

Must be 'object' for tool input schemas.

required string Name

required Type Type

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required Int Version

The agent's current version. Starts at 1 and increments when the agent is modified.

string? NextPage

Opaque cursor for the next page. Null when no more results.

List Agent Versions

C#

```shiki
VersionListParams parameters = new()
{
    AgentID = "agent_011CZkYpogX7uDKUyvBTophP"
};

var page = await client.Beta.Agents.Versions.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

Response 200

```shiki
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
