# Deployments

Copy page



Python

# Deployments

##### [Create Deployment](api/beta/deployments/create.md)

beta.deployments.create(DeploymentCreateParams\*\*kwargs)  -> [BetaManagedAgentsDeployment](api/beta.md)

POST/v1/deployments

##### [List Deployments](api/beta/deployments/list.md)

beta.deployments.list(DeploymentListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsDeployment](api/beta.md)]

GET/v1/deployments

##### [Get Deployment](api/beta/deployments/retrieve.md)

beta.deployments.retrieve(strdeployment\_id, DeploymentRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsDeployment](api/beta.md)

GET/v1/deployments/{deployment\_id}

##### [Update Deployment](api/beta/deployments/update.md)

beta.deployments.update(strdeployment\_id, DeploymentUpdateParams\*\*kwargs)  -> [BetaManagedAgentsDeployment](api/beta.md)

POST/v1/deployments/{deployment\_id}

##### [Archive Deployment](api/beta/deployments/archive.md)

beta.deployments.archive(strdeployment\_id, DeploymentArchiveParams\*\*kwargs)  -> [BetaManagedAgentsDeployment](api/beta.md)

POST/v1/deployments/{deployment\_id}/archive

##### [Run Deployment Now](api/beta/deployments/run.md)

beta.deployments.run(strdeployment\_id, DeploymentRunParams\*\*kwargs)  -> [BetaManagedAgentsDeploymentRun](api/beta.md)

POST/v1/deployments/{deployment\_id}/run

##### [Pause Deployment](api/beta/deployments/pause.md)

beta.deployments.pause(strdeployment\_id, DeploymentPauseParams\*\*kwargs)  -> [BetaManagedAgentsDeployment](api/beta.md)

POST/v1/deployments/{deployment\_id}/pause

##### [Unpause Deployment](api/beta/deployments/unpause.md)

beta.deployments.unpause(strdeployment\_id, DeploymentUnpauseParams\*\*kwargs)  -> [BetaManagedAgentsDeployment](api/beta.md)

POST/v1/deployments/{deployment\_id}/unpause

##### ModelsExpand Collapse



class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …

The deployment's agent was archived.

type: Literal["agent\_archived\_error"]



class BetaManagedAgentsCronSchedule: …

5-field POSIX cron schedule with computed runtime timestamps.

expression: str

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

timezone: str

IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC").

type: Literal["cron"]

last\_run\_at: Optional[datetime]

A timestamp in RFC 3339 format

upcoming\_runs\_at: Optional[List[datetime]]

Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.



class BetaManagedAgentsCronScheduleParams: …

5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

expression: str

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

timezone: str

Required. IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC"). Validated against the IANA timezone database.

type: Literal["cron"]



class BetaManagedAgentsDeployment: …

A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

id: str

Unique identifier for this deployment.



agent: [BetaManagedAgentsAgentReference](api/beta.md)

A resolved agent reference with a concrete version.

id: str

type: Literal["agent"]

version: int

archived\_at: Optional[datetime]

A timestamp in RFC 3339 format

created\_at: datetime

A timestamp in RFC 3339 format

description: Optional[str]

Description of what the deployment does.

environment\_id: str

ID of the `environment` where sessions run.



initial\_events: List[[BetaManagedAgentsDeploymentInitialEvent](api/beta.md)]

Events sent to each session immediately after creation.

One of the following:



class BetaManagedAgentsDeploymentUserMessageEvent: …

A user message sent to the session.



content: List[Content]

Array of content blocks for the user message.

One of the following:



class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]



class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.



source: Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]



class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.



class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]



class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]



class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]



class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.

type: Literal["user.message"]



class BetaManagedAgentsDeploymentUserDefineOutcomeEvent: …

An outcome the agent should work toward. The agent begins work on receipt.

description: str

What the agent should produce. This is the task specification.



rubric: Rubric

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubric: …

Rubric referenced by a file uploaded via the Files API.

file\_id: str

ID of the rubric file.

type: Literal["file"]



class BetaManagedAgentsTextRubric: …

Rubric content provided inline as text.

content: str

Rubric content. Plain text or markdown — the grader treats it as freeform text.

type: Literal["text"]

type: Literal["user.define\_outcome"]

max\_iterations: Optional[int]

Eval→revision cycles before giving up. Default 3, max 20.



class BetaManagedAgentsDeploymentSystemMessageEvent: …

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.



content: List[[BetaManagedAgentsSystemContentBlock](api/beta.md)]

