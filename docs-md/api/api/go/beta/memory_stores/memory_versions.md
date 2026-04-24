# Memory Versions

Copy page

Go

# Memory Versions

##### [ListMemoryVersions](api/beta/memory_stores/memory_versions/list.md)

client.Beta.MemoryStores.MemoryVersions.List(ctx, memoryStoreID, params) (\*PageCursor[[BetaManagedAgentsMemoryVersion](api/beta.md)], error)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [GetMemoryVersion](api/beta/memory_stores/memory_versions/retrieve.md)

client.Beta.MemoryStores.MemoryVersions.Get(ctx, memoryVersionID, params) (\*[BetaManagedAgentsMemoryVersion](api/beta.md), error)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [RedactMemoryVersion](api/beta/memory_stores/memory_versions/redact.md)

client.Beta.MemoryStores.MemoryVersions.Redact(ctx, memoryVersionID, params) (\*[BetaManagedAgentsMemoryVersion](api/beta.md), error)

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

##### ModelsExpand Collapse

type BetaManagedAgentsActorUnion interface{…}

Accepts one of the following:

type BetaManagedAgentsSessionActor struct{…}

SessionID string

Type BetaManagedAgentsSessionActorType

type BetaManagedAgentsAPIActor struct{…}

APIKeyID string

Type BetaManagedAgentsAPIActorType

type BetaManagedAgentsUserActor struct{…}

Type BetaManagedAgentsUserActorType

UserID string

type BetaManagedAgentsAPIActor struct{…}

APIKeyID string

Type BetaManagedAgentsAPIActorType

type BetaManagedAgentsMemoryVersion struct{…}

ID string

CreatedAt Time

A timestamp in RFC 3339 format

MemoryID string

MemoryStoreID string

Operation [BetaManagedAgentsMemoryVersionOperation](api/beta.md)

MemoryVersionOperation enum

Accepts one of the following:

const BetaManagedAgentsMemoryVersionOperationCreated [BetaManagedAgentsMemoryVersionOperation](api/beta.md) = "created"

const BetaManagedAgentsMemoryVersionOperationModified [BetaManagedAgentsMemoryVersionOperation](api/beta.md) = "modified"

const BetaManagedAgentsMemoryVersionOperationDeleted [BetaManagedAgentsMemoryVersionOperation](api/beta.md) = "deleted"

Type BetaManagedAgentsMemoryVersionType

Content stringoptional

ContentSha256 stringoptional

ContentSizeBytes int64optional

CreatedBy [BetaManagedAgentsActorUnion](api/beta.md)optional

Accepts one of the following:

type BetaManagedAgentsSessionActor struct{…}

SessionID string

Type BetaManagedAgentsSessionActorType

type BetaManagedAgentsAPIActor struct{…}

APIKeyID string

Type BetaManagedAgentsAPIActorType

type BetaManagedAgentsUserActor struct{…}

Type BetaManagedAgentsUserActorType

UserID string

Path stringoptional

RedactedAt Timeoptional

A timestamp in RFC 3339 format

RedactedBy [BetaManagedAgentsActorUnion](api/beta.md)optional

Accepts one of the following:

type BetaManagedAgentsSessionActor struct{…}

SessionID string

Type BetaManagedAgentsSessionActorType

type BetaManagedAgentsAPIActor struct{…}

APIKeyID string

Type BetaManagedAgentsAPIActorType

type BetaManagedAgentsUserActor struct{…}

Type BetaManagedAgentsUserActorType

UserID string

type BetaManagedAgentsMemoryVersionOperation string

MemoryVersionOperation enum

Accepts one of the following:

const BetaManagedAgentsMemoryVersionOperationCreated [BetaManagedAgentsMemoryVersionOperation](api/beta.md) = "created"

const BetaManagedAgentsMemoryVersionOperationModified [BetaManagedAgentsMemoryVersionOperation](api/beta.md) = "modified"

const BetaManagedAgentsMemoryVersionOperationDeleted [BetaManagedAgentsMemoryVersionOperation](api/beta.md) = "deleted"

type BetaManagedAgentsSessionActor struct{…}

SessionID string

Type BetaManagedAgentsSessionActorType

type BetaManagedAgentsUserActor struct{…}

Type BetaManagedAgentsUserActorType

UserID string

---

*Copyright © Anthropic. All rights reserved.*
