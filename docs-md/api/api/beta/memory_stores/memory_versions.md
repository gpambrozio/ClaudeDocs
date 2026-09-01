# Memory Versions

Copy page



cURL

# Memory Versions

##### [List memory versions](api/http/beta/memory_stores/memory_versions/list.md)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/http/beta/memory_stores/memory_versions/retrieve.md)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/http/beta/memory_stores/memory_versions/redact.md)

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

##### Models



BetaManagedAgentsActor = [BetaManagedAgentsSessionActor](api/http/beta/memory_stores/memory_versions.md) { session\_id, type } or [BetaManagedAgentsAPIActor](api/http/beta/memory_stores/memory_versions.md) { api\_key\_id, type } or [BetaManagedAgentsUserActor](api/http/beta/memory_stores/memory_versions.md) { type, user\_id } or [BetaManagedAgentsServiceAccountActor](api/http/beta/memory_stores/memory_versions.md) { service\_account\_id, type }

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

One of the following:



BetaManagedAgentsAPIActor object{ api\_key\_id, type }

Attribution for a write made directly via the public API (outside of any session).



api\_key\_id: string

ID of the API key that performed the write. This identifies the key, not the secret.

minLength1

type: "api\_actor"



BetaManagedAgentsMemoryVersion object{ id, created\_at, memory\_id, 10 more }

A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and are not deleted with the memory; each version is retained for at least the version retention period after it was written, unless the store itself is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.



BetaManagedAgentsMemoryVersionOperation = "created" or "modified" or "deleted"

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

One of the following:

"created"

"modified"

"deleted"



BetaManagedAgentsServiceAccountActor object{ service\_account\_id, type }

Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.



service\_account\_id: string

ID of the service account that performed the write (a `svac_...` value).

minLength1

type: "service\_account\_actor"



BetaManagedAgentsSessionActor object{ session\_id, type }

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.



session\_id: string

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

minLength1

type: "session\_actor"



BetaManagedAgentsUserActor object{ type, user\_id }

Attribution for a write made by a human user through the Anthropic Console.

type: "user\_actor"



user\_id: string

ID of the user who performed the write (a `user_...` value).

minLength1

---

*Copyright © Anthropic. All rights reserved.*
