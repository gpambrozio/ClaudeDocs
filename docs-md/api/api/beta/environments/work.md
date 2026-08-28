# Work

Copy page



cURL

# Work

##### [Get Work Item](api/http/beta/environments/work/retrieve.md)

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/http/beta/environments/work/poll.md)

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/http/beta/environments/work/ack.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/http/beta/environments/work/heartbeat.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/http/beta/environments/work/stop.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/http/beta/environments/work/list.md)

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/http/beta/environments/work/update.md)

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/http/beta/environments/work/stats.md)

GET/v1/environments/{environment\_id}/work/stats

##### Models



BetaSelfHostedWork object{ id, acknowledged\_at, created\_at, 10 more }

Work resource representing a unit of work in a self-hosted environment.

Work items are queued when sessions are created or when long-dormant sessions
receive new messages. The environment worker polls for work to execute in a
self-hosted sandbox.



BetaSelfHostedWorkHeartbeatResponse object{ last\_heartbeat, lease\_extended, state, 2 more }

Response after recording a heartbeat for a work item.

last\_heartbeat: string

RFC 3339 timestamp of the actual heartbeat from DB

lease\_extended: boolean

Whether the heartbeat succeeded in extending the lease



state: "queued" or "starting" or "active" or 2 more

Current state of the work item (active/stopping/stopped)

One of the following:

"queued"

"starting"

"active"

"stopping"

"stopped"

ttl\_seconds: number

Effective TTL applied to the lease



type: "work\_heartbeat"

The type of response

defaultwork\_heartbeat



BetaSelfHostedWorkListResponse object{ data, next\_page }

Response when listing work items with cursor-based pagination.



BetaSelfHostedWorkQueueStats object{ depth, oldest\_queued\_at, pending, 2 more }

Statistics about the work queue for an environment.

Uses Redis Stream consumer group metrics for O(1) queries.

depth: number

Number of work items waiting to be picked up (lag from consumer group)

oldest\_queued\_at: string or null

RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty



pending: number

Number of work items being processed (polled but not acknowledged)

default0



type: "work\_queue\_stats"

The type of object

defaultwork\_queue\_stats

workers\_polling: number or null

Number of workers that have polled for work in the last 30 seconds. Requires worker\_id to be sent with poll requests.



BetaSelfHostedWorkStopRequest object{ force }

Request to stop a work item.



force: optional boolean

If true, immediately stop work without graceful shutdown

defaultfalse



BetaSelfHostedWorkUpdateRequest object{ metadata }

Request to update work item metadata.

metadata: map[string]

Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.



BetaSessionWorkData object{ id, type }

Work data for session work items.

This resource type is used when work represents a session that needs to be executed
in a self-hosted environment.

id: string

Session identifier (e.g., 'session\_...')

type: "session"

Type of work data

---

*Copyright © Anthropic. All rights reserved.*
