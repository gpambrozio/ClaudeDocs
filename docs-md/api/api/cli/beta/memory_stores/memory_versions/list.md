# List memory versions

Copy page



CLI

# List memory versions

$ ant beta:memory-stores:memory-versions list

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

List memory versions

##### ParametersExpand Collapse

--memory-store-id: string

Path param: Path parameter memory\_store\_id

--api-key-id: optional string

Query param: Query parameter for api\_key\_id

--created-at-gte: optional string

Query param: Return versions created at or after this time (inclusive).

--created-at-lte: optional string

Query param: Return versions created at or before this time (inclusive).

--limit: optional number

Query param: Query parameter for limit

--memory-id: optional string

Query param: Query parameter for memory\_id

--operation: optional "created" or "modified" or "deleted"

Query param: Query parameter for operation

--page: optional string

Query param: Query parameter for page

--session-id: optional string

Query param: Query parameter for session\_id

--view: optional "basic" or "full"

Query param: Query parameter for view

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



BetaManagedAgentsListMemoryVersionsResult: object { data, next\_page } 

Response payload for [List memory versions](api/beta/memory_stores/memory_versions/list.md).



data: optional array of [BetaManagedAgentsMemoryVersion](api/beta.md) { id, created\_at, memory\_id, 10 more } 

One page of `memory_version` objects, ordered by `created_at` descending (newest first), with `id` as tiebreak.

id: string

Unique identifier for this version (a `memver_...` value).

created\_at: string

A timestamp in RFC 3339 format

memory\_id: string

ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](api/beta/memory_stores/memory_versions/list.md) to retrieve the full lineage including the `deleted` row.

memory\_store\_id: string

ID of the memory store this version belongs to (a `memstore_...` value).



operation: "created" or "modified" or "deleted"

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

"created"

"modified"

"deleted"



type: "memory\_version"

"memory\_version"

content: optional string

The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

content\_sha256: optional string

Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

content\_size\_bytes: optional number

Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.



created\_by: optional [BetaManagedAgentsSessionActor](api/beta.md) { session\_id, type }  or [BetaManagedAgentsAPIActor](api/beta.md) { api\_key\_id, type }  or [BetaManagedAgentsUserActor](api/beta.md) { type, user\_id } 

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).



beta\_managed\_agents\_session\_actor: object { session\_id, type } 

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: string

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.



type: "session\_actor"

"session\_actor"



beta\_managed\_agents\_api\_actor: object { api\_key\_id, type } 

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: string

ID of the API key that performed the write. This identifies the key, not the secret.



type: "api\_actor"

"api\_actor"



beta\_managed\_agents\_user\_actor: object { type, user\_id } 

Attribution for a write made by a human user through the Anthropic Console.



type: "user\_actor"

"user\_actor"

user\_id: string

ID of the user who performed the write (a `user_...` value).

path: optional string

The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

redacted\_at: optional string

A timestamp in RFC 3339 format



redacted\_by: optional [BetaManagedAgentsSessionActor](api/beta.md) { session\_id, type }  or [BetaManagedAgentsAPIActor](api/beta.md) { api\_key\_id, type }  or [BetaManagedAgentsUserActor](api/beta.md) { type, user\_id } 

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).



beta\_managed\_agents\_session\_actor: object { session\_id, type } 

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: string

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.



type: "session\_actor"

"session\_actor"



beta\_managed\_agents\_api\_actor: object { api\_key\_id, type } 

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: string

ID of the API key that performed the write. This identifies the key, not the secret.



type: "api\_actor"

"api\_actor"



beta\_managed\_agents\_user\_actor: object { type, user\_id } 

Attribution for a write made by a human user through the Anthropic Console.



type: "user\_actor"

"user\_actor"

user\_id: string

ID of the user who performed the write (a `user_...` value).

next\_page: optional string

Opaque cursor for the next page (a `page_...` value), or `null` if there are no more results. Pass as `page` on the next request.

List memory versions

CLI

```shiki
ant beta:memory-stores:memory-versions list \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
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
