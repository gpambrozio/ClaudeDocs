# Update Agent

Copy page

Java

# Update Agent

[BetaManagedAgentsAgent](api/beta.md) beta().agents().update(AgentUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/agents/{agent\_id}

Update Agent

##### ParametersExpand Collapse

AgentUpdateParams params

Optional<String> agentId

Optional<List<AnthropicBeta>> betas

Optional header to specify the beta version(s) you want to use.

MESSAGE\_BATCHES\_2024\_09\_24("message-batches-2024-09-24")

PROMPT\_CACHING\_2024\_07\_31("prompt-caching-2024-07-31")

COMPUTER\_USE\_2024\_10\_22("computer-use-2024-10-22")

COMPUTER\_USE\_2025\_01\_24("computer-use-2025-01-24")

PDFS\_2024\_09\_25("pdfs-2024-09-25")

TOKEN\_COUNTING\_2024\_11\_01("token-counting-2024-11-01")

TOKEN\_EFFICIENT\_TOOLS\_2025\_02\_19("token-efficient-tools-2025-02-19")

OUTPUT\_128K\_2025\_02\_19("output-128k-2025-02-19")

FILES\_API\_2025\_04\_14("files-api-2025-04-14")

MCP\_CLIENT\_2025\_04\_04("mcp-client-2025-04-04")

MCP\_CLIENT\_2025\_11\_20("mcp-client-2025-11-20")

DEV\_FULL\_THINKING\_2025\_05\_14("dev-full-thinking-2025-05-14")

INTERLEAVED\_THINKING\_2025\_05\_14("interleaved-thinking-2025-05-14")

CODE\_EXECUTION\_2025\_05\_22("code-execution-2025-05-22")

EXTENDED\_CACHE\_TTL\_2025\_04\_11("extended-cache-ttl-2025-04-11")

CONTEXT\_1M\_2025\_08\_07("context-1m-2025-08-07")

CONTEXT\_MANAGEMENT\_2025\_06\_27("context-management-2025-06-27")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED\_2025\_08\_26("model-context-window-exceeded-2025-08-26")

SKILLS\_2025\_10\_02("skills-2025-10-02")

FAST\_MODE\_2026\_02\_01("fast-mode-2026-02-01")

OUTPUT\_300K\_2026\_03\_24("output-300k-2026-03-24")

USER\_PROFILES\_2026\_03\_24("user-profiles-2026-03-24")

ADVISOR\_TOOL\_2026\_03\_01("advisor-tool-2026-03-01")

long version

The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. The request fails if this does not match the server's current version.

Optional<String> description

Description. Up to 2048 characters. Omit to preserve; send empty string or null to clear.

Optional<List<[BetaManagedAgentsUrlMcpServerParams](api/beta.md)>> mcpServers

MCP servers. Full replacement. Omit to preserve; send empty array or null to clear. Names must be unique. Maximum 20.

String name

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

Type type

String url

Endpoint URL for the MCP server.

Optional<Metadata> metadata

Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

Optional<Model> model

Model identifier. Accepts the [model string](about-claude/models/overview.md), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control. Omit to preserve. Cannot be cleared.

enum BetaManagedAgentsModel:

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

class BetaManagedAgentsModelConfigParams:

An object that defines additional configuration control over model use

BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

Optional<String> name

Human-readable name. 1-256 characters. Omit to preserve. Cannot be cleared.

Optional<List<[BetaManagedAgentsSkillParams](api/beta.md)>> skills

Skills. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 20.

class BetaManagedAgentsAnthropicSkillParams:

An Anthropic-managed skill.

String skillId

Identifier of the Anthropic skill (e.g., "xlsx").

Type type

Optional<String> version

Version to pin. Defaults to latest if omitted.

class BetaManagedAgentsCustomSkillParams:

A user-created custom skill.

String skillId

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

Type type

Optional<String> version

Version to pin. Defaults to latest if omitted.

Optional<String> system

System prompt. Up to 100,000 characters. Omit to preserve; send empty string or null to clear.

Optional<List<Tool>> tools

Tool configurations available to the agent. Full replacement. Omit to preserve; send empty array or null to clear. Maximum of 128 tools across all toolsets allowed.

class BetaManagedAgentsAgentToolset20260401Params:

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

Type type

Optional<List<[BetaManagedAgentsAgentToolConfigParams](api/beta.md)>> configs

Per-tool configuration overrides.

Name name

Built-in agent tool identifier.

Accepts one of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")

Optional<Boolean> enabled

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.

Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Optional<[BetaManagedAgentsAgentToolsetDefaultConfigParams](api/beta.md)> defaultConfig

Default configuration for all tools in a toolset.

Optional<Boolean> enabled

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

class BetaManagedAgentsMcpToolsetParams:

Configuration for tools from an MCP server defined in `mcp_servers`.

String mcpServerName

Name of the MCP server. Must match a server name from the mcp\_servers array. 1-255 characters.

Type type

Optional<List<[BetaManagedAgentsMcpToolConfigParams](api/beta.md)>> configs

Per-tool configuration overrides.

String name

Name of the MCP tool to configure. 1-128 characters.

Optional<Boolean> enabled

Whether this tool is enabled. Overrides the `default_config` setting.

Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Optional<[BetaManagedAgentsMcpToolsetDefaultConfigParams](api/beta.md)> defaultConfig

Default configuration for all tools from an MCP server.

Optional<Boolean> enabled

Whether tools are enabled by default. Defaults to true if not specified.

Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

class BetaManagedAgentsCustomToolParams:

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

String description

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

Optional<Properties> properties

JSON Schema properties defining the tool's input parameters.

Optional<List<String>> required

List of required property names.

Optional<Type> type

Must be 'object' for tool input schemas.

String name

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

Type type

##### ReturnsExpand Collapse

class BetaManagedAgentsAgent:

A Managed Agents `agent`.

String id

Optional<LocalDateTime> archivedAt

A timestamp in RFC 3339 format

LocalDateTime createdAt

A timestamp in RFC 3339 format

Optional<String> description

List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> mcpServers

String name

Type type

String url

Metadata metadata

[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.

BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

String name

List<Skill> skills

Accepts one of the following:

class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version

class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system

List<Tool> tools

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401:

List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled

Name name

Built-in agent tool identifier.

Accepts one of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type

class BetaManagedAgentsMcpToolset:

List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type

class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description

[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

Optional<Properties> properties

JSON Schema properties defining the tool's input parameters.

Optional<List<String>> required

List of required property names.

Optional<Type> type

Must be 'object' for tool input schemas.

String name

Type type

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

long version

The agent's current version. Starts at 1 and increments when the agent is modified.

Update Agent

Java

```shiki
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.agents.AgentUpdateParams;
import com.anthropic.models.beta.agents.BetaManagedAgentsAgent;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        AgentUpdateParams params = AgentUpdateParams.builder()
            .agentId("agent_011CZkYpogX7uDKUyvBTophP")
            .version(1)
            .build();
        BetaManagedAgentsAgent betaManagedAgentsAgent = client.beta().agents().update(params);
    }
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
