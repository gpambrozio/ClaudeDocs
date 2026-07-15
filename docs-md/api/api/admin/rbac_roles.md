# RBAC Roles

Copy page



# RBAC Roles

##### [List RBAC Roles](api/admin/rbac_roles/list.md)

GET/v1/organizations/rbac\_roles

##### [Get RBAC Role](api/admin/rbac_roles/retrieve.md)

GET/v1/organizations/rbac\_roles/{role\_id}

##### ModelsExpand Collapse



RbacRole object { id, created\_at, name, 2 more } 

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

#### RBAC RolesPermissions

##### [List RBAC Role Permissions](api/admin/rbac_roles/permissions/list.md)

GET/v1/organizations/rbac\_roles/{role\_id}/permissions

---

*Copyright © Anthropic. All rights reserved.*
