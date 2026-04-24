# Memory Stores

Copy page

Ruby

# Memory Stores

##### [CreateMemoryStore](api/beta/memory_stores/create.md)

beta.memory\_stores.create(\*\*kwargs) -> [BetaManagedAgentsMemoryStore](api/beta.md) { id, type, archived\_at, 5 more }

POST/v1/memory\_stores

##### [ListMemoryStores](api/beta/memory_stores/list.md)

beta.memory\_stores.list(\*\*kwargs) -> PageCursor<[BetaManagedAgentsMemoryStore](api/beta.md) { id, type, archived\_at, 5 more } >

GET/v1/memory\_stores

##### [GetMemoryStore](api/beta/memory_stores/retrieve.md)

beta.memory\_stores.retrieve(memory\_store\_id, \*\*kwargs) -> [BetaManagedAgentsMemoryStore](api/beta.md) { id, type, archived\_at, 5 more }

GET/v1/memory\_stores/{memory\_store\_id}

##### [UpdateMemoryStore](api/beta/memory_stores/update.md)

beta.memory\_stores.update(memory\_store\_id, \*\*kwargs) -> [BetaManagedAgentsMemoryStore](api/beta.md) { id, type, archived\_at, 5 more }

POST/v1/memory\_stores/{memory\_store\_id}

##### [DeleteMemoryStore](api/beta/memory_stores/delete.md)

beta.memory\_stores.delete(memory\_store\_id, \*\*kwargs) -> [BetaManagedAgentsDeletedMemoryStore](api/beta.md) { id, type }

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [ArchiveMemoryStore](api/beta/memory_stores/archive.md)

beta.memory\_stores.archive(memory\_store\_id, \*\*kwargs) -> [BetaManagedAgentsMemoryStore](api/beta.md) { id, type, archived\_at, 5 more }

