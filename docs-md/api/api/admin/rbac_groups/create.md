# Create RBAC Group

Copy page



# Create RBAC Group

POST/v1/organizations/rbac\_groups

Create an RBAC Group in the Claude Enterprise tenant. Groups created via the API have source type `"direct"`.

The RBAC Groups API is available to Claude Enterprise organizations only.

##### Body



name: string

Name of the RBAC Group. Not uniqueness-enforced.

maxLength255

minLength1

##### Returns



RbacGroup object{ id, created\_at, name, 4 more }

id: string

ID of the RBAC Group.



created\_at: string

RFC 3339 timestamp of when the RBAC Group was created.

formatdate-time

name: string

Name of the RBAC Group. Not uniqueness-enforced.

roles: array of string or null

RBAC Role IDs attached to this RBAC Group. Role attachment is managed in the admin settings and is read-only on this API. `null` means role data was temporarily unavailable — retry to distinguish from an empty list.



source\_type: "direct" or "scim"

How the RBAC Group was created: `"direct"` for groups created directly (for example, in the organization's admin settings), `"scim"` for groups provisioned by the identity provider.

One of the following:

"direct"

"scim"



type: "rbac\_group"

Object type.

For RBAC Groups, this is always `"rbac_group"`.

defaultrbac\_group



updated\_at: string

RFC 3339 timestamp of when the RBAC Group was last updated.

formatdate-time

Create RBAC Group

cURL

```shiki
curl https://api.anthropic.com/v1/organizations/rbac_groups \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -d '{
          "name": "Engineering"
        }'
```

Response 200



```shiki
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
```

##### Returns Examples

Response 200



```shiki
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
```

---

*Copyright © Anthropic. All rights reserved.*
