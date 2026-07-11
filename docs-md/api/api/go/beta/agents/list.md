# List Agents

Copy page



Go

# List Agents

client.Beta.Agents.List(ctx, params) (\*PageCursor[[BetaManagedAgentsAgent](api/beta/agents.md)], error)

GET/v1/agents

List Agents

##### ParametersExpand Collapse



params BetaAgentListParams

CreatedAtGte param.Field[[Time](api/beta/agents/list.md)]Optional

Query param: Return agents created at or after this time (inclusive).

CreatedAtLte param.Field[[Time](api/beta/agents/list.md)]Optional

Query param: Return agents created at or before this time (inclusive).

IncludeArchived param.Field[bool]Optional

Query param: Include archived agents in results. Defaults to false.

Limit param.Field[int64]Optional

Query param: Maximum results per page. Default 20, maximum 100.

Page param.Field[string]Optional

Query param: Opaque pagination cursor from a previous response.



Betas param.Field[[]AnthropicBeta]Optional

Header param: Optional header to specify the beta version(s) you want to use.

string



type AnthropicBeta string

One of the following:

const AnthropicBetaMessageBatches2024\_09\_24 AnthropicBeta = "message-batches-2024-09-24"

const AnthropicBetaPromptCaching2024\_07\_31 AnthropicBeta = "prompt-caching-2024-07-31"

const AnthropicBetaComputerUse2024\_10\_22 AnthropicBeta = "computer-use-2024-10-22"

const AnthropicBetaComputerUse2025\_01\_24 AnthropicBeta = "computer-use-2025-01-24"

const AnthropicBetaPDFs2024\_09\_25 AnthropicBeta = "pdfs-2024-09-25"

const AnthropicBetaTokenCounting2024\_11\_01 AnthropicBeta = "token-counting-2024-11-01"

const AnthropicBetaTokenEfficientTools2025\_02\_19 AnthropicBeta = "token-efficient-tools-2025-02-19"

const AnthropicBetaOutput128k2025\_02\_19 AnthropicBeta = "output-128k-2025-02-19"

const AnthropicBetaFilesAPI2025\_04\_14 AnthropicBeta = "files-api-2025-04-14"

const AnthropicBetaMCPClient2025\_04\_04 AnthropicBeta = "mcp-client-2025-04-04"

const AnthropicBetaMCPClient2025\_11\_20 AnthropicBeta = "mcp-client-2025-11-20"

const AnthropicBetaDevFullThinking2025\_05\_14 AnthropicBeta = "dev-full-thinking-2025-05-14"

const AnthropicBetaInterleavedThinking2025\_05\_14 AnthropicBeta = "interleaved-thinking-2025-05-14"

const AnthropicBetaCodeExecution2025\_05\_22 AnthropicBeta = "code-execution-2025-05-22"

const AnthropicBetaExtendedCacheTTL2025\_04\_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"

const AnthropicBetaContext1m2025\_08\_07 AnthropicBeta = "context-1m-2025-08-07"

const AnthropicBetaContextManagement2025\_06\_27 AnthropicBeta = "context-management-2025-06-27"

const AnthropicBetaModelContextWindowExceeded2025\_08\_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"

const AnthropicBetaSkills2025\_10\_02 AnthropicBeta = "skills-2025-10-02"

const AnthropicBetaFastMode2026\_02\_01 AnthropicBeta = "fast-mode-2026-02-01"

const AnthropicBetaOutput300k2026\_03\_24 AnthropicBeta = "output-300k-2026-03-24"

const AnthropicBetaUserProfiles2026\_03\_24 AnthropicBeta = "user-profiles-2026-03-24"

const AnthropicBetaAdvisorTool2026\_03\_01 AnthropicBeta = "advisor-tool-2026-03-01"

const AnthropicBetaManagedAgents2026\_04\_01 AnthropicBeta = "managed-agents-2026-04-01"

const AnthropicBetaCacheDiagnosis2026\_04\_07 AnthropicBeta = "cache-diagnosis-2026-04-07"

const AnthropicBetaThinkingTokenCount2026\_05\_13 AnthropicBeta = "thinking-token-count-2026-05-13"

const AnthropicBetaServerSideFallback2026\_06\_01 AnthropicBeta = "server-side-fallback-2026-06-01"

const AnthropicBetaFallbackCredit2026\_06\_01 AnthropicBeta = "fallback-credit-2026-06-01"

const AnthropicBetaAgentMemory2026\_07\_22 AnthropicBeta = "agent-memory-2026-07-22"

##### ReturnsExpand Collapse



type BetaManagedAgentsAgent struct{…}

A Managed Agents `agent`.

ID string

ArchivedAt Time

A timestamp in RFC 3339 format

CreatedAt Time

A timestamp in RFC 3339 format

Description string



MCPServers [][BetaManagedAgentsMCPServerURLDefinition](api/beta/agents.md)

Name string

Type BetaManagedAgentsMCPServerURLDefinitionType

URL string

Metadata map[string, string]



Model [BetaManagedAgentsModelConfig](api/beta/agents.md)

Model identifier and configuration.



ID BetaManagedAgentsModel

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



type BetaManagedAgentsModel string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

const BetaManagedAgentsModelClaudeSonnet5 BetaManagedAgentsModel = "claude-sonnet-5"

