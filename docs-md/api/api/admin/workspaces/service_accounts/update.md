# Update Service Account Workspace Member

Copy page



# Update Service Account Workspace Member

POST/v1/organizations/workspaces/{workspace\_id}/service\_accounts/{service\_account\_id}

Change a service account's role in a workspace.

The new `workspace_role` replaces the current one. Only explicit
memberships can be updated; to set a role on the implicit
default-workspace membership, add the service account explicitly with
`POST /workspaces/{workspace_id}/service_accounts`. Archived workspaces
return 400. Archived service accounts cannot be updated and are
rejected. Requires an OAuth bearer or Console session; Admin API keys
are not accepted.

##### Path ParametersExpand Collapse

workspace\_id: string

ID of the workspace.

service\_account\_id: string

ID of the service account.

##### Header ParametersExpand Collapse



"anthropic-beta": optional array of string

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

##### Body ParametersJSONExpand Collapse



workspace\_role: "workspace\_admin" or "workspace\_developer" or "workspace\_restricted\_developer" or "workspace\_user"

New role for the service account in this workspace.

One of the following:

"workspace\_admin"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_user"

##### ReturnsExpand Collapse

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

Update Service Account Workspace Member



```shiki
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/service_accounts/$SERVICE_ACCOUNT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
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
