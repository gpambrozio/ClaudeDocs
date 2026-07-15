# List RBAC Roles

Copy page



# List RBAC Roles

GET/v1/organizations/rbac\_roles

List RBAC Roles in the organization.

The RBAC Roles API is in beta and available to Claude Enterprise organizations only. Requests must send the `ce-user-management-2026-07-13` value in the `anthropic-beta` header.

##### Query ParametersExpand Collapse



limit: optional number

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

maximum1000

minimum1

page: optional string

Optionally set to the `next_page` token from the previous response.

##### Header ParametersExpand Collapse



"anthropic-beta": optional array of string

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

##### ReturnsExpand Collapse



data: array of [RbacRole](api/admin/rbac_roles.md) { id, created\_at, name, 2 more } 

id: string

ID of the RBAC Role.

created\_at: string

RFC 3339 datetime string indicating when the RBAC Role was created.

name: string

Name of the RBAC Role.



type: "rbac\_role"

Object type.

For RBAC Roles, this is always `"rbac_role"`.

updated\_at: string

RFC 3339 datetime string indicating when the RBAC Role was last updated.

has\_more: boolean

Indicates whether there are more results beyond this page.

next\_page: string

Opaque cursor for the next page. Pass as the `page` parameter on the next
request.

List RBAC Roles



```shiki
curl https://api.anthropic.com/v1/organizations/rbac_roles \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "data": [
    {
      "id": "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "name": "Project Editor",
      "type": "rbac_role",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "has_more": true,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19yb2xlXzAxIn0"
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "id": "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "name": "Project Editor",
      "type": "rbac_role",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "has_more": true,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19yb2xlXzAxIn0"
}
```

---

*Copyright © Anthropic. All rights reserved.*
