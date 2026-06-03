# Get Queue Statistics

Copy page

SDK language

C#

# Get Queue Statistics

[BetaSelfHostedWorkQueueStats](api/beta.md) Beta.Environments.Work.Stats(WorkStatsParamsparameters, CancellationTokencancellationToken = default)

GET/v1/environments/{environment\_id}/work/stats

Get statistics about the work queue for an environment.

##### ParametersExpand Collapse

WorkStatsParams parameters

required string environmentID

IReadOnlyList<[AnthropicBeta](api/beta.md)> betas

Optional header to specify the beta version(s) you want to use.

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

"thinking-token-count-2026-05-13"ThinkingTokenCount2026\_05\_13

##### ReturnsExpand Collapse

class BetaSelfHostedWorkQueueStats:

Statistics about the work queue for an environment.

Uses Redis Stream consumer group metrics for O(1) queries.

required Long Depth

Number of work items waiting to be picked up (lag from consumer group)

required string? OldestQueuedAt

RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

required Long Pending

Number of work items being processed (polled but not acknowledged)

JsonElement Type "work\_queue\_stats"constant

The type of object

required Long? WorkersPolling

Number of workers that have polled for work in the last 30 seconds. Requires worker\_id to be sent with poll requests.

Get Queue Statistics

C#

```shiki
WorkStatsParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW"
};

var betaSelfHostedWorkQueueStats = await client.Beta.Environments.Work.Stats(parameters);

Console.WriteLine(betaSelfHostedWorkQueueStats);
```

Response 200

```shiki
{
  "depth": 0,
  "oldest_queued_at": "oldest_queued_at",
  "pending": 0,
  "type": "work_queue_stats",
  "workers_polling": 0
}
```

##### Returns Examples

Response 200

```shiki
{
  "depth": 0,
  "oldest_queued_at": "oldest_queued_at",
  "pending": 0,
  "type": "work_queue_stats",
  "workers_polling": 0
}
```

---

*Copyright © Anthropic. All rights reserved.*
