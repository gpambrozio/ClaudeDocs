# Members

Copy page



# Members

##### [List RBAC Group Members](api/http/admin/rbac_groups/members/list.md)

GET/v1/organizations/rbac\_groups/{group\_id}/members

##### [Add RBAC Group Member](api/http/admin/rbac_groups/members/create.md)

POST/v1/organizations/rbac\_groups/{group\_id}/members

##### [Remove RBAC Group Member](api/http/admin/rbac_groups/members/delete.md)

DELETE/v1/organizations/rbac\_groups/{group\_id}/members/{user\_id}

##### Models



RbacGroupMember object{ created\_at, email, group\_id, 2 more }



created\_at: string

RFC 3339 timestamp of when the User was added to the RBAC Group.

formatdate-time

email: string

Email of the User.

group\_id: string

ID of the RBAC Group.



type: "rbac\_group\_member"

Object type.

For RBAC Group Members, this is always `"rbac_group_member"`.

defaultrbac\_group\_member

user\_id: string

ID of the User.



RbacGroupMemberDeleted object{ group\_id, type, user\_id }

group\_id: string

ID of the RBAC Group.



type: "rbac\_group\_member\_deleted"

Deleted object type. For RBAC Group Members, this is always `"rbac_group_member_deleted"`.

defaultrbac\_group\_member\_deleted

user\_id: string

ID of the User.

---

*Copyright © Anthropic. All rights reserved.*
