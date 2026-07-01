# List Deployments

Copy page



Go

# List Deployments

client.Beta.Deployments.List(ctx, params) (\*PageCursor[[BetaManagedAgentsDeployment](api/beta/deployments.md)], error)

GET/v1/deployments

List Deployments

##### ParametersExpand Collapse



params BetaDeploymentListParams

AgentID param.Field[string]Optional

Query param: Filter by agent ID.

CreatedAtGte param.Field[[Time](api/beta/deployments/list.md)]Optional

Query param: Return deployments created at or after this time (inclusive).

CreatedAtLte param.Field[[Time](api/beta/deployments/list.md)]Optional

Query param: Return deployments created at or before this time (inclusive).

IncludeArchived param.Field[bool]Optional

Query param: When true, includes archived deployments. Default: false (exclude archived).

Limit param.Field[int64]Optional

Query param: Maximum results per page. Default 20, maximum 100.

Page param.Field[string]Optional

Query param: Opaque pagination cursor.

Status param.Field[[BetaManagedAgentsDeploymentStatus](api/beta/deployments.md)]Optional

Query param: Filter by status: active or paused. Omit for both. To include archived deployments, use include\_archived instead; the two cannot be combined.



Betas param.Field[[]AnthropicBeta]Optional

Header param: Optional header to specify the beta version(s) you want to use.

string



type AnthropicBeta string

One of the following:

const AnthropicBetaMessageBatches2024\_09\_24 AnthropicBeta = "message-batches-2024-09-24"

const AnthropicBetaPromptCaching2024\_07\_31 AnthropicBeta = "prompt-caching-2024-07-31"

const AnthropicBetaComputerUse2024\_10\_22 AnthropicBeta = "computer-use-2024-10-22"

const AnthropicBetaComputerUse2025\_01\_24 AnthropicBeta = "computer-use-2025-01-24"

const AnthropicBetaPDFs2024\_09\_25 AnthropicBeta = "pdfs-2024-09-25"

const AnthropicBetaTokenCounting2024\_11\_01 AnthropicBeta = "token-counting-2024-11-01"

const AnthropicBetaTokenEfficientTools2025\_02\_19 AnthropicBeta = "token-efficient-tools-2025-02-19"

const AnthropicBetaOutput128k2025\_02\_19 AnthropicBeta = "output-128k-2025-02-19"

const AnthropicBetaFilesAPI2025\_04\_14 AnthropicBeta = "files-api-2025-04-14"

const AnthropicBetaMCPClient2025\_04\_04 AnthropicBeta = "mcp-client-2025-04-04"

const AnthropicBetaMCPClient2025\_11\_20 AnthropicBeta = "mcp-client-2025-11-20"

const AnthropicBetaDevFullThinking2025\_05\_14 AnthropicBeta = "dev-full-thinking-2025-05-14"

const AnthropicBetaInterleavedThinking2025\_05\_14 AnthropicBeta = "interleaved-thinking-2025-05-14"

const AnthropicBetaCodeExecution2025\_05\_22 AnthropicBeta = "code-execution-2025-05-22"

const AnthropicBetaExtendedCacheTTL2025\_04\_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"

const AnthropicBetaContext1m2025\_08\_07 AnthropicBeta = "context-1m-2025-08-07"

const AnthropicBetaContextManagement2025\_06\_27 AnthropicBeta = "context-management-2025-06-27"

const AnthropicBetaModelContextWindowExceeded2025\_08\_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"

const AnthropicBetaSkills2025\_10\_02 AnthropicBeta = "skills-2025-10-02"

const AnthropicBetaFastMode2026\_02\_01 AnthropicBeta = "fast-mode-2026-02-01"

const AnthropicBetaOutput300k2026\_03\_24 AnthropicBeta = "output-300k-2026-03-24"

const AnthropicBetaUserProfiles2026\_03\_24 AnthropicBeta = "user-profiles-2026-03-24"

const AnthropicBetaAdvisorTool2026\_03\_01 AnthropicBeta = "advisor-tool-2026-03-01"

const AnthropicBetaManagedAgents2026\_04\_01 AnthropicBeta = "managed-agents-2026-04-01"

const AnthropicBetaCacheDiagnosis2026\_04\_07 AnthropicBeta = "cache-diagnosis-2026-04-07"

const AnthropicBetaThinkingTokenCount2026\_05\_13 AnthropicBeta = "thinking-token-count-2026-05-13"

const AnthropicBetaServerSideFallback2026\_06\_01 AnthropicBeta = "server-side-fallback-2026-06-01"

const AnthropicBetaFallbackCredit2026\_06\_01 AnthropicBeta = "fallback-credit-2026-06-01"

##### ReturnsExpand Collapse



type BetaManagedAgentsDeployment struct{…}

A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

ID string

Unique identifier for this deployment.



Agent [BetaManagedAgentsAgentReference](api/beta/agents.md)

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

InitialEvents [][BetaManagedAgentsDeploymentInitialEventUnion](api/beta/deployments.md)

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

Content [][BetaManagedAgentsSystemContentBlock](api/beta/sessions.md)

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

PausedReason [BetaManagedAgentsDeploymentPausedReasonUnion](api/beta/deployments.md)

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

Error [BetaManagedAgentsDeploymentPausedReasonErrorUnion](api/beta/deployments.md)

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

Resources [][BetaManagedAgentsSessionResourceConfigUnion](api/beta/deployments.md)

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

Schedule [BetaManagedAgentsSchedule](api/beta/deployments.md)

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

Status [BetaManagedAgentsDeploymentStatus](api/beta/deployments.md)

Lifecycle status of a deployment.

One of the following:

const BetaManagedAgentsDeploymentStatusActive [BetaManagedAgentsDeploymentStatus](api/beta/deployments.md) = "active"

const BetaManagedAgentsDeploymentStatusPaused [BetaManagedAgentsDeploymentStatus](api/beta/deployments.md) = "paused"

Type BetaManagedAgentsDeploymentType

UpdatedAt Time

A timestamp in RFC 3339 format

VaultIDs []string

Vault IDs supplying stored credentials for sessions created from this deployment.

List Deployments

Go

```shiki
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  page, err := client.Beta.Deployments.List(context.TODO(), anthropic.BetaDeploymentListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

Response 200



```shiki
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

---

*Copyright © Anthropic. All rights reserved.*
