# Approve Spend Limit Increase Request

Copy page



# Approve Spend Limit Increase Request

POST/v1/organizations/spend\_limit\_increase\_requests/{spend\_limit\_increase\_request\_id}/approve

Approve a pending spend limit increase request.

Writes a per-user spend limit at `amount` for the requester and
transitions the request to `approved`. `period` defaults to the period
the member was blocked on. Anthropic emails the requester unless
`suppress_notification` is set.

##### Path parameters

spend\_limit\_increase\_request\_id: string

ID of the spend limit increase request.

##### Body

amount: string

New per-user spend limit as a non-negative integer decimal string (minor units).



period: optional "daily" or "monthly" or "weekly" or null

One of the following:

"daily"

"monthly"

"weekly"

suppress\_notification: optional boolean

##### Returns

id: string



actor: object{ deleted, email\_address, name, 2 more }

A user within the organization. `name` and `email_address` are
null when the underlying account is unavailable or has been deleted;
`deleted` is true only for deleted accounts.



deleted: boolean

True only when the underlying account has been deleted.

defaultfalse

email\_address: string or null

The user's email address. Null when the account is unavailable or has been deleted.

name: string or null

The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.



type: "user\_actor"

Actor type. Always `user_actor`.

defaultuser\_actor

user\_id: string

Tagged ID of the user.



created\_at: string

formatdate-time



period: "daily" or "monthly" or "weekly"

One of the following:

"daily"

"monthly"

"weekly"



resolved\_at: string or null

formatdate-time



resolved\_by: object{ deleted, email\_address, name, 2 more } or object{ scoped\_api\_key\_id, type } or null

A user within the organization. `name` and `email_address` are
null when the underlying account is unavailable or has been deleted;
`deleted` is true only for deleted accounts.

One of the following:



UserActor object{ deleted, email\_address, name, 2 more }

A user within the organization. `name` and `email_address` are
null when the underlying account is unavailable or has been deleted;
`deleted` is true only for deleted accounts.



deleted: boolean

True only when the underlying account has been deleted.

defaultfalse

email\_address: string or null

The user's email address. Null when the account is unavailable or has been deleted.

name: string or null

The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.



type: "user\_actor"

Actor type. Always `user_actor`.

defaultuser\_actor

user\_id: string

Tagged ID of the user.



ScopedAPIKeyActor object{ scoped\_api\_key\_id, type }

A scoped Admin API key acting on behalf of the organization.

scoped\_api\_key\_id: string



type: "scoped\_api\_key\_actor"

defaultscoped\_api\_key\_actor



spend\_limit: [SpendLimit](api/http/admin/spend_limits.md) { id, amount, created\_at, 5 more }

A configured spend limit: a cap on metered spend for one scope and period.



spend\_summary: [SpendSummary](api/http/admin/spend_limits.md) { actor, amount, currency, 5 more } or null

Per-member effective-limit report row (`GET /spend_limits/effective`).



status: "approved" or "denied" or "pending"

One of the following:

"approved"

"denied"

"pending"



type: "spend\_limit\_increase\_request"

defaultspend\_limit\_increase\_request



### Approve Spend Limit Increase Request

cURL



```shiki
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/$SPEND_LIMIT_INCREASE_REQUEST_ID/approve \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "amount": "50000",
          "period": "monthly"
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
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "period": "monthly",
  "resolved_at": "2019-12-27T18:11:19.117Z",
  "resolved_by": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "spend_limit": {
    "id": "id",
    "amount": "50000",
    "created_at": "2019-12-27T18:11:19.117Z",
    "currency": "USD",
    "period": "monthly",
    "scope": {
      "type": "user",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
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
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "amount": "50000",
    "currency": "USD",
    "period": "monthly",
    "period_to_date_spend": "12050.5",
    "scope": {
      "type": "user",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "source": {
      "type": "user",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "spend_limit_id": "spend_limit_id"
  },
  "status": "approved",
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
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "period": "monthly",
  "resolved_at": "2019-12-27T18:11:19.117Z",
  "resolved_by": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "spend_limit": {
    "id": "id",
    "amount": "50000",
    "created_at": "2019-12-27T18:11:19.117Z",
    "currency": "USD",
    "period": "monthly",
    "scope": {
      "type": "user",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
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
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "amount": "50000",
    "currency": "USD",
    "period": "monthly",
    "period_to_date_spend": "12050.5",
    "scope": {
      "type": "user",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "source": {
      "type": "user",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "spend_limit_id": "spend_limit_id"
  },
  "status": "approved",
  "type": "spend_limit_increase_request"
}
```

---

*Copyright © Anthropic. All rights reserved.*
