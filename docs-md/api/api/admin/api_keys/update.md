# Update API Key

Copy page

# Update API Key

POST/v1/organizations/api\_keys/{api\_key\_id}

Update API Key

##### Path ParametersExpand Collapse

api\_key\_id: string

ID of the API key.

##### Body ParametersJSONExpand Collapse

name: optional string

Name of the API key.

status: optional "active" or "inactive" or "archived"

Status of the API key.

Accepts one of the following:

"active"

"inactive"

"archived"

##### ReturnsExpand Collapse

APIKey = object { id, created\_at, created\_by, 5 more }

id: string

ID of the API key.

created\_at: string

RFC 3339 datetime string indicating when the API Key was created.

created\_by: object { id, type }

The ID and type of the actor that created the API key.

id: string

ID of the actor that created the object.

type: string

Type of the actor that created the object.

name: string

Name of the API key.

partial\_key\_hint: string

Partially redacted hint for the API key.

status: "active" or "inactive" or "archived"

Status of the API key.

Accepts one of the following:

"active"

"inactive"

"archived"

type: "api\_key"

Object type.

For API Keys, this is always `"api_key"`.

workspace\_id: string

ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace.

Update API Key

```shiki
curl https://api.anthropic.com/v1/organizations/api_keys/$API_KEY_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY" \
    -d '{}'
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
