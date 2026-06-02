# Start a session

Copy page

A session is an agent instance within an environment. Each session references an [agent](managed-agents/agent-setup.md) and an [environment](managed-agents/environments.md) (both created separately), and maintains conversation history across multiple interactions. Sessions follow a two-step lifecycle: first [create the session](#creating-a-session) to provision its sandbox, then [send a user event](#starting-the-session) to start work.

All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.

## Creating a session

A session requires an `agent` ID and an `environment` ID. Agents are versioned resources; passing in the `agent` ID as a string starts the session with the latest agent version.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
ant beta:sessions create \
  --agent "$AGENT_ID" \
  --environment-id "$ENVIRONMENT_ID"
```

To pin a session to a specific agent version, pass an object. This lets you control exactly which version runs and stage rollouts of new versions independently.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
ant beta:sessions create <<YAML
agent:
  type: agent
  id: $AGENT_ID
  version: 1
environment_id: $ENVIRONMENT_ID
YAML
```

The agent defines how Claude behaves within the session, including the model, system prompt, tools, and MCP servers. See [Define your agent](managed-agents/agent-setup.md) for details.

## MCP authentication through vaults

If your agent uses MCP tools that require authentication, pass `vault_ids` at session creation to reference a vault containing stored OAuth credentials. Anthropic manages token refresh on your behalf. See [Authenticate with vaults](managed-agents/vaults.md) for how to create vaults and register credentials.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
ant beta:sessions create <<YAML
agent: $AGENT_ID
environment_id: $ENVIRONMENT_ID
vault_ids:
  - $VAULT_ID
YAML
```

## Starting the session

Creating a session provisions the environment's sandbox but does not start any work. To delegate a task, send events to the session using a [user event](managed-agents/reference.md). The session acts as a state machine that tracks progress while events drive the actual execution.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

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

See [Session statuses](managed-agents/session-operations.md) for the statuses a session moves through, and [Session operations](managed-agents/session-operations.md) for retrieving, listing, updating, archiving, and deleting sessions.

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
