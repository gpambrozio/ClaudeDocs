# Memories

Copy page

Ruby

# Memories

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

---

*Copyright © Anthropic. All rights reserved.*
