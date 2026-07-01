# Pause Deployment

Copy page



TypeScript

# Pause Deployment

client.beta.deployments.pause(stringdeploymentID, DeploymentPauseParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsDeployment](api/beta/deployments.md) { id, agent, archived\_at, 13 more }

POST/v1/deployments/{deployment\_id}/pause

Pause Deployment

##### ParametersExpand Collapse

deploymentID: string



params: DeploymentPauseParams { betas } 



betas?: Array<[AnthropicBeta](api/beta.md)>

Optional header to specify the beta version(s) you want to use.

One of the following:

(string & {})



"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 25 more

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

BetaManagedAgentsDeployment { id, agent, archived\_at, 13 more } 

A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

id: string

Unique identifier for this deployment.



agent: [BetaManagedAgentsAgentReference](api/beta/agents.md) { id, type, version } 

A resolved agent reference with a concrete version.

id: string

type: "agent"

version: number

archived\_at: string | null

A timestamp in RFC 3339 format

created\_at: string

A timestamp in RFC 3339 format

description: string | null

Description of what the deployment does.

environment\_id: string

ID of the `environment` where sessions run.



initial\_events: Array<[BetaManagedAgentsDeploymentInitialEvent](api/beta/deployments.md)>

Events sent to each session immediately after creation.

One of the following:



BetaManagedAgentsDeploymentUserMessageEvent { content, type } 

A user message sent to the session.



content: Array<[BetaManagedAgentsTextBlock](api/beta/sessions/events.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta/sessions/events.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta/sessions/events.md) { source, type, context, title } >

Array of content blocks for the user message.

One of the following:



BetaManagedAgentsTextBlock { text, type } 

Regular text content.

text: string

The text content.

type: "text"



BetaManagedAgentsImageBlock { source, type } 

Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](api/beta/sessions/events.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta/sessions/events.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for image source variants.

One of the following:



BetaManagedAgentsBase64ImageSource { data, media\_type, type } 

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"



BetaManagedAgentsURLImageSource { type, url } 

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.



BetaManagedAgentsFileImageSource { file\_id, type } 

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"



BetaManagedAgentsDocumentBlock { source, type, context, title } 

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta/sessions/events.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta/sessions/events.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta/sessions/events.md) { file\_id, type } 

Union type for document source variants.

One of the following:



BetaManagedAgentsBase64DocumentSource { data, media\_type, type } 

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"



BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type } 

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"



BetaManagedAgentsURLDocumentSource { type, url } 

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.



BetaManagedAgentsFileDocumentSource { file\_id, type } 

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context?: string | null

Additional context about the document for the model.

title?: string | null

The title of the document.

type: "user.message"



BetaManagedAgentsDeploymentUserDefineOutcomeEvent { description, rubric, type, max\_iterations } 

An outcome the agent should work toward. The agent begins work on receipt.

description: string

What the agent should produce. This is the task specification.



rubric: [BetaManagedAgentsFileRubric](api/beta/sessions/events.md) { file\_id, type }  | [BetaManagedAgentsTextRubric](api/beta/sessions/events.md) { content, type } 

Rubric for grading the quality of an outcome.

One of the following:



BetaManagedAgentsFileRubric { file\_id, type } 

Rubric referenced by a file uploaded via the Files API.

file\_id: string

ID of the rubric file.

type: "file"



BetaManagedAgentsTextRubric { content, type } 

Rubric content provided inline as text.

content: string

Rubric content. Plain text or markdown — the grader treats it as freeform text.

type: "text"

type: "user.define\_outcome"

max\_iterations?: number | null

Eval→revision cycles before giving up. Default 3, max 20.



BetaManagedAgentsDeploymentSystemMessageEvent { content, type } 

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.



content: Array<[BetaManagedAgentsSystemContentBlock](api/beta/sessions.md) { text, type } >

System content blocks to append. Text-only.

text: string

The text content.

type: "text"

type: "system.message"

metadata: Record<string, string>

Arbitrary key-value metadata. Maximum 16 pairs.

name: string

Human-readable name.



paused\_reason: [BetaManagedAgentsDeploymentPausedReason](api/beta/deployments.md) | null

Why a deployment is paused. Non-null exactly when `status` is `paused`.

One of the following:



BetaManagedAgentsManualDeploymentPausedReason { type } 

The caller invoked the pause endpoint on the deployment.

