# Stop Work

Copy page

CLI

# Stop Work

$ ant beta:environments:work stop

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Stop a work item, initiating graceful or forced shutdown.

##### ParametersExpand Collapse

--environment-id: string

Path param

--work-id: string

Path param

--force: optional boolean

Body param: If true, immediately stop work without graceful shutdown

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

beta\_self\_hosted\_work: object { id, acknowledged\_at, created\_at, 9 more }

Work resource representing a unit of work in a self-hosted environment.

Work items are queued when sessions are created or when long-dormant sessions
receive new messages. The environment worker polls for work to execute in a
self-hosted sandbox.

id: string

Work identifier (e.g., 'work\_...')

acknowledged\_at: string

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

created\_at: string

RFC 3339 timestamp when work was created

data: object { id, type }

The actual work to be performed

id: string

Session identifier (e.g., 'session\_...')

type: "session"

Type of work data

environment\_id: string

Environment identifier this work belongs to (e.g., `env_...`)

latest\_heartbeat\_at: string

RFC 3339 timestamp of the most recent heartbeat

metadata: map[string]

User-provided metadata key-value pairs associated with this work item

started\_at: string

RFC 3339 timestamp when work execution started

state: "queued" or "starting" or "active" or 2 more

Current state of the work item

"queued"

"starting"

"active"

"stopping"

"stopped"

stop\_requested\_at: string

RFC 3339 timestamp when stop was requested

stopped\_at: string

RFC 3339 timestamp when work execution stopped

type: "work"

The type of object (always 'work')

Stop Work

CLI

```shiki
ant beta:environments:work stop \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW \
  --work-id work_id
```

Response 200

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
