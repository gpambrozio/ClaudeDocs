# Memory Versions

Copy page

TypeScript

# Memory Versions

##### [ListMemoryVersions](api/beta/memory_stores/memory_versions/list.md)

client.beta.memoryStores.memoryVersions.list(stringmemoryStoreID, MemoryVersionListParams { api\_key\_id, createdAtGte, createdAtLte, 7 more } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsMemoryVersion](api/beta.md) { id, created\_at, memory\_id, 10 more } >

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [GetMemoryVersion](api/beta/memory_stores/memory_versions/retrieve.md)

client.beta.memoryStores.memoryVersions.retrieve(stringmemoryVersionID, MemoryVersionRetrieveParams { memory\_store\_id, view, betas } params, RequestOptionsoptions?): [BetaManagedAgentsMemoryVersion](api/beta.md) { id, created\_at, memory\_id, 10 more }

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [RedactMemoryVersion](api/beta/memory_stores/memory_versions/redact.md)

client.beta.memoryStores.memoryVersions.redact(stringmemoryVersionID, MemoryVersionRedactParams { memory\_store\_id, betas } params, RequestOptionsoptions?): [BetaManagedAgentsMemoryVersion](api/beta.md) { id, created\_at, memory\_id, 10 more }

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

##### ModelsExpand Collapse

BetaManagedAgentsActor = [BetaManagedAgentsSessionActor](api/beta.md) { session\_id, type }  | [BetaManagedAgentsAPIActor](api/beta.md) { api\_key\_id, type }  | [BetaManagedAgentsUserActor](api/beta.md) { type, user\_id }

Accepts one of the following:

BetaManagedAgentsSessionActor { session\_id, type }

session\_id: string

type: "session\_actor"

BetaManagedAgentsAPIActor { api\_key\_id, type }

api\_key\_id: string

type: "api\_actor"

BetaManagedAgentsUserActor { type, user\_id }

type: "user\_actor"

user\_id: string

BetaManagedAgentsAPIActor { api\_key\_id, type }

api\_key\_id: string

type: "api\_actor"

BetaManagedAgentsMemoryVersion { id, created\_at, memory\_id, 10 more }

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

content?: string | null

content\_sha256?: string | null

content\_size\_bytes?: number | null

created\_by?: [BetaManagedAgentsActor](api/beta.md)

Accepts one of the following:

BetaManagedAgentsSessionActor { session\_id, type }

session\_id: string

type: "session\_actor"

BetaManagedAgentsAPIActor { api\_key\_id, type }

api\_key\_id: string

type: "api\_actor"

BetaManagedAgentsUserActor { type, user\_id }

type: "user\_actor"

user\_id: string

path?: string | null

redacted\_at?: string | null

A timestamp in RFC 3339 format

redacted\_by?: [BetaManagedAgentsActor](api/beta.md)

Accepts one of the following:

BetaManagedAgentsSessionActor { session\_id, type }

session\_id: string

type: "session\_actor"

BetaManagedAgentsAPIActor { api\_key\_id, type }

api\_key\_id: string

type: "api\_actor"

BetaManagedAgentsUserActor { type, user\_id }

type: "user\_actor"

user\_id: string

BetaManagedAgentsMemoryVersionOperation = "created" | "modified" | "deleted"

MemoryVersionOperation enum

Accepts one of the following:

"created"

"modified"

"deleted"

BetaManagedAgentsSessionActor { session\_id, type }

session\_id: string

type: "session\_actor"

BetaManagedAgentsUserActor { type, user\_id }

type: "user\_actor"

user\_id: string

---

*Copyright © Anthropic. All rights reserved.*
