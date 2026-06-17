# Settings

Copy page





To enable the Compliance API, see [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Settings

##### [Get effective organization settings](api/compliance/organizations/settings/retrieve.md)

GET/v1/compliance/organizations/{organization\_id}/settings

##### ModelsExpand Collapse



SettingRetrieveResponse object { organization\_id, settings, type } 

The resolved settings in force for one organization at read time.

Settings appear at most once each, in a fixed relative order, and values
reflect the enforced state. A setting the organization's administrators
cannot change — for example, one controlled by Anthropic policy or not
available to the organization — is omitted from the list.

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
is the only key. An empty object means no retention limit is in force.

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
