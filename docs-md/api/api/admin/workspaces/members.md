# Members

Copy page



# Members

##### [Create Workspace Member](api/admin/workspaces/members/create.md)

POST/v1/organizations/workspaces/{workspace\_id}/members

##### [Get Workspace Member](api/admin/workspaces/members/retrieve.md)

GET/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

##### [List Workspace Members](api/admin/workspaces/members/list.md)

GET/v1/organizations/workspaces/{workspace\_id}/members

##### [Update Workspace Member](api/admin/workspaces/members/update.md)

POST/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

##### [Delete Workspace Member](api/admin/workspaces/members/delete.md)

DELETE/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

##### ModelsExpand Collapse



WorkspaceMember object { type, user\_id, workspace\_id, workspace\_role } 



type: "workspace\_member"

Object type.

For Workspace Members, this is always `"workspace_member"`.

user\_id: string

ID of the User.

workspace\_id: string

ID of the Workspace.



workspace\_role: "workspace\_admin" or "workspace\_billing" or "workspace\_developer" or 2 more

Role of the Workspace Member.

One of the following:

"workspace\_admin"

"workspace\_billing"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_user"



MemberDeleteResponse object { type, user\_id, workspace\_id } 



type: "workspace\_member\_deleted"

Deleted object type.

For Workspace Members, this is always `"workspace_member_deleted"`.

user\_id: string

ID of the User.

workspace\_id: string

ID of the Workspace.

---

*Copyright © Anthropic. All rights reserved.*
