# Update Session Resource

Copy page

Ruby

# Update Session Resource

beta.sessions.resources.update(resource\_id, \*\*kwargs) -> [ResourceUpdateResponse](api/beta.md)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

Update Session Resource

##### ParametersExpand Collapse

session\_id: String

resource\_id: String

authorization\_token: String

New authorization token for the resource. Currently only `github_repository` resources support token rotation.

betas: Array[[AnthropicBeta](api/beta.md)]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

String

:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 18 more

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

##### ReturnsExpand Collapse

ResourceUpdateResponse = [BetaManagedAgentsGitHubRepositoryResource](api/beta.md) { id, created\_at, mount\_path, 4 more }  | [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }

The updated session resource.

Accepts one of the following:

class BetaManagedAgentsGitHubRepositoryResource { id, created\_at, mount\_path, 4 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

mount\_path: String

type: :github\_repository

updated\_at: Time

A timestamp in RFC 3339 format

url: String

checkout: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }

Accepts one of the following:

class BetaManagedAgentsBranchCheckout { name, type }

name: String

Branch name to check out.

type: :branch

class BetaManagedAgentsCommitCheckout { sha, type }

sha: String

Full commit SHA to check out.

type: :commit

class BetaManagedAgentsFileResource { id, created\_at, file\_id, 3 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

file\_id: String

mount\_path: String

type: :file

updated\_at: Time

A timestamp in RFC 3339 format

Update Session Resource

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

resource = anthropic.beta.sessions.resources.update(
  "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7",
  authorization_token: "ghp_exampletoken"
)

puts(resource)
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
