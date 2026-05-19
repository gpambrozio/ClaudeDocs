# Work

Copy page

Java

# Work

##### [Get Work Item](api/beta/environments/work/retrieve.md)

[BetaSelfHostedWork](api/beta.md) beta().environments().work().retrieve(WorkRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

[BetaSelfHostedWork](api/beta.md) beta().environments().work().poll(WorkPollParamsparams = WorkPollParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

[BetaSelfHostedWork](api/beta.md) beta().environments().work().ack(WorkAckParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

[BetaSelfHostedWorkHeartbeatResponse](api/beta.md) beta().environments().work().heartbeat(WorkHeartbeatParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

[BetaSelfHostedWork](api/beta.md) beta().environments().work().stop(WorkStopParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

WorkListPage beta().environments().work().list(WorkListParamsparams = WorkListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

[BetaSelfHostedWork](api/beta.md) beta().environments().work().update(WorkUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

[BetaSelfHostedWorkQueueStats](api/beta.md) beta().environments().work().stats(WorkStatsParamsparams = WorkStatsParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/environments/{environment\_id}/work/stats

##### ModelsExpand Collapse

class BetaSelfHostedWork:

Work resource representing a unit of work in a self-hosted environment.

Work items are queued when sessions are created or when long-dormant sessions
receive new messages. The environment worker polls for work to execute in a
self-hosted sandbox.

String id

Work identifier (e.g., 'work\_...')

Optional<String> acknowledgedAt

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

String createdAt

RFC 3339 timestamp when work was created

[BetaSessionWorkData](api/beta.md) data

The actual work to be performed

String id

Session identifier (e.g., 'session\_...')

JsonValue; type "session"constant"session"constant

Type of work data

String environmentId

Environment identifier this work belongs to (e.g., `env_...`)

Optional<String> latestHeartbeatAt

RFC 3339 timestamp of the most recent heartbeat

Metadata metadata

User-provided metadata key-value pairs associated with this work item

Optional<String> startedAt

RFC 3339 timestamp when work execution started

State state

Current state of the work item

Accepts one of the following:

QUEUED("queued")

STARTING("starting")

ACTIVE("active")

STOPPING("stopping")

STOPPED("stopped")

Optional<String> stopRequestedAt

RFC 3339 timestamp when stop was requested

Optional<String> stoppedAt

RFC 3339 timestamp when work execution stopped

JsonValue; type "work"constant"work"constant

The type of object (always 'work')

class BetaSelfHostedWorkHeartbeatResponse:

Response after recording a heartbeat for a work item.

String lastHeartbeat

RFC 3339 timestamp of the actual heartbeat from DB

boolean leaseExtended

Whether the heartbeat succeeded in extending the lease

State state

Current state of the work item (active/stopping/stopped)

Accepts one of the following:

QUEUED("queued")

STARTING("starting")

ACTIVE("active")

STOPPING("stopping")

STOPPED("stopped")

long ttlSeconds

Effective TTL applied to the lease

JsonValue; type "work\_heartbeat"constant"work\_heartbeat"constant

The type of response

class BetaSelfHostedWorkListResponse:

Response when listing work items with cursor-based pagination.

List<[BetaSelfHostedWork](api/beta.md)> data

List of work items

String id

Work identifier (e.g., 'work\_...')

Optional<String> acknowledgedAt

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

String createdAt

RFC 3339 timestamp when work was created

[BetaSessionWorkData](api/beta.md) data

The actual work to be performed

String id

Session identifier (e.g., 'session\_...')

JsonValue; type "session"constant"session"constant

Type of work data

String environmentId

Environment identifier this work belongs to (e.g., `env_...`)

Optional<String> latestHeartbeatAt

RFC 3339 timestamp of the most recent heartbeat

Metadata metadata

User-provided metadata key-value pairs associated with this work item

Optional<String> startedAt

RFC 3339 timestamp when work execution started

State state

Current state of the work item

Accepts one of the following:

QUEUED("queued")

STARTING("starting")

ACTIVE("active")

STOPPING("stopping")

STOPPED("stopped")

Optional<String> stopRequestedAt

RFC 3339 timestamp when stop was requested

Optional<String> stoppedAt

RFC 3339 timestamp when work execution stopped

JsonValue; type "work"constant"work"constant

The type of object (always 'work')

Optional<String> nextPage

Opaque cursor for fetching the next page of results

class BetaSelfHostedWorkQueueStats:

Statistics about the work queue for an environment.

Uses Redis Stream consumer group metrics for O(1) queries.

long depth

Number of work items waiting to be picked up (lag from consumer group)

Optional<String> oldestQueuedAt

RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

long pending

Number of work items being processed (polled but not acknowledged)

JsonValue; type "work\_queue\_stats"constant"work\_queue\_stats"constant

The type of object

Optional<Long> workersPolling

Number of workers that have polled for work in the last 30 seconds. Requires worker\_id to be sent with poll requests.

class BetaSelfHostedWorkStopRequest:

Request to stop a work item.

Optional<Boolean> force

If true, immediately stop work without graceful shutdown

class BetaSelfHostedWorkUpdateRequest:

Request to update work item metadata.

Metadata metadata

Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

class BetaSessionWorkData:

Work data for session work items.

This resource type is used when work represents a session that needs to be executed
in a self-hosted environment.

String id

Session identifier (e.g., 'session\_...')

JsonValue; type "session"constant"session"constant

Type of work data

---

*Copyright © Anthropic. All rights reserved.*
