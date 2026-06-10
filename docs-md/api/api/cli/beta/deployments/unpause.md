# Unpause Deployment

Copy page

SDK language

CLI

# Unpause Deployment

$ ant beta:deployments unpause

POST/v1/deployments/{deployment\_id}/unpause

Unpause Deployment

##### ParametersExpand Collapse

--deployment-id: string

Path parameter deployment\_id

--beta: optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

beta\_managed\_agents\_deployment: object { id, agent, archived\_at, 13 more }

A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

id: string

Unique identifier for this deployment.

agent: object { id, type, version }

A resolved agent reference with a concrete version.

id: string

type: "agent"

"agent"

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

beta\_managed\_agents\_deployment\_user\_message\_event: object { content, type }

A user message sent to the session.

content: array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

Array of content blocks for the user message.

beta\_managed\_agents\_text\_block: object { text, type }

Regular text content.

text: string

The text content.

type: "text"

"text"

beta\_managed\_agents\_image\_block: object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "image"

"image"

beta\_managed\_agents\_document\_block: object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

type: "user.message"

"user.message"

beta\_managed\_agents\_deployment\_user\_define\_outcome\_event: object { description, rubric, type, max\_iterations }

An outcome the agent should work toward. The agent begins work on receipt.

description: string

What the agent should produce. This is the task specification.

rubric: [BetaManagedAgentsFileRubric](api/beta.md) { file\_id, type }  or [BetaManagedAgentsTextRubric](api/beta.md) { content, type }

Rubric for grading the quality of an outcome.

beta\_managed\_agents\_file\_rubric: object { file\_id, type }

Rubric referenced by a file uploaded via the Files API.

file\_id: string

ID of the rubric file.

type: "file"

"file"

beta\_managed\_agents\_text\_rubric: object { content, type }

Rubric content provided inline as text.

content: string

Rubric content. Plain text or markdown — the grader treats it as freeform text.

type: "text"

"text"

type: "user.define\_outcome"

"user.define\_outcome"

max\_iterations: optional number

Eval→revision cycles before giving up. Default 3, max 20.

beta\_managed\_agents\_deployment\_system\_message\_event: object { content, type }

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

content: array of [BetaManagedAgentsSystemContentBlock](api/beta.md) { text, type }

System content blocks to append. Text-only.

text: string

The text content.

type: "text"

"text"

type: "system.message"

"system.message"

metadata: map[string]

Arbitrary key-value metadata. Maximum 16 pairs.

name: string

Human-readable name.

paused\_reason: [BetaManagedAgentsManualDeploymentPausedReason](api/beta.md) { type }  or [BetaManagedAgentsErrorDeploymentPausedReason](api/beta.md) { error, type }

Why a deployment is paused. Non-null exactly when `status` is `paused`.

beta\_managed\_agents\_manual\_deployment\_paused\_reason: object { type }

The caller invoked the pause endpoint on the deployment.

type: "manual"

"manual"

beta\_managed\_agents\_error\_deployment\_paused\_reason: object { error, type }

A scheduled fire recorded a failed run whose error auto-pauses the deployment.

error: [BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError](api/beta.md) { type }  or [BetaManagedAgentsAgentArchivedDeploymentPausedReasonError](api/beta.md) { type }  or [BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError](api/beta.md) { type }  or 11 more

The error that triggered an auto-pause. Matches the failed run's `error.type`.

beta\_managed\_agents\_environment\_archived\_deployment\_paused\_reason\_error: object { type }

The deployment's environment was archived.

type: "environment\_archived\_error"

"environment\_archived\_error"

beta\_managed\_agents\_agent\_archived\_deployment\_paused\_reason\_error: object { type }

The deployment's agent was archived.

type: "agent\_archived\_error"

"agent\_archived\_error"

beta\_managed\_agents\_environment\_not\_found\_deployment\_paused\_reason\_error: object { type }

The deployment's environment no longer exists.

type: "environment\_not\_found\_error"

"environment\_not\_found\_error"

beta\_managed\_agents\_vault\_not\_found\_deployment\_paused\_reason\_error: object { type }

A vault referenced by the deployment no longer exists.

type: "vault\_not\_found\_error"

"vault\_not\_found\_error"

