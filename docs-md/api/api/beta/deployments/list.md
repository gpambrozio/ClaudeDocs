# List Deployments

Copy page



cURL

# List Deployments

GET/v1/deployments

List Deployments

##### Query parameters

agent\_id: optional string

Filter by agent ID.



"created\_at[gte]": optional string

Return deployments created at or after this time (inclusive).

formatdate-time



"created\_at[lte]": optional string

Return deployments created at or before this time (inclusive).

formatdate-time

include\_archived: optional boolean

When true, includes archived deployments. Default: false (exclude archived).



limit: optional number

Maximum results per page. Default 20, maximum 100.

formatint32

page: optional string

Opaque pagination cursor.



status: optional [BetaManagedAgentsDeploymentStatus](api/http/beta/deployments.md)

Filter by status: active or paused. Omit for both. To include archived deployments, use include\_archived instead; the two cannot be combined.

One of the following:

"active"

"paused"

##### Headers



"anthropic-beta": optional array of [AnthropicBeta](api/http/beta.md)

Optional header to specify the beta version(s) you want to use.

One of the following:

string



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more

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

"user-profiles-2026-08-18"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"dreaming-2026-04-21"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"server-side-fallback-2026-07-01"

"fallback-credit-2026-06-01"

"fallback-credit-2026-07-01"

"agent-memory-2026-07-22"

"mid-conversation-tool-changes-2026-07-01"

"compact-2026-01-12"

"computer-use-2025-11-24"

"mcp-tunnels-2026-06-22"

"structured-outputs-2025-11-13"

"task-budgets-2026-03-13"

"thinking-display-updates-2026-08-18"

"ce-user-management-2026-07-13"

##### Returns



data: array of [BetaManagedAgentsDeployment](api/http/beta/deployments.md) { id, agent, archived\_at, 14 more }

List of deployments.

id: string

Unique identifier for this deployment.



agent: [BetaManagedAgentsAgentReference](api/http/beta/agents.md) { id, type, version }

A resolved agent reference with a concrete version.

id: string

type: "agent"



version: number

formatint32



archived\_at: string or null

A timestamp in RFC 3339 format

formatdate-time



created\_at: string

A timestamp in RFC 3339 format

formatdate-time

description: string or null

Description of what the deployment does.

environment\_id: string

ID of the `environment` where sessions run.



initial\_events: array of [BetaManagedAgentsDeploymentInitialEvent](api/http/beta/deployments.md)

Events sent to each session immediately after creation.

One of the following:



BetaManagedAgentsDeploymentUserMessageEvent object{ content, type }

A user message sent to the session.



BetaManagedAgentsDeploymentUserDefineOutcomeEvent object{ description, rubric, type, max\_iterations }

An outcome the agent should work toward. The agent begins work on receipt.



BetaManagedAgentsDeploymentSystemMessageEvent object{ content, type }

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.



content: array of [BetaManagedAgentsSystemContentBlock](api/http/beta/sessions.md) { text, type }

System content blocks to append. Text-only.



text: string

The text content.

minLength1

type: "text"

type: "system.message"

metadata: map[string]

Arbitrary key-value metadata. Maximum 16 pairs.

name: string

Human-readable name.



paused\_reason: [BetaManagedAgentsDeploymentPausedReason](api/http/beta/deployments.md) or null

Why a deployment is paused. Non-null exactly when `status` is `paused`.

One of the following:



BetaManagedAgentsManualDeploymentPausedReason object{ type }

The caller invoked the pause endpoint on the deployment.

type: "manual"



BetaManagedAgentsErrorDeploymentPausedReason object{ error, type }

A scheduled fire recorded a failed run whose error auto-pauses the deployment.



error: [BetaManagedAgentsDeploymentPausedReasonError](api/http/beta/deployments.md)

The error that triggered an auto-pause. Matches the failed run's `error.type`.

One of the following:

type: "error"



resources: array of [BetaManagedAgentsSessionResourceConfig](api/http/beta/deployments.md)

Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

One of the following:



BetaManagedAgentsGitHubRepositoryResourceConfig object{ type, url, checkout, mount\_path }

A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.



BetaManagedAgentsFileResourceConfig object{ file\_id, type, mount\_path }

A file mounted into each session's container.

file\_id: string

ID of a previously uploaded file.

type: "file"

mount\_path: optional string or null

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.



BetaManagedAgentsMemoryStoreResourceConfig object{ memory\_store\_id, type, access, instructions }

A memory store attached to each session created from this deployment.

