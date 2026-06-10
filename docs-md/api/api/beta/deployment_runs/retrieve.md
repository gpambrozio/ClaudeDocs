# Get Deployment Run

Copy page

SDK language

cURL

# Get Deployment Run

GET/v1/deployment\_runs/{deployment\_run\_id}

Get Deployment Run

##### Path ParametersExpand Collapse

deployment\_run\_id: string

##### Header ParametersExpand Collapse

"anthropic-beta": optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

One of the following:

string

"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more

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

"server-side-fallback-2026-06-01"

"fallback-credit-2026-06-01"

##### ReturnsExpand Collapse

BetaManagedAgentsDeploymentRun object { id, agent, created\_at, 5 more }

A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

id: string

Unique identifier for this run (`drun_...`).

agent: [BetaManagedAgentsAgentReference](api/beta.md) { id, type, version }

A resolved agent reference with a concrete version.

id: string

type: "agent"

version: number

created\_at: string

A timestamp in RFC 3339 format

deployment\_id: string

ID of the deployment that produced this run.

error: [BetaManagedAgentsEnvironmentArchivedRunError](api/beta.md) { message, type }  or [BetaManagedAgentsAgentArchivedRunError](api/beta.md) { message, type }  or [BetaManagedAgentsEnvironmentNotFoundRunError](api/beta.md) { message, type }  or 13 more

Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

One of the following:

BetaManagedAgentsEnvironmentArchivedRunError object { message, type }

The deployment's environment was archived.

message: string

Human-readable error description.

type: "environment\_archived\_error"

BetaManagedAgentsAgentArchivedRunError object { message, type }

The deployment's agent was archived.

message: string

Human-readable error description.

type: "agent\_archived\_error"

BetaManagedAgentsEnvironmentNotFoundRunError object { message, type }

The deployment's environment no longer exists.

message: string

Human-readable error description.

type: "environment\_not\_found\_error"

BetaManagedAgentsVaultNotFoundRunError object { message, type }

A vault referenced by the deployment no longer exists.

message: string

Human-readable error description.

type: "vault\_not\_found\_error"

BetaManagedAgentsVaultArchivedRunError object { message, type }

A vault referenced by the deployment is archived.

message: string

Human-readable error description.

type: "vault\_archived\_error"

BetaManagedAgentsFileNotFoundRunError object { message, type }

A file resource referenced by the deployment no longer exists.

message: string

Human-readable error description.

type: "file\_not\_found\_error"

BetaManagedAgentsMemoryStoreArchivedRunError object { message, type }

A memory store referenced by the deployment is archived.

message: string

Human-readable error description.

type: "memory\_store\_archived\_error"

BetaManagedAgentsSkillNotFoundRunError object { message, type }

A skill referenced by the deployment's agent no longer exists.

message: string

Human-readable error description.

type: "skill\_not\_found\_error"

BetaManagedAgentsSessionResourceNotFoundRunError object { message, type }

A referenced resource no longer exists and its kind was not reported.

message: string

Human-readable error description.

type: "session\_resource\_not\_found\_error"

BetaManagedAgentsWorkspaceArchivedRunError object { message, type }

The deployment's workspace was archived.

message: string

Human-readable error description.

type: "workspace\_archived\_error"

BetaManagedAgentsOrganizationDisabledRunError object { message, type }

The deployment's organization is disabled.

message: string

Human-readable error description.

type: "organization\_disabled\_error"

BetaManagedAgentsSessionRateLimitedRunError object { message, type }

Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

message: string

Human-readable error description.

type: "session\_rate\_limited\_error"

BetaManagedAgentsSessionCreationRejectedRunError object { message, type }

The session create request was rejected with a non-retryable validation error.

message: string

Human-readable error description.

type: "session\_creation\_rejected\_error"

BetaManagedAgentsUnknownRunError object { message, type }

An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

message: string

Human-readable error description.

type: "unknown\_error"

BetaManagedAgentsSelfHostedResourcesUnsupportedRunError object { message, type }

The deployment configures resources, but its environment is self-hosted and cannot mount them.

message: string

Human-readable error description.

type: "self\_hosted\_resources\_unsupported\_error"

BetaManagedAgentsMCPEgressBlockedRunError object { message, type }

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

message: string

Human-readable error description.

type: "mcp\_egress\_blocked\_error"

session\_id: string

Populated on success. Null on creation failure. Exactly one of session\_id or error is non-null.

trigger\_context: [BetaManagedAgentsTriggerContext](api/beta.md)

Describes what triggered a deployment run, with trigger-specific metadata.

One of the following:

BetaManagedAgentsScheduleTriggerContext object { scheduled\_at, type }

The run was fired by the deployment's cron schedule.

scheduled\_at: string

A timestamp in RFC 3339 format

type: "schedule"

BetaManagedAgentsManualTriggerContext object { type }

The run was started manually by creating a session directly against the deployment.

type: "manual"

type: "deployment\_run"

Get Deployment Run

cURL

```shiki
curl https://api.anthropic.com/v1/deployment_runs/$DEPLOYMENT_RUN_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```shiki
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
```

##### Returns Examples

Response 200



```shiki
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
```

---

*Copyright © Anthropic. All rights reserved.*
