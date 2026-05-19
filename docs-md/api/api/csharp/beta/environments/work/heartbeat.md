# Record Heartbeat

Copy page

C#

# Record Heartbeat

[BetaSelfHostedWorkHeartbeatResponse](api/beta.md) Beta.Environments.Work.Heartbeat(WorkHeartbeatParamsparameters, CancellationTokencancellationToken = default)

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Record a heartbeat for a work item to maintain the lease.

##### ParametersExpand Collapse

WorkHeartbeatParams parameters

required string environmentID

Path param

required string workID

Path param

Long? desiredTtlSeconds

Query param: Desired TTL in seconds

string? expectedLastHeartbeat

Query param: Expected last\_heartbeat for conditional update (optimistic concurrency). Use literal 'NO\_HEARTBEAT' to claim an unclaimed lease (first heartbeat). For subsequent heartbeats, echo the server's previous last\_heartbeat value exactly. Returns 412 Precondition Failed if the actual value doesn't match.

IReadOnlyList<[AnthropicBeta](api/beta.md)> betas

Header param: Optional header to specify the beta version(s) you want to use.

"message-batches-2024-09-24"MessageBatches2024\_09\_24

"prompt-caching-2024-07-31"PromptCaching2024\_07\_31

"computer-use-2024-10-22"ComputerUse2024\_10\_22

"computer-use-2025-01-24"ComputerUse2025\_01\_24

"pdfs-2024-09-25"Pdfs2024\_09\_25

"token-counting-2024-11-01"TokenCounting2024\_11\_01

"token-efficient-tools-2025-02-19"TokenEfficientTools2025\_02\_19

"output-128k-2025-02-19"Output128k2025\_02\_19

"files-api-2025-04-14"FilesApi2025\_04\_14

"mcp-client-2025-04-04"McpClient2025\_04\_04

"mcp-client-2025-11-20"McpClient2025\_11\_20

"dev-full-thinking-2025-05-14"DevFullThinking2025\_05\_14

"interleaved-thinking-2025-05-14"InterleavedThinking2025\_05\_14

"code-execution-2025-05-22"CodeExecution2025\_05\_22

"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025\_04\_11

"context-1m-2025-08-07"Context1m2025\_08\_07

"context-management-2025-06-27"ContextManagement2025\_06\_27

"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025\_08\_26

"skills-2025-10-02"Skills2025\_10\_02

"fast-mode-2026-02-01"FastMode2026\_02\_01

"output-300k-2026-03-24"Output300k2026\_03\_24

"user-profiles-2026-03-24"UserProfiles2026\_03\_24

"advisor-tool-2026-03-01"AdvisorTool2026\_03\_01

"managed-agents-2026-04-01"ManagedAgents2026\_04\_01

"cache-diagnosis-2026-04-07"CacheDiagnosis2026\_04\_07

##### ReturnsExpand Collapse

class BetaSelfHostedWorkHeartbeatResponse:

Response after recording a heartbeat for a work item.

required string LastHeartbeat

RFC 3339 timestamp of the actual heartbeat from DB

required Boolean LeaseExtended

Whether the heartbeat succeeded in extending the lease

required State State

Current state of the work item (active/stopping/stopped)

Accepts one of the following:

"queued"Queued

"starting"Starting

"active"Active

"stopping"Stopping

"stopped"Stopped

required Long TtlSeconds

Effective TTL applied to the lease

JsonElement Type "work\_heartbeat"constant

The type of response

Record Heartbeat

C#

```shiki
WorkHeartbeatParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW",
    WorkID = "work_id",
};

var betaSelfHostedWorkHeartbeatResponse = await client.Beta.Environments.Work.Heartbeat(parameters);

Console.WriteLine(betaSelfHostedWorkHeartbeatResponse);
```

Response 200

```shiki
{
  "last_heartbeat": "last_heartbeat",
  "lease_extended": true,
  "state": "queued",
  "ttl_seconds": 0,
  "type": "work_heartbeat"
}
```

##### Returns Examples

Response 200

```shiki
{
  "last_heartbeat": "last_heartbeat",
  "lease_extended": true,
  "state": "queued",
  "ttl_seconds": 0,
  "type": "work_heartbeat"
}
```

---

*Copyright © Anthropic. All rights reserved.*
