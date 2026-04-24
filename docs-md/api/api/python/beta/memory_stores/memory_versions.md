# Memory Versions

Copy page

Python

# Memory Versions

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
