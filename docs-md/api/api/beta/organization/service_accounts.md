# Service Accounts

Copy page



cURL

# Service Accounts

##### [Create Service Account](api/http/beta/organization/service_accounts/create.md)

POST/v1/organizations/service\_accounts

##### [List Service Accounts](api/http/beta/organization/service_accounts/list.md)

GET/v1/organizations/service\_accounts

##### [Get Service Account](api/http/beta/organization/service_accounts/retrieve.md)

GET/v1/organizations/service\_accounts/{service\_account\_id}

##### [Update Service Account](api/http/beta/organization/service_accounts/update.md)

POST/v1/organizations/service\_accounts/{service\_account\_id}

##### [Archive Service Account](api/http/beta/organization/service_accounts/archive.md)

POST/v1/organizations/service\_accounts/{service\_account\_id}/archive

##### Models



BetaServiceAccount object{ id, archived\_at, archived\_by\_actor\_id, 8 more }

Named non-human identity within the caller's organization.

A service account is a pure identity: name + org. Authorization lives on
whatever references it (federation rules).



BetaServiceAccountWorkspaceMember object{ created\_by\_actor\_id, implicit, service\_account\_id, 3 more }

created\_by\_actor\_id: string or null

Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

implicit: boolean or null

True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

service\_account\_id: string

Tagged service account ID (`svac_...`).



type: "service\_account\_workspace\_member"

defaultservice\_account\_workspace\_member

workspace\_id: string

Tagged workspace ID (`wrkspc_...`).



workspace\_role: [BetaWorkspaceRole](api/http/beta/organization/workspaces.md)

Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

One of the following:

"workspace\_admin"

"workspace\_billing"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_user"

#### Service Accounts[Workspaces](api/http/beta/organization/service_accounts/workspaces.md)

##### [Add Workspace To Service Account](api/http/beta/organization/service_accounts/workspaces/add.md)

POST/v1/organizations/service\_accounts/{service\_account\_id}/workspaces

##### [List Workspaces For Service Account](api/http/beta/organization/service_accounts/workspaces/list.md)

GET/v1/organizations/service\_accounts/{service\_account\_id}/workspaces

##### [Remove Workspace From Service Account](api/http/beta/organization/service_accounts/workspaces/remove.md)

DELETE/v1/organizations/service\_accounts/{service\_account\_id}/workspaces/{workspace\_id}

---

*Copyright © Anthropic. All rights reserved.*
