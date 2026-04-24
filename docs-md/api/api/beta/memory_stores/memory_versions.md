# Memory Versions

Copy page

cURL

# Memory Versions

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
