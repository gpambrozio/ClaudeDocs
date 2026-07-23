# Define your agent

Copy page



An agent is a reusable, versioned configuration that defines persona and capabilities. It bundles the model, system prompt, tools, MCP servers, and skills that shape how Claude behaves during a session.

Create the agent once as a reusable resource and reference it by ID each time you [start a session](managed-agents/sessions.md). Agents are versioned and easier to manage across many sessions.



Managed Agents API requests require the `managed-agents-2026-04-01` beta header, except memory store endpoints, which use `agent-memory-2026-07-22` instead. The SDK sets the correct beta header automatically. See [Beta headers](api/beta-headers.md).

##  Agent configuration fields

| Field | Description |
| --- | --- |
| `name` | Required. A human-readable name for the agent. |
| `model` | Required. The Claude [model](about-claude/models/overview.md) that powers the agent. Accepts a model ID string or an object, for example `{"id": "claude-opus-4-8"}`. All Claude 4.5-family and later models are supported. The object form also accepts a `speed` and an `effort` level; see the tips under [Create an agent](#create-an-agent) and [Effort levels](build-with-claude/effort.md). |
| `system` | A [system prompt](build-with-claude/prompt-engineering/claude-prompting-best-practices.md) that defines the agent's behavior and persona. The system prompt is distinct from [user messages](managed-agents/reference.md), which should describe the work to be done. |
| `tools` | The tools available to the agent. Combines [pre-built agent tools](managed-agents/tools.md), [MCP tools](managed-agents/mcp-connector.md), and [custom tools](managed-agents/tools.md). |
| `mcp_servers` | [MCP servers](managed-agents/mcp-connector.md) that provide standardized third-party capabilities. |
| `skills` | [Skills](managed-agents/skills.md) that supply domain-specific context with progressive disclosure. |
| `multiagent` | A coordinator declaration listing the agents this agent can delegate to. See [Multiagent orchestration](managed-agents/multiagent-orchestration.md). |
| `description` | A description of what the agent does. |
| `metadata` | Arbitrary key-value pairs for your own tracking. |

You can also override `model`, `system`, `tools`, `mcp_servers`, and `skills` for a single session without changing the agent. An `effort` level set inside a per-session `model` override isn't applied; set it on the agent instead. See [Override agent configuration for a session](managed-agents/sessions.md).

##  Create an agent

The following example defines a coding agent that uses Claude Opus 4.8 with access to the pre-built agent toolset. The toolset lets the agent write code, read files, search the web, and more. See the [agent tools reference](managed-agents/tools.md) for the full list of supported tools.

The examples use curl, the `ant` CLI, or one of the SDKs. If you haven't set one up, the [quickstart](managed-agents/quickstart.md) covers installation and client setup.

curlCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
agent=$(ant beta:agents create \
  --name "Coding Assistant" \
  --model '{id: claude-opus-4-8}' \
  --system "You are a helpful coding agent." \
  --tool '{type: agent_toolset_20260401}' \
  --format json)

AGENT_ID=$(jq -r '.id' <<< "$agent")
AGENT_VERSION=$(jq -r '.version' <<< "$agent")
```



To use Claude Opus 4.8 or Claude Opus 4.7 with [fast mode](build-with-claude/fast-mode.md), pass `model` as an object, for example: `{"id": "claude-opus-4-8", "speed": "fast"}`. Fast mode for Claude Opus 4.7 is deprecated; see [Fast mode](build-with-claude/fast-mode.md) for the removal date and behavior.



To set the model's effort level, pass `model` as an object, for example: `{"id": "claude-opus-4-8", "effort": "high"}`. The `effort` field accepts a level string (`low`, `medium`, `high`, `xhigh`, or `max`) or an object such as `{"type": "high"}`. See [Effort levels](build-with-claude/effort.md) for what each level does.

The response echoes your configuration and adds `id`, `type`, `version`, `created_at`, `updated_at`, and `archived_at` fields, and fills in `model` fields you omit, such as `effort`, with their defaults. The `version` starts at 1 and increments each time an update changes the agent.

```shiki
{
  "id": "agent_01HqR2k7vXbZ9mNpL3wYcT8f",
  "type": "agent",
  "name": "Coding Assistant",
  "model": {
    "id": "claude-opus-4-8",
    "effort": { "type": "high" },
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



The `default_config` on the toolset shows its default [permission policy](managed-agents/permission-policies.md), `always_allow`, which applies unless you configure one.

##  Update an agent

Updating an agent generates a new version when the configuration changes. The `version` field is optional: supply it for optimistic concurrency (a mismatch returns a 409), or omit it to apply the update unconditionally (last write wins). Updates to archived agents are rejected.

curlCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:agents update \
  --agent-id "$AGENT_ID" \
  --version "$AGENT_VERSION" \
  --system "You are a helpful coding agent. Always write tests."
```

The preceding example supplies `version` from the create response, so the update only applies if nothing else has changed the agent since you read it. To apply an update unconditionally, omit `version` from the request:

curl



```shiki
updated_agent=$(curl -fsSL "https://api.anthropic.com/v1/agents/$AGENT_ID" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d '{
    "description": "Writes and reviews code."
  }')

echo "New version: $(jq -r '.version' <<< "$updated_agent")"
```

###  Update semantics

- **`version`** is optional and must be at least 1 when supplied. When supplied, the request returns a 409 if it doesn't match the agent's current version, even when the fields you send already match the stored values; re-read the agent and retry. When omitted, the update applies unconditionally and the most recent update silently replaces any concurrent one, with no error to either caller. Supplying `version` is the recommended default for interactive callers, and omitting it fits declarative apply loops, such as a CI job that syncs checked-in agent definitions, where the loop owns the agent.
- **Omitted fields are preserved.** You only need to include the fields you want to change.
- **Scalar fields** (`model`, `system`, `name`, `description`) are replaced with the new value. `system` and `description` can be cleared by passing `null`. `model` and `name` are mandatory and cannot be cleared. Within a `model` object you supply, `effort` is the exception: if the model `id` is unchanged, omitting `effort` leaves the stored effort level unchanged. If you change the model `id`, an omitted `effort` resets to the new model's default.
- **Array fields** (`tools`, `mcp_servers`, `skills`) are fully replaced by the new array. To clear an array field entirely, pass `null` or an empty array.
- **`multiagent`** is replaced as a whole, including its `agents` roster. Pass `null` to clear it.
- **Metadata** is merged at the key level. Keys you provide are added or updated. Keys you omit are preserved. To delete a specific key, set its value to `null`.
- **No-op detection.** If the update produces no change relative to the current version, no new version is created and the existing version is returned.
- **Coordinator rosters are not updated.** Coordinators that reference this agent in their `multiagent.agents` roster keep the version that was pinned when the coordinator was created or last updated, even if the reference omits `version`. To delegate to the new version, [update the coordinator](managed-agents/multiagent-orchestration.md) so its roster references it.

##  Agent lifecycle

| Operation | Behavior |
| --- | --- |
| **Update** | Generates a new agent version when the configuration changes. |
| **List versions** | Returns the full version history so you can track changes over time. |
| **Archive** | Makes the agent read-only. New sessions cannot reference it, but existing sessions continue to run. |

###  List versions

Fetch the full version history to track how an agent has changed over time. Results are paginated, and the SDK examples fetch every page automatically.

curlCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:agents:versions list --agent-id "$AGENT_ID"
```

###  Archive an agent

Archiving makes the agent read-only and cannot be undone. Existing sessions continue to run, but new sessions cannot reference the agent. The response sets `archived_at` to the archive timestamp.

curlCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:agents archive --agent-id "$AGENT_ID"
```

##  Next steps

[

Tools

Configure tools available to your agent.](managed-agents/tools.md)[

Skills

Attach reusable, filesystem-based expertise to your agent for domain-specific workflows.](managed-agents/skills.md)[

Start a session

Create a session to run your agent and begin executing tasks.](managed-agents/sessions.md)[

Reference

Event types, self-hosted worker CLI flags, supported MCP server types, rate limits, and branding guidelines for Claude Managed Agents.](managed-agents/reference.md)

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
