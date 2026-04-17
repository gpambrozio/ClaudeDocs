# Start a session

Copy page

A session is a running agent instance within an environment. Each session references an [agent](managed-agents/agent-setup.md) and an [environment](managed-agents/environments.md) (both created separately), and maintains conversation history across multiple interactions.

All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.

## Creating a session

A session requires an `agent` ID and an `environment` ID. Agents are versioned resources; passing in the `agent` ID as a string starts the session with the latest agent version.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
)
```

To pin a session to a specific agent version, pass an object. This lets you control exactly which version runs and stage rollouts of new versions independently.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
pinned_session = client.beta.sessions.create(
    agent={"type": "agent", "id": agent.id, "version": 1},
    environment_id=environment.id,
)
```

The agent defines how Claude behaves within the session, including the model, system prompt, tools, and MCP servers. See [Agent setup](managed-agents/agent-setup.md) for details.

## MCP authentication through vaults

If your agent uses MCP tools that require authentication, pass `vault_ids` at session creation to reference a vault containing stored OAuth credentials. Anthropic manages token refresh on your behalf. See [Authenticate with vaults](managed-agents/vaults.md) for how to create vaults and register credentials.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
vault_session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    vault_ids=[vault.id],
)
```

## Starting the session

Creating a session provisions the environment and agent but does not start any work. To delegate a task, send events to the session using a [user event](managed-agents/events-and-streaming.md). The session acts as a state machine that tracks progress while events drive the actual execution.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
client.beta.sessions.events.send(
    session.id,
    events=[
        {
            "type": "user.message",
            "content": [
                {"type": "text", "text": "List the files in the working directory."}
            ],
        },
    ],
)
```

See [Events and streaming](managed-agents/events-and-streaming.md) for how to stream the agent's responses and handle tool confirmations.

## Session statuses

Sessions progress through these statuses:

| Status | Description |
| --- | --- |
| `idle` | Agent is waiting for input, including user messages or tool confirmations. Sessions start in `idle`. |
| `running` | Agent is actively executing |
| `rescheduling` | Transient error occurred, retrying automatically |
| `terminated` | Session has ended due to an unrecoverable error |

## Other session operations

### Retrieving a session

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
retrieved = client.beta.sessions.retrieve(session.id)
print(f"Status: {retrieved.status}")
```

### Listing sessions

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
for session in client.beta.sessions.list():
    print(f"{session.id}: {session.status}")
```

### Archiving a session

Archive a session to prevent new events from being sent while preserving its history:

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
client.beta.sessions.archive(session.id)
```

### Deleting a session

Delete a session to permanently remove its record, events, and associated container. A `running` session cannot be deleted; send an [interrupt event](managed-agents/events-and-streaming.md) if you need to delete it immediately.

Files, memory stores, environments, and agents are independent resources and are not affected by session deletion.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
client.beta.sessions.delete(session.id)
```

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
