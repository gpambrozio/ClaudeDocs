# Deployment Runs

Copy page

SDK language

PHP

# Deployment Runs

##### [List Deployment Runs](api/beta/deployment_runs/list.md)

$client->beta->deploymentRuns->list(?\Datetime createdAtGt, ?\Datetime createdAtGte, ?\Datetime createdAtLt, ?\Datetime createdAtLte, ?string deploymentID, ?bool hasError, ?int limit, ?string page, ?[BetaManagedAgentsTriggerType](api/beta.md) triggerType, ?list<AnthropicBeta> betas): PageCursor<[BetaManagedAgentsDeploymentRun](api/beta.md)>

GET/v1/deployment\_runs

##### [Get Deployment Run](api/beta/deployment_runs/retrieve.md)

$client->beta->deploymentRuns->retrieve(string deploymentRunID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeploymentRun](api/beta.md)

GET/v1/deployment\_runs/{deployment\_run\_id}

##### ModelsExpand Collapse

[BetaManagedAgentsAgentArchivedRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsDeploymentRun](api/beta.md)

string id

Unique identifier for this run (`drun_...`).

[BetaManagedAgentsAgentReference](api/beta.md) agent

A resolved agent reference with a concrete version.

\Datetime createdAt

A timestamp in RFC 3339 format

string deploymentID

ID of the deployment that produced this run.

?Error error

Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

?string sessionID

Populated on success. Null on creation failure. Exactly one of session\_id or error is non-null.

[BetaManagedAgentsTriggerContext](api/beta.md) triggerContext

Describes what triggered a deployment run, with trigger-specific metadata.

Type type

[BetaManagedAgentsEnvironmentArchivedRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsEnvironmentNotFoundRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsFileNotFoundRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsManualTriggerContext](api/beta.md)

Type type

[BetaManagedAgentsMCPEgressBlockedRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsMemoryStoreArchivedRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsOrganizationDisabledRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsScheduleTriggerContext](api/beta.md)

\Datetime scheduledAt

A timestamp in RFC 3339 format

Type type

[BetaManagedAgentsSelfHostedResourcesUnsupportedRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsSessionCreationRejectedRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsSessionRateLimitedRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsSessionResourceNotFoundRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsSkillNotFoundRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsTriggerContext](api/beta.md)

One of the following:

[BetaManagedAgentsScheduleTriggerContext](api/beta.md)

\Datetime scheduledAt

A timestamp in RFC 3339 format

Type type

[BetaManagedAgentsManualTriggerContext](api/beta.md)

Type type

[BetaManagedAgentsTriggerType](api/beta.md)

One of the following:

"schedule"

"manual"

[BetaManagedAgentsUnknownRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsVaultArchivedRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsVaultNotFoundRunError](api/beta.md)

string message

Human-readable error description.

Type type

[BetaManagedAgentsWorkspaceArchivedRunError](api/beta.md)

string message

Human-readable error description.

Type type

---

*Copyright © Anthropic. All rights reserved.*
