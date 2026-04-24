# DeleteMemory

Copy page

C#

# DeleteMemory

[BetaManagedAgentsDeletedMemory](api/beta.md) Beta.MemoryStores.Memories.Delete(MemoryDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

DeleteMemory

##### ParametersExpand Collapse

MemoryDeleteParams parameters

required string memoryStoreID

Path param: Path parameter memory\_store\_id

required string memoryID

Path param: Path parameter memory\_id

string expectedContentSha256

Query param: Query parameter for expected\_content\_sha256

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

"advisor-tool-2026-03-01"AdvisorTool2026\_03\_01

##### ReturnsExpand Collapse

class BetaManagedAgentsDeletedMemory:

required string ID

required Type Type

DeleteMemory

C#

```shiki
MemoryDeleteParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryID = "memory_id",
};

var betaManagedAgentsDeletedMemory = await client.Beta.MemoryStores.Memories.Delete(parameters);

Console.WriteLine(betaManagedAgentsDeletedMemory);
```

Response 200

```shiki
{
  "id": "id",
  "type": "memory_deleted"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "id",
  "type": "memory_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
