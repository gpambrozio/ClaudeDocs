# RedactMemoryVersion

Copy page

Ruby

# RedactMemoryVersion

beta.memory\_stores.memory\_versions.redact(memory\_version\_id, \*\*kwargs) -> [BetaManagedAgentsMemoryVersion](api/beta.md) { id, created\_at, memory\_id, 10 more }

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

RedactMemoryVersion

##### ParametersExpand Collapse

memory\_store\_id: String

memory\_version\_id: String

betas: Array[[AnthropicBeta](api/beta.md)]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

String

:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 19 more

Accepts one of the following:

:"message-batches-2024-09-24"

:"prompt-caching-2024-07-31"

:"computer-use-2024-10-22"

:"computer-use-2025-01-24"

:"pdfs-2024-09-25"

:"token-counting-2024-11-01"

:"token-efficient-tools-2025-02-19"

:"output-128k-2025-02-19"

:"files-api-2025-04-14"

:"mcp-client-2025-04-04"

:"mcp-client-2025-11-20"

:"dev-full-thinking-2025-05-14"

:"interleaved-thinking-2025-05-14"

:"code-execution-2025-05-22"

:"extended-cache-ttl-2025-04-11"

:"context-1m-2025-08-07"

:"context-management-2025-06-27"

:"model-context-window-exceeded-2025-08-26"

:"skills-2025-10-02"

:"fast-mode-2026-02-01"

:"output-300k-2026-03-24"

:"advisor-tool-2026-03-01"

##### ReturnsExpand Collapse

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

RedactMemoryVersion

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory_version = anthropic.beta.memory_stores.memory_versions.redact(
  "memory_version_id",
  memory_store_id: "memory_store_id"
)

puts(beta_managed_agents_memory_version)
```

Response 200

```shiki
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_id": "memory_id",
  "memory_store_id": "memory_store_id",
  "operation": "created",
  "type": "memory_version",
  "content": "content",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_by": {
    "session_id": "x",
    "type": "session_actor"
  },
  "path": "path",
  "redacted_at": "2019-12-27T18:11:19.117Z",
  "redacted_by": {
    "session_id": "x",
    "type": "session_actor"
  }
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_id": "memory_id",
  "memory_store_id": "memory_store_id",
  "operation": "created",
  "type": "memory_version",
  "content": "content",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_by": {
    "session_id": "x",
    "type": "session_actor"
  },
  "path": "path",
  "redacted_at": "2019-12-27T18:11:19.117Z",
  "redacted_by": {
    "session_id": "x",
    "type": "session_actor"
  }
}
```

---

*Copyright © Anthropic. All rights reserved.*
