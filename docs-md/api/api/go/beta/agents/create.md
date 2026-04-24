# Create Agent

Copy page

Go

# Create Agent

client.Beta.Agents.New(ctx, params) (\*[BetaManagedAgentsAgent](api/beta.md), error)

POST/v1/agents

Create Agent

##### ParametersExpand Collapse

params BetaAgentNewParams

Model param.Field[[BetaManagedAgentsModelConfigParamsResp](api/beta.md)]

Body param: Model identifier. Accepts the [model string](about-claude/models/overview.md), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control

type BetaManagedAgentsModelConfigParamsResp struct{…}

An object that defines additional configuration control over model use

ID BetaManagedAgentsModel

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

type BetaManagedAgentsModel string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

const BetaManagedAgentsModelClaudeOpus4\_7 BetaManagedAgentsModel = "claude-opus-4-7"

Frontier intelligence for long-running agents and coding

const BetaManagedAgentsModelClaudeOpus4\_6 BetaManagedAgentsModel = "claude-opus-4-6"

Most intelligent model for building agents and coding

const BetaManagedAgentsModelClaudeSonnet4\_6 BetaManagedAgentsModel = "claude-sonnet-4-6"

Best combination of speed and intelligence

const BetaManagedAgentsModelClaudeHaiku4\_5 BetaManagedAgentsModel = "claude-haiku-4-5"

Fastest model with near-frontier intelligence

const BetaManagedAgentsModelClaudeHaiku4\_5\_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

const BetaManagedAgentsModelClaudeOpus4\_5 BetaManagedAgentsModel = "claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

const BetaManagedAgentsModelClaudeOpus4\_5\_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

const BetaManagedAgentsModelClaudeSonnet4\_5 BetaManagedAgentsModel = "claude-sonnet-4-5"

High-performance model for agents and coding

const BetaManagedAgentsModelClaudeSonnet4\_5\_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"

High-performance model for agents and coding

string

Speed BetaManagedAgentsModelConfigParamsSpeedoptional

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

const BetaManagedAgentsModelConfigParamsSpeedStandard BetaManagedAgentsModelConfigParamsSpeed = "standard"

const BetaManagedAgentsModelConfigParamsSpeedFast BetaManagedAgentsModelConfigParamsSpeed = "fast"

Name param.Field[string]

Body param: Human-readable name for the agent. 1-256 characters.

Description param.Field[string]optional

Body param: Description of what the agent does. Up to 2048 characters.

MCPServers param.Field[[][BetaManagedAgentsURLMCPServerParamsResp](api/beta.md)]optional

Body param: MCP servers this agent connects to. Maximum 20. Names must be unique within the array.

Name string

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

Type BetaManagedAgentsURLMCPServerParamsType

URL string

Endpoint URL for the MCP server.

Metadata param.Field[map[string, string]]optional

Body param: Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

Skills param.Field[[][BetaManagedAgentsSkillParamsUnionResp](api/beta.md)]optional

Body param: Skills available to the agent. Maximum 20.

type BetaManagedAgentsAnthropicSkillParamsResp struct{…}

An Anthropic-managed skill.

SkillID string

Identifier of the Anthropic skill (e.g., "xlsx").

Type BetaManagedAgentsAnthropicSkillParamsType

Version stringoptional

Version to pin. Defaults to latest if omitted.

type BetaManagedAgentsCustomSkillParamsResp struct{…}

A user-created custom skill.

SkillID string

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

Type BetaManagedAgentsCustomSkillParamsType

Version stringoptional

Version to pin. Defaults to latest if omitted.

System param.Field[string]optional

Body param: System prompt for the agent. Up to 100,000 characters.

Tools param.Field[[]BetaAgentNewParamsToolUnion]optional

Body param: Tool configurations available to the agent. Maximum of 128 tools across all toolsets allowed.

type BetaManagedAgentsAgentToolset20260401ParamsResp struct{…}

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

Type BetaManagedAgentsAgentToolset20260401ParamsType

Configs [][BetaManagedAgentsAgentToolConfigParamsResp](api/beta.md)optional

