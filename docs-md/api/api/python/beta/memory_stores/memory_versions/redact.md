# RedactMemoryVersion

Copy page

Python

# RedactMemoryVersion

beta.memory\_stores.memory\_versions.redact(strmemory\_version\_id, MemoryVersionRedactParams\*\*kwargs)  -> [BetaManagedAgentsMemoryVersion](api/beta.md)

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

RedactMemoryVersion

##### ParametersExpand Collapse

memory\_store\_id: str

memory\_version\_id: str

betas: Optional[List[[AnthropicBetaParam](api/beta.md)]]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

str

Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 19 more]

Accepts one of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"advisor-tool-2026-03-01"

##### ReturnsExpand Collapse

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

RedactMemoryVersion

Python

```shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_memory_version = client.beta.memory_stores.memory_versions.redact(
    memory_version_id="memory_version_id",
    memory_store_id="memory_store_id",
)
print(beta_managed_agents_memory_version.id)
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
