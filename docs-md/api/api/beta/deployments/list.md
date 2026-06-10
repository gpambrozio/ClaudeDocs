# List Deployments

Copy page

SDK language

cURL

# List Deployments

GET/v1/deployments

List Deployments

##### Query ParametersExpand Collapse

agent\_id: optional string

Filter by agent ID.

"created\_at[gte]": optional string

Return deployments created at or after this time (inclusive).

"created\_at[lte]": optional string

Return deployments created at or before this time (inclusive).

include\_archived: optional boolean

When true, includes archived deployments. Default: false (exclude archived).

limit: optional number

Maximum results per page. Default 20, maximum 100.

page: optional string

Opaque pagination cursor.

status: optional [BetaManagedAgentsDeploymentStatus](api/beta.md)

Filter by status: active or paused. Omit for both. To include archived deployments, use include\_archived instead; the two cannot be combined.

One of the following:

"active"

"paused"

##### Header ParametersExpand Collapse

"anthropic-beta": optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

One of the following:

string

"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more

One of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"fallback-credit-2026-06-01"

##### ReturnsExpand Collapse

data: array of [BetaManagedAgentsDeployment](api/beta.md) { id, agent, archived\_at, 13 more }

List of deployments.

id: string

Unique identifier for this deployment.

agent: [BetaManagedAgentsAgentReference](api/beta.md) { id, type, version }

A resolved agent reference with a concrete version.

id: string

type: "agent"

version: number

archived\_at: string

A timestamp in RFC 3339 format

created\_at: string

A timestamp in RFC 3339 format

description: string

Description of what the deployment does.

environment\_id: string

ID of the `environment` where sessions run.

initial\_events: array of [BetaManagedAgentsDeploymentInitialEvent](api/beta.md)

Events sent to each session immediately after creation.

One of the following:

BetaManagedAgentsDeploymentUserMessageEvent object { content, type }

A user message sent to the session.

content: array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

Array of content blocks for the user message.

One of the following:

