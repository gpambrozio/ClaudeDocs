# Deployments

Copy page



cURL

# Deployments

##### [Create Deployment](api/http/beta/deployments/create.md)

POST/v1/deployments

##### [List Deployments](api/http/beta/deployments/list.md)

GET/v1/deployments

##### [Get Deployment](api/http/beta/deployments/retrieve.md)

GET/v1/deployments/{deployment\_id}

##### [Update Deployment](api/http/beta/deployments/update.md)

POST/v1/deployments/{deployment\_id}

##### [Archive Deployment](api/http/beta/deployments/archive.md)

POST/v1/deployments/{deployment\_id}/archive

##### [Run Deployment Now](api/http/beta/deployments/run.md)

POST/v1/deployments/{deployment\_id}/run

##### [Pause Deployment](api/http/beta/deployments/pause.md)

POST/v1/deployments/{deployment\_id}/pause

##### [Unpause Deployment](api/http/beta/deployments/unpause.md)

POST/v1/deployments/{deployment\_id}/unpause

##### Models



BetaManagedAgentsAgentArchivedDeploymentPausedReasonError object{ type }

The deployment's agent was archived.

type: "agent\_archived\_error"



BetaManagedAgentsCronSchedule object{ expression, timezone, type, 2 more }

5-field POSIX cron schedule with computed runtime timestamps.



expression: string

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

minLength1

maxLength256



timezone: string

IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC").

minLength1

type: "cron"



last\_run\_at: optional string or null

A timestamp in RFC 3339 format

formatdate-time

upcoming\_runs\_at: optional array of string

Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.



BetaManagedAgentsCronScheduleParams object{ expression, timezone, type }

5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.



expression: string

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

minLength1

maxLength256



timezone: string

Required. IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC"). Validated against the IANA timezone database.

minLength1

type: "cron"



BetaManagedAgentsDeployment object{ id, agent, archived\_at, 14 more }

A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.



BetaManagedAgentsDeploymentInitialEvent = [BetaManagedAgentsDeploymentUserMessageEvent](api/http/beta/deployments.md) { content, type } or [BetaManagedAgentsDeploymentUserDefineOutcomeEvent](api/http/beta/deployments.md) { description, rubric, type, max\_iterations } or [BetaManagedAgentsDeploymentSystemMessageEvent](api/http/beta/deployments.md) { content, type }

An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

One of the following:



BetaManagedAgentsDeploymentInitialEventParams = [BetaManagedAgentsUserMessageEventParams](api/http/beta/sessions/events.md) { content, type } or [BetaManagedAgentsUserDefineOutcomeEventParams](api/http/beta/sessions/events.md) { description, rubric, type, max\_iterations } or [BetaManagedAgentsSystemMessageEventParams](api/http/beta/sessions/events.md) { content, type }

An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

One of the following:



BetaManagedAgentsDeploymentPausedReason = [BetaManagedAgentsManualDeploymentPausedReason](api/http/beta/deployments.md) { type } or [BetaManagedAgentsErrorDeploymentPausedReason](api/http/beta/deployments.md) { error, type }

Why a deployment is paused. Non-null exactly when `status` is `paused`.

One of the following:



BetaManagedAgentsManualDeploymentPausedReason object{ type }

The caller invoked the pause endpoint on the deployment.

type: "manual"



BetaManagedAgentsErrorDeploymentPausedReason object{ error, type }

A scheduled fire recorded a failed run whose error auto-pauses the deployment.



error: [BetaManagedAgentsDeploymentPausedReasonError](api/http/beta/deployments.md)

The error that triggered an auto-pause. Matches the failed run's `error.type`.

One of the following:

type: "error"



BetaManagedAgentsDeploymentPausedReasonError = [BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError](api/http/beta/deployments.md) { type } or [BetaManagedAgentsAgentArchivedDeploymentPausedReasonError](api/http/beta/deployments.md) { type } or [BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError](api/http/beta/deployments.md) { type } or 11 more

The error that triggered an auto-pause. Matches the failed run's `error.type`.

One of the following:



BetaManagedAgentsDeploymentStatus = "active" or "paused"

Lifecycle status of a deployment.

One of the following:

"active"

"paused"



BetaManagedAgentsDeploymentSystemMessageEvent object{ content, type }

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.



content: array of [BetaManagedAgentsSystemContentBlock](api/http/beta/sessions.md) { text, type }

