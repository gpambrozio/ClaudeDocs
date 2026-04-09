# Create Session

Copy page

TypeScript

# Create Session

client.beta.sessions.create(SessionCreateParams { agent, environment\_id, metadata, 4 more } params, RequestOptionsoptions?): [BetaManagedAgentsSession](api/beta.md) { id, agent, archived\_at, 11 more }

POST/v1/sessions

Create Session

##### ParametersExpand Collapse

params: SessionCreateParams { agent, environment\_id, metadata, 4 more }

agent: string | [BetaManagedAgentsAgentParams](api/beta.md) { id, type, version }

Body param: Agent identifier. Accepts the `agent` ID string, which pins the latest version for the session, or an `agent` object with both id and version specified.

Accepts one of the following:

string

BetaManagedAgentsAgentParams { id, type, version }

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: string

The `agent` ID.

type: "agent"

version?: number

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

environment\_id: string

Body param: ID of the `environment` defining the container configuration for this session.

metadata?: Record<string, string>

Body param: Arbitrary key-value metadata attached to the session.

resources?: Array<[BetaManagedAgentsGitHubRepositoryResourceParams](api/beta.md) { authorization\_token, type, url, 2 more }  | [BetaManagedAgentsFileResourceParams](api/beta.md) { file\_id, type, mount\_path } >

Body param: Resources (e.g. repositories, files) to mount into the session's container.

Accepts one of the following:

BetaManagedAgentsGitHubRepositoryResourceParams { authorization\_token, type, url, 2 more }

Mount a GitHub repository into the session's container.

authorization\_token: string

GitHub authorization token used to clone the repository.

type: "github\_repository"

url: string

Github URL of the repository

checkout?: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }  | null

Branch or commit to check out. Defaults to the repository's default branch.

Accepts one of the following:

BetaManagedAgentsBranchCheckout { name, type }

name: string

Branch name to check out.

type: "branch"

BetaManagedAgentsCommitCheckout { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

mount\_path?: string | null

Mount path in the container. Defaults to `/workspace/<repo-name>`.

BetaManagedAgentsFileResourceParams { file\_id, type, mount\_path }

Mount a file uploaded via the Files API into the session.

file\_id: string

ID of a previously uploaded file.

type: "file"

mount\_path?: string | null

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

title?: string | null

Body param: Human-readable session title.

vault\_ids?: Array<string>

Body param: Vault IDs for stored credentials the agent can use during the session.

betas?: Array<[AnthropicBeta](api/beta.md)>

Header param: Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

(string & {})

"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 18 more

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

##### ReturnsExpand Collapse

BetaManagedAgentsSession { id, agent, archived\_at, 11 more }

A Managed Agents `session`.

id: string

agent: [BetaManagedAgentsSessionAgent](api/beta.md) { id, description, mcp\_servers, 7 more }

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: string

description: string | null

mcp\_servers: Array<[BetaManagedAgentsMCPServerURLDefinition](api/beta.md) { name, type, url } >

name: string

type: "url"

url: string

model: [BetaManagedAgentsModelConfig](api/beta.md) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-haiku-4-5" | 5 more

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

(string & {})

speed?: "standard" | "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"

"fast"

name: string

skills: Array<[BetaManagedAgentsAnthropicSkill](api/beta.md) { skill\_id, type, version }  | [BetaManagedAgentsCustomSkill](api/beta.md) { skill\_id, type, version } >

Accepts one of the following:

BetaManagedAgentsAnthropicSkill { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string

BetaManagedAgentsCustomSkill { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string | null

tools: Array<[BetaManagedAgentsAgentToolset20260401](api/beta.md) { configs, default\_config, type }  | [BetaManagedAgentsMCPToolset](api/beta.md) { configs, default\_config, mcp\_server\_name, type }  | [BetaManagedAgentsCustomTool](api/beta.md) { description, input\_schema, name, type } >

Accepts one of the following:

BetaManagedAgentsAgentToolset20260401 { configs, default\_config, type }

configs: Array<[BetaManagedAgentsAgentToolConfig](api/beta.md) { enabled, name, permission\_policy } >

enabled: boolean

name: "bash" | "edit" | "read" | 5 more

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

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"

BetaManagedAgentsMCPToolset { configs, default\_config, mcp\_server\_name, type }

configs: Array<[BetaManagedAgentsMCPToolConfig](api/beta.md) { enabled, name, permission\_policy } >

enabled: boolean

name: string

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"

BetaManagedAgentsCustomTool { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: string

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md) { properties, required, type }

JSON Schema for custom tool input parameters.

properties?: Record<string, unknown> | null

JSON Schema properties defining the tool's input parameters.

required?: Array<string>

List of required property names.

type?: "object"

Must be 'object' for tool input schemas.

name: string

type: "custom"

type: "agent"

version: number

archived\_at: string | null

A timestamp in RFC 3339 format

created\_at: string

A timestamp in RFC 3339 format

environment\_id: string

metadata: Record<string, string>

resources: Array<[BetaManagedAgentsSessionResource](api/beta.md)>

Accepts one of the following:

BetaManagedAgentsGitHubRepositoryResource { id, created\_at, mount\_path, 4 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

mount\_path: string

type: "github\_repository"

updated\_at: string

A timestamp in RFC 3339 format

url: string

checkout?: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }  | null

Accepts one of the following:

BetaManagedAgentsBranchCheckout { name, type }

name: string

Branch name to check out.

type: "branch"

BetaManagedAgentsCommitCheckout { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

BetaManagedAgentsFileResource { id, created\_at, file\_id, 3 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

file\_id: string

mount\_path: string

type: "file"

updated\_at: string

A timestamp in RFC 3339 format

stats: [BetaManagedAgentsSessionStats](api/beta.md) { active\_seconds, duration\_seconds }

Timing statistics for a session.

active\_seconds?: number

Cumulative time in seconds the session spent in running status. Excludes idle time.

duration\_seconds?: number

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

status: "rescheduling" | "running" | "idle" | "terminated"

SessionStatus enum

Accepts one of the following:

"rescheduling"

"running"

"idle"

"terminated"

title: string | null

type: "session"

updated\_at: string

A timestamp in RFC 3339 format

usage: [BetaManagedAgentsSessionUsage](api/beta.md) { cache\_creation, cache\_read\_input\_tokens, input\_tokens, output\_tokens }

Cumulative token usage for a session across all turns.

cache\_creation?: [BetaManagedAgentsCacheCreationUsage](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens?: number

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens?: number

Tokens used to create 5-minute ephemeral cache entries.

cache\_read\_input\_tokens?: number

Total tokens read from prompt cache.

input\_tokens?: number

Total input tokens consumed across all turns.

output\_tokens?: number

Total output tokens generated across all turns.

vault\_ids: Array<string>

Vault IDs attached to the session at creation. Empty when no vaults were supplied.

Create Session

TypeScript

```shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsSession = await client.beta.sessions.create({
  agent: 'agent_011CZkYpogX7uDKUyvBTophP',
  environment_id: 'env_011CZkZ9X2dpNyB7HsEFoRfW',
});

console.log(betaManagedAgentsSession.id);
```

Response 200

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
  "archived_at": "2019-12-27T18:11:19.117Z",
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
```

##### Returns Examples

Response 200

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
  "archived_at": "2019-12-27T18:11:19.117Z",
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
```

---

*Copyright © Anthropic. All rights reserved.*
