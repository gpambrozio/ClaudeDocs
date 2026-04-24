# Memories

Copy page

CLI

# Memories

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

---

*Copyright © Anthropic. All rights reserved.*
