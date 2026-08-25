# List Service Accounts

Copy page



# List Service Accounts

GET/v1/organizations/service\_accounts

List service accounts in the caller's organization.

Results are ordered by creation time, newest first. Use `limit` and the
`next_page` cursor to paginate; set `include_archived=true` to include
archived service accounts.

##### Query parameters



include\_archived: optional boolean

Include archived resources. Defaults to false.

defaultfalse

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

data: array of [ServiceAccount](api/http/admin/service_accounts.md) { id, archived\_at, archived\_by\_actor\_id, 8 more }

id: string

Tagged ID of the service account.



archived\_at: string or null

If set, this service account is archived.

formatdate-time

archived\_by\_actor\_id: string or null

Tagged ID (`user_`/`svac_`) of the actor that archived this service account.



created\_at: string

When this service account was created.

formatdate-time

created\_by\_actor\_id: string or null

Tagged ID (`user_`/`svac_`) of the actor that created this service account.

description: string or null

Optional free-text description.

name: string

Admin-chosen slug identifier.



organization\_role: "admin" or "developer"

Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

One of the following:

"admin"

"developer"



type: "service\_account"

defaultservice\_account



updated\_at: string

When this service account was last updated.

formatdate-time

updated\_by\_actor\_id: string or null

Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

next\_page: string or null

Opaque cursor for the next page, or null if no more results.

### List Service Accounts

cURL



```shiki
curl https://api.anthropic.com/v1/organizations/service_accounts \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "data": [
    {
      "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "description": "description",
      "name": "ci-deploy-bot",
      "organization_role": "admin",
      "type": "service_account",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id"
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
      "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "description": "description",
      "name": "ci-deploy-bot",
      "organization_role": "admin",
      "type": "service_account",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id"
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
