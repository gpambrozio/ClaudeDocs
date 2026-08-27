# List Workspace Members

Copy page



cURL

# List Workspace Members

GET/v1/organizations/workspaces/{workspace\_id}/members

List Workspace Members

##### Path parameters

workspace\_id: string

ID of the Workspace.

##### Query parameters

after\_id: optional string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

before\_id: optional string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.



limit: optional number

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

default20

maximum1000

minimum1

##### Returns



data: array of [BetaWorkspaceMember](api/http/beta/organization/workspaces.md) { type, user\_id, workspace\_id, workspace\_role }

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

first\_id: string or null

First ID in the `data` list. Can be used as the `before_id` for the previous page.

has\_more: boolean

Indicates if there are more results in the requested page direction.

last\_id: string or null

Last ID in the `data` list. Can be used as the `after_id` for the next page.

### List Workspace Members

cURL



```shiki
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```shiki
{
  "data": [
    {
      "type": "workspace_member",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      "workspace_role": "workspace_admin"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "type": "workspace_member",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      "workspace_role": "workspace_admin"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

---

*Copyright © Anthropic. All rights reserved.*
