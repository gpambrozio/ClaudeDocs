# Memory Versions

Copy page

Java

# Memory Versions

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
