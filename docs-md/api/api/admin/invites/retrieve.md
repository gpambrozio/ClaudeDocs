# Get Invite

Copy page



# Get Invite

GET/v1/organizations/invites/{invite\_id}

For Claude Enterprise organizations, this endpoint's availability is in beta.

##### Path ParametersExpand Collapse

invite\_id: string

ID of the Invite.

##### ReturnsExpand Collapse

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

Get Invite



```shiki
curl https://api.anthropic.com/v1/organizations/invites/$INVITE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "accepted_at": "2019-12-27T18:11:19.117Z",
  "email": "user@emaildomain.com",
  "expires_at": "2024-11-20T23:58:27.427722Z",
  "invited_at": "2024-10-30T23:58:27.427722Z",
  "rbac_group_ids": [
    "string"
  ],
  "role": "user",
  "status": "pending",
  "type": "invite"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "accepted_at": "2019-12-27T18:11:19.117Z",
  "email": "user@emaildomain.com",
  "expires_at": "2024-11-20T23:58:27.427722Z",
  "invited_at": "2024-10-30T23:58:27.427722Z",
  "rbac_group_ids": [
    "string"
  ],
  "role": "user",
  "status": "pending",
  "type": "invite"
}
```

---

*Copyright © Anthropic. All rights reserved.*
