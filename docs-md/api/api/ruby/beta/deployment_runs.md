# Deployment Runs

Copy page

SDK language

Ruby

# Deployment Runs

##### [List Deployment Runs](api/beta/deployment_runs/list.md)

beta.deployment\_runs.list(\*\*kwargs) -> PageCursor<[BetaManagedAgentsDeploymentRun](api/beta.md) { id, agent, created\_at, 5 more } >

GET/v1/deployment\_runs

##### [Get Deployment Run](api/beta/deployment_runs/retrieve.md)

beta.deployment\_runs.retrieve(deployment\_run\_id, \*\*kwargs) -> [BetaManagedAgentsDeploymentRun](api/beta.md) { id, agent, created\_at, 5 more }

GET/v1/deployment\_runs/{deployment\_run\_id}

##### ModelsExpand Collapse

class BetaManagedAgentsAgentArchivedRunError { message, type }

The deployment's agent was archived.

message: String

Human-readable error description.

type: :agent\_archived\_error

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

class BetaManagedAgentsEnvironmentArchivedRunError { message, type }

The deployment's environment was archived.

message: String

Human-readable error description.

type: :environment\_archived\_error

class BetaManagedAgentsEnvironmentNotFoundRunError { message, type }

The deployment's environment no longer exists.

message: String

Human-readable error description.

type: :environment\_not\_found\_error

class BetaManagedAgentsFileNotFoundRunError { message, type }

A file resource referenced by the deployment no longer exists.

message: String

Human-readable error description.

type: :file\_not\_found\_error

class BetaManagedAgentsManualTriggerContext { type }

The run was started manually by creating a session directly against the deployment.

type: :manual

class BetaManagedAgentsMCPEgressBlockedRunError { message, type }

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

message: String

Human-readable error description.

type: :mcp\_egress\_blocked\_error

class BetaManagedAgentsMemoryStoreArchivedRunError { message, type }

A memory store referenced by the deployment is archived.

message: String

Human-readable error description.

type: :memory\_store\_archived\_error

class BetaManagedAgentsOrganizationDisabledRunError { message, type }

The deployment's organization is disabled.

message: String

Human-readable error description.

type: :organization\_disabled\_error

class BetaManagedAgentsScheduleTriggerContext { scheduled\_at, type }

The run was fired by the deployment's cron schedule.

scheduled\_at: Time

A timestamp in RFC 3339 format

type: :schedule

class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError { message, type }

The deployment configures resources, but its environment is self-hosted and cannot mount them.

message: String

Human-readable error description.

type: :self\_hosted\_resources\_unsupported\_error

class BetaManagedAgentsSessionCreationRejectedRunError { message, type }

The session create request was rejected with a non-retryable validation error.

message: String

Human-readable error description.

type: :session\_creation\_rejected\_error

class BetaManagedAgentsSessionRateLimitedRunError { message, type }

Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

message: String

Human-readable error description.

type: :session\_rate\_limited\_error

class BetaManagedAgentsSessionResourceNotFoundRunError { message, type }

A referenced resource no longer exists and its kind was not reported.

message: String

Human-readable error description.

type: :session\_resource\_not\_found\_error

class BetaManagedAgentsSkillNotFoundRunError { message, type }

A skill referenced by the deployment's agent no longer exists.

message: String

Human-readable error description.

type: :skill\_not\_found\_error

BetaManagedAgentsTriggerContext = [BetaManagedAgentsScheduleTriggerContext](api/beta.md) { scheduled\_at, type }  | [BetaManagedAgentsManualTriggerContext](api/beta.md) { type }

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

BetaManagedAgentsTriggerType = :schedule | :manual

What triggered a deployment run.

One of the following:

:schedule

:manual

class BetaManagedAgentsUnknownRunError { message, type }

An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

message: String

Human-readable error description.

type: :unknown\_error

class BetaManagedAgentsVaultArchivedRunError { message, type }

A vault referenced by the deployment is archived.

message: String

Human-readable error description.

type: :vault\_archived\_error

class BetaManagedAgentsVaultNotFoundRunError { message, type }

A vault referenced by the deployment no longer exists.

message: String

Human-readable error description.

type: :vault\_not\_found\_error

class BetaManagedAgentsWorkspaceArchivedRunError { message, type }

The deployment's workspace was archived.

message: String

Human-readable error description.

type: :workspace\_archived\_error

---

*Copyright © Anthropic. All rights reserved.*
