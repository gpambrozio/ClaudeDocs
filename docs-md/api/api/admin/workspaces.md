# Workspaces

Copy page

# Workspaces

##### [Create Workspace](api/admin/workspaces/create.md)

post/v1/organizations/workspaces

##### [Get Workspace](api/admin/workspaces/retrieve.md)

get/v1/organizations/workspaces/{workspace\_id}

##### [List Workspaces](api/admin/workspaces/list.md)

get/v1/organizations/workspaces

##### [Update Workspace](api/admin/workspaces/update.md)

post/v1/organizations/workspaces/{workspace\_id}

##### [Archive Workspace](api/admin/workspaces/archive.md)

post/v1/organizations/workspaces/{workspace\_id}/archive

#### WorkspacesMembers

##### [Create Workspace Member](api/admin/workspaces/members/create.md)

post/v1/organizations/workspaces/{workspace\_id}/members

##### [Get Workspace Member](api/admin/workspaces/members/retrieve.md)

get/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

##### [List Workspace Members](api/admin/workspaces/members/list.md)

get/v1/organizations/workspaces/{workspace\_id}/members

##### [Update Workspace Member](api/admin/workspaces/members/update.md)

post/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

##### [Delete Workspace Member](api/admin/workspaces/members/delete.md)

delete/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

##### ModelsExpand Collapse

WorkspaceMember = object { type, user\_id, workspace\_id, workspace\_role }

type: "workspace\_member"

Object type.

For Workspace Members, this is always `"workspace_member"`.

Accepts one of the following:

"workspace\_member"

user\_id: string

ID of the User.

workspace\_id: string

ID of the Workspace.

workspace\_role: "workspace\_user" or "workspace\_developer" or "workspace\_admin" or "workspace\_billing"

Role of the Workspace Member.

Accepts one of the following:

"workspace\_user"

"workspace\_developer"

"workspace\_admin"

"workspace\_billing"