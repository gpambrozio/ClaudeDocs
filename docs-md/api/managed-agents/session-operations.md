# Session operations

Copy page

Once a session exists, use these operations to read, update, archive, or delete it. See [Start a session](managed-agents/sessions.md) for creating a session and sending it work.

All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.

## Session statuses

Sessions progress through these statuses. See [Start a session](managed-agents/sessions.md) for the session lifecycle.

| Status | Description |
| --- | --- |
| `idle` | Agent is waiting for input, including user messages or tool confirmations. Sessions start in `idle`. |
| `running` | Agent is actively executing. |
| `rescheduling` | Transient error occurred, retrying automatically. |
| `terminated` | Session has ended because of an unrecoverable error. |

## Updating the agent configuration

You can update a session's `agent.tools` and `agent.mcp_servers`, including permission policies, mid-session without creating a new agent version. Updates are session-local and do not propagate back to the underlying agent.

The semantics of an update are full replacement: the provided array is the new value. To preserve existing entries, `GET` the session, modify the array, and `POST` it back.

The session must be `idle` to update the agent. [Interrupt](managed-agents/events-and-streaming.md) the session if you need to update the agent while it's running.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:sessions update --session-id "$SESSION_ID" <<'YAML'
agent:
  tools:
    - type: agent_toolset_20260401
    - type: mcp_toolset
      mcp_server_name: linear
  mcp_servers:
    - type: url
      name: linear
      url: https://mcp.linear.app/sse
YAML
```

## Retrieving a session

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:sessions retrieve --session-id "$SESSION_ID"
```

## Listing sessions

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:sessions list --agent-id "$AGENT_ID"
```

## Archiving a session

Archive a session to prevent new events from being sent while preserving its history. A `running` session cannot be archived; send an [interrupt event](managed-agents/events-and-streaming.md) if you need to archive it immediately.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:sessions archive \
  --session-id "$SESSION_ID"
```

## Deleting a session

Delete a session to permanently remove its record, events, and associated sandbox. A `running` session cannot be deleted; send an [interrupt event](managed-agents/events-and-streaming.md) if you need to delete it immediately.

Files, memory stores, vaults, skills, environments, and agents are independent resources and are not affected by session deletion.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:sessions delete \
  --session-id "$SESSION_ID"
```

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
