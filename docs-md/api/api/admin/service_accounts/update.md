# Update Service Account

Copy page



# Update Service Account

POST/v1/organizations/service\_accounts/{service\_account\_id}

Update a service account.

Only `description` and `organization_role` are mutable; `name` cannot be
changed. Archived service accounts cannot be updated; this returns 400.
Setting `organization_role` to `admin` (even when unchanged) requires an
interactive credential (a user OAuth token or a Console session). Admin
API keys are not accepted.

##### Path ParametersExpand Collapse

service\_account\_id: string

ID of the service account to update.

##### Header ParametersExpand Collapse



"anthropic-beta": optional array of string

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

##### Body ParametersJSONExpand Collapse

description: optional string

Replaces the description. Omit to leave unchanged; send `null` to clear (the field is stored as an empty string).



organization\_role: optional "admin" or "developer"

Replaces the org-level role. Omit or send `null` to leave unchanged.

One of the following:

"admin"

"developer"

##### ReturnsExpand Collapse

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

Update Service Account



```shiki
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{}'
```

Response 200



```shiki
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
```

##### Returns Examples

Response 200



```shiki
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
```

---

*Copyright © Anthropic. All rights reserved.*
