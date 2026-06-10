# List Deployment Runs

Copy page

SDK language

Ruby

# List Deployment Runs

beta.deployment\_runs.list(\*\*kwargs) -> PageCursor<[BetaManagedAgentsDeploymentRun](api/beta.md) { id, agent, created\_at, 5 more } >

GET/v1/deployment\_runs

List Deployment Runs

##### ParametersExpand Collapse

created\_at\_gt: Time

Return runs created strictly after this time (exclusive).

created\_at\_gte: Time

Return runs created at or after this time (inclusive).

created\_at\_lt: Time

Return runs created strictly before this time (exclusive).

created\_at\_lte: Time

Return runs created at or before this time (inclusive).

deployment\_id: String

Filter to a specific deployment. Omit to list across all deployments in the workspace. Filtering by a non-existent deployment\_id returns 200 with empty data.

has\_error: bool

Filter: true for runs with non-null error, false for runs with non-null session\_id. Omit for all.

limit: Integer

Maximum results per page. Default 20, maximum 1000.

page: String

Opaque pagination cursor. Pass next\_page from the previous response. Invalid or expired cursors return 400.

trigger\_type: [BetaManagedAgentsTriggerType](api/beta.md)

Filter runs by what triggered them. Omit to return all runs.

One of the following:

:schedule

:manual

betas: Array[[AnthropicBeta](api/beta.md)]

Optional header to specify the beta version(s) you want to use.

One of the following:

String = String

AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 25 more

One of the following:

:"message-batches-2024-09-24"

:"prompt-caching-2024-07-31"

:"computer-use-2024-10-22"

:"computer-use-2025-01-24"

:"pdfs-2024-09-25"

:"token-counting-2024-11-01"

:"token-efficient-tools-2025-02-19"

:"output-128k-2025-02-19"

:"files-api-2025-04-14"

:"mcp-client-2025-04-04"

:"mcp-client-2025-11-20"

:"dev-full-thinking-2025-05-14"

:"interleaved-thinking-2025-05-14"

:"code-execution-2025-05-22"

:"extended-cache-ttl-2025-04-11"

:"context-1m-2025-08-07"

:"context-management-2025-06-27"

:"model-context-window-exceeded-2025-08-26"

:"skills-2025-10-02"

:"fast-mode-2026-02-01"

:"output-300k-2026-03-24"

:"user-profiles-2026-03-24"

:"advisor-tool-2026-03-01"

:"managed-agents-2026-04-01"

:"cache-diagnosis-2026-04-07"

:"thinking-token-count-2026-05-13"

:"server-side-fallback-2026-06-01"

:"fallback-credit-2026-06-01"

##### ReturnsExpand Collapse

class BetaManagedAgentsDeploymentRun { id, agent, created\_at, 5 more }

A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

id: String

Unique identifier for this run (`drun_...`).

agent: [BetaManagedAgentsAgentReference](api/beta.md) { id, type, version }

A resolved agent reference with a concrete version.

id: String

type: :agent

version: Integer

created\_at: Time

A timestamp in RFC 3339 format

deployment\_id: String

ID of the deployment that produced this run.

error: [BetaManagedAgentsEnvironmentArchivedRunError](api/beta.md) { message, type }  | [BetaManagedAgentsAgentArchivedRunError](api/beta.md) { message, type }  | [BetaManagedAgentsEnvironmentNotFoundRunError](api/beta.md) { message, type }  | 13 more

Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

One of the following:

class BetaManagedAgentsEnvironmentArchivedRunError { message, type }

The deployment's environment was archived.

message: String

Human-readable error description.

type: :environment\_archived\_error

class BetaManagedAgentsAgentArchivedRunError { message, type }

The deployment's agent was archived.

message: String

Human-readable error description.

type: :agent\_archived\_error

class BetaManagedAgentsEnvironmentNotFoundRunError { message, type }

The deployment's environment no longer exists.

message: String

Human-readable error description.

type: :environment\_not\_found\_error