Per-tool configuration overrides.

Name BetaManagedAgentsAgentToolConfigParamsName

Built-in agent tool identifier.

Accepts one of the following:

const BetaManagedAgentsAgentToolConfigParamsNameBash BetaManagedAgentsAgentToolConfigParamsName = "bash"

const BetaManagedAgentsAgentToolConfigParamsNameEdit BetaManagedAgentsAgentToolConfigParamsName = "edit"

const BetaManagedAgentsAgentToolConfigParamsNameRead BetaManagedAgentsAgentToolConfigParamsName = "read"

const BetaManagedAgentsAgentToolConfigParamsNameWrite BetaManagedAgentsAgentToolConfigParamsName = "write"

const BetaManagedAgentsAgentToolConfigParamsNameGlob BetaManagedAgentsAgentToolConfigParamsName = "glob"

const BetaManagedAgentsAgentToolConfigParamsNameGrep BetaManagedAgentsAgentToolConfigParamsName = "grep"

const BetaManagedAgentsAgentToolConfigParamsNameWebFetch BetaManagedAgentsAgentToolConfigParamsName = "web\_fetch"

const BetaManagedAgentsAgentToolConfigParamsNameWebSearch BetaManagedAgentsAgentToolConfigParamsName = "web\_search"

Enabled booloptional

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.

PermissionPolicy BetaManagedAgentsAgentToolConfigParamsPermissionPolicyUnionRespoptional

Permission policy for tool execution.

Accepts one of the following:

type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType

type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType

DefaultConfig [BetaManagedAgentsAgentToolsetDefaultConfigParamsResp](api/beta.md)optional

Default configuration for all tools in a toolset.

Enabled booloptional

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigParamsPermissionPolicyUnionRespoptional

Permission policy for tool execution.

Accepts one of the following:

type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType

type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType

type BetaManagedAgentsMCPToolsetParamsResp struct{…}

Configuration for tools from an MCP server defined in `mcp_servers`.

MCPServerName string

Name of the MCP server. Must match a server name from the mcp\_servers array. 1-255 characters.

Type BetaManagedAgentsMCPToolsetParamsType

Configs [][BetaManagedAgentsMCPToolConfigParamsResp](api/beta.md)optional

Per-tool configuration overrides.

Name string

Name of the MCP tool to configure. 1-128 characters.

Enabled booloptional

Whether this tool is enabled. Overrides the `default_config` setting.

PermissionPolicy BetaManagedAgentsMCPToolConfigParamsPermissionPolicyUnionRespoptional

Permission policy for tool execution.

Accepts one of the following:

type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType

type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType

DefaultConfig [BetaManagedAgentsMCPToolsetDefaultConfigParamsResp](api/beta.md)optional

Default configuration for all tools from an MCP server.

Enabled booloptional

Whether tools are enabled by default. Defaults to true if not specified.

PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigParamsPermissionPolicyUnionRespoptional

Permission policy for tool execution.

Accepts one of the following:

type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType

type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType

type BetaManagedAgentsCustomToolParamsResp struct{…}

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

Description string

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

InputSchema [BetaManagedAgentsCustomToolInputSchema](api/beta.md)

JSON Schema for custom tool input parameters.

Properties map[string, any]optional

JSON Schema properties defining the tool's input parameters.

Required []stringoptional

List of required property names.

Type BetaManagedAgentsCustomToolInputSchemaTypeoptional

Must be 'object' for tool input schemas.

Name string

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

Type BetaManagedAgentsCustomToolParamsType

Betas param.Field[[]AnthropicBeta]optional

Header param: Optional header to specify the beta version(s) you want to use.

string

type AnthropicBeta string

Accepts one of the following:

const AnthropicBetaMessageBatches2024\_09\_24 AnthropicBeta = "message-batches-2024-09-24"

const AnthropicBetaPromptCaching2024\_07\_31 AnthropicBeta = "prompt-caching-2024-07-31"

