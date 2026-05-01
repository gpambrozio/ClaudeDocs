# List Sessions

Copy page

Python

# List Sessions

beta.sessions.list(SessionListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsSession](api/beta.md)]

GET/v1/sessions

List Sessions

##### ParametersExpand Collapse

agent\_id: Optional[str]

Filter sessions created with this agent ID.

agent\_version: Optional[int]

Filter by agent version. Only applies when agent\_id is also set.

created\_at\_gt: Optional[Union[str, datetime]]

Return sessions created after this time (exclusive).

created\_at\_gte: Optional[Union[str, datetime]]

Return sessions created at or after this time (inclusive).

created\_at\_lt: Optional[Union[str, datetime]]

Return sessions created before this time (exclusive).

created\_at\_lte: Optional[Union[str, datetime]]

Return sessions created at or before this time (inclusive).

include\_archived: Optional[[bool](api/beta/sessions/list.md)]

When true, includes archived sessions. Default: false (exclude archived).

limit: Optional[int]

Maximum number of results to return.

memory\_store\_id: Optional[str]

Filter sessions whose resources contain a memory\_store with this memory store ID.

order: Optional[Literal["asc", "desc"]]

Sort direction for results, ordered by created\_at. Defaults to desc (newest first).

Accepts one of the following:

"asc"

"desc"

page: Optional[str]

Opaque pagination cursor from a previous response's next\_page.

betas: Optional[List[[AnthropicBetaParam](api/beta.md)]]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

str

Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 20 more]

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

"user-profiles-2026-03-24"

"advisor-tool-2026-03-01"

##### ReturnsExpand Collapse

class BetaManagedAgentsSession: …

A Managed Agents `session`.

id: str

agent: [BetaManagedAgentsSessionAgent](api/beta.md)

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: str

description: Optional[str]

mcp\_servers: List[[BetaManagedAgentsMCPServerURLDefinition](api/beta.md)]

name: str

type: Literal["url"]

url: str

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

version: int

archived\_at: Optional[datetime]

A timestamp in RFC 3339 format

created\_at: datetime

A timestamp in RFC 3339 format

environment\_id: str

metadata: Dict[str, str]

resources: List[[BetaManagedAgentsSessionResource](api/beta.md)]

Accepts one of the following:

class BetaManagedAgentsGitHubRepositoryResource: …

id: str

created\_at: datetime

A timestamp in RFC 3339 format

mount\_path: str

type: Literal["github\_repository"]

updated\_at: datetime

A timestamp in RFC 3339 format

url: str

checkout: Optional[Checkout]

Accepts one of the following:

class BetaManagedAgentsBranchCheckout: …

name: str

Branch name to check out.

type: Literal["branch"]

class BetaManagedAgentsCommitCheckout: …

sha: str

Full commit SHA to check out.

type: Literal["commit"]

class BetaManagedAgentsFileResource: …

id: str

created\_at: datetime

A timestamp in RFC 3339 format

file\_id: str

mount\_path: str

type: Literal["file"]

updated\_at: datetime

A timestamp in RFC 3339 format

class BetaManagedAgentsMemoryStoreResource: …

A memory store attached to an agent session.

memory\_store\_id: str

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: Literal["memory\_store"]

access: Optional[Literal["read\_write", "read\_only"]]

Access mode for an attached memory store.

Accepts one of the following:

"read\_write"

"read\_only"

description: Optional[str]

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

instructions: Optional[str]

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

mount\_path: Optional[str]

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

name: Optional[str]

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

stats: [BetaManagedAgentsSessionStats](api/beta.md)

Timing statistics for a session.

active\_seconds: Optional[float]

Cumulative time in seconds the session spent in running status. Excludes idle time.

duration\_seconds: Optional[float]

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

status: Literal["rescheduling", "running", "idle", "terminated"]

SessionStatus enum

Accepts one of the following:

"rescheduling"

"running"

"idle"

"terminated"

title: Optional[str]

type: Literal["session"]

updated\_at: datetime

A timestamp in RFC 3339 format

usage: [BetaManagedAgentsSessionUsage](api/beta.md)

Cumulative token usage for a session across all turns.

cache\_creation: Optional[BetaManagedAgentsCacheCreationUsage]

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: Optional[int]

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: Optional[int]

Tokens used to create 5-minute ephemeral cache entries.

cache\_read\_input\_tokens: Optional[int]

Total tokens read from prompt cache.

input\_tokens: Optional[int]

Total input tokens consumed across all turns.

output\_tokens: Optional[int]

Total output tokens generated across all turns.

vault\_ids: List[str]

Vault IDs attached to the session at creation. Empty when no vaults were supplied.

List Sessions

Python

```shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.sessions.list()
page = page.data[0]
print(page.id)
```

Response 200

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
      ]
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

##### Returns Examples

Response 200

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
      ]
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

---

*Copyright © Anthropic. All rights reserved.*
