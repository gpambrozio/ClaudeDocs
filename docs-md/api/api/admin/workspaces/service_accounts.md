# Service Accounts

Copy page



# Service Accounts

##### [Create Service Account Workspace Member](api/admin/workspaces/service_accounts/create.md)

POST/v1/organizations/workspaces/{workspace\_id}/service\_accounts

##### [Get Service Account Workspace Member](api/admin/workspaces/service_accounts/retrieve.md)

GET/v1/organizations/workspaces/{workspace\_id}/service\_accounts/{service\_account\_id}

##### [List Service Account Workspace Members](api/admin/workspaces/service_accounts/list.md)

GET/v1/organizations/workspaces/{workspace\_id}/service\_accounts

##### [Update Service Account Workspace Member](api/admin/workspaces/service_accounts/update.md)

POST/v1/organizations/workspaces/{workspace\_id}/service\_accounts/{service\_account\_id}

##### [Delete Service Account Workspace Member](api/admin/workspaces/service_accounts/delete.md)

DELETE/v1/organizations/workspaces/{workspace\_id}/service\_accounts/{service\_account\_id}

##### ModelsExpand Collapse



ServiceAccountCreateResponse object { created\_by\_actor\_id, implicit, service\_account\_id, 3 more } 

created\_by\_actor\_id: string

Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

implicit: boolean

True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace\_user and cannot be removed.

service\_account\_id: string

Tagged service account ID (`svac_...`).

type: "service\_account\_workspace\_member"

workspace\_id: string

Tagged workspace ID (`wrkspc_...`).



workspace\_role: "workspace\_user" or "workspace\_developer" or "workspace\_restricted\_developer" or 2 more

Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

One of the following:

"workspace\_user"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_admin"

"workspace\_billing"



ServiceAccountRetrieveResponse object { created\_by\_actor\_id, implicit, service\_account\_id, 3 more } 

created\_by\_actor\_id: string

Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

implicit: boolean

True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace\_user and cannot be removed.

service\_account\_id: string

Tagged service account ID (`svac_...`).

type: "service\_account\_workspace\_member"

workspace\_id: string

Tagged workspace ID (`wrkspc_...`).



workspace\_role: "workspace\_user" or "workspace\_developer" or "workspace\_restricted\_developer" or 2 more

Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

One of the following:

"workspace\_user"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_admin"

"workspace\_billing"



ServiceAccountListResponse object { created\_by\_actor\_id, implicit, service\_account\_id, 3 more } 

created\_by\_actor\_id: string

Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

implicit: boolean

True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace\_user and cannot be removed.

service\_account\_id: string

Tagged service account ID (`svac_...`).

type: "service\_account\_workspace\_member"

workspace\_id: string

Tagged workspace ID (`wrkspc_...`).



workspace\_role: "workspace\_user" or "workspace\_developer" or "workspace\_restricted\_developer" or 2 more

Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

One of the following:

"workspace\_user"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_admin"

"workspace\_billing"



ServiceAccountUpdateResponse object { created\_by\_actor\_id, implicit, service\_account\_id, 3 more } 

created\_by\_actor\_id: string

Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

implicit: boolean

True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace\_user and cannot be removed.

service\_account\_id: string

Tagged service account ID (`svac_...`).

type: "service\_account\_workspace\_member"

workspace\_id: string

Tagged workspace ID (`wrkspc_...`).



workspace\_role: "workspace\_user" or "workspace\_developer" or "workspace\_restricted\_developer" or 2 more

Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

One of the following:

"workspace\_user"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_admin"

"workspace\_billing"



ServiceAccountDeleteResponse object { service\_account\_id, type, workspace\_id } 

service\_account\_id: string

Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

type: "service\_account\_workspace\_member\_deleted"

workspace\_id: string

Tagged workspace ID (`wrkspc_...`) named in the delete request.

---

*Copyright © Anthropic. All rights reserved.*
