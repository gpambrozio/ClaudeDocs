# Create Agent

Copy page

Python

# Create Agent

beta.agents.create(AgentCreateParams\*\*kwargs)  -> [BetaManagedAgentsAgent](api/beta.md)

POST/v1/agents

Create Agent

##### ParametersExpand Collapse

model: [Model](api/beta/agents/create.md)

Model identifier. Accepts the [model string](about-claude/models/overview.md), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control

Accepts one of the following:

Union[Literal["claude-opus-4-7", "claude-opus-4-6", "claude-sonnet-4-6", 6 more], str]

Accepts one of the following:

Literal["claude-opus-4-7", "claude-opus-4-6", "claude-sonnet-4-6", 6 more]

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

Accepts one of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

str

class BetaManagedAgentsModelConfigParams: …

An object that defines additional configuration control over model use

id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

Literal["claude-opus-4-7", "claude-opus-4-6", "claude-sonnet-4-6", 6 more]

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

Accepts one of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

str

speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"

"fast"

name: str

Human-readable name for the agent. 1-256 characters.

description: Optional[str]

Description of what the agent does. Up to 2048 characters.

mcp\_servers: Optional[Iterable[[BetaManagedAgentsURLMCPServerParams](api/beta.md)]]

MCP servers this agent connects to. Maximum 20. Names must be unique within the array.

name: str

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

type: Literal["url"]

url: str

Endpoint URL for the MCP server.

metadata: Optional[Dict[str, str]]

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

skills: Optional[Iterable[[BetaManagedAgentsSkillParams](api/beta.md)]]

Skills available to the agent. Maximum 20.

Accepts one of the following:

class BetaManagedAgentsAnthropicSkillParams: …

An Anthropic-managed skill.

skill\_id: str

Identifier of the Anthropic skill (e.g., "xlsx").

type: Literal["anthropic"]

version: Optional[str]

Version to pin. Defaults to latest if omitted.

class BetaManagedAgentsCustomSkillParams: …

A user-created custom skill.

skill\_id: str

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

type: Literal["custom"]

version: Optional[str]

Version to pin. Defaults to latest if omitted.

system: Optional[str]

System prompt for the agent. Up to 100,000 characters.

tools: Optional[Iterable[Tool]]

Tool configurations available to the agent. Maximum of 128 tools across all toolsets allowed.

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401Params: …

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

type: Literal["agent\_toolset\_20260401"]

configs: Optional[List[[BetaManagedAgentsAgentToolConfigParams](api/beta.md)]]

Per-tool configuration overrides.

name: Literal["bash", "edit", "read", 5 more]

Built-in agent tool identifier.

Accepts one of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

enabled: Optional[bool]

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.

permission\_policy: Optional[PermissionPolicy]

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

default\_config: Optional[BetaManagedAgentsAgentToolsetDefaultConfigParams]

Default configuration for all tools in a toolset.

enabled: Optional[bool]

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

permission\_policy: Optional[PermissionPolicy]

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

class BetaManagedAgentsMCPToolsetParams: …

Configuration for tools from an MCP server defined in `mcp_servers`.

mcp\_server\_name: str

Name of the MCP server. Must match a server name from the mcp\_servers array. 1-255 characters.

type: Literal["mcp\_toolset"]

configs: Optional[List[[BetaManagedAgentsMCPToolConfigParams](api/beta.md)]]

Per-tool configuration overrides.

name: str

Name of the MCP tool to configure. 1-128 characters.

enabled: Optional[bool]

Whether this tool is enabled. Overrides the `default_config` setting.

permission\_policy: Optional[PermissionPolicy]

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

default\_config: Optional[BetaManagedAgentsMCPToolsetDefaultConfigParams]

Default configuration for all tools from an MCP server.

enabled: Optional[bool]

Whether tools are enabled by default. Defaults to true if not specified.

permission\_policy: Optional[PermissionPolicy]

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

class BetaManagedAgentsCustomToolParams: …

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

description: str

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md)

JSON Schema for custom tool input parameters.

properties: Optional[Dict[str, object]]

JSON Schema properties defining the tool's input parameters.

required: Optional[List[str]]

List of required property names.

type: Optional[Literal["object"]]

Must be 'object' for tool input schemas.

name: str

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

type: Literal["custom"]

betas: Optional[List[[AnthropicBetaParam](api/beta.md)]]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

str

Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 19 more]

Accepts one of the following:

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

"advisor-tool-2026-03-01"

##### ReturnsExpand Collapse

class BetaManagedAgentsAgent: …

A Managed Agents `agent`.

id: str

archived\_at: Optional[datetime]

A timestamp in RFC 3339 format

created\_at: datetime

A timestamp in RFC 3339 format

description: Optional[str]

mcp\_servers: List[[BetaManagedAgentsMCPServerURLDefinition](api/beta.md)]

name: str

type: Literal["url"]

url: str

metadata: Dict[str, str]

model: [BetaManagedAgentsModelConfig](api/beta.md)

Model identifier and configuration.

id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

Literal["claude-opus-4-7", "claude-opus-4-6", "claude-sonnet-4-6", 6 more]

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

Accepts one of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

str

speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"

"fast"

name: str

skills: List[Skill]

Accepts one of the following:

class BetaManagedAgentsAnthropicSkill: …

A resolved Anthropic-managed skill.

skill\_id: str

type: Literal["anthropic"]

version: str

class BetaManagedAgentsCustomSkill: …

A resolved user-created custom skill.

skill\_id: str

type: Literal["custom"]

version: str

system: Optional[str]

tools: List[Tool]

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401: …

configs: List[[BetaManagedAgentsAgentToolConfig](api/beta.md)]

enabled: bool

name: Literal["bash", "edit", "read", 5 more]

Built-in agent tool identifier.

Accepts one of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

permission\_policy: PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md)

Resolved default configuration for agent tools.

enabled: bool

permission\_policy: PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

type: Literal["agent\_toolset\_20260401"]

class BetaManagedAgentsMCPToolset: …

configs: List[[BetaManagedAgentsMCPToolConfig](api/beta.md)]

enabled: bool

name: str

permission\_policy: PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md)

Resolved default configuration for all tools from an MCP server.

enabled: bool

permission\_policy: PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

mcp\_server\_name: str

type: Literal["mcp\_toolset"]

class BetaManagedAgentsCustomTool: …

A custom tool as returned in API responses.

description: str

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md)

JSON Schema for custom tool input parameters.

properties: Optional[Dict[str, object]]

JSON Schema properties defining the tool's input parameters.

required: Optional[List[str]]

List of required property names.

type: Optional[Literal["object"]]

Must be 'object' for tool input schemas.

name: str

type: Literal["custom"]

type: Literal["agent"]

updated\_at: datetime

A timestamp in RFC 3339 format

version: int

The agent's current version. Starts at 1 and increments when the agent is modified.

Create Agent

Python

```shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_agent = client.beta.agents.create(
    model="claude-sonnet-4-6",
    name="My First Agent",
)
print(beta_managed_agents_agent.id)
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
