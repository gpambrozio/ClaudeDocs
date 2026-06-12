# Memory Versions

Copy page

SDK language

Ruby

# Memory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

beta.memory\_stores.memory\_versions.list(memory\_store\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsMemoryVersion](api/beta.md) { id, created\_at, memory\_id, 10 more } >

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

beta.memory\_stores.memory\_versions.retrieve(memory\_version\_id, \*\*kwargs) -> [BetaManagedAgentsMemoryVersion](api/beta.md) { id, created\_at, memory\_id, 10 more }

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

beta.memory\_stores.memory\_versions.redact(memory\_version\_id, \*\*kwargs) -> [BetaManagedAgentsMemoryVersion](api/beta.md) { id, created\_at, memory\_id, 10 more }

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

##### ModelsExpand Collapse



BetaManagedAgentsActor = [BetaManagedAgentsSessionActor](api/beta.md) { session\_id, type }  | [BetaManagedAgentsAPIActor](api/beta.md) { api\_key\_id, type }  | [BetaManagedAgentsUserActor](api/beta.md) { type, user\_id } 

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

One of the following:



class BetaManagedAgentsSessionActor { session\_id, type } 

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: String

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: :session\_actor



class BetaManagedAgentsAPIActor { api\_key\_id, type } 

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: String

ID of the API key that performed the write. This identifies the key, not the secret.

type: :api\_actor



class BetaManagedAgentsUserActor { type, user\_id } 

Attribution for a write made by a human user through the Anthropic Console.

type: :user\_actor

user\_id: String

ID of the user who performed the write (a `user_...` value).



class BetaManagedAgentsAPIActor { api\_key\_id, type } 

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: String

ID of the API key that performed the write. This identifies the key, not the secret.

type: :api\_actor



class BetaManagedAgentsMemoryVersion { id, created\_at, memory\_id, 10 more } 

A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

id: String

Unique identifier for this version (a `memver_...` value).

created\_at: Time

A timestamp in RFC 3339 format

memory\_id: String

ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](api/beta/memory_stores/memory_versions/list.md) to retrieve the full lineage including the `deleted` row.

memory\_store\_id: String

ID of the memory store this version belongs to (a `memstore_...` value).



operation: [BetaManagedAgentsMemoryVersionOperation](api/beta.md)

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

One of the following:

:created

:modified

:deleted

type: :memory\_version

content: String

The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

content\_sha256: String

Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

content\_size\_bytes: Integer

Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.



created\_by: [BetaManagedAgentsActor](api/beta.md)

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

One of the following:



class BetaManagedAgentsSessionActor { session\_id, type } 

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: String

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: :session\_actor



class BetaManagedAgentsAPIActor { api\_key\_id, type } 

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: String

ID of the API key that performed the write. This identifies the key, not the secret.

type: :api\_actor



class BetaManagedAgentsUserActor { type, user\_id } 

Attribution for a write made by a human user through the Anthropic Console.

type: :user\_actor

user\_id: String

ID of the user who performed the write (a `user_...` value).

path: String

The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

redacted\_at: Time

A timestamp in RFC 3339 format



redacted\_by: [BetaManagedAgentsActor](api/beta.md)

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

One of the following:



class BetaManagedAgentsSessionActor { session\_id, type } 

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: String

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: :session\_actor



class BetaManagedAgentsAPIActor { api\_key\_id, type } 

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: String

ID of the API key that performed the write. This identifies the key, not the secret.

type: :api\_actor



class BetaManagedAgentsUserActor { type, user\_id } 

Attribution for a write made by a human user through the Anthropic Console.

type: :user\_actor

user\_id: String

ID of the user who performed the write (a `user_...` value).



BetaManagedAgentsMemoryVersionOperation = :created | :modified | :deleted

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

One of the following:

:created

:modified

:deleted



class BetaManagedAgentsSessionActor { session\_id, type } 

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: String

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: :session\_actor



class BetaManagedAgentsUserActor { type, user\_id } 

Attribution for a write made by a human user through the Anthropic Console.

type: :user\_actor

user\_id: String

ID of the user who performed the write (a `user_...` value).

---

*Copyright © Anthropic. All rights reserved.*
