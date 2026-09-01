# Get RBAC Role

Copy page



# Get RBAC Role

GET/v1/organizations/rbac\_roles/{role\_id}

Retrieve an RBAC Role by ID.

The RBAC Roles API is available to Claude Enterprise organizations only.

##### Path parameters

role\_id: string

ID of the RBAC Role.

##### Returns



RbacRole object{ id, created\_at, name, 2 more }

id: string

ID of the RBAC Role.



created\_at: string

RFC 3339 datetime string indicating when the RBAC Role was created.

formatdate-time

name: string

Name of the RBAC Role.



type: "rbac\_role"

Object type.

For RBAC Roles, this is always `"rbac_role"`.

defaultrbac\_role



updated\_at: string

RFC 3339 datetime string indicating when the RBAC Role was last updated.

formatdate-time

Get RBAC Role

cURL

```shiki
curl https://api.anthropic.com/v1/organizations/rbac_roles/$ROLE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "id": "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "name": "Project Editor",
  "type": "rbac_role",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "name": "Project Editor",
  "type": "rbac_role",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

---

*Copyright © Anthropic. All rights reserved.*
