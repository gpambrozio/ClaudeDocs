# Pause Deployment

Copy page

SDK language

Java

# Pause Deployment

[BetaManagedAgentsDeployment](api/beta.md) beta().deployments().pause(DeploymentPauseParamsparams = DeploymentPauseParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/deployments/{deployment\_id}/pause

Pause Deployment

##### ParametersExpand Collapse

DeploymentPauseParams params

Optional<String> deploymentId

Optional<List<AnthropicBeta>> betas

Optional header to specify the beta version(s) you want to use.

MESSAGE\_BATCHES\_2024\_09\_24("message-batches-2024-09-24")

PROMPT\_CACHING\_2024\_07\_31("prompt-caching-2024-07-31")

COMPUTER\_USE\_2024\_10\_22("computer-use-2024-10-22")

COMPUTER\_USE\_2025\_01\_24("computer-use-2025-01-24")

PDFS\_2024\_09\_25("pdfs-2024-09-25")

TOKEN\_COUNTING\_2024\_11\_01("token-counting-2024-11-01")

TOKEN\_EFFICIENT\_TOOLS\_2025\_02\_19("token-efficient-tools-2025-02-19")

OUTPUT\_128K\_2025\_02\_19("output-128k-2025-02-19")

FILES\_API\_2025\_04\_14("files-api-2025-04-14")

MCP\_CLIENT\_2025\_04\_04("mcp-client-2025-04-04")

MCP\_CLIENT\_2025\_11\_20("mcp-client-2025-11-20")

DEV\_FULL\_THINKING\_2025\_05\_14("dev-full-thinking-2025-05-14")

INTERLEAVED\_THINKING\_2025\_05\_14("interleaved-thinking-2025-05-14")

CODE\_EXECUTION\_2025\_05\_22("code-execution-2025-05-22")

EXTENDED\_CACHE\_TTL\_2025\_04\_11("extended-cache-ttl-2025-04-11")

CONTEXT\_1M\_2025\_08\_07("context-1m-2025-08-07")

CONTEXT\_MANAGEMENT\_2025\_06\_27("context-management-2025-06-27")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED\_2025\_08\_26("model-context-window-exceeded-2025-08-26")

SKILLS\_2025\_10\_02("skills-2025-10-02")

FAST\_MODE\_2026\_02\_01("fast-mode-2026-02-01")

OUTPUT\_300K\_2026\_03\_24("output-300k-2026-03-24")

USER\_PROFILES\_2026\_03\_24("user-profiles-2026-03-24")

ADVISOR\_TOOL\_2026\_03\_01("advisor-tool-2026-03-01")

MANAGED\_AGENTS\_2026\_04\_01("managed-agents-2026-04-01")

CACHE\_DIAGNOSIS\_2026\_04\_07("cache-diagnosis-2026-04-07")

THINKING\_TOKEN\_COUNT\_2026\_05\_13("thinking-token-count-2026-05-13")

SERVER\_SIDE\_FALLBACK\_2026\_06\_01("server-side-fallback-2026-06-01")

FALLBACK\_CREDIT\_2026\_06\_01("fallback-credit-2026-06-01")

##### ReturnsExpand Collapse

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

Pause Deployment

Java

```shiki
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.deployments.BetaManagedAgentsDeployment;
import com.anthropic.models.beta.deployments.DeploymentPauseParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsDeployment betaManagedAgentsDeployment = client.beta().deployments().pause("deployment_id");
    }
}
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
