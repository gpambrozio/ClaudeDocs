# Deployments

Copy page



C#

# Deployments

##### [Create Deployment](api/beta/deployments/create.md)

[BetaManagedAgentsDeployment](api/beta.md) Beta.Deployments.Create(DeploymentCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/deployments

##### [List Deployments](api/beta/deployments/list.md)

[DeploymentListPageResponse](api/beta.md) Beta.Deployments.List(DeploymentListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/deployments

##### [Get Deployment](api/beta/deployments/retrieve.md)

[BetaManagedAgentsDeployment](api/beta.md) Beta.Deployments.Retrieve(DeploymentRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/deployments/{deployment\_id}

##### [Update Deployment](api/beta/deployments/update.md)

[BetaManagedAgentsDeployment](api/beta.md) Beta.Deployments.Update(DeploymentUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/deployments/{deployment\_id}

##### [Archive Deployment](api/beta/deployments/archive.md)

[BetaManagedAgentsDeployment](api/beta.md) Beta.Deployments.Archive(DeploymentArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/deployments/{deployment\_id}/archive

##### [Run Deployment Now](api/beta/deployments/run.md)

[BetaManagedAgentsDeploymentRun](api/beta.md) Beta.Deployments.Run(DeploymentRunParamsparameters, CancellationTokencancellationToken = default)

POST/v1/deployments/{deployment\_id}/run

##### [Pause Deployment](api/beta/deployments/pause.md)

[BetaManagedAgentsDeployment](api/beta.md) Beta.Deployments.Pause(DeploymentPauseParamsparameters, CancellationTokencancellationToken = default)

POST/v1/deployments/{deployment\_id}/pause

##### [Unpause Deployment](api/beta/deployments/unpause.md)

[BetaManagedAgentsDeployment](api/beta.md) Beta.Deployments.Unpause(DeploymentUnpauseParamsparameters, CancellationTokencancellationToken = default)

POST/v1/deployments/{deployment\_id}/unpause

##### ModelsExpand Collapse



class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:

The deployment's agent was archived.

required Type Type



class BetaManagedAgentsCronSchedule:

5-field POSIX cron schedule with computed runtime timestamps.

required string Expression

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

required string Timezone

IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC").

required Type Type

DateTimeOffset? LastRunAt

A timestamp in RFC 3339 format

IReadOnlyList<DateTimeOffset> UpcomingRunsAt

Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.



class BetaManagedAgentsCronScheduleParams:

5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

required string Expression

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

required string Timezone

Required. IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC"). Validated against the IANA timezone database.

required Type Type



class BetaManagedAgentsDeployment:

A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

required string ID

Unique identifier for this deployment.



required [BetaManagedAgentsAgentReference](api/beta.md) Agent

A resolved agent reference with a concrete version.

required string ID

required Type Type

required Int Version

required DateTimeOffset? ArchivedAt

A timestamp in RFC 3339 format

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string? Description

Description of what the deployment does.

required string EnvironmentID

ID of the `environment` where sessions run.



required IReadOnlyList<[BetaManagedAgentsDeploymentInitialEvent](api/beta.md)> InitialEvents

Events sent to each session immediately after creation.

One of the following:



class BetaManagedAgentsDeploymentUserMessageEvent:

A user message sent to the session.



required IReadOnlyList<Content> Content

Array of content blocks for the user message.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type



class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:

An outcome the agent should work toward. The agent begins work on receipt.

required string Description

What the agent should produce. This is the task specification.



required Rubric Rubric

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubric:

Rubric referenced by a file uploaded via the Files API.

required string FileID

ID of the rubric file.

required Type Type



class BetaManagedAgentsTextRubric:

Rubric content provided inline as text.

required string Content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

required Type Type

required Type Type

Int? MaxIterations

Eval→revision cycles before giving up. Default 3, max 20.



class BetaManagedAgentsDeploymentSystemMessageEvent:

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.



required IReadOnlyList<[BetaManagedAgentsSystemContentBlock](api/beta.md)> Content

System content blocks to append. Text-only.

required string Text

The text content.

required Type Type

required Type Type

required IReadOnlyDictionary<string, string> Metadata

Arbitrary key-value metadata. Maximum 16 pairs.

required string Name

Human-readable name.



required [BetaManagedAgentsDeploymentPausedReason](api/beta.md)? PausedReason

Why a deployment is paused. Non-null exactly when `status` is `paused`.

One of the following:



class BetaManagedAgentsManualDeploymentPausedReason:

The caller invoked the pause endpoint on the deployment.

required Type Type



class BetaManagedAgentsErrorDeploymentPausedReason:

A scheduled fire recorded a failed run whose error auto-pauses the deployment.



required [BetaManagedAgentsDeploymentPausedReasonError](api/beta.md) Error

The error that triggered an auto-pause. Matches the failed run's `error.type`.

One of the following:



class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:

The deployment's environment was archived.

required Type Type



class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:

The deployment's agent was archived.

required Type Type



class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:

The deployment's environment no longer exists.

required Type Type



class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:

A vault referenced by the deployment no longer exists.

required Type Type



class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:

A file resource referenced by the deployment no longer exists.

required Type Type



class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:

A referenced resource no longer exists and its kind was not reported.

required Type Type



class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:

The deployment's workspace was archived.

required Type Type



class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:

The deployment's organization is disabled.

required Type Type



class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:

A memory store referenced by the deployment is archived.

required Type Type



class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:

A skill referenced by the deployment's agent no longer exists.

required Type Type



class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:

A vault referenced by the deployment is archived.

required Type Type



class BetaManagedAgentsUnknownDeploymentPausedReasonError:

An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

required Type Type



class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:

The deployment configures resources, but its environment is self-hosted and cannot mount them.

required Type Type



class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

required Type Type

required Type Type



required IReadOnlyList<[BetaManagedAgentsSessionResourceConfig](api/beta.md)> Resources

Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

One of the following:



class BetaManagedAgentsGitHubRepositoryResourceConfig:

A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

required Type Type

required string Url

Github URL of the repository



Checkout? Checkout

Branch or commit to check out. Defaults to the repository's default branch.

One of the following:



class BetaManagedAgentsBranchCheckout:

required string Name

Branch name to check out.

required Type Type



class BetaManagedAgentsCommitCheckout:

required string Sha

Full commit SHA to check out.

required Type Type

string? MountPath

Mount path in the container. Defaults to `/workspace/<repo-name>`.



class BetaManagedAgentsFileResourceConfig:

A file mounted into each session's container.

required string FileID

ID of a previously uploaded file.

required Type Type

string? MountPath

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.



class BetaManagedAgentsMemoryStoreResourceConfig:

A memory store attached to each session created from this deployment.

required string MemoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

required Type Type



Access? Access

Access mode for an attached memory store.

One of the following:

"read\_write"ReadWrite

"read\_only"ReadOnly

string? Instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.



required [BetaManagedAgentsSchedule](api/beta.md)? Schedule

5-field POSIX cron schedule with computed runtime timestamps.

required string Expression

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

required string Timezone

IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC").

required Type Type

DateTimeOffset? LastRunAt

A timestamp in RFC 3339 format

IReadOnlyList<DateTimeOffset> UpcomingRunsAt

Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.



required [BetaManagedAgentsDeploymentStatus](api/beta.md) Status

Lifecycle status of a deployment.

One of the following:

"active"Active

"paused"Paused

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required IReadOnlyList<string> VaultIds

Vault IDs supplying stored credentials for sessions created from this deployment.



class BetaManagedAgentsDeploymentInitialEvent: A class that can be one of several variants.union 

An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.



class BetaManagedAgentsDeploymentUserMessageEvent:

A user message sent to the session.



required IReadOnlyList<Content> Content

Array of content blocks for the user message.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type



class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:

An outcome the agent should work toward. The agent begins work on receipt.

required string Description

What the agent should produce. This is the task specification.



required Rubric Rubric

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubric:

Rubric referenced by a file uploaded via the Files API.

required string FileID

ID of the rubric file.

required Type Type



class BetaManagedAgentsTextRubric:

Rubric content provided inline as text.

required string Content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

required Type Type

required Type Type

Int? MaxIterations

Eval→revision cycles before giving up. Default 3, max 20.



class BetaManagedAgentsDeploymentSystemMessageEvent:

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.



required IReadOnlyList<[BetaManagedAgentsSystemContentBlock](api/beta.md)> Content

System content blocks to append. Text-only.

required string Text

The text content.

required Type Type

required Type Type



class BetaManagedAgentsDeploymentInitialEventParams: A class that can be one of several variants.union 

An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.



class BetaManagedAgentsUserMessageEventParams:

Parameters for sending a user message to the session.



required IReadOnlyList<Content> Content

Array of content blocks for the user message.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type



class BetaManagedAgentsUserDefineOutcomeEventParams:

Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

required string Description

What the agent should produce. This is the task specification.



required Rubric Rubric

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubricParams:

Rubric referenced by a file uploaded via the Files API.

required string FileID

ID of the rubric file.

required Type Type



class BetaManagedAgentsTextRubricParams:

Rubric content provided inline as text.

required string Content

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

required Type Type

required Type Type

Int? MaxIterations

Eval→revision cycles before giving up. Default 3, max 20.



class BetaManagedAgentsSystemMessageEventParams:

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.



required IReadOnlyList<[BetaManagedAgentsSystemContentBlock](api/beta.md)> Content

System content blocks to append. Text-only.

required string Text

The text content.

required Type Type

required Type Type



class BetaManagedAgentsDeploymentPausedReason: A class that can be one of several variants.union 

Why a deployment is paused. Non-null exactly when `status` is `paused`.



class BetaManagedAgentsManualDeploymentPausedReason:

The caller invoked the pause endpoint on the deployment.

required Type Type



class BetaManagedAgentsErrorDeploymentPausedReason:

A scheduled fire recorded a failed run whose error auto-pauses the deployment.



required [BetaManagedAgentsDeploymentPausedReasonError](api/beta.md) Error

The error that triggered an auto-pause. Matches the failed run's `error.type`.

One of the following:



class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:

The deployment's environment was archived.

required Type Type



class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:

The deployment's agent was archived.

required Type Type



class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:

The deployment's environment no longer exists.

required Type Type



class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:

A vault referenced by the deployment no longer exists.

required Type Type



class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:

A file resource referenced by the deployment no longer exists.

required Type Type



class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:

A referenced resource no longer exists and its kind was not reported.

required Type Type



class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:

The deployment's workspace was archived.

required Type Type



class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:

The deployment's organization is disabled.

required Type Type



class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:

A memory store referenced by the deployment is archived.

required Type Type



class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:

A skill referenced by the deployment's agent no longer exists.

required Type Type



class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:

A vault referenced by the deployment is archived.

required Type Type



class BetaManagedAgentsUnknownDeploymentPausedReasonError:

An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

required Type Type



class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:

The deployment configures resources, but its environment is self-hosted and cannot mount them.

required Type Type



class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

required Type Type

required Type Type



class BetaManagedAgentsDeploymentPausedReasonError: A class that can be one of several variants.union 

The error that triggered an auto-pause. Matches the failed run's `error.type`.



class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:

The deployment's environment was archived.

required Type Type



class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:

The deployment's agent was archived.

required Type Type



class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:

The deployment's environment no longer exists.

required Type Type



class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:

A vault referenced by the deployment no longer exists.

required Type Type



class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:

A file resource referenced by the deployment no longer exists.

required Type Type



class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:

A referenced resource no longer exists and its kind was not reported.

required Type Type



class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:

The deployment's workspace was archived.

required Type Type



class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:

The deployment's organization is disabled.

required Type Type



class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:

A memory store referenced by the deployment is archived.

required Type Type



class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:

A skill referenced by the deployment's agent no longer exists.

required Type Type



class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:

A vault referenced by the deployment is archived.

required Type Type



class BetaManagedAgentsUnknownDeploymentPausedReasonError:

An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

required Type Type



class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:

The deployment configures resources, but its environment is self-hosted and cannot mount them.

required Type Type



class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

required Type Type



enum BetaManagedAgentsDeploymentStatus:

Lifecycle status of a deployment.

"active"Active

"paused"Paused



class BetaManagedAgentsDeploymentSystemMessageEvent:

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.



required IReadOnlyList<[BetaManagedAgentsSystemContentBlock](api/beta.md)> Content

System content blocks to append. Text-only.

required string Text

The text content.

required Type Type

required Type Type



class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:

An outcome the agent should work toward. The agent begins work on receipt.

required string Description

What the agent should produce. This is the task specification.



required Rubric Rubric

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubric:

Rubric referenced by a file uploaded via the Files API.

required string FileID

ID of the rubric file.

required Type Type



class BetaManagedAgentsTextRubric:

Rubric content provided inline as text.

required string Content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

required Type Type

required Type Type

Int? MaxIterations

Eval→revision cycles before giving up. Default 3, max 20.



class BetaManagedAgentsDeploymentUserMessageEvent:

A user message sent to the session.



required IReadOnlyList<Content> Content

Array of content blocks for the user message.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type



class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:

The deployment's environment was archived.

required Type Type



class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:

The deployment's environment no longer exists.

required Type Type



class BetaManagedAgentsErrorDeploymentPausedReason:

A scheduled fire recorded a failed run whose error auto-pauses the deployment.



required [BetaManagedAgentsDeploymentPausedReasonError](api/beta.md) Error

The error that triggered an auto-pause. Matches the failed run's `error.type`.

One of the following:



class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:

The deployment's environment was archived.

required Type Type



class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:

The deployment's agent was archived.

required Type Type



class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:

The deployment's environment no longer exists.

required Type Type



class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:

A vault referenced by the deployment no longer exists.

required Type Type



class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:

A file resource referenced by the deployment no longer exists.

required Type Type



class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:

A referenced resource no longer exists and its kind was not reported.

required Type Type



class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:

The deployment's workspace was archived.

required Type Type



class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:

The deployment's organization is disabled.

required Type Type



class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:

A memory store referenced by the deployment is archived.

required Type Type



class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:

A skill referenced by the deployment's agent no longer exists.

required Type Type



class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:

A vault referenced by the deployment is archived.

required Type Type



class BetaManagedAgentsUnknownDeploymentPausedReasonError:

An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

required Type Type



class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:

The deployment configures resources, but its environment is self-hosted and cannot mount them.

required Type Type



class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

required Type Type

required Type Type



class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:

A file resource referenced by the deployment no longer exists.

required Type Type



class BetaManagedAgentsFileResourceConfig:

A file mounted into each session's container.

required string FileID

ID of a previously uploaded file.

required Type Type

string? MountPath

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.



class BetaManagedAgentsGitHubRepositoryResourceConfig:

A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

required Type Type

required string Url

Github URL of the repository



Checkout? Checkout

Branch or commit to check out. Defaults to the repository's default branch.

One of the following:



class BetaManagedAgentsBranchCheckout:

required string Name

Branch name to check out.

required Type Type



class BetaManagedAgentsCommitCheckout:

required string Sha

Full commit SHA to check out.

required Type Type

string? MountPath

Mount path in the container. Defaults to `/workspace/<repo-name>`.



class BetaManagedAgentsManualDeploymentPausedReason:

The caller invoked the pause endpoint on the deployment.

required Type Type



class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

required Type Type



class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:

A memory store referenced by the deployment is archived.

required Type Type



class BetaManagedAgentsMemoryStoreResourceConfig:

A memory store attached to each session created from this deployment.

required string MemoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

required Type Type



Access? Access

Access mode for an attached memory store.

One of the following:

"read\_write"ReadWrite

"read\_only"ReadOnly

string? Instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.



class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:

The deployment's organization is disabled.

required Type Type



class BetaManagedAgentsSchedule:

5-field POSIX cron schedule with computed runtime timestamps.

required string Expression

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

required string Timezone

IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC").

required Type Type

DateTimeOffset? LastRunAt

A timestamp in RFC 3339 format

IReadOnlyList<DateTimeOffset> UpcomingRunsAt

Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.



class BetaManagedAgentsScheduleParams:

5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

required string Expression

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

required string Timezone

Required. IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC"). Validated against the IANA timezone database.

required Type Type



class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:

The deployment configures resources, but its environment is self-hosted and cannot mount them.

required Type Type



class BetaManagedAgentsSessionResourceConfig: A class that can be one of several variants.union 

A configured session resource. Echoes the input minus write-only credentials.



class BetaManagedAgentsGitHubRepositoryResourceConfig:

A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

required Type Type

required string Url

Github URL of the repository



Checkout? Checkout

Branch or commit to check out. Defaults to the repository's default branch.

One of the following:



class BetaManagedAgentsBranchCheckout:

required string Name

Branch name to check out.

required Type Type



class BetaManagedAgentsCommitCheckout:

required string Sha

Full commit SHA to check out.

required Type Type

string? MountPath

Mount path in the container. Defaults to `/workspace/<repo-name>`.



class BetaManagedAgentsFileResourceConfig:

A file mounted into each session's container.

required string FileID

ID of a previously uploaded file.

required Type Type

string? MountPath

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.



class BetaManagedAgentsMemoryStoreResourceConfig:

A memory store attached to each session created from this deployment.

required string MemoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

required Type Type



Access? Access

Access mode for an attached memory store.

One of the following:

"read\_write"ReadWrite

"read\_only"ReadOnly

string? Instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.



class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:

A referenced resource no longer exists and its kind was not reported.

required Type Type



class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:

A skill referenced by the deployment's agent no longer exists.

required Type Type



class BetaManagedAgentsUnknownDeploymentPausedReasonError:

An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

required Type Type



class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:

A vault referenced by the deployment is archived.

required Type Type



class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:

A vault referenced by the deployment no longer exists.

required Type Type



class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:

The deployment's workspace was archived.

required Type Type

---

*Copyright © Anthropic. All rights reserved.*
