# List Deployment Runs

Copy page



C#

# List Deployment Runs

[DeploymentRunListPageResponse](api/beta.md) Beta.DeploymentRuns.List(DeploymentRunListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/deployment\_runs

List Deployment Runs

##### ParametersExpand Collapse



DeploymentRunListParams parameters

DateTimeOffset createdAtGt

Query param: Return runs created strictly after this time (exclusive).

DateTimeOffset createdAtGte

Query param: Return runs created at or after this time (inclusive).

DateTimeOffset createdAtLt

Query param: Return runs created strictly before this time (exclusive).

DateTimeOffset createdAtLte

Query param: Return runs created at or before this time (inclusive).

string deploymentID

Query param: Filter to a specific deployment. Omit to list across all deployments in the workspace. Filtering by a non-existent deployment\_id returns 200 with empty data.

Boolean hasError

Query param: Filter: true for runs with non-null error, false for runs with non-null session\_id. Omit for all.

Int limit

Query param: Maximum results per page. Default 20, maximum 1000.

string page

Query param: Opaque pagination cursor. Pass next\_page from the previous response. Invalid or expired cursors return 400.

[BetaManagedAgentsTriggerType](api/beta.md) triggerType

Query param: Filter runs by what triggered them. Omit to return all runs.



IReadOnlyList<[AnthropicBeta](api/beta.md)> betas

Header param: Optional header to specify the beta version(s) you want to use.

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

##### ReturnsExpand Collapse



class DeploymentRunListPageResponse:

Paginated list of deployment runs. Sorted by created\_at descending (most recent first).



required IReadOnlyList<[BetaManagedAgentsDeploymentRun](api/beta.md)> Data

List of deployment runs.

required string ID

Unique identifier for this run (`drun_...`).



required [BetaManagedAgentsAgentReference](api/beta.md) Agent

A resolved agent reference with a concrete version.

required string ID

required Type Type

required Int Version

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string DeploymentID

ID of the deployment that produced this run.



required Error? Error

Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

One of the following:



class BetaManagedAgentsEnvironmentArchivedRunError:

The deployment's environment was archived.

required string Message

Human-readable error description.

required Type Type



class BetaManagedAgentsAgentArchivedRunError:

The deployment's agent was archived.

required string Message

Human-readable error description.

required Type Type



class BetaManagedAgentsEnvironmentNotFoundRunError:

The deployment's environment no longer exists.

required string Message

Human-readable error description.

required Type Type



class BetaManagedAgentsVaultNotFoundRunError:

A vault referenced by the deployment no longer exists.

required string Message

Human-readable error description.

required Type Type



class BetaManagedAgentsVaultArchivedRunError:

A vault referenced by the deployment is archived.

required string Message

Human-readable error description.

required Type Type



class BetaManagedAgentsFileNotFoundRunError:

A file resource referenced by the deployment no longer exists.

required string Message

Human-readable error description.

required Type Type



class BetaManagedAgentsMemoryStoreArchivedRunError:

A memory store referenced by the deployment is archived.

required string Message

Human-readable error description.

required Type Type



class BetaManagedAgentsSkillNotFoundRunError:

A skill referenced by the deployment's agent no longer exists.

required string Message

Human-readable error description.

required Type Type



class BetaManagedAgentsSessionResourceNotFoundRunError:

A referenced resource no longer exists and its kind was not reported.

required string Message

Human-readable error description.

required Type Type



class BetaManagedAgentsWorkspaceArchivedRunError:

The deployment's workspace was archived.

required string Message

Human-readable error description.

required Type Type



class BetaManagedAgentsOrganizationDisabledRunError:

The deployment's organization is disabled.

required string Message

Human-readable error description.

required Type Type



class BetaManagedAgentsSessionRateLimitedRunError:

Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

required string Message

Human-readable error description.

required Type Type



class BetaManagedAgentsSessionCreationRejectedRunError:

The session create request was rejected with a non-retryable validation error.

required string Message

Human-readable error description.

required Type Type



class BetaManagedAgentsUnknownRunError:

An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

required string Message

Human-readable error description.

required Type Type



class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError:

The deployment configures resources, but its environment is self-hosted and cannot mount them.

required string Message

Human-readable error description.

required Type Type



class BetaManagedAgentsMcpEgressBlockedRunError:

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

required string Message

Human-readable error description.

required Type Type

required string? SessionID

Populated on success. Null on creation failure. Exactly one of session\_id or error is non-null.



required [BetaManagedAgentsTriggerContext](api/beta.md) TriggerContext

Describes what triggered a deployment run, with trigger-specific metadata.

One of the following:



class BetaManagedAgentsScheduleTriggerContext:

The run was fired by the deployment's cron schedule.

required DateTimeOffset ScheduledAt

A timestamp in RFC 3339 format

required Type Type



class BetaManagedAgentsManualTriggerContext:

The run was started manually by creating a session directly against the deployment.

required Type Type

required Type Type

string? NextPage

Opaque cursor for the next page. Null when no more results.

List Deployment Runs

C#

```shiki
DeploymentRunListParams parameters = new();

var page = await client.Beta.DeploymentRuns.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
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
      "created_at": "2019-12-27T18:11:19.117Z",
      "deployment_id": "deployment_id",
      "error": {
        "message": "message",
        "type": "environment_archived_error"
      },
      "session_id": "session_id",
      "trigger_context": {
        "scheduled_at": "2019-12-27T18:11:19.117Z",
        "type": "schedule"
      },
      "type": "deployment_run"
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
      "created_at": "2019-12-27T18:11:19.117Z",
      "deployment_id": "deployment_id",
      "error": {
        "message": "message",
        "type": "environment_archived_error"
      },
      "session_id": "session_id",
      "trigger_context": {
        "scheduled_at": "2019-12-27T18:11:19.117Z",
        "type": "schedule"
      },
      "type": "deployment_run"
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
