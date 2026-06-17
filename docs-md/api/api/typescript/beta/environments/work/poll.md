# Poll for Work

Copy page



TypeScript

# Poll for Work

client.beta.environments.work.poll(stringenvironmentID, WorkPollParams { block\_ms, reclaim\_older\_than\_ms, betas, Anthropic-Worker-ID } params?, RequestOptionsoptions?): [BetaSelfHostedWork](api/beta.md) { id, acknowledged\_at, created\_at, 9 more }  | null

GET/v1/environments/{environment\_id}/work/poll

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Long poll for work items in the queue.

##### ParametersExpand Collapse

environmentID: string



params: WorkPollParams { block\_ms, reclaim\_older\_than\_ms, betas, Anthropic-Worker-ID } 

block\_ms?: number | null

Query param: How long to wait for work to arrive before returning. Must be 1-999 in milliseconds. Defaults to non-blocking (returns immediately if no work is available).

reclaim\_older\_than\_ms?: number | null

Query param: Reclaim unacknowledged work items older than this many milliseconds. If omitted, uses the default (5000ms).



betas?: Array<[AnthropicBeta](api/beta.md)>

Header param: Optional header to specify the beta version(s) you want to use.

One of the following:

(string & {})



"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 25 more

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"fallback-credit-2026-06-01"

"Anthropic-Worker-ID"?: string

Header param: Unique identifier for the specific worker polling, used to track aggregated environment-level work metrics in Console

##### ReturnsExpand Collapse



[BetaSelfHostedWork](api/beta.md) { id, acknowledged\_at, created\_at, 9 more }  | null

id: string

Work identifier (e.g., 'work\_...')

acknowledged\_at: string | null

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

created\_at: string

RFC 3339 timestamp when work was created



data: [BetaSessionWorkData](api/beta.md) { id, type } 

The actual work to be performed

id: string

Session identifier (e.g., 'session\_...')

type: "session"

Type of work data

environment\_id: string

Environment identifier this work belongs to (e.g., `env_...`)

latest\_heartbeat\_at: string | null

RFC 3339 timestamp of the most recent heartbeat

metadata: Record<string, string>

User-provided metadata key-value pairs associated with this work item

started\_at: string | null

RFC 3339 timestamp when work execution started



state: "queued" | "starting" | "active" | 2 more

Current state of the work item

One of the following:

"queued"

"starting"

"active"

"stopping"

"stopped"

stop\_requested\_at: string | null

RFC 3339 timestamp when stop was requested

stopped\_at: string | null

RFC 3339 timestamp when work execution stopped

type: "work"

The type of object (always 'work')

Poll for Work

TypeScript

```shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaSelfHostedWork = await client.beta.environments.work.poll('env_011CZkZ9X2dpNyB7HsEFoRfW');

console.log(betaSelfHostedWork.id);
```

Response 200



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



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
