# Invites

Copy page

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

Invite object { id, email, expires\_at, 4 more } 

id: string

ID of the Invite.

email: string

Email of the User being invited.

expires\_at: string

RFC 3339 datetime string indicating when the Invite expires.

invited\_at: string

RFC 3339 datetime string indicating when the Invite was created.



role: "user" or "developer" or "billing" or 2 more

Organization role of the User.

One of the following:

"user"

"developer"

"billing"

"admin"

"claude\_code\_user"



status: "accepted" or "expired" or "deleted" or "pending"

Status of the Invite.

One of the following:

"accepted"

"expired"

"deleted"

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
