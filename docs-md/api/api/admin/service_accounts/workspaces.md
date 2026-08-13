# Workspaces

Copy page



# Workspaces

##### [Add Workspace To Service Account](api/admin/service_accounts/workspaces/create.md)

POST/v1/organizations/service\_accounts/{service\_account\_id}/workspaces

##### [List Workspaces For Service Account](api/admin/service_accounts/workspaces/list.md)

GET/v1/organizations/service\_accounts/{service\_account\_id}/workspaces

##### [Remove Workspace From Service Account](api/admin/service_accounts/workspaces/delete.md)

DELETE/v1/organizations/service\_accounts/{service\_account\_id}/workspaces/{workspace\_id}

##### ModelsExpand Collapse



WorkspaceCreateResponse object { created\_by\_actor\_id, implicit, service\_account\_id, 3 more } 

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

workspace\_role: "workspace\_admin" or "workspace\_billing" or "workspace\_developer" or 2 more

Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

One of the following:

"workspace\_admin"

"workspace\_billing"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_user"



WorkspaceListResponse object { created\_by\_actor\_id, implicit, service\_account\_id, 3 more } 

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

workspace\_role: "workspace\_admin" or "workspace\_billing" or "workspace\_developer" or 2 more

Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

One of the following:

"workspace\_admin"

"workspace\_billing"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_user"



WorkspaceDeleteResponse object { service\_account\_id, type, workspace\_id } 

service\_account\_id: string

Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

type: "service\_account\_workspace\_member\_deleted"

workspace\_id: string

Tagged workspace ID (`wrkspc_...`) named in the delete request.

---

*Copyright © Anthropic. All rights reserved.*
