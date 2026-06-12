# Work

Copy page

SDK language

C#

# Work

##### [Get Work Item](api/beta/environments/work/retrieve.md)

[BetaSelfHostedWork](api/beta.md) Beta.Environments.Work.Retrieve(WorkRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

[BetaSelfHostedWork](api/beta.md)? Beta.Environments.Work.Poll(WorkPollParamsparameters, CancellationTokencancellationToken = default)

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

[BetaSelfHostedWork](api/beta.md) Beta.Environments.Work.Ack(WorkAckParamsparameters, CancellationTokencancellationToken = default)

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

[BetaSelfHostedWorkHeartbeatResponse](api/beta.md) Beta.Environments.Work.Heartbeat(WorkHeartbeatParamsparameters, CancellationTokencancellationToken = default)

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

[BetaSelfHostedWork](api/beta.md) Beta.Environments.Work.Stop(WorkStopParamsparameters, CancellationTokencancellationToken = default)

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

[BetaSelfHostedWorkListResponse](api/beta.md) Beta.Environments.Work.List(WorkListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

[BetaSelfHostedWork](api/beta.md) Beta.Environments.Work.Update(WorkUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

[BetaSelfHostedWorkQueueStats](api/beta.md) Beta.Environments.Work.Stats(WorkStatsParamsparameters, CancellationTokencancellationToken = default)

GET/v1/environments/{environment\_id}/work/stats

##### ModelsExpand Collapse



class BetaSelfHostedWork:

Work resource representing a unit of work in a self-hosted environment.

Work items are queued when sessions are created or when long-dormant sessions
receive new messages. The environment worker polls for work to execute in a
self-hosted sandbox.

required string ID

Work identifier (e.g., 'work\_...')

required string? AcknowledgedAt

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

required string CreatedAt

RFC 3339 timestamp when work was created



required [BetaSessionWorkData](api/beta.md) Data

The actual work to be performed

required string ID

Session identifier (e.g., 'session\_...')

JsonElement Type "session"constant

Type of work data

required string EnvironmentID

Environment identifier this work belongs to (e.g., `env_...`)

required string? LatestHeartbeatAt

RFC 3339 timestamp of the most recent heartbeat

required IReadOnlyDictionary<string, string> Metadata

User-provided metadata key-value pairs associated with this work item

required string? StartedAt

RFC 3339 timestamp when work execution started



required State State

Current state of the work item

One of the following:

"queued"Queued

"starting"Starting

"active"Active

"stopping"Stopping

"stopped"Stopped

required string? StopRequestedAt

RFC 3339 timestamp when stop was requested

required string? StoppedAt

RFC 3339 timestamp when work execution stopped

JsonElement Type "work"constant

The type of object (always 'work')



class BetaSelfHostedWorkHeartbeatResponse:

Response after recording a heartbeat for a work item.

required string LastHeartbeat

RFC 3339 timestamp of the actual heartbeat from DB

required Boolean LeaseExtended

Whether the heartbeat succeeded in extending the lease



required State State

Current state of the work item (active/stopping/stopped)

One of the following:

"queued"Queued

"starting"Starting

"active"Active

"stopping"Stopping

"stopped"Stopped

required Long TtlSeconds

Effective TTL applied to the lease

JsonElement Type "work\_heartbeat"constant

The type of response



class BetaSelfHostedWorkListResponse:

Response when listing work items with cursor-based pagination.



required IReadOnlyList<[BetaSelfHostedWork](api/beta.md)> Data

List of work items

required string ID

Work identifier (e.g., 'work\_...')

required string? AcknowledgedAt

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

required string CreatedAt

RFC 3339 timestamp when work was created



required [BetaSessionWorkData](api/beta.md) Data

The actual work to be performed

required string ID

Session identifier (e.g., 'session\_...')

JsonElement Type "session"constant

Type of work data

required string EnvironmentID

Environment identifier this work belongs to (e.g., `env_...`)

required string? LatestHeartbeatAt

RFC 3339 timestamp of the most recent heartbeat

required IReadOnlyDictionary<string, string> Metadata

User-provided metadata key-value pairs associated with this work item

required string? StartedAt

RFC 3339 timestamp when work execution started



required State State

Current state of the work item

One of the following:

"queued"Queued

"starting"Starting

"active"Active

"stopping"Stopping

"stopped"Stopped

required string? StopRequestedAt

RFC 3339 timestamp when stop was requested

required string? StoppedAt

RFC 3339 timestamp when work execution stopped

JsonElement Type "work"constant

The type of object (always 'work')

required string? NextPage

Opaque cursor for fetching the next page of results



class BetaSelfHostedWorkQueueStats:

Statistics about the work queue for an environment.

Uses Redis Stream consumer group metrics for O(1) queries.

required Long Depth

Number of work items waiting to be picked up (lag from consumer group)

required string? OldestQueuedAt

RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

required Long Pending

Number of work items being processed (polled but not acknowledged)

JsonElement Type "work\_queue\_stats"constant

The type of object

required Long? WorkersPolling

Number of workers that have polled for work in the last 30 seconds. Requires worker\_id to be sent with poll requests.



class BetaSelfHostedWorkStopRequest:

Request to stop a work item.

Boolean Force

If true, immediately stop work without graceful shutdown



class BetaSelfHostedWorkUpdateRequest:

Request to update work item metadata.

required IReadOnlyDictionary<string, string> Metadata

Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.



class BetaSessionWorkData:

Work data for session work items.

This resource type is used when work represents a session that needs to be executed
in a self-hosted environment.

required string ID

Session identifier (e.g., 'session\_...')

JsonElement Type "session"constant

Type of work data

---

*Copyright © Anthropic. All rights reserved.*
