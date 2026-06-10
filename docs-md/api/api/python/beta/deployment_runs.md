# Deployment Runs

Copy page

SDK language

Python

# Deployment Runs

##### [List Deployment Runs](api/beta/deployment_runs/list.md)

beta.deployment\_runs.list(DeploymentRunListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsDeploymentRun](api/beta.md)]

GET/v1/deployment\_runs

##### [Get Deployment Run](api/beta/deployment_runs/retrieve.md)

beta.deployment\_runs.retrieve(strdeployment\_run\_id, DeploymentRunRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsDeploymentRun](api/beta.md)

GET/v1/deployment\_runs/{deployment\_run\_id}

##### ModelsExpand Collapse

class BetaManagedAgentsAgentArchivedRunError: …

The deployment's agent was archived.

message: str

Human-readable error description.

type: Literal["agent\_archived\_error"]

class BetaManagedAgentsDeploymentRun: …

A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

id: str

Unique identifier for this run (`drun_...`).

agent: [BetaManagedAgentsAgentReference](api/beta.md)

A resolved agent reference with a concrete version.

id: str

type: Literal["agent"]

version: int

created\_at: datetime

A timestamp in RFC 3339 format

deployment\_id: str

ID of the deployment that produced this run.

error: Optional[Error]

Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

One of the following:

class BetaManagedAgentsEnvironmentArchivedRunError: …

The deployment's environment was archived.

message: str

Human-readable error description.

type: Literal["environment\_archived\_error"]

class BetaManagedAgentsAgentArchivedRunError: …

The deployment's agent was archived.

message: str

Human-readable error description.

type: Literal["agent\_archived\_error"]

class BetaManagedAgentsEnvironmentNotFoundRunError: …

The deployment's environment no longer exists.

message: str

Human-readable error description.

type: Literal["environment\_not\_found\_error"]

class BetaManagedAgentsVaultNotFoundRunError: …

A vault referenced by the deployment no longer exists.

message: str

Human-readable error description.

type: Literal["vault\_not\_found\_error"]

class BetaManagedAgentsVaultArchivedRunError: …

A vault referenced by the deployment is archived.

message: str

Human-readable error description.

type: Literal["vault\_archived\_error"]

class BetaManagedAgentsFileNotFoundRunError: …

A file resource referenced by the deployment no longer exists.

message: str

Human-readable error description.

type: Literal["file\_not\_found\_error"]

class BetaManagedAgentsMemoryStoreArchivedRunError: …

A memory store referenced by the deployment is archived.

message: str

Human-readable error description.

type: Literal["memory\_store\_archived\_error"]

class BetaManagedAgentsSkillNotFoundRunError: …

A skill referenced by the deployment's agent no longer exists.

message: str

Human-readable error description.

type: Literal["skill\_not\_found\_error"]

class BetaManagedAgentsSessionResourceNotFoundRunError: …

A referenced resource no longer exists and its kind was not reported.

message: str

Human-readable error description.

type: Literal["session\_resource\_not\_found\_error"]

class BetaManagedAgentsWorkspaceArchivedRunError: …

The deployment's workspace was archived.

message: str

Human-readable error description.

type: Literal["workspace\_archived\_error"]

class BetaManagedAgentsOrganizationDisabledRunError: …

The deployment's organization is disabled.

message: str

Human-readable error description.

type: Literal["organization\_disabled\_error"]

class BetaManagedAgentsSessionRateLimitedRunError: …

Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

message: str

Human-readable error description.

type: Literal["session\_rate\_limited\_error"]

class BetaManagedAgentsSessionCreationRejectedRunError: …

The session create request was rejected with a non-retryable validation error.

message: str

Human-readable error description.

type: Literal["session\_creation\_rejected\_error"]

class BetaManagedAgentsUnknownRunError: …

An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

message: str

Human-readable error description.

type: Literal["unknown\_error"]

class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError: …

The deployment configures resources, but its environment is self-hosted and cannot mount them.

message: str

Human-readable error description.

type: Literal["self\_hosted\_resources\_unsupported\_error"]

class BetaManagedAgentsMCPEgressBlockedRunError: …

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

message: str

Human-readable error description.

type: Literal["mcp\_egress\_blocked\_error"]

session\_id: Optional[str]

Populated on success. Null on creation failure. Exactly one of session\_id or error is non-null.

