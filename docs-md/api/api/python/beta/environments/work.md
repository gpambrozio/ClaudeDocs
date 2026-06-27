# Work

Copy page



Python

# Work

##### [Get Work Item](api/beta/environments/work/retrieve.md)

beta.environments.work.retrieve(strwork\_id, WorkRetrieveParams\*\*kwargs)  -> [BetaSelfHostedWork](api/beta/environments/work.md)

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

beta.environments.work.poll(strenvironment\_id, WorkPollParams\*\*kwargs)  -> [BetaSelfHostedWork](api/beta/environments/work.md)

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

beta.environments.work.ack(strwork\_id, WorkAckParams\*\*kwargs)  -> [BetaSelfHostedWork](api/beta/environments/work.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

beta.environments.work.heartbeat(strwork\_id, WorkHeartbeatParams\*\*kwargs)  -> [BetaSelfHostedWorkHeartbeatResponse](api/beta/environments/work.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

beta.environments.work.stop(strwork\_id, WorkStopParams\*\*kwargs)  -> [BetaSelfHostedWork](api/beta/environments/work.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

beta.environments.work.list(strenvironment\_id, WorkListParams\*\*kwargs)  -> SyncPageCursor[[BetaSelfHostedWork](api/beta/environments/work.md)]

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

beta.environments.work.update(strwork\_id, WorkUpdateParams\*\*kwargs)  -> [BetaSelfHostedWork](api/beta/environments/work.md)

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

beta.environments.work.stats(strenvironment\_id, WorkStatsParams\*\*kwargs)  -> [BetaSelfHostedWorkQueueStats](api/beta/environments/work.md)

GET/v1/environments/{environment\_id}/work/stats

##### ModelsExpand Collapse



class BetaSelfHostedWork: …

Work resource representing a unit of work in a self-hosted environment.

Work items are queued when sessions are created or when long-dormant sessions
receive new messages. The environment worker polls for work to execute in a
self-hosted sandbox.

id: str

Work identifier (e.g., 'work\_...')

acknowledged\_at: Optional[str]

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

created\_at: str

RFC 3339 timestamp when work was created



data: [BetaSessionWorkData](api/beta/environments/work.md)

The actual work to be performed

id: str

Session identifier (e.g., 'session\_...')

type: Literal["session"]

Type of work data

environment\_id: str

Environment identifier this work belongs to (e.g., `env_...`)

latest\_heartbeat\_at: Optional[str]

RFC 3339 timestamp of the most recent heartbeat

metadata: Dict[str, str]

User-provided metadata key-value pairs associated with this work item

started\_at: Optional[str]

RFC 3339 timestamp when work execution started



state: Literal["queued", "starting", "active", 2 more]

Current state of the work item

One of the following:

"queued"

"starting"

"active"

"stopping"

"stopped"

stop\_requested\_at: Optional[str]

RFC 3339 timestamp when stop was requested

stopped\_at: Optional[str]

RFC 3339 timestamp when work execution stopped

type: Literal["work"]

The type of object (always 'work')



class BetaSelfHostedWorkHeartbeatResponse: …

Response after recording a heartbeat for a work item.

last\_heartbeat: str

RFC 3339 timestamp of the actual heartbeat from DB

lease\_extended: bool

Whether the heartbeat succeeded in extending the lease



state: Literal["queued", "starting", "active", 2 more]

Current state of the work item (active/stopping/stopped)

One of the following:

"queued"

"starting"

"active"

"stopping"

"stopped"

ttl\_seconds: int

Effective TTL applied to the lease

type: Literal["work\_heartbeat"]

The type of response



class BetaSelfHostedWorkListResponse: …

Response when listing work items with cursor-based pagination.



data: List[[BetaSelfHostedWork](api/beta/environments/work.md)]

List of work items

id: str

Work identifier (e.g., 'work\_...')

acknowledged\_at: Optional[str]

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

created\_at: str

RFC 3339 timestamp when work was created



data: [BetaSessionWorkData](api/beta/environments/work.md)

The actual work to be performed

id: str

Session identifier (e.g., 'session\_...')

type: Literal["session"]

Type of work data

environment\_id: str

Environment identifier this work belongs to (e.g., `env_...`)

latest\_heartbeat\_at: Optional[str]

RFC 3339 timestamp of the most recent heartbeat

metadata: Dict[str, str]

User-provided metadata key-value pairs associated with this work item

started\_at: Optional[str]

RFC 3339 timestamp when work execution started



state: Literal["queued", "starting", "active", 2 more]

Current state of the work item

One of the following:

"queued"

"starting"

"active"

"stopping"

"stopped"

stop\_requested\_at: Optional[str]

RFC 3339 timestamp when stop was requested

stopped\_at: Optional[str]

RFC 3339 timestamp when work execution stopped

type: Literal["work"]

The type of object (always 'work')

next\_page: Optional[str]

Opaque cursor for fetching the next page of results



class BetaSelfHostedWorkQueueStats: …

Statistics about the work queue for an environment.

Uses Redis Stream consumer group metrics for O(1) queries.

depth: int

Number of work items waiting to be picked up (lag from consumer group)

oldest\_queued\_at: Optional[str]

RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

pending: int

Number of work items being processed (polled but not acknowledged)

type: Literal["work\_queue\_stats"]

The type of object

workers\_polling: Optional[int]

Number of workers that have polled for work in the last 30 seconds. Requires worker\_id to be sent with poll requests.



class BetaSelfHostedWorkStopRequest: …

Request to stop a work item.

force: Optional[bool]

If true, immediately stop work without graceful shutdown



class BetaSelfHostedWorkUpdateRequest: …

Request to update work item metadata.

metadata: Dict[str, Optional[str]]

Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.



class BetaSessionWorkData: …

Work data for session work items.

This resource type is used when work represents a session that needs to be executed
in a self-hosted environment.

id: str

Session identifier (e.g., 'session\_...')

type: Literal["session"]

Type of work data

---

*Copyright © Anthropic. All rights reserved.*
