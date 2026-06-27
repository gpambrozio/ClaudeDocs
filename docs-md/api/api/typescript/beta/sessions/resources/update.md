# Update Session Resource

Copy page



TypeScript

# Update Session Resource

client.beta.sessions.resources.update(stringresourceID, ResourceUpdateParams { session\_id, authorization\_token, betas } params, RequestOptionsoptions?): [ResourceUpdateResponse](api/beta/sessions/resources.md)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

Update Session Resource

##### ParametersExpand Collapse

resourceID: string



params: ResourceUpdateParams { session\_id, authorization\_token, betas } 

session\_id: string

Path param: Path parameter session\_id

authorization\_token: string

Body param: New authorization token for the resource. Currently only `github_repository` resources support token rotation.



betas?: Array<[AnthropicBeta](api/beta.md)>

Header param: Optional header to specify the beta version(s) you want to use.

One of the following:

(string & {})



"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 25 more

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

ResourceUpdateResponse = [BetaManagedAgentsGitHubRepositoryResource](api/beta/sessions/resources.md) { id, created\_at, mount\_path, 4 more }  | [BetaManagedAgentsFileResource](api/beta/sessions/resources.md) { id, created\_at, file\_id, 3 more }  | [BetaManagedAgentsMemoryStoreResource](api/beta/sessions/resources.md) { memory\_store\_id, type, access, 4 more } 

The updated session resource.

One of the following:



BetaManagedAgentsGitHubRepositoryResource { id, created\_at, mount\_path, 4 more } 

id: string

created\_at: string

A timestamp in RFC 3339 format

mount\_path: string

type: "github\_repository"

updated\_at: string

A timestamp in RFC 3339 format

url: string



checkout?: [BetaManagedAgentsBranchCheckout](api/beta/sessions.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta/sessions.md) { sha, type }  | null

One of the following:



BetaManagedAgentsBranchCheckout { name, type } 

name: string

Branch name to check out.

type: "branch"



BetaManagedAgentsCommitCheckout { sha, type } 

sha: string

Full commit SHA to check out.

type: "commit"



BetaManagedAgentsFileResource { id, created\_at, file\_id, 3 more } 

id: string

created\_at: string

A timestamp in RFC 3339 format

file\_id: string

mount\_path: string

type: "file"

updated\_at: string

A timestamp in RFC 3339 format



BetaManagedAgentsMemoryStoreResource { memory\_store\_id, type, access, 4 more } 

A memory store attached to an agent session.

memory\_store\_id: string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: "memory\_store"



access?: "read\_write" | "read\_only" | null

Access mode for an attached memory store.

One of the following:

"read\_write"

"read\_only"

description?: string

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

instructions?: string | null

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

mount\_path?: string | null

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

name?: string | null

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

Update Session Resource

TypeScript

```shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const resource = await client.beta.sessions.resources.update('sesrsc_011CZkZBJq5dWxk9fVLNcPht', {
  session_id: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  authorization_token: 'ghp_exampletoken',
});

console.log(resource);
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