trigger\_context: [BetaManagedAgentsTriggerContext](api/beta.md)

Describes what triggered a deployment run, with trigger-specific metadata.

One of the following:

class BetaManagedAgentsScheduleTriggerContext: …

The run was fired by the deployment's cron schedule.

scheduled\_at: datetime

A timestamp in RFC 3339 format

type: Literal["schedule"]

class BetaManagedAgentsManualTriggerContext: …

The run was started manually by creating a session directly against the deployment.

type: Literal["manual"]

type: Literal["deployment\_run"]

class BetaManagedAgentsEnvironmentArchivedRunError: …

The deployment's environment was archived.

message: str

Human-readable error description.

type: Literal["environment\_archived\_error"]

class BetaManagedAgentsEnvironmentNotFoundRunError: …

The deployment's environment no longer exists.

message: str

Human-readable error description.

type: Literal["environment\_not\_found\_error"]

class BetaManagedAgentsFileNotFoundRunError: …

A file resource referenced by the deployment no longer exists.

message: str

Human-readable error description.

type: Literal["file\_not\_found\_error"]

class BetaManagedAgentsManualTriggerContext: …

The run was started manually by creating a session directly against the deployment.

type: Literal["manual"]

class BetaManagedAgentsMCPEgressBlockedRunError: …

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

message: str

Human-readable error description.

type: Literal["mcp\_egress\_blocked\_error"]

class BetaManagedAgentsMemoryStoreArchivedRunError: …

A memory store referenced by the deployment is archived.

message: str

Human-readable error description.

type: Literal["memory\_store\_archived\_error"]

class BetaManagedAgentsOrganizationDisabledRunError: …

The deployment's organization is disabled.

message: str

Human-readable error description.

type: Literal["organization\_disabled\_error"]

class BetaManagedAgentsScheduleTriggerContext: …

The run was fired by the deployment's cron schedule.

scheduled\_at: datetime

A timestamp in RFC 3339 format

type: Literal["schedule"]

class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError: …

The deployment configures resources, but its environment is self-hosted and cannot mount them.

message: str

Human-readable error description.

type: Literal["self\_hosted\_resources\_unsupported\_error"]

class BetaManagedAgentsSessionCreationRejectedRunError: …

The session create request was rejected with a non-retryable validation error.

message: str

Human-readable error description.

type: Literal["session\_creation\_rejected\_error"]

class BetaManagedAgentsSessionRateLimitedRunError: …

Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

message: str

Human-readable error description.

type: Literal["session\_rate\_limited\_error"]

class BetaManagedAgentsSessionResourceNotFoundRunError: …

A referenced resource no longer exists and its kind was not reported.

message: str

Human-readable error description.

type: Literal["session\_resource\_not\_found\_error"]

class BetaManagedAgentsSkillNotFoundRunError: …

A skill referenced by the deployment's agent no longer exists.

message: str

Human-readable error description.

type: Literal["skill\_not\_found\_error"]

[BetaManagedAgentsTriggerContext](api/beta.md)

Describes what triggered a deployment run, with trigger-specific metadata.

One of the following:

class BetaManagedAgentsScheduleTriggerContext: …

The run was fired by the deployment's cron schedule.

scheduled\_at: datetime

A timestamp in RFC 3339 format

type: Literal["schedule"]

class BetaManagedAgentsManualTriggerContext: …

The run was started manually by creating a session directly against the deployment.

type: Literal["manual"]

Literal["schedule", "manual"]

What triggered a deployment run.

One of the following:

"schedule"

"manual"

class BetaManagedAgentsUnknownRunError: …

An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

message: str

Human-readable error description.

type: Literal["unknown\_error"]

class BetaManagedAgentsVaultArchivedRunError: …

A vault referenced by the deployment is archived.

message: str

Human-readable error description.

type: Literal["vault\_archived\_error"]

class BetaManagedAgentsVaultNotFoundRunError: …

A vault referenced by the deployment no longer exists.

message: str

Human-readable error description.

type: Literal["vault\_not\_found\_error"]

class BetaManagedAgentsWorkspaceArchivedRunError: …

The deployment's workspace was archived.

message: str

Human-readable error description.

type: Literal["workspace\_archived\_error"]

---

*Copyright © Anthropic. All rights reserved.*
