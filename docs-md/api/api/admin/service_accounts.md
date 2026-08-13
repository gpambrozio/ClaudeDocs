# Service Accounts

Copy page



# Service Accounts

##### [Create Service Account](api/admin/service_accounts/create.md)

POST/v1/organizations/service\_accounts

##### [Get Service Account](api/admin/service_accounts/retrieve.md)

GET/v1/organizations/service\_accounts/{service\_account\_id}

##### [List Service Accounts](api/admin/service_accounts/list.md)

GET/v1/organizations/service\_accounts

##### [Update Service Account](api/admin/service_accounts/update.md)

POST/v1/organizations/service\_accounts/{service\_account\_id}

##### [Archive Service Account](api/admin/service_accounts/archive.md)

POST/v1/organizations/service\_accounts/{service\_account\_id}/archive

##### ModelsExpand Collapse



ServiceAccount object { id, archived\_at, archived\_by\_actor\_id, 8 more } 

Named non-human identity within the caller's organization.

A service account is a pure identity: name + org. Authorization lives on
whatever references it (federation rules).

id: string

Tagged ID of the service account.

archived\_at: string

If set, this service account is archived.

archived\_by\_actor\_id: string

Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

created\_at: string

When this service account was created.

created\_by\_actor\_id: string

Tagged ID (`user_`/`svac_`) of the actor that created this service account.

description: string

Optional free-text description.

name: string

Admin-chosen slug identifier.



organization\_role: "admin" or "developer"

Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

One of the following:

"admin"

"developer"

type: "service\_account"

updated\_at: string

When this service account was last updated.

updated\_by\_actor\_id: string

Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Service AccountsWorkspaces

##### [Add Workspace To Service Account](api/admin/service_accounts/workspaces/create.md)

POST/v1/organizations/service\_accounts/{service\_account\_id}/workspaces

##### [List Workspaces For Service Account](api/admin/service_accounts/workspaces/list.md)

GET/v1/organizations/service\_accounts/{service\_account\_id}/workspaces

##### [Remove Workspace From Service Account](api/admin/service_accounts/workspaces/delete.md)

DELETE/v1/organizations/service\_accounts/{service\_account\_id}/workspaces/{workspace\_id}

---

*Copyright © Anthropic. All rights reserved.*
