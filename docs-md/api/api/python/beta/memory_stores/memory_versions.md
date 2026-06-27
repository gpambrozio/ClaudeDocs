# Memory Versions

Copy page



Python

# Memory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

beta.memory\_stores.memory\_versions.list(strmemory\_store\_id, MemoryVersionListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md)]

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

beta.memory\_stores.memory\_versions.retrieve(strmemory\_version\_id, MemoryVersionRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

beta.memory\_stores.memory\_versions.redact(strmemory\_version\_id, MemoryVersionRedactParams\*\*kwargs)  -> [BetaManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md)

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

##### ModelsExpand Collapse



[BetaManagedAgentsActor](api/beta/memory_stores/memory_versions.md)

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

One of the following:



class BetaManagedAgentsSessionActor: …

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: str

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: Literal["session\_actor"]



class BetaManagedAgentsAPIActor: …

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: str

ID of the API key that performed the write. This identifies the key, not the secret.

type: Literal["api\_actor"]



class BetaManagedAgentsUserActor: …

Attribution for a write made by a human user through the Anthropic Console.

type: Literal["user\_actor"]

user\_id: str

ID of the user who performed the write (a `user_...` value).



class BetaManagedAgentsAPIActor: …

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: str

ID of the API key that performed the write. This identifies the key, not the secret.

type: Literal["api\_actor"]



class BetaManagedAgentsMemoryVersion: …

A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

id: str

Unique identifier for this version (a `memver_...` value).

created\_at: datetime

A timestamp in RFC 3339 format

memory\_id: str

ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](api/beta/memory_stores/memory_versions/list.md) to retrieve the full lineage including the `deleted` row.

memory\_store\_id: str

ID of the memory store this version belongs to (a `memstore_...` value).



operation: [BetaManagedAgentsMemoryVersionOperation](api/beta/memory_stores/memory_versions.md)

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

One of the following:

"created"

"modified"

"deleted"

type: Literal["memory\_version"]

content: Optional[str]

The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

content\_sha256: Optional[str]

Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

content\_size\_bytes: Optional[int]

Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.



created\_by: Optional[BetaManagedAgentsActor]

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

One of the following:



class BetaManagedAgentsSessionActor: …

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: str

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: Literal["session\_actor"]



class BetaManagedAgentsAPIActor: …

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: str

ID of the API key that performed the write. This identifies the key, not the secret.

type: Literal["api\_actor"]



class BetaManagedAgentsUserActor: …

Attribution for a write made by a human user through the Anthropic Console.

type: Literal["user\_actor"]

user\_id: str

ID of the user who performed the write (a `user_...` value).

path: Optional[str]

The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

redacted\_at: Optional[datetime]

A timestamp in RFC 3339 format



redacted\_by: Optional[BetaManagedAgentsActor]

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

One of the following:



class BetaManagedAgentsSessionActor: …

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: str

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: Literal["session\_actor"]



class BetaManagedAgentsAPIActor: …

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: str

ID of the API key that performed the write. This identifies the key, not the secret.

type: Literal["api\_actor"]



class BetaManagedAgentsUserActor: …

Attribution for a write made by a human user through the Anthropic Console.

type: Literal["user\_actor"]

user\_id: str

ID of the user who performed the write (a `user_...` value).



Literal["created", "modified", "deleted"]

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

One of the following:

"created"

"modified"

"deleted"



class BetaManagedAgentsSessionActor: …

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: str

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: Literal["session\_actor"]



class BetaManagedAgentsUserActor: …

Attribution for a write made by a human user through the Anthropic Console.

type: Literal["user\_actor"]

user\_id: str

ID of the user who performed the write (a `user_...` value).

---

*Copyright © Anthropic. All rights reserved.*
