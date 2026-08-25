# Invites

Copy page



# Invites

##### [Create Invite](api/http/admin/invites/create.md)

POST/v1/organizations/invites

##### [Get Invite](api/http/admin/invites/retrieve.md)

GET/v1/organizations/invites/{invite\_id}

##### [List Invites](api/http/admin/invites/list.md)

GET/v1/organizations/invites

##### [Delete Invite](api/http/admin/invites/delete.md)

DELETE/v1/organizations/invites/{invite\_id}

##### Models



Invite object{ id, accepted\_at, email, 6 more }



InviteDeleteResponse object{ id, type }

id: string

ID of the Invite.



type: "invite\_deleted"

Deleted object type.

For Invites, this is always `"invite_deleted"`.

defaultinvite\_deleted

---

*Copyright © Anthropic. All rights reserved.*
