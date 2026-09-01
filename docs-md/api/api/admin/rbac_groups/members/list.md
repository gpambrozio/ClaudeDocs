# List RBAC Group Members

Copy page



# List RBAC Group Members

GET/v1/organizations/rbac\_groups/{group\_id}/members

List members of an RBAC Group.

The RBAC Groups API is available to Claude Enterprise organizations only.

##### Path parameters

group\_id: string

ID of the RBAC Group.

##### Query parameters



limit: optional number

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

default20

maximum1000

minimum1

page: optional string

Optionally set to the `next_page` token from the previous response.

##### Returns



data: array of [RbacGroupMember](api/http/admin/rbac_groups/members.md) { created\_at, email, group\_id, 2 more }



created\_at: string

RFC 3339 timestamp of when the User was added to the RBAC Group.

formatdate-time

email: string

Email of the User.

group\_id: string

ID of the RBAC Group.



type: "rbac\_group\_member"

Object type.

For RBAC Group Members, this is always `"rbac_group_member"`.

defaultrbac\_group\_member

user\_id: string

ID of the User.

has\_more: boolean

Indicates if there are more results in the requested page direction.

next\_page: string or null

Token to provide in as `page` in the subsequent request to retrieve the next page of data.

List RBAC Group Members

cURL

```shiki
curl https://api.anthropic.com/v1/organizations/rbac_groups/$GROUP_ID/members \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "data": [
    {
      "created_at": "2024-10-30T23:58:27.427722Z",
      "email": "user@emaildomain.com",
      "group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "type": "rbac_group_member",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    }
  ],
  "has_more": false,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19ncm91cF8wMSJ9"
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "created_at": "2024-10-30T23:58:27.427722Z",
      "email": "user@emaildomain.com",
      "group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "type": "rbac_group_member",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    }
  ],
  "has_more": false,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19ncm91cF8wMSJ9"
}
```

---

*Copyright © Anthropic. All rights reserved.*
