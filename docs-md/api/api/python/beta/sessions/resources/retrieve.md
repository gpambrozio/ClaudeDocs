# Get Session Resource

Copy page

SDK language

Python

# Get Session Resource

beta.sessions.resources.retrieve(strresource\_id, ResourceRetrieveParams\*\*kwargs)  -> [ResourceRetrieveResponse](api/beta.md)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

Get Session Resource

##### ParametersExpand Collapse

session\_id: str

resource\_id: str



betas: Optional[List[[AnthropicBetaParam](api/beta.md)]]

Optional header to specify the beta version(s) you want to use.

One of the following:

str



Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]

One of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"fallback-credit-2026-06-01"

##### ReturnsExpand Collapse



[ResourceRetrieveResponse](api/beta.md)

The requested session resource.

One of the following:



class BetaManagedAgentsGitHubRepositoryResource: …

id: str

created\_at: datetime

A timestamp in RFC 3339 format

mount\_path: str

type: Literal["github\_repository"]

updated\_at: datetime

A timestamp in RFC 3339 format

url: str



checkout: Optional[Checkout]

One of the following:



class BetaManagedAgentsBranchCheckout: …

name: str

Branch name to check out.

type: Literal["branch"]



class BetaManagedAgentsCommitCheckout: …

sha: str

Full commit SHA to check out.

type: Literal["commit"]



class BetaManagedAgentsFileResource: …

id: str

created\_at: datetime

A timestamp in RFC 3339 format

file\_id: str

mount\_path: str

type: Literal["file"]

updated\_at: datetime

A timestamp in RFC 3339 format



class BetaManagedAgentsMemoryStoreResource: …

A memory store attached to an agent session.

memory\_store\_id: str

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: Literal["memory\_store"]



access: Optional[Literal["read\_write", "read\_only"]]

Access mode for an attached memory store.

One of the following:

"read\_write"

"read\_only"

description: Optional[str]

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

instructions: Optional[str]

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

mount\_path: Optional[str]

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

name: Optional[str]

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

Get Session Resource

Python

```shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
resource = client.beta.sessions.resources.retrieve(
    resource_id="sesrsc_011CZkZBJq5dWxk9fVLNcPht",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
print(resource)
```

Response 200



```shiki
{
  "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
  "created_at": "2026-03-15T10:00:00Z",
  "mount_path": "/workspace/example-repo",
  "type": "github_repository",
  "updated_at": "2026-03-15T10:00:00Z",
  "url": "https://github.com/example-org/example-repo",
  "checkout": {
    "name": "main",
    "type": "branch"
  }
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
  "created_at": "2026-03-15T10:00:00Z",
  "mount_path": "/workspace/example-repo",
  "type": "github_repository",
  "updated_at": "2026-03-15T10:00:00Z",
  "url": "https://github.com/example-org/example-repo",
  "checkout": {
    "name": "main",
    "type": "branch"
  }
}
```

---

*Copyright © Anthropic. All rights reserved.*
