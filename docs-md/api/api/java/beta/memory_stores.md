# Memory Stores

Copy page

Java

# Memory Stores

##### [CreateMemoryStore](api/beta/memory_stores/create.md)

[BetaManagedAgentsMemoryStore](api/beta.md) beta().memoryStores().create(MemoryStoreCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/memory\_stores

##### [ListMemoryStores](api/beta/memory_stores/list.md)

MemoryStoreListPage beta().memoryStores().list(MemoryStoreListParamsparams = MemoryStoreListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/memory\_stores

##### [GetMemoryStore](api/beta/memory_stores/retrieve.md)

[BetaManagedAgentsMemoryStore](api/beta.md) beta().memoryStores().retrieve(MemoryStoreRetrieveParamsparams = MemoryStoreRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/memory\_stores/{memory\_store\_id}

##### [UpdateMemoryStore](api/beta/memory_stores/update.md)

[BetaManagedAgentsMemoryStore](api/beta.md) beta().memoryStores().update(MemoryStoreUpdateParamsparams = MemoryStoreUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/memory\_stores/{memory\_store\_id}

##### [DeleteMemoryStore](api/beta/memory_stores/delete.md)

[BetaManagedAgentsDeletedMemoryStore](api/beta.md) beta().memoryStores().delete(MemoryStoreDeleteParamsparams = MemoryStoreDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [ArchiveMemoryStore](api/beta/memory_stores/archive.md)

[BetaManagedAgentsMemoryStore](api/beta.md) beta().memoryStores().archive(MemoryStoreArchiveParamsparams = MemoryStoreArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/memory\_stores/{memory\_store\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsDeletedMemoryStore:

String id

Type type

class BetaManagedAgentsMemoryStore:

String id

Type type

Optional<LocalDateTime> archivedAt

A timestamp in RFC 3339 format

Optional<LocalDateTime> createdAt

A timestamp in RFC 3339 format

Optional<String> description

Optional<Metadata> metadata

Optional<String> name

Optional<LocalDateTime> updatedAt

A timestamp in RFC 3339 format

#### Memory StoresMemories

##### [CreateMemory](api/beta/memory_stores/memories/create.md)

[BetaManagedAgentsMemory](api/beta.md) beta().memoryStores().memories().create(MemoryCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [ListMemories](api/beta/memory_stores/memories/list.md)

MemoryListPage beta().memoryStores().memories().list(MemoryListParamsparams = MemoryListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [GetMemory](api/beta/memory_stores/memories/retrieve.md)

[BetaManagedAgentsMemory](api/beta.md) beta().memoryStores().memories().retrieve(MemoryRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [UpdateMemory](api/beta/memory_stores/memories/update.md)

[BetaManagedAgentsMemory](api/beta.md) beta().memoryStores().memories().update(MemoryUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [DeleteMemory](api/beta/memory_stores/memories/delete.md)

[BetaManagedAgentsDeletedMemory](api/beta.md) beta().memoryStores().memories().delete(MemoryDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### ModelsExpand Collapse

class BetaManagedAgentsContentSha256Precondition:

Type type

Optional<String> contentSha256

class BetaManagedAgentsDeletedMemory:

String id

Type type

class BetaManagedAgentsMemory:

String id

String contentSha256

long contentSizeBytes

LocalDateTime createdAt

A timestamp in RFC 3339 format

String memoryStoreId

String memoryVersionId

String path

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

Optional<String> content

class BetaManagedAgentsMemoryListItem: A class that can be one of several variants.union

class BetaManagedAgentsMemory:

String id

String contentSha256

long contentSizeBytes

LocalDateTime createdAt

A timestamp in RFC 3339 format

String memoryStoreId

String memoryVersionId

String path

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

Optional<String> content

class BetaManagedAgentsMemoryPrefix:

String path

Type type

class BetaManagedAgentsMemoryPathConflictError:

Type type

Optional<String> conflictingMemoryId

Optional<String> conflictingPath

Optional<String> message

class BetaManagedAgentsMemoryPreconditionFailedError:

Type type

Optional<String> message

class BetaManagedAgentsMemoryPrefix:

String path

Type type

enum BetaManagedAgentsMemoryView:

MemoryView enum

BASIC("basic")

FULL("full")

class BetaManagedAgentsPrecondition:

Type type

Optional<String> contentSha256

#### Memory StoresMemory Versions

##### [ListMemoryVersions](api/beta/memory_stores/memory_versions/list.md)

MemoryVersionListPage beta().memoryStores().memoryVersions().list(MemoryVersionListParamsparams = MemoryVersionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [GetMemoryVersion](api/beta/memory_stores/memory_versions/retrieve.md)

[BetaManagedAgentsMemoryVersion](api/beta.md) beta().memoryStores().memoryVersions().retrieve(MemoryVersionRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [RedactMemoryVersion](api/beta/memory_stores/memory_versions/redact.md)

[BetaManagedAgentsMemoryVersion](api/beta.md) beta().memoryStores().memoryVersions().redact(MemoryVersionRedactParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

##### ModelsExpand Collapse

class BetaManagedAgentsActor: A class that can be one of several variants.union

class BetaManagedAgentsSessionActor:

String sessionId

Type type

class BetaManagedAgentsApiActor:

String apiKeyId

Type type

class BetaManagedAgentsUserActor:

Type type

String userId

class BetaManagedAgentsApiActor:

String apiKeyId

Type type

class BetaManagedAgentsMemoryVersion:

String id

LocalDateTime createdAt

A timestamp in RFC 3339 format

String memoryId

String memoryStoreId

[BetaManagedAgentsMemoryVersionOperation](api/beta.md) operation

MemoryVersionOperation enum

Accepts one of the following:

CREATED("created")

MODIFIED("modified")

DELETED("deleted")

Type type

Optional<String> content

Optional<String> contentSha256

Optional<Long> contentSizeBytes

Optional<[BetaManagedAgentsActor](api/beta.md)> createdBy

Accepts one of the following:

class BetaManagedAgentsSessionActor:

String sessionId

Type type

class BetaManagedAgentsApiActor:

String apiKeyId

Type type

class BetaManagedAgentsUserActor:

Type type

String userId

Optional<String> path

Optional<LocalDateTime> redactedAt

A timestamp in RFC 3339 format

Optional<[BetaManagedAgentsActor](api/beta.md)> redactedBy

Accepts one of the following:

class BetaManagedAgentsSessionActor:

String sessionId

Type type

class BetaManagedAgentsApiActor:

String apiKeyId

Type type

class BetaManagedAgentsUserActor:

Type type

String userId

enum BetaManagedAgentsMemoryVersionOperation:

MemoryVersionOperation enum

CREATED("created")

MODIFIED("modified")

DELETED("deleted")

class BetaManagedAgentsSessionActor:

String sessionId

Type type

class BetaManagedAgentsUserActor:

Type type

String userId

---

*Copyright © Anthropic. All rights reserved.*
