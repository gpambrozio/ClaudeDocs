# Update Deployment

Copy page

SDK language

Python

# Update Deployment

beta.deployments.update(strdeployment\_id, DeploymentUpdateParams\*\*kwargs)  -> [BetaManagedAgentsDeployment](api/beta.md)

POST/v1/deployments/{deployment\_id}

Update Deployment

##### ParametersExpand Collapse

deployment\_id: str



agent: Optional[[Agent](api/beta/deployments/update.md)]

Agent to deploy. Accepts the `agent` ID string, which re-pins to the latest version, or an `agent` object with both id and version specified. Omit to preserve. Cannot be cleared.

One of the following:

str



class BetaManagedAgentsAgentParams: …

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: str

The `agent` ID.

type: Literal["agent"]

version: Optional[int]

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

description: Optional[str]

Description. Omit to preserve; send empty string or null to clear.

environment\_id: Optional[str]

ID of the `environment` where sessions run. Omit to preserve. Cannot be cleared.



initial\_events: Optional[Iterable[[BetaManagedAgentsDeploymentInitialEventParams](api/beta.md)]]

Initial events. Full replacement. Omit to preserve. Cannot be cleared. At least 1, maximum 50.

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

metadata: Optional[Dict[str, Optional[str]]]

Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

name: Optional[str]

Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.



resources: Optional[Iterable[Resource]]

Session resources. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 500.

One of the following:



class BetaManagedAgentsGitHubRepositoryResourceParams: …

Mount a GitHub repository into the session's container.

authorization\_token: str

GitHub authorization token used to clone the repository.

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

class BetaManagedAgentsFileResourceParams: …

Mount a file uploaded via the Files API into the session.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

mount\_path: Optional[str]

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.



class BetaManagedAgentsMemoryStoreResourceParam: …

Parameters for attaching a memory store to an agent session.

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

schedule: Optional[BetaManagedAgentsScheduleParams]

5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

expression: str

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

timezone: str

Required. IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC"). Validated against the IANA timezone database.

type: Literal["cron"]

vault\_ids: Optional[Sequence[str]]

Vault IDs. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 50.



betas: Optional[List[[AnthropicBetaParam](api/beta.md)]]

Optional header to specify the beta version(s) you want to use.

One of the following:

str



Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]

One of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"fallback-credit-2026-06-01"

##### ReturnsExpand Collapse

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

Update Deployment

Python

```shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_deployment = client.beta.deployments.update(
    deployment_id="deployment_id",
)
print(beta_managed_agents_deployment.id)
```

Response 200



```shiki
{
  "id": "id",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "type": "agent",
    "version": 1
  },
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "environment_id": "environment_id",
  "initial_events": [
    {
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "x",
    "timezone": "x",
    "type": "cron",
    "last_run_at": "2019-12-27T18:11:19.117Z",
    "upcoming_runs_at": [
      "2019-12-27T18:11:19.117Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "vault_ids": [
    "string"
  ]
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "id",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "type": "agent",
    "version": 1
  },
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "environment_id": "environment_id",
  "initial_events": [
    {
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "x",
    "timezone": "x",
    "type": "cron",
    "last_run_at": "2019-12-27T18:11:19.117Z",
    "upcoming_runs_at": [
      "2019-12-27T18:11:19.117Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "vault_ids": [
    "string"
  ]
}
```

---

*Copyright © Anthropic. All rights reserved.*
