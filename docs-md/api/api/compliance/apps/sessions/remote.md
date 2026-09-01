# Remote

Copy page



# Remote

##### [List remote sessions](api/http/compliance/apps/sessions/remote/list.md)

GET/v1/compliance/apps/sessions/remote

##### Models



RemoteListResponse object{ id, agent\_id, claude\_project\_id, 7 more }

Metadata for one remote session, as returned in the list response
and in the messages response's `session` field.

Carries session attributes only, not transcript content. Use the
messages endpoint to retrieve a session's transcript.

#### Remote[Messages](api/http/compliance/apps/sessions/remote/messages.md)

##### [Retrieve remote session messages](api/http/compliance/apps/sessions/remote/messages/list.md)

GET/v1/compliance/apps/sessions/remote/{claude\_remote\_session\_id}/messages

---

*Copyright © Anthropic. All rights reserved.*
