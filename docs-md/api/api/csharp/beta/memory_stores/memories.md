# Memories

Copy page

C#

# Memories

##### [CreateMemory](api/beta/memory_stores/memories/create.md)

[BetaManagedAgentsMemory](api/beta.md) Beta.MemoryStores.Memories.Create(MemoryCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [ListMemories](api/beta/memory_stores/memories/list.md)

[MemoryListPageResponse](api/beta.md) Beta.MemoryStores.Memories.List(MemoryListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [GetMemory](api/beta/memory_stores/memories/retrieve.md)

[BetaManagedAgentsMemory](api/beta.md) Beta.MemoryStores.Memories.Retrieve(MemoryRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [UpdateMemory](api/beta/memory_stores/memories/update.md)

[BetaManagedAgentsMemory](api/beta.md) Beta.MemoryStores.Memories.Update(MemoryUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [DeleteMemory](api/beta/memory_stores/memories/delete.md)

[BetaManagedAgentsDeletedMemory](api/beta.md) Beta.MemoryStores.Memories.Delete(MemoryDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### ModelsExpand Collapse

class BetaManagedAgentsContentSha256Precondition:

required Type Type

string ContentSha256

class BetaManagedAgentsDeletedMemory:

required string ID

required Type Type

class BetaManagedAgentsMemory:

required string ID

required string ContentSha256

required Int ContentSizeBytes

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string MemoryStoreID

required string MemoryVersionID

required string Path

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

string? Content

class BetaManagedAgentsMemoryListItem: A class that can be one of several variants.union

class BetaManagedAgentsMemory:

required string ID

required string ContentSha256

required Int ContentSizeBytes

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string MemoryStoreID

required string MemoryVersionID

required string Path

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

string? Content

class BetaManagedAgentsMemoryPrefix:

required string Path

required Type Type

class BetaManagedAgentsMemoryPathConflictError:

required Type Type

string ConflictingMemoryID

string ConflictingPath

string Message

class BetaManagedAgentsMemoryPreconditionFailedError:

required Type Type

string Message

class BetaManagedAgentsMemoryPrefix:

required string Path

required Type Type

enum BetaManagedAgentsMemoryView:

MemoryView enum

"basic"Basic

"full"Full

class BetaManagedAgentsPrecondition:

required Type Type

string ContentSha256

---

*Copyright © Anthropic. All rights reserved.*
