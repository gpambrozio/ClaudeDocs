# Local

Copy page



# Local

##### [List local sessions](api/http/compliance/apps/sessions/local/list.md)

GET/v1/compliance/apps/sessions/local

##### [Retrieve a local session](api/http/compliance/apps/sessions/local/retrieve.md)

GET/v1/compliance/apps/sessions/local/{local\_session\_id}

##### Models



LocalListResponse object{ id, created\_at, organization\_uuid, 5 more }

A Cowork or Claude Code session that a user ran on their own computer
while signed in with their organization account.



LocalRetrieveResponse object{ id, created\_at, organization\_uuid, 5 more }

A Cowork or Claude Code session that a user ran on their own computer
while signed in with their organization account.

#### Local[Messages](api/http/compliance/apps/sessions/local/messages.md)

##### [Retrieve local session messages](api/http/compliance/apps/sessions/local/messages/list.md)

GET/v1/compliance/apps/sessions/local/{local\_session\_id}/messages

---

*Copyright © Anthropic. All rights reserved.*
