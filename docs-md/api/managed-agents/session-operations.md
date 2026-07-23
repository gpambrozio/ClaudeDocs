# Session operations

Copy page



Once a session exists, use these operations to read, update, archive, or delete it. See [Start a session](managed-agents/sessions.md) for creating a session and sending it work.



Managed Agents API requests require the `managed-agents-2026-04-01` beta header, except memory store endpoints, which use `agent-memory-2026-07-22` instead. The SDK sets the correct beta header automatically. See [Beta headers](api/beta-headers.md).

##  Session statuses

Sessions progress through these statuses. See [Start a session](managed-agents/sessions.md) for the session lifecycle.

| Status | Description |
| --- | --- |
| `idle` | Agent is waiting for input, including user messages or tool confirmations. Sessions created without `initial_events` start in `idle`. |
| `running` | Agent is actively executing. |
| `rescheduling` | Transient error occurred, retrying automatically. |
| `terminated` | Session has ended, either because of an unrecoverable error or on completion. |

##  Updating the agent configuration

You can update a session's `agent.tools` and `agent.mcp_servers`, including permission policies, mid-session without creating a new agent version. Updates are session-local and do not propagate back to the underlying agent.

Only the agent's `tools` and `mcp_servers` can change after a session is created. To run a session with `model`, `system`, or `skills` values other than the agent's, use [agent configuration overrides](managed-agents/sessions.md) when you create the session. The agent's configured `system` field is fixed for the session's lifetime. On models that support it, you can still append system-level guidance mid-session by sending a [`system.message` event](managed-agents/events-and-streaming.md).

The semantics of a `tools` or `mcp_servers` update are full replacement: the provided array is the new value. To preserve existing entries, `GET` the session, modify the array, and `POST` it back.

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

##  Retrieving a session

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:sessions retrieve --session-id "$SESSION_ID"
```

##  Listing sessions

Results from `GET /v1/sessions` are paginated. Use the `limit` query parameter to control the page size. Each response includes a `next_page` cursor; pass it as the `page` parameter on the next request to fetch the following page. `next_page` is `null` when there are no more results.

To go back a page, pass `prev_page` as the `page` parameter. `prev_page` is `null` when you're on the first page.

A `page` cursor is opaque and encodes the `order` of the request that produced it. The `order` query parameter sets the sort direction of the results, `asc` or `desc` by creation time; the default is `desc` (newest first). Reusing a cursor with a different `order` returns a 400 error; other query parameters, including filters and `limit`, can change between paginated requests. For the pagination fields shared across list endpoints, see [Pagination](api/overview.md).

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
# --format raw returns one page envelope with its prev_page and next_page
# cursors; the default output auto-paginates and emits only the sessions.
cursors=$(ant beta:sessions list \
  --agent-id "$AGENT_ID" \
  --limit 1 \
  --format raw \
  --transform '{prev_page,next_page}')
printf '%s\n' "$cursors"

# Pass the next_page cursor back as --page to fetch the next page.
NEXT_PAGE=$(jq -r '.next_page' <<< "$cursors")
ant beta:sessions list \
  --agent-id "$AGENT_ID" \
  --limit 1 \
  --page "$NEXT_PAGE" \
  --format raw \
  --transform '{prev_page,next_page}'
# Pass that response's prev_page as --page to go back the same way.
```

##  Archiving a session

Archive a session to prevent new events from being sent while preserving its history. A `running` session cannot be archived; send an [interrupt event](managed-agents/events-and-streaming.md) if you need to archive it immediately.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:sessions archive \
  --session-id "$SESSION_ID"
```

##  Deleting a session

Delete a session to permanently remove its record, events, and associated sandbox. A `running` session cannot be deleted; send an [interrupt event](managed-agents/events-and-streaming.md) if you need to delete it immediately.

Files, memory stores, vaults, skills, environments, and agents are independent resources and are not affected by session deletion.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:sessions delete \
  --session-id "$SESSION_ID"
```

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
