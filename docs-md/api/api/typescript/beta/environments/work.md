# Work

Copy page



TypeScript

# Work

##### [Get Work Item](api/beta/environments/work/retrieve.md)

client.beta.environments.work.retrieve(stringworkID, WorkRetrieveParams { environment\_id, betas } params, RequestOptionsoptions?): [BetaSelfHostedWork](api/beta.md) { id, acknowledged\_at, created\_at, 9 more }

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

client.beta.environments.work.poll(stringenvironmentID, WorkPollParams { block\_ms, reclaim\_older\_than\_ms, betas, Anthropic-Worker-ID } params?, RequestOptionsoptions?): [BetaSelfHostedWork](api/beta.md) { id, acknowledged\_at, created\_at, 9 more }  | null

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

client.beta.environments.work.ack(stringworkID, WorkAckParams { environment\_id, betas } params, RequestOptionsoptions?): [BetaSelfHostedWork](api/beta.md) { id, acknowledged\_at, created\_at, 9 more }

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

client.beta.environments.work.heartbeat(stringworkID, WorkHeartbeatParams { environment\_id, desired\_ttl\_seconds, expected\_last\_heartbeat, betas } params, RequestOptionsoptions?): [BetaSelfHostedWorkHeartbeatResponse](api/beta.md) { last\_heartbeat, lease\_extended, state, 2 more }

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

client.beta.environments.work.stop(stringworkID, WorkStopParams { environment\_id, force, betas } params, RequestOptionsoptions?): [BetaSelfHostedWork](api/beta.md) { id, acknowledged\_at, created\_at, 9 more }

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

client.beta.environments.work.list(stringenvironmentID, WorkListParams { limit, page, betas } params?, RequestOptionsoptions?): PageCursor<[BetaSelfHostedWork](api/beta.md) { id, acknowledged\_at, created\_at, 9 more } >

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

client.beta.environments.work.update(stringworkID, WorkUpdateParams { environment\_id, metadata, betas } params, RequestOptionsoptions?): [BetaSelfHostedWork](api/beta.md) { id, acknowledged\_at, created\_at, 9 more }

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

client.beta.environments.work.stats(stringenvironmentID, WorkStatsParams { betas } params?, RequestOptionsoptions?): [BetaSelfHostedWorkQueueStats](api/beta.md) { depth, oldest\_queued\_at, pending, 2 more }

GET/v1/environments/{environment\_id}/work/stats

##### ModelsExpand Collapse



BetaSelfHostedWork { id, acknowledged\_at, created\_at, 9 more } 

Work resource representing a unit of work in a self-hosted environment.

Work items are queued when sessions are created or when long-dormant sessions
receive new messages. The environment worker polls for work to execute in a
self-hosted sandbox.

id: string

Work identifier (e.g., 'work\_...')

acknowledged\_at: string | null

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

created\_at: string

RFC 3339 timestamp when work was created



data: [BetaSessionWorkData](api/beta.md) { id, type } 

The actual work to be performed

id: string

Session identifier (e.g., 'session\_...')

type: "session"

Type of work data

environment\_id: string

Environment identifier this work belongs to (e.g., `env_...`)

latest\_heartbeat\_at: string | null

RFC 3339 timestamp of the most recent heartbeat

metadata: Record<string, string>

User-provided metadata key-value pairs associated with this work item

started\_at: string | null

RFC 3339 timestamp when work execution started



state: "queued" | "starting" | "active" | 2 more

Current state of the work item

One of the following:

"queued"

"starting"

"active"

"stopping"

"stopped"

stop\_requested\_at: string | null

RFC 3339 timestamp when stop was requested

stopped\_at: string | null

RFC 3339 timestamp when work execution stopped

type: "work"

The type of object (always 'work')



BetaSelfHostedWorkHeartbeatResponse { last\_heartbeat, lease\_extended, state, 2 more } 

Response after recording a heartbeat for a work item.

last\_heartbeat: string

RFC 3339 timestamp of the actual heartbeat from DB

lease\_extended: boolean

Whether the heartbeat succeeded in extending the lease



state: "queued" | "starting" | "active" | 2 more

Current state of the work item (active/stopping/stopped)

One of the following:

"queued"

"starting"

"active"

"stopping"

"stopped"

ttl\_seconds: number

Effective TTL applied to the lease

type: "work\_heartbeat"

The type of response



BetaSelfHostedWorkListResponse { data, next\_page } 

Response when listing work items with cursor-based pagination.



data: Array<[BetaSelfHostedWork](api/beta.md) { id, acknowledged\_at, created\_at, 9 more } >

List of work items

id: string

Work identifier (e.g., 'work\_...')

acknowledged\_at: string | null

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

created\_at: string

RFC 3339 timestamp when work was created



data: [BetaSessionWorkData](api/beta.md) { id, type } 

The actual work to be performed

id: string

Session identifier (e.g., 'session\_...')

type: "session"

Type of work data

environment\_id: string

Environment identifier this work belongs to (e.g., `env_...`)

latest\_heartbeat\_at: string | null

RFC 3339 timestamp of the most recent heartbeat

metadata: Record<string, string>

User-provided metadata key-value pairs associated with this work item

started\_at: string | null

RFC 3339 timestamp when work execution started



state: "queued" | "starting" | "active" | 2 more

Current state of the work item

One of the following:

"queued"

"starting"

"active"

"stopping"

"stopped"

stop\_requested\_at: string | null

RFC 3339 timestamp when stop was requested

stopped\_at: string | null

RFC 3339 timestamp when work execution stopped

type: "work"

The type of object (always 'work')

next\_page: string | null

Opaque cursor for fetching the next page of results



BetaSelfHostedWorkQueueStats { depth, oldest\_queued\_at, pending, 2 more } 

Statistics about the work queue for an environment.

Uses Redis Stream consumer group metrics for O(1) queries.

depth: number

Number of work items waiting to be picked up (lag from consumer group)

oldest\_queued\_at: string | null

RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

pending: number

Number of work items being processed (polled but not acknowledged)

type: "work\_queue\_stats"

The type of object

workers\_polling: number | null

Number of workers that have polled for work in the last 30 seconds. Requires worker\_id to be sent with poll requests.



BetaSelfHostedWorkStopRequest { force } 

Request to stop a work item.

force?: boolean

If true, immediately stop work without graceful shutdown



BetaSelfHostedWorkUpdateRequest { metadata } 

Request to update work item metadata.

metadata: Record<string, string | null>

Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.



BetaSessionWorkData { id, type } 

Work data for session work items.

This resource type is used when work represents a session that needs to be executed
in a self-hosted environment.

id: string

Session identifier (e.g., 'session\_...')

type: "session"

Type of work data

---

*Copyright © Anthropic. All rights reserved.*
