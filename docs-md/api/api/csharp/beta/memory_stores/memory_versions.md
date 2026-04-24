# Memory Versions

Copy page

C#

# Memory Versions

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
