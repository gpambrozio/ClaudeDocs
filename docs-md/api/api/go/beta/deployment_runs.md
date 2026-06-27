# Deployment Runs

Copy page



Go

# Deployment Runs

##### [List Deployment Runs](api/beta/deployment_runs/list.md)

client.Beta.DeploymentRuns.List(ctx, params) (\*PageCursor[[BetaManagedAgentsDeploymentRun](api/beta/deployment_runs.md)], error)

GET/v1/deployment\_runs

##### [Get Deployment Run](api/beta/deployment_runs/retrieve.md)

client.Beta.DeploymentRuns.Get(ctx, deploymentRunID, query) (\*[BetaManagedAgentsDeploymentRun](api/beta/deployment_runs.md), error)

GET/v1/deployment\_runs/{deployment\_run\_id}

##### ModelsExpand Collapse



type BetaManagedAgentsAgentArchivedRunError struct{…}

The deployment's agent was archived.

Message string

Human-readable error description.

Type BetaManagedAgentsAgentArchivedRunErrorType



type BetaManagedAgentsDeploymentRun struct{…}

A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

ID string

Unique identifier for this run (`drun_...`).



Agent [BetaManagedAgentsAgentReference](api/beta/agents.md)

A resolved agent reference with a concrete version.

ID string

Type BetaManagedAgentsAgentReferenceType

Version int64

CreatedAt Time

A timestamp in RFC 3339 format

DeploymentID string

ID of the deployment that produced this run.



Error BetaManagedAgentsDeploymentRunErrorUnion

Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

One of the following:



type BetaManagedAgentsEnvironmentArchivedRunError struct{…}

The deployment's environment was archived.

Message string

Human-readable error description.

Type BetaManagedAgentsEnvironmentArchivedRunErrorType



type BetaManagedAgentsAgentArchivedRunError struct{…}

The deployment's agent was archived.

Message string

Human-readable error description.

Type BetaManagedAgentsAgentArchivedRunErrorType



type BetaManagedAgentsEnvironmentNotFoundRunError struct{…}

The deployment's environment no longer exists.

Message string

Human-readable error description.

Type BetaManagedAgentsEnvironmentNotFoundRunErrorType



type BetaManagedAgentsVaultNotFoundRunError struct{…}

A vault referenced by the deployment no longer exists.

Message string

Human-readable error description.

Type BetaManagedAgentsVaultNotFoundRunErrorType



type BetaManagedAgentsVaultArchivedRunError struct{…}

A vault referenced by the deployment is archived.

Message string

Human-readable error description.

Type BetaManagedAgentsVaultArchivedRunErrorType



type BetaManagedAgentsFileNotFoundRunError struct{…}

A file resource referenced by the deployment no longer exists.

Message string

Human-readable error description.

Type BetaManagedAgentsFileNotFoundRunErrorType



type BetaManagedAgentsMemoryStoreArchivedRunError struct{…}

A memory store referenced by the deployment is archived.

Message string

Human-readable error description.

Type BetaManagedAgentsMemoryStoreArchivedRunErrorType



type BetaManagedAgentsSkillNotFoundRunError struct{…}

A skill referenced by the deployment's agent no longer exists.

Message string

Human-readable error description.

Type BetaManagedAgentsSkillNotFoundRunErrorType



type BetaManagedAgentsSessionResourceNotFoundRunError struct{…}

A referenced resource no longer exists and its kind was not reported.

Message string

Human-readable error description.

Type BetaManagedAgentsSessionResourceNotFoundRunErrorType



type BetaManagedAgentsWorkspaceArchivedRunError struct{…}

The deployment's workspace was archived.

Message string

Human-readable error description.

Type BetaManagedAgentsWorkspaceArchivedRunErrorType



type BetaManagedAgentsOrganizationDisabledRunError struct{…}

The deployment's organization is disabled.

Message string

Human-readable error description.

Type BetaManagedAgentsOrganizationDisabledRunErrorType



type BetaManagedAgentsSessionRateLimitedRunError struct{…}

Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

Message string

Human-readable error description.

Type BetaManagedAgentsSessionRateLimitedRunErrorType



type BetaManagedAgentsSessionCreationRejectedRunError struct{…}

The session create request was rejected with a non-retryable validation error.

Message string

Human-readable error description.

Type BetaManagedAgentsSessionCreationRejectedRunErrorType



type BetaManagedAgentsUnknownRunError struct{…}

An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

Message string

Human-readable error description.

Type BetaManagedAgentsUnknownRunErrorType



type BetaManagedAgentsSelfHostedResourcesUnsupportedRunError struct{…}

The deployment configures resources, but its environment is self-hosted and cannot mount them.

Message string

Human-readable error description.

Type BetaManagedAgentsSelfHostedResourcesUnsupportedRunErrorType



type BetaManagedAgentsMCPEgressBlockedRunError struct{…}

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

Message string

Human-readable error description.

Type BetaManagedAgentsMCPEgressBlockedRunErrorType

SessionID string

Populated on success. Null on creation failure. Exactly one of session\_id or error is non-null.