System content blocks to append. Text-only.

text: str

The text content.

type: Literal["text"]

type: Literal["system.message"]

metadata: Dict[str, str]

Arbitrary key-value metadata. Maximum 16 pairs.

name: str

Human-readable name.



paused\_reason: Optional[BetaManagedAgentsDeploymentPausedReason]

Why a deployment is paused. Non-null exactly when `status` is `paused`.

One of the following:



class BetaManagedAgentsManualDeploymentPausedReason: …

The caller invoked the pause endpoint on the deployment.

type: Literal["manual"]



class BetaManagedAgentsErrorDeploymentPausedReason: …

A scheduled fire recorded a failed run whose error auto-pauses the deployment.



error: [BetaManagedAgentsDeploymentPausedReasonError](api/beta.md)

The error that triggered an auto-pause. Matches the failed run's `error.type`.

One of the following:



class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …

The deployment's environment was archived.

type: Literal["environment\_archived\_error"]



class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …

The deployment's agent was archived.

type: Literal["agent\_archived\_error"]



class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …

The deployment's environment no longer exists.

type: Literal["environment\_not\_found\_error"]



class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …

A vault referenced by the deployment no longer exists.

type: Literal["vault\_not\_found\_error"]



class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …

A file resource referenced by the deployment no longer exists.

type: Literal["file\_not\_found\_error"]



class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …

A referenced resource no longer exists and its kind was not reported.

type: Literal["session\_resource\_not\_found\_error"]



class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …

The deployment's workspace was archived.

type: Literal["workspace\_archived\_error"]



class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …

The deployment's organization is disabled.

type: Literal["organization\_disabled\_error"]



class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …

A memory store referenced by the deployment is archived.

type: Literal["memory\_store\_archived\_error"]



class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …

A skill referenced by the deployment's agent no longer exists.

type: Literal["skill\_not\_found\_error"]



class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …

A vault referenced by the deployment is archived.

type: Literal["vault\_archived\_error"]



class BetaManagedAgentsUnknownDeploymentPausedReasonError: …

An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

type: Literal["unknown\_error"]



class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …

The deployment configures resources, but its environment is self-hosted and cannot mount them.

type: Literal["self\_hosted\_resources\_unsupported\_error"]



class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

type: Literal["mcp\_egress\_blocked\_error"]

type: Literal["error"]



resources: List[[BetaManagedAgentsSessionResourceConfig](api/beta.md)]

Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

One of the following:



class BetaManagedAgentsGitHubRepositoryResourceConfig: …

A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

type: Literal["github\_repository"]

url: str

Github URL of the repository



checkout: Optional[Checkout]

Branch or commit to check out. Defaults to the repository's default branch.

One of the following:



class BetaManagedAgentsBranchCheckout: …

name: str

Branch name to check out.

type: Literal["branch"]



class BetaManagedAgentsCommitCheckout: …

sha: str

Full commit SHA to check out.

type: Literal["commit"]

mount\_path: Optional[str]

Mount path in the container. Defaults to `/workspace/<repo-name>`.



class BetaManagedAgentsFileResourceConfig: …

A file mounted into each session's container.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

mount\_path: Optional[str]

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.



class BetaManagedAgentsMemoryStoreResourceConfig: …

A memory store attached to each session created from this deployment.

memory\_store\_id: str

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: Literal["memory\_store"]



access: Optional[Literal["read\_write", "read\_only"]]

Access mode for an attached memory store.

One of the following:

"read\_write"

"read\_only"

instructions: Optional[str]

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.



schedule: Optional[BetaManagedAgentsSchedule]

5-field POSIX cron schedule with computed runtime timestamps.

expression: str

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

timezone: str

IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC").

type: Literal["cron"]

last\_run\_at: Optional[datetime]

A timestamp in RFC 3339 format

upcoming\_runs\_at: Optional[List[datetime]]

Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.



status: [BetaManagedAgentsDeploymentStatus](api/beta.md)

Lifecycle status of a deployment.

One of the following:

"active"

"paused"

type: Literal["deployment"]

updated\_at: datetime

A timestamp in RFC 3339 format

vault\_ids: List[str]

Vault IDs supplying stored credentials for sessions created from this deployment.



[BetaManagedAgentsDeploymentInitialEvent](api/beta.md)

An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

One of the following:



class BetaManagedAgentsDeploymentUserMessageEvent: …

A user message sent to the session.



content: List[Content]

Array of content blocks for the user message.

One of the following:



