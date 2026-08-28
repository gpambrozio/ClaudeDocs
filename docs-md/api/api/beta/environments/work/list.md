# List Work Items

Copy page



cURL

# List Work Items

GET/v1/environments/{environment\_id}/work

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

List work items in an environment.

##### Path parameters

environment\_id: string

##### Query parameters



limit: optional number

Maximum number of work items to return

default20

maximum1000

minimum1

page: optional string

Opaque cursor from previous response for pagination

##### Headers



"anthropic-beta": optional array of [AnthropicBeta](api/http/beta.md)

Optional header to specify the beta version(s) you want to use.

One of the following:

string



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more

One of the following:

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

"user-profiles-2026-08-18"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"dreaming-2026-04-21"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"server-side-fallback-2026-07-01"

"fallback-credit-2026-06-01"

"fallback-credit-2026-07-01"

"agent-memory-2026-07-22"

"mid-conversation-tool-changes-2026-07-01"

"compact-2026-01-12"

"computer-use-2025-11-24"

"mcp-tunnels-2026-06-22"

"structured-outputs-2025-11-13"

"task-budgets-2026-03-13"

"thinking-display-updates-2026-08-18"

"ce-user-management-2026-07-13"

##### Returns



BetaSelfHostedWorkListResponse object{ data, next\_page }

Response when listing work items with cursor-based pagination.



### List Work Items

cURL



```shiki
curl https://api.anthropic.com/v1/environments/$ENVIRONMENT_ID/work \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```shiki
{
  "data": [
    {
      "id": "id",
      "acknowledged_at": "acknowledged_at",
      "created_at": "created_at",
      "data": {
        "id": "id",
        "type": "session"
      },
      "environment_id": "environment_id",
      "latest_heartbeat_at": "latest_heartbeat_at",
      "metadata": {
        "foo": "string"
      },
      "secret": "secret",
      "started_at": "started_at",
      "state": "queued",
      "stop_requested_at": "stop_requested_at",
      "stopped_at": "stopped_at",
      "type": "work"
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "id": "id",
      "acknowledged_at": "acknowledged_at",
      "created_at": "created_at",
      "data": {
        "id": "id",
        "type": "session"
      },
      "environment_id": "environment_id",
      "latest_heartbeat_at": "latest_heartbeat_at",
      "metadata": {
        "foo": "string"
      },
      "secret": "secret",
      "started_at": "started_at",
      "state": "queued",
      "stop_requested_at": "stop_requested_at",
      "stopped_at": "stopped_at",
      "type": "work"
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
