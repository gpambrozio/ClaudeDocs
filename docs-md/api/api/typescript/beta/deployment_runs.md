# Deployment Runs

Copy page

SDK language

TypeScript

# Deployment Runs

##### [List Deployment Runs](api/beta/deployment_runs/list.md)

client.beta.deploymentRuns.list(DeploymentRunListParams { created\_at[gt], created\_at[gte], created\_at[lt], 7 more } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsDeploymentRun](api/beta.md) { id, agent, created\_at, 5 more } >

GET/v1/deployment\_runs

##### [Get Deployment Run](api/beta/deployment_runs/retrieve.md)

client.beta.deploymentRuns.retrieve(stringdeploymentRunID, DeploymentRunRetrieveParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsDeploymentRun](api/beta.md) { id, agent, created\_at, 5 more }

GET/v1/deployment\_runs/{deployment\_run\_id}

##### ModelsExpand Collapse

BetaManagedAgentsAgentArchivedRunError { message, type }

The deployment's agent was archived.

message: string

Human-readable error description.

type: "agent\_archived\_error"

BetaManagedAgentsDeploymentRun { id, agent, created\_at, 5 more }

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

error: [BetaManagedAgentsEnvironmentArchivedRunError](api/beta.md) { message, type }  | [BetaManagedAgentsAgentArchivedRunError](api/beta.md) { message, type }  | [BetaManagedAgentsEnvironmentNotFoundRunError](api/beta.md) { message, type }  | 13 more | null

Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

One of the following:

BetaManagedAgentsEnvironmentArchivedRunError { message, type }

The deployment's environment was archived.

message: string

Human-readable error description.

type: "environment\_archived\_error"

BetaManagedAgentsAgentArchivedRunError { message, type }

The deployment's agent was archived.

message: string

Human-readable error description.

type: "agent\_archived\_error"

BetaManagedAgentsEnvironmentNotFoundRunError { message, type }

The deployment's environment no longer exists.

message: string

Human-readable error description.

type: "environment\_not\_found\_error"

BetaManagedAgentsVaultNotFoundRunError { message, type }

A vault referenced by the deployment no longer exists.

message: string

Human-readable error description.

type: "vault\_not\_found\_error"

BetaManagedAgentsVaultArchivedRunError { message, type }

A vault referenced by the deployment is archived.

message: string

Human-readable error description.

type: "vault\_archived\_error"

BetaManagedAgentsFileNotFoundRunError { message, type }

A file resource referenced by the deployment no longer exists.

message: string

Human-readable error description.

type: "file\_not\_found\_error"

BetaManagedAgentsMemoryStoreArchivedRunError { message, type }

A memory store referenced by the deployment is archived.

message: string

Human-readable error description.

type: "memory\_store\_archived\_error"

BetaManagedAgentsSkillNotFoundRunError { message, type }

A skill referenced by the deployment's agent no longer exists.

message: string

Human-readable error description.

type: "skill\_not\_found\_error"

BetaManagedAgentsSessionResourceNotFoundRunError { message, type }

A referenced resource no longer exists and its kind was not reported.

message: string

Human-readable error description.

type: "session\_resource\_not\_found\_error"

BetaManagedAgentsWorkspaceArchivedRunError { message, type }

The deployment's workspace was archived.

message: string

Human-readable error description.

type: "workspace\_archived\_error"

BetaManagedAgentsOrganizationDisabledRunError { message, type }

The deployment's organization is disabled.

message: string

Human-readable error description.

type: "organization\_disabled\_error"

BetaManagedAgentsSessionRateLimitedRunError { message, type }

Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

message: string

Human-readable error description.

type: "session\_rate\_limited\_error"

BetaManagedAgentsSessionCreationRejectedRunError { message, type }

The session create request was rejected with a non-retryable validation error.

message: string

Human-readable error description.

type: "session\_creation\_rejected\_error"

BetaManagedAgentsUnknownRunError { message, type }

An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

message: string

Human-readable error description.

type: "unknown\_error"

BetaManagedAgentsSelfHostedResourcesUnsupportedRunError { message, type }

The deployment configures resources, but its environment is self-hosted and cannot mount them.

message: string

Human-readable error description.

type: "self\_hosted\_resources\_unsupported\_error"

BetaManagedAgentsMCPEgressBlockedRunError { message, type }

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

message: string

Human-readable error description.

type: "mcp\_egress\_blocked\_error"

session\_id: string | null

Populated on success. Null on creation failure. Exactly one of session\_id or error is non-null.

