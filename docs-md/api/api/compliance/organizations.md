# Organizations

Copy page





To enable the Compliance API, see [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Organizations

##### [List organizations](api/compliance/organizations/list.md)

GET/v1/compliance/organizations

##### ModelsExpand Collapse



OrganizationListResponse object { data } 

List of organizations under a parent organization.



data: array of object { created\_at, name, uuid } 

List of organizations sorted by creation date, ascending

created\_at: string

Organization creation time (RFC 3339 format)

name: string

Organization name

uuid: string

Unique identifier for the organization (UUID format)

#### OrganizationsUsers

##### [List organization users](api/compliance/organizations/users/list.md)

GET/v1/compliance/organizations/{org\_uuid}/users

##### ModelsExpand Collapse



UserListResponse object { id, created\_at, email, 2 more } 

User member information for compliance responses.

id: string

User identifier (tagged ID)

created\_at: string

User account creation timestamp

email: string

User's current email address

full\_name: string

User's current full name



organization\_role: "admin" or "billing" or "claude\_code\_user" or 6 more

User's built-in role within the organization. This is distinct from any custom RBAC roles that may also be assigned.

One of the following:

"admin"

"billing"

"claude\_code\_user"

"developer"

"managed"

"membership\_admin"

"owner"

"primary\_owner"

"user"

#### OrganizationsRoles

##### [List Compliance Roles](api/compliance/organizations/roles/list.md)

GET/v1/compliance/organizations/{org\_uuid}/roles

##### [Get Compliance Role](api/compliance/organizations/roles/retrieve.md)

GET/v1/compliance/organizations/{org\_uuid}/roles/{role\_id}

##### ModelsExpand Collapse



RoleListResponse object { id, created\_at, description, 2 more } 

Role information for compliance responses.

id: string

Role identifier (tagged ID)

created\_at: string

Role creation timestamp (ISO 8601)

description: string

Role description

name: string

Role name

updated\_at: string

Role last-updated timestamp (ISO 8601)



RoleRetrieveResponse object { id, created\_at, description, 2 more } 

Role information for compliance responses.

id: string

Role identifier (tagged ID)

created\_at: string

Role creation timestamp (ISO 8601)

description: string

Role description

name: string

Role name

updated\_at: string

Role last-updated timestamp (ISO 8601)

#### OrganizationsRolesPermissions

##### [List Compliance Role Permissions](api/compliance/organizations/roles/permissions/list.md)

GET/v1/compliance/organizations/{org\_uuid}/roles/{role\_id}/permissions

##### ModelsExpand Collapse



PermissionListResponse object { action, resource\_id, resource\_type } 

Permission granted by a role.

action: string

Action permitted on the resource

resource\_id: string

Identifier of the resource the permission applies to

resource\_type: string

Type of resource the permission applies to

#### OrganizationsSettings

##### [Get effective organization settings](api/compliance/organizations/settings/retrieve.md)

GET/v1/compliance/organizations/{organization\_id}/settings

##### ModelsExpand Collapse



SettingRetrieveResponse object { api\_keys, organization\_id, settings, type } 

The resolved settings in force for one organization at read time.

Settings appear at most once each, in a fixed relative order, and values
reflect the enforced state. A setting the organization's administrators
cannot change — for example, one controlled by Anthropic policy or not
available to the organization — is omitted from the list.



api\_keys: array of object { id, created\_at, created\_by\_id, 4 more } 

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

type: optional "compliance\_api\_key"

organization\_id: string



settings: array of object { name, value, type }  or object { name, value, type }  or object { name, value, type }  or 2 more

One of the following:



Boolean object { name, value, type } 

A setting whose enforced value is a single true/false flag.



name: "api\_workbench\_feedback\_collection\_enabled" or "claude\_ai\_feedback\_collection\_enabled" or "claude\_code\_trusted\_devices\_required" or 9 more

One of the following:

"api\_workbench\_feedback\_collection\_enabled"

"claude\_ai\_feedback\_collection\_enabled"

"claude\_code\_trusted\_devices\_required"

"code\_execution\_enabled"

"code\_execution\_network\_egress\_enabled"

"content\_redaction\_enabled"

"directory\_sync\_enabled"

"frontier\_data\_use\_enabled"

"ip\_allowlist\_enabled"

"sso\_claude\_ai\_enforced"

"sso\_console\_enforced"

"sso\_enabled"

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

StringList object { name, value, type } 

A setting whose enforced value is a list of strings.



name: "allowed\_invite\_domains" or "ip\_allowlist\_ip\_ranges"

One of the following:

"allowed\_invite\_domains"

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

---

*Copyright © Anthropic. All rights reserved.*