TriggerContext [BetaManagedAgentsTriggerContextUnion](api/beta/deployment_runs.md)

Describes what triggered a deployment run, with trigger-specific metadata.

One of the following:



type BetaManagedAgentsScheduleTriggerContext struct{…}

The run was fired by the deployment's cron schedule.

ScheduledAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsScheduleTriggerContextType



type BetaManagedAgentsManualTriggerContext struct{…}

The run was started manually by creating a session directly against the deployment.

Type BetaManagedAgentsManualTriggerContextType

Type BetaManagedAgentsDeploymentRunType



type BetaManagedAgentsEnvironmentArchivedRunError struct{…}

The deployment's environment was archived.

Message string

Human-readable error description.

Type BetaManagedAgentsEnvironmentArchivedRunErrorType



type BetaManagedAgentsEnvironmentNotFoundRunError struct{…}

The deployment's environment no longer exists.

Message string

Human-readable error description.

Type BetaManagedAgentsEnvironmentNotFoundRunErrorType



type BetaManagedAgentsFileNotFoundRunError struct{…}

A file resource referenced by the deployment no longer exists.

Message string

Human-readable error description.

Type BetaManagedAgentsFileNotFoundRunErrorType



type BetaManagedAgentsManualTriggerContext struct{…}

The run was started manually by creating a session directly against the deployment.

Type BetaManagedAgentsManualTriggerContextType



type BetaManagedAgentsMCPEgressBlockedRunError struct{…}

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

Message string

Human-readable error description.

Type BetaManagedAgentsMCPEgressBlockedRunErrorType



type BetaManagedAgentsMemoryStoreArchivedRunError struct{…}

A memory store referenced by the deployment is archived.

Message string

Human-readable error description.

Type BetaManagedAgentsMemoryStoreArchivedRunErrorType



type BetaManagedAgentsOrganizationDisabledRunError struct{…}

The deployment's organization is disabled.

Message string

Human-readable error description.

Type BetaManagedAgentsOrganizationDisabledRunErrorType



type BetaManagedAgentsScheduleTriggerContext struct{…}

The run was fired by the deployment's cron schedule.

ScheduledAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsScheduleTriggerContextType



type BetaManagedAgentsSelfHostedResourcesUnsupportedRunError struct{…}

The deployment configures resources, but its environment is self-hosted and cannot mount them.

Message string

Human-readable error description.

Type BetaManagedAgentsSelfHostedResourcesUnsupportedRunErrorType



type BetaManagedAgentsSessionCreationRejectedRunError struct{…}

The session create request was rejected with a non-retryable validation error.

Message string

Human-readable error description.

Type BetaManagedAgentsSessionCreationRejectedRunErrorType



type BetaManagedAgentsSessionRateLimitedRunError struct{…}

Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

Message string

Human-readable error description.

Type BetaManagedAgentsSessionRateLimitedRunErrorType



type BetaManagedAgentsSessionResourceNotFoundRunError struct{…}

A referenced resource no longer exists and its kind was not reported.

Message string

Human-readable error description.

Type BetaManagedAgentsSessionResourceNotFoundRunErrorType



type BetaManagedAgentsSkillNotFoundRunError struct{…}

A skill referenced by the deployment's agent no longer exists.

Message string

Human-readable error description.

Type BetaManagedAgentsSkillNotFoundRunErrorType



type BetaManagedAgentsTriggerContextUnion interface{…}

Describes what triggered a deployment run, with trigger-specific metadata.

One of the following:



type BetaManagedAgentsScheduleTriggerContext struct{…}

The run was fired by the deployment's cron schedule.

ScheduledAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsScheduleTriggerContextType



type BetaManagedAgentsManualTriggerContext struct{…}

The run was started manually by creating a session directly against the deployment.

Type BetaManagedAgentsManualTriggerContextType



type BetaManagedAgentsTriggerType string

What triggered a deployment run.

One of the following:

const BetaManagedAgentsTriggerTypeSchedule [BetaManagedAgentsTriggerType](api/beta/deployment_runs.md) = "schedule"

const BetaManagedAgentsTriggerTypeManual [BetaManagedAgentsTriggerType](api/beta/deployment_runs.md) = "manual"



type BetaManagedAgentsUnknownRunError struct{…}

An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

Message string

Human-readable error description.

Type BetaManagedAgentsUnknownRunErrorType



type BetaManagedAgentsVaultArchivedRunError struct{…}

A vault referenced by the deployment is archived.

Message string

Human-readable error description.

Type BetaManagedAgentsVaultArchivedRunErrorType



type BetaManagedAgentsVaultNotFoundRunError struct{…}

A vault referenced by the deployment no longer exists.

Message string

Human-readable error description.

Type BetaManagedAgentsVaultNotFoundRunErrorType



type BetaManagedAgentsWorkspaceArchivedRunError struct{…}

The deployment's workspace was archived.

Message string

Human-readable error description.

Type BetaManagedAgentsWorkspaceArchivedRunErrorType

---

*Copyright © Anthropic. All rights reserved.*
