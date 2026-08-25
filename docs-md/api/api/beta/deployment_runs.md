# Deployment Runs

Copy page



cURL

# Deployment Runs

##### [List Deployment Runs](api/http/beta/deployment_runs/list.md)

GET/v1/deployment\_runs

##### [Get Deployment Run](api/http/beta/deployment_runs/retrieve.md)

GET/v1/deployment\_runs/{deployment\_run\_id}

##### Models



BetaManagedAgentsAgentArchivedRunError object{ message, type }

The deployment's agent was archived.

message: string

Human-readable error description.

type: "agent\_archived\_error"



BetaManagedAgentsDeploymentRun object{ id, agent, created\_at, 5 more }

A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.



BetaManagedAgentsEnvironmentArchivedRunError object{ message, type }

The deployment's environment was archived.

message: string

Human-readable error description.

type: "environment\_archived\_error"



BetaManagedAgentsEnvironmentNotFoundRunError object{ message, type }

The deployment's environment no longer exists.

message: string

Human-readable error description.

type: "environment\_not\_found\_error"



BetaManagedAgentsFileNotFoundRunError object{ message, type }

A file resource referenced by the deployment no longer exists.

message: string

Human-readable error description.

type: "file\_not\_found\_error"



BetaManagedAgentsManualTriggerContext object{ type }

The run was started manually by creating a session directly against the deployment.

type: "manual"



BetaManagedAgentsMCPEgressBlockedRunError object{ message, type }

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

message: string

Human-readable error description.

type: "mcp\_egress\_blocked\_error"



BetaManagedAgentsMemoryStoreArchivedRunError object{ message, type }

A memory store referenced by the deployment is archived.

message: string

Human-readable error description.

type: "memory\_store\_archived\_error"



BetaManagedAgentsOrganizationDisabledRunError object{ message, type }

The deployment's organization is disabled.

message: string

Human-readable error description.

type: "organization\_disabled\_error"



BetaManagedAgentsScheduleTriggerContext object{ scheduled\_at, type }

The run was fired by the deployment's cron schedule.



scheduled\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "schedule"



BetaManagedAgentsSelfHostedResourcesUnsupportedRunError object{ message, type }

The deployment configures resources, but its environment is self-hosted and cannot mount them.

message: string

Human-readable error description.

type: "self\_hosted\_resources\_unsupported\_error"



BetaManagedAgentsSessionCreationRejectedRunError object{ message, type }

The session create request was rejected with a non-retryable validation error.

message: string

Human-readable error description.

type: "session\_creation\_rejected\_error"



BetaManagedAgentsSessionRateLimitedRunError object{ message, type }

Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

message: string

Human-readable error description.

type: "session\_rate\_limited\_error"



BetaManagedAgentsSessionResourceNotFoundRunError object{ message, type }

A referenced resource no longer exists and its kind was not reported.

message: string

Human-readable error description.

type: "session\_resource\_not\_found\_error"



BetaManagedAgentsSkillNotFoundRunError object{ message, type }

A skill referenced by the deployment's agent no longer exists.

message: string

Human-readable error description.

type: "skill\_not\_found\_error"



BetaManagedAgentsTriggerContext = [BetaManagedAgentsScheduleTriggerContext](api/http/beta/deployment_runs.md) { scheduled\_at, type } or [BetaManagedAgentsManualTriggerContext](api/http/beta/deployment_runs.md) { type }

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



BetaManagedAgentsTriggerType = "schedule" or "manual"

What triggered a deployment run.

One of the following:

"schedule"

"manual"



BetaManagedAgentsUnknownRunError object{ message, type }

An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

message: string

Human-readable error description.

type: "unknown\_error"



BetaManagedAgentsVaultArchivedRunError object{ message, type }

A vault referenced by the deployment is archived.

message: string

Human-readable error description.

type: "vault\_archived\_error"



BetaManagedAgentsVaultNotFoundRunError object{ message, type }

A vault referenced by the deployment no longer exists.

message: string

Human-readable error description.

type: "vault\_not\_found\_error"



BetaManagedAgentsWorkspaceArchivedRunError object{ message, type }

The deployment's workspace was archived.

message: string

Human-readable error description.

type: "workspace\_archived\_error"

---

*Copyright © Anthropic. All rights reserved.*