const AnthropicBetaComputerUse2024\_10\_22 AnthropicBeta = "computer-use-2024-10-22"

const AnthropicBetaComputerUse2025\_01\_24 AnthropicBeta = "computer-use-2025-01-24"

const AnthropicBetaPDFs2024\_09\_25 AnthropicBeta = "pdfs-2024-09-25"

const AnthropicBetaTokenCounting2024\_11\_01 AnthropicBeta = "token-counting-2024-11-01"

const AnthropicBetaTokenEfficientTools2025\_02\_19 AnthropicBeta = "token-efficient-tools-2025-02-19"

const AnthropicBetaOutput128k2025\_02\_19 AnthropicBeta = "output-128k-2025-02-19"

const AnthropicBetaFilesAPI2025\_04\_14 AnthropicBeta = "files-api-2025-04-14"

const AnthropicBetaMCPClient2025\_04\_04 AnthropicBeta = "mcp-client-2025-04-04"

const AnthropicBetaMCPClient2025\_11\_20 AnthropicBeta = "mcp-client-2025-11-20"

const AnthropicBetaDevFullThinking2025\_05\_14 AnthropicBeta = "dev-full-thinking-2025-05-14"

const AnthropicBetaInterleavedThinking2025\_05\_14 AnthropicBeta = "interleaved-thinking-2025-05-14"

const AnthropicBetaCodeExecution2025\_05\_22 AnthropicBeta = "code-execution-2025-05-22"

const AnthropicBetaExtendedCacheTTL2025\_04\_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"

const AnthropicBetaContext1m2025\_08\_07 AnthropicBeta = "context-1m-2025-08-07"

const AnthropicBetaContextManagement2025\_06\_27 AnthropicBeta = "context-management-2025-06-27"

const AnthropicBetaModelContextWindowExceeded2025\_08\_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"

const AnthropicBetaSkills2025\_10\_02 AnthropicBeta = "skills-2025-10-02"

const AnthropicBetaFastMode2026\_02\_01 AnthropicBeta = "fast-mode-2026-02-01"

const AnthropicBetaOutput300k2026\_03\_24 AnthropicBeta = "output-300k-2026-03-24"

const AnthropicBetaAdvisorTool2026\_03\_01 AnthropicBeta = "advisor-tool-2026-03-01"

##### ReturnsExpand Collapse

type BetaManagedAgentsAgent struct{…}

A Managed Agents `agent`.

ID string

ArchivedAt Time

A timestamp in RFC 3339 format

CreatedAt Time

A timestamp in RFC 3339 format

Description string

MCPServers [][BetaManagedAgentsMCPServerURLDefinition](api/beta.md)

Name string

Type BetaManagedAgentsMCPServerURLDefinitionType

URL string

Metadata map[string, string]

Model [BetaManagedAgentsModelConfig](api/beta.md)

Model identifier and configuration.

ID BetaManagedAgentsModel

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

type BetaManagedAgentsModel string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

const BetaManagedAgentsModelClaudeOpus4\_7 BetaManagedAgentsModel = "claude-opus-4-7"

Frontier intelligence for long-running agents and coding

const BetaManagedAgentsModelClaudeOpus4\_6 BetaManagedAgentsModel = "claude-opus-4-6"

Most intelligent model for building agents and coding

const BetaManagedAgentsModelClaudeSonnet4\_6 BetaManagedAgentsModel = "claude-sonnet-4-6"

Best combination of speed and intelligence

const BetaManagedAgentsModelClaudeHaiku4\_5 BetaManagedAgentsModel = "claude-haiku-4-5"

Fastest model with near-frontier intelligence

const BetaManagedAgentsModelClaudeHaiku4\_5\_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

const BetaManagedAgentsModelClaudeOpus4\_5 BetaManagedAgentsModel = "claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

const BetaManagedAgentsModelClaudeOpus4\_5\_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

const BetaManagedAgentsModelClaudeSonnet4\_5 BetaManagedAgentsModel = "claude-sonnet-4-5"

High-performance model for agents and coding

const BetaManagedAgentsModelClaudeSonnet4\_5\_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"

