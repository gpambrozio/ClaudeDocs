# Get Queue Statistics

Copy page

Python

# Get Queue Statistics

beta.environments.work.stats(strenvironment\_id, WorkStatsParams\*\*kwargs)  -> [BetaSelfHostedWorkQueueStats](api/beta.md)

GET/v1/environments/{environment\_id}/work/stats

Get statistics about the work queue for an environment.

##### ParametersExpand Collapse

environment\_id: str

betas: Optional[List[[AnthropicBetaParam](api/beta.md)]]

Optional header to specify the beta version(s) you want to use.

One of the following:

str

Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 24 more]

One of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"thinking-token-count-2026-05-13"

"mid-conversation-system-2026-04-07"

##### ReturnsExpand Collapse

class BetaSelfHostedWorkQueueStats: …

Statistics about the work queue for an environment.

Uses Redis Stream consumer group metrics for O(1) queries.

depth: int

Number of work items waiting to be picked up (lag from consumer group)

oldest\_queued\_at: Optional[str]

RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

pending: int

Number of work items being processed (polled but not acknowledged)

type: Literal["work\_queue\_stats"]

The type of object

workers\_polling: Optional[int]

Number of workers that have polled for work in the last 30 seconds. Requires worker\_id to be sent with poll requests.

Get Queue Statistics

Python

```shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_self_hosted_work_queue_stats = client.beta.environments.work.stats(
    environment_id="env_011CZkZ9X2dpNyB7HsEFoRfW",
)
print(beta_self_hosted_work_queue_stats.depth)
```

Response 200

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
