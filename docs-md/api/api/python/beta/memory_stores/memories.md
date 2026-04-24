# Memories

Copy page

Python

# Memories

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

---

*Copyright © Anthropic. All rights reserved.*
