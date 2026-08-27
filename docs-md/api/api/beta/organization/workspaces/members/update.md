# Update Workspace Member

Copy page



cURL

# Update Workspace Member

POST/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

Update Workspace Member

##### Path parameters

workspace\_id: string

ID of the Workspace.

user\_id: string

ID of the User.

##### Body



workspace\_role: [BetaWorkspaceRole](api/http/beta/organization/workspaces.md)

New workspace role for the User.

One of the following:

"workspace\_admin"

"workspace\_billing"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_user"

##### Returns



BetaWorkspaceMember object{ type, user\_id, workspace\_id, workspace\_role }



type: "workspace\_member"

Object type.

For Workspace Members, this is always `"workspace_member"`.

defaultworkspace\_member

user\_id: string

ID of the User.

workspace\_id: string

ID of the Workspace.



workspace\_role: [BetaWorkspaceRole](api/http/beta/organization/workspaces.md)

Role of the Workspace Member.

One of the following:

"workspace\_admin"

"workspace\_billing"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_user"

### Update Workspace Member

cURL



```shiki
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members/$USER_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
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
  "workspace_role": "workspace_admin"
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
  "workspace_role": "workspace_admin"
}
```

---

*Copyright © Anthropic. All rights reserved.*
