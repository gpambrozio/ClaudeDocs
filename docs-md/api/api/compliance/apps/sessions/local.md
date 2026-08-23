# Local

Copy page



# Local

##### [List local sessions](api/compliance/apps/sessions/local/list.md)

GET/v1/compliance/apps/sessions/local

##### [Retrieve a local session](api/compliance/apps/sessions/local/retrieve.md)

GET/v1/compliance/apps/sessions/local/{local\_session\_id}

##### ModelsExpand Collapse



LocalListResponse object { id, created\_at, organization\_uuid, 4 more } 

A Cowork or Claude Code session that a user ran on their own computer
while signed in with their organization account.

id: string

Local session identifier, prefixed `clls_`. Unique within the parent organization. Treat as an opaque string; the format may change without notice.

created\_at: string

Timestamp of the session's first retained inference call (RFC 3339, UTC). When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected, so this value is the timestamp of the earliest retained call: always strictly after the boundary, never the boundary itself.

organization\_uuid: string

UUID of the child organization the session belongs to

product\_surface: string or null

The product the session ran in: `cowork` for Cowork sessions in Claude Desktop, or `claude_code` for Claude Code sessions. New values appear as coverage expands; treat unrecognized values as opaque. `null` when the surface was not recorded.

type: "compliance\_local\_session"



user: object { id, email\_address } 

The authenticated user at the time of the session. Always set; `user.id` is always populated. `user.email_address` is null when the user's account has been deleted or the user is no longer a member of an organization the key may read.

id: string

User identifier (tagged ID, prefixed `user_`). Always set, so attribution survives after the user's account is deleted or the user leaves the organizations the key may read.

email\_address: string or null

User's email address. Null when the user's account has been deleted or the user is no longer a member of an organization the key may read. The messages endpoint does not resolve email addresses; this field is always null there.

workspace\_id: string or null

Workspace identifier (tagged ID, prefixed `wrkspc_`). Null for sessions not attributed to a workspace.



LocalRetrieveResponse object { id, created\_at, organization\_uuid, 4 more } 

A Cowork or Claude Code session that a user ran on their own computer
while signed in with their organization account.

id: string

Local session identifier, prefixed `clls_`. Unique within the parent organization. Treat as an opaque string; the format may change without notice.

created\_at: string

Timestamp of the session's first retained inference call (RFC 3339, UTC). When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected, so this value is the timestamp of the earliest retained call: always strictly after the boundary, never the boundary itself.

organization\_uuid: string

UUID of the child organization the session belongs to

product\_surface: string or null

The product the session ran in: `cowork` for Cowork sessions in Claude Desktop, or `claude_code` for Claude Code sessions. New values appear as coverage expands; treat unrecognized values as opaque. `null` when the surface was not recorded.

type: "compliance\_local\_session"



user: object { id, email\_address } 

The authenticated user at the time of the session. Always set; `user.id` is always populated. `user.email_address` is null when the user's account has been deleted or the user is no longer a member of an organization the key may read.

id: string

User identifier (tagged ID, prefixed `user_`). Always set, so attribution survives after the user's account is deleted or the user leaves the organizations the key may read.

email\_address: string or null

User's email address. Null when the user's account has been deleted or the user is no longer a member of an organization the key may read. The messages endpoint does not resolve email addresses; this field is always null there.

workspace\_id: string or null

Workspace identifier (tagged ID, prefixed `wrkspc_`). Null for sessions not attributed to a workspace.

#### LocalMessages

##### [Retrieve local session messages](api/compliance/apps/sessions/local/messages/list.md)

GET/v1/compliance/apps/sessions/local/{local\_session\_id}/messages

---

*Copyright © Anthropic. All rights reserved.*
