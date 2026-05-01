# Memory Versions

Copy page

CLI

# Memory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

$ ant beta:memory-stores:memory-versions list

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

$ ant beta:memory-stores:memory-versions retrieve

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

$ ant beta:memory-stores:memory-versions redact

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

##### ModelsExpand Collapse

beta\_managed\_agents\_actor: [BetaManagedAgentsSessionActor](api/beta.md) { session\_id, type }  or [BetaManagedAgentsAPIActor](api/beta.md) { api\_key\_id, type }  or [BetaManagedAgentsUserActor](api/beta.md) { type, user\_id }

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

beta\_managed\_agents\_session\_actor: object { session\_id, type }

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: string

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: "session\_actor"

"session\_actor"

beta\_managed\_agents\_api\_actor: object { api\_key\_id, type }

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: string

ID of the API key that performed the write. This identifies the key, not the secret.

type: "api\_actor"

"api\_actor"

beta\_managed\_agents\_user\_actor: object { type, user\_id }

Attribution for a write made by a human user through the Anthropic Console.

type: "user\_actor"

"user\_actor"

user\_id: string

ID of the user who performed the write (a `user_...` value).

beta\_managed\_agents\_api\_actor: object { api\_key\_id, type }

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: string

ID of the API key that performed the write. This identifies the key, not the secret.

type: "api\_actor"

"api\_actor"

beta\_managed\_agents\_memory\_version: object { id, created\_at, memory\_id, 10 more }

A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

id: string

Unique identifier for this version (a `memver_...` value).

created\_at: string

A timestamp in RFC 3339 format

memory\_id: string

ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](api/beta/memory_stores/memory_versions/list.md) to retrieve the full lineage including the `deleted` row.

memory\_store\_id: string

ID of the memory store this version belongs to (a `memstore_...` value).

operation: "created" or "modified" or "deleted"

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

"created"

"modified"

"deleted"

type: "memory\_version"

"memory\_version"

content: optional string

The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

content\_sha256: optional string

Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

content\_size\_bytes: optional number

Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

created\_by: optional [BetaManagedAgentsSessionActor](api/beta.md) { session\_id, type }  or [BetaManagedAgentsAPIActor](api/beta.md) { api\_key\_id, type }  or [BetaManagedAgentsUserActor](api/beta.md) { type, user\_id }

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

beta\_managed\_agents\_session\_actor: object { session\_id, type }

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: string

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: "session\_actor"

"session\_actor"

beta\_managed\_agents\_api\_actor: object { api\_key\_id, type }

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: string

ID of the API key that performed the write. This identifies the key, not the secret.

type: "api\_actor"

"api\_actor"

beta\_managed\_agents\_user\_actor: object { type, user\_id }

Attribution for a write made by a human user through the Anthropic Console.

type: "user\_actor"

"user\_actor"

user\_id: string

ID of the user who performed the write (a `user_...` value).

path: optional string

The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

redacted\_at: optional string

A timestamp in RFC 3339 format

redacted\_by: optional [BetaManagedAgentsSessionActor](api/beta.md) { session\_id, type }  or [BetaManagedAgentsAPIActor](api/beta.md) { api\_key\_id, type }  or [BetaManagedAgentsUserActor](api/beta.md) { type, user\_id }

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

beta\_managed\_agents\_session\_actor: object { session\_id, type }

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: string

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: "session\_actor"

"session\_actor"

beta\_managed\_agents\_api\_actor: object { api\_key\_id, type }

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: string

ID of the API key that performed the write. This identifies the key, not the secret.

type: "api\_actor"

"api\_actor"

beta\_managed\_agents\_user\_actor: object { type, user\_id }

Attribution for a write made by a human user through the Anthropic Console.

type: "user\_actor"

"user\_actor"

user\_id: string

ID of the user who performed the write (a `user_...` value).

beta\_managed\_agents\_memory\_version\_operation: "created" or "modified" or "deleted"

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

"created"

"modified"

"deleted"

beta\_managed\_agents\_session\_actor: object { session\_id, type }

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: string

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: "session\_actor"

"session\_actor"

beta\_managed\_agents\_user\_actor: object { type, user\_id }

Attribution for a write made by a human user through the Anthropic Console.

type: "user\_actor"

"user\_actor"

user\_id: string

ID of the user who performed the write (a `user_...` value).

---

*Copyright © Anthropic. All rights reserved.*
