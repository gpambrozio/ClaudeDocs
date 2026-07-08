# Get effective organization settings

Copy page





To enable the Compliance API, see [Set up the Compliance API](manage-claude/compliance-api-access.md).

# Get effective organization settings

GET/v1/compliance/organizations/{organization\_id}/settings

Retrieve the effective settings for an organization.

Returns the settings currently in force for the given organization — the
enforced state after all policies are applied, which may differ from what
is configured in the admin console. Settings an organization's
administrators cannot change (for example, ones controlled by Anthropic
policy or not available to the organization) are omitted from the list.

The organization must belong to the API key's organization hierarchy;
unknown organizations and organizations outside the hierarchy return 404.

##### Path ParametersExpand Collapse

organization\_id: string

The organization's UUID

##### Header ParametersExpand Collapse

"x-api-key": optional string

##### ReturnsExpand Collapse



api\_keys: array of object { id, created\_at, created\_by\_id, 5 more } 

Compliance API keys configured for the organization hierarchy, ordered by creation time ascending. Key secret values are never included.

id: string

Unique identifier for the API key.

created\_at: string

When the key was created.

created\_by\_id: string

Identifier of the user who created the key, or null when the key was created by automation or its creator's account no longer exists.

is\_active: boolean

Whether the key is currently active. A deactivated key is listed for audit visibility but cannot authenticate requests.

name: string

The name given to the API key when it was created.

scopes: array of string

The permission scopes granted to the key.

expires\_at: optional string

When the key will stop authenticating, or null when the key does not expire.

type: optional "compliance\_api\_key"

organization\_id: string



settings: array of object { name, value, type }  or object { name, value, type }  or object { name, value, type }  or 3 more

One of the following:



Boolean object { name, value, type } 

A setting whose enforced value is a single true/false flag.



name: "ai\_powered\_artifacts\_enabled" or "api\_workbench\_feedback\_collection\_enabled" or "artifact\_connectors\_enabled" or 43 more

One of the following:

"ai\_powered\_artifacts\_enabled"

"api\_workbench\_feedback\_collection\_enabled"

"artifact\_connectors\_enabled"

"ask\_your\_org\_enabled"

"chat\_enabled"

"claude\_ai\_chat\_sharing\_enabled"

"claude\_ai\_feedback\_collection\_enabled"

"claude\_ai\_integration\_sharing\_enabled"

"claude\_code\_desktop\_auto\_permissions\_enabled"

"claude\_code\_desktop\_bypass\_permissions\_enabled"

"claude\_code\_desktop\_enabled"

"claude\_code\_fast\_mode\_enabled"

"claude\_code\_metrics\_logging\_enabled"

"claude\_code\_remote\_control\_enabled"

"claude\_code\_review\_enabled"

"claude\_code\_routines\_enabled"

"claude\_code\_security\_enabled"

"claude\_code\_trusted\_devices\_required"

"claude\_code\_web\_enabled"

"claude\_code\_workflows\_enabled"

"claude\_design\_enabled"

"claude\_in\_slack\_enabled"

"code\_execution\_enabled"

"code\_execution\_network\_egress\_enabled"

"connector\_tools\_default\_always\_allow"

"content\_redaction\_enabled"

"desktop\_extension\_allowlist\_enabled"

"directory\_sync\_enabled"

"frontier\_data\_use\_enabled"

"hipaa\_compliance\_enabled"

"inline\_visualizations\_enabled"

"ip\_allowlist\_enabled"

"location\_metadata\_enabled"

"member\_usage\_dashboard\_visible"

"memory\_enabled"

"org\_wide\_skill\_sharing\_enabled"

"public\_projects\_enabled"

"skill\_sharing\_enabled"

"skills\_enabled"

"sso\_claude\_ai\_enforced"

"sso\_console\_enforced"

"sso\_enabled"

"third\_party\_interactive\_content\_enabled"

"user\_skill\_creation\_enabled"

"web\_search\_enabled"

"work\_across\_apps\_enabled"

value: boolean

type: optional "boolean"



Integer object { name, value, type } 

A setting whose enforced value is a whole number; null means no limit
is in force.

name: "account\_session\_duration\_seconds"

value: number

type: optional "integer"



String object { name, value, type } 

A setting whose enforced value is a single string; null means no value
is configured.



name: "claude\_code\_default\_worker\_environment\_id" or "claude\_code\_default\_worker\_pool\_id"

One of the following:

"claude\_code\_default\_worker\_environment\_id"

"claude\_code\_default\_worker\_pool\_id"

value: string

type: optional "string"



StringList object { name, value, type } 

A setting whose enforced value is a list of strings.



name: "allowed\_invite\_domains" or "disabled\_admin\_request\_types" or "ip\_allowlist\_ip\_ranges"

One of the following:

"allowed\_invite\_domains"

"disabled\_admin\_request\_types"

"ip\_allowlist\_ip\_ranges"

value: array of string

type: optional "string\_list"



ProvisioningMode object { value, name, type } 

How organization members are provisioned, resolved to the enforced mode.

A configured mode is reported only while the mechanism that enforces it is
active: just-in-time modes require single sign-on to be enabled, and SCIM
modes require directory sync to be enabled. Otherwise `login_only` is
reported, regardless of any stored configuration.



value: "jit\_advanced" or "jit\_permissive" or "login\_only" or 2 more

How organization members are provisioned under SSO.

One of the following:

"jit\_advanced"

"jit\_permissive"

"login\_only"

"scim\_advanced"

"scim\_permissive"

name: optional "sso\_provisioning\_mode"

type: optional "provisioning\_mode"



DataRetention object { value, name, type } 

The data retention periods in force, keyed by the type of data they
apply to.

A key of `all` covers every data type and is exclusive: when present it
is the only key. A missing key means no organization-level
administrator-configured retention period is in force for that data type;
Anthropic's service defaults may still apply.



value: map[object { duration, timescale, type }  or object { type } ]

One of the following:



Fixed object { duration, timescale, type } 

A fixed retention window measured from each item's last activity.

duration: number



timescale: "day" or "month"

One of the following:

"day"

"month"

type: optional "fixed"



Indefinite object { type } 

An indefinite retention period: data is kept with no time limit.

type: optional "indefinite"

name: optional "data\_retention\_periods"

type: optional "data\_retention"

type: optional "effective\_organization\_settings"

Get effective organization settings



```shiki
curl https://api.anthropic.com/v1/compliance/organizations/$ORGANIZATION_ID/settings \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```shiki
{
  "api_keys": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "created_by_id": "created_by_id",
      "is_active": true,
      "name": "name",
      "scopes": [
        "string"
      ],
      "expires_at": "2019-12-27T18:11:19.117Z",
      "type": "compliance_api_key"
    }
  ],
  "organization_id": "organization_id",
  "settings": [
    {
      "name": "ai_powered_artifacts_enabled",
      "value": true,
      "type": "boolean"
    }
  ],
  "type": "effective_organization_settings"
}
```

##### Returns Examples

Response 200



```shiki
{
  "api_keys": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "created_by_id": "created_by_id",
      "is_active": true,
      "name": "name",
      "scopes": [
        "string"
      ],
      "expires_at": "2019-12-27T18:11:19.117Z",
      "type": "compliance_api_key"
    }
  ],
  "organization_id": "organization_id",
  "settings": [
    {
      "name": "ai_powered_artifacts_enabled",
      "value": true,
      "type": "boolean"
    }
  ],
  "type": "effective_organization_settings"
}
```

---

*Copyright © Anthropic. All rights reserved.*
