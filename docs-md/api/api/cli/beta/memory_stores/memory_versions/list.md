# ListMemoryVersions

Copy page

CLI

# ListMemoryVersions

$ ant beta:memory-stores:memory-versions list

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

ListMemoryVersions

##### ParametersExpand Collapse

--memory-store-id: string

Path param: Path parameter memory\_store\_id

--api-key-id: optional string

Query param: Query parameter for api\_key\_id

--created-at-gte: optional string

Query param: Return versions created at or after this time (inclusive).

--created-at-lte: optional string

Query param: Return versions created at or before this time (inclusive).

--limit: optional number

Query param: Query parameter for limit

--memory-id: optional string

Query param: Query parameter for memory\_id

--operation: optional "created" or "modified" or "deleted"

Query param: Query parameter for operation

--page: optional string

Query param: Query parameter for page

--session-id: optional string

Query param: Query parameter for session\_id

--view: optional "basic" or "full"

Query param: Query parameter for view

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

BetaManagedAgentsListMemoryVersionsResult: object { data, next\_page }

data: optional array of [BetaManagedAgentsMemoryVersion](api/beta.md) { id, created\_at, memory\_id, 10 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

memory\_id: string

memory\_store\_id: string

operation: "created" or "modified" or "deleted"

MemoryVersionOperation enum

"created"

"modified"

"deleted"

type: "memory\_version"

"memory\_version"

content: optional string

content\_sha256: optional string

content\_size\_bytes: optional number

created\_by: optional [BetaManagedAgentsSessionActor](api/beta.md) { session\_id, type }  or [BetaManagedAgentsAPIActor](api/beta.md) { api\_key\_id, type }  or [BetaManagedAgentsUserActor](api/beta.md) { type, user\_id }

beta\_managed\_agents\_session\_actor: object { session\_id, type }

session\_id: string

type: "session\_actor"

"session\_actor"

beta\_managed\_agents\_api\_actor: object { api\_key\_id, type }

api\_key\_id: string

type: "api\_actor"

"api\_actor"

beta\_managed\_agents\_user\_actor: object { type, user\_id }

type: "user\_actor"

"user\_actor"

user\_id: string

path: optional string

redacted\_at: optional string

A timestamp in RFC 3339 format

redacted\_by: optional [BetaManagedAgentsSessionActor](api/beta.md) { session\_id, type }  or [BetaManagedAgentsAPIActor](api/beta.md) { api\_key\_id, type }  or [BetaManagedAgentsUserActor](api/beta.md) { type, user\_id }

beta\_managed\_agents\_session\_actor: object { session\_id, type }

session\_id: string

type: "session\_actor"

"session\_actor"

beta\_managed\_agents\_api\_actor: object { api\_key\_id, type }

api\_key\_id: string

type: "api\_actor"

"api\_actor"

beta\_managed\_agents\_user\_actor: object { type, user\_id }

type: "user\_actor"

"user\_actor"

user\_id: string

next\_page: optional string

ListMemoryVersions

CLI

```shiki
ant beta:memory-stores:memory-versions list \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

Response 200

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
