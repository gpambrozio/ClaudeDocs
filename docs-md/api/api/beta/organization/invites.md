# Invites

Copy page



cURL

# Invites

##### [Create Invite](api/http/beta/organization/invites/create.md)

POST/v1/organizations/invites

##### [List Invites](api/http/beta/organization/invites/list.md)

GET/v1/organizations/invites

##### [Get Invite](api/http/beta/organization/invites/retrieve.md)

GET/v1/organizations/invites/{invite\_id}

##### [Delete Invite](api/http/beta/organization/invites/delete.md)

DELETE/v1/organizations/invites/{invite\_id}

##### Models



BetaOrganizationInvite object{ id, accepted\_at, email, 6 more }



InviteDeleteResponse object{ id, type }

id: string

ID of the Invite.



type: "invite\_deleted"

Deleted object type.

For Invites, this is always `"invite_deleted"`.

defaultinvite\_deleted

---

*Copyright © Anthropic. All rights reserved.*
