# Deployments

Copy page

SDK language

PHP

# Deployments

##### [Create Deployment](api/beta/deployments/create.md)

$client->beta->deployments->create([Agent](api/beta/deployments/create.md) agent, string environmentID, list<[BetaManagedAgentsDeploymentInitialEventParams](api/beta.md)> initialEvents, string name, ?string description, ?array<string,string> metadata, ?list<Resource> resources, ?[BetaManagedAgentsScheduleParams](api/beta.md) schedule, ?list<string> vaultIDs, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeployment](api/beta.md)

POST/v1/deployments

##### [List Deployments](api/beta/deployments/list.md)

$client->beta->deployments->list(?string agentID, ?\Datetime createdAtGte, ?\Datetime createdAtLte, ?bool includeArchived, ?int limit, ?string page, ?[BetaManagedAgentsDeploymentStatus](api/beta.md) status, ?list<AnthropicBeta> betas): PageCursor<[BetaManagedAgentsDeployment](api/beta.md)>

GET/v1/deployments

##### [Get Deployment](api/beta/deployments/retrieve.md)

$client->beta->deployments->retrieve(string deploymentID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeployment](api/beta.md)

GET/v1/deployments/{deployment\_id}

##### [Update Deployment](api/beta/deployments/update.md)

$client->beta->deployments->update(string deploymentID, ?[Agent](api/beta/deployments/update.md) agent, ?string description, ?string environmentID, ?list<[BetaManagedAgentsDeploymentInitialEventParams](api/beta.md)> initialEvents, ?array<string,string> metadata, ?string name, ?list<Resource> resources, ?[BetaManagedAgentsScheduleParams](api/beta.md) schedule, ?list<string> vaultIDs, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeployment](api/beta.md)

POST/v1/deployments/{deployment\_id}

##### [Archive Deployment](api/beta/deployments/archive.md)

$client->beta->deployments->archive(string deploymentID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeployment](api/beta.md)

POST/v1/deployments/{deployment\_id}/archive

##### [Run Deployment Now](api/beta/deployments/run.md)

$client->beta->deployments->run(string deploymentID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeploymentRun](api/beta.md)

POST/v1/deployments/{deployment\_id}/run

##### [Pause Deployment](api/beta/deployments/pause.md)

$client->beta->deployments->pause(string deploymentID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeployment](api/beta.md)

POST/v1/deployments/{deployment\_id}/pause

##### [Unpause Deployment](api/beta/deployments/unpause.md)

$client->beta->deployments->unpause(string deploymentID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeployment](api/beta.md)

POST/v1/deployments/{deployment\_id}/unpause

##### ModelsExpand Collapse

[BetaManagedAgentsAgentArchivedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsCronSchedule](api/beta.md)

string expression

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

string timezone

IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC").

Type type

?\Datetime lastRunAt

A timestamp in RFC 3339 format

?list<\Datetime> upcomingRunsAt

Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

[BetaManagedAgentsCronScheduleParams](api/beta.md)

string expression

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

string timezone

Required. IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC"). Validated against the IANA timezone database.

Type type

[BetaManagedAgentsDeployment](api/beta.md)

string id

Unique identifier for this deployment.

[BetaManagedAgentsAgentReference](api/beta.md) agent

A resolved agent reference with a concrete version.

?\Datetime archivedAt

A timestamp in RFC 3339 format

\Datetime createdAt

A timestamp in RFC 3339 format

?string description

Description of what the deployment does.

string environmentID

ID of the `environment` where sessions run.

list<[BetaManagedAgentsDeploymentInitialEvent](api/beta.md)> initialEvents

Events sent to each session immediately after creation.

array<string,string> metadata

Arbitrary key-value metadata. Maximum 16 pairs.

string name

Human-readable name.

?[BetaManagedAgentsDeploymentPausedReason](api/beta.md) pausedReason

Why a deployment is paused. Non-null exactly when `status` is `paused`.

list<[BetaManagedAgentsSessionResourceConfig](api/beta.md)> resources

Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

?[BetaManagedAgentsSchedule](api/beta.md) schedule

5-field POSIX cron schedule with computed runtime timestamps.

[BetaManagedAgentsDeploymentStatus](api/beta.md) status

Lifecycle status of a deployment.

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

list<string> vaultIDs

Vault IDs supplying stored credentials for sessions created from this deployment.

[BetaManagedAgentsDeploymentInitialEvent](api/beta.md)

One of the following:

[BetaManagedAgentsDeploymentUserMessageEvent](api/beta.md)

list<Content> content

