# List Effective Spend Limits

Copy page



# List Effective Spend Limits

GET/v1/organizations/spend\_limits/effective

List each member's effective spend limit and period-to-date spend.

Returns one row per (member, period) the member resolves a cap for, with
the `source` scope the cap was inherited from. Paginates by member, so a
member's periods never split across pages.

##### Query ParametersExpand Collapse

limit: optional number

page: optional string

period: optional array of string

user\_ids: optional array of string

##### ReturnsExpand Collapse



data: array of [SpendSummary](api/admin.md) { actor, amount, currency, 5 more } 

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

next\_page: string

List Effective Spend Limits



```shiki
curl https://api.anthropic.com/v1/organizations/spend_limits/effective \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "data": [
    {
      "actor": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_id"
      },
      "amount": "amount",
      "currency": "currency",
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
      "actor": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_id"
      },
      "amount": "amount",
      "currency": "currency",
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
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
