# Memory Stores

Copy page

C#

# Memory Stores

##### [CreateMemoryStore](api/beta/memory_stores/create.md)

[BetaManagedAgentsMemoryStore](api/beta.md) Beta.MemoryStores.Create(MemoryStoreCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/memory\_stores

##### [ListMemoryStores](api/beta/memory_stores/list.md)

[MemoryStoreListPageResponse](api/beta.md) Beta.MemoryStores.List(MemoryStoreListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/memory\_stores

##### [GetMemoryStore](api/beta/memory_stores/retrieve.md)

[BetaManagedAgentsMemoryStore](api/beta.md) Beta.MemoryStores.Retrieve(MemoryStoreRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/memory\_stores/{memory\_store\_id}

##### [UpdateMemoryStore](api/beta/memory_stores/update.md)

[BetaManagedAgentsMemoryStore](api/beta.md) Beta.MemoryStores.Update(MemoryStoreUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/memory\_stores/{memory\_store\_id}

##### [DeleteMemoryStore](api/beta/memory_stores/delete.md)

[BetaManagedAgentsDeletedMemoryStore](api/beta.md) Beta.MemoryStores.Delete(MemoryStoreDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [ArchiveMemoryStore](api/beta/memory_stores/archive.md)

[BetaManagedAgentsMemoryStore](api/beta.md) Beta.MemoryStores.Archive(MemoryStoreArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/memory\_stores/{memory\_store\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsDeletedMemoryStore:

required string ID

required Type Type

class BetaManagedAgentsMemoryStore:

required string ID

required Type Type

DateTimeOffset? ArchivedAt

A timestamp in RFC 3339 format

DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

string Description

IReadOnlyDictionary<string, string> Metadata

string Name

DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

#### Memory StoresMemories

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

#### Memory StoresMemory Versions

##### [ListMemoryVersions](api/beta/memory_stores/memory_versions/list.md)

[MemoryVersionListPageResponse](api/beta.md) Beta.MemoryStores.MemoryVersions.List(MemoryVersionListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [GetMemoryVersion](api/beta/memory_stores/memory_versions/retrieve.md)

[BetaManagedAgentsMemoryVersion](api/beta.md) Beta.MemoryStores.MemoryVersions.Retrieve(MemoryVersionRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [RedactMemoryVersion](api/beta/memory_stores/memory_versions/redact.md)

[BetaManagedAgentsMemoryVersion](api/beta.md) Beta.MemoryStores.MemoryVersions.Redact(MemoryVersionRedactParamsparameters, CancellationTokencancellationToken = default)

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

##### ModelsExpand Collapse

class BetaManagedAgentsActor: A class that can be one of several variants.union

class BetaManagedAgentsSessionActor:

required string SessionID

required Type Type

class BetaManagedAgentsApiActor:

required string ApiKeyID

required Type Type

class BetaManagedAgentsUserActor:

required Type Type

required string UserID

class BetaManagedAgentsApiActor:

required string ApiKeyID

required Type Type

class BetaManagedAgentsMemoryVersion:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string MemoryID

required string MemoryStoreID

required [BetaManagedAgentsMemoryVersionOperation](api/beta.md) Operation

MemoryVersionOperation enum

Accepts one of the following:

"created"Created

"modified"Modified

"deleted"Deleted

required Type Type

string? Content

string? ContentSha256

Int? ContentSizeBytes

[BetaManagedAgentsActor](api/beta.md) CreatedBy

Accepts one of the following:

class BetaManagedAgentsSessionActor:

required string SessionID

required Type Type

class BetaManagedAgentsApiActor:

required string ApiKeyID

required Type Type

class BetaManagedAgentsUserActor:

required Type Type

required string UserID

string? Path

DateTimeOffset? RedactedAt

A timestamp in RFC 3339 format

[BetaManagedAgentsActor](api/beta.md) RedactedBy

Accepts one of the following:

class BetaManagedAgentsSessionActor:

required string SessionID

required Type Type

class BetaManagedAgentsApiActor:

required string ApiKeyID

required Type Type

class BetaManagedAgentsUserActor:

required Type Type

required string UserID

enum BetaManagedAgentsMemoryVersionOperation:

MemoryVersionOperation enum

"created"Created

"modified"Modified

"deleted"Deleted

class BetaManagedAgentsSessionActor:

required string SessionID

required Type Type

class BetaManagedAgentsUserActor:

required Type Type

required string UserID

---

*Copyright © Anthropic. All rights reserved.*
