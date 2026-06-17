# Record Heartbeat

Copy page



CLI

# Record Heartbeat

$ ant beta:environments:work heartbeat

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Record a heartbeat for a work item to maintain the lease.

##### ParametersExpand Collapse

--environment-id: string

Path param

--work-id: string

Path param

--desired-ttl-seconds: optional number

Query param: Desired TTL in seconds

--expected-last-heartbeat: optional string

Query param: Expected last\_heartbeat for conditional update (optimistic concurrency). Use literal 'NO\_HEARTBEAT' to claim an unclaimed lease (first heartbeat). For subsequent heartbeats, echo the server's previous last\_heartbeat value exactly. Returns 412 Precondition Failed if the actual value doesn't match.

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



beta\_self\_hosted\_work\_heartbeat\_response: object { last\_heartbeat, lease\_extended, state, 2 more } 

Response after recording a heartbeat for a work item.

last\_heartbeat: string

RFC 3339 timestamp of the actual heartbeat from DB

lease\_extended: boolean

Whether the heartbeat succeeded in extending the lease



state: "queued" or "starting" or "active" or 2 more

Current state of the work item (active/stopping/stopped)

"queued"

"starting"

"active"

"stopping"

"stopped"

ttl\_seconds: number

Effective TTL applied to the lease

type: "work\_heartbeat"

The type of response

Record Heartbeat

CLI

```shiki
ant beta:environments:work heartbeat \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW \
  --work-id work_id
```

Response 200



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



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
