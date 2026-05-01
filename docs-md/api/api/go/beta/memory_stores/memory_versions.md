# Memory Versions

Copy page

Go

# Memory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

client.Beta.MemoryStores.MemoryVersions.List(ctx, memoryStoreID, params) (\*PageCursor[[BetaManagedAgentsMemoryVersion](api/beta.md)], error)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

client.Beta.MemoryStores.MemoryVersions.Get(ctx, memoryVersionID, params) (\*[BetaManagedAgentsMemoryVersion](api/beta.md), error)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

client.Beta.MemoryStores.MemoryVersions.Redact(ctx, memoryVersionID, params) (\*[BetaManagedAgentsMemoryVersion](api/beta.md), error)

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

##### ModelsExpand Collapse

type BetaManagedAgentsActorUnion interface{…}

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

Accepts one of the following:

type BetaManagedAgentsSessionActor struct{…}

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

SessionID string

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

Type BetaManagedAgentsSessionActorType

type BetaManagedAgentsAPIActor struct{…}

Attribution for a write made directly via the public API (outside of any session).

APIKeyID string

ID of the API key that performed the write. This identifies the key, not the secret.

Type BetaManagedAgentsAPIActorType

type BetaManagedAgentsUserActor struct{…}

Attribution for a write made by a human user through the Anthropic Console.

Type BetaManagedAgentsUserActorType

UserID string

ID of the user who performed the write (a `user_...` value).

type BetaManagedAgentsAPIActor struct{…}

Attribution for a write made directly via the public API (outside of any session).

APIKeyID string

ID of the API key that performed the write. This identifies the key, not the secret.

Type BetaManagedAgentsAPIActorType

type BetaManagedAgentsMemoryVersion struct{…}

A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

ID string

Unique identifier for this version (a `memver_...` value).

CreatedAt Time

A timestamp in RFC 3339 format

MemoryID string

ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](api/beta/memory_stores/memory_versions/list.md) to retrieve the full lineage including the `deleted` row.

MemoryStoreID string

ID of the memory store this version belongs to (a `memstore_...` value).

Operation [BetaManagedAgentsMemoryVersionOperation](api/beta.md)

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

Accepts one of the following:

const BetaManagedAgentsMemoryVersionOperationCreated [BetaManagedAgentsMemoryVersionOperation](api/beta.md) = "created"

const BetaManagedAgentsMemoryVersionOperationModified [BetaManagedAgentsMemoryVersionOperation](api/beta.md) = "modified"

const BetaManagedAgentsMemoryVersionOperationDeleted [BetaManagedAgentsMemoryVersionOperation](api/beta.md) = "deleted"

Type BetaManagedAgentsMemoryVersionType

Content stringoptional

The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

ContentSha256 stringoptional

Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

ContentSizeBytes int64optional

Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

CreatedBy [BetaManagedAgentsActorUnion](api/beta.md)optional

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

Accepts one of the following:

type BetaManagedAgentsSessionActor struct{…}

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

SessionID string

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

Type BetaManagedAgentsSessionActorType

type BetaManagedAgentsAPIActor struct{…}

Attribution for a write made directly via the public API (outside of any session).

APIKeyID string

ID of the API key that performed the write. This identifies the key, not the secret.

Type BetaManagedAgentsAPIActorType

type BetaManagedAgentsUserActor struct{…}

Attribution for a write made by a human user through the Anthropic Console.

Type BetaManagedAgentsUserActorType

UserID string

ID of the user who performed the write (a `user_...` value).

Path stringoptional

The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

RedactedAt Timeoptional

A timestamp in RFC 3339 format

RedactedBy [BetaManagedAgentsActorUnion](api/beta.md)optional

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

Accepts one of the following:

type BetaManagedAgentsSessionActor struct{…}

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

SessionID string

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

Type BetaManagedAgentsSessionActorType

type BetaManagedAgentsAPIActor struct{…}

Attribution for a write made directly via the public API (outside of any session).

APIKeyID string

ID of the API key that performed the write. This identifies the key, not the secret.

Type BetaManagedAgentsAPIActorType

type BetaManagedAgentsUserActor struct{…}

Attribution for a write made by a human user through the Anthropic Console.

Type BetaManagedAgentsUserActorType

UserID string

ID of the user who performed the write (a `user_...` value).

type BetaManagedAgentsMemoryVersionOperation string

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

Accepts one of the following:

const BetaManagedAgentsMemoryVersionOperationCreated [BetaManagedAgentsMemoryVersionOperation](api/beta.md) = "created"

const BetaManagedAgentsMemoryVersionOperationModified [BetaManagedAgentsMemoryVersionOperation](api/beta.md) = "modified"

const BetaManagedAgentsMemoryVersionOperationDeleted [BetaManagedAgentsMemoryVersionOperation](api/beta.md) = "deleted"

type BetaManagedAgentsSessionActor struct{…}

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

SessionID string

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

Type BetaManagedAgentsSessionActorType

type BetaManagedAgentsUserActor struct{…}

Attribution for a write made by a human user through the Anthropic Console.

Type BetaManagedAgentsUserActorType

UserID string

ID of the user who performed the write (a `user_...` value).

---

*Copyright © Anthropic. All rights reserved.*
