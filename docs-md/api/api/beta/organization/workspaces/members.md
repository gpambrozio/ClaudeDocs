# Members

Copy page



cURL

# Members

##### [List Workspace Members](api/http/beta/organization/workspaces/members/list.md)

GET/v1/organizations/workspaces/{workspace\_id}/members

##### [Create Workspace Member](api/http/beta/organization/workspaces/members/add.md)

POST/v1/organizations/workspaces/{workspace\_id}/members

##### [Get Workspace Member](api/http/beta/organization/workspaces/members/retrieve.md)

GET/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

##### [Update Workspace Member](api/http/beta/organization/workspaces/members/update.md)

POST/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

##### [Delete Workspace Member](api/http/beta/organization/workspaces/members/remove.md)

DELETE/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

##### Models



MemberRemoveResponse object{ type, user\_id, workspace\_id }



type: "workspace\_member\_deleted"

Deleted object type.

For Workspace Members, this is always `"workspace_member_deleted"`.

defaultworkspace\_member\_deleted

user\_id: string

ID of the User.

workspace\_id: string

ID of the Workspace.

---

*Copyright © Anthropic. All rights reserved.*