High-performance model for agents and coding

string

Speed BetaManagedAgentsModelConfigSpeedoptional

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"

const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"

Name string

Skills []BetaManagedAgentsAgentSkillUnion

Accepts one of the following:

type BetaManagedAgentsAnthropicSkill struct{…}

A resolved Anthropic-managed skill.

SkillID string

Type BetaManagedAgentsAnthropicSkillType

Version string

type BetaManagedAgentsCustomSkill struct{…}

A resolved user-created custom skill.

SkillID string

Type BetaManagedAgentsCustomSkillType

Version string

System string

Tools []BetaManagedAgentsAgentToolUnion

Accepts one of the following:

type BetaManagedAgentsAgentToolset20260401 struct{…}

Configs [][BetaManagedAgentsAgentToolConfig](api/beta.md)

Enabled bool

Name BetaManagedAgentsAgentToolConfigName

Built-in agent tool identifier.

Accepts one of the following:

const BetaManagedAgentsAgentToolConfigNameBash BetaManagedAgentsAgentToolConfigName = "bash"

const BetaManagedAgentsAgentToolConfigNameEdit BetaManagedAgentsAgentToolConfigName = "edit"

const BetaManagedAgentsAgentToolConfigNameRead BetaManagedAgentsAgentToolConfigName = "read"

const BetaManagedAgentsAgentToolConfigNameWrite BetaManagedAgentsAgentToolConfigName = "write"

const BetaManagedAgentsAgentToolConfigNameGlob BetaManagedAgentsAgentToolConfigName = "glob"

const BetaManagedAgentsAgentToolConfigNameGrep BetaManagedAgentsAgentToolConfigName = "grep"

const BetaManagedAgentsAgentToolConfigNameWebFetch BetaManagedAgentsAgentToolConfigName = "web\_fetch"

const BetaManagedAgentsAgentToolConfigNameWebSearch BetaManagedAgentsAgentToolConfigName = "web\_search"

PermissionPolicy BetaManagedAgentsAgentToolConfigPermissionPolicyUnion

Permission policy for tool execution.

Accepts one of the following:

type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType

type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType

DefaultConfig [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md)

Resolved default configuration for agent tools.

Enabled bool

PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion

Permission policy for tool execution.

Accepts one of the following:

type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType

type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType

Type BetaManagedAgentsAgentToolset20260401Type

type BetaManagedAgentsMCPToolset struct{…}

Configs [][BetaManagedAgentsMCPToolConfig](api/beta.md)

Enabled bool

Name string

PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion

Permission policy for tool execution.

Accepts one of the following:

type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType

type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType

DefaultConfig [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md)

Resolved default configuration for all tools from an MCP server.

Enabled bool

PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion

Permission policy for tool execution.

Accepts one of the following:

type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType

type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType

MCPServerName string

Type BetaManagedAgentsMCPToolsetType

type BetaManagedAgentsCustomTool struct{…}

A custom tool as returned in API responses.

Description string

InputSchema [BetaManagedAgentsCustomToolInputSchema](api/beta.md)

JSON Schema for custom tool input parameters.

Properties map[string, any]optional

JSON Schema properties defining the tool's input parameters.

Required []stringoptional

List of required property names.

Type BetaManagedAgentsCustomToolInputSchemaTypeoptional

Must be 'object' for tool input schemas.

Name string

Type BetaManagedAgentsCustomToolType

Type BetaManagedAgentsAgentType

UpdatedAt Time

A timestamp in RFC 3339 format

Version int64

The agent's current version. Starts at 1 and increments when the agent is modified.

Create Agent

Go

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
  betaManagedAgentsAgent, err := client.Beta.Agents.New(context.TODO(), anthropic.BetaAgentNewParams{
    Model: anthropic.BetaManagedAgentsModelConfigParams{
      ID: anthropic.BetaManagedAgentsModelClaudeOpus4_6,
    },
    Name: "My First Agent",
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsAgent.ID)
}
```

Response 200

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
