# Start a session

Copy page



A session is an agent instance within an environment. Each session references an [agent](managed-agents/agent-setup.md) and an [environment](managed-agents/environments.md) (both created separately), and maintains conversation history across multiple interactions. Sessions follow a two-step lifecycle: first [create the session](#creating-a-session) to provision its sandbox, then [send a user event](#starting-the-session) to start work.



All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.

##  Creating a session

A session requires an `agent` ID and an `environment` ID. Agents are versioned resources; passing in the `agent` ID as a string starts the session with the latest agent version.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:sessions create \
  --agent "$AGENT_ID" \
  --environment-id "$ENVIRONMENT_ID"
```

To pin a session to a specific agent version, pass an object. This lets you control exactly which version runs and stage rollouts of new versions independently.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:sessions create <<YAML
agent:
  type: agent
  id: $AGENT_ID
  version: 1
environment_id: $ENVIRONMENT_ID
YAML
```

###  Override agent configuration for a session

You can pass `agent` in three forms: an agent ID string, a pinned-version object (`type: "agent"`), or an overrides object. The overrides form changes parts of the agent's configuration for a single session. Use it to try a different model or grant an extra tool in one session without versioning the agent. For the overrides form, set `type` to `agent_with_overrides` and pass the agent's `id` and optionally a `version` (omit `version` to use the agent's latest version). Then include any of `model`, `system`, `tools`, `mcp_servers`, or `skills` with the values the session should use.

Each overridable field follows the same three rules:

- **Omit the field:** The session inherits the value from the agent version it references.
- **Set the field to `null`, or to an empty array for list fields:** The session runs with that field cleared. This rule applies in full to `system`, `mcp_servers`, and `skills`. There are two exceptions:
  - `model` is never clearable. A session always needs a model, so `model: null` returns a 400 `agent_model_required` error.
  - Clearing `tools` returns a 400 error when the session's effective `skills` is non-empty, because skills require the `read` tool. Otherwise, `tools: null` and `tools: []` clear the field.
- **Set the field to a value:** The value replaces the agent's value in full. Overrides never merge with the agent's configuration, so a `tools` override must list every tool the session should have.

Overrides apply only to the session you create. They do not modify the agent resource or create a new agent version, so other sessions that reference the same agent are unaffected.

In the response, the `agent` object reflects the configuration the session runs with after the overrides are applied. Its `id` and `version` still identify the agent and version the overrides are applied to. This lets you trace a session back to its base agent.

The following example starts a session that overrides the model and clears the system prompt:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
# The response's `agent` is the resolved snapshot: each override replaces that
# field for this session only, and the agent resource keeps its id and version.
ant beta:sessions create \
  --transform 'agent.{id,version,model,system}' \
  --format json <<YAML
agent:
  type: agent_with_overrides
  id: $AGENT_ID
  model:
    id: claude-sonnet-5
  system: null
environment_id: $ENVIRONMENT_ID
YAML
```



The agent defines how Claude behaves within the session, including the model, system prompt, tools, and MCP servers. See [Define your agent](managed-agents/agent-setup.md) for details.

##  MCP authentication through vaults

If your agent uses MCP tools that require authentication, pass `vault_ids` at session creation to reference a vault containing stored OAuth credentials. Anthropic manages token refresh on your behalf. See [Authenticate with vaults](managed-agents/vaults.md) for how to create vaults and register credentials.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:sessions create <<YAML
agent: $AGENT_ID
environment_id: $ENVIRONMENT_ID
vault_ids:
  - $VAULT_ID
YAML
```

##  Starting the session

Creating a session provisions the environment's sandbox but does not start any work. To delegate a task, send events to the session using a [user event](managed-agents/reference.md). The session acts as a state machine that tracks progress while events drive the actual execution.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:sessions:events send \
  --session-id "$SESSION_ID" <<'YAML'
events:
  - type: user.message
    content:
      - type: text
        text: List the files in the working directory.
YAML
```

See [Session event stream](managed-agents/events-and-streaming.md) for how to stream the agent's responses and handle tool confirmations.

See [Session statuses](managed-agents/session-operations.md) for the statuses a session moves through.

##  Next steps

[

Session operations

Retrieve, list, update, archive, and delete Claude Managed Agents sessions.](managed-agents/session-operations.md)[

Session event stream

Send events, stream responses, and interrupt or redirect your session mid-execution.](managed-agents/events-and-streaming.md)[Scheduled deployments

Create and manage deployments with the Claude API: run an agent on a recurring cron schedule and inspect its run history.](managed-agents/scheduled-deployments.md)

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
