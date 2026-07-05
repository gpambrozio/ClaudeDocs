# Create Workspace Member

Copy page



# Create Workspace Member

POST/v1/organizations/workspaces/{workspace\_id}/members

Create Workspace Member

##### Path ParametersExpand Collapse

workspace\_id: string

ID of the Workspace.

##### Body ParametersJSONExpand Collapse

user\_id: string

ID of the User.



workspace\_role: "workspace\_admin" or "workspace\_developer" or "workspace\_restricted\_developer" or "workspace\_user"

Role of the new Workspace Member. Cannot be "workspace\_billing".

One of the following:

"workspace\_admin"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_user"

##### ReturnsExpand Collapse

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

Create Workspace Member



```shiki
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
          "workspace_role": "workspace_admin"
        }'
```

Response 200



```shiki
{
  "type": "workspace_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "workspace_role": "workspace_user"
}
```

##### Returns Examples

Response 200



```shiki
{
  "type": "workspace_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "workspace_role": "workspace_user"
}
```

---

*Copyright © Anthropic. All rights reserved.*
