# Approve Spend Limit Increase Request

Copy page



# Approve Spend Limit Increase Request

POST/v1/organizations/spend\_limit\_increase\_requests/{spend\_limit\_increase\_request\_id}/approve

Approve a pending spend limit increase request.

Writes a per-user spend limit at `amount` for the requester and
transitions the request to `approved`. `period` defaults to the period
the member was blocked on. Anthropic emails the requester unless
`suppress_notification` is set.

##### Path ParametersExpand Collapse

spend\_limit\_increase\_request\_id: string

ID of the spend limit increase request.

##### Body ParametersJSONExpand Collapse

amount: string

New per-user cap as a non-negative integer decimal string (minor units).



period: optional "monthly" or "daily" or "weekly"

One of the following:

"monthly"

"daily"

"weekly"

suppress\_notification: optional boolean

##### ReturnsExpand Collapse

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

spend\_limit: [SpendLimit](api/admin.md) { id, amount, created\_at, 5 more } 

id: string

amount: string

created\_at: string

currency: string



period: "monthly" or "daily" or "weekly"

One of the following:

"monthly"

"daily"

"weekly"



scope: object { type, user\_id }  or object { seat\_tier, type }  or object { rbac\_group\_id, type }  or 2 more

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

type: "spend\_limit"

updated\_at: string



spend\_summary: [SpendSummary](api/admin.md) { actor, amount, currency, 5 more } 

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

Approve Spend Limit Increase Request



```shiki
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/$SPEND_LIMIT_INCREASE_REQUEST_ID/approve \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "amount": "amount"
        }'
```

Response 200



```shiki
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
  "spend_limit": {
    "id": "id",
    "amount": "amount",
    "created_at": "2019-12-27T18:11:19.117Z",
    "currency": "currency",
    "period": "monthly",
    "scope": {
      "type": "user",
      "user_id": "user_id"
    },
    "type": "spend_limit",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "spend_summary": {
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
  },
  "status": "pending",
  "type": "spend_limit_increase_request"
}
```

##### Returns Examples

Response 200



```shiki
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
  "spend_limit": {
    "id": "id",
    "amount": "amount",
    "created_at": "2019-12-27T18:11:19.117Z",
    "currency": "currency",
    "period": "monthly",
    "scope": {
      "type": "user",
      "user_id": "user_id"
    },
    "type": "spend_limit",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "spend_summary": {
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
  },
  "status": "pending",
  "type": "spend_limit_increase_request"
}
```

---

*Copyright © Anthropic. All rights reserved.*
