# List Session Resources

Copy page

SDK language

CLI

# List Session Resources

$ ant beta:sessions:resources list

GET/v1/sessions/{session\_id}/resources

List Session Resources

##### ParametersExpand Collapse

--session-id: string

Path param: Path parameter session\_id

--limit: optional number

Query param: Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

--page: optional string

Query param: Opaque cursor from a previous response's next\_page field.

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



BetaManagedAgentsListSessionResources: object { data, next\_page } 

Paginated list of resources attached to a session.



data: array of [BetaManagedAgentsSessionResource](api/beta.md)

Resources for the session, ordered by `created_at`.



beta\_managed\_agents\_github\_repository\_resource: object { id, created\_at, mount\_path, 4 more } 

id: string

created\_at: string

A timestamp in RFC 3339 format

mount\_path: string



type: "github\_repository"

"github\_repository"

updated\_at: string

A timestamp in RFC 3339 format

url: string



checkout: optional [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  or [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type } 



beta\_managed\_agents\_branch\_checkout: object { name, type } 

name: string

Branch name to check out.



type: "branch"

"branch"



beta\_managed\_agents\_commit\_checkout: object { sha, type } 

sha: string

Full commit SHA to check out.



type: "commit"

"commit"



beta\_managed\_agents\_file\_resource: object { id, created\_at, file\_id, 3 more } 

id: string

created\_at: string

A timestamp in RFC 3339 format

file\_id: string

mount\_path: string



type: "file"

"file"

updated\_at: string

A timestamp in RFC 3339 format



beta\_managed\_agents\_memory\_store\_resource: object { memory\_store\_id, type, access, 4 more } 

A memory store attached to an agent session.

memory\_store\_id: string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.



type: "memory\_store"

"memory\_store"



access: optional "read\_write" or "read\_only"

Access mode for an attached memory store.

"read\_write"

"read\_only"

description: optional string

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

instructions: optional string

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

mount\_path: optional string

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

name: optional string

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

next\_page: optional string

Opaque cursor for the next page. Null when no more results.

List Session Resources

CLI

```shiki
ant beta:sessions:resources list \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```

Response 200



```shiki
{
  "data": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

---

*Copyright © Anthropic. All rights reserved.*
