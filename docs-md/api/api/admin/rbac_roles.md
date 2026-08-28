# RBAC Roles

Copy page



# RBAC Roles

##### [List RBAC Roles](api/http/admin/rbac_roles/list.md)

GET/v1/organizations/rbac\_roles

##### [Get RBAC Role](api/http/admin/rbac_roles/retrieve.md)

GET/v1/organizations/rbac\_roles/{role\_id}

##### Models



RbacRole object{ id, created\_at, name, 2 more }

id: string

ID of the RBAC Role.



created\_at: string

RFC 3339 datetime string indicating when the RBAC Role was created.

formatdate-time

name: string

Name of the RBAC Role.



type: "rbac\_role"

Object type.

For RBAC Roles, this is always `"rbac_role"`.

defaultrbac\_role



updated\_at: string

RFC 3339 datetime string indicating when the RBAC Role was last updated.

formatdate-time

#### RBAC Roles[Permissions](api/http/admin/rbac_roles/permissions.md)

##### [List RBAC Role Permissions](api/http/admin/rbac_roles/permissions/list.md)

GET/v1/organizations/rbac\_roles/{role\_id}/permissions

---

*Copyright © Anthropic. All rights reserved.*
