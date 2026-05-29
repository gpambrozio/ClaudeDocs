# Update Work Item

Copy page

Go

# Update Work Item

client.Beta.Environments.Work.Update(ctx, workID, params) (\*[BetaSelfHostedWork](api/beta.md), error)

POST/v1/environments/{environment\_id}/work/{work\_id}

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Update work item metadata with merge semantics.

##### ParametersExpand Collapse

workID string

params BetaEnvironmentWorkUpdateParams

EnvironmentID param.Field[string]

Path param

BetaSelfHostedWorkUpdateRequest param.Field[[BetaSelfHostedWorkUpdateRequest](api/beta.md)]

Body param: Request to update work item metadata.

Betas param.Field[[]AnthropicBeta]Optional

Header param: Optional header to specify the beta version(s) you want to use.

string

type AnthropicBeta string

One of the following:

const AnthropicBetaMessageBatches2024\_09\_24 AnthropicBeta = "message-batches-2024-09-24"

const AnthropicBetaPromptCaching2024\_07\_31 AnthropicBeta = "prompt-caching-2024-07-31"

const AnthropicBetaComputerUse2024\_10\_22 AnthropicBeta = "computer-use-2024-10-22"

const AnthropicBetaComputerUse2025\_01\_24 AnthropicBeta = "computer-use-2025-01-24"

const AnthropicBetaPDFs2024\_09\_25 AnthropicBeta = "pdfs-2024-09-25"

const AnthropicBetaTokenCounting2024\_11\_01 AnthropicBeta = "token-counting-2024-11-01"

const AnthropicBetaTokenEfficientTools2025\_02\_19 AnthropicBeta = "token-efficient-tools-2025-02-19"

const AnthropicBetaOutput128k2025\_02\_19 AnthropicBeta = "output-128k-2025-02-19"

const AnthropicBetaFilesAPI2025\_04\_14 AnthropicBeta = "files-api-2025-04-14"

const AnthropicBetaMCPClient2025\_04\_04 AnthropicBeta = "mcp-client-2025-04-04"

const AnthropicBetaMCPClient2025\_11\_20 AnthropicBeta = "mcp-client-2025-11-20"

const AnthropicBetaDevFullThinking2025\_05\_14 AnthropicBeta = "dev-full-thinking-2025-05-14"

const AnthropicBetaInterleavedThinking2025\_05\_14 AnthropicBeta = "interleaved-thinking-2025-05-14"

const AnthropicBetaCodeExecution2025\_05\_22 AnthropicBeta = "code-execution-2025-05-22"

const AnthropicBetaExtendedCacheTTL2025\_04\_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"

const AnthropicBetaContext1m2025\_08\_07 AnthropicBeta = "context-1m-2025-08-07"

const AnthropicBetaContextManagement2025\_06\_27 AnthropicBeta = "context-management-2025-06-27"

const AnthropicBetaModelContextWindowExceeded2025\_08\_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"

const AnthropicBetaSkills2025\_10\_02 AnthropicBeta = "skills-2025-10-02"

const AnthropicBetaFastMode2026\_02\_01 AnthropicBeta = "fast-mode-2026-02-01"

const AnthropicBetaOutput300k2026\_03\_24 AnthropicBeta = "output-300k-2026-03-24"

const AnthropicBetaUserProfiles2026\_03\_24 AnthropicBeta = "user-profiles-2026-03-24"

const AnthropicBetaAdvisorTool2026\_03\_01 AnthropicBeta = "advisor-tool-2026-03-01"

const AnthropicBetaManagedAgents2026\_04\_01 AnthropicBeta = "managed-agents-2026-04-01"

const AnthropicBetaCacheDiagnosis2026\_04\_07 AnthropicBeta = "cache-diagnosis-2026-04-07"

const AnthropicBetaThinkingTokenCount2026\_05\_13 AnthropicBeta = "thinking-token-count-2026-05-13"

const AnthropicBetaMidConversationSystem2026\_04\_07 AnthropicBeta = "mid-conversation-system-2026-04-07"

##### ReturnsExpand Collapse

type BetaSelfHostedWork struct{…}

Work resource representing a unit of work in a self-hosted environment.

Work items are queued when sessions are created or when long-dormant sessions
receive new messages. The environment worker polls for work to execute in a
self-hosted sandbox.

ID string

Work identifier (e.g., 'work\_...')

AcknowledgedAt string

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

CreatedAt string

RFC 3339 timestamp when work was created

Data [BetaSessionWorkData](api/beta.md)

The actual work to be performed

ID string

Session identifier (e.g., 'session\_...')

Type Session

Type of work data

EnvironmentID string

Environment identifier this work belongs to (e.g., `env_...`)

LatestHeartbeatAt string

RFC 3339 timestamp of the most recent heartbeat

Metadata map[string, string]

User-provided metadata key-value pairs associated with this work item

StartedAt string

RFC 3339 timestamp when work execution started

State BetaSelfHostedWorkState

Current state of the work item

One of the following:

const BetaSelfHostedWorkStateQueued BetaSelfHostedWorkState = "queued"

const BetaSelfHostedWorkStateStarting BetaSelfHostedWorkState = "starting"

const BetaSelfHostedWorkStateActive BetaSelfHostedWorkState = "active"

const BetaSelfHostedWorkStateStopping BetaSelfHostedWorkState = "stopping"

const BetaSelfHostedWorkStateStopped BetaSelfHostedWorkState = "stopped"

StopRequestedAt string

RFC 3339 timestamp when stop was requested

StoppedAt string

RFC 3339 timestamp when work execution stopped

Type Work

The type of object (always 'work')

Update Work Item

Go

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
  betaSelfHostedWork, err := client.Beta.Environments.Work.Update(
    context.TODO(),
    "work_id",
    anthropic.BetaEnvironmentWorkUpdateParams{
      EnvironmentID: "env_011CZkZ9X2dpNyB7HsEFoRfW",
      BetaSelfHostedWorkUpdateRequest: anthropic.BetaSelfHostedWorkUpdateRequestParam{
        Metadata: map[string]string{
        "foo": "string",
        },
      },
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaSelfHostedWork.ID)
}
```

Response 200

```shiki
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

---

*Copyright © Anthropic. All rights reserved.*
