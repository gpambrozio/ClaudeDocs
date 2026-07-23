# Redact a memory version

Copy page



cURL

# Redact a memory version

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

Redact a memory version

##### Path ParametersExpand Collapse

memory\_store\_id: string

memory\_version\_id: string

##### Header ParametersExpand Collapse



"anthropic-beta": optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

One of the following:

string



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 27 more

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

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"dreaming-2026-04-21"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"fallback-credit-2026-06-01"

"agent-memory-2026-07-22"

##### ReturnsExpand Collapse



BetaManagedAgentsMemoryVersion object { id, created\_at, memory\_id, 10 more } 

A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

id: string

Unique identifier for this version (a `memver_...` value).

created\_at: string

A timestamp in RFC 3339 format

memory\_id: string

ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](api/beta/memory_stores/memory_versions/list.md) to retrieve the full lineage including the `deleted` row.

memory\_store\_id: string

ID of the memory store this version belongs to (a `memstore_...` value).



operation: [BetaManagedAgentsMemoryVersionOperation](api/beta/memory_stores/memory_versions.md)

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

One of the following:

"created"

"modified"

"deleted"

type: "memory\_version"

content: optional string

The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

content\_sha256: optional string

Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

content\_size\_bytes: optional number

Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.



created\_by: optional [BetaManagedAgentsActor](api/beta/memory_stores/memory_versions.md)

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

One of the following:



BetaManagedAgentsSessionActor object { session\_id, type } 

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: string

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: "session\_actor"



BetaManagedAgentsAPIActor object { api\_key\_id, type } 

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: string

ID of the API key that performed the write. This identifies the key, not the secret.

type: "api\_actor"



BetaManagedAgentsUserActor object { type, user\_id } 

Attribution for a write made by a human user through the Anthropic Console.

type: "user\_actor"

user\_id: string

ID of the user who performed the write (a `user_...` value).

path: optional string

The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

redacted\_at: optional string

A timestamp in RFC 3339 format



redacted\_by: optional [BetaManagedAgentsActor](api/beta/memory_stores/memory_versions.md)

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

One of the following:



BetaManagedAgentsSessionActor object { session\_id, type } 

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: string

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: "session\_actor"



BetaManagedAgentsAPIActor object { api\_key\_id, type } 

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: string

ID of the API key that performed the write. This identifies the key, not the secret.

type: "api\_actor"



BetaManagedAgentsUserActor object { type, user\_id } 

Attribution for a write made by a human user through the Anthropic Console.

type: "user\_actor"

user\_id: string

ID of the user who performed the write (a `user_...` value).

Redact a memory version

cURL

```shiki
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memory_versions/$MEMORY_VERSION_ID/redact \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



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



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
