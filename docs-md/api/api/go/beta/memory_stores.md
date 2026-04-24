# Memory Stores

Copy page

Go

# Memory Stores

##### [CreateMemoryStore](api/beta/memory_stores/create.md)

client.Beta.MemoryStores.New(ctx, params) (\*[BetaManagedAgentsMemoryStore](api/beta.md), error)

POST/v1/memory\_stores

##### [ListMemoryStores](api/beta/memory_stores/list.md)

client.Beta.MemoryStores.List(ctx, params) (\*PageCursor[[BetaManagedAgentsMemoryStore](api/beta.md)], error)

GET/v1/memory\_stores

##### [GetMemoryStore](api/beta/memory_stores/retrieve.md)

client.Beta.MemoryStores.Get(ctx, memoryStoreID, query) (\*[BetaManagedAgentsMemoryStore](api/beta.md), error)

GET/v1/memory\_stores/{memory\_store\_id}

##### [UpdateMemoryStore](api/beta/memory_stores/update.md)

client.Beta.MemoryStores.Update(ctx, memoryStoreID, params) (\*[BetaManagedAgentsMemoryStore](api/beta.md), error)

POST/v1/memory\_stores/{memory\_store\_id}

##### [DeleteMemoryStore](api/beta/memory_stores/delete.md)

client.Beta.MemoryStores.Delete(ctx, memoryStoreID, body) (\*[BetaManagedAgentsDeletedMemoryStore](api/beta.md), error)

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [ArchiveMemoryStore](api/beta/memory_stores/archive.md)

client.Beta.MemoryStores.Archive(ctx, memoryStoreID, body) (\*[BetaManagedAgentsMemoryStore](api/beta.md), error)

POST/v1/memory\_stores/{memory\_store\_id}/archive

##### ModelsExpand Collapse

type BetaManagedAgentsDeletedMemoryStore struct{…}

ID string

Type BetaManagedAgentsDeletedMemoryStoreType

type BetaManagedAgentsMemoryStore struct{…}

ID string

Type BetaManagedAgentsMemoryStoreType

ArchivedAt Timeoptional

A timestamp in RFC 3339 format

CreatedAt Timeoptional

A timestamp in RFC 3339 format

Description stringoptional

Metadata map[string, string]optional

Name stringoptional

UpdatedAt Timeoptional

A timestamp in RFC 3339 format

#### Memory StoresMemories

##### [CreateMemory](api/beta/memory_stores/memories/create.md)

client.Beta.MemoryStores.Memories.New(ctx, memoryStoreID, params) (\*[BetaManagedAgentsMemory](api/beta.md), error)

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [ListMemories](api/beta/memory_stores/memories/list.md)

client.Beta.MemoryStores.Memories.List(ctx, memoryStoreID, params) (\*PageCursor[[BetaManagedAgentsMemoryListItemUnion](api/beta.md)], error)

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [GetMemory](api/beta/memory_stores/memories/retrieve.md)

client.Beta.MemoryStores.Memories.Get(ctx, memoryID, params) (\*[BetaManagedAgentsMemory](api/beta.md), error)

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [UpdateMemory](api/beta/memory_stores/memories/update.md)

client.Beta.MemoryStores.Memories.Update(ctx, memoryID, params) (\*[BetaManagedAgentsMemory](api/beta.md), error)

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [DeleteMemory](api/beta/memory_stores/memories/delete.md)

client.Beta.MemoryStores.Memories.Delete(ctx, memoryID, params) (\*[BetaManagedAgentsDeletedMemory](api/beta.md), error)

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### ModelsExpand Collapse

type BetaManagedAgentsContentSha256Precondition struct{…}

Type BetaManagedAgentsContentSha256PreconditionType

ContentSha256 stringoptional

type BetaManagedAgentsDeletedMemory struct{…}

ID string

Type BetaManagedAgentsDeletedMemoryType

type BetaManagedAgentsMemory struct{…}

ID string

ContentSha256 string

ContentSizeBytes int64

CreatedAt Time

A timestamp in RFC 3339 format

MemoryStoreID string

MemoryVersionID string

Path string

Type BetaManagedAgentsMemoryType

UpdatedAt Time

A timestamp in RFC 3339 format

Content stringoptional

type BetaManagedAgentsMemoryListItemUnion interface{…}

Accepts one of the following:

type BetaManagedAgentsMemory struct{…}

ID string

ContentSha256 string

ContentSizeBytes int64

CreatedAt Time

A timestamp in RFC 3339 format

MemoryStoreID string

MemoryVersionID string

Path string

Type BetaManagedAgentsMemoryType

UpdatedAt Time

A timestamp in RFC 3339 format

Content stringoptional

type BetaManagedAgentsMemoryPrefix struct{…}

Path string

Type BetaManagedAgentsMemoryPrefixType

type BetaManagedAgentsMemoryPathConflictError struct{…}

Type BetaManagedAgentsMemoryPathConflictErrorType

ConflictingMemoryID stringoptional

ConflictingPath stringoptional

Message stringoptional

type BetaManagedAgentsMemoryPreconditionFailedError struct{…}

Type BetaManagedAgentsMemoryPreconditionFailedErrorType

Message stringoptional

type BetaManagedAgentsMemoryPrefix struct{…}

Path string

Type BetaManagedAgentsMemoryPrefixType

type BetaManagedAgentsMemoryView string

MemoryView enum

Accepts one of the following:

const BetaManagedAgentsMemoryViewBasic [BetaManagedAgentsMemoryView](api/beta.md) = "basic"

const BetaManagedAgentsMemoryViewFull [BetaManagedAgentsMemoryView](api/beta.md) = "full"

type BetaManagedAgentsPrecondition struct{…}

Type BetaManagedAgentsPreconditionType

ContentSha256 stringoptional

#### Memory StoresMemory Versions

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