type: "manual"



BetaManagedAgentsErrorDeploymentPausedReason { error, type } 

A scheduled fire recorded a failed run whose error auto-pauses the deployment.



error: [BetaManagedAgentsDeploymentPausedReasonError](api/beta/deployments.md)

The error that triggered an auto-pause. Matches the failed run's `error.type`.

One of the following:



BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError { type } 

The deployment's environment was archived.

type: "environment\_archived\_error"



BetaManagedAgentsAgentArchivedDeploymentPausedReasonError { type } 

The deployment's agent was archived.

type: "agent\_archived\_error"



BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError { type } 

The deployment's environment no longer exists.

type: "environment\_not\_found\_error"



BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError { type } 

A vault referenced by the deployment no longer exists.

type: "vault\_not\_found\_error"



BetaManagedAgentsFileNotFoundDeploymentPausedReasonError { type } 

A file resource referenced by the deployment no longer exists.

type: "file\_not\_found\_error"



BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError { type } 

A referenced resource no longer exists and its kind was not reported.

type: "session\_resource\_not\_found\_error"



BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError { type } 

The deployment's workspace was archived.

type: "workspace\_archived\_error"



BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError { type } 

The deployment's organization is disabled.

type: "organization\_disabled\_error"



BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError { type } 

A memory store referenced by the deployment is archived.

type: "memory\_store\_archived\_error"



BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError { type } 

A skill referenced by the deployment's agent no longer exists.

type: "skill\_not\_found\_error"



BetaManagedAgentsVaultArchivedDeploymentPausedReasonError { type } 

A vault referenced by the deployment is archived.

type: "vault\_archived\_error"



BetaManagedAgentsUnknownDeploymentPausedReasonError { type } 

An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

type: "unknown\_error"



BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError { type } 

The deployment configures resources, but its environment is self-hosted and cannot mount them.

type: "self\_hosted\_resources\_unsupported\_error"



BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError { type } 

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

type: "mcp\_egress\_blocked\_error"

type: "error"



resources: Array<[BetaManagedAgentsSessionResourceConfig](api/beta/deployments.md)>

Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

One of the following:



BetaManagedAgentsGitHubRepositoryResourceConfig { type, url, checkout, mount\_path } 

A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

type: "github\_repository"

url: string

Github URL of the repository



checkout?: [BetaManagedAgentsBranchCheckout](api/beta/sessions.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta/sessions.md) { sha, type }  | null

Branch or commit to check out. Defaults to the repository's default branch.

One of the following:



BetaManagedAgentsBranchCheckout { name, type } 

name: string

Branch name to check out.

type: "branch"



BetaManagedAgentsCommitCheckout { sha, type } 

sha: string

Full commit SHA to check out.

type: "commit"

mount\_path?: string | null

Mount path in the container. Defaults to `/workspace/<repo-name>`.



BetaManagedAgentsFileResourceConfig { file\_id, type, mount\_path } 

A file mounted into each session's container.

file\_id: string

ID of a previously uploaded file.

type: "file"

mount\_path?: string | null

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.



BetaManagedAgentsMemoryStoreResourceConfig { memory\_store\_id, type, access, instructions } 

A memory store attached to each session created from this deployment.

memory\_store\_id: string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: "memory\_store"



access?: "read\_write" | "read\_only" | null

Access mode for an attached memory store.

One of the following:

"read\_write"

"read\_only"

instructions?: string | null

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.



schedule: [BetaManagedAgentsSchedule](api/beta/deployments.md) { expression, timezone, type, 2 more }  | null

5-field POSIX cron schedule with computed runtime timestamps.

expression: string

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

timezone: string

IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC").

type: "cron"

last\_run\_at?: string | null

A timestamp in RFC 3339 format

upcoming\_runs\_at?: Array<string>

Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.



status: [BetaManagedAgentsDeploymentStatus](api/beta/deployments.md)

Lifecycle status of a deployment.

One of the following:

"active"

"paused"

type: "deployment"

updated\_at: string

A timestamp in RFC 3339 format

vault\_ids: Array<string>

Vault IDs supplying stored credentials for sessions created from this deployment.

Pause Deployment

TypeScript

```shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsDeployment = await client.beta.deployments.pause(
  'depl_011CZkZcDH3vPqd7xnEfwTai',
);

console.log(betaManagedAgentsDeployment.id);
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
