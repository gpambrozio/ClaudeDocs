# Service Accounts

Copy page



cURL

# Service Accounts

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

##### Models



ServiceAccountRemoveResponse object{ service\_account\_id, type, workspace\_id }

service\_account\_id: string

Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.



type: "service\_account\_workspace\_member\_deleted"

defaultservice\_account\_workspace\_member\_deleted

workspace\_id: string

Tagged workspace ID (`wrkspc_...`) named in the delete request.

---

*Copyright © Anthropic. All rights reserved.*