POST/v1/memory\_stores/{memory\_store\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsDeletedMemoryStore { id, type }

id: String

type: :memory\_store\_deleted

class BetaManagedAgentsMemoryStore { id, type, archived\_at, 5 more }

id: String

type: :memory\_store

archived\_at: Time

A timestamp in RFC 3339 format

created\_at: Time

A timestamp in RFC 3339 format

description: String

metadata: Hash[Symbol, String]

name: String

updated\_at: Time

A timestamp in RFC 3339 format

#### Memory StoresMemories

##### [CreateMemory](api/beta/memory_stores/memories/create.md)

beta.memory\_stores.memories.create(memory\_store\_id, \*\*kwargs) -> [BetaManagedAgentsMemory](api/beta.md) { id, content\_sha256, content\_size\_bytes, 7 more }

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [ListMemories](api/beta/memory_stores/memories/list.md)

beta.memory\_stores.memories.list(memory\_store\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsMemoryListItem](api/beta.md)>

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [GetMemory](api/beta/memory_stores/memories/retrieve.md)

beta.memory\_stores.memories.retrieve(memory\_id, \*\*kwargs) -> [BetaManagedAgentsMemory](api/beta.md) { id, content\_sha256, content\_size\_bytes, 7 more }

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [UpdateMemory](api/beta/memory_stores/memories/update.md)

beta.memory\_stores.memories.update(memory\_id, \*\*kwargs) -> [BetaManagedAgentsMemory](api/beta.md) { id, content\_sha256, content\_size\_bytes, 7 more }

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [DeleteMemory](api/beta/memory_stores/memories/delete.md)

beta.memory\_stores.memories.delete(memory\_id, \*\*kwargs) -> [BetaManagedAgentsDeletedMemory](api/beta.md) { id, type }

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### ModelsExpand Collapse

class BetaManagedAgentsContentSha256Precondition { type, content\_sha256 }

type: :content\_sha256

content\_sha256: String

class BetaManagedAgentsDeletedMemory { id, type }

id: String

type: :memory\_deleted

class BetaManagedAgentsMemory { id, content\_sha256, content\_size\_bytes, 7 more }

id: String

content\_sha256: String

content\_size\_bytes: Integer

created\_at: Time

A timestamp in RFC 3339 format

memory\_store\_id: String

memory\_version\_id: String

path: String

type: :memory

updated\_at: Time

A timestamp in RFC 3339 format

content: String

BetaManagedAgentsMemoryListItem = [BetaManagedAgentsMemory](api/beta.md) { id, content\_sha256, content\_size\_bytes, 7 more }  | [BetaManagedAgentsMemoryPrefix](api/beta.md) { path, type }

Accepts one of the following:

class BetaManagedAgentsMemory { id, content\_sha256, content\_size\_bytes, 7 more }

id: String

content\_sha256: String

content\_size\_bytes: Integer

created\_at: Time

A timestamp in RFC 3339 format

memory\_store\_id: String

memory\_version\_id: String

path: String

type: :memory

updated\_at: Time

A timestamp in RFC 3339 format

content: String

class BetaManagedAgentsMemoryPrefix { path, type }

path: String

type: :memory\_prefix

class BetaManagedAgentsMemoryPathConflictError { type, conflicting\_memory\_id, conflicting\_path, message }

type: :memory\_path\_conflict\_error

conflicting\_memory\_id: String

conflicting\_path: String

message: String

class BetaManagedAgentsMemoryPreconditionFailedError { type, message }

type: :memory\_precondition\_failed\_error

message: String

class BetaManagedAgentsMemoryPrefix { path, type }

path: String

type: :memory\_prefix

BetaManagedAgentsMemoryView = :basic | :full

MemoryView enum

Accepts one of the following:

:basic

:full

class BetaManagedAgentsPrecondition { type, content\_sha256 }

type: :content\_sha256

content\_sha256: String

#### Memory StoresMemory Versions

##### [ListMemoryVersions](api/beta/memory_stores/memory_versions/list.md)

beta.memory\_stores.memory\_versions.list(memory\_store\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsMemoryVersion](api/beta.md) { id, created\_at, memory\_id, 10 more } >

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [GetMemoryVersion](api/beta/memory_stores/memory_versions/retrieve.md)

beta.memory\_stores.memory\_versions.retrieve(memory\_version\_id, \*\*kwargs) -> [BetaManagedAgentsMemoryVersion](api/beta.md) { id, created\_at, memory\_id, 10 more }

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [RedactMemoryVersion](api/beta/memory_stores/memory_versions/redact.md)

beta.memory\_stores.memory\_versions.redact(memory\_version\_id, \*\*kwargs) -> [BetaManagedAgentsMemoryVersion](api/beta.md) { id, created\_at, memory\_id, 10 more }

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

##### ModelsExpand Collapse

BetaManagedAgentsActor = [BetaManagedAgentsSessionActor](api/beta.md) { session\_id, type }  | [BetaManagedAgentsAPIActor](api/beta.md) { api\_key\_id, type }  | [BetaManagedAgentsUserActor](api/beta.md) { type, user\_id }

Accepts one of the following:

class BetaManagedAgentsSessionActor { session\_id, type }

session\_id: String

type: :session\_actor

class BetaManagedAgentsAPIActor { api\_key\_id, type }

api\_key\_id: String

type: :api\_actor

class BetaManagedAgentsUserActor { type, user\_id }

type: :user\_actor

user\_id: String

class BetaManagedAgentsAPIActor { api\_key\_id, type }

api\_key\_id: String

type: :api\_actor

class BetaManagedAgentsMemoryVersion { id, created\_at, memory\_id, 10 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

memory\_id: String

memory\_store\_id: String

operation: [BetaManagedAgentsMemoryVersionOperation](api/beta.md)

MemoryVersionOperation enum

Accepts one of the following:

:created

:modified

:deleted

type: :memory\_version

content: String

content\_sha256: String

content\_size\_bytes: Integer

created\_by: [BetaManagedAgentsActor](api/beta.md)

Accepts one of the following:

class BetaManagedAgentsSessionActor { session\_id, type }

session\_id: String

type: :session\_actor

class BetaManagedAgentsAPIActor { api\_key\_id, type }

api\_key\_id: String

type: :api\_actor

class BetaManagedAgentsUserActor { type, user\_id }

type: :user\_actor

user\_id: String

path: String

redacted\_at: Time

A timestamp in RFC 3339 format

redacted\_by: [BetaManagedAgentsActor](api/beta.md)

Accepts one of the following:

class BetaManagedAgentsSessionActor { session\_id, type }

session\_id: String

type: :session\_actor

class BetaManagedAgentsAPIActor { api\_key\_id, type }

api\_key\_id: String

type: :api\_actor

class BetaManagedAgentsUserActor { type, user\_id }

type: :user\_actor

user\_id: String

BetaManagedAgentsMemoryVersionOperation = :created | :modified | :deleted

MemoryVersionOperation enum

Accepts one of the following:

:created

:modified

:deleted

class BetaManagedAgentsSessionActor { session\_id, type }

session\_id: String

type: :session\_actor

class BetaManagedAgentsUserActor { type, user\_id }

type: :user\_actor

user\_id: String

---

*Copyright © Anthropic. All rights reserved.*
