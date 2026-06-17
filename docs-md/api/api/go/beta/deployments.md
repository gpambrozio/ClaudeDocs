# Deployments

Copy page



Go

# Deployments

##### [Create Deployment](api/beta/deployments/create.md)

client.Beta.Deployments.New(ctx, params) (\*[BetaManagedAgentsDeployment](api/beta.md), error)

POST/v1/deployments

##### [List Deployments](api/beta/deployments/list.md)

client.Beta.Deployments.List(ctx, params) (\*PageCursor[[BetaManagedAgentsDeployment](api/beta.md)], error)

GET/v1/deployments

##### [Get Deployment](api/beta/deployments/retrieve.md)

client.Beta.Deployments.Get(ctx, deploymentID, query) (\*[BetaManagedAgentsDeployment](api/beta.md), error)

GET/v1/deployments/{deployment\_id}

##### [Update Deployment](api/beta/deployments/update.md)

client.Beta.Deployments.Update(ctx, deploymentID, params) (\*[BetaManagedAgentsDeployment](api/beta.md), error)

POST/v1/deployments/{deployment\_id}

##### [Archive Deployment](api/beta/deployments/archive.md)

client.Beta.Deployments.Archive(ctx, deploymentID, body) (\*[BetaManagedAgentsDeployment](api/beta.md), error)

POST/v1/deployments/{deployment\_id}/archive

##### [Run Deployment Now](api/beta/deployments/run.md)

client.Beta.Deployments.Run(ctx, deploymentID, body) (\*[BetaManagedAgentsDeploymentRun](api/beta.md), error)

POST/v1/deployments/{deployment\_id}/run

##### [Pause Deployment](api/beta/deployments/pause.md)

client.Beta.Deployments.Pause(ctx, deploymentID, body) (\*[BetaManagedAgentsDeployment](api/beta.md), error)

POST/v1/deployments/{deployment\_id}/pause

##### [Unpause Deployment](api/beta/deployments/unpause.md)

client.Beta.Deployments.Unpause(ctx, deploymentID, body) (\*[BetaManagedAgentsDeployment](api/beta.md), error)

POST/v1/deployments/{deployment\_id}/unpause

##### ModelsExpand Collapse



type BetaManagedAgentsAgentArchivedDeploymentPausedReasonError struct{…}

The deployment's agent was archived.

Type BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorType



type BetaManagedAgentsCronSchedule struct{…}

5-field POSIX cron schedule with computed runtime timestamps.

Expression string

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

Timezone string

IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC").

Type BetaManagedAgentsCronScheduleType

LastRunAt TimeOptional

A timestamp in RFC 3339 format

UpcomingRunsAt []TimeOptional

Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.



type BetaManagedAgentsCronScheduleParamsResp struct{…}

5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

Expression string

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

Timezone string

Required. IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC"). Validated against the IANA timezone database.

Type BetaManagedAgentsCronScheduleParamsType



type BetaManagedAgentsDeployment struct{…}

A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

ID string

Unique identifier for this deployment.



Agent [BetaManagedAgentsAgentReference](api/beta.md)

A resolved agent reference with a concrete version.

ID string

Type BetaManagedAgentsAgentReferenceType

Version int64

ArchivedAt Time

A timestamp in RFC 3339 format

CreatedAt Time

A timestamp in RFC 3339 format

Description string

Description of what the deployment does.

EnvironmentID string

ID of the `environment` where sessions run.



InitialEvents [][BetaManagedAgentsDeploymentInitialEventUnion](api/beta.md)

Events sent to each session immediately after creation.

One of the following:



type BetaManagedAgentsDeploymentUserMessageEvent struct{…}

A user message sent to the session.



Content []BetaManagedAgentsDeploymentUserMessageEventContentUnion

Array of content blocks for the user message.

One of the following:



type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType



type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.



Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

One of the following:



type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType



type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.



type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType



type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

One of the following:



type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType



type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType



type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.



type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringOptional

Additional context about the document for the model.

Title stringOptional

The title of the document.

Type BetaManagedAgentsDeploymentUserMessageEventType



type BetaManagedAgentsDeploymentUserDefineOutcomeEvent struct{…}

An outcome the agent should work toward. The agent begins work on receipt.

Description string

What the agent should produce. This is the task specification.



Rubric BetaManagedAgentsDeploymentUserDefineOutcomeEventRubricUnion

Rubric for grading the quality of an outcome.

One of the following:



