# Get Queue Statistics

Copy page



Ruby

# Get Queue Statistics

beta.environments.work.stats(environment\_id, \*\*kwargs) -> [BetaSelfHostedWorkQueueStats](api/beta.md) { depth, oldest\_queued\_at, pending, 2 more }

GET/v1/environments/{environment\_id}/work/stats

Get statistics about the work queue for an environment.

##### ParametersExpand Collapse

environment\_id: String

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

class BetaSelfHostedWorkQueueStats { depth, oldest\_queued\_at, pending, 2 more } 

Statistics about the work queue for an environment.

Uses Redis Stream consumer group metrics for O(1) queries.

depth: Integer

Number of work items waiting to be picked up (lag from consumer group)

oldest\_queued\_at: String

RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

pending: Integer

Number of work items being processed (polled but not acknowledged)

type: :work\_queue\_stats

The type of object

workers\_polling: Integer

Number of workers that have polled for work in the last 30 seconds. Requires worker\_id to be sent with poll requests.

Get Queue Statistics

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_self_hosted_work_queue_stats = anthropic.beta.environments.work.stats("env_011CZkZ9X2dpNyB7HsEFoRfW")

puts(beta_self_hosted_work_queue_stats)
```

Response 200



```shiki
{
  "depth": 0,
  "oldest_queued_at": "oldest_queued_at",
  "pending": 0,
  "type": "work_queue_stats",
  "workers_polling": 0
}
```

##### Returns Examples

Response 200



```shiki
{
  "depth": 0,
  "oldest_queued_at": "oldest_queued_at",
  "pending": 0,
  "type": "work_queue_stats",
  "workers_polling": 0
}
```

---

*Copyright © Anthropic. All rights reserved.*
