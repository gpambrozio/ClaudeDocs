# Memory Versions

Copy page

Ruby

# Memory Versions

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
