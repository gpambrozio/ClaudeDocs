# Memory Stores

Copy page

cURL

# Memory Stores

##### [CreateMemoryStore](api/beta/memory_stores/create.md)

POST/v1/memory\_stores

##### [ListMemoryStores](api/beta/memory_stores/list.md)

GET/v1/memory\_stores

##### [GetMemoryStore](api/beta/memory_stores/retrieve.md)

GET/v1/memory\_stores/{memory\_store\_id}

##### [UpdateMemoryStore](api/beta/memory_stores/update.md)

POST/v1/memory\_stores/{memory\_store\_id}

##### [DeleteMemoryStore](api/beta/memory_stores/delete.md)

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [ArchiveMemoryStore](api/beta/memory_stores/archive.md)

POST/v1/memory\_stores/{memory\_store\_id}/archive

##### ModelsExpand Collapse

BetaManagedAgentsDeletedMemoryStore = object { id, type }

id: string

type: "memory\_store\_deleted"

BetaManagedAgentsMemoryStore = object { id, type, archived\_at, 5 more }

id: string

type: "memory\_store"

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

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [ListMemories](api/beta/memory_stores/memories/list.md)

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [GetMemory](api/beta/memory_stores/memories/retrieve.md)

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [UpdateMemory](api/beta/memory_stores/memories/update.md)

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [DeleteMemory](api/beta/memory_stores/memories/delete.md)

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### ModelsExpand Collapse

BetaManagedAgentsContentSha256Precondition = object { type, content\_sha256 }

type: "content\_sha256"

content\_sha256: optional string

BetaManagedAgentsDeletedMemory = object { id, type }

id: string

type: "memory\_deleted"

BetaManagedAgentsMemory = object { id, content\_sha256, content\_size\_bytes, 7 more }

id: string

content\_sha256: string

content\_size\_bytes: number

created\_at: string

A timestamp in RFC 3339 format

memory\_store\_id: string

memory\_version\_id: string

path: string

type: "memory"

updated\_at: string

A timestamp in RFC 3339 format

content: optional string

BetaManagedAgentsMemoryListItem = [BetaManagedAgentsMemory](api/beta.md) { id, content\_sha256, content\_size\_bytes, 7 more }  or [BetaManagedAgentsMemoryPrefix](api/beta.md) { path, type }

Accepts one of the following:

BetaManagedAgentsMemory = object { id, content\_sha256, content\_size\_bytes, 7 more }

id: string

content\_sha256: string

content\_size\_bytes: number

created\_at: string

A timestamp in RFC 3339 format

memory\_store\_id: string

memory\_version\_id: string

path: string

type: "memory"

updated\_at: string

A timestamp in RFC 3339 format

content: optional string

BetaManagedAgentsMemoryPrefix = object { path, type }

path: string

type: "memory\_prefix"

BetaManagedAgentsMemoryPathConflictError = object { type, conflicting\_memory\_id, conflicting\_path, message }

type: "memory\_path\_conflict\_error"

conflicting\_memory\_id: optional string

conflicting\_path: optional string

message: optional string

BetaManagedAgentsMemoryPreconditionFailedError = object { type, message }

type: "memory\_precondition\_failed\_error"

message: optional string

BetaManagedAgentsMemoryPrefix = object { path, type }

path: string

type: "memory\_prefix"

BetaManagedAgentsMemoryView = "basic" or "full"

MemoryView enum

Accepts one of the following:

"basic"

"full"

BetaManagedAgentsPrecondition = object { type, content\_sha256 }

type: "content\_sha256"

content\_sha256: optional string

#### Memory StoresMemory Versions

##### [ListMemoryVersions](api/beta/memory_stores/memory_versions/list.md)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [GetMemoryVersion](api/beta/memory_stores/memory_versions/retrieve.md)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [RedactMemoryVersion](api/beta/memory_stores/memory_versions/redact.md)

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

##### ModelsExpand Collapse

BetaManagedAgentsActor = [BetaManagedAgentsSessionActor](api/beta.md) { session\_id, type }  or [BetaManagedAgentsAPIActor](api/beta.md) { api\_key\_id, type }  or [BetaManagedAgentsUserActor](api/beta.md) { type, user\_id }

Accepts one of the following:

BetaManagedAgentsSessionActor = object { session\_id, type }

session\_id: string

type: "session\_actor"

BetaManagedAgentsAPIActor = object { api\_key\_id, type }

api\_key\_id: string

type: "api\_actor"

BetaManagedAgentsUserActor = object { type, user\_id }

type: "user\_actor"

user\_id: string

BetaManagedAgentsAPIActor = object { api\_key\_id, type }

api\_key\_id: string

type: "api\_actor"

BetaManagedAgentsMemoryVersion = object { id, created\_at, memory\_id, 10 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

memory\_id: string

memory\_store\_id: string

operation: [BetaManagedAgentsMemoryVersionOperation](api/beta.md)

MemoryVersionOperation enum

Accepts one of the following:

"created"

"modified"

"deleted"

type: "memory\_version"

content: optional string

content\_sha256: optional string

content\_size\_bytes: optional number

created\_by: optional [BetaManagedAgentsActor](api/beta.md)

Accepts one of the following:

BetaManagedAgentsSessionActor = object { session\_id, type }

session\_id: string

type: "session\_actor"

BetaManagedAgentsAPIActor = object { api\_key\_id, type }

api\_key\_id: string

type: "api\_actor"

BetaManagedAgentsUserActor = object { type, user\_id }

type: "user\_actor"

user\_id: string

path: optional string

redacted\_at: optional string

A timestamp in RFC 3339 format

redacted\_by: optional [BetaManagedAgentsActor](api/beta.md)

Accepts one of the following:

BetaManagedAgentsSessionActor = object { session\_id, type }

session\_id: string

type: "session\_actor"

BetaManagedAgentsAPIActor = object { api\_key\_id, type }

api\_key\_id: string

type: "api\_actor"

BetaManagedAgentsUserActor = object { type, user\_id }

type: "user\_actor"

user\_id: string

BetaManagedAgentsMemoryVersionOperation = "created" or "modified" or "deleted"

MemoryVersionOperation enum

Accepts one of the following:

"created"

"modified"

"deleted"

BetaManagedAgentsSessionActor = object { session\_id, type }

session\_id: string

type: "session\_actor"

BetaManagedAgentsUserActor = object { type, user\_id }

type: "user\_actor"

user\_id: string

---

*Copyright © Anthropic. All rights reserved.*
