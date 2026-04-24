# Memories

Copy page

cURL

# Memories

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

---

*Copyright © Anthropic. All rights reserved.*
