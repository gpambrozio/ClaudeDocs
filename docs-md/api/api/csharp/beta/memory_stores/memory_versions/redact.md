# Redact a memory version

Copy page

C#

# Redact a memory version

[BetaManagedAgentsMemoryVersion](api/beta.md) Beta.MemoryStores.MemoryVersions.Redact(MemoryVersionRedactParamsparameters, CancellationTokencancellationToken = default)

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

Redact a memory version

##### ParametersExpand Collapse

MemoryVersionRedactParams parameters

required string memoryStoreID

Path param: Path parameter memory\_store\_id

required string memoryVersionID

Path param: Path parameter memory\_version\_id

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

##### ReturnsExpand Collapse

class BetaManagedAgentsMemoryVersion:

A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

required string ID

Unique identifier for this version (a `memver_...` value).

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string MemoryID

ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](api/beta/memory_stores/memory_versions/list.md) to retrieve the full lineage including the `deleted` row.

required string MemoryStoreID

ID of the memory store this version belongs to (a `memstore_...` value).

required [BetaManagedAgentsMemoryVersionOperation](api/beta.md) Operation

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

Accepts one of the following:

"created"Created

"modified"Modified

"deleted"Deleted

required Type Type

string? Content

The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

string? ContentSha256

Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

Int? ContentSizeBytes

Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

[BetaManagedAgentsActor](api/beta.md) CreatedBy

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

Accepts one of the following:

class BetaManagedAgentsSessionActor:

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

required string SessionID

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

required Type Type

class BetaManagedAgentsApiActor:

Attribution for a write made directly via the public API (outside of any session).

required string ApiKeyID

ID of the API key that performed the write. This identifies the key, not the secret.

required Type Type

class BetaManagedAgentsUserActor:

Attribution for a write made by a human user through the Anthropic Console.

required Type Type

required string UserID

ID of the user who performed the write (a `user_...` value).

string? Path

The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

DateTimeOffset? RedactedAt

A timestamp in RFC 3339 format

[BetaManagedAgentsActor](api/beta.md) RedactedBy

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

Accepts one of the following:

class BetaManagedAgentsSessionActor:

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

required string SessionID

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

required Type Type

class BetaManagedAgentsApiActor:

Attribution for a write made directly via the public API (outside of any session).

required string ApiKeyID

ID of the API key that performed the write. This identifies the key, not the secret.

required Type Type

class BetaManagedAgentsUserActor:

Attribution for a write made by a human user through the Anthropic Console.

required Type Type

required string UserID

ID of the user who performed the write (a `user_...` value).

Redact a memory version

C#

```shiki
MemoryVersionRedactParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryVersionID = "memory_version_id",
};

var betaManagedAgentsMemoryVersion = await client.Beta.MemoryStores.MemoryVersions.Redact(parameters);

Console.WriteLine(betaManagedAgentsMemoryVersion);
```

Response 200

```shiki
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_id": "memory_id",
  "memory_store_id": "memory_store_id",
  "operation": "created",
  "type": "memory_version",
  "content": "content",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_by": {
    "session_id": "x",
    "type": "session_actor"
  },
  "path": "path",
  "redacted_at": "2019-12-27T18:11:19.117Z",
  "redacted_by": {
    "session_id": "x",
    "type": "session_actor"
  }
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_id": "memory_id",
  "memory_store_id": "memory_store_id",
  "operation": "created",
  "type": "memory_version",
  "content": "content",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_by": {
    "session_id": "x",
    "type": "session_actor"
  },
  "path": "path",
  "redacted_at": "2019-12-27T18:11:19.117Z",
  "redacted_by": {
    "session_id": "x",
    "type": "session_actor"
  }
}
```

---

*Copyright © Anthropic. All rights reserved.*
