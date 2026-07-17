# MCP connector

Copy page



Claude Managed Agents supports connecting [Model Context Protocol (MCP)](https://modelcontextprotocol.io) servers to your agents. This gives the agent access to external tools, data sources, and services through a standardized protocol.

MCP configuration is split across two steps:

1. **Agent creation** declares which MCP servers the agent connects to, by name and URL.
2. **Session creation** supplies authentication for those servers by referencing a pre-registered vault (see [Authenticate with vaults](managed-agents/vaults.md)).

This separation keeps secrets out of reusable agent definitions while letting each session authenticate with its own credentials.



Managed Agents API requests require the `managed-agents-2026-04-01` beta header, except memory store endpoints, which use `agent-memory-2026-07-22` instead. The SDK sets the correct beta header automatically. See [Beta headers](api/beta-headers.md).

##  Declare MCP servers on the agent

Specify MCP servers in the `mcp_servers` array when creating an agent. Each server needs a `type`, a unique `name`, and a `url`. No authentication tokens are provided at this stage.

Each declared server also needs a matching `mcp_toolset` entry in the `tools` array. The toolset's `mcp_server_name` must match the server's `name`.

curlCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
AGENT_ID=$(ant beta:agents create \
  --name "GitHub Assistant" \
  --model claude-opus-4-8 \
  --mcp-server '{type: url, name: github, url: "https://api.githubcopilot.com/mcp/"}' \
  --tool '{type: agent_toolset_20260401}' \
  --tool '{type: mcp_toolset, mcp_server_name: github}' \
  --transform id --raw-output)
```



The MCP toolset defaults to a permission policy of `always_ask`, which requires user approval before each tool call. See [permission policies](managed-agents/permission-policies.md) to configure this behavior.

###  `mcp_servers` field reference

Each entry in the `mcp_servers` array defines one connection.

| Field | Description |
| --- | --- |
| `type` | Required. Must be `"url"`. |
| `name` | Required. A unique name for this server within the agent (1–255 characters). Used as the `mcp_server_name` in the `tools` array and surfaced on MCP tool events in the [session event stream](managed-agents/events-and-streaming.md). |
| `url` | Required. The endpoint of the remote MCP server (up to 2,048 characters). See [Supported MCP server types](managed-agents/reference.md) for transport requirements. |

Constraints:

- An agent can declare up to 20 MCP servers. Server names must be unique within the array.
- Every `mcp_servers` entry must be referenced by an `mcp_toolset` in the `tools` array, and every `mcp_toolset` must reference a declared server. The API rejects agent definitions with unreferenced servers or dangling toolsets.

##  Configure which MCP tools are available

The `mcp_toolset` entry supports the same `default_config` and `configs` shape as the built-in agent toolset, applied to the tools the MCP server exposes. The `name` in each `configs` entry is the bare tool name as reported by the server.

By default all tools exposed by the MCP server are enabled. To enable only specific tools, set `default_config.enabled` to `false` and explicitly enable the tools you want:

```shiki
{
  "type": "mcp_toolset",
  "mcp_server_name": "github",
  "default_config": { "enabled": false },
  "configs": [
    { "name": "get_issue", "enabled": true },
    { "name": "list_issues", "enabled": true },
    { "name": "add_issue_comment", "enabled": true }
  ]
}
```



This pattern is useful when a server exposes many tools but the agent only needs a few, or when you want tools added by the server operator to stay off until you review them.

To disable specific tools while keeping the rest enabled, omit `default_config` and set `enabled: false` on individual entries:

```shiki
{
  "type": "mcp_toolset",
  "mcp_server_name": "github",
  "configs": [{ "name": "delete_repository", "enabled": false }]
}
```



See [configuring the toolset](managed-agents/tools.md) for the general `default_config` / `configs` pattern, and [MCP toolset permissions](managed-agents/permission-policies.md) for setting `permission_policy` on MCP tools and handling confirmation requests.

###  MCP tool output handling

When an MCP tool output exceeds 100,000 tokens, it is automatically written to a file in the sandbox. The model receives a truncated preview with the file path and can read the full content from there.

##  Provide authentication at session creation

When starting a session, pass `vault_ids` to provide credentials for your MCP servers. Vaults are collections of credentials that you register once and reference by ID. See [Authenticate with vaults](managed-agents/vaults.md) for how to create vaults and manage credentials.

curlCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    vault_ids=[vault.id],
)
```

Credentials are matched by URL, so the vault must contain a credential whose `mcp_server_url` exactly matches the `url` declared in `mcp_servers`. If none matches, the connection is attempted unauthenticated. See [Add a credential](managed-agents/vaults.md) for the `static_bearer` and `mcp_oauth` credential types.

###  Handle connection and authentication failures

Session creation does not validate MCP connectivity or credentials. If an MCP server is unreachable or rejects the supplied credential, the session still starts and interaction remains possible. A [`session.error`](managed-agents/events-and-streaming.md) event is emitted with the `mcp_server_name` of the affected server and a `retry_status`:

| Error type | Meaning |
| --- | --- |
| `mcp_connection_failed_error` | The MCP server could not be reached (network error, timeout, or non-authentication HTTP failure). |
| `mcp_authentication_failed_error` | The MCP server was reached but rejected the credential from the attached vault. |

You can decide whether to block further interaction on this error, trigger a credential rotation, or let the session continue without the affected server's tools. The connection is retried on the next `session.status_idle` to `session.status_running` transition.

##  Next steps

[

Permission policies

Control when agent and MCP tools run.](managed-agents/permission-policies.md)[

Session event stream

Send events, stream responses, and interrupt or redirect your session mid-execution.](managed-agents/events-and-streaming.md)[

Supported MCP server types

Transport requirements for remote MCP servers.](managed-agents/reference.md)

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
