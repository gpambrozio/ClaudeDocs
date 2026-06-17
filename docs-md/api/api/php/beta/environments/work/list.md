# List Work Items

Copy page



PHP

# List Work Items

$client->beta->environments->work->list(string environmentID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[SelfHostedWork](api/beta.md)>

GET/v1/environments/{environment\_id}/work

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

List work items in an environment.

##### ParametersExpand Collapse

environmentID: string

limit?:optional int

Maximum number of work items to return

page?:optional string

Opaque cursor from previous response for pagination

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



[SelfHostedWork](api/beta.md)

string id

Work identifier (e.g., 'work\_...')

?string acknowledgedAt

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

string createdAt

RFC 3339 timestamp when work was created

[SessionWorkData](api/beta.md) data

The actual work to be performed

string environmentID

Environment identifier this work belongs to (e.g., `env_...`)

?string latestHeartbeatAt

RFC 3339 timestamp of the most recent heartbeat

array<string,string> metadata

User-provided metadata key-value pairs associated with this work item

?string startedAt

RFC 3339 timestamp when work execution started

State state

Current state of the work item

?string stopRequestedAt

RFC 3339 timestamp when stop was requested

?string stoppedAt

RFC 3339 timestamp when work execution stopped

"work" type

The type of object (always 'work')

List Work Items

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->environments->work->list(
  'env_011CZkZ9X2dpNyB7HsEFoRfW',
  limit: 1,
  page: 'page',
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

Response 200



```shiki
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
