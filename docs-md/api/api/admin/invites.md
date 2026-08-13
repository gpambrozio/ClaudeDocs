# Invites

Copy page



# Invites

##### [Create Invite](api/admin/invites/create.md)

POST/v1/organizations/invites

##### [Get Invite](api/admin/invites/retrieve.md)

GET/v1/organizations/invites/{invite\_id}

##### [List Invites](api/admin/invites/list.md)

GET/v1/organizations/invites

##### [Delete Invite](api/admin/invites/delete.md)

DELETE/v1/organizations/invites/{invite\_id}

##### ModelsExpand Collapse



Invite object { id, accepted\_at, email, 6 more } 

id: string

ID of the Invite.

accepted\_at: string

RFC 3339 datetime string indicating when the Invite was accepted, or null.

email: string

Email of the User being invited.

expires\_at: string

RFC 3339 datetime string indicating when the Invite expires.

invited\_at: string

RFC 3339 datetime string indicating when the Invite was created.

rbac\_group\_ids: array of string

RBAC group IDs recorded on the Invite (beta, Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.



role: "admin" or "billing" or "claude\_code\_user" or 6 more

Organization role of the User.

One of the following:

"admin"

"billing"

"claude\_code\_user"

"developer"

"managed"

"membership\_admin"

"owner"

"primary\_owner"

"user"



status: "accepted" or "deleted" or "expired" or "pending"

Status of the Invite.

One of the following:

"accepted"

"deleted"

"expired"

"pending"



type: "invite"

Object type.

For Invites, this is always `"invite"`.



InviteDeleteResponse object { id, type } 

id: string

ID of the Invite.



type: "invite\_deleted"

Deleted object type.

For Invites, this is always `"invite_deleted"`.

---

*Copyright © Anthropic. All rights reserved.*
