# Workspaces

Copy page



cURL

# Workspaces

##### [Add Workspace To Service Account](api/http/beta/organization/service_accounts/workspaces/add.md)

POST/v1/organizations/service\_accounts/{service\_account\_id}/workspaces

##### [List Workspaces For Service Account](api/http/beta/organization/service_accounts/workspaces/list.md)

GET/v1/organizations/service\_accounts/{service\_account\_id}/workspaces

##### [Remove Workspace From Service Account](api/http/beta/organization/service_accounts/workspaces/remove.md)

DELETE/v1/organizations/service\_accounts/{service\_account\_id}/workspaces/{workspace\_id}

##### Models



WorkspaceRemoveResponse object{ service\_account\_id, type, workspace\_id }

service\_account\_id: string

Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.



type: "service\_account\_workspace\_member\_deleted"

defaultservice\_account\_workspace\_member\_deleted

workspace\_id: string

Tagged workspace ID (`wrkspc_...`) named in the delete request.

---

*Copyright © Anthropic. All rights reserved.*