type BetaManagedAgentsFileRubric struct{…}

Rubric referenced by a file uploaded via the Files API.

FileID string

ID of the rubric file.

Type BetaManagedAgentsFileRubricType



type BetaManagedAgentsTextRubric struct{…}

Rubric content provided inline as text.

Content string

Rubric content. Plain text or markdown — the grader treats it as freeform text.

Type BetaManagedAgentsTextRubricType

Type BetaManagedAgentsDeploymentUserDefineOutcomeEventType

MaxIterations int64Optional

Eval→revision cycles before giving up. Default 3, max 20.



type BetaManagedAgentsDeploymentSystemMessageEvent struct{…}

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.



Content [][BetaManagedAgentsSystemContentBlock](api/beta.md)

System content blocks to append. Text-only.

Text string

The text content.

Type BetaManagedAgentsSystemContentBlockType

Type BetaManagedAgentsDeploymentSystemMessageEventType

Metadata map[string, string]

Arbitrary key-value metadata. Maximum 16 pairs.

Name string

Human-readable name.



PausedReason [BetaManagedAgentsDeploymentPausedReasonUnion](api/beta.md)

Why a deployment is paused. Non-null exactly when `status` is `paused`.

One of the following:



type BetaManagedAgentsManualDeploymentPausedReason struct{…}

The caller invoked the pause endpoint on the deployment.

Type BetaManagedAgentsManualDeploymentPausedReasonType



type BetaManagedAgentsErrorDeploymentPausedReason struct{…}

A scheduled fire recorded a failed run whose error auto-pauses the deployment.



Error [BetaManagedAgentsDeploymentPausedReasonErrorUnion](api/beta.md)

The error that triggered an auto-pause. Matches the failed run's `error.type`.

One of the following:



type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError struct{…}

The deployment's environment was archived.

Type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType



type BetaManagedAgentsAgentArchivedDeploymentPausedReasonError struct{…}

The deployment's agent was archived.

Type BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorType



type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError struct{…}

The deployment's environment no longer exists.

Type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError struct{…}

A vault referenced by the deployment no longer exists.

Type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsFileNotFoundDeploymentPausedReasonError struct{…}

A file resource referenced by the deployment no longer exists.

Type BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError struct{…}

A referenced resource no longer exists and its kind was not reported.

Type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError struct{…}

The deployment's workspace was archived.

Type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType



type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError struct{…}

The deployment's organization is disabled.

Type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType



type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError struct{…}

A memory store referenced by the deployment is archived.

Type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType



type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError struct{…}

A skill referenced by the deployment's agent no longer exists.

Type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsVaultArchivedDeploymentPausedReasonError struct{…}

A vault referenced by the deployment is archived.

Type BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType



type BetaManagedAgentsUnknownDeploymentPausedReasonError struct{…}

An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

Type BetaManagedAgentsUnknownDeploymentPausedReasonErrorType



type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError struct{…}

The deployment configures resources, but its environment is self-hosted and cannot mount them.

Type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType



type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError struct{…}

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

Type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType

Type BetaManagedAgentsErrorDeploymentPausedReasonType



Resources [][BetaManagedAgentsSessionResourceConfigUnion](api/beta.md)

Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

One of the following:



type BetaManagedAgentsGitHubRepositoryResourceConfig struct{…}

A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

Type BetaManagedAgentsGitHubRepositoryResourceConfigType

URL string

Github URL of the repository



Checkout BetaManagedAgentsGitHubRepositoryResourceConfigCheckoutUnionOptional

Branch or commit to check out. Defaults to the repository's default branch.

One of the following:



type BetaManagedAgentsBranchCheckout struct{…}

Name string

Branch name to check out.

Type BetaManagedAgentsBranchCheckoutType



type BetaManagedAgentsCommitCheckout struct{…}

Sha string

Full commit SHA to check out.

Type BetaManagedAgentsCommitCheckoutType

MountPath stringOptional

Mount path in the container. Defaults to `/workspace/<repo-name>`.



type BetaManagedAgentsFileResourceConfig struct{…}

A file mounted into each session's container.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileResourceConfigType

MountPath stringOptional

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.



type BetaManagedAgentsMemoryStoreResourceConfig struct{…}

A memory store attached to each session created from this deployment.

MemoryStoreID string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type BetaManagedAgentsMemoryStoreResourceConfigType



Access BetaManagedAgentsMemoryStoreResourceConfigAccessOptional

Access mode for an attached memory store.

