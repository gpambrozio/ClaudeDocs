# Memory Versions

Copy page

PHP

# Memory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

$client->beta->memoryStores->memoryVersions->list(string memoryStoreID, ?string apiKeyID, ?\Datetime createdAtGte, ?\Datetime createdAtLte, ?int limit, ?string memoryID, ?[ManagedAgentsMemoryVersionOperation](api/beta.md) operation, ?string page, ?string sessionID, ?[ManagedAgentsMemoryView](api/beta.md) view, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsMemoryVersion](api/beta.md)>

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

$client->beta->memoryStores->memoryVersions->retrieve(string memoryVersionID, string memoryStoreID, ?[ManagedAgentsMemoryView](api/beta.md) view, ?list<AnthropicBeta> betas): [ManagedAgentsMemoryVersion](api/beta.md)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

$client->beta->memoryStores->memoryVersions->redact(string memoryVersionID, string memoryStoreID, ?list<AnthropicBeta> betas): [ManagedAgentsMemoryVersion](api/beta.md)

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

##### ModelsExpand Collapse

[ManagedAgentsActor](api/beta.md)

One of the following:

[ManagedAgentsSessionActor](api/beta.md)

string sessionID

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

Type type

[ManagedAgentsAPIActor](api/beta.md)

string apiKeyID

ID of the API key that performed the write. This identifies the key, not the secret.

Type type

[ManagedAgentsUserActor](api/beta.md)

Type type

string userID

ID of the user who performed the write (a `user_...` value).

[ManagedAgentsAPIActor](api/beta.md)

string apiKeyID

ID of the API key that performed the write. This identifies the key, not the secret.

Type type

[ManagedAgentsMemoryVersion](api/beta.md)

string id

Unique identifier for this version (a `memver_...` value).

\Datetime createdAt

A timestamp in RFC 3339 format

string memoryID

ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](api/beta/memory_stores/memory_versions/list.md) to retrieve the full lineage including the `deleted` row.

string memoryStoreID

ID of the memory store this version belongs to (a `memstore_...` value).

[ManagedAgentsMemoryVersionOperation](api/beta.md) operation

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

Type type

?string content

The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

?string contentSha256

Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

?int contentSizeBytes

Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

?[ManagedAgentsActor](api/beta.md) createdBy

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

?string path

The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

?\Datetime redactedAt

A timestamp in RFC 3339 format

?[ManagedAgentsActor](api/beta.md) redactedBy

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

[ManagedAgentsMemoryVersionOperation](api/beta.md)

One of the following:

"created"

"modified"

"deleted"

[ManagedAgentsSessionActor](api/beta.md)

string sessionID

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

Type type

[ManagedAgentsUserActor](api/beta.md)

Type type

string userID

ID of the user who performed the write (a `user_...` value).

---

*Copyright © Anthropic. All rights reserved.*
