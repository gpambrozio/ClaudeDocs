# Add Workspace To Service Account

Copy page



# Add Workspace To Service Account

POST/v1/organizations/service\_accounts/{service\_account\_id}/workspaces

Add a service account to a workspace with the given `workspace_role`.

Mirror of `POST /workspaces/{workspace_id}/service_accounts`, addressed
from the service-account side; both create the same membership. If the
service account is already an explicit member of the workspace, its
`workspace_role` is replaced with the value supplied here. Archived
workspaces return 400. Archived service accounts cannot be added and are
rejected. Requires an OAuth bearer or Console session; Admin API keys
are not accepted.

##### Path parameters

service\_account\_id: string

ID of the service account.

##### Headers



"anthropic-beta": optional array of string

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

##### Body

workspace\_id: string

Tagged workspace ID to add the service account to.



workspace\_role: "workspace\_admin" or "workspace\_developer" or "workspace\_restricted\_developer" or "workspace\_user"

Role to assign to the service account in this workspace.

One of the following:

"workspace\_admin"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_user"

##### Returns

created\_by\_actor\_id: string or null

Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

implicit: boolean or null

True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

service\_account\_id: string

Tagged service account ID (`svac_...`).



type: "service\_account\_workspace\_member"

defaultservice\_account\_workspace\_member

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

Add Workspace To Service Account

cURL

```shiki
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID/workspaces \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "workspace_id": "workspace_id",
          "workspace_role": "workspace_admin"
        }'
```

Response 200



```shiki
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
}
```

##### Returns Examples

Response 200



```shiki
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
}
```

---

*Copyright © Anthropic. All rights reserved.*
