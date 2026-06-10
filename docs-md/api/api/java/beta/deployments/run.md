# Run Deployment Now

Copy page

SDK language

Java

# Run Deployment Now

[BetaManagedAgentsDeploymentRun](api/beta.md) beta().deployments().run(DeploymentRunParamsparams = DeploymentRunParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/deployments/{deployment\_id}/run

Run Deployment Now

##### ParametersExpand Collapse

DeploymentRunParams params

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

class BetaManagedAgentsDeploymentRun:

A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

String id

Unique identifier for this run (`drun_...`).

[BetaManagedAgentsAgentReference](api/beta.md) agent

A resolved agent reference with a concrete version.

String id

Type type

long version

LocalDateTime createdAt

A timestamp in RFC 3339 format

String deploymentId

ID of the deployment that produced this run.

Optional<Error> error

Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

One of the following:

class BetaManagedAgentsEnvironmentArchivedRunError:

The deployment's environment was archived.

String message

Human-readable error description.

Type type

class BetaManagedAgentsAgentArchivedRunError:

The deployment's agent was archived.

String message

Human-readable error description.

Type type

class BetaManagedAgentsEnvironmentNotFoundRunError:

The deployment's environment no longer exists.

String message

Human-readable error description.

Type type

class BetaManagedAgentsVaultNotFoundRunError:

A vault referenced by the deployment no longer exists.

String message

Human-readable error description.

Type type

class BetaManagedAgentsVaultArchivedRunError:

A vault referenced by the deployment is archived.

String message

Human-readable error description.

Type type

class BetaManagedAgentsFileNotFoundRunError:

A file resource referenced by the deployment no longer exists.

String message

Human-readable error description.

Type type

class BetaManagedAgentsMemoryStoreArchivedRunError:

A memory store referenced by the deployment is archived.

String message

Human-readable error description.

Type type

class BetaManagedAgentsSkillNotFoundRunError:

A skill referenced by the deployment's agent no longer exists.

String message

Human-readable error description.

Type type

class BetaManagedAgentsSessionResourceNotFoundRunError:

A referenced resource no longer exists and its kind was not reported.

String message

Human-readable error description.

Type type

class BetaManagedAgentsWorkspaceArchivedRunError:

The deployment's workspace was archived.

String message

Human-readable error description.

Type type

class BetaManagedAgentsOrganizationDisabledRunError:

The deployment's organization is disabled.

String message

Human-readable error description.

Type type

class BetaManagedAgentsSessionRateLimitedRunError:

Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

String message

Human-readable error description.

Type type

class BetaManagedAgentsSessionCreationRejectedRunError:

The session create request was rejected with a non-retryable validation error.

String message

Human-readable error description.

Type type

class BetaManagedAgentsUnknownRunError:

An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

String message

Human-readable error description.

Type type

class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError:

The deployment configures resources, but its environment is self-hosted and cannot mount them.

String message

Human-readable error description.

Type type

class BetaManagedAgentsMcpEgressBlockedRunError:

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

String message

Human-readable error description.

Type type

Optional<String> sessionId

Populated on success. Null on creation failure. Exactly one of session\_id or error is non-null.

[BetaManagedAgentsTriggerContext](api/beta.md) triggerContext

Describes what triggered a deployment run, with trigger-specific metadata.

One of the following:

class BetaManagedAgentsScheduleTriggerContext:

The run was fired by the deployment's cron schedule.

LocalDateTime scheduledAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsManualTriggerContext:

The run was started manually by creating a session directly against the deployment.

Type type

Type type

Run Deployment Now

Java

```shiki
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.deploymentruns.BetaManagedAgentsDeploymentRun;
import com.anthropic.models.beta.deployments.DeploymentRunParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsDeploymentRun betaManagedAgentsDeploymentRun = client.beta().deployments().run("deployment_id");
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