class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]



class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.



source: Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]



class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.



class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]



class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]



class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]



class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.

type: Literal["user.message"]



class BetaManagedAgentsDeploymentUserDefineOutcomeEvent: …

An outcome the agent should work toward. The agent begins work on receipt.

description: str

What the agent should produce. This is the task specification.



rubric: Rubric

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubric: …

Rubric referenced by a file uploaded via the Files API.

file\_id: str

ID of the rubric file.

type: Literal["file"]



class BetaManagedAgentsTextRubric: …

Rubric content provided inline as text.

content: str

Rubric content. Plain text or markdown — the grader treats it as freeform text.

type: Literal["text"]

type: Literal["user.define\_outcome"]

max\_iterations: Optional[int]

Eval→revision cycles before giving up. Default 3, max 20.



class BetaManagedAgentsDeploymentSystemMessageEvent: …

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.



content: List[[BetaManagedAgentsSystemContentBlock](api/beta.md)]

System content blocks to append. Text-only.

text: str

The text content.

type: Literal["text"]

type: Literal["system.message"]



[BetaManagedAgentsDeploymentInitialEventParams](api/beta.md)

An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

One of the following:



class BetaManagedAgentsUserMessageEventParams: …

Parameters for sending a user message to the session.



content: List[Content]

Array of content blocks for the user message.

One of the following:



class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]



class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.



source: Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]



class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.



class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]



class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]



class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]



class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.

type: Literal["user.message"]



class BetaManagedAgentsUserDefineOutcomeEventParams: …

Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

description: str

What the agent should produce. This is the task specification.



rubric: Rubric

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubricParams: …

Rubric referenced by a file uploaded via the Files API.

file\_id: str

ID of the rubric file.

type: Literal["file"]



class BetaManagedAgentsTextRubricParams: …

Rubric content provided inline as text.

content: str

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

type: Literal["text"]

type: Literal["user.define\_outcome"]

max\_iterations: Optional[int]

Eval→revision cycles before giving up. Default 3, max 20.



class BetaManagedAgentsSystemMessageEventParams: …

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.



content: List[[BetaManagedAgentsSystemContentBlock](api/beta.md)]

System content blocks to append. Text-only.

text: str

The text content.

type: Literal["text"]

type: Literal["system.message"]



[BetaManagedAgentsDeploymentPausedReason](api/beta.md)

Why a deployment is paused. Non-null exactly when `status` is `paused`.

One of the following:



class BetaManagedAgentsManualDeploymentPausedReason: …

The caller invoked the pause endpoint on the deployment.

type: Literal["manual"]



class BetaManagedAgentsErrorDeploymentPausedReason: …

A scheduled fire recorded a failed run whose error auto-pauses the deployment.



error: [BetaManagedAgentsDeploymentPausedReasonError](api/beta.md)

The error that triggered an auto-pause. Matches the failed run's `error.type`.

One of the following:



class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …

The deployment's environment was archived.

type: Literal["environment\_archived\_error"]



class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …

The deployment's agent was archived.

type: Literal["agent\_archived\_error"]



class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …

The deployment's environment no longer exists.

type: Literal["environment\_not\_found\_error"]



class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …

A vault referenced by the deployment no longer exists.

type: Literal["vault\_not\_found\_error"]



class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …

A file resource referenced by the deployment no longer exists.

type: Literal["file\_not\_found\_error"]



class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …

A referenced resource no longer exists and its kind was not reported.

type: Literal["session\_resource\_not\_found\_error"]



class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …

The deployment's workspace was archived.

type: Literal["workspace\_archived\_error"]



class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …

The deployment's organization is disabled.

type: Literal["organization\_disabled\_error"]



class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …

A memory store referenced by the deployment is archived.

type: Literal["memory\_store\_archived\_error"]



class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …

A skill referenced by the deployment's agent no longer exists.

type: Literal["skill\_not\_found\_error"]



class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …

A vault referenced by the deployment is archived.

type: Literal["vault\_archived\_error"]



class BetaManagedAgentsUnknownDeploymentPausedReasonError: …

An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

type: Literal["unknown\_error"]



class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …

The deployment configures resources, but its environment is self-hosted and cannot mount them.

type: Literal["self\_hosted\_resources\_unsupported\_error"]



class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

type: Literal["mcp\_egress\_blocked\_error"]

type: Literal["error"]



[BetaManagedAgentsDeploymentPausedReasonError](api/beta.md)

The error that triggered an auto-pause. Matches the failed run's `error.type`.

