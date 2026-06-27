# Work

Copy page



Ruby

# Work

##### [Get Work Item](api/beta/environments/work/retrieve.md)

beta.environments.work.retrieve(work\_id, \*\*kwargs) -> [BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 9 more }

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

beta.environments.work.poll(environment\_id, \*\*kwargs) -> [BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 9 more }

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

beta.environments.work.ack(work\_id, \*\*kwargs) -> [BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 9 more }

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

beta.environments.work.heartbeat(work\_id, \*\*kwargs) -> [BetaSelfHostedWorkHeartbeatResponse](api/beta/environments/work.md) { last\_heartbeat, lease\_extended, state, 2 more }

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

beta.environments.work.stop(work\_id, \*\*kwargs) -> [BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 9 more }

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

beta.environments.work.list(environment\_id, \*\*kwargs) -> PageCursor<[BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 9 more } >

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

beta.environments.work.update(work\_id, \*\*kwargs) -> [BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 9 more }

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

beta.environments.work.stats(environment\_id, \*\*kwargs) -> [BetaSelfHostedWorkQueueStats](api/beta/environments/work.md) { depth, oldest\_queued\_at, pending, 2 more }

GET/v1/environments/{environment\_id}/work/stats

##### ModelsExpand Collapse



class BetaSelfHostedWork { id, acknowledged\_at, created\_at, 9 more } 

Work resource representing a unit of work in a self-hosted environment.

Work items are queued when sessions are created or when long-dormant sessions
receive new messages. The environment worker polls for work to execute in a
self-hosted sandbox.

id: String

Work identifier (e.g., 'work\_...')

acknowledged\_at: String

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

created\_at: String

RFC 3339 timestamp when work was created



data: [BetaSessionWorkData](api/beta/environments/work.md) { id, type } 

The actual work to be performed

id: String

Session identifier (e.g., 'session\_...')

type: :session

Type of work data

environment\_id: String

Environment identifier this work belongs to (e.g., `env_...`)

latest\_heartbeat\_at: String

RFC 3339 timestamp of the most recent heartbeat

metadata: Hash[Symbol, String]

User-provided metadata key-value pairs associated with this work item

started\_at: String

RFC 3339 timestamp when work execution started



state: :queued | :starting | :active | 2 more

Current state of the work item

One of the following:

:queued

:starting

:active

:stopping

:stopped

stop\_requested\_at: String

RFC 3339 timestamp when stop was requested

stopped\_at: String

RFC 3339 timestamp when work execution stopped

type: :work

The type of object (always 'work')



class BetaSelfHostedWorkHeartbeatResponse { last\_heartbeat, lease\_extended, state, 2 more } 

Response after recording a heartbeat for a work item.

last\_heartbeat: String

RFC 3339 timestamp of the actual heartbeat from DB

lease\_extended: bool

Whether the heartbeat succeeded in extending the lease



state: :queued | :starting | :active | 2 more

Current state of the work item (active/stopping/stopped)

One of the following:

:queued

:starting

:active

:stopping

:stopped

ttl\_seconds: Integer

Effective TTL applied to the lease

type: :work\_heartbeat

The type of response



class BetaSelfHostedWorkListResponse { data, next\_page } 

Response when listing work items with cursor-based pagination.



data: Array[[BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 9 more } ]

List of work items

id: String

Work identifier (e.g., 'work\_...')

acknowledged\_at: String

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

created\_at: String

RFC 3339 timestamp when work was created



data: [BetaSessionWorkData](api/beta/environments/work.md) { id, type } 

The actual work to be performed

id: String

Session identifier (e.g., 'session\_...')

type: :session

Type of work data

environment\_id: String

Environment identifier this work belongs to (e.g., `env_...`)

latest\_heartbeat\_at: String

RFC 3339 timestamp of the most recent heartbeat

metadata: Hash[Symbol, String]

User-provided metadata key-value pairs associated with this work item

started\_at: String

RFC 3339 timestamp when work execution started



state: :queued | :starting | :active | 2 more

Current state of the work item

One of the following:

:queued

:starting

:active

:stopping

:stopped

stop\_requested\_at: String

RFC 3339 timestamp when stop was requested

stopped\_at: String

RFC 3339 timestamp when work execution stopped

type: :work

The type of object (always 'work')

next\_page: String

Opaque cursor for fetching the next page of results



class BetaSelfHostedWorkQueueStats { depth, oldest\_queued\_at, pending, 2 more } 

Statistics about the work queue for an environment.

Uses Redis Stream consumer group metrics for O(1) queries.

depth: Integer

Number of work items waiting to be picked up (lag from consumer group)

oldest\_queued\_at: String

RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

pending: Integer

Number of work items being processed (polled but not acknowledged)

type: :work\_queue\_stats

The type of object

workers\_polling: Integer

Number of workers that have polled for work in the last 30 seconds. Requires worker\_id to be sent with poll requests.



class BetaSelfHostedWorkStopRequest { force } 

Request to stop a work item.

force: bool

If true, immediately stop work without graceful shutdown



class BetaSelfHostedWorkUpdateRequest { metadata } 

Request to update work item metadata.

metadata: Hash[Symbol, String]

Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.



class BetaSessionWorkData { id, type } 

Work data for session work items.

This resource type is used when work represents a session that needs to be executed
in a self-hosted environment.

id: String

Session identifier (e.g., 'session\_...')

type: :session

Type of work data

---

*Copyright © Anthropic. All rights reserved.*
