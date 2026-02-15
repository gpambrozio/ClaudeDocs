# Create Workspace Member

Copy page

# Create Workspace Member

POST/v1/organizations/workspaces/{workspace\_id}/members

Create Workspace Member

##### Path ParametersExpand Collapse

workspace\_id: string

ID of the Workspace.

##### Body ParametersJSONExpand Collapse

user\_id: string

ID of the User.

workspace\_role: "workspace\_user" or "workspace\_developer" or "workspace\_admin"

Role of the new Workspace Member. Cannot be "workspace\_billing".

Accepts one of the following:

"workspace\_user"

"workspace\_developer"

"workspace\_admin"

##### ReturnsExpand Collapse

WorkspaceMember = object { type, user\_id, workspace\_id, workspace\_role }

type: "workspace\_member"

Object type.

For Workspace Members, this is always `"workspace_member"`.

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

Create Workspace Member

```shiki
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY" \
    -d '{
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
          "workspace_role": "workspace_user"
        }'
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