One of the following:



class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …

The deployment's environment was archived.

type: Literal["environment\_archived\_error"]



class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …

The deployment's agent was archived.

type: Literal["agent\_archived\_error"]



class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …

The deployment's environment no longer exists.

type: Literal["environment\_not\_found\_error"]



class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …

A vault referenced by the deployment no longer exists.

type: Literal["vault\_not\_found\_error"]



class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …

A file resource referenced by the deployment no longer exists.

type: Literal["file\_not\_found\_error"]



class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …

A referenced resource no longer exists and its kind was not reported.

type: Literal["session\_resource\_not\_found\_error"]



class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …

The deployment's workspace was archived.

type: Literal["workspace\_archived\_error"]



class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …

The deployment's organization is disabled.

type: Literal["organization\_disabled\_error"]



class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …

A memory store referenced by the deployment is archived.

type: Literal["memory\_store\_archived\_error"]



class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …

A skill referenced by the deployment's agent no longer exists.

type: Literal["skill\_not\_found\_error"]



class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …

A vault referenced by the deployment is archived.

type: Literal["vault\_archived\_error"]



class BetaManagedAgentsUnknownDeploymentPausedReasonError: …

An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

type: Literal["unknown\_error"]



class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …

The deployment configures resources, but its environment is self-hosted and cannot mount them.

type: Literal["self\_hosted\_resources\_unsupported\_error"]



class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

type: Literal["mcp\_egress\_blocked\_error"]



Literal["active", "paused"]

Lifecycle status of a deployment.

One of the following:

"active"

"paused"



class BetaManagedAgentsDeploymentSystemMessageEvent: …

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.



content: List[[BetaManagedAgentsSystemContentBlock](api/beta.md)]

System content blocks to append. Text-only.

text: str

The text content.

type: Literal["text"]

type: Literal["system.message"]



class BetaManagedAgentsDeploymentUserDefineOutcomeEvent: …

An outcome the agent should work toward. The agent begins work on receipt.

description: str

What the agent should produce. This is the task specification.



rubric: Rubric

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubric: …

Rubric referenced by a file uploaded via the Files API.

file\_id: str

ID of the rubric file.

type: Literal["file"]



class BetaManagedAgentsTextRubric: …

Rubric content provided inline as text.

content: str

Rubric content. Plain text or markdown — the grader treats it as freeform text.

type: Literal["text"]

type: Literal["user.define\_outcome"]

max\_iterations: Optional[int]

Eval→revision cycles before giving up. Default 3, max 20.



class BetaManagedAgentsDeploymentUserMessageEvent: …

A user message sent to the session.



content: List[Content]

Array of content blocks for the user message.

One of the following:



class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]



class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.



source: Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]



class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.



class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]



class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]



class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]



class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.

type: Literal["user.message"]



class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …

The deployment's environment was archived.

type: Literal["environment\_archived\_error"]



class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …

The deployment's environment no longer exists.

type: Literal["environment\_not\_found\_error"]



class BetaManagedAgentsErrorDeploymentPausedReason: …

A scheduled fire recorded a failed run whose error auto-pauses the deployment.



error: [BetaManagedAgentsDeploymentPausedReasonError](api/beta.md)

The error that triggered an auto-pause. Matches the failed run's `error.type`.

One of the following:



class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …

The deployment's environment was archived.

type: Literal["environment\_archived\_error"]



class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …

The deployment's agent was archived.

type: Literal["agent\_archived\_error"]



class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …

The deployment's environment no longer exists.

type: Literal["environment\_not\_found\_error"]



class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …

A vault referenced by the deployment no longer exists.

type: Literal["vault\_not\_found\_error"]



class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …

A file resource referenced by the deployment no longer exists.

type: Literal["file\_not\_found\_error"]



class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …

A referenced resource no longer exists and its kind was not reported.

type: Literal["session\_resource\_not\_found\_error"]



class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …

The deployment's workspace was archived.

type: Literal["workspace\_archived\_error"]



class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …

The deployment's organization is disabled.

type: Literal["organization\_disabled\_error"]



class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …

A memory store referenced by the deployment is archived.

type: Literal["memory\_store\_archived\_error"]



class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …

A skill referenced by the deployment's agent no longer exists.

type: Literal["skill\_not\_found\_error"]



class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …

A vault referenced by the deployment is archived.

type: Literal["vault\_archived\_error"]



class BetaManagedAgentsUnknownDeploymentPausedReasonError: …

