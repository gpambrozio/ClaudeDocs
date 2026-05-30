# Work

Copy page

SDK language

Go

# Work

##### [Get Work Item](api/beta/environments/work/retrieve.md)

client.Beta.Environments.Work.Get(ctx, workID, params) (\*[BetaSelfHostedWork](api/beta.md), error)

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

client.Beta.Environments.Work.Poll(ctx, environmentID, params) (\*[BetaSelfHostedWork](api/beta.md), error)

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

client.Beta.Environments.Work.Ack(ctx, workID, params) (\*[BetaSelfHostedWork](api/beta.md), error)

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

client.Beta.Environments.Work.Heartbeat(ctx, workID, params) (\*[BetaSelfHostedWorkHeartbeatResponse](api/beta.md), error)

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

client.Beta.Environments.Work.Stop(ctx, workID, params) (\*[BetaSelfHostedWork](api/beta.md), error)

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

client.Beta.Environments.Work.List(ctx, environmentID, params) (\*PageCursor[[BetaSelfHostedWork](api/beta.md)], error)

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

client.Beta.Environments.Work.Update(ctx, workID, params) (\*[BetaSelfHostedWork](api/beta.md), error)

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

client.Beta.Environments.Work.Stats(ctx, environmentID, query) (\*[BetaSelfHostedWorkQueueStats](api/beta.md), error)

GET/v1/environments/{environment\_id}/work/stats

##### ModelsExpand Collapse

type BetaSelfHostedWork struct{…}

Work resource representing a unit of work in a self-hosted environment.

Work items are queued when sessions are created or when long-dormant sessions
receive new messages. The environment worker polls for work to execute in a
self-hosted sandbox.

ID string

Work identifier (e.g., 'work\_...')

AcknowledgedAt string

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

CreatedAt string

RFC 3339 timestamp when work was created

Data [BetaSessionWorkData](api/beta.md)

The actual work to be performed

ID string

Session identifier (e.g., 'session\_...')

Type Session

Type of work data

EnvironmentID string

Environment identifier this work belongs to (e.g., `env_...`)

LatestHeartbeatAt string

RFC 3339 timestamp of the most recent heartbeat

Metadata map[string, string]

User-provided metadata key-value pairs associated with this work item

StartedAt string

RFC 3339 timestamp when work execution started

State BetaSelfHostedWorkState

Current state of the work item

One of the following:

const BetaSelfHostedWorkStateQueued BetaSelfHostedWorkState = "queued"

const BetaSelfHostedWorkStateStarting BetaSelfHostedWorkState = "starting"

const BetaSelfHostedWorkStateActive BetaSelfHostedWorkState = "active"

const BetaSelfHostedWorkStateStopping BetaSelfHostedWorkState = "stopping"

const BetaSelfHostedWorkStateStopped BetaSelfHostedWorkState = "stopped"

StopRequestedAt string

RFC 3339 timestamp when stop was requested

StoppedAt string

RFC 3339 timestamp when work execution stopped

Type Work

The type of object (always 'work')

type BetaSelfHostedWorkHeartbeatResponse struct{…}

Response after recording a heartbeat for a work item.

LastHeartbeat string

RFC 3339 timestamp of the actual heartbeat from DB

LeaseExtended bool

Whether the heartbeat succeeded in extending the lease

State BetaSelfHostedWorkHeartbeatResponseState

Current state of the work item (active/stopping/stopped)

One of the following:

const BetaSelfHostedWorkHeartbeatResponseStateQueued BetaSelfHostedWorkHeartbeatResponseState = "queued"

const BetaSelfHostedWorkHeartbeatResponseStateStarting BetaSelfHostedWorkHeartbeatResponseState = "starting"

const BetaSelfHostedWorkHeartbeatResponseStateActive BetaSelfHostedWorkHeartbeatResponseState = "active"

const BetaSelfHostedWorkHeartbeatResponseStateStopping BetaSelfHostedWorkHeartbeatResponseState = "stopping"

const BetaSelfHostedWorkHeartbeatResponseStateStopped BetaSelfHostedWorkHeartbeatResponseState = "stopped"

TTLSeconds int64

Effective TTL applied to the lease

Type WorkHeartbeat

The type of response

type BetaSelfHostedWorkListResponse struct{…}

Response when listing work items with cursor-based pagination.

Data [][BetaSelfHostedWork](api/beta.md)

List of work items

ID string

Work identifier (e.g., 'work\_...')

AcknowledgedAt string

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

CreatedAt string

RFC 3339 timestamp when work was created

Data [BetaSessionWorkData](api/beta.md)

The actual work to be performed

ID string

Session identifier (e.g., 'session\_...')

Type Session

Type of work data

EnvironmentID string

Environment identifier this work belongs to (e.g., `env_...`)

LatestHeartbeatAt string

RFC 3339 timestamp of the most recent heartbeat

Metadata map[string, string]

User-provided metadata key-value pairs associated with this work item

StartedAt string

RFC 3339 timestamp when work execution started

State BetaSelfHostedWorkState

Current state of the work item

One of the following:

const BetaSelfHostedWorkStateQueued BetaSelfHostedWorkState = "queued"

const BetaSelfHostedWorkStateStarting BetaSelfHostedWorkState = "starting"

const BetaSelfHostedWorkStateActive BetaSelfHostedWorkState = "active"

const BetaSelfHostedWorkStateStopping BetaSelfHostedWorkState = "stopping"

const BetaSelfHostedWorkStateStopped BetaSelfHostedWorkState = "stopped"

StopRequestedAt string

RFC 3339 timestamp when stop was requested

StoppedAt string

RFC 3339 timestamp when work execution stopped

Type Work

The type of object (always 'work')

NextPage string

Opaque cursor for fetching the next page of results

type BetaSelfHostedWorkQueueStats struct{…}

Statistics about the work queue for an environment.

Uses Redis Stream consumer group metrics for O(1) queries.

Depth int64

Number of work items waiting to be picked up (lag from consumer group)

OldestQueuedAt string

RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

Pending int64

Number of work items being processed (polled but not acknowledged)

Type WorkQueueStats

The type of object

WorkersPolling int64

Number of workers that have polled for work in the last 30 seconds. Requires worker\_id to be sent with poll requests.

type BetaSelfHostedWorkStopRequest struct{…}

Request to stop a work item.

Force boolOptional

If true, immediately stop work without graceful shutdown

type BetaSelfHostedWorkUpdateRequest struct{…}

Request to update work item metadata.

Metadata map[string, string]

Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

type BetaSessionWorkData struct{…}

Work data for session work items.

This resource type is used when work represents a session that needs to be executed
in a self-hosted environment.

ID string

Session identifier (e.g., 'session\_...')

Type Session

Type of work data

---

*Copyright © Anthropic. All rights reserved.*
