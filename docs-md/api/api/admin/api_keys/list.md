# List API Keys

Copy page



# List API Keys

GET/v1/organizations/api\_keys

List API Keys

##### Query parameters

after\_id: optional string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

before\_id: optional string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

created\_by\_user\_id: optional string

Filter by the ID of the User who created the object.



limit: optional number

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

default20

maximum1000

minimum1



status: optional "active" or "archived" or "expired" or "inactive"

Filter by API key status.

One of the following:

"active"

"archived"

"expired"

"inactive"

workspace\_id: optional string

Filter by Workspace ID.

##### Returns



data: array of [APIKey](api/http/$shared.md) { id, created\_at, created\_by, 8 more }

id: string

ID of the API key.



created\_at: string

RFC 3339 datetime string indicating when the API Key was created.

formatdate-time



created\_by: object{ id, type } or null

The ID and type of the actor that created the API key, or `null` when the
creator is not recorded (legacy, workload-identity-federated, or
system-created keys).

id: string

ID of the actor that created the object.



type: "service\_account" or "user"

Type of the actor that created the object.

One of the following:

"service\_account"

"user"



expires\_at: string or null

RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

formatdate-time

name: string

Name of the API key.

partial\_key\_hint: string or null

Partially redacted hint for the API key.



principal: object{ type, user\_id } or object{ service\_account\_id, type } or null

The principal the API key acts as (a User or a Service Account), or `null` if the API key is not bound to a principal.

One of the following:



UserActor object{ type, user\_id }



type: "user\_actor"

Principal type. Always `"user_actor"` for a User.

defaultuser\_actor

user\_id: string

ID of the User the API key acts as.



ServiceAccountActor object{ service\_account\_id, type }

service\_account\_id: string

ID of the Service Account the API key acts as.



type: "service\_account\_actor"

Principal type. Always `"service_account_actor"` for a Service Account.

defaultservice\_account\_actor



scope: object{ type } or object{ type, workspace\_id }

Where the API key belongs: its Workspace (`{"type": "workspace", "workspace_id": "wrkspc_..."}`, with the Workspace's real ID even when it is the organization's default Workspace), or the organization (`{"type": "organization"}`) for a principal-bound API key that has no Workspace.

One of the following:



Organization object{ type }



type: "organization"

Scope type. Always `"organization"`: the API key has no Workspace. Only a principal-bound API key can have this scope.

defaultorganization



Workspace object{ type, workspace\_id }



type: "workspace"

Scope type. Always `"workspace"`: the API key belongs to one Workspace.

defaultworkspace

workspace\_id: string

ID of the Workspace the API key belongs to. Unlike the deprecated top-level `workspace_id`, this is the Workspace's real ID even for the organization's default Workspace.



status: "active" or "archived" or "expired" or "inactive"

Status of the API key.

One of the following:

"active"

"archived"

"expired"

"inactive"



type: "api\_key"

Object type.

For API Keys, this is always `"api_key"`.

defaultapi\_key



workspace\_id: string or null⁠Deprecated

Deprecated: use `scope` instead. ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace. Also `null` for a principal-bound API key that has no Workspace; `scope` tells the two apart.

Use `scope` instead. `workspace\_id` is `null` both for an API key in the default Workspace and for a principal-bound API key that has no Workspace.

first\_id: string or null

First ID in the `data` list. Can be used as the `before_id` for the previous page.

has\_more: boolean

Indicates if there are more results in the requested page direction.

last\_id: string or null

Last ID in the `data` list. Can be used as the `after_id` for the next page.

List API Keys

cURL

```shiki
curl https://api.anthropic.com/v1/organizations/api_keys \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN"
```

Response 200



```shiki
{
  "data": [
    {
      "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by": {
        "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
        "type": "user"
      },
      "expires_at": "2024-10-30T23:58:27.427722Z",
      "name": "Developer Key",
      "partial_key_hint": "sk-ant-api03-R2D...igAA",
      "principal": {
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "scope": {
        "type": "workspace",
        "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
      },
      "status": "active",
      "type": "api_key",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
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
      "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by": {
        "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
        "type": "user"
      },
      "expires_at": "2024-10-30T23:58:27.427722Z",
      "name": "Developer Key",
      "partial_key_hint": "sk-ant-api03-R2D...igAA",
      "principal": {
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "scope": {
        "type": "workspace",
        "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
      },
      "status": "active",
      "type": "api_key",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

---

*Copyright © Anthropic. All rights reserved.*
