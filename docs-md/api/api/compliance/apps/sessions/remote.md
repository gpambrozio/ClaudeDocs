# Remote

Copy page



# Remote

##### [List remote sessions](api/compliance/apps/sessions/remote/list.md)

GET/v1/compliance/apps/sessions/remote

##### ModelsExpand Collapse



RemoteListResponse object { id, agent\_id, claude\_project\_id, 7 more } 

Metadata for one remote session, as returned in the list response
and in the messages response's `session` field.

Carries session attributes only, not transcript content. Use the
messages endpoint to retrieve a session's transcript.

id: string

Remote session identifier

agent\_id: string or null

Identifier of the automated agent that owns the session. Null for user-owned sessions. At most one of `user` and `agent_id` is set.

claude\_project\_id: string or null

ID of the project the session is bound to. Null when the session has no project binding.

created\_at: string

When the session was created (RFC 3339, UTC)

organization\_uuid: string

UUID of the organization the session belongs to

product\_surface: string or null

The Claude product the session was created from. Currently `cowork_remote`, for Cowork sessions started on claude.ai web or mobile. More values will appear as other surfaces launch, so treat any unrecognized value as an unclassified surface rather than an error. Null for sessions created before this field was recorded, for surfaces that do not stamp it, and for unrecognized tag values.



started\_by\_user: object { id, email\_address }  or null

A user associated with a remote session.

id: string

User identifier

email\_address: string or null

User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

status: string

Session lifecycle state. One of `active`, `paused`, `archived`, or `failed` — the lifecycle states the owning product surface exposes — plus `pending`, a brief transient state that resolves before any transcript content exists. The list endpoint includes `pending`; the messages endpoint returns 404 for it. Deleted sessions are not returned on either endpoint. Treat unrecognized values as an unknown state rather than an error.

updated\_at: string

When the session was last modified (RFC 3339, UTC)



user: object { id, email\_address }  or null

A user associated with a remote session.

id: string

User identifier

email\_address: string or null

User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

#### RemoteMessages

##### [Retrieve remote session messages](api/compliance/apps/sessions/remote/messages/list.md)

GET/v1/compliance/apps/sessions/remote/{claude\_remote\_session\_id}/messages

---

*Copyright © Anthropic. All rights reserved.*
