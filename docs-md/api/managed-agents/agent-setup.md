# Define your agent

Copy page

An agent is a reusable, versioned configuration that defines persona and capabilities. It bundles the model, system prompt, tools, MCP servers, and skills that shape how Claude behaves during a session.

Create the agent once as a reusable resource and reference it by ID each time you [start a session](managed-agents/sessions.md). Agents are versioned and easier to manage across many sessions.

All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.

## Agent configuration fields

| Field | Description |
| --- | --- |
| `name` | Required. A human-readable name for the agent. |
| `model` | Required. The Claude [model](about-claude/models/overview.md) that powers the agent. All Claude 4.5 and later models are supported. |
| `system` | A [system prompt](build-with-claude/prompt-engineering/claude-prompting-best-practices.md) that defines the agent's behavior and persona. The system prompt is distinct from [user messages](managed-agents/events-and-streaming.md), which should describe the work to be done. |
| `tools` | The tools available to the agent. Combines [pre-built agent tools](managed-agents/tools.md), [MCP tools](managed-agents/mcp-connector.md), and [custom tools](managed-agents/tools.md). |
| `mcp_servers` | MCP servers that provide standardized third-party capabilities. |
| `skills` | [Skills](managed-agents/skills.md) that supply domain-specific context with progressive disclosure. |
| `callable_agents` | Other agents this agent can invoke for [multi-agent orchestration](managed-agents/multi-agent.md). This is a research preview feature; [request access](https://claude.com/form/claude-managed-agents) to try it. |
| `description` | A description of what the agent does. |
| `metadata` | Arbitrary key-value pairs for your own tracking. |

## Create an agent

The following example defines a coding agent that uses Claude Sonnet 4.6 with access to the pre-built agent toolset. The toolset lets the agent write code, read files, search the web, and more. See the [agent tools reference](managed-agents/tools.md) for the full list of supported tools.

CLI

```shiki
ant beta:agents create \
  --name "Coding Assistant" \
  --model claude-sonnet-4-6 \
  --system "You are a helpful coding agent." \
  --tool '{type: agent_toolset_20260401}'
```

To use Claude Opus 4.6 with [fast mode](build-with-claude/fast-mode.md), pass `model` as an object: `{"id": "claude-opus-4-6", "speed": "fast"}`.

The response echoes your configuration and adds `id`, `version`, `created_at`, `updated_at`, and `archived_at` fields. The `version` starts at 1 and increments each time you update the agent.

```shiki
{
  "id": "agent_01HqR2k7vXbZ9mNpL3wYcT8f",
  "type": "agent",
  "name": "Coding Assistant",
  "model": {
    "id": "claude-sonnet-4-6",
    "speed": "standard"
  },
  "system": "You are a helpful coding agent.",
  "description": null,
  "tools": [
    {
      "type": "agent_toolset_20260401",
      "default_config": {
        "permission_policy": { "type": "always_allow" }
      }
    }
  ],
  "skills": [],
  "mcp_servers": [],
  "metadata": {},
  "version": 1,
  "created_at": "2026-04-03T18:24:10.412Z",
  "updated_at": "2026-04-03T18:24:10.412Z",
  "archived_at": null
}
```

## Update an agent

Updating an agent generates a new version. Pass the current `version` to ensure you're updating from a known state.

CLI

```shiki
ant beta:agents update \
  --agent-id "$AGENT_ID" \
  --version "$AGENT_VERSION" \
  --system "You are a helpful coding agent. Always write tests."
```

### Update semantics

- **Omitted fields are preserved.** You only need to include the fields you want to change.
- **Scalar fields** (`model`, `system`, `name`, etc.) are replaced with the new value. `system` and `description` can be cleared by passing `null`. `model` and `name` are mandatory and cannot be cleared.
- **Array fields** (`tools`, `mcp_servers`, `skills`, `callable_agents`) are fully replaced by the new array. To clear an array field entirely, pass `null` or an empty array.
- **Metadata** is merged at the key level. Keys you provide are added or updated. Keys you omit are preserved. To delete a specific key, set its value to an empty string.
- **No-op detection.** If the update produces no change relative to the current version, no new version is created and the existing version is returned.

## Agent lifecycle

| Operation | Behavior |
| --- | --- |
| **Update** | Generates a new agent version. |
| **List versions** | Fetch the full version history to track changes over time. |
| **Archive** | The agent becomes read-only. New sessions cannot reference it, but existing sessions continue to run. |

### List versions

Fetch the full version history to track how an agent has changed over time.

CLI

```shiki
ant beta:agents:versions list --agent-id "$AGENT_ID"
```

### Archive an agent

Archiving makes the agent read-only. Existing sessions continue to run, but new sessions cannot reference the agent. The response sets `archived_at` to the archive timestamp.

CLI

```shiki
ant beta:agents archive --agent-id "$AGENT_ID"
```

## Next steps

- [Configure tools](managed-agents/tools.md) to customize which capabilities the agent can use.
- [Attach skills](managed-agents/skills.md) for domain-specific expertise.
- [Start a session](managed-agents/sessions.md) that references your agent.

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
