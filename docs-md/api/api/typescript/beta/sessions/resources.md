# Resources

Copy page

TypeScript

# Resources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

client.beta.sessions.resources.add(stringsessionID, ResourceAddParams { file\_id, type, mount\_path, betas } params, RequestOptionsoptions?): [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

client.beta.sessions.resources.list(stringsessionID, ResourceListParams { limit, page, betas } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsSessionResource](api/beta.md)>

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

client.beta.sessions.resources.retrieve(stringresourceID, ResourceRetrieveParams { session\_id, betas } params, RequestOptionsoptions?): [ResourceRetrieveResponse](api/beta.md)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

client.beta.sessions.resources.update(stringresourceID, ResourceUpdateParams { session\_id, authorization\_token, betas } params, RequestOptionsoptions?): [ResourceUpdateResponse](api/beta.md)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

client.beta.sessions.resources.delete(stringresourceID, ResourceDeleteParams { session\_id, betas } params, RequestOptionsoptions?): [BetaManagedAgentsDeleteSessionResource](api/beta.md) { id, type }

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

##### ModelsExpand Collapse

BetaManagedAgentsDeleteSessionResource { id, type }

Confirmation of resource deletion.

id: string

type: "session\_resource\_deleted"

BetaManagedAgentsFileResource { id, created\_at, file\_id, 3 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

file\_id: string

mount\_path: string

type: "file"

updated\_at: string

A timestamp in RFC 3339 format

BetaManagedAgentsGitHubRepositoryResource { id, created\_at, mount\_path, 4 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

mount\_path: string

type: "github\_repository"

updated\_at: string

A timestamp in RFC 3339 format

url: string

checkout?: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }  | null

Accepts one of the following:

BetaManagedAgentsBranchCheckout { name, type }

name: string

Branch name to check out.

type: "branch"

BetaManagedAgentsCommitCheckout { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

BetaManagedAgentsSessionResource = [BetaManagedAgentsGitHubRepositoryResource](api/beta.md) { id, created\_at, mount\_path, 4 more }  | [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }

Accepts one of the following:

BetaManagedAgentsGitHubRepositoryResource { id, created\_at, mount\_path, 4 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

mount\_path: string

type: "github\_repository"

updated\_at: string

A timestamp in RFC 3339 format

url: string

checkout?: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }  | null

Accepts one of the following:

BetaManagedAgentsBranchCheckout { name, type }

name: string

Branch name to check out.

type: "branch"

BetaManagedAgentsCommitCheckout { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

BetaManagedAgentsFileResource { id, created\_at, file\_id, 3 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

file\_id: string

mount\_path: string

type: "file"

updated\_at: string

A timestamp in RFC 3339 format

ResourceRetrieveResponse = [BetaManagedAgentsGitHubRepositoryResource](api/beta.md) { id, created\_at, mount\_path, 4 more }  | [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }

The requested session resource.

Accepts one of the following:

BetaManagedAgentsGitHubRepositoryResource { id, created\_at, mount\_path, 4 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

mount\_path: string

type: "github\_repository"

updated\_at: string

A timestamp in RFC 3339 format

url: string

checkout?: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }  | null

Accepts one of the following:

BetaManagedAgentsBranchCheckout { name, type }

name: string

Branch name to check out.

type: "branch"

BetaManagedAgentsCommitCheckout { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

BetaManagedAgentsFileResource { id, created\_at, file\_id, 3 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

file\_id: string

mount\_path: string

type: "file"

updated\_at: string

A timestamp in RFC 3339 format

ResourceUpdateResponse = [BetaManagedAgentsGitHubRepositoryResource](api/beta.md) { id, created\_at, mount\_path, 4 more }  | [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }

The updated session resource.

Accepts one of the following:

BetaManagedAgentsGitHubRepositoryResource { id, created\_at, mount\_path, 4 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

mount\_path: string

type: "github\_repository"

updated\_at: string

A timestamp in RFC 3339 format

url: string

checkout?: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }  | null

Accepts one of the following:

BetaManagedAgentsBranchCheckout { name, type }

name: string

Branch name to check out.

type: "branch"

BetaManagedAgentsCommitCheckout { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

BetaManagedAgentsFileResource { id, created\_at, file\_id, 3 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

file\_id: string

mount\_path: string

type: "file"

updated\_at: string

A timestamp in RFC 3339 format

---

*Copyright © Anthropic. All rights reserved.*