High-performance model for coding and agents

const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

const BetaManagedAgentsModelClaudeOpus4\_8 BetaManagedAgentsModel = "claude-opus-4-8"

Frontier intelligence for long-running agents and coding

const BetaManagedAgentsModelClaudeOpus4\_7 BetaManagedAgentsModel = "claude-opus-4-7"

Frontier intelligence for long-running agents and coding

const BetaManagedAgentsModelClaudeOpus4\_6 BetaManagedAgentsModel = "claude-opus-4-6"

Most intelligent model for building agents and coding

const BetaManagedAgentsModelClaudeSonnet4\_6 BetaManagedAgentsModel = "claude-sonnet-4-6"

Best combination of speed and intelligence

const BetaManagedAgentsModelClaudeHaiku4\_5 BetaManagedAgentsModel = "claude-haiku-4-5"

Fastest model with near-frontier intelligence

const BetaManagedAgentsModelClaudeHaiku4\_5\_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

const BetaManagedAgentsModelClaudeOpus4\_5 BetaManagedAgentsModel = "claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

const BetaManagedAgentsModelClaudeOpus4\_5\_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

const BetaManagedAgentsModelClaudeSonnet4\_5 BetaManagedAgentsModel = "claude-sonnet-4-5"

High-performance model for agents and coding

const BetaManagedAgentsModelClaudeSonnet4\_5\_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"

High-performance model for agents and coding

string



Speed BetaManagedAgentsModelConfigSpeedOptional

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"

const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"



Multiagent [BetaManagedAgentsMultiagent](api/beta/sessions.md)

Resolved coordinator topology with a concrete agent roster.



Agents [][BetaManagedAgentsAgentReference](api/beta/agents.md)

Agents the coordinator may spawn as session threads, each resolved to a specific version.

ID string

Type BetaManagedAgentsAgentReferenceType

Version int64

Type BetaManagedAgentsMultiagentType

Name string



Skills []BetaManagedAgentsAgentSkillUnion

One of the following:



type BetaManagedAgentsAnthropicSkill struct{…}

A resolved Anthropic-managed skill.

SkillID string

Type BetaManagedAgentsAnthropicSkillType

Version string



type BetaManagedAgentsCustomSkill struct{…}

A resolved user-created custom skill.

SkillID string

Type BetaManagedAgentsCustomSkillType

Version string

System string



Tools []BetaManagedAgentsAgentToolUnion

One of the following:



type BetaManagedAgentsAgentToolset20260401 struct{…}



Configs [][BetaManagedAgentsAgentToolConfig](api/beta/agents.md)

Enabled bool



Name BetaManagedAgentsAgentToolConfigName

Built-in agent tool identifier.

One of the following:

const BetaManagedAgentsAgentToolConfigNameBash BetaManagedAgentsAgentToolConfigName = "bash"

const BetaManagedAgentsAgentToolConfigNameEdit BetaManagedAgentsAgentToolConfigName = "edit"

const BetaManagedAgentsAgentToolConfigNameRead BetaManagedAgentsAgentToolConfigName = "read"

const BetaManagedAgentsAgentToolConfigNameWrite BetaManagedAgentsAgentToolConfigName = "write"

const BetaManagedAgentsAgentToolConfigNameGlob BetaManagedAgentsAgentToolConfigName = "glob"

const BetaManagedAgentsAgentToolConfigNameGrep BetaManagedAgentsAgentToolConfigName = "grep"

const BetaManagedAgentsAgentToolConfigNameWebFetch BetaManagedAgentsAgentToolConfigName = "web\_fetch"

const BetaManagedAgentsAgentToolConfigNameWebSearch BetaManagedAgentsAgentToolConfigName = "web\_search"



PermissionPolicy BetaManagedAgentsAgentToolConfigPermissionPolicyUnion

Permission policy for tool execution.

One of the following:



type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType



type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType



DefaultConfig [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta/agents.md)

Resolved default configuration for agent tools.

Enabled bool



PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion

Permission policy for tool execution.

One of the following:



type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType



type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType

Type BetaManagedAgentsAgentToolset20260401Type



type BetaManagedAgentsMCPToolset struct{…}



Configs [][BetaManagedAgentsMCPToolConfig](api/beta/agents.md)

Enabled bool

Name string



PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion

Permission policy for tool execution.

One of the following:



type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType



type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType



DefaultConfig [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta/agents.md)

Resolved default configuration for all tools from an MCP server.

Enabled bool



PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion

Permission policy for tool execution.

One of the following:



type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType



type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType

MCPServerName string

Type BetaManagedAgentsMCPToolsetType



type BetaManagedAgentsCustomTool struct{…}

A custom tool as returned in API responses.

Description string



InputSchema [BetaManagedAgentsCustomToolInputSchema](api/beta/agents.md)

JSON Schema for custom tool input parameters.

Type Object

Properties map[string, any]Optional

Required []stringOptional

Name string

Type BetaManagedAgentsCustomToolType

Type BetaManagedAgentsAgentType

UpdatedAt Time

A timestamp in RFC 3339 format

Version int64

The agent's current version. Starts at 1 and increments when the agent is modified.

List Agents

Go

```shiki
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  page, err := client.Beta.Agents.List(context.TODO(), anthropic.BetaAgentListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
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
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
