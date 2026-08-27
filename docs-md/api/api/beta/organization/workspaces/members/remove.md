# Delete Workspace Member

Copy page



cURL

# Delete Workspace Member

DELETE/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

Delete Workspace Member

##### Path parameters

workspace\_id: string

ID of the Workspace.

user\_id: string

ID of the User.

##### Returns



type: "workspace\_member\_deleted"

Deleted object type.

For Workspace Members, this is always `"workspace_member_deleted"`.

defaultworkspace\_member\_deleted

user\_id: string

ID of the User.

workspace\_id: string

ID of the Workspace.

### Delete Workspace Member

cURL



```shiki
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members/$USER_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```shiki
{
  "type": "workspace_member_deleted",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

##### Returns Examples

Response 200



```shiki
{
  "type": "workspace_member_deleted",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

---

*Copyright © Anthropic. All rights reserved.*
