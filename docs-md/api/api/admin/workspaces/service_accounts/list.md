# List Service Account Workspace Members

Copy page



# List Service Account Workspace Members

GET/v1/organizations/workspaces/{workspace\_id}/service\_accounts

List the service accounts that are members of a workspace.

Each entry includes the service account's `workspace_role`. Use `limit`
and the `next_page` cursor to paginate. Archived workspaces return 400;
use `GET /service_accounts/{id}/workspaces` to audit memberships of an
archived workspace. The implicit default-workspace membership is not
included in this list. Memberships of archived service accounts are
omitted from the results.

##### Path parameters

workspace\_id: string

ID of the workspace.

##### Query parameters



limit: optional number

Number of results per page.

default20

maximum100

minimum1

page: optional string

Opaque cursor from a previous response's `next_page`.

##### Headers



"anthropic-beta": optional array of string

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

##### Returns



data: array of object{ created\_by\_actor\_id, implicit, service\_account\_id, 3 more }

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

workspace\_role: "workspace\_admin" or "workspace\_billing" or "workspace\_developer" or 2 more

Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

One of the following:

"workspace\_admin"

"workspace\_billing"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_user"

next\_page: string or null

Opaque cursor for the next page, or null if no more results.



### List Service Account Workspace Members

cURL



```shiki
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/service_accounts \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "data": [
    {
      "created_by_actor_id": "created_by_actor_id",
      "implicit": true,
      "service_account_id": "service_account_id",
      "type": "service_account_workspace_member",
      "workspace_id": "workspace_id",
      "workspace_role": "workspace_admin"
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "created_by_actor_id": "created_by_actor_id",
      "implicit": true,
      "service_account_id": "service_account_id",
      "type": "service_account_workspace_member",
      "workspace_id": "workspace_id",
      "workspace_role": "workspace_admin"
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
