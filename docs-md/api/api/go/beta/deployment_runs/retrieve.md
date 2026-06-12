# Get Deployment Run

Copy page

SDK language

Go

# Get Deployment Run

client.Beta.DeploymentRuns.Get(ctx, deploymentRunID, query) (\*[BetaManagedAgentsDeploymentRun](api/beta.md), error)

GET/v1/deployment\_runs/{deployment\_run\_id}

Get Deployment Run

##### ParametersExpand Collapse

deploymentRunID string



query BetaDeploymentRunGetParams



Betas param.Field[[]AnthropicBeta]Optional

Optional header to specify the beta version(s) you want to use.

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

type BetaManagedAgentsDeploymentRun struct{…}

A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

ID string

Unique identifier for this run (`drun_...`).



Agent [BetaManagedAgentsAgentReference](api/beta.md)

A resolved agent reference with a concrete version.

ID string

Type BetaManagedAgentsAgentReferenceType

Version int64

CreatedAt Time

A timestamp in RFC 3339 format

DeploymentID string

ID of the deployment that produced this run.



Error BetaManagedAgentsDeploymentRunErrorUnion

Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

One of the following:



type BetaManagedAgentsEnvironmentArchivedRunError struct{…}

The deployment's environment was archived.

Message string

Human-readable error description.

Type BetaManagedAgentsEnvironmentArchivedRunErrorType



type BetaManagedAgentsAgentArchivedRunError struct{…}

The deployment's agent was archived.

Message string

Human-readable error description.

Type BetaManagedAgentsAgentArchivedRunErrorType



type BetaManagedAgentsEnvironmentNotFoundRunError struct{…}

The deployment's environment no longer exists.

Message string

Human-readable error description.

Type BetaManagedAgentsEnvironmentNotFoundRunErrorType



type BetaManagedAgentsVaultNotFoundRunError struct{…}

A vault referenced by the deployment no longer exists.

Message string

Human-readable error description.

Type BetaManagedAgentsVaultNotFoundRunErrorType



type BetaManagedAgentsVaultArchivedRunError struct{…}

A vault referenced by the deployment is archived.

Message string

Human-readable error description.

Type BetaManagedAgentsVaultArchivedRunErrorType



type BetaManagedAgentsFileNotFoundRunError struct{…}

A file resource referenced by the deployment no longer exists.

Message string

Human-readable error description.

Type BetaManagedAgentsFileNotFoundRunErrorType



type BetaManagedAgentsMemoryStoreArchivedRunError struct{…}

A memory store referenced by the deployment is archived.

Message string

Human-readable error description.

Type BetaManagedAgentsMemoryStoreArchivedRunErrorType



type BetaManagedAgentsSkillNotFoundRunError struct{…}

A skill referenced by the deployment's agent no longer exists.

Message string

Human-readable error description.

Type BetaManagedAgentsSkillNotFoundRunErrorType



type BetaManagedAgentsSessionResourceNotFoundRunError struct{…}

A referenced resource no longer exists and its kind was not reported.

Message string

Human-readable error description.

Type BetaManagedAgentsSessionResourceNotFoundRunErrorType



type BetaManagedAgentsWorkspaceArchivedRunError struct{…}

The deployment's workspace was archived.

Message string

Human-readable error description.

Type BetaManagedAgentsWorkspaceArchivedRunErrorType



type BetaManagedAgentsOrganizationDisabledRunError struct{…}

The deployment's organization is disabled.

Message string

Human-readable error description.

Type BetaManagedAgentsOrganizationDisabledRunErrorType



type BetaManagedAgentsSessionRateLimitedRunError struct{…}

Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

Message string

Human-readable error description.

Type BetaManagedAgentsSessionRateLimitedRunErrorType



type BetaManagedAgentsSessionCreationRejectedRunError struct{…}

The session create request was rejected with a non-retryable validation error.

Message string

Human-readable error description.

Type BetaManagedAgentsSessionCreationRejectedRunErrorType



type BetaManagedAgentsUnknownRunError struct{…}

An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

Message string

Human-readable error description.

Type BetaManagedAgentsUnknownRunErrorType



type BetaManagedAgentsSelfHostedResourcesUnsupportedRunError struct{…}

The deployment configures resources, but its environment is self-hosted and cannot mount them.

Message string

Human-readable error description.

Type BetaManagedAgentsSelfHostedResourcesUnsupportedRunErrorType



type BetaManagedAgentsMCPEgressBlockedRunError struct{…}

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

Message string

Human-readable error description.

Type BetaManagedAgentsMCPEgressBlockedRunErrorType

SessionID string

Populated on success. Null on creation failure. Exactly one of session\_id or error is non-null.



TriggerContext [BetaManagedAgentsTriggerContextUnion](api/beta.md)

Describes what triggered a deployment run, with trigger-specific metadata.

One of the following:



type BetaManagedAgentsScheduleTriggerContext struct{…}

The run was fired by the deployment's cron schedule.

ScheduledAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsScheduleTriggerContextType



type BetaManagedAgentsManualTriggerContext struct{…}

The run was started manually by creating a session directly against the deployment.

Type BetaManagedAgentsManualTriggerContextType

Type BetaManagedAgentsDeploymentRunType

Get Deployment Run

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
  betaManagedAgentsDeploymentRun, err := client.Beta.DeploymentRuns.Get(
    context.TODO(),
    "deployment_run_id",
    anthropic.BetaDeploymentRunGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsDeploymentRun.ID)
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
```

---

*Copyright © Anthropic. All rights reserved.*
