# Workspaces

Copy page



cURL

# Workspaces

##### [List Workspaces](api/http/beta/organization/workspaces/list.md)

GET/v1/organizations/workspaces

##### [Create Workspace](api/http/beta/organization/workspaces/create.md)

POST/v1/organizations/workspaces

##### [Get Workspace](api/http/beta/organization/workspaces/retrieve.md)

GET/v1/organizations/workspaces/{workspace\_id}

##### [Update Workspace](api/http/beta/organization/workspaces/update.md)

POST/v1/organizations/workspaces/{workspace\_id}

##### [Archive Workspace](api/http/beta/organization/workspaces/archive.md)

POST/v1/organizations/workspaces/{workspace\_id}/archive

##### Models



BetaAllowedInferenceGeo = "global" or "us"

One of the following:

"global"

"us"



BetaDataResidency object{ allowed\_inference\_geos, default\_inference\_geo, workspace\_geo }



allowed\_inference\_geos: array of string or "unrestricted"

Permitted inference geo values. 'unrestricted' means all geos are allowed.

One of the following:

Geos = array of string

Unrestricted = "unrestricted"

default\_inference\_geo: string

Default inference geo applied when requests omit the parameter.

workspace\_geo: string

Geographic region for workspace data storage. Immutable after creation.



BetaDataResidencyCreateConfig object{ allowed\_inference\_geos, default\_inference\_geo, workspace\_geo }



allowed\_inference\_geos: optional array of [BetaAllowedInferenceGeo](api/http/beta/organization/workspaces.md) or "unrestricted" or null

Permitted inference geo values. Defaults to 'unrestricted' if omitted, which allows all geos. Use the string 'unrestricted' to allow all geos, or a list of specific geos.

One of the following:



Geos = array of [BetaAllowedInferenceGeo](api/http/beta/organization/workspaces.md)

One of the following:

"global"

"us"

Unrestricted = "unrestricted"



default\_inference\_geo: optional "global" or "us" or null

Default inference geo applied when requests omit the parameter. Defaults to 'global' if omitted. Must be a member of `allowed_inference_geos` unless `allowed_inference_geos` is `"unrestricted"`.

One of the following:

"global"

"us"

workspace\_geo: optional "us" or null

Geographic region for workspace data storage. Immutable after creation. Defaults to 'us' if omitted.



BetaDataResidencyUpdateConfig object{ allowed\_inference\_geos, default\_inference\_geo }



allowed\_inference\_geos: optional array of [BetaAllowedInferenceGeo](api/http/beta/organization/workspaces.md) or "unrestricted" or null

Permitted inference geo values. Use 'unrestricted' to allow all geos, or a list of specific geos.

One of the following:



Geos = array of [BetaAllowedInferenceGeo](api/http/beta/organization/workspaces.md)

One of the following:

"global"

"us"

Unrestricted = "unrestricted"



default\_inference\_geo: optional "global" or "us" or null

Default inference geo applied when requests omit the parameter. Must be a member of `allowed_inference_geos` unless `allowed_inference_geos` is `"unrestricted"`.

One of the following:

"global"

"us"



BetaNoBillingWorkspaceRole = "workspace\_admin" or "workspace\_developer" or "workspace\_restricted\_developer" or "workspace\_user"

One of the following:

"workspace\_admin"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_user"



BetaWorkspace object{ id, archived\_at, compartment\_id, 7 more }



BetaWorkspaceMember object{ type, user\_id, workspace\_id, workspace\_role }



type: "workspace\_member"

Object type.

For Workspace Members, this is always `"workspace_member"`.

defaultworkspace\_member

user\_id: string

ID of the User.

workspace\_id: string

ID of the Workspace.



workspace\_role: [BetaWorkspaceRole](api/http/beta/organization/workspaces.md)

Role of the Workspace Member.

One of the following:

"workspace\_admin"

"workspace\_billing"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_user"



BetaWorkspaceRole = "workspace\_admin" or "workspace\_billing" or "workspace\_developer" or 2 more

One of the following:

"workspace\_admin"

"workspace\_billing"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_user"

#### Workspaces[Rate Limits](api/http/beta/organization/workspaces/rate_limits.md)

##### [List Workspace Rate Limits](api/http/beta/organization/workspaces/rate_limits/list.md)

GET/v1/organizations/workspaces/{workspace\_id}/rate\_limits

#### Workspaces[Members](api/http/beta/organization/workspaces/members.md)

##### [List Workspace Members](api/http/beta/organization/workspaces/members/list.md)

GET/v1/organizations/workspaces/{workspace\_id}/members

##### [Create Workspace Member](api/http/beta/organization/workspaces/members/add.md)

POST/v1/organizations/workspaces/{workspace\_id}/members

##### [Get Workspace Member](api/http/beta/organization/workspaces/members/retrieve.md)

GET/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

##### [Update Workspace Member](api/http/beta/organization/workspaces/members/update.md)

POST/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

##### [Delete Workspace Member](api/http/beta/organization/workspaces/members/remove.md)

DELETE/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

#### Workspaces[Service Accounts](api/http/beta/organization/workspaces/service_accounts.md)

##### [List Service Account Workspace Members](api/http/beta/organization/workspaces/service_accounts/list.md)

GET/v1/organizations/workspaces/{workspace\_id}/service\_accounts

##### [Create Service Account Workspace Member](api/http/beta/organization/workspaces/service_accounts/add.md)

POST/v1/organizations/workspaces/{workspace\_id}/service\_accounts

##### [Get Service Account Workspace Member](api/http/beta/organization/workspaces/service_accounts/retrieve.md)

GET/v1/organizations/workspaces/{workspace\_id}/service\_accounts/{service\_account\_id}

##### [Update Service Account Workspace Member](api/http/beta/organization/workspaces/service_accounts/update.md)

POST/v1/organizations/workspaces/{workspace\_id}/service\_accounts/{service\_account\_id}

##### [Delete Service Account Workspace Member](api/http/beta/organization/workspaces/service_accounts/remove.md)

DELETE/v1/organizations/workspaces/{workspace\_id}/service\_accounts/{service\_account\_id}

---

*Copyright © Anthropic. All rights reserved.*
