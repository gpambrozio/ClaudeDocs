# Update Work Item

Copy page



Java

# Update Work Item

[BetaSelfHostedWork](api/beta/environments/work.md) beta().environments().work().update(WorkUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/environments/{environment\_id}/work/{work\_id}

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Update work item metadata with merge semantics.

##### ParametersExpand Collapse



WorkUpdateParams params

String environmentId

Optional<String> workId



Optional<List<AnthropicBeta>> betas

Optional header to specify the beta version(s) you want to use.

MESSAGE\_BATCHES\_2024\_09\_24("message-batches-2024-09-24")

PROMPT\_CACHING\_2024\_07\_31("prompt-caching-2024-07-31")

COMPUTER\_USE\_2024\_10\_22("computer-use-2024-10-22")

COMPUTER\_USE\_2025\_01\_24("computer-use-2025-01-24")

PDFS\_2024\_09\_25("pdfs-2024-09-25")

TOKEN\_COUNTING\_2024\_11\_01("token-counting-2024-11-01")

TOKEN\_EFFICIENT\_TOOLS\_2025\_02\_19("token-efficient-tools-2025-02-19")

OUTPUT\_128K\_2025\_02\_19("output-128k-2025-02-19")

FILES\_API\_2025\_04\_14("files-api-2025-04-14")

MCP\_CLIENT\_2025\_04\_04("mcp-client-2025-04-04")

MCP\_CLIENT\_2025\_11\_20("mcp-client-2025-11-20")

DEV\_FULL\_THINKING\_2025\_05\_14("dev-full-thinking-2025-05-14")

INTERLEAVED\_THINKING\_2025\_05\_14("interleaved-thinking-2025-05-14")

CODE\_EXECUTION\_2025\_05\_22("code-execution-2025-05-22")

EXTENDED\_CACHE\_TTL\_2025\_04\_11("extended-cache-ttl-2025-04-11")

CONTEXT\_1M\_2025\_08\_07("context-1m-2025-08-07")

CONTEXT\_MANAGEMENT\_2025\_06\_27("context-management-2025-06-27")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED\_2025\_08\_26("model-context-window-exceeded-2025-08-26")

SKILLS\_2025\_10\_02("skills-2025-10-02")

FAST\_MODE\_2026\_02\_01("fast-mode-2026-02-01")

OUTPUT\_300K\_2026\_03\_24("output-300k-2026-03-24")

USER\_PROFILES\_2026\_03\_24("user-profiles-2026-03-24")

ADVISOR\_TOOL\_2026\_03\_01("advisor-tool-2026-03-01")

MANAGED\_AGENTS\_2026\_04\_01("managed-agents-2026-04-01")

CACHE\_DIAGNOSIS\_2026\_04\_07("cache-diagnosis-2026-04-07")

THINKING\_TOKEN\_COUNT\_2026\_05\_13("thinking-token-count-2026-05-13")

SERVER\_SIDE\_FALLBACK\_2026\_06\_01("server-side-fallback-2026-06-01")

FALLBACK\_CREDIT\_2026\_06\_01("fallback-credit-2026-06-01")

[BetaSelfHostedWorkUpdateRequest](api/beta/environments/work.md) betaSelfHostedWorkUpdateRequest

Request to update work item metadata.

##### ReturnsExpand Collapse



class BetaSelfHostedWork:

Work resource representing a unit of work in a self-hosted environment.

Work items are queued when sessions are created or when long-dormant sessions
receive new messages. The environment worker polls for work to execute in a
self-hosted sandbox.

String id

Work identifier (e.g., 'work\_...')

Optional<String> acknowledgedAt

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

String createdAt

RFC 3339 timestamp when work was created



[BetaSessionWorkData](api/beta/environments/work.md) data

The actual work to be performed

String id

Session identifier (e.g., 'session\_...')

JsonValue; type "session"constant"session"constant

Type of work data

String environmentId

Environment identifier this work belongs to (e.g., `env_...`)

Optional<String> latestHeartbeatAt

RFC 3339 timestamp of the most recent heartbeat

Metadata metadata

User-provided metadata key-value pairs associated with this work item

Optional<String> startedAt

RFC 3339 timestamp when work execution started



State state

Current state of the work item

One of the following:

QUEUED("queued")

STARTING("starting")

ACTIVE("active")

STOPPING("stopping")

STOPPED("stopped")

Optional<String> stopRequestedAt

RFC 3339 timestamp when stop was requested

Optional<String> stoppedAt

RFC 3339 timestamp when work execution stopped

JsonValue; type "work"constant"work"constant

The type of object (always 'work')

Update Work Item

Java

```shiki
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.JsonValue;
import com.anthropic.models.beta.environments.work.BetaSelfHostedWork;
import com.anthropic.models.beta.environments.work.BetaSelfHostedWorkUpdateRequest;
import com.anthropic.models.beta.environments.work.WorkUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        WorkUpdateParams params = WorkUpdateParams.builder()
            .environmentId("env_011CZkZ9X2dpNyB7HsEFoRfW")
            .workId("work_id")
            .betaSelfHostedWorkUpdateRequest(BetaSelfHostedWorkUpdateRequest.builder()
                .metadata(BetaSelfHostedWorkUpdateRequest.Metadata.builder()
                    .putAdditionalProperty("foo", JsonValue.from("string"))
                    .build())
                .build())
            .build();
        BetaSelfHostedWork betaSelfHostedWork = client.beta().environments().work().update(params);
    }
}
```

Response 200



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



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