memory\_store\_id: string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: "memory\_store"



access: optional "read\_write" or "read\_only" or null

Access mode for an attached memory store.

One of the following:

"read\_write"

"read\_only"

instructions: optional string or null

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.



schedule: [BetaManagedAgentsSchedule](api/http/beta/deployments.md) { expression, timezone, type, 2 more } or null

5-field POSIX cron schedule with computed runtime timestamps.



expression: string

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

minLength1

maxLength256



timezone: string

IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC").

minLength1

type: "cron"



last\_run\_at: optional string or null

A timestamp in RFC 3339 format

formatdate-time

upcoming\_runs\_at: optional array of string

Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.



status: [BetaManagedAgentsDeploymentStatus](api/http/beta/deployments.md)

Lifecycle status of a deployment.

One of the following:

"active"

"paused"

type: "deployment"



updated\_at: string

A timestamp in RFC 3339 format

formatdate-time

vault\_ids: array of string

Vault IDs supplying stored credentials for sessions created from this deployment.



budget: optional [BetaManagedAgentsBudgetLimit](api/http/beta/sessions.md) { max\_list\_cost, type } or null

A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.



max\_list\_cost: [BetaMonetaryAmount](api/http/beta.md) { amount, currency }

A monetary amount in a specific currency.

amount: string

Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

currency: [BetaCurrency](api/http/beta.md)

Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

type: "limit"

next\_page: optional string or null

Opaque cursor for the next page. Null when no more results.

### List Deployments

cURL



```shiki
curl https://api.anthropic.com/v1/deployments \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```shiki
{
  "data": [
    {
      "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
      "agent": {
        "id": "agent_011CZkYpogX7uDKUyvBTophP",
        "type": "agent",
        "version": 1
      },
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "description": "Compiles yesterday's orders into a report every weekday morning.",
      "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
      "initial_events": [
        {
          "content": [
            {
              "text": "Compile yesterday's orders into report.md.",
              "type": "text"
            }
          ],
          "type": "user.message"
        }
      ],
      "metadata": {},
      "name": "Daily order report",
      "paused_reason": {
        "type": "manual"
      },
      "resources": [
        {
          "type": "github_repository",
          "url": "url",
          "checkout": {
            "name": "main",
            "type": "branch"
          },
          "mount_path": "mount_path"
        }
      ],
      "schedule": {
        "expression": "0 9 * * 1-5",
        "timezone": "America/Los_Angeles",
        "type": "cron",
        "last_run_at": "2026-03-16T16:00:09Z",
        "upcoming_runs_at": [
          "2026-03-17T16:00:00Z",
          "2026-03-18T16:00:00Z"
        ]
      },
      "status": "active",
      "type": "deployment",
      "updated_at": "2026-03-15T10:00:00Z",
      "vault_ids": [
        "vlt_011CZkZDLs7fYzm1hXNPeRjv"
      ],
      "budget": {
        "max_list_cost": {
          "amount": "2500",
          "currency": "USD"
        },
        "type": "limit"
      }
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
      "agent": {
        "id": "agent_011CZkYpogX7uDKUyvBTophP",
        "type": "agent",
        "version": 1
      },
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "description": "Compiles yesterday's orders into a report every weekday morning.",
      "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
      "initial_events": [
        {
          "content": [
            {
              "text": "Compile yesterday's orders into report.md.",
              "type": "text"
            }
          ],
          "type": "user.message"
        }
      ],
      "metadata": {},
      "name": "Daily order report",
      "paused_reason": {
        "type": "manual"
      },
      "resources": [
        {
          "type": "github_repository",
          "url": "url",
          "checkout": {
            "name": "main",
            "type": "branch"
          },
          "mount_path": "mount_path"
        }
      ],
      "schedule": {
        "expression": "0 9 * * 1-5",
        "timezone": "America/Los_Angeles",
        "type": "cron",
        "last_run_at": "2026-03-16T16:00:09Z",
        "upcoming_runs_at": [
          "2026-03-17T16:00:00Z",
          "2026-03-18T16:00:00Z"
        ]
      },
      "status": "active",
      "type": "deployment",
      "updated_at": "2026-03-15T10:00:00Z",
      "vault_ids": [
        "vlt_011CZkZDLs7fYzm1hXNPeRjv"
      ],
      "budget": {
        "max_list_cost": {
          "amount": "2500",
          "currency": "USD"
        },
        "type": "limit"
      }
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

---

*Copyright © Anthropic. All rights reserved.*
