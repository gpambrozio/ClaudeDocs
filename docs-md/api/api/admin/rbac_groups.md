# RBAC Groups

Copy page



# RBAC Groups

##### [List RBAC Groups](api/admin/rbac_groups/list.md)

GET/v1/organizations/rbac\_groups

##### [Get RBAC Group](api/admin/rbac_groups/retrieve.md)

GET/v1/organizations/rbac\_groups/{group\_id}

##### [Create RBAC Group](api/admin/rbac_groups/create.md)

POST/v1/organizations/rbac\_groups

##### [Update RBAC Group](api/admin/rbac_groups/update.md)

POST/v1/organizations/rbac\_groups/{group\_id}

##### [Delete RBAC Group](api/admin/rbac_groups/delete.md)

DELETE/v1/organizations/rbac\_groups/{group\_id}

##### ModelsExpand Collapse



RbacGroup object { id, created\_at, name, 4 more } 

id: string

ID of the RBAC Group.

created\_at: string

RFC 3339 timestamp of when the RBAC Group was created.

name: string

Name of the RBAC Group. Not uniqueness-enforced.

roles: array of string

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

updated\_at: string

RFC 3339 timestamp of when the RBAC Group was last updated.



RbacGroupDeleted object { id, type } 

id: string

ID of the RBAC Group.



type: "rbac\_group\_deleted"

Deleted object type.

For RBAC Groups, this is always `"rbac_group_deleted"`.

#### RBAC GroupsMembers

##### [List RBAC Group Members](api/admin/rbac_groups/members/list.md)

GET/v1/organizations/rbac\_groups/{group\_id}/members

##### [Add RBAC Group Member](api/admin/rbac_groups/members/create.md)

POST/v1/organizations/rbac\_groups/{group\_id}/members

##### [Remove RBAC Group Member](api/admin/rbac_groups/members/delete.md)

DELETE/v1/organizations/rbac\_groups/{group\_id}/members/{user\_id}

---

*Copyright © Anthropic. All rights reserved.*