trigger\_context: [BetaManagedAgentsTriggerContext](api/beta.md)

Describes what triggered a deployment run, with trigger-specific metadata.

One of the following:

BetaManagedAgentsScheduleTriggerContext { scheduled\_at, type }

The run was fired by the deployment's cron schedule.

scheduled\_at: string

A timestamp in RFC 3339 format

type: "schedule"

BetaManagedAgentsManualTriggerContext { type }

The run was started manually by creating a session directly against the deployment.

type: "manual"

type: "deployment\_run"

BetaManagedAgentsEnvironmentArchivedRunError { message, type }

The deployment's environment was archived.

message: string

Human-readable error description.

type: "environment\_archived\_error"

BetaManagedAgentsEnvironmentNotFoundRunError { message, type }

The deployment's environment no longer exists.

message: string

Human-readable error description.

type: "environment\_not\_found\_error"

BetaManagedAgentsFileNotFoundRunError { message, type }

A file resource referenced by the deployment no longer exists.

message: string

Human-readable error description.

type: "file\_not\_found\_error"

BetaManagedAgentsManualTriggerContext { type }

The run was started manually by creating a session directly against the deployment.

type: "manual"

BetaManagedAgentsMCPEgressBlockedRunError { message, type }

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

message: string

Human-readable error description.

type: "mcp\_egress\_blocked\_error"

BetaManagedAgentsMemoryStoreArchivedRunError { message, type }

A memory store referenced by the deployment is archived.

message: string

Human-readable error description.

type: "memory\_store\_archived\_error"

BetaManagedAgentsOrganizationDisabledRunError { message, type }

The deployment's organization is disabled.

message: string

Human-readable error description.

type: "organization\_disabled\_error"

BetaManagedAgentsScheduleTriggerContext { scheduled\_at, type }

The run was fired by the deployment's cron schedule.

scheduled\_at: string

A timestamp in RFC 3339 format

type: "schedule"

BetaManagedAgentsSelfHostedResourcesUnsupportedRunError { message, type }

The deployment configures resources, but its environment is self-hosted and cannot mount them.

message: string

Human-readable error description.

type: "self\_hosted\_resources\_unsupported\_error"

BetaManagedAgentsSessionCreationRejectedRunError { message, type }

The session create request was rejected with a non-retryable validation error.

message: string

Human-readable error description.

type: "session\_creation\_rejected\_error"

BetaManagedAgentsSessionRateLimitedRunError { message, type }

Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

message: string

Human-readable error description.

type: "session\_rate\_limited\_error"

BetaManagedAgentsSessionResourceNotFoundRunError { message, type }

A referenced resource no longer exists and its kind was not reported.

message: string

Human-readable error description.

type: "session\_resource\_not\_found\_error"

BetaManagedAgentsSkillNotFoundRunError { message, type }

A skill referenced by the deployment's agent no longer exists.

message: string

Human-readable error description.

type: "skill\_not\_found\_error"

BetaManagedAgentsTriggerContext = [BetaManagedAgentsScheduleTriggerContext](api/beta.md) { scheduled\_at, type }  | [BetaManagedAgentsManualTriggerContext](api/beta.md) { type }

Describes what triggered a deployment run, with trigger-specific metadata.

One of the following:

BetaManagedAgentsScheduleTriggerContext { scheduled\_at, type }

The run was fired by the deployment's cron schedule.

scheduled\_at: string

A timestamp in RFC 3339 format

type: "schedule"

BetaManagedAgentsManualTriggerContext { type }

The run was started manually by creating a session directly against the deployment.

type: "manual"

BetaManagedAgentsTriggerType = "schedule" | "manual"

What triggered a deployment run.

One of the following:

"schedule"

"manual"

BetaManagedAgentsUnknownRunError { message, type }

An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

message: string

Human-readable error description.

type: "unknown\_error"

BetaManagedAgentsVaultArchivedRunError { message, type }

A vault referenced by the deployment is archived.

message: string

Human-readable error description.

type: "vault\_archived\_error"

BetaManagedAgentsVaultNotFoundRunError { message, type }

A vault referenced by the deployment no longer exists.

message: string

Human-readable error description.

type: "vault\_not\_found\_error"

BetaManagedAgentsWorkspaceArchivedRunError { message, type }

The deployment's workspace was archived.

message: string

Human-readable error description.

type: "workspace\_archived\_error"

---

*Copyright © Anthropic. All rights reserved.*