BetaManagedAgentsTextBlock object { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

One of the following:

BetaManagedAgentsBase64ImageSource object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource object { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

One of the following:

BetaManagedAgentsBase64DocumentSource object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource object { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

type: "user.message"

BetaManagedAgentsDeploymentUserDefineOutcomeEvent object { description, rubric, type, max\_iterations }

An outcome the agent should work toward. The agent begins work on receipt.

description: string

What the agent should produce. This is the task specification.

rubric: [BetaManagedAgentsFileRubric](api/beta.md) { file\_id, type }  or [BetaManagedAgentsTextRubric](api/beta.md) { content, type }

Rubric for grading the quality of an outcome.

One of the following:

BetaManagedAgentsFileRubric object { file\_id, type }

Rubric referenced by a file uploaded via the Files API.

file\_id: string

ID of the rubric file.

type: "file"

BetaManagedAgentsTextRubric object { content, type }

Rubric content provided inline as text.

content: string

Rubric content. Plain text or markdown — the grader treats it as freeform text.

type: "text"

type: "user.define\_outcome"

max\_iterations: optional number

Eval→revision cycles before giving up. Default 3, max 20.

BetaManagedAgentsDeploymentSystemMessageEvent object { content, type }

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

content: array of [BetaManagedAgentsSystemContentBlock](api/beta.md) { text, type }

System content blocks to append. Text-only.

text: string

The text content.

type: "text"

type: "system.message"

metadata: map[string]

Arbitrary key-value metadata. Maximum 16 pairs.

name: string

Human-readable name.

paused\_reason: [BetaManagedAgentsDeploymentPausedReason](api/beta.md)

Why a deployment is paused. Non-null exactly when `status` is `paused`.

One of the following:

BetaManagedAgentsManualDeploymentPausedReason object { type }

The caller invoked the pause endpoint on the deployment.

type: "manual"

BetaManagedAgentsErrorDeploymentPausedReason object { error, type }

A scheduled fire recorded a failed run whose error auto-pauses the deployment.

error: [BetaManagedAgentsDeploymentPausedReasonError](api/beta.md)

The error that triggered an auto-pause. Matches the failed run's `error.type`.

One of the following:

BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError object { type }

The deployment's environment was archived.

type: "environment\_archived\_error"

BetaManagedAgentsAgentArchivedDeploymentPausedReasonError object { type }

The deployment's agent was archived.

type: "agent\_archived\_error"

BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError object { type }

The deployment's environment no longer exists.

type: "environment\_not\_found\_error"

BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError object { type }

A vault referenced by the deployment no longer exists.

type: "vault\_not\_found\_error"

BetaManagedAgentsFileNotFoundDeploymentPausedReasonError object { type }

A file resource referenced by the deployment no longer exists.

type: "file\_not\_found\_error"

BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError object { type }

A referenced resource no longer exists and its kind was not reported.

type: "session\_resource\_not\_found\_error"

BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError object { type }

The deployment's workspace was archived.

type: "workspace\_archived\_error"

BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError object { type }

The deployment's organization is disabled.

type: "organization\_disabled\_error"

BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError object { type }

A memory store referenced by the deployment is archived.

type: "memory\_store\_archived\_error"

BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError object { type }

A skill referenced by the deployment's agent no longer exists.

type: "skill\_not\_found\_error"

BetaManagedAgentsVaultArchivedDeploymentPausedReasonError object { type }

A vault referenced by the deployment is archived.

type: "vault\_archived\_error"

BetaManagedAgentsUnknownDeploymentPausedReasonError object { type }

An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

type: "unknown\_error"

BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError object { type }

The deployment configures resources, but its environment is self-hosted and cannot mount them.

type: "self\_hosted\_resources\_unsupported\_error"

BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError object { type }

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

type: "mcp\_egress\_blocked\_error"

type: "error"

resources: array of [BetaManagedAgentsSessionResourceConfig](api/beta.md)

Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

One of the following:

BetaManagedAgentsGitHubRepositoryResourceConfig object { type, url, checkout, mount\_path }

A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

type: "github\_repository"

url: string

Github URL of the repository

checkout: optional [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  or [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }

Branch or commit to check out. Defaults to the repository's default branch.

One of the following:

BetaManagedAgentsBranchCheckout object { name, type }

name: string

Branch name to check out.

type: "branch"

BetaManagedAgentsCommitCheckout object { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

mount\_path: optional string

Mount path in the container. Defaults to `/workspace/<repo-name>`.

BetaManagedAgentsFileResourceConfig object { file\_id, type, mount\_path }

A file mounted into each session's container.

file\_id: string

ID of a previously uploaded file.

type: "file"

mount\_path: optional string

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

BetaManagedAgentsMemoryStoreResourceConfig object { memory\_store\_id, type, access, instructions }

A memory store attached to each session created from this deployment.

memory\_store\_id: string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: "memory\_store"

access: optional "read\_write" or "read\_only"

Access mode for an attached memory store.

One of the following:

"read\_write"

"read\_only"

instructions: optional string

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

schedule: [BetaManagedAgentsSchedule](api/beta.md) { expression, timezone, type, 2 more }

5-field POSIX cron schedule with computed runtime timestamps.

expression: string

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

timezone: string

IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC").

type: "cron"

last\_run\_at: optional string

A timestamp in RFC 3339 format

upcoming\_runs\_at: optional array of string

Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

status: [BetaManagedAgentsDeploymentStatus](api/beta.md)

Lifecycle status of a deployment.

One of the following:

"active"

"paused"

type: "deployment"

updated\_at: string

A timestamp in RFC 3339 format

vault\_ids: array of string

Vault IDs supplying stored credentials for sessions created from this deployment.

next\_page: optional string

Opaque cursor for the next page. Null when no more results.

List Deployments

cURL

```shiki
curl https://api.anthropic.com/v1/deployments \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```shiki
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