beta\_managed\_agents\_file\_not\_found\_deployment\_paused\_reason\_error: object { type }

A file resource referenced by the deployment no longer exists.

type: "file\_not\_found\_error"

"file\_not\_found\_error"

beta\_managed\_agents\_session\_resource\_not\_found\_deployment\_paused\_reason\_error: object { type }

A referenced resource no longer exists and its kind was not reported.

type: "session\_resource\_not\_found\_error"

"session\_resource\_not\_found\_error"

beta\_managed\_agents\_workspace\_archived\_deployment\_paused\_reason\_error: object { type }

The deployment's workspace was archived.

type: "workspace\_archived\_error"

"workspace\_archived\_error"

beta\_managed\_agents\_organization\_disabled\_deployment\_paused\_reason\_error: object { type }

The deployment's organization is disabled.

type: "organization\_disabled\_error"

"organization\_disabled\_error"

beta\_managed\_agents\_memory\_store\_archived\_deployment\_paused\_reason\_error: object { type }

A memory store referenced by the deployment is archived.

type: "memory\_store\_archived\_error"

"memory\_store\_archived\_error"

beta\_managed\_agents\_skill\_not\_found\_deployment\_paused\_reason\_error: object { type }

A skill referenced by the deployment's agent no longer exists.

type: "skill\_not\_found\_error"

"skill\_not\_found\_error"

beta\_managed\_agents\_vault\_archived\_deployment\_paused\_reason\_error: object { type }

A vault referenced by the deployment is archived.

type: "vault\_archived\_error"

"vault\_archived\_error"

beta\_managed\_agents\_unknown\_deployment\_paused\_reason\_error: object { type }

An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

type: "unknown\_error"

"unknown\_error"

beta\_managed\_agents\_self\_hosted\_resources\_unsupported\_deployment\_paused\_reason\_error: object { type }

The deployment configures resources, but its environment is self-hosted and cannot mount them.

type: "self\_hosted\_resources\_unsupported\_error"

"self\_hosted\_resources\_unsupported\_error"

beta\_managed\_agents\_mcp\_egress\_blocked\_deployment\_paused\_reason\_error: object { type }

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

type: "mcp\_egress\_blocked\_error"

"mcp\_egress\_blocked\_error"

type: "error"

"error"

resources: array of [BetaManagedAgentsSessionResourceConfig](api/beta.md)

Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

beta\_managed\_agents\_github\_repository\_resource\_config: object { type, url, checkout, mount\_path }

A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

type: "github\_repository"

"github\_repository"

url: string

Github URL of the repository

checkout: optional [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  or [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }

Branch or commit to check out. Defaults to the repository's default branch.

beta\_managed\_agents\_branch\_checkout: object { name, type }

name: string

Branch name to check out.

type: "branch"

"branch"

beta\_managed\_agents\_commit\_checkout: object { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

"commit"

mount\_path: optional string

Mount path in the container. Defaults to `/workspace/<repo-name>`.

beta\_managed\_agents\_file\_resource\_config: object { file\_id, type, mount\_path }

A file mounted into each session's container.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

mount\_path: optional string

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

beta\_managed\_agents\_memory\_store\_resource\_config: object { memory\_store\_id, type, access, instructions }

A memory store attached to each session created from this deployment.

memory\_store\_id: string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: "memory\_store"

"memory\_store"

access: optional "read\_write" or "read\_only"

Access mode for an attached memory store.

"read\_write"

"read\_only"

instructions: optional string

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

schedule: object { expression, timezone, type, 2 more }

5-field POSIX cron schedule with computed runtime timestamps.

expression: string

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

timezone: string

IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC").

type: "cron"

"cron"

last\_run\_at: optional string

A timestamp in RFC 3339 format

upcoming\_runs\_at: optional array of string

Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

status: "active" or "paused"

Lifecycle status of a deployment.

"active"

"paused"

type: "deployment"

"deployment"

updated\_at: string

A timestamp in RFC 3339 format

vault\_ids: array of string

Vault IDs supplying stored credentials for sessions created from this deployment.

Unpause Deployment

CLI

```shiki
ant beta:deployments unpause \
  --api-key my-anthropic-api-key \
  --deployment-id deployment_id
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
