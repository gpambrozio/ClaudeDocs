# Resources

Copy page



cURL

# Resources

##### [Add Session Resource](api/http/beta/sessions/resources/add.md)

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/http/beta/sessions/resources/list.md)

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/http/beta/sessions/resources/retrieve.md)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/http/beta/sessions/resources/update.md)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/http/beta/sessions/resources/delete.md)

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

##### Models



BetaManagedAgentsDeleteSessionResource object{ id, type }

Confirmation of resource deletion.

id: string

type: "session\_resource\_deleted"



BetaManagedAgentsFileResource object{ id, created\_at, file\_id, 3 more }

id: string



created\_at: string

A timestamp in RFC 3339 format

formatdate-time

file\_id: string

mount\_path: string

type: "file"



updated\_at: string

A timestamp in RFC 3339 format

formatdate-time



BetaManagedAgentsGitHubRepositoryResource object{ id, created\_at, mount\_path, 4 more }



BetaManagedAgentsMemoryStoreResource object{ memory\_store\_id, type, access, 4 more }

A memory store attached to an agent session.



BetaManagedAgentsSessionResource = [BetaManagedAgentsGitHubRepositoryResource](api/http/beta/sessions/resources.md) { id, created\_at, mount\_path, 4 more } or [BetaManagedAgentsFileResource](api/http/beta/sessions/resources.md) { id, created\_at, file\_id, 3 more } or [BetaManagedAgentsMemoryStoreResource](api/http/beta/sessions/resources.md) { memory\_store\_id, type, access, 4 more }

A memory store attached to an agent session.

One of the following:



ResourceRetrieveResponse = [BetaManagedAgentsGitHubRepositoryResource](api/http/beta/sessions/resources.md) { id, created\_at, mount\_path, 4 more } or [BetaManagedAgentsFileResource](api/http/beta/sessions/resources.md) { id, created\_at, file\_id, 3 more } or [BetaManagedAgentsMemoryStoreResource](api/http/beta/sessions/resources.md) { memory\_store\_id, type, access, 4 more }

The requested session resource.

One of the following:



ResourceUpdateResponse = [BetaManagedAgentsGitHubRepositoryResource](api/http/beta/sessions/resources.md) { id, created\_at, mount\_path, 4 more } or [BetaManagedAgentsFileResource](api/http/beta/sessions/resources.md) { id, created\_at, file\_id, 3 more } or [BetaManagedAgentsMemoryStoreResource](api/http/beta/sessions/resources.md) { memory\_store\_id, type, access, 4 more }

The updated session resource.

One of the following:

---

*Copyright © Anthropic. All rights reserved.*
