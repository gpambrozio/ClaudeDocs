# Work

Copy page

SDK language

CLI

# Work

##### [Get Work Item](api/beta/environments/work/retrieve.md)

$ ant beta:environments:work retrieve

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

$ ant beta:environments:work poll

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

$ ant beta:environments:work ack

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

$ ant beta:environments:work heartbeat

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

$ ant beta:environments:work stop

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

$ ant beta:environments:work list

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

$ ant beta:environments:work update

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

$ ant beta:environments:work stats

GET/v1/environments/{environment\_id}/work/stats

##### ModelsExpand Collapse

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

beta\_self\_hosted\_work\_heartbeat\_response: object { last\_heartbeat, lease\_extended, state, 2 more }

Response after recording a heartbeat for a work item.

last\_heartbeat: string

RFC 3339 timestamp of the actual heartbeat from DB

lease\_extended: boolean

Whether the heartbeat succeeded in extending the lease

state: "queued" or "starting" or "active" or 2 more

Current state of the work item (active/stopping/stopped)

"queued"

"starting"

"active"

"stopping"

"stopped"

ttl\_seconds: number

Effective TTL applied to the lease

type: "work\_heartbeat"

The type of response

beta\_self\_hosted\_work\_list\_response: object { data, next\_page }

Response when listing work items with cursor-based pagination.

data: array of [BetaSelfHostedWork](api/beta.md) { id, acknowledged\_at, created\_at, 9 more }

List of work items

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

next\_page: string

Opaque cursor for fetching the next page of results

beta\_self\_hosted\_work\_queue\_stats: object { depth, oldest\_queued\_at, pending, 2 more }

Statistics about the work queue for an environment.

Uses Redis Stream consumer group metrics for O(1) queries.

depth: number

Number of work items waiting to be picked up (lag from consumer group)

oldest\_queued\_at: string

RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

pending: number

Number of work items being processed (polled but not acknowledged)

type: "work\_queue\_stats"

The type of object

workers\_polling: number

Number of workers that have polled for work in the last 30 seconds. Requires worker\_id to be sent with poll requests.

beta\_self\_hosted\_work\_stop\_request: object { force }

Request to stop a work item.

force: optional boolean

If true, immediately stop work without graceful shutdown

beta\_self\_hosted\_work\_update\_request: object { metadata }

Request to update work item metadata.

metadata: map[string]

Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

beta\_session\_work\_data: object { id, type }

Work data for session work items.

This resource type is used when work represents a session that needs to be executed
in a self-hosted environment.

id: string

Session identifier (e.g., 'session\_...')

type: "session"

Type of work data

---

*Copyright © Anthropic. All rights reserved.*
