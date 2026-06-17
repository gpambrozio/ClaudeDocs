# Record Heartbeat

Copy page



Ruby

# Record Heartbeat

beta.environments.work.heartbeat(work\_id, \*\*kwargs) -> [BetaSelfHostedWorkHeartbeatResponse](api/beta.md) { last\_heartbeat, lease\_extended, state, 2 more }

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Record a heartbeat for a work item to maintain the lease.

##### ParametersExpand Collapse

environment\_id: String

work\_id: String

desired\_ttl\_seconds: Integer

Desired TTL in seconds

expected\_last\_heartbeat: String

Expected last\_heartbeat for conditional update (optimistic concurrency). Use literal 'NO\_HEARTBEAT' to claim an unclaimed lease (first heartbeat). For subsequent heartbeats, echo the server's previous last\_heartbeat value exactly. Returns 412 Precondition Failed if the actual value doesn't match.



betas: Array[[AnthropicBeta](api/beta.md)]

Optional header to specify the beta version(s) you want to use.

One of the following:

String = String



AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 25 more

One of the following:

:"message-batches-2024-09-24"

:"prompt-caching-2024-07-31"

:"computer-use-2024-10-22"

:"computer-use-2025-01-24"

:"pdfs-2024-09-25"

:"token-counting-2024-11-01"

:"token-efficient-tools-2025-02-19"

:"output-128k-2025-02-19"

:"files-api-2025-04-14"

:"mcp-client-2025-04-04"

:"mcp-client-2025-11-20"

:"dev-full-thinking-2025-05-14"

:"interleaved-thinking-2025-05-14"

:"code-execution-2025-05-22"

:"extended-cache-ttl-2025-04-11"

:"context-1m-2025-08-07"

:"context-management-2025-06-27"

:"model-context-window-exceeded-2025-08-26"

:"skills-2025-10-02"

:"fast-mode-2026-02-01"

:"output-300k-2026-03-24"

:"user-profiles-2026-03-24"

:"advisor-tool-2026-03-01"

:"managed-agents-2026-04-01"

:"cache-diagnosis-2026-04-07"

:"thinking-token-count-2026-05-13"

:"server-side-fallback-2026-06-01"

:"fallback-credit-2026-06-01"

##### ReturnsExpand Collapse



class BetaSelfHostedWorkHeartbeatResponse { last\_heartbeat, lease\_extended, state, 2 more } 

Response after recording a heartbeat for a work item.

last\_heartbeat: String

RFC 3339 timestamp of the actual heartbeat from DB

lease\_extended: bool

Whether the heartbeat succeeded in extending the lease



state: :queued | :starting | :active | 2 more

Current state of the work item (active/stopping/stopped)

One of the following:

:queued

:starting

:active

:stopping

:stopped

ttl\_seconds: Integer

Effective TTL applied to the lease

type: :work\_heartbeat

The type of response

Record Heartbeat

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_self_hosted_work_heartbeat_response = anthropic.beta.environments.work.heartbeat("work_id", environment_id: "env_011CZkZ9X2dpNyB7HsEFoRfW")

puts(beta_self_hosted_work_heartbeat_response)
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
