# Update API Key

Copy page



# Update API Key

POST/v1/organizations/api\_keys/{api\_key\_id}

Update API Key

##### Path ParametersExpand Collapse

api\_key\_id: string

ID of the API key.

##### Body ParametersJSONExpand Collapse

name: optional string

Name of the API key.



status: optional "active" or "archived" or "inactive"

Status of the API key.

One of the following:

"active"

"archived"

"inactive"

##### ReturnsExpand Collapse



APIKey object { id, created\_at, created\_by, 7 more } 

id: string

ID of the API key.

created\_at: string

RFC 3339 datetime string indicating when the API Key was created.



created\_by: object { id, type } 

The ID and type of the actor that created the API key.

id: string

ID of the actor that created the object.

type: string

Type of the actor that created the object.

expires\_at: string

RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

name: string

Name of the API key.

partial\_key\_hint: string

Partially redacted hint for the API key.



principal: object { id, type } 

The ID and type of the principal the API key acts as, or `null` if the key is not bound to a principal.

id: string

ID of the principal the API key acts as: a User ID (`user_...`) when the type is `user`, or a Service Account ID (`svac_...`) when the type is `service_account`.



type: "service\_account" or "user"

Type of the principal the API key acts as.

One of the following:

"service\_account"

"user"

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

workspace\_id: string

ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace.

Update API Key



```shiki
curl https://api.anthropic.com/v1/organizations/api_keys/$API_KEY_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{}'
```

Response 200



```shiki
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
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "type": "user"
  },
  "status": "active",
  "type": "api_key",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

##### Returns Examples

Response 200



```shiki
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
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "type": "user"
  },
  "status": "active",
  "type": "api_key",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

---

*Copyright © Anthropic. All rights reserved.*
