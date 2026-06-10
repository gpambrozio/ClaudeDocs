# Deployment Runs

Copy page

SDK language

C#

# Deployment Runs

##### [List Deployment Runs](api/beta/deployment_runs/list.md)

[DeploymentRunListPageResponse](api/beta.md) Beta.DeploymentRuns.List(DeploymentRunListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/deployment\_runs

##### [Get Deployment Run](api/beta/deployment_runs/retrieve.md)

[BetaManagedAgentsDeploymentRun](api/beta.md) Beta.DeploymentRuns.Retrieve(DeploymentRunRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/deployment\_runs/{deployment\_run\_id}

##### ModelsExpand Collapse

class BetaManagedAgentsAgentArchivedRunError:

The deployment's agent was archived.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsDeploymentRun:

A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

required string ID

Unique identifier for this run (`drun_...`).

required [BetaManagedAgentsAgentReference](api/beta.md) Agent

A resolved agent reference with a concrete version.

required string ID

required Type Type

required Int Version

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string DeploymentID

ID of the deployment that produced this run.

required Error? Error

Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

One of the following:

class BetaManagedAgentsEnvironmentArchivedRunError:

The deployment's environment was archived.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsAgentArchivedRunError:

The deployment's agent was archived.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsEnvironmentNotFoundRunError:

The deployment's environment no longer exists.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsVaultNotFoundRunError:

A vault referenced by the deployment no longer exists.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsVaultArchivedRunError:

A vault referenced by the deployment is archived.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsFileNotFoundRunError:

A file resource referenced by the deployment no longer exists.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsMemoryStoreArchivedRunError:

A memory store referenced by the deployment is archived.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsSkillNotFoundRunError:

A skill referenced by the deployment's agent no longer exists.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsSessionResourceNotFoundRunError:

A referenced resource no longer exists and its kind was not reported.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsWorkspaceArchivedRunError:

The deployment's workspace was archived.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsOrganizationDisabledRunError:

The deployment's organization is disabled.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsSessionRateLimitedRunError:

Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsSessionCreationRejectedRunError:

The session create request was rejected with a non-retryable validation error.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsUnknownRunError:

An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError:

The deployment configures resources, but its environment is self-hosted and cannot mount them.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsMcpEgressBlockedRunError:

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

required string Message

Human-readable error description.

required Type Type

required string? SessionID

Populated on success. Null on creation failure. Exactly one of session\_id or error is non-null.

required [BetaManagedAgentsTriggerContext](api/beta.md) TriggerContext

Describes what triggered a deployment run, with trigger-specific metadata.

One of the following:

class BetaManagedAgentsScheduleTriggerContext:

The run was fired by the deployment's cron schedule.

required DateTimeOffset ScheduledAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsManualTriggerContext:

The run was started manually by creating a session directly against the deployment.

required Type Type

required Type Type

class BetaManagedAgentsEnvironmentArchivedRunError:

The deployment's environment was archived.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsEnvironmentNotFoundRunError:

The deployment's environment no longer exists.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsFileNotFoundRunError:

A file resource referenced by the deployment no longer exists.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsManualTriggerContext:

The run was started manually by creating a session directly against the deployment.

required Type Type

class BetaManagedAgentsMcpEgressBlockedRunError:

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsMemoryStoreArchivedRunError:

A memory store referenced by the deployment is archived.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsOrganizationDisabledRunError:

The deployment's organization is disabled.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsScheduleTriggerContext:

The run was fired by the deployment's cron schedule.

required DateTimeOffset ScheduledAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError:

The deployment configures resources, but its environment is self-hosted and cannot mount them.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsSessionCreationRejectedRunError:

The session create request was rejected with a non-retryable validation error.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsSessionRateLimitedRunError:

Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsSessionResourceNotFoundRunError:

A referenced resource no longer exists and its kind was not reported.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsSkillNotFoundRunError:

A skill referenced by the deployment's agent no longer exists.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsTriggerContext: A class that can be one of several variants.union

Describes what triggered a deployment run, with trigger-specific metadata.

class BetaManagedAgentsScheduleTriggerContext:

The run was fired by the deployment's cron schedule.

required DateTimeOffset ScheduledAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsManualTriggerContext:

The run was started manually by creating a session directly against the deployment.

required Type Type

enum BetaManagedAgentsTriggerType:

What triggered a deployment run.

"schedule"Schedule

"manual"Manual

class BetaManagedAgentsUnknownRunError:

An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsVaultArchivedRunError:

A vault referenced by the deployment is archived.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsVaultNotFoundRunError:

A vault referenced by the deployment no longer exists.

required string Message

Human-readable error description.

required Type Type

class BetaManagedAgentsWorkspaceArchivedRunError:

The deployment's workspace was archived.

required string Message

Human-readable error description.

required Type Type

---

*Copyright © Anthropic. All rights reserved.*
