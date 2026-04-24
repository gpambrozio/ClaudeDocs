# Memory Stores

Copy page

CLI

# Memory Stores

##### [CreateMemoryStore](api/beta/memory_stores/create.md)

$ ant beta:memory-stores create

POST/v1/memory\_stores

##### [ListMemoryStores](api/beta/memory_stores/list.md)

$ ant beta:memory-stores list

GET/v1/memory\_stores

##### [GetMemoryStore](api/beta/memory_stores/retrieve.md)

$ ant beta:memory-stores retrieve

GET/v1/memory\_stores/{memory\_store\_id}

##### [UpdateMemoryStore](api/beta/memory_stores/update.md)

$ ant beta:memory-stores update

POST/v1/memory\_stores/{memory\_store\_id}

##### [DeleteMemoryStore](api/beta/memory_stores/delete.md)

$ ant beta:memory-stores delete

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [ArchiveMemoryStore](api/beta/memory_stores/archive.md)

$ ant beta:memory-stores archive

POST/v1/memory\_stores/{memory\_store\_id}/archive

##### ModelsExpand Collapse

beta\_managed\_agents\_deleted\_memory\_store: object { id, type }

id: string

type: "memory\_store\_deleted"

"memory\_store\_deleted"

beta\_managed\_agents\_memory\_store: object { id, type, archived\_at, 5 more }

id: string

type: "memory\_store"

"memory\_store"

archived\_at: optional string

A timestamp in RFC 3339 format

created\_at: optional string

A timestamp in RFC 3339 format

description: optional string

metadata: optional map[string]

name: optional string

updated\_at: optional string

A timestamp in RFC 3339 format

#### Memory StoresMemories

##### [CreateMemory](api/beta/memory_stores/memories/create.md)

$ ant beta:memory-stores:memories create

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [ListMemories](api/beta/memory_stores/memories/list.md)

$ ant beta:memory-stores:memories list

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [GetMemory](api/beta/memory_stores/memories/retrieve.md)

$ ant beta:memory-stores:memories retrieve

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [UpdateMemory](api/beta/memory_stores/memories/update.md)

$ ant beta:memory-stores:memories update

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [DeleteMemory](api/beta/memory_stores/memories/delete.md)

$ ant beta:memory-stores:memories delete

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### ModelsExpand Collapse

beta\_managed\_agents\_content\_sha256\_precondition: object { type, content\_sha256 }

type: "content\_sha256"

"content\_sha256"

content\_sha256: optional string

beta\_managed\_agents\_deleted\_memory: object { id, type }

id: string

type: "memory\_deleted"

"memory\_deleted"

beta\_managed\_agents\_memory: object { id, content\_sha256, content\_size\_bytes, 7 more }

id: string

content\_sha256: string

content\_size\_bytes: number

created\_at: string

A timestamp in RFC 3339 format

memory\_store\_id: string

memory\_version\_id: string

path: string

type: "memory"

"memory"

updated\_at: string

A timestamp in RFC 3339 format

content: optional string

beta\_managed\_agents\_memory\_list\_item: [BetaManagedAgentsMemory](api/beta.md) { id, content\_sha256, content\_size\_bytes, 7 more }  or [BetaManagedAgentsMemoryPrefix](api/beta.md) { path, type }

beta\_managed\_agents\_memory: object { id, content\_sha256, content\_size\_bytes, 7 more }

id: string

content\_sha256: string

content\_size\_bytes: number

created\_at: string

A timestamp in RFC 3339 format

memory\_store\_id: string

memory\_version\_id: string

path: string

type: "memory"

"memory"

updated\_at: string

A timestamp in RFC 3339 format

content: optional string

beta\_managed\_agents\_memory\_prefix: object { path, type }

path: string

type: "memory\_prefix"

"memory\_prefix"

beta\_managed\_agents\_memory\_path\_conflict\_error: object { type, conflicting\_memory\_id, conflicting\_path, message }

type: "memory\_path\_conflict\_error"

"memory\_path\_conflict\_error"

conflicting\_memory\_id: optional string

conflicting\_path: optional string

message: optional string

beta\_managed\_agents\_memory\_precondition\_failed\_error: object { type, message }

type: "memory\_precondition\_failed\_error"

"memory\_precondition\_failed\_error"

message: optional string

beta\_managed\_agents\_memory\_prefix: object { path, type }

path: string

type: "memory\_prefix"

"memory\_prefix"

beta\_managed\_agents\_memory\_view: "basic" or "full"

MemoryView enum

"basic"

"full"

beta\_managed\_agents\_precondition: object { type, content\_sha256 }

type: "content\_sha256"

"content\_sha256"

content\_sha256: optional string

#### Memory StoresMemory Versions

##### [ListMemoryVersions](api/beta/memory_stores/memory_versions/list.md)

$ ant beta:memory-stores:memory-versions list

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [GetMemoryVersion](api/beta/memory_stores/memory_versions/retrieve.md)

$ ant beta:memory-stores:memory-versions retrieve

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [RedactMemoryVersion](api/beta/memory_stores/memory_versions/redact.md)

$ ant beta:memory-stores:memory-versions redact

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

##### ModelsExpand Collapse

beta\_managed\_agents\_actor: [BetaManagedAgentsSessionActor](api/beta.md) { session\_id, type }  or [BetaManagedAgentsAPIActor](api/beta.md) { api\_key\_id, type }  or [BetaManagedAgentsUserActor](api/beta.md) { type, user\_id }

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

beta\_managed\_agents\_api\_actor: object { api\_key\_id, type }

api\_key\_id: string

type: "api\_actor"

"api\_actor"

beta\_managed\_agents\_memory\_version: object { id, created\_at, memory\_id, 10 more }

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

beta\_managed\_agents\_memory\_version\_operation: "created" or "modified" or "deleted"

MemoryVersionOperation enum

"created"

"modified"

"deleted"

beta\_managed\_agents\_session\_actor: object { session\_id, type }

session\_id: string

type: "session\_actor"

"session\_actor"

beta\_managed\_agents\_user\_actor: object { type, user\_id }

type: "user\_actor"

"user\_actor"

user\_id: string

---

*Copyright © Anthropic. All rights reserved.*
