# Deployment Runs

Copy page

SDK language

Java

# Deployment Runs

##### [List Deployment Runs](api/beta/deployment_runs/list.md)

DeploymentRunListPage beta().deploymentRuns().list(DeploymentRunListParamsparams = DeploymentRunListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/deployment\_runs

##### [Get Deployment Run](api/beta/deployment_runs/retrieve.md)

[BetaManagedAgentsDeploymentRun](api/beta.md) beta().deploymentRuns().retrieve(DeploymentRunRetrieveParamsparams = DeploymentRunRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/deployment\_runs/{deployment\_run\_id}

##### ModelsExpand Collapse



class BetaManagedAgentsAgentArchivedRunError:

The deployment's agent was archived.

String message

Human-readable error description.

Type type



class BetaManagedAgentsDeploymentRun:

A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

String id

Unique identifier for this run (`drun_...`).



[BetaManagedAgentsAgentReference](api/beta.md) agent

A resolved agent reference with a concrete version.

String id

Type type

long version

LocalDateTime createdAt

A timestamp in RFC 3339 format

String deploymentId

ID of the deployment that produced this run.



Optional<Error> error

Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

One of the following:



class BetaManagedAgentsEnvironmentArchivedRunError:

The deployment's environment was archived.

String message

Human-readable error description.

Type type



class BetaManagedAgentsAgentArchivedRunError:

The deployment's agent was archived.

String message

Human-readable error description.

Type type



class BetaManagedAgentsEnvironmentNotFoundRunError:

The deployment's environment no longer exists.

String message

Human-readable error description.

Type type



class BetaManagedAgentsVaultNotFoundRunError:

A vault referenced by the deployment no longer exists.

String message

Human-readable error description.

Type type



class BetaManagedAgentsVaultArchivedRunError:

A vault referenced by the deployment is archived.

String message

Human-readable error description.

Type type



class BetaManagedAgentsFileNotFoundRunError:

A file resource referenced by the deployment no longer exists.

String message

Human-readable error description.

Type type



class BetaManagedAgentsMemoryStoreArchivedRunError:

A memory store referenced by the deployment is archived.

String message

Human-readable error description.

Type type



class BetaManagedAgentsSkillNotFoundRunError:

A skill referenced by the deployment's agent no longer exists.

String message

Human-readable error description.

Type type



class BetaManagedAgentsSessionResourceNotFoundRunError:

A referenced resource no longer exists and its kind was not reported.

String message

Human-readable error description.

Type type



class BetaManagedAgentsWorkspaceArchivedRunError:

The deployment's workspace was archived.

String message

Human-readable error description.

Type type



class BetaManagedAgentsOrganizationDisabledRunError:

The deployment's organization is disabled.

String message

Human-readable error description.

Type type



class BetaManagedAgentsSessionRateLimitedRunError:

Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

String message

Human-readable error description.

Type type



class BetaManagedAgentsSessionCreationRejectedRunError:

The session create request was rejected with a non-retryable validation error.

String message

Human-readable error description.

Type type



class BetaManagedAgentsUnknownRunError:

An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

String message

Human-readable error description.

Type type



class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError:

The deployment configures resources, but its environment is self-hosted and cannot mount them.

String message

Human-readable error description.

Type type



class BetaManagedAgentsMcpEgressBlockedRunError:

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

String message

Human-readable error description.

Type type

Optional<String> sessionId

Populated on success. Null on creation failure. Exactly one of session\_id or error is non-null.



[BetaManagedAgentsTriggerContext](api/beta.md) triggerContext

Describes what triggered a deployment run, with trigger-specific metadata.

One of the following:



class BetaManagedAgentsScheduleTriggerContext:

The run was fired by the deployment's cron schedule.

LocalDateTime scheduledAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsManualTriggerContext:

The run was started manually by creating a session directly against the deployment.

Type type

Type type



class BetaManagedAgentsEnvironmentArchivedRunError:

The deployment's environment was archived.

String message

Human-readable error description.

Type type



class BetaManagedAgentsEnvironmentNotFoundRunError:

The deployment's environment no longer exists.

String message

Human-readable error description.

Type type



class BetaManagedAgentsFileNotFoundRunError:

A file resource referenced by the deployment no longer exists.

String message

Human-readable error description.

Type type



class BetaManagedAgentsManualTriggerContext:

The run was started manually by creating a session directly against the deployment.

Type type



class BetaManagedAgentsMcpEgressBlockedRunError:

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

String message

Human-readable error description.

Type type



class BetaManagedAgentsMemoryStoreArchivedRunError:

A memory store referenced by the deployment is archived.

String message

Human-readable error description.

Type type



class BetaManagedAgentsOrganizationDisabledRunError:

The deployment's organization is disabled.

String message

Human-readable error description.

Type type



class BetaManagedAgentsScheduleTriggerContext:

The run was fired by the deployment's cron schedule.

LocalDateTime scheduledAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError:

The deployment configures resources, but its environment is self-hosted and cannot mount them.

String message

Human-readable error description.

Type type



class BetaManagedAgentsSessionCreationRejectedRunError:

The session create request was rejected with a non-retryable validation error.

String message

Human-readable error description.

Type type



class BetaManagedAgentsSessionRateLimitedRunError:

Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

String message

Human-readable error description.

Type type



class BetaManagedAgentsSessionResourceNotFoundRunError:

A referenced resource no longer exists and its kind was not reported.

String message

Human-readable error description.

Type type



class BetaManagedAgentsSkillNotFoundRunError:

A skill referenced by the deployment's agent no longer exists.

String message

Human-readable error description.

Type type



class BetaManagedAgentsTriggerContext: A class that can be one of several variants.union 

Describes what triggered a deployment run, with trigger-specific metadata.



class BetaManagedAgentsScheduleTriggerContext:

The run was fired by the deployment's cron schedule.

LocalDateTime scheduledAt

A timestamp in RFC 3339 format

Type type



class BetaManagedAgentsManualTriggerContext:

The run was started manually by creating a session directly against the deployment.

Type type



enum BetaManagedAgentsTriggerType:

What triggered a deployment run.

SCHEDULE("schedule")

MANUAL("manual")



class BetaManagedAgentsUnknownRunError:

An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

String message

Human-readable error description.

Type type



class BetaManagedAgentsVaultArchivedRunError:

A vault referenced by the deployment is archived.

String message

Human-readable error description.

Type type



class BetaManagedAgentsVaultNotFoundRunError:

A vault referenced by the deployment no longer exists.

String message

Human-readable error description.

Type type



class BetaManagedAgentsWorkspaceArchivedRunError:

The deployment's workspace was archived.

String message

Human-readable error description.

Type type

---

*Copyright © Anthropic. All rights reserved.*
