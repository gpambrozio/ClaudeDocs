# Stop Work

Copy page



cURL

# Stop Work

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Stop a work item, initiating graceful or forced shutdown.

##### Path ParametersExpand Collapse

environment\_id: string

work\_id: string

##### Header ParametersExpand Collapse



"anthropic-beta": optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

One of the following:

string



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 26 more

One of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"fallback-credit-2026-06-01"

"agent-memory-2026-07-22"

##### Body ParametersJSONExpand Collapse

force: optional boolean

If true, immediately stop work without graceful shutdown

##### ReturnsExpand Collapse



BetaSelfHostedWork object { id, acknowledged\_at, created\_at, 9 more } 

Work resource representing a unit of work in a self-hosted environment.

Work items are queued when sessions are created or when long-dormant sessions
receive new messages. The environment worker polls for work to execute in a
self-hosted sandbox.

id: string

Work identifier (e.g., 'work\_...')

acknowledged\_at: string

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

created\_at: string

RFC 3339 timestamp when work was created



data: [BetaSessionWorkData](api/beta/environments/work.md) { id, type } 

The actual work to be performed

id: string

Session identifier (e.g., 'session\_...')

type: "session"

Type of work data

environment\_id: string

Environment identifier this work belongs to (e.g., `env_...`)

latest\_heartbeat\_at: string

RFC 3339 timestamp of the most recent heartbeat

metadata: map[string]

User-provided metadata key-value pairs associated with this work item

started\_at: string

RFC 3339 timestamp when work execution started



state: "queued" or "starting" or "active" or 2 more

Current state of the work item

One of the following:

"queued"

"starting"

"active"

"stopping"

"stopped"

stop\_requested\_at: string

RFC 3339 timestamp when stop was requested

stopped\_at: string

RFC 3339 timestamp when work execution stopped

type: "work"

The type of object (always 'work')

Stop Work

cURL

```shiki
curl https://api.anthropic.com/v1/environments/$ENVIRONMENT_ID/work/$WORK_ID/stop \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{}'
```

Response 200



```shiki
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
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

##### Returns Examples

Response 200



```shiki
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
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

---

*Copyright © Anthropic. All rights reserved.*
