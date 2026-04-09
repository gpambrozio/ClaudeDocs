# Resources

Copy page

Ruby

# Resources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

beta.sessions.resources.add(session\_id, \*\*kwargs) -> [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

beta.sessions.resources.list(session\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsSessionResource](api/beta.md)>

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

beta.sessions.resources.retrieve(resource\_id, \*\*kwargs) -> [ResourceRetrieveResponse](api/beta.md)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

beta.sessions.resources.update(resource\_id, \*\*kwargs) -> [ResourceUpdateResponse](api/beta.md)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

beta.sessions.resources.delete(resource\_id, \*\*kwargs) -> [BetaManagedAgentsDeleteSessionResource](api/beta.md) { id, type }

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

##### ModelsExpand Collapse

class BetaManagedAgentsDeleteSessionResource { id, type }

Confirmation of resource deletion.

id: String

type: :session\_resource\_deleted

class BetaManagedAgentsFileResource { id, created\_at, file\_id, 3 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

file\_id: String

mount\_path: String

type: :file

updated\_at: Time

A timestamp in RFC 3339 format

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

BetaManagedAgentsSessionResource = [BetaManagedAgentsGitHubRepositoryResource](api/beta.md) { id, created\_at, mount\_path, 4 more }  | [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }

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

ResourceRetrieveResponse = [BetaManagedAgentsGitHubRepositoryResource](api/beta.md) { id, created\_at, mount\_path, 4 more }  | [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }

The requested session resource.

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

---

*Copyright © Anthropic. All rights reserved.*
