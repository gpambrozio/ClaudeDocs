# Delete Workspace Member

Copy page

# Delete Workspace Member

DELETE/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

Delete Workspace Member

##### Path ParametersExpand Collapse

workspace\_id: string

ID of the Workspace.

user\_id: string

ID of the User.

##### ReturnsExpand Collapse

type: "workspace\_member\_deleted"

Deleted object type.

For Workspace Members, this is always `"workspace_member_deleted"`.

user\_id: string

ID of the User.

workspace\_id: string

ID of the Workspace.

Delete Workspace Member

```shiki
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members/$USER_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
