# List Invites

Copy page



# List Invites

GET/v1/organizations/invites

List the organization's invites.

##### Query parameters

after\_id: optional string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

before\_id: optional string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.



email: optional string

Filter by the email address the Invite was sent to. Matches the same way as the Users list's `email` filter (normalized, case-insensitive).

formatemail



limit: optional number

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

default20

maximum1000

minimum1



roles: optional array of string

Filter to items whose `role` equals one of the supplied values. Repeatable; values are OR'ed together.

Accepted values depend on the organization type: Console and API organizations accept `user`, `developer`, `billing`, `admin`, and `claude_code_user`; Claude Enterprise organizations accept `user`, `owner`, `primary_owner`, `membership_admin`, and `managed`.



statuses: optional array of "accepted" or "expired" or "pending"

Filter by Invite status. Repeatable; values are OR'ed together. Omit to return `pending`, `accepted`, and `expired` Invites alike.

One of the following:

"accepted"

"expired"

"pending"

##### Returns



data: array of [Invite](api/http/admin/invites.md) { id, accepted\_at, email, 6 more }

id: string

ID of the Invite.



accepted\_at: string or null

RFC 3339 datetime string indicating when the Invite was accepted, or null.

formatdate-time

email: string

Email of the User being invited.



expires\_at: string

RFC 3339 datetime string indicating when the Invite expires.

formatdate-time



invited\_at: string

RFC 3339 datetime string indicating when the Invite was created.

formatdate-time

rbac\_group\_ids: array of string

RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

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

defaultinvite

first\_id: string or null

First ID in the `data` list. Can be used as the `before_id` for the previous page.

has\_more: boolean

Indicates if there are more results in the requested page direction.

last\_id: string or null

Last ID in the `data` list. Can be used as the `after_id` for the next page.

List Invites

cURL

```shiki
curl https://api.anthropic.com/v1/organizations/invites \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "data": [
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
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
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
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

---

*Copyright © Anthropic. All rights reserved.*
