# Invites

Copy page

# Invites

##### [Create Invite](api/admin/invites/create.md)

post/v1/organizations/invites

##### [Get Invite](api/admin/invites/retrieve.md)

get/v1/organizations/invites/{invite\_id}

##### [List Invites](api/admin/invites/list.md)

get/v1/organizations/invites

##### [Delete Invite](api/admin/invites/delete.md)

delete/v1/organizations/invites/{invite\_id}

##### ModelsExpand Collapse

Invite = object { id, email, expires\_at, 4 more }

id: string

ID of the Invite.

email: string

Email of the User being invited.

expires\_at: string

RFC 3339 datetime string indicating when the Invite expires.

formatdate-time

invited\_at: string

RFC 3339 datetime string indicating when the Invite was created.

formatdate-time

role: "user" or "developer" or "billing" or 2 more

Organization role of the User.

Accepts one of the following:

"user"

"developer"

"billing"

"admin"

"claude\_code\_user"

status: "accepted" or "expired" or "deleted" or "pending"

Status of the Invite.

Accepts one of the following:

"accepted"

"expired"

"deleted"

"pending"

type: "invite"

Object type.

For Invites, this is always `"invite"`.

Accepts one of the following:

"invite"

---

*Copyright © Anthropic. All rights reserved.*
