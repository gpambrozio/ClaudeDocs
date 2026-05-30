# Record Heartbeat

Copy page

SDK language

PHP

# Record Heartbeat

$client->beta->environments->work->heartbeat(string workID, string environmentID, ?int desiredTTLSeconds, ?string expectedLastHeartbeat, ?list<AnthropicBeta> betas): [SelfHostedWorkHeartbeatResponse](api/beta.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Record a heartbeat for a work item to maintain the lease.

##### ParametersExpand Collapse

environmentID: string

workID: string

desiredTTLSeconds?:optional int

Desired TTL in seconds

expectedLastHeartbeat?:optional string

Expected last\_heartbeat for conditional update (optimistic concurrency). Use literal 'NO\_HEARTBEAT' to claim an unclaimed lease (first heartbeat). For subsequent heartbeats, echo the server's previous last\_heartbeat value exactly. Returns 412 Precondition Failed if the actual value doesn't match.

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

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

Record Heartbeat

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaSelfHostedWorkHeartbeatResponse = $client
  ->beta
  ->environments
  ->work
  ->heartbeat(
  'work_id',
  environmentID: 'env_011CZkZ9X2dpNyB7HsEFoRfW',
  desiredTTLSeconds: 0,
  expectedLastHeartbeat: 'expected_last_heartbeat',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaSelfHostedWorkHeartbeatResponse);
```

Response 200

```shiki
{
  "last_heartbeat": "last_heartbeat",
  "lease_extended": true,
  "state": "queued",
  "ttl_seconds": 0,
  "type": "work_heartbeat"
}
```

##### Returns Examples

Response 200

```shiki
{
  "last_heartbeat": "last_heartbeat",
  "lease_extended": true,
  "state": "queued",
  "ttl_seconds": 0,
  "type": "work_heartbeat"
}
```

---

*Copyright © Anthropic. All rights reserved.*
