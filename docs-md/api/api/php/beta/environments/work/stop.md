# Stop Work

Copy page

PHP

# Stop Work

$client->beta->environments->work->stop(string workID, string environmentID, ?bool force, ?list<AnthropicBeta> betas): [SelfHostedWork](api/beta.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Stop a work item, initiating graceful or forced shutdown.

##### ParametersExpand Collapse

environmentID: string

workID: string

force?:optional bool

If true, immediately stop work without graceful shutdown

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

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

Stop Work

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaSelfHostedWork = $client->beta->environments->work->stop(
  'work_id',
  environmentID: 'env_011CZkZ9X2dpNyB7HsEFoRfW',
  force: true,
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaSelfHostedWork);
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
