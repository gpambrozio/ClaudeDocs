# Get Session Resource

Copy page

CLI

# Get Session Resource

$ ant beta:sessions:resources retrieve

GET/v1/sessions/{session\_id}/resources/{resource\_id}

Get Session Resource

##### ParametersExpand Collapse

--session-id: string

Path param: Path parameter session\_id

--resource-id: string

Path param: Path parameter resource\_id

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

BetaSessionResourceGetResponse: [BetaManagedAgentsGitHubRepositoryResource](api/beta.md) { id, created\_at, mount\_path, 4 more }  or [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }  or [BetaManagedAgentsMemoryStoreResource](api/beta.md) { memory\_store\_id, type, access, 4 more }

The requested session resource.

beta\_managed\_agents\_github\_repository\_resource: object { id, created\_at, mount\_path, 4 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

mount\_path: string

type: "github\_repository"

"github\_repository"

updated\_at: string

A timestamp in RFC 3339 format

url: string

checkout: optional [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  or [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }

beta\_managed\_agents\_branch\_checkout: object { name, type }

name: string

Branch name to check out.

type: "branch"

"branch"

beta\_managed\_agents\_commit\_checkout: object { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

"commit"

beta\_managed\_agents\_file\_resource: object { id, created\_at, file\_id, 3 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

file\_id: string

mount\_path: string

type: "file"

"file"

updated\_at: string

A timestamp in RFC 3339 format

beta\_managed\_agents\_memory\_store\_resource: object { memory\_store\_id, type, access, 4 more }

A memory store attached to an agent session.

memory\_store\_id: string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: "memory\_store"

"memory\_store"

access: optional "read\_write" or "read\_only"

Access mode for an attached memory store.

"read\_write"

"read\_only"

description: optional string

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

instructions: optional string

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

mount\_path: optional string

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

name: optional string

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

Get Session Resource

CLI

```shiki
ant beta:sessions:resources retrieve \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --resource-id sesrsc_011CZkZBJq5dWxk9fVLNcPht
```

Response 200

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