One of the following:

const BetaManagedAgentsMemoryStoreResourceConfigAccessReadWrite BetaManagedAgentsMemoryStoreResourceConfigAccess = "read\_write"

const BetaManagedAgentsMemoryStoreResourceConfigAccessReadOnly BetaManagedAgentsMemoryStoreResourceConfigAccess = "read\_only"

Instructions stringOptional

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.



Schedule [BetaManagedAgentsSchedule](api/beta.md)

5-field POSIX cron schedule with computed runtime timestamps.

Expression string

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

Timezone string

IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC").

Type BetaManagedAgentsScheduleType

LastRunAt TimeOptional

A timestamp in RFC 3339 format

UpcomingRunsAt []TimeOptional

Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.



Status [BetaManagedAgentsDeploymentStatus](api/beta.md)

Lifecycle status of a deployment.

One of the following:

const BetaManagedAgentsDeploymentStatusActive [BetaManagedAgentsDeploymentStatus](api/beta.md) = "active"

const BetaManagedAgentsDeploymentStatusPaused [BetaManagedAgentsDeploymentStatus](api/beta.md) = "paused"

Type BetaManagedAgentsDeploymentType

UpdatedAt Time

A timestamp in RFC 3339 format

VaultIDs []string

Vault IDs supplying stored credentials for sessions created from this deployment.



type BetaManagedAgentsDeploymentInitialEventUnion interface{…}

An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

One of the following:



type BetaManagedAgentsDeploymentUserMessageEvent struct{…}

A user message sent to the session.



Content []BetaManagedAgentsDeploymentUserMessageEventContentUnion

Array of content blocks for the user message.

One of the following:



type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType



type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.



Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

One of the following:



type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType



type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.



type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType



type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

One of the following:



type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType



type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType



type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.



type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringOptional

Additional context about the document for the model.

Title stringOptional

The title of the document.

Type BetaManagedAgentsDeploymentUserMessageEventType



type BetaManagedAgentsDeploymentUserDefineOutcomeEvent struct{…}

An outcome the agent should work toward. The agent begins work on receipt.

Description string

What the agent should produce. This is the task specification.



Rubric BetaManagedAgentsDeploymentUserDefineOutcomeEventRubricUnion

Rubric for grading the quality of an outcome.

One of the following:



type BetaManagedAgentsFileRubric struct{…}

Rubric referenced by a file uploaded via the Files API.

FileID string

ID of the rubric file.

Type BetaManagedAgentsFileRubricType



type BetaManagedAgentsTextRubric struct{…}

Rubric content provided inline as text.

Content string

Rubric content. Plain text or markdown — the grader treats it as freeform text.

Type BetaManagedAgentsTextRubricType

Type BetaManagedAgentsDeploymentUserDefineOutcomeEventType

MaxIterations int64Optional

Eval→revision cycles before giving up. Default 3, max 20.



type BetaManagedAgentsDeploymentSystemMessageEvent struct{…}

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.



Content [][BetaManagedAgentsSystemContentBlock](api/beta.md)

System content blocks to append. Text-only.

Text string

The text content.

Type BetaManagedAgentsSystemContentBlockType

Type BetaManagedAgentsDeploymentSystemMessageEventType



type BetaManagedAgentsDeploymentInitialEventParamsUnionResp interface{…}

An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

One of the following:



type BetaManagedAgentsUserMessageEventParamsResp struct{…}

Parameters for sending a user message to the session.



Content []BetaManagedAgentsUserMessageEventParamsContentUnionResp

Array of content blocks for the user message.

One of the following:



type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType



type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.



Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

One of the following:



type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType



type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.



type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType



type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

One of the following:



type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType



type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType



type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.



type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringOptional

Additional context about the document for the model.

Title stringOptional

The title of the document.

Type BetaManagedAgentsUserMessageEventParamsType



type BetaManagedAgentsUserDefineOutcomeEventParamsResp struct{…}

Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

Description string

What the agent should produce. This is the task specification.



Rubric BetaManagedAgentsUserDefineOutcomeEventParamsRubricUnionResp

Rubric for grading the quality of an outcome.

One of the following:



type BetaManagedAgentsFileRubricParamsResp struct{…}

Rubric referenced by a file uploaded via the Files API.

FileID string

ID of the rubric file.

Type BetaManagedAgentsFileRubricParamsType



type BetaManagedAgentsTextRubricParamsResp struct{…}

Rubric content provided inline as text.