class BetaManagedAgentsVaultNotFoundRunError { message, type }

A vault referenced by the deployment no longer exists.

message: String

Human-readable error description.

type: :vault\_not\_found\_error

class BetaManagedAgentsVaultArchivedRunError { message, type }

A vault referenced by the deployment is archived.

message: String

Human-readable error description.

type: :vault\_archived\_error

class BetaManagedAgentsFileNotFoundRunError { message, type }

A file resource referenced by the deployment no longer exists.

message: String

Human-readable error description.

type: :file\_not\_found\_error

class BetaManagedAgentsMemoryStoreArchivedRunError { message, type }

A memory store referenced by the deployment is archived.

message: String

Human-readable error description.

type: :memory\_store\_archived\_error

class BetaManagedAgentsSkillNotFoundRunError { message, type }

A skill referenced by the deployment's agent no longer exists.

message: String

Human-readable error description.

type: :skill\_not\_found\_error

class BetaManagedAgentsSessionResourceNotFoundRunError { message, type }

A referenced resource no longer exists and its kind was not reported.

message: String

Human-readable error description.

type: :session\_resource\_not\_found\_error

class BetaManagedAgentsWorkspaceArchivedRunError { message, type }

The deployment's workspace was archived.

message: String

Human-readable error description.

type: :workspace\_archived\_error

class BetaManagedAgentsOrganizationDisabledRunError { message, type }

The deployment's organization is disabled.

message: String

Human-readable error description.

type: :organization\_disabled\_error

class BetaManagedAgentsSessionRateLimitedRunError { message, type }

Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

message: String

Human-readable error description.

type: :session\_rate\_limited\_error

class BetaManagedAgentsSessionCreationRejectedRunError { message, type }

The session create request was rejected with a non-retryable validation error.

message: String

Human-readable error description.

type: :session\_creation\_rejected\_error

class BetaManagedAgentsUnknownRunError { message, type }

An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

message: String

Human-readable error description.

type: :unknown\_error

class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError { message, type }

The deployment configures resources, but its environment is self-hosted and cannot mount them.

message: String

Human-readable error description.

type: :self\_hosted\_resources\_unsupported\_error

class BetaManagedAgentsMCPEgressBlockedRunError { message, type }

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

message: String

Human-readable error description.

type: :mcp\_egress\_blocked\_error

session\_id: String

Populated on success. Null on creation failure. Exactly one of session\_id or error is non-null.

trigger\_context: [BetaManagedAgentsTriggerContext](api/beta.md)

Describes what triggered a deployment run, with trigger-specific metadata.

One of the following:

class BetaManagedAgentsScheduleTriggerContext { scheduled\_at, type }

The run was fired by the deployment's cron schedule.

scheduled\_at: Time

A timestamp in RFC 3339 format

type: :schedule

class BetaManagedAgentsManualTriggerContext { type }

The run was started manually by creating a session directly against the deployment.

type: :manual

type: :deployment\_run

List Deployment Runs

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.deployment_runs.list

puts(page)
```

Response 200



```shiki
{
  "data": [
    {
      "id": "id",
      "agent": {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "type": "agent",
        "version": 1
      },
      "created_at": "2019-12-27T18:11:19.117Z",
      "deployment_id": "deployment_id",
      "error": {
        "message": "message",
        "type": "environment_archived_error"
      },
      "session_id": "session_id",
      "trigger_context": {
        "scheduled_at": "2019-12-27T18:11:19.117Z",
        "type": "schedule"
      },
      "type": "deployment_run"
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
      "agent": {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "type": "agent",
        "version": 1
      },
      "created_at": "2019-12-27T18:11:19.117Z",
      "deployment_id": "deployment_id",
      "error": {
        "message": "message",
        "type": "environment_archived_error"
      },
      "session_id": "session_id",
      "trigger_context": {
        "scheduled_at": "2019-12-27T18:11:19.117Z",
        "type": "schedule"
      },
      "type": "deployment_run"
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
