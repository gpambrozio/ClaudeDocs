# Memory Stores

Copy page

Python

# Memory Stores

##### [CreateMemoryStore](api/beta/memory_stores/create.md)

beta.memory\_stores.create(MemoryStoreCreateParams\*\*kwargs)  -> [BetaManagedAgentsMemoryStore](api/beta.md)

POST/v1/memory\_stores

##### [ListMemoryStores](api/beta/memory_stores/list.md)

beta.memory\_stores.list(MemoryStoreListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsMemoryStore](api/beta.md)]

GET/v1/memory\_stores

##### [GetMemoryStore](api/beta/memory_stores/retrieve.md)

beta.memory\_stores.retrieve(strmemory\_store\_id, MemoryStoreRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsMemoryStore](api/beta.md)

GET/v1/memory\_stores/{memory\_store\_id}

##### [UpdateMemoryStore](api/beta/memory_stores/update.md)

beta.memory\_stores.update(strmemory\_store\_id, MemoryStoreUpdateParams\*\*kwargs)  -> [BetaManagedAgentsMemoryStore](api/beta.md)

POST/v1/memory\_stores/{memory\_store\_id}

##### [DeleteMemoryStore](api/beta/memory_stores/delete.md)

beta.memory\_stores.delete(strmemory\_store\_id, MemoryStoreDeleteParams\*\*kwargs)  -> [BetaManagedAgentsDeletedMemoryStore](api/beta.md)

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [ArchiveMemoryStore](api/beta/memory_stores/archive.md)

beta.memory\_stores.archive(strmemory\_store\_id, MemoryStoreArchiveParams\*\*kwargs)  -> [BetaManagedAgentsMemoryStore](api/beta.md)

POST/v1/memory\_stores/{memory\_store\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsDeletedMemoryStore: …

id: str

type: Literal["memory\_store\_deleted"]

class BetaManagedAgentsMemoryStore: …

id: str

type: Literal["memory\_store"]

archived\_at: Optional[datetime]

A timestamp in RFC 3339 format

created\_at: Optional[datetime]

A timestamp in RFC 3339 format

description: Optional[str]

metadata: Optional[Dict[str, str]]

name: Optional[str]

updated\_at: Optional[datetime]

A timestamp in RFC 3339 format

#### Memory StoresMemories

##### [CreateMemory](api/beta/memory_stores/memories/create.md)

beta.memory\_stores.memories.create(strmemory\_store\_id, MemoryCreateParams\*\*kwargs)  -> [BetaManagedAgentsMemory](api/beta.md)

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [ListMemories](api/beta/memory_stores/memories/list.md)

beta.memory\_stores.memories.list(strmemory\_store\_id, MemoryListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsMemoryListItem](api/beta.md)]

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [GetMemory](api/beta/memory_stores/memories/retrieve.md)

beta.memory\_stores.memories.retrieve(strmemory\_id, MemoryRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsMemory](api/beta.md)

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [UpdateMemory](api/beta/memory_stores/memories/update.md)

beta.memory\_stores.memories.update(strmemory\_id, MemoryUpdateParams\*\*kwargs)  -> [BetaManagedAgentsMemory](api/beta.md)

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [DeleteMemory](api/beta/memory_stores/memories/delete.md)

beta.memory\_stores.memories.delete(strmemory\_id, MemoryDeleteParams\*\*kwargs)  -> [BetaManagedAgentsDeletedMemory](api/beta.md)

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### ModelsExpand Collapse

class BetaManagedAgentsContentSha256Precondition: …

type: Literal["content\_sha256"]

content\_sha256: Optional[str]

class BetaManagedAgentsDeletedMemory: …

id: str

type: Literal["memory\_deleted"]

class BetaManagedAgentsMemory: …

id: str

content\_sha256: str

content\_size\_bytes: int

created\_at: datetime

A timestamp in RFC 3339 format

memory\_store\_id: str

memory\_version\_id: str

path: str

type: Literal["memory"]

updated\_at: datetime

A timestamp in RFC 3339 format

content: Optional[str]

[BetaManagedAgentsMemoryListItem](api/beta.md)

Accepts one of the following:

class BetaManagedAgentsMemory: …

id: str

