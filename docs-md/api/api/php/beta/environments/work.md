# Work

Copy page

PHP

# Work

##### [Get Work Item](api/beta/environments/work/retrieve.md)

$client->beta->environments->work->retrieve(string workID, string environmentID, ?list<AnthropicBeta> betas): [SelfHostedWork](api/beta.md)

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

$client->beta->environments->work->poll(string environmentID, ?int blockMs, ?int reclaimOlderThanMs, ?list<AnthropicBeta> betas, ?string anthropicWorkerID): [SelfHostedWork](api/beta.md)

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

$client->beta->environments->work->ack(string workID, string environmentID, ?list<AnthropicBeta> betas): [SelfHostedWork](api/beta.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

$client->beta->environments->work->heartbeat(string workID, string environmentID, ?int desiredTTLSeconds, ?string expectedLastHeartbeat, ?list<AnthropicBeta> betas): [SelfHostedWorkHeartbeatResponse](api/beta.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

$client->beta->environments->work->stop(string workID, string environmentID, ?bool force, ?list<AnthropicBeta> betas): [SelfHostedWork](api/beta.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

$client->beta->environments->work->list(string environmentID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[SelfHostedWork](api/beta.md)>

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

$client->beta->environments->work->update(string workID, string environmentID, array<string,string> metadata, ?list<AnthropicBeta> betas): [SelfHostedWork](api/beta.md)

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

$client->beta->environments->work->stats(string environmentID, ?list<AnthropicBeta> betas): [SelfHostedWorkQueueStats](api/beta.md)

GET/v1/environments/{environment\_id}/work/stats

##### ModelsExpand Collapse

[SelfHostedWork](api/beta.md)

string id

Work identifier (e.g., 'work\_...')

?string acknowledgedAt

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

string createdAt

RFC 3339 timestamp when work was created

[SessionWorkData](api/beta.md) data

The actual work to be performed

string environmentID

Environment identifier this work belongs to (e.g., `env_...`)

?string latestHeartbeatAt

RFC 3339 timestamp of the most recent heartbeat

array<string,string> metadata

User-provided metadata key-value pairs associated with this work item

?string startedAt

RFC 3339 timestamp when work execution started

State state

Current state of the work item

?string stopRequestedAt

RFC 3339 timestamp when stop was requested

?string stoppedAt

RFC 3339 timestamp when work execution stopped

"work" type

The type of object (always 'work')

[SelfHostedWorkHeartbeatResponse](api/beta.md)

string lastHeartbeat

RFC 3339 timestamp of the actual heartbeat from DB

bool leaseExtended

Whether the heartbeat succeeded in extending the lease

State state

Current state of the work item (active/stopping/stopped)

int ttlSeconds

Effective TTL applied to the lease

"work\_heartbeat" type

The type of response

[SelfHostedWorkListResponse](api/beta.md)

list<[SelfHostedWork](api/beta.md)> data

List of work items

?string nextPage

Opaque cursor for fetching the next page of results

[SelfHostedWorkQueueStats](api/beta.md)

int depth

Number of work items waiting to be picked up (lag from consumer group)

?string oldestQueuedAt

RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

int pending

Number of work items being processed (polled but not acknowledged)

"work\_queue\_stats" type

The type of object

?int workersPolling

Number of workers that have polled for work in the last 30 seconds. Requires worker\_id to be sent with poll requests.

[SelfHostedWorkStopRequest](api/beta.md)

?bool force

If true, immediately stop work without graceful shutdown

[SelfHostedWorkUpdateRequest](api/beta.md)

array<string,string> metadata

Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

[SessionWorkData](api/beta.md)

string id

Session identifier (e.g., 'session\_...')

"session" type

Type of work data

---

*Copyright © Anthropic. All rights reserved.*
