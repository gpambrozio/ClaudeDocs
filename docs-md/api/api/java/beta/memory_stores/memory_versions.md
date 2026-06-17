# Memory Versions

Copy page



Java

# Memory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

MemoryVersionListPage beta().memoryStores().memoryVersions().list(MemoryVersionListParamsparams = MemoryVersionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

[BetaManagedAgentsMemoryVersion](api/beta.md) beta().memoryStores().memoryVersions().retrieve(MemoryVersionRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

[BetaManagedAgentsMemoryVersion](api/beta.md) beta().memoryStores().memoryVersions().redact(MemoryVersionRedactParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

##### ModelsExpand Collapse



class BetaManagedAgentsActor: A class that can be one of several variants.union 

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).



class BetaManagedAgentsSessionActor:

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

String sessionId

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

Type type



class BetaManagedAgentsApiActor:

Attribution for a write made directly via the public API (outside of any session).

String apiKeyId

ID of the API key that performed the write. This identifies the key, not the secret.

Type type



class BetaManagedAgentsUserActor:

Attribution for a write made by a human user through the Anthropic Console.

Type type

String userId

ID of the user who performed the write (a `user_...` value).



class BetaManagedAgentsApiActor:

Attribution for a write made directly via the public API (outside of any session).

String apiKeyId

ID of the API key that performed the write. This identifies the key, not the secret.

Type type



class BetaManagedAgentsMemoryVersion:

A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

String id

Unique identifier for this version (a `memver_...` value).

LocalDateTime createdAt

A timestamp in RFC 3339 format

String memoryId

ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](api/beta/memory_stores/memory_versions/list.md) to retrieve the full lineage including the `deleted` row.

String memoryStoreId

ID of the memory store this version belongs to (a `memstore_...` value).



[BetaManagedAgentsMemoryVersionOperation](api/beta.md) operation

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

One of the following:

CREATED("created")

MODIFIED("modified")

DELETED("deleted")

Type type

Optional<String> content

The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

Optional<String> contentSha256

Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

Optional<Long> contentSizeBytes

Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.



Optional<[BetaManagedAgentsActor](api/beta.md)> createdBy

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

One of the following:



class BetaManagedAgentsSessionActor:

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

String sessionId

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

Type type



class BetaManagedAgentsApiActor:

Attribution for a write made directly via the public API (outside of any session).

String apiKeyId

ID of the API key that performed the write. This identifies the key, not the secret.

Type type



class BetaManagedAgentsUserActor:

Attribution for a write made by a human user through the Anthropic Console.

Type type

String userId

ID of the user who performed the write (a `user_...` value).

Optional<String> path

The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

Optional<LocalDateTime> redactedAt

A timestamp in RFC 3339 format



Optional<[BetaManagedAgentsActor](api/beta.md)> redactedBy

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

One of the following:



class BetaManagedAgentsSessionActor:

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

String sessionId

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

Type type



class BetaManagedAgentsApiActor:

Attribution for a write made directly via the public API (outside of any session).

String apiKeyId

ID of the API key that performed the write. This identifies the key, not the secret.

Type type



class BetaManagedAgentsUserActor:

Attribution for a write made by a human user through the Anthropic Console.

Type type

String userId

ID of the user who performed the write (a `user_...` value).



enum BetaManagedAgentsMemoryVersionOperation:

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

CREATED("created")

MODIFIED("modified")

DELETED("deleted")



class BetaManagedAgentsSessionActor:

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

String sessionId

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

Type type



class BetaManagedAgentsUserActor:

Attribution for a write made by a human user through the Anthropic Console.

Type type

String userId

ID of the user who performed the write (a `user_...` value).

---

*Copyright © Anthropic. All rights reserved.*
