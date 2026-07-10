# Archive Deployment

Copy page



C#

# Archive Deployment

[BetaManagedAgentsDeployment](api/beta/deployments.md) Beta.Deployments.Archive(DeploymentArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/deployments/{deployment\_id}/archive

Archive Deployment

##### ParametersExpand Collapse



DeploymentArchiveParams parameters

required string deploymentID

Path parameter deployment\_id



IReadOnlyList<[AnthropicBeta](api/beta.md)> betas

Optional header to specify the beta version(s) you want to use.

"message-batches-2024-09-24"MessageBatches2024\_09\_24

"prompt-caching-2024-07-31"PromptCaching2024\_07\_31

"computer-use-2024-10-22"ComputerUse2024\_10\_22

"computer-use-2025-01-24"ComputerUse2025\_01\_24

"pdfs-2024-09-25"Pdfs2024\_09\_25

"token-counting-2024-11-01"TokenCounting2024\_11\_01

"token-efficient-tools-2025-02-19"TokenEfficientTools2025\_02\_19

"output-128k-2025-02-19"Output128k2025\_02\_19

"files-api-2025-04-14"FilesApi2025\_04\_14

"mcp-client-2025-04-04"McpClient2025\_04\_04

"mcp-client-2025-11-20"McpClient2025\_11\_20

"dev-full-thinking-2025-05-14"DevFullThinking2025\_05\_14

"interleaved-thinking-2025-05-14"InterleavedThinking2025\_05\_14

"code-execution-2025-05-22"CodeExecution2025\_05\_22

"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025\_04\_11

"context-1m-2025-08-07"Context1m2025\_08\_07

"context-management-2025-06-27"ContextManagement2025\_06\_27

"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025\_08\_26

"skills-2025-10-02"Skills2025\_10\_02

"fast-mode-2026-02-01"FastMode2026\_02\_01

"output-300k-2026-03-24"Output300k2026\_03\_24

"user-profiles-2026-03-24"UserProfiles2026\_03\_24

"advisor-tool-2026-03-01"AdvisorTool2026\_03\_01

"managed-agents-2026-04-01"ManagedAgents2026\_04\_01

"cache-diagnosis-2026-04-07"CacheDiagnosis2026\_04\_07

"thinking-token-count-2026-05-13"ThinkingTokenCount2026\_05\_13

"server-side-fallback-2026-06-01"ServerSideFallback2026\_06\_01

"fallback-credit-2026-06-01"FallbackCredit2026\_06\_01

"agent-memory-2026-07-22"AgentMemory2026\_07\_22

##### ReturnsExpand Collapse



class BetaManagedAgentsDeployment:

A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

required string ID

Unique identifier for this deployment.



required [BetaManagedAgentsAgentReference](api/beta/agents.md) Agent

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

required IReadOnlyList<[BetaManagedAgentsDeploymentInitialEvent](api/beta/deployments.md)> InitialEvents

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

required IReadOnlyList<[BetaManagedAgentsSystemContentBlock](api/beta/sessions.md)> Content

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

required [BetaManagedAgentsDeploymentPausedReason](api/beta/deployments.md)? PausedReason

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

required [BetaManagedAgentsDeploymentPausedReasonError](api/beta/deployments.md) Error

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

required IReadOnlyList<[BetaManagedAgentsSessionResourceConfig](api/beta/deployments.md)> Resources

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

required [BetaManagedAgentsSchedule](api/beta/deployments.md)? Schedule

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

required [BetaManagedAgentsDeploymentStatus](api/beta/deployments.md) Status

Lifecycle status of a deployment.

One of the following:

"active"Active

"paused"Paused

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required IReadOnlyList<string> VaultIds

Vault IDs supplying stored credentials for sessions created from this deployment.

Archive Deployment

C#

```shiki
DeploymentArchiveParams parameters = new()
{
    DeploymentID = "depl_011CZkZcDH3vPqd7xnEfwTai"
};

var betaManagedAgentsDeployment = await client.Beta.Deployments.Archive(parameters);

Console.WriteLine(betaManagedAgentsDeployment);
```

Response 200



```shiki
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
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
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
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
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

---

*Copyright © Anthropic. All rights reserved.*
