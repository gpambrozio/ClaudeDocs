# Resources

Copy page

CLI

# Resources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

$ ant beta:sessions:resources add

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

$ ant beta:sessions:resources list

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

$ ant beta:sessions:resources retrieve

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

$ ant beta:sessions:resources update

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

$ ant beta:sessions:resources delete

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

##### ModelsExpand Collapse

beta\_managed\_agents\_delete\_session\_resource: object { id, type }

Confirmation of resource deletion.

id: string

type: "session\_resource\_deleted"

"session\_resource\_deleted"

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

beta\_managed\_agents\_session\_resource: [BetaManagedAgentsGitHubRepositoryResource](api/beta.md) { id, created\_at, mount\_path, 4 more }  or [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }

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

---

*Copyright © Anthropic. All rights reserved.*
