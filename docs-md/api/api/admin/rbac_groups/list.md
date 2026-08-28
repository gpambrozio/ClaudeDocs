# List RBAC Groups

Copy page



# List RBAC Groups

GET/v1/organizations/rbac\_groups

List RBAC Groups in the Claude Enterprise tenant.

The RBAC Groups API is available to Claude Enterprise organizations only.

##### Query parameters



limit: optional number

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

default20

maximum1000

minimum1

page: optional string

Optionally set to the `next_page` token from the previous response.

##### Returns



data: array of [RbacGroup](api/http/admin/rbac_groups.md) { id, created\_at, name, 4 more }

id: string

ID of the RBAC Group.



created\_at: string

RFC 3339 timestamp of when the RBAC Group was created.

formatdate-time

name: string

Name of the RBAC Group. Not uniqueness-enforced.

roles: array of string or null

RBAC Role IDs attached to this RBAC Group. Role attachment is managed in the admin settings and is read-only on this API. `null` means role data was temporarily unavailable — retry to distinguish from an empty list.



source\_type: "direct" or "scim"

How the RBAC Group was created: `"direct"` for groups created directly (for example, in the organization's admin settings), `"scim"` for groups provisioned by the identity provider.

One of the following:

"direct"

"scim"



type: "rbac\_group"

Object type.

For RBAC Groups, this is always `"rbac_group"`.

defaultrbac\_group



updated\_at: string

RFC 3339 timestamp of when the RBAC Group was last updated.

formatdate-time

has\_more: boolean

Indicates if there are more results in the requested page direction.

next\_page: string or null

Token to provide in as `page` in the subsequent request to retrieve the next page of data.



### List RBAC Groups

cURL



```shiki
curl https://api.anthropic.com/v1/organizations/rbac_groups \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "data": [
    {
      "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "name": "Engineering",
      "roles": [
        "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
      ],
      "source_type": "direct",
      "type": "rbac_group",
      "updated_at": "2024-10-30T23:58:27.427722Z"
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
      "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "name": "Engineering",
      "roles": [
        "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
      ],
      "source_type": "direct",
      "type": "rbac_group",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "has_more": false,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19ncm91cF8wMSJ9"
}
```

---

*Copyright © Anthropic. All rights reserved.*
