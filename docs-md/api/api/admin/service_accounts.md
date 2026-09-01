# Service Accounts

Copy page



# Service Accounts

##### [Create Service Account](api/http/admin/service_accounts/create.md)

POST/v1/organizations/service\_accounts

##### [Get Service Account](api/http/admin/service_accounts/retrieve.md)

GET/v1/organizations/service\_accounts/{service\_account\_id}

##### [List Service Accounts](api/http/admin/service_accounts/list.md)

GET/v1/organizations/service\_accounts

##### [Update Service Account](api/http/admin/service_accounts/update.md)

POST/v1/organizations/service\_accounts/{service\_account\_id}

##### [Archive Service Account](api/http/admin/service_accounts/archive.md)

POST/v1/organizations/service\_accounts/{service\_account\_id}/archive

##### Models



ServiceAccount object{ id, archived\_at, archived\_by\_actor\_id, 8 more }

Named non-human identity within the caller's organization.

A service account is a pure identity: name + org. Authorization lives on
whatever references it (federation rules).

#### Service Accounts[Workspaces](api/http/admin/service_accounts/workspaces.md)

##### [Add Workspace To Service Account](api/http/admin/service_accounts/workspaces/create.md)

POST/v1/organizations/service\_accounts/{service\_account\_id}/workspaces

##### [List Workspaces For Service Account](api/http/admin/service_accounts/workspaces/list.md)

GET/v1/organizations/service\_accounts/{service\_account\_id}/workspaces

##### [Remove Workspace From Service Account](api/http/admin/service_accounts/workspaces/delete.md)

DELETE/v1/organizations/service\_accounts/{service\_account\_id}/workspaces/{workspace\_id}

---

*Copyright © Anthropic. All rights reserved.*