Content string

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

Type BetaManagedAgentsTextRubricParamsType

Type BetaManagedAgentsUserDefineOutcomeEventParamsType

MaxIterations int64Optional

Eval→revision cycles before giving up. Default 3, max 20.



type BetaManagedAgentsSystemMessageEventParamsResp struct{…}

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.



Content [][BetaManagedAgentsSystemContentBlock](api/beta.md)

System content blocks to append. Text-only.

Text string

The text content.

Type BetaManagedAgentsSystemContentBlockType

Type BetaManagedAgentsSystemMessageEventParamsType



type BetaManagedAgentsDeploymentPausedReasonUnion interface{…}

Why a deployment is paused. Non-null exactly when `status` is `paused`.

One of the following:



type BetaManagedAgentsManualDeploymentPausedReason struct{…}

The caller invoked the pause endpoint on the deployment.

Type BetaManagedAgentsManualDeploymentPausedReasonType



type BetaManagedAgentsErrorDeploymentPausedReason struct{…}

A scheduled fire recorded a failed run whose error auto-pauses the deployment.



Error [BetaManagedAgentsDeploymentPausedReasonErrorUnion](api/beta.md)

The error that triggered an auto-pause. Matches the failed run's `error.type`.

One of the following:



type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError struct{…}

The deployment's environment was archived.

Type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType



type BetaManagedAgentsAgentArchivedDeploymentPausedReasonError struct{…}

The deployment's agent was archived.

Type BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorType



type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError struct{…}

The deployment's environment no longer exists.

Type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError struct{…}

A vault referenced by the deployment no longer exists.

Type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsFileNotFoundDeploymentPausedReasonError struct{…}

A file resource referenced by the deployment no longer exists.

Type BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError struct{…}

A referenced resource no longer exists and its kind was not reported.

Type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError struct{…}

The deployment's workspace was archived.

Type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType



type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError struct{…}

The deployment's organization is disabled.

Type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType



type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError struct{…}

A memory store referenced by the deployment is archived.

Type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType



type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError struct{…}

A skill referenced by the deployment's agent no longer exists.

Type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsVaultArchivedDeploymentPausedReasonError struct{…}

A vault referenced by the deployment is archived.

Type BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType



type BetaManagedAgentsUnknownDeploymentPausedReasonError struct{…}

An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

Type BetaManagedAgentsUnknownDeploymentPausedReasonErrorType



type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError struct{…}

The deployment configures resources, but its environment is self-hosted and cannot mount them.

Type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType



type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError struct{…}

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

Type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType

Type BetaManagedAgentsErrorDeploymentPausedReasonType



type BetaManagedAgentsDeploymentPausedReasonErrorUnion interface{…}

The error that triggered an auto-pause. Matches the failed run's `error.type`.

One of the following:



type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError struct{…}

The deployment's environment was archived.

Type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType



type BetaManagedAgentsAgentArchivedDeploymentPausedReasonError struct{…}

The deployment's agent was archived.

Type BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorType



type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError struct{…}

The deployment's environment no longer exists.

Type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError struct{…}

A vault referenced by the deployment no longer exists.

Type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsFileNotFoundDeploymentPausedReasonError struct{…}

A file resource referenced by the deployment no longer exists.

Type BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError struct{…}

A referenced resource no longer exists and its kind was not reported.

Type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError struct{…}

The deployment's workspace was archived.

Type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType



type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError struct{…}

The deployment's organization is disabled.

Type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType



type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError struct{…}

A memory store referenced by the deployment is archived.

Type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType



type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError struct{…}

A skill referenced by the deployment's agent no longer exists.

Type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsVaultArchivedDeploymentPausedReasonError struct{…}

A vault referenced by the deployment is archived.

Type BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType



type BetaManagedAgentsUnknownDeploymentPausedReasonError struct{…}

An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

Type BetaManagedAgentsUnknownDeploymentPausedReasonErrorType



type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError struct{…}

The deployment configures resources, but its environment is self-hosted and cannot mount them.

Type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType



type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError struct{…}

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

Type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType



type BetaManagedAgentsDeploymentStatus string

Lifecycle status of a deployment.

One of the following:

const BetaManagedAgentsDeploymentStatusActive [BetaManagedAgentsDeploymentStatus](api/beta.md) = "active"

const BetaManagedAgentsDeploymentStatusPaused [BetaManagedAgentsDeploymentStatus](api/beta.md) = "paused"