content\_sha256: str

content\_size\_bytes: int

created\_at: datetime

A timestamp in RFC 3339 format

memory\_store\_id: str

memory\_version\_id: str

path: str

type: Literal["memory"]

updated\_at: datetime

A timestamp in RFC 3339 format

content: Optional[str]

class BetaManagedAgentsMemoryPrefix: …

path: str

type: Literal["memory\_prefix"]

class BetaManagedAgentsMemoryPathConflictError: …

type: Literal["memory\_path\_conflict\_error"]

conflicting\_memory\_id: Optional[str]

conflicting\_path: Optional[str]

message: Optional[str]

class BetaManagedAgentsMemoryPreconditionFailedError: …

type: Literal["memory\_precondition\_failed\_error"]

message: Optional[str]

class BetaManagedAgentsMemoryPrefix: …

path: str

type: Literal["memory\_prefix"]

Literal["basic", "full"]

MemoryView enum

Accepts one of the following:

"basic"

"full"

class BetaManagedAgentsPrecondition: …

type: Literal["content\_sha256"]

content\_sha256: Optional[str]

#### Memory StoresMemory Versions

##### [ListMemoryVersions](api/beta/memory_stores/memory_versions/list.md)

beta.memory\_stores.memory\_versions.list(strmemory\_store\_id, MemoryVersionListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsMemoryVersion](api/beta.md)]

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [GetMemoryVersion](api/beta/memory_stores/memory_versions/retrieve.md)

beta.memory\_stores.memory\_versions.retrieve(strmemory\_version\_id, MemoryVersionRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsMemoryVersion](api/beta.md)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [RedactMemoryVersion](api/beta/memory_stores/memory_versions/redact.md)

beta.memory\_stores.memory\_versions.redact(strmemory\_version\_id, MemoryVersionRedactParams\*\*kwargs)  -> [BetaManagedAgentsMemoryVersion](api/beta.md)

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

##### ModelsExpand Collapse

[BetaManagedAgentsActor](api/beta.md)

Accepts one of the following:

class BetaManagedAgentsSessionActor: …

session\_id: str

type: Literal["session\_actor"]

class BetaManagedAgentsAPIActor: …

api\_key\_id: str

type: Literal["api\_actor"]

class BetaManagedAgentsUserActor: …

type: Literal["user\_actor"]

user\_id: str

class BetaManagedAgentsAPIActor: …

api\_key\_id: str

type: Literal["api\_actor"]

class BetaManagedAgentsMemoryVersion: …

id: str

created\_at: datetime

A timestamp in RFC 3339 format

memory\_id: str

memory\_store\_id: str

operation: [BetaManagedAgentsMemoryVersionOperation](api/beta.md)

MemoryVersionOperation enum

Accepts one of the following:

"created"

"modified"

"deleted"

type: Literal["memory\_version"]

content: Optional[str]

content\_sha256: Optional[str]

content\_size\_bytes: Optional[int]

created\_by: Optional[BetaManagedAgentsActor]

Accepts one of the following:

class BetaManagedAgentsSessionActor: …

session\_id: str

type: Literal["session\_actor"]

class BetaManagedAgentsAPIActor: …

api\_key\_id: str

type: Literal["api\_actor"]

class BetaManagedAgentsUserActor: …

type: Literal["user\_actor"]

user\_id: str

path: Optional[str]

redacted\_at: Optional[datetime]

A timestamp in RFC 3339 format

redacted\_by: Optional[BetaManagedAgentsActor]

Accepts one of the following:

class BetaManagedAgentsSessionActor: …

session\_id: str

type: Literal["session\_actor"]

class BetaManagedAgentsAPIActor: …

api\_key\_id: str

type: Literal["api\_actor"]

class BetaManagedAgentsUserActor: …

type: Literal["user\_actor"]

user\_id: str

Literal["created", "modified", "deleted"]

MemoryVersionOperation enum

Accepts one of the following:

"created"

"modified"

"deleted"

class BetaManagedAgentsSessionActor: …

session\_id: str

type: Literal["session\_actor"]

class BetaManagedAgentsUserActor: …

type: Literal["user\_actor"]

user\_id: str

---

*Copyright © Anthropic. All rights reserved.*
