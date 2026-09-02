# Create Deployment

Copy page



cURL

# Create Deployment

POST/v1/deployments

Create Deployment

##### Headers



"anthropic-beta": optional array of [AnthropicBeta](api/http/beta.md)

Optional header to specify the beta version(s) you want to use.

One of the following:

string



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 41 more

One of the following:

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

"user-profiles-2026-08-18"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"dreaming-2026-04-21"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"server-side-fallback-2026-07-01"

"fallback-credit-2026-06-01"

"fallback-credit-2026-07-01"

"agent-memory-2026-07-22"

"mid-conversation-tool-changes-2026-07-01"

"compact-2026-01-12"

"computer-use-2025-11-24"

"mcp-tunnels-2026-06-22"

"structured-outputs-2025-11-13"

"task-budgets-2026-03-13"

"thinking-display-updates-2026-08-18"

"ce-user-management-2026-07-13"

"mid-conversation-output-config-2026-07-01"

"thinking-binding-controls-2026-08-01"

"mid-conversation-system-clear-at-2026-08-21"

##### Body



agent: string or [BetaManagedAgentsAgentParams](api/http/beta/sessions.md) { id, type, version }

Agent to deploy. Accepts the `agent` ID string, which pins the latest version, or an `agent` object with both id and version specified. The agent must exist and not be archived.

One of the following:

string



BetaManagedAgentsAgentParams object{ id, type, version }

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version



id: string

The `agent` ID.

minLength1

maxLength128

type: "agent"



version: optional number

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

formatint32



environment\_id: string

ID of the `environment` defining the container configuration for sessions created from this deployment.

minLength1

maxLength128



initial\_events: array of [BetaManagedAgentsDeploymentInitialEventParams](api/http/beta/deployments.md)

Events to send to each session immediately after creation. At least 1, maximum 50.

One of the following:



BetaManagedAgentsUserMessageEventParams object{ content, type }

Parameters for sending a user message to the session.



BetaManagedAgentsUserDefineOutcomeEventParams object{ description, rubric, type, max\_iterations }

Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.



BetaManagedAgentsSystemMessageEventParams object{ content, type }

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.



content: array of [BetaManagedAgentsSystemContentBlock](api/http/beta/sessions.md) { text, type }

System content blocks to append. Text-only.



text: string

The text content.

minLength1

type: "text"

type: "system.message"



name: string

Human-readable name for the deployment.

minLength1

maxLength256



budget: optional [BetaManagedAgentsBudgetLimit](api/http/beta/sessions.md) { max\_list\_cost, type } or null

A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.



max\_list\_cost: [BetaMonetaryAmount](api/http/beta.md) { amount, currency }

A monetary amount in a specific currency.

amount: string

Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

currency: [BetaCurrency](api/http/beta.md)

Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

type: "limit"



description: optional string or null

Description of what the deployment does.

maxLength2048

metadata: optional map[string]

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.



resources: optional array of [BetaManagedAgentsGitHubRepositoryResourceParams](api/http/beta/sessions.md) { authorization\_token, type, url, 2 more } or [BetaManagedAgentsFileResourceParams](api/http/beta/sessions.md) { file\_id, type, mount\_path } or [BetaManagedAgentsMemoryStoreResourceParam](api/http/beta/sessions.md) { memory\_store\_id, type, access, instructions }

Resources (e.g. repositories, files) to mount into each session's container. Maximum 500.

One of the following:



BetaManagedAgentsGitHubRepositoryResourceParams object{ authorization\_token, type, url, 2 more }

Mount a GitHub repository into the session's container.



BetaManagedAgentsFileResourceParams object{ file\_id, type, mount\_path }

Mount a file uploaded via the Files API into the session.



file\_id: string

ID of a previously uploaded file.

minLength1

maxLength128

type: "file"



mount\_path: optional string or null

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

minLength1

maxLength4096



BetaManagedAgentsMemoryStoreResourceParam object{ memory\_store\_id, type, access, instructions }

Parameters for attaching a memory store to an agent session.

memory\_store\_id: string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: "memory\_store"



access: optional "read\_write" or "read\_only" or null

Access mode for an attached memory store.

One of the following:

"read\_write"

"read\_only"



instructions: optional string or null

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

maxLength4096



schedule: optional [BetaManagedAgentsScheduleParams](api/http/beta/deployments.md) { expression, timezone, type } or null

5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.



expression: string

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

minLength1

maxLength256



timezone: string

Required. IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC"). Validated against the IANA timezone database.

minLength1

type: "cron"

vault\_ids: optional array of string

Vault IDs for stored credentials the agent can use during sessions created from this deployment. Maximum 50.

##### Returns



BetaManagedAgentsDeployment object{ id, agent, archived\_at, 14 more }

A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

Create Deployment

cURL

```shiki
curl https://api.anthropic.com/v1/deployments \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "agent": "string",
          "environment_id": "x",
          "initial_events": [
            {
              "content": [
                {
                  "text": "Where is my order #1234?",
                  "type": "text"
                }
              ],
              "type": "user.message"
            }
          ],
          "name": "x"
        }'
```

Response 200



```shiki
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
```

##### Returns Examples

Response 200



```shiki
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
```

---

*Copyright © Anthropic. All rights reserved.*