type BetaManagedAgentsDeploymentSystemMessageEvent struct{…}

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.



Content [][BetaManagedAgentsSystemContentBlock](api/beta.md)

System content blocks to append. Text-only.

Text string

The text content.

Type BetaManagedAgentsSystemContentBlockType

Type BetaManagedAgentsDeploymentSystemMessageEventType



type BetaManagedAgentsDeploymentUserDefineOutcomeEvent struct{…}

An outcome the agent should work toward. The agent begins work on receipt.

Description string

What the agent should produce. This is the task specification.



Rubric BetaManagedAgentsDeploymentUserDefineOutcomeEventRubricUnion

Rubric for grading the quality of an outcome.

One of the following:



type BetaManagedAgentsFileRubric struct{…}

Rubric referenced by a file uploaded via the Files API.

FileID string

ID of the rubric file.

Type BetaManagedAgentsFileRubricType



type BetaManagedAgentsTextRubric struct{…}

Rubric content provided inline as text.

Content string

Rubric content. Plain text or markdown — the grader treats it as freeform text.

Type BetaManagedAgentsTextRubricType

Type BetaManagedAgentsDeploymentUserDefineOutcomeEventType

MaxIterations int64Optional

Eval→revision cycles before giving up. Default 3, max 20.



type BetaManagedAgentsDeploymentUserMessageEvent struct{…}

A user message sent to the session.



Content []BetaManagedAgentsDeploymentUserMessageEventContentUnion

Array of content blocks for the user message.

One of the following:



type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType



type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.



Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

One of the following:



type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType



type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.



type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType



type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

One of the following:



type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType



type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType



type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.



type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringOptional

Additional context about the document for the model.

Title stringOptional

The title of the document.

Type BetaManagedAgentsDeploymentUserMessageEventType



type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError struct{…}

The deployment's environment was archived.

Type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType



type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError struct{…}

The deployment's environment no longer exists.

Type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsErrorDeploymentPausedReason struct{…}

A scheduled fire recorded a failed run whose error auto-pauses the deployment.



Error [BetaManagedAgentsDeploymentPausedReasonErrorUnion](api/beta.md)

The error that triggered an auto-pause. Matches the failed run's `error.type`.

One of the following:



type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError struct{…}

The deployment's environment was archived.

Type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType



type BetaManagedAgentsAgentArchivedDeploymentPausedReasonError struct{…}

The deployment's agent was archived.

Type BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorType



type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError struct{…}

The deployment's environment no longer exists.

Type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError struct{…}

A vault referenced by the deployment no longer exists.

Type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsFileNotFoundDeploymentPausedReasonError struct{…}

A file resource referenced by the deployment no longer exists.

Type BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError struct{…}

A referenced resource no longer exists and its kind was not reported.

Type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError struct{…}

The deployment's workspace was archived.

Type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType



type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError struct{…}

The deployment's organization is disabled.

Type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType



type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError struct{…}

A memory store referenced by the deployment is archived.

Type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType



type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError struct{…}

A skill referenced by the deployment's agent no longer exists.

Type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsVaultArchivedDeploymentPausedReasonError struct{…}

A vault referenced by the deployment is archived.

Type BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType



type BetaManagedAgentsUnknownDeploymentPausedReasonError struct{…}

An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

Type BetaManagedAgentsUnknownDeploymentPausedReasonErrorType



type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError struct{…}

The deployment configures resources, but its environment is self-hosted and cannot mount them.

Type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType



type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError struct{…}

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

Type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType

Type BetaManagedAgentsErrorDeploymentPausedReasonType



type BetaManagedAgentsFileNotFoundDeploymentPausedReasonError struct{…}

A file resource referenced by the deployment no longer exists.

Type BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsFileResourceConfig struct{…}

A file mounted into each session's container.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileResourceConfigType

MountPath stringOptional

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.



type BetaManagedAgentsGitHubRepositoryResourceConfig struct{…}

A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

Type BetaManagedAgentsGitHubRepositoryResourceConfigType

URL string

Github URL of the repository



Checkout BetaManagedAgentsGitHubRepositoryResourceConfigCheckoutUnionOptional

Branch or commit to check out. Defaults to the repository's default branch.

One of the following:



type BetaManagedAgentsBranchCheckout struct{…}

Name string

Branch name to check out.

Type BetaManagedAgentsBranchCheckoutType



