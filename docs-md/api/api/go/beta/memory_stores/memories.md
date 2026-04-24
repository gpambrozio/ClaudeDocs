# Memories

Copy page

Go

# Memories

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

---

*Copyright © Anthropic. All rights reserved.*
