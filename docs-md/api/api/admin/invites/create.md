# Create Invite

Copy page



# Create Invite

POST/v1/organizations/invites

For Claude Enterprise organizations, this endpoint's availability is in beta.

On plans that draw members from a finite pool of purchased seats, the invite automatically consumes a seat from the lowest tier with availability; there is no seat-tier parameter. When no seat is free the request fails with a 400 error rather than purchasing a seat.

##### Body ParametersJSONExpand Collapse

email: string

Email of the User.



role: "billing" or "claude\_code\_user" or "developer" or 2 more

Role for the invited User.

The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations (beta) accept `user` and `managed`.

One of the following:

"billing"

"claude\_code\_user"

"developer"

"managed"

"user"

rbac\_group\_ids: optional array of string

RBAC group IDs to assign to the User when the Invite is accepted. A non-empty array is accepted only for a Claude Enterprise organization with RBAC groups (beta), and requires the key to carry the `write:rbac_groups` scope.

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

Create Invite



```shiki
curl https://api.anthropic.com/v1/organizations/invites \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "email": "user@emaildomain.com",
          "role": "user"
        }'
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
