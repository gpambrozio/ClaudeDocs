# Resources

Copy page

Python

# Resources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

beta.sessions.resources.add(strsession\_id, ResourceAddParams\*\*kwargs)  -> [BetaManagedAgentsFileResource](api/beta.md)

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

beta.sessions.resources.list(strsession\_id, ResourceListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsSessionResource](api/beta.md)]

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

beta.sessions.resources.retrieve(strresource\_id, ResourceRetrieveParams\*\*kwargs)  -> [ResourceRetrieveResponse](api/beta.md)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

beta.sessions.resources.update(strresource\_id, ResourceUpdateParams\*\*kwargs)  -> [ResourceUpdateResponse](api/beta.md)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

beta.sessions.resources.delete(strresource\_id, ResourceDeleteParams\*\*kwargs)  -> [BetaManagedAgentsDeleteSessionResource](api/beta.md)

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

##### ModelsExpand Collapse

class BetaManagedAgentsDeleteSessionResource: …

Confirmation of resource deletion.

id: str

type: Literal["session\_resource\_deleted"]

class BetaManagedAgentsFileResource: …

id: str

created\_at: datetime

A timestamp in RFC 3339 format

file\_id: str

mount\_path: str

type: Literal["file"]

updated\_at: datetime

A timestamp in RFC 3339 format

class BetaManagedAgentsGitHubRepositoryResource: …

id: str

created\_at: datetime

A timestamp in RFC 3339 format

mount\_path: str

type: Literal["github\_repository"]

updated\_at: datetime

A timestamp in RFC 3339 format

url: str

checkout: Optional[Checkout]

Accepts one of the following:

class BetaManagedAgentsBranchCheckout: …

name: str

Branch name to check out.

type: Literal["branch"]

class BetaManagedAgentsCommitCheckout: …

sha: str

Full commit SHA to check out.

type: Literal["commit"]

[BetaManagedAgentsSessionResource](api/beta.md)

Accepts one of the following:

class BetaManagedAgentsGitHubRepositoryResource: …

id: str

created\_at: datetime

A timestamp in RFC 3339 format

mount\_path: str

type: Literal["github\_repository"]

updated\_at: datetime

A timestamp in RFC 3339 format

url: str

checkout: Optional[Checkout]

Accepts one of the following:

class BetaManagedAgentsBranchCheckout: …

name: str

Branch name to check out.

type: Literal["branch"]

class BetaManagedAgentsCommitCheckout: …

sha: str

Full commit SHA to check out.

type: Literal["commit"]

class BetaManagedAgentsFileResource: …

id: str

created\_at: datetime

A timestamp in RFC 3339 format

file\_id: str

mount\_path: str

type: Literal["file"]

updated\_at: datetime

A timestamp in RFC 3339 format

[ResourceRetrieveResponse](api/beta.md)

The requested session resource.

Accepts one of the following:

class BetaManagedAgentsGitHubRepositoryResource: …

id: str

created\_at: datetime

A timestamp in RFC 3339 format

mount\_path: str

type: Literal["github\_repository"]

updated\_at: datetime

A timestamp in RFC 3339 format

url: str

checkout: Optional[Checkout]

Accepts one of the following:

class BetaManagedAgentsBranchCheckout: …

name: str

Branch name to check out.

type: Literal["branch"]

class BetaManagedAgentsCommitCheckout: …

sha: str

Full commit SHA to check out.

type: Literal["commit"]

class BetaManagedAgentsFileResource: …

id: str

created\_at: datetime

A timestamp in RFC 3339 format

file\_id: str

mount\_path: str

type: Literal["file"]

updated\_at: datetime

A timestamp in RFC 3339 format

[ResourceUpdateResponse](api/beta.md)

The updated session resource.

Accepts one of the following:

class BetaManagedAgentsGitHubRepositoryResource: …

id: str

created\_at: datetime

A timestamp in RFC 3339 format

mount\_path: str

type: Literal["github\_repository"]

updated\_at: datetime

A timestamp in RFC 3339 format

url: str

checkout: Optional[Checkout]

Accepts one of the following:

class BetaManagedAgentsBranchCheckout: …

name: str

Branch name to check out.

type: Literal["branch"]

class BetaManagedAgentsCommitCheckout: …

sha: str

Full commit SHA to check out.

type: Literal["commit"]

class BetaManagedAgentsFileResource: …

id: str

created\_at: datetime

A timestamp in RFC 3339 format

file\_id: str

mount\_path: str

type: Literal["file"]

updated\_at: datetime

A timestamp in RFC 3339 format

---

*Copyright © Anthropic. All rights reserved.*
