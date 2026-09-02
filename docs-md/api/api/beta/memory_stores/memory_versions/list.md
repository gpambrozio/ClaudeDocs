# List memory versions

Copy page



cURL

# List memory versions

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

List memory versions

##### Path parameters

memory\_store\_id: string

##### Query parameters

api\_key\_id: optional string

Query parameter for api\_key\_id



"created\_at[gte]": optional string

Return versions created at or after this time (inclusive).

formatdate-time



"created\_at[lte]": optional string

Return versions created at or before this time (inclusive).

formatdate-time



limit: optional number

Query parameter for limit

formatint32

memory\_id: optional string

Query parameter for memory\_id



operation: optional [BetaManagedAgentsMemoryVersionOperation](api/http/beta/memory_stores/memory_versions.md)

Query parameter for operation

One of the following:

"created"

"modified"

"deleted"

page: optional string

Query parameter for page

service\_account\_id: optional string

Query parameter for service\_account\_id

session\_id: optional string

Query parameter for session\_id



view: optional [BetaManagedAgentsMemoryView](api/http/beta/memory_stores/memories.md)

Query parameter for view

One of the following:

"basic"

"full"

##### Headers



"anthropic-beta": optional array of [AnthropicBeta](api/http/beta.md)

Optional header to specify the beta version(s) you want to use.

One of the following:

string



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 41 more

One of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"user-profiles-2026-08-18"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"dreaming-2026-04-21"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"server-side-fallback-2026-07-01"

"fallback-credit-2026-06-01"

"fallback-credit-2026-07-01"

"agent-memory-2026-07-22"

"mid-conversation-tool-changes-2026-07-01"

"compact-2026-01-12"

"computer-use-2025-11-24"

"mcp-tunnels-2026-06-22"

"structured-outputs-2025-11-13"

"task-budgets-2026-03-13"

"thinking-display-updates-2026-08-18"

"ce-user-management-2026-07-13"

"mid-conversation-output-config-2026-07-01"

"thinking-binding-controls-2026-08-01"

"mid-conversation-system-clear-at-2026-08-21"

##### Returns



data: optional array of [BetaManagedAgentsMemoryVersion](api/http/beta/memory_stores/memory_versions.md) { id, created\_at, memory\_id, 10 more }

One page of `memory_version` objects, ordered by `created_at` descending (newest first), with `id` as tiebreak.

id: string

Unique identifier for this version (a `memver_...` value).



created\_at: string

A timestamp in RFC 3339 format

formatdate-time

memory\_id: string

ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](api/beta/memory_stores/memory_versions/list.md) to retrieve the memory's retained versions, including the `deleted` row while the lineage is retained.

memory\_store\_id: string

ID of the memory store this version belongs to (a `memstore_...` value).



operation: [BetaManagedAgentsMemoryVersionOperation](api/http/beta/memory_stores/memory_versions.md)

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

One of the following:

"created"

"modified"

"deleted"

type: "memory\_version"

content: optional string or null

The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

content\_sha256: optional string or null

Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.



content\_size\_bytes: optional number or null

Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

formatint32



created\_by: optional [BetaManagedAgentsActor](api/http/beta/memory_stores/memory_versions.md)

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

One of the following:

path: optional string or null

The memory's path at the time of this write. `null` if and only if `redacted_at` is set.



redacted\_at: optional string or null

A timestamp in RFC 3339 format

formatdate-time



redacted\_by: optional [BetaManagedAgentsActor](api/http/beta/memory_stores/memory_versions.md)

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

One of the following:

next\_page: optional string or null

Opaque cursor for the next page (a `page_...` value), or `null` if there are no more results. Pass as `page` on the next request.

List memory versions

cURL

```shiki
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memory_versions \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```shiki
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