Array of content blocks for the user message.

Type type

[BetaManagedAgentsDeploymentUserDefineOutcomeEvent](api/beta.md)

string description

What the agent should produce. This is the task specification.

Rubric rubric

Rubric for grading the quality of an outcome.

Type type

?int maxIterations

Eval→revision cycles before giving up. Default 3, max 20.

[BetaManagedAgentsDeploymentSystemMessageEvent](api/beta.md)

list<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks to append. Text-only.

Type type

[BetaManagedAgentsDeploymentInitialEventParams](api/beta.md)

One of the following:

[ManagedAgentsUserMessageEventParams](api/beta.md)

list<Content> content

Array of content blocks for the user message.

Type type

[ManagedAgentsUserDefineOutcomeEventParams](api/beta.md)

string description

What the agent should produce. This is the task specification.

Rubric rubric

Rubric for grading the quality of an outcome.

Type type

?int maxIterations

Eval→revision cycles before giving up. Default 3, max 20.

[ManagedAgentsSystemMessageEventParams](api/beta.md)

list<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks to append. Text-only.

Type type

[BetaManagedAgentsDeploymentPausedReason](api/beta.md)

One of the following:

[BetaManagedAgentsManualDeploymentPausedReason](api/beta.md)

Type type

[BetaManagedAgentsErrorDeploymentPausedReason](api/beta.md)

[BetaManagedAgentsDeploymentPausedReasonError](api/beta.md) error

The error that triggered an auto-pause. Matches the failed run's `error.type`.

Type type

[BetaManagedAgentsDeploymentPausedReasonError](api/beta.md)

One of the following:

[BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsAgentArchivedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsFileNotFoundDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsVaultArchivedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsUnknownDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsDeploymentStatus](api/beta.md)

One of the following:

"active"

"paused"

[BetaManagedAgentsDeploymentSystemMessageEvent](api/beta.md)

list<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks to append. Text-only.

Type type

[BetaManagedAgentsDeploymentUserDefineOutcomeEvent](api/beta.md)

string description

What the agent should produce. This is the task specification.

Rubric rubric

Rubric for grading the quality of an outcome.

Type type

?int maxIterations

Eval→revision cycles before giving up. Default 3, max 20.

[BetaManagedAgentsDeploymentUserMessageEvent](api/beta.md)

list<Content> content

Array of content blocks for the user message.

Type type

[BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsErrorDeploymentPausedReason](api/beta.md)

[BetaManagedAgentsDeploymentPausedReasonError](api/beta.md) error

The error that triggered an auto-pause. Matches the failed run's `error.type`.

Type type

[BetaManagedAgentsFileNotFoundDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsFileResourceConfig](api/beta.md)

string fileID

ID of a previously uploaded file.

Type type

?string mountPath

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

[BetaManagedAgentsGitHubRepositoryResourceConfig](api/beta.md)

Type type

string url

Github URL of the repository

?Checkout checkout

Branch or commit to check out. Defaults to the repository's default branch.

?string mountPath

Mount path in the container. Defaults to `/workspace/<repo-name>`.

[BetaManagedAgentsManualDeploymentPausedReason](api/beta.md)

Type type

[BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsMemoryStoreResourceConfig](api/beta.md)

string memoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type type

?Access access

Access mode for an attached memory store.

?string instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

[BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsSchedule](api/beta.md)

string expression

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

string timezone

IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC").

Type type

?\Datetime lastRunAt

A timestamp in RFC 3339 format

?list<\Datetime> upcomingRunsAt

Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

[BetaManagedAgentsScheduleParams](api/beta.md)

string expression

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

string timezone

Required. IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC"). Validated against the IANA timezone database.

Type type

[BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsSessionResourceConfig](api/beta.md)

One of the following:

[BetaManagedAgentsGitHubRepositoryResourceConfig](api/beta.md)

Type type

string url

Github URL of the repository

?Checkout checkout

Branch or commit to check out. Defaults to the repository's default branch.

?string mountPath

Mount path in the container. Defaults to `/workspace/<repo-name>`.

[BetaManagedAgentsFileResourceConfig](api/beta.md)

string fileID

ID of a previously uploaded file.

Type type

?string mountPath

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

[BetaManagedAgentsMemoryStoreResourceConfig](api/beta.md)

string memoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type type

?Access access

Access mode for an attached memory store.

?string instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

[BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsUnknownDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsVaultArchivedDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError](api/beta.md)

Type type

[BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError](api/beta.md)

Type type

---

*Copyright © Anthropic. All rights reserved.*