type BetaManagedAgentsCommitCheckout struct{…}

Sha string

Full commit SHA to check out.

Type BetaManagedAgentsCommitCheckoutType

MountPath stringOptional

Mount path in the container. Defaults to `/workspace/<repo-name>`.



type BetaManagedAgentsManualDeploymentPausedReason struct{…}

The caller invoked the pause endpoint on the deployment.

Type BetaManagedAgentsManualDeploymentPausedReasonType



type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError struct{…}

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

Type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType



type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError struct{…}

A memory store referenced by the deployment is archived.

Type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType



type BetaManagedAgentsMemoryStoreResourceConfig struct{…}

A memory store attached to each session created from this deployment.

MemoryStoreID string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type BetaManagedAgentsMemoryStoreResourceConfigType



Access BetaManagedAgentsMemoryStoreResourceConfigAccessOptional

Access mode for an attached memory store.

One of the following:

const BetaManagedAgentsMemoryStoreResourceConfigAccessReadWrite BetaManagedAgentsMemoryStoreResourceConfigAccess = "read\_write"

const BetaManagedAgentsMemoryStoreResourceConfigAccessReadOnly BetaManagedAgentsMemoryStoreResourceConfigAccess = "read\_only"

Instructions stringOptional

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.



type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError struct{…}

The deployment's organization is disabled.

Type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType



type BetaManagedAgentsSchedule struct{…}

5-field POSIX cron schedule with computed runtime timestamps.

Expression string

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

Timezone string

IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC").

Type BetaManagedAgentsScheduleType

LastRunAt TimeOptional

A timestamp in RFC 3339 format

UpcomingRunsAt []TimeOptional

Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.



type BetaManagedAgentsScheduleParamsResp struct{…}

5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

Expression string

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

Timezone string

Required. IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC"). Validated against the IANA timezone database.

Type BetaManagedAgentsScheduleParamsType



type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError struct{…}

The deployment configures resources, but its environment is self-hosted and cannot mount them.

Type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType



type BetaManagedAgentsSessionResourceConfigUnion interface{…}

A configured session resource. Echoes the input minus write-only credentials.

One of the following:



type BetaManagedAgentsGitHubRepositoryResourceConfig struct{…}

A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

Type BetaManagedAgentsGitHubRepositoryResourceConfigType

URL string

Github URL of the repository



Checkout BetaManagedAgentsGitHubRepositoryResourceConfigCheckoutUnionOptional

Branch or commit to check out. Defaults to the repository's default branch.

One of the following:



type BetaManagedAgentsBranchCheckout struct{…}

Name string

Branch name to check out.

Type BetaManagedAgentsBranchCheckoutType



type BetaManagedAgentsCommitCheckout struct{…}

Sha string

Full commit SHA to check out.

Type BetaManagedAgentsCommitCheckoutType

MountPath stringOptional

Mount path in the container. Defaults to `/workspace/<repo-name>`.



type BetaManagedAgentsFileResourceConfig struct{…}

A file mounted into each session's container.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileResourceConfigType

MountPath stringOptional

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.



type BetaManagedAgentsMemoryStoreResourceConfig struct{…}

A memory store attached to each session created from this deployment.

MemoryStoreID string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type BetaManagedAgentsMemoryStoreResourceConfigType



Access BetaManagedAgentsMemoryStoreResourceConfigAccessOptional

Access mode for an attached memory store.

One of the following:

const BetaManagedAgentsMemoryStoreResourceConfigAccessReadWrite BetaManagedAgentsMemoryStoreResourceConfigAccess = "read\_write"

const BetaManagedAgentsMemoryStoreResourceConfigAccessReadOnly BetaManagedAgentsMemoryStoreResourceConfigAccess = "read\_only"

Instructions stringOptional

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.



type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError struct{…}

A referenced resource no longer exists and its kind was not reported.

Type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError struct{…}

A skill referenced by the deployment's agent no longer exists.

Type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsUnknownDeploymentPausedReasonError struct{…}

An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

Type BetaManagedAgentsUnknownDeploymentPausedReasonErrorType



type BetaManagedAgentsVaultArchivedDeploymentPausedReasonError struct{…}

A vault referenced by the deployment is archived.

Type BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType



type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError struct{…}

A vault referenced by the deployment no longer exists.

Type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType



type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError struct{…}

The deployment's workspace was archived.

Type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType

---

*Copyright © Anthropic. All rights reserved.*