System content blocks to append. Text-only.



text: string

The text content.

minLength1

type: "text"

type: "system.message"



BetaManagedAgentsDeploymentUserDefineOutcomeEvent object{ description, rubric, type, max\_iterations }

An outcome the agent should work toward. The agent begins work on receipt.



BetaManagedAgentsDeploymentUserMessageEvent object{ content, type }

A user message sent to the session.



BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError object{ type }

The deployment's environment was archived.

type: "environment\_archived\_error"



BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError object{ type }

The deployment's environment no longer exists.

type: "environment\_not\_found\_error"



BetaManagedAgentsErrorDeploymentPausedReason object{ error, type }

A scheduled fire recorded a failed run whose error auto-pauses the deployment.



error: [BetaManagedAgentsDeploymentPausedReasonError](api/http/beta/deployments.md)

The error that triggered an auto-pause. Matches the failed run's `error.type`.

One of the following:

type: "error"



BetaManagedAgentsFileNotFoundDeploymentPausedReasonError object{ type }

A file resource referenced by the deployment no longer exists.

type: "file\_not\_found\_error"



BetaManagedAgentsFileResourceConfig object{ file\_id, type, mount\_path }

A file mounted into each session's container.

file\_id: string

ID of a previously uploaded file.

type: "file"

mount\_path: optional string or null

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.



BetaManagedAgentsGitHubRepositoryResourceConfig object{ type, url, checkout, mount\_path }

A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.



BetaManagedAgentsManualDeploymentPausedReason object{ type }

The caller invoked the pause endpoint on the deployment.

type: "manual"



BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError object{ type }

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

type: "mcp\_egress\_blocked\_error"



BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError object{ type }

A memory store referenced by the deployment is archived.

type: "memory\_store\_archived\_error"



BetaManagedAgentsMemoryStoreResourceConfig object{ memory\_store\_id, type, access, instructions }

A memory store attached to each session created from this deployment.

memory\_store\_id: string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: "memory\_store"



access: optional "read\_write" or "read\_only" or null

Access mode for an attached memory store.

One of the following:

"read\_write"

"read\_only"

instructions: optional string or null

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.



BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError object{ type }

The deployment's organization is disabled.

type: "organization\_disabled\_error"



BetaManagedAgentsSchedule object{ expression, timezone, type, 2 more }

5-field POSIX cron schedule with computed runtime timestamps.



expression: string

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

minLength1

maxLength256



timezone: string

IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC").

minLength1

type: "cron"



last\_run\_at: optional string or null

A timestamp in RFC 3339 format

formatdate-time

upcoming\_runs\_at: optional array of string

Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.



BetaManagedAgentsScheduleParams object{ expression, timezone, type }

5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.



expression: string

5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

minLength1

maxLength256



timezone: string

Required. IANA timezone identifier (e.g., "America/Los\_Angeles", "UTC"). Validated against the IANA timezone database.

minLength1

type: "cron"



BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError object{ type }

The deployment configures resources, but its environment is self-hosted and cannot mount them.

type: "self\_hosted\_resources\_unsupported\_error"



BetaManagedAgentsSessionResourceConfig = [BetaManagedAgentsGitHubRepositoryResourceConfig](api/http/beta/deployments.md) { type, url, checkout, mount\_path } or [BetaManagedAgentsFileResourceConfig](api/http/beta/deployments.md) { file\_id, type, mount\_path } or [BetaManagedAgentsMemoryStoreResourceConfig](api/http/beta/deployments.md) { memory\_store\_id, type, access, instructions }

A configured session resource. Echoes the input minus write-only credentials.

One of the following:



BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError object{ type }

A referenced resource no longer exists and its kind was not reported.

type: "session\_resource\_not\_found\_error"



BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError object{ type }

A skill referenced by the deployment's agent no longer exists.

type: "skill\_not\_found\_error"



BetaManagedAgentsUnknownDeploymentPausedReasonError object{ type }

An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

type: "unknown\_error"



BetaManagedAgentsVaultArchivedDeploymentPausedReasonError object{ type }

A vault referenced by the deployment is archived.

type: "vault\_archived\_error"



BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError object{ type }

A vault referenced by the deployment no longer exists.

type: "vault\_not\_found\_error"



BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError object{ type }

The deployment's workspace was archived.

type: "workspace\_archived\_error"

---

*Copyright © Anthropic. All rights reserved.*
