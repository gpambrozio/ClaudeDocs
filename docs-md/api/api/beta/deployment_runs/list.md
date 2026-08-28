# List Deployment Runs

Copy page



cURL

# List Deployment Runs

GET/v1/deployment\_runs

List Deployment Runs

##### Query parameters



"created\_at[gt]": optional string

Return runs created strictly after this time (exclusive).

formatdate-time



"created\_at[gte]": optional string

Return runs created at or after this time (inclusive).

formatdate-time



"created\_at[lt]": optional string

Return runs created strictly before this time (exclusive).

formatdate-time



"created\_at[lte]": optional string

Return runs created at or before this time (inclusive).

formatdate-time

deployment\_id: optional string

Filter to a specific deployment. Omit to list across all deployments in the workspace. Filtering by a non-existent deployment\_id returns 200 with empty data.

has\_error: optional boolean

Filter: true for runs with non-null error, false for runs with non-null session\_id. Omit for all.



limit: optional number

Maximum results per page. Default 20, maximum 1000.

formatint32

page: optional string

Opaque pagination cursor. Pass next\_page from the previous response. Invalid or expired cursors return 400.



trigger\_type: optional [BetaManagedAgentsTriggerType](api/http/beta/deployment_runs.md)

Filter runs by what triggered them. Omit to return all runs.

One of the following:

"schedule"

"manual"

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

data: array of [BetaManagedAgentsDeploymentRun](api/http/beta/deployment_runs.md) { id, agent, created\_at, 5 more }

List of deployment runs.

id: string

Unique identifier for this run (`drun_...`).



agent: [BetaManagedAgentsAgentReference](api/http/beta/agents.md) { id, type, version }

A resolved agent reference with a concrete version.

id: string

type: "agent"



version: number

formatint32



created\_at: string

A timestamp in RFC 3339 format

formatdate-time

deployment\_id: string

ID of the deployment that produced this run.



error: [BetaManagedAgentsEnvironmentArchivedRunError](api/http/beta/deployment_runs.md) { message, type } or [BetaManagedAgentsAgentArchivedRunError](api/http/beta/deployment_runs.md) { message, type } or [BetaManagedAgentsEnvironmentNotFoundRunError](api/http/beta/deployment_runs.md) { message, type } or 13 more or null

Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

One of the following:



BetaManagedAgentsEnvironmentArchivedRunError object{ message, type }

The deployment's environment was archived.

message: string

Human-readable error description.

type: "environment\_archived\_error"



BetaManagedAgentsAgentArchivedRunError object{ message, type }

The deployment's agent was archived.

message: string

Human-readable error description.

type: "agent\_archived\_error"



BetaManagedAgentsEnvironmentNotFoundRunError object{ message, type }

The deployment's environment no longer exists.

message: string

Human-readable error description.

type: "environment\_not\_found\_error"



BetaManagedAgentsVaultNotFoundRunError object{ message, type }

A vault referenced by the deployment no longer exists.

message: string

Human-readable error description.

type: "vault\_not\_found\_error"



BetaManagedAgentsVaultArchivedRunError object{ message, type }

A vault referenced by the deployment is archived.

message: string

Human-readable error description.

type: "vault\_archived\_error"



BetaManagedAgentsFileNotFoundRunError object{ message, type }

A file resource referenced by the deployment no longer exists.

message: string

Human-readable error description.

type: "file\_not\_found\_error"



BetaManagedAgentsMemoryStoreArchivedRunError object{ message, type }

A memory store referenced by the deployment is archived.

message: string

Human-readable error description.

type: "memory\_store\_archived\_error"



BetaManagedAgentsSkillNotFoundRunError object{ message, type }

A skill referenced by the deployment's agent no longer exists.

message: string

Human-readable error description.

type: "skill\_not\_found\_error"



BetaManagedAgentsSessionResourceNotFoundRunError object{ message, type }

A referenced resource no longer exists and its kind was not reported.

message: string

Human-readable error description.

type: "session\_resource\_not\_found\_error"



BetaManagedAgentsWorkspaceArchivedRunError object{ message, type }

The deployment's workspace was archived.

message: string

Human-readable error description.

type: "workspace\_archived\_error"



BetaManagedAgentsOrganizationDisabledRunError object{ message, type }

The deployment's organization is disabled.

message: string

Human-readable error description.

type: "organization\_disabled\_error"



BetaManagedAgentsSessionRateLimitedRunError object{ message, type }

Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

message: string

Human-readable error description.

type: "session\_rate\_limited\_error"



BetaManagedAgentsSessionCreationRejectedRunError object{ message, type }

The session create request was rejected with a non-retryable validation error.

message: string

Human-readable error description.

type: "session\_creation\_rejected\_error"



BetaManagedAgentsUnknownRunError object{ message, type }

An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

message: string

Human-readable error description.

type: "unknown\_error"



BetaManagedAgentsSelfHostedResourcesUnsupportedRunError object{ message, type }

The deployment configures resources, but its environment is self-hosted and cannot mount them.

message: string

Human-readable error description.

type: "self\_hosted\_resources\_unsupported\_error"



BetaManagedAgentsMCPEgressBlockedRunError object{ message, type }

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

message: string

Human-readable error description.

type: "mcp\_egress\_blocked\_error"

session\_id: string or null

Populated on success. Null on creation failure. Exactly one of session\_id or error is non-null.



trigger\_context: [BetaManagedAgentsTriggerContext](api/http/beta/deployment_runs.md)

Describes what triggered a deployment run, with trigger-specific metadata.

One of the following:



BetaManagedAgentsScheduleTriggerContext object{ scheduled\_at, type }

The run was fired by the deployment's cron schedule.



scheduled\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "schedule"



BetaManagedAgentsManualTriggerContext object{ type }

The run was started manually by creating a session directly against the deployment.

type: "manual"

type: "deployment\_run"

next\_page: optional string or null

Opaque cursor for the next page. Null when no more results.



### List Deployment Runs

cURL



```shiki
curl https://api.anthropic.com/v1/deployment_runs \
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
