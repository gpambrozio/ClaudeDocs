# Deployments

Copy page

SDK language

Java

# Deployments

##### [Create Deployment](api/beta/deployments/create.md)

[BetaManagedAgentsDeployment](api/beta.md) beta().deployments().create(DeploymentCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/deployments

##### [List Deployments](api/beta/deployments/list.md)

DeploymentListPage beta().deployments().list(DeploymentListParamsparams = DeploymentListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/deployments

##### [Get Deployment](api/beta/deployments/retrieve.md)

[BetaManagedAgentsDeployment](api/beta.md) beta().deployments().retrieve(DeploymentRetrieveParamsparams = DeploymentRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/deployments/{deployment\_id}

##### [Update Deployment](api/beta/deployments/update.md)

[BetaManagedAgentsDeployment](api/beta.md) beta().deployments().update(DeploymentUpdateParamsparams = DeploymentUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/deployments/{deployment\_id}

##### [Archive Deployment](api/beta/deployments/archive.md)

[BetaManagedAgentsDeployment](api/beta.md) beta().deployments().archive(DeploymentArchiveParamsparams = DeploymentArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/deployments/{deployment\_id}/archive

##### [Run Deployment Now](api/beta/deployments/run.md)

[BetaManagedAgentsDeploymentRun](api/beta.md) beta().deployments().run(DeploymentRunParamsparams = DeploymentRunParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/deployments/{deployment\_id}/run

##### [Pause Deployment](api/beta/deployments/pause.md)

[BetaManagedAgentsDeployment](api/beta.md) beta().deployments().pause(DeploymentPauseParamsparams = DeploymentPauseParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/deployments/{deployment\_id}/pause

##### [Unpause Deployment](api/beta/deployments/unpause.md)

[BetaManagedAgentsDeployment](api/beta.md) beta().deployments().unpause(DeploymentUnpauseParamsparams = DeploymentUnpauseParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/deployments/{deployment\_id}/unpause

##### ModelsExpand Collapse

class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:

The deployment's agent was archived.

Type type

class BetaManagedAgentsCronSchedule:

5-field POSIX cron schedule with computed runtime timestamps.

String expression

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

String timezone

IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC").

Type type

Optional<LocalDateTime> lastRunAt

A timestamp in RFC 3339 format

Optional<List<LocalDateTime>> upcomingRunsAt

Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

class BetaManagedAgentsCronScheduleParams:

5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

String expression

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

String timezone

Required. IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC"). Validated against the IANA timezone database.

Type type

class BetaManagedAgentsDeployment:

A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

String id

Unique identifier for this deployment.

[BetaManagedAgentsAgentReference](api/beta.md) agent

A resolved agent reference with a concrete version.

String id

Type type

long version

Optional<LocalDateTime> archivedAt

A timestamp in RFC 3339 format

LocalDateTime createdAt

A timestamp in RFC 3339 format

Optional<String> description

Description of what the deployment does.

String environmentId

ID of the `environment` where sessions run.

List<[BetaManagedAgentsDeploymentInitialEvent](api/beta.md)> initialEvents

Events sent to each session immediately after creation.

One of the following:

class BetaManagedAgentsDeploymentUserMessageEvent:

A user message sent to the session.

List<Content> content

Array of content blocks for the user message.

One of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

One of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

One of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Type type

class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:

An outcome the agent should work toward. The agent begins work on receipt.

String description

What the agent should produce. This is the task specification.

Rubric rubric

Rubric for grading the quality of an outcome.

One of the following:

class BetaManagedAgentsFileRubric:

Rubric referenced by a file uploaded via the Files API.

String fileId

ID of the rubric file.

Type type

class BetaManagedAgentsTextRubric:

Rubric content provided inline as text.

String content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

Type type

Type type

Optional<Long> maxIterations

Eval→revision cycles before giving up. Default 3, max 20.

class BetaManagedAgentsDeploymentSystemMessageEvent:

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

List<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks to append. Text-only.

String text

The text content.

Type type

Type type

Metadata metadata

Arbitrary key-value metadata. Maximum 16 pairs.

String name

Human-readable name.

Optional<[BetaManagedAgentsDeploymentPausedReason](api/beta.md)> pausedReason

Why a deployment is paused. Non-null exactly when `status` is `paused`.

One of the following:

class BetaManagedAgentsManualDeploymentPausedReason:

The caller invoked the pause endpoint on the deployment.

Type type

class BetaManagedAgentsErrorDeploymentPausedReason:

A scheduled fire recorded a failed run whose error auto-pauses the deployment.

[BetaManagedAgentsDeploymentPausedReasonError](api/beta.md) error

The error that triggered an auto-pause. Matches the failed run's `error.type`.

One of the following:

class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:

The deployment's environment was archived.

Type type

class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:

The deployment's agent was archived.

Type type

class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:

The deployment's environment no longer exists.

Type type

class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:

A vault referenced by the deployment no longer exists.

Type type

class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:

A file resource referenced by the deployment no longer exists.

Type type

class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:

A referenced resource no longer exists and its kind was not reported.

Type type

class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:

The deployment's workspace was archived.

Type type

class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:

The deployment's organization is disabled.

Type type

class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:

A memory store referenced by the deployment is archived.

Type type

class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:

A skill referenced by the deployment's agent no longer exists.

Type type

class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:

A vault referenced by the deployment is archived.

Type type

class BetaManagedAgentsUnknownDeploymentPausedReasonError:

An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

Type type

class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:

The deployment configures resources, but its environment is self-hosted and cannot mount them.

Type type

class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

Type type

Type type

List<[BetaManagedAgentsSessionResourceConfig](api/beta.md)> resources

Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

One of the following:

class BetaManagedAgentsGitHubRepositoryResourceConfig:

A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

Type type

String url

Github URL of the repository

Optional<Checkout> checkout

Branch or commit to check out. Defaults to the repository's default branch.

One of the following:

class BetaManagedAgentsBranchCheckout:

String name

Branch name to check out.

Type type

class BetaManagedAgentsCommitCheckout:

String sha

Full commit SHA to check out.

Type type

Optional<String> mountPath

Mount path in the container. Defaults to `/workspace/<repo-name>`.

class BetaManagedAgentsFileResourceConfig:

A file mounted into each session's container.

String fileId

ID of a previously uploaded file.

Type type

Optional<String> mountPath

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

class BetaManagedAgentsMemoryStoreResourceConfig:

A memory store attached to each session created from this deployment.

String memoryStoreId

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type type

Optional<Access> access

Access mode for an attached memory store.

One of the following:

READ\_WRITE("read\_write")

READ\_ONLY("read\_only")

Optional<String> instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

Optional<[BetaManagedAgentsSchedule](api/beta.md)> schedule

5-field POSIX cron schedule with computed runtime timestamps.

String expression

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

String timezone

IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC").

Type type

Optional<LocalDateTime> lastRunAt

A timestamp in RFC 3339 format

Optional<List<LocalDateTime>> upcomingRunsAt

Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

[BetaManagedAgentsDeploymentStatus](api/beta.md) status

Lifecycle status of a deployment.

One of the following:

ACTIVE("active")

PAUSED("paused")

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

List<String> vaultIds

Vault IDs supplying stored credentials for sessions created from this deployment.

class BetaManagedAgentsDeploymentInitialEvent: A class that can be one of several variants.union

An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

class BetaManagedAgentsDeploymentUserMessageEvent:

A user message sent to the session.

List<Content> content

Array of content blocks for the user message.

One of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

One of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

One of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Type type

class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:

An outcome the agent should work toward. The agent begins work on receipt.

String description

What the agent should produce. This is the task specification.

Rubric rubric

Rubric for grading the quality of an outcome.

One of the following:

class BetaManagedAgentsFileRubric:

Rubric referenced by a file uploaded via the Files API.

String fileId

ID of the rubric file.

Type type

class BetaManagedAgentsTextRubric:

Rubric content provided inline as text.

String content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

Type type

Type type

Optional<Long> maxIterations

Eval→revision cycles before giving up. Default 3, max 20.

class BetaManagedAgentsDeploymentSystemMessageEvent:

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

List<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks to append. Text-only.

String text

The text content.

Type type

Type type

class BetaManagedAgentsDeploymentInitialEventParams: A class that can be one of several variants.union

An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

class BetaManagedAgentsUserMessageEventParams:

Parameters for sending a user message to the session.

List<Content> content

Array of content blocks for the user message.

One of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

One of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

One of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Type type

class BetaManagedAgentsUserDefineOutcomeEventParams:

Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

String description

What the agent should produce. This is the task specification.

Rubric rubric

Rubric for grading the quality of an outcome.

One of the following:

class BetaManagedAgentsFileRubricParams:

Rubric referenced by a file uploaded via the Files API.

String fileId

ID of the rubric file.

Type type

class BetaManagedAgentsTextRubricParams:

Rubric content provided inline as text.

String content

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

Type type

Type type

Optional<Long> maxIterations

Eval→revision cycles before giving up. Default 3, max 20.

class BetaManagedAgentsSystemMessageEventParams:

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

List<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks to append. Text-only.

String text

The text content.

Type type

Type type

class BetaManagedAgentsDeploymentPausedReason: A class that can be one of several variants.union

Why a deployment is paused. Non-null exactly when `status` is `paused`.

class BetaManagedAgentsManualDeploymentPausedReason:

The caller invoked the pause endpoint on the deployment.

Type type

class BetaManagedAgentsErrorDeploymentPausedReason:

A scheduled fire recorded a failed run whose error auto-pauses the deployment.

[BetaManagedAgentsDeploymentPausedReasonError](api/beta.md) error

The error that triggered an auto-pause. Matches the failed run's `error.type`.

One of the following:

class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:

The deployment's environment was archived.

Type type

class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:

The deployment's agent was archived.

Type type

class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:

The deployment's environment no longer exists.

Type type

class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:

A vault referenced by the deployment no longer exists.

Type type

class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:

A file resource referenced by the deployment no longer exists.

Type type

class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:

A referenced resource no longer exists and its kind was not reported.

Type type

class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:

The deployment's workspace was archived.

Type type

class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:

The deployment's organization is disabled.

Type type

class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:

A memory store referenced by the deployment is archived.

Type type

class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:

A skill referenced by the deployment's agent no longer exists.

Type type

class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:

A vault referenced by the deployment is archived.

Type type

class BetaManagedAgentsUnknownDeploymentPausedReasonError:

An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

Type type

class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:

The deployment configures resources, but its environment is self-hosted and cannot mount them.

Type type

class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

Type type

Type type

class BetaManagedAgentsDeploymentPausedReasonError: A class that can be one of several variants.union

The error that triggered an auto-pause. Matches the failed run's `error.type`.

class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:

The deployment's environment was archived.

Type type

class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:

The deployment's agent was archived.

Type type

class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:

The deployment's environment no longer exists.

Type type

class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:

A vault referenced by the deployment no longer exists.

Type type

class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:

A file resource referenced by the deployment no longer exists.

Type type

class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:

A referenced resource no longer exists and its kind was not reported.

Type type

class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:

The deployment's workspace was archived.

Type type

class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:

The deployment's organization is disabled.

Type type

class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:

A memory store referenced by the deployment is archived.

Type type

class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:

A skill referenced by the deployment's agent no longer exists.

Type type

class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:

A vault referenced by the deployment is archived.

Type type

class BetaManagedAgentsUnknownDeploymentPausedReasonError:

An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

Type type

class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:

The deployment configures resources, but its environment is self-hosted and cannot mount them.

Type type

class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

Type type

enum BetaManagedAgentsDeploymentStatus:

Lifecycle status of a deployment.

ACTIVE("active")

PAUSED("paused")

class BetaManagedAgentsDeploymentSystemMessageEvent:

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

List<[BetaManagedAgentsSystemContentBlock](api/beta.md)> content

System content blocks to append. Text-only.

String text

The text content.

Type type

Type type

class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:

An outcome the agent should work toward. The agent begins work on receipt.

String description

What the agent should produce. This is the task specification.

Rubric rubric

Rubric for grading the quality of an outcome.

One of the following:

class BetaManagedAgentsFileRubric:

Rubric referenced by a file uploaded via the Files API.

String fileId

ID of the rubric file.

Type type

class BetaManagedAgentsTextRubric:

Rubric content provided inline as text.

String content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

Type type

Type type

Optional<Long> maxIterations

Eval→revision cycles before giving up. Default 3, max 20.

class BetaManagedAgentsDeploymentUserMessageEvent:

A user message sent to the session.

List<Content> content

Array of content blocks for the user message.

One of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

One of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

One of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Type type

class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:

The deployment's environment was archived.

Type type

class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:

The deployment's environment no longer exists.

Type type

class BetaManagedAgentsErrorDeploymentPausedReason:

A scheduled fire recorded a failed run whose error auto-pauses the deployment.

[BetaManagedAgentsDeploymentPausedReasonError](api/beta.md) error

The error that triggered an auto-pause. Matches the failed run's `error.type`.

One of the following:

class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:

The deployment's environment was archived.

Type type

class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:

The deployment's agent was archived.

Type type

class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:

The deployment's environment no longer exists.

Type type

class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:

A vault referenced by the deployment no longer exists.

Type type

class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:

A file resource referenced by the deployment no longer exists.

Type type

class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:

A referenced resource no longer exists and its kind was not reported.

Type type

class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:

The deployment's workspace was archived.

Type type

class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:

The deployment's organization is disabled.

Type type

class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:

A memory store referenced by the deployment is archived.

Type type

class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:

A skill referenced by the deployment's agent no longer exists.

Type type

class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:

A vault referenced by the deployment is archived.

Type type

class BetaManagedAgentsUnknownDeploymentPausedReasonError:

An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

Type type

class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:

The deployment configures resources, but its environment is self-hosted and cannot mount them.

Type type

class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

Type type

Type type

class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:

A file resource referenced by the deployment no longer exists.

Type type

class BetaManagedAgentsFileResourceConfig:

A file mounted into each session's container.

String fileId

ID of a previously uploaded file.

Type type

Optional<String> mountPath

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

class BetaManagedAgentsGitHubRepositoryResourceConfig:

A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

Type type

String url

Github URL of the repository

Optional<Checkout> checkout

Branch or commit to check out. Defaults to the repository's default branch.

One of the following:

class BetaManagedAgentsBranchCheckout:

String name

Branch name to check out.

Type type

class BetaManagedAgentsCommitCheckout:

String sha

Full commit SHA to check out.

Type type

Optional<String> mountPath

Mount path in the container. Defaults to `/workspace/<repo-name>`.

class BetaManagedAgentsManualDeploymentPausedReason:

The caller invoked the pause endpoint on the deployment.

Type type

class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

Type type

class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:

A memory store referenced by the deployment is archived.

Type type

class BetaManagedAgentsMemoryStoreResourceConfig:

A memory store attached to each session created from this deployment.

String memoryStoreId

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type type

Optional<Access> access

Access mode for an attached memory store.

One of the following:

READ\_WRITE("read\_write")

READ\_ONLY("read\_only")

Optional<String> instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:

The deployment's organization is disabled.

Type type

class BetaManagedAgentsSchedule:

5-field POSIX cron schedule with computed runtime timestamps.

String expression

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

String timezone

IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC").

Type type

Optional<LocalDateTime> lastRunAt

A timestamp in RFC 3339 format

Optional<List<LocalDateTime>> upcomingRunsAt

Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

class BetaManagedAgentsScheduleParams:

5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

String expression

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

String timezone

Required. IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC"). Validated against the IANA timezone database.

Type type

class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:

The deployment configures resources, but its environment is self-hosted and cannot mount them.

Type type

class BetaManagedAgentsSessionResourceConfig: A class that can be one of several variants.union

A configured session resource. Echoes the input minus write-only credentials.

class BetaManagedAgentsGitHubRepositoryResourceConfig:

A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

Type type

String url

Github URL of the repository

Optional<Checkout> checkout

Branch or commit to check out. Defaults to the repository's default branch.

One of the following:

class BetaManagedAgentsBranchCheckout:

String name

Branch name to check out.

Type type

class BetaManagedAgentsCommitCheckout:

String sha

Full commit SHA to check out.

Type type

Optional<String> mountPath

Mount path in the container. Defaults to `/workspace/<repo-name>`.

class BetaManagedAgentsFileResourceConfig:

A file mounted into each session's container.

String fileId

ID of a previously uploaded file.

Type type

Optional<String> mountPath

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

class BetaManagedAgentsMemoryStoreResourceConfig:

A memory store attached to each session created from this deployment.

String memoryStoreId

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type type

Optional<Access> access

Access mode for an attached memory store.

One of the following:

READ\_WRITE("read\_write")

READ\_ONLY("read\_only")

Optional<String> instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:

A referenced resource no longer exists and its kind was not reported.

Type type

class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:

A skill referenced by the deployment's agent no longer exists.

Type type

class BetaManagedAgentsUnknownDeploymentPausedReasonError:

An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

Type type

class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:

A vault referenced by the deployment is archived.

Type type

class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:

A vault referenced by the deployment no longer exists.

Type type

class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:

The deployment's workspace was archived.

Type type

---

*Copyright © Anthropic. All rights reserved.*
