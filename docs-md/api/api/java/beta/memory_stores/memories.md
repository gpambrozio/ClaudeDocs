# Memories

Copy page

Java

# Memories

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

---

*Copyright © Anthropic. All rights reserved.*
