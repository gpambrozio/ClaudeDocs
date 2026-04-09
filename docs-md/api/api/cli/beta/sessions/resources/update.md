# Update Session Resource

Copy page

CLI

# Update Session Resource

$ ant beta:sessions:resources update

POST/v1/sessions/{session\_id}/resources/{resource\_id}

Update Session Resource

##### ParametersExpand Collapse

--session-id: string

Path param: Path parameter session\_id

--resource-id: string

Path param: Path parameter resource\_id

--authorization-token: string

Body param: New authorization token for the resource. Currently only `github_repository` resources support token rotation.

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

BetaSessionResourceUpdateResponse: [BetaManagedAgentsGitHubRepositoryResource](api/beta.md) { id, created\_at, mount\_path, 4 more }  or [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }

The updated session resource.

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

Update Session Resource

CLI

```shiki
ant beta:sessions:resources update \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --resource-id sesrsc_011CZkZBJq5dWxk9fVLNcPht \
  --authorization-token ghp_exampletoken
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
