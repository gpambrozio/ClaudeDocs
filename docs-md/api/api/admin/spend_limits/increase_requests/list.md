# List Spend Limit Increase Requests

Copy page



# List Spend Limit Increase Requests

GET/v1/organizations/spend\_limit\_increase\_requests

List spend limit increase requests, most recent first.

Pending requests include a live `spend_summary` for the requester.
Requests whose requester is no longer a member are excluded.

##### Query ParametersExpand Collapse

actor\_ids: optional array of string

Filter by requester, as `user_...` tagged IDs.

limit: optional number

page: optional string

Opaque cursor from a previous response's `next_page`.



status: optional array of "pending" or "approved" or "denied"

Filter by status. Omit to return all.

One of the following:

"pending"

"approved"

"denied"

##### ReturnsExpand Collapse



data: array of [SpendLimitIncreaseRequest](api/admin/spend_limits/increase_requests.md) { id, actor, created\_at, 6 more } 

id: string



actor: object { deleted, email\_address, name, 2 more } 

A user within the organization. `name` and `email_address` are
null when the underlying account is unavailable or has been deleted;
`deleted` is true only for deleted accounts.

deleted: boolean

email\_address: string

name: string

type: "user\_actor"

user\_id: string

created\_at: string



period: "monthly" or "daily" or "weekly"

One of the following:

"monthly"

"daily"

"weekly"

resolved\_at: string



resolved\_by: object { deleted, email\_address, name, 2 more }  or object { scoped\_api\_key\_id, type } 

A user within the organization. `name` and `email_address` are
null when the underlying account is unavailable or has been deleted;
`deleted` is true only for deleted accounts.

One of the following:



UserActor object { deleted, email\_address, name, 2 more } 

A user within the organization. `name` and `email_address` are
null when the underlying account is unavailable or has been deleted;
`deleted` is true only for deleted accounts.

deleted: boolean

email\_address: string

name: string

type: "user\_actor"

user\_id: string



ScopedAPIKeyActor object { scoped\_api\_key\_id, type } 

A scoped Admin API key acting on behalf of the organization.

scoped\_api\_key\_id: string

type: "scoped\_api\_key\_actor"



spend\_summary: [SpendSummary](api/admin/spend_limits.md) { actor, amount, currency, 5 more } 

Per-member effective-limit report row (GET /spend\_limits/effective).



actor: object { deleted, email\_address, name, 2 more } 

A user within the organization. `name` and `email_address` are
null when the underlying account is unavailable or has been deleted;
`deleted` is true only for deleted accounts.

deleted: boolean

email\_address: string

name: string

type: "user\_actor"

user\_id: string

amount: string

currency: string



period: "monthly" or "daily" or "weekly"

One of the following:

"monthly"

"daily"

"weekly"

period\_to\_date\_spend: string



scope: object { type, user\_id } 

type: "user"

user\_id: string



source: object { type, user\_id }  or object { seat\_tier, type }  or object { rbac\_group\_id, type }  or 2 more

One of the following:



User object { type, user\_id } 

type: "user"

user\_id: string



SeatTier object { seat\_tier, type } 

seat\_tier: string

type: "seat\_tier"



RbacGroup object { rbac\_group\_id, type } 

rbac\_group\_id: string

type: "rbac\_group"



OrganizationService object { service, type } 

service: string

type: "organization\_service"



Organization object { type } 

type: "organization"

spend\_limit\_id: string



status: "pending" or "approved" or "denied"

One of the following:

"pending"

"approved"

"denied"

type: "spend\_limit\_increase\_request"

next\_page: string

List Spend Limit Increase Requests



```shiki
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "data": [
    {
      "id": "id",
      "actor": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_id"
      },
      "created_at": "2019-12-27T18:11:19.117Z",
      "period": "monthly",
      "resolved_at": "2019-12-27T18:11:19.117Z",
      "resolved_by": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_id"
      },
      "spend_summary": {
        "actor": {
          "deleted": true,
          "email_address": "email_address",
          "name": "name",
          "type": "user_actor",
          "user_id": "user_id"
        },
        "amount": "50000",
        "currency": "USD",
        "period": "monthly",
        "period_to_date_spend": "period_to_date_spend",
        "scope": {
          "type": "user",
          "user_id": "user_id"
        },
        "source": {
          "type": "user",
          "user_id": "user_id"
        },
        "spend_limit_id": "spend_limit_id"
      },
      "status": "pending",
      "type": "spend_limit_increase_request"
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
      "id": "id",
      "actor": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_id"
      },
      "created_at": "2019-12-27T18:11:19.117Z",
      "period": "monthly",
      "resolved_at": "2019-12-27T18:11:19.117Z",
      "resolved_by": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_id"
      },
      "spend_summary": {
        "actor": {
          "deleted": true,
          "email_address": "email_address",
          "name": "name",
          "type": "user_actor",
          "user_id": "user_id"
        },
        "amount": "50000",
        "currency": "USD",
        "period": "monthly",
        "period_to_date_spend": "period_to_date_spend",
        "scope": {
          "type": "user",
          "user_id": "user_id"
        },
        "source": {
          "type": "user",
          "user_id": "user_id"
        },
        "spend_limit_id": "spend_limit_id"
      },
      "status": "pending",
      "type": "spend_limit_increase_request"
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