An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

type: Literal["unknown\_error"]



class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …

The deployment configures resources, but its environment is self-hosted and cannot mount them.

type: Literal["self\_hosted\_resources\_unsupported\_error"]



class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

type: Literal["mcp\_egress\_blocked\_error"]

type: Literal["error"]



class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …

A file resource referenced by the deployment no longer exists.

type: Literal["file\_not\_found\_error"]



class BetaManagedAgentsFileResourceConfig: …

A file mounted into each session's container.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

mount\_path: Optional[str]

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.



class BetaManagedAgentsGitHubRepositoryResourceConfig: …

A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

type: Literal["github\_repository"]

url: str

Github URL of the repository



checkout: Optional[Checkout]

Branch or commit to check out. Defaults to the repository's default branch.

One of the following:



class BetaManagedAgentsBranchCheckout: …

name: str

Branch name to check out.

type: Literal["branch"]



class BetaManagedAgentsCommitCheckout: …

sha: str

Full commit SHA to check out.

type: Literal["commit"]

mount\_path: Optional[str]

Mount path in the container. Defaults to `/workspace/<repo-name>`.



class BetaManagedAgentsManualDeploymentPausedReason: …

The caller invoked the pause endpoint on the deployment.

type: Literal["manual"]



class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

type: Literal["mcp\_egress\_blocked\_error"]



class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …

A memory store referenced by the deployment is archived.

type: Literal["memory\_store\_archived\_error"]



class BetaManagedAgentsMemoryStoreResourceConfig: …

A memory store attached to each session created from this deployment.

memory\_store\_id: str

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: Literal["memory\_store"]



access: Optional[Literal["read\_write", "read\_only"]]

Access mode for an attached memory store.

One of the following:

"read\_write"

"read\_only"

instructions: Optional[str]

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.



class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …

The deployment's organization is disabled.

type: Literal["organization\_disabled\_error"]



class BetaManagedAgentsSchedule: …

5-field POSIX cron schedule with computed runtime timestamps.

expression: str

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

timezone: str

IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC").

type: Literal["cron"]

last\_run\_at: Optional[datetime]

A timestamp in RFC 3339 format

upcoming\_runs\_at: Optional[List[datetime]]

Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.



class BetaManagedAgentsScheduleParams: …

5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

expression: str

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

timezone: str

Required. IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC"). Validated against the IANA timezone database.

type: Literal["cron"]



class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …

The deployment configures resources, but its environment is self-hosted and cannot mount them.

type: Literal["self\_hosted\_resources\_unsupported\_error"]



[BetaManagedAgentsSessionResourceConfig](api/beta.md)

A configured session resource. Echoes the input minus write-only credentials.

One of the following:



class BetaManagedAgentsGitHubRepositoryResourceConfig: …

A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

type: Literal["github\_repository"]

url: str

Github URL of the repository



checkout: Optional[Checkout]

Branch or commit to check out. Defaults to the repository's default branch.

One of the following:



class BetaManagedAgentsBranchCheckout: …

name: str

Branch name to check out.

type: Literal["branch"]



class BetaManagedAgentsCommitCheckout: …

sha: str

Full commit SHA to check out.

type: Literal["commit"]

mount\_path: Optional[str]

Mount path in the container. Defaults to `/workspace/<repo-name>`.



class BetaManagedAgentsFileResourceConfig: …

A file mounted into each session's container.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

mount\_path: Optional[str]

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.



class BetaManagedAgentsMemoryStoreResourceConfig: …

A memory store attached to each session created from this deployment.

memory\_store\_id: str

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: Literal["memory\_store"]



access: Optional[Literal["read\_write", "read\_only"]]

Access mode for an attached memory store.

One of the following:

"read\_write"

"read\_only"

instructions: Optional[str]

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.



class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …

A referenced resource no longer exists and its kind was not reported.

type: Literal["session\_resource\_not\_found\_error"]



class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …

A skill referenced by the deployment's agent no longer exists.

type: Literal["skill\_not\_found\_error"]



class BetaManagedAgentsUnknownDeploymentPausedReasonError: …

An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

type: Literal["unknown\_error"]



class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …

A vault referenced by the deployment is archived.

type: Literal["vault\_archived\_error"]



class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …

A vault referenced by the deployment no longer exists.

type: Literal["vault\_not\_found\_error"]



class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …

The deployment's workspace was archived.

type: Literal["workspace\_archived\_error"]

---

*Copyright © Anthropic. All rights reserved.*
