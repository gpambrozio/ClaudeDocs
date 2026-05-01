# Retrieve a memory store

Copy page

C#

# Retrieve a memory store

[BetaManagedAgentsMemoryStore](api/beta.md) Beta.MemoryStores.Retrieve(MemoryStoreRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/memory\_stores/{memory\_store\_id}

Retrieve a memory store

##### ParametersExpand Collapse

MemoryStoreRetrieveParams parameters

required string memoryStoreID

Path parameter memory\_store\_id

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

##### ReturnsExpand Collapse

class BetaManagedAgentsMemoryStore:

A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

required string ID

Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string Name

Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

DateTimeOffset? ArchivedAt

A timestamp in RFC 3339 format

string Description

Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

IReadOnlyDictionary<string, string> Metadata

Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

Retrieve a memory store

C#

```shiki
MemoryStoreRetrieveParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var betaManagedAgentsMemoryStore = await client.Beta.MemoryStores.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsMemoryStore);
```

Response 200

```shiki
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  }
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  }
}
```

---

*Copyright © Anthropic. All rights reserved.*
