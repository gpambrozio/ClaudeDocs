# Memory Versions

Copy page

CLI

# Memory Versions

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
