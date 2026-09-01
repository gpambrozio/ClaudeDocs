# List Spend Limit Increase Requests

Copy page



# List Spend Limit Increase Requests

GET/v1/organizations/spend\_limit\_increase\_requests

List spend limit increase requests, most recent first.

Pending requests include a live `spend_summary` for the requester.
Requests whose requester is no longer a member are excluded.

##### Query parameters

actor\_ids: optional array of string

Filter by requester, as `user_...` tagged IDs.



limit: optional number

default20

maximum1000

minimum1

page: optional string

Opaque cursor from a previous response's `next_page`.



status: optional array of "approved" or "denied" or "pending"

Filter by status. Omit to return all.

One of the following:

"approved"

"denied"

"pending"

##### Returns



data: array of [SpendLimitIncreaseRequest](api/http/admin/spend_limits/increase_requests.md) { id, actor, created\_at, 6 more }

id: string



actor: object{ deleted, email\_address, name, 2 more }

A user within the organization. `name` and `email_address` are
null when the underlying account is unavailable or has been deleted;
`deleted` is true only for deleted accounts.



deleted: boolean

True only when the underlying account has been deleted.

defaultfalse

email\_address: string or null

The user's email address. Null when the account is unavailable or has been deleted.

name: string or null

The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.



type: "user\_actor"

Actor type. Always `user_actor`.

defaultuser\_actor

user\_id: string

Tagged ID of the user.



created\_at: string

formatdate-time



period: "daily" or "monthly" or "weekly"

One of the following:

"daily"

"monthly"

"weekly"



resolved\_at: string or null

formatdate-time



resolved\_by: object{ deleted, email\_address, name, 2 more } or object{ scoped\_api\_key\_id, type } or null

A user within the organization. `name` and `email_address` are
null when the underlying account is unavailable or has been deleted;
`deleted` is true only for deleted accounts.

One of the following:



UserActor object{ deleted, email\_address, name, 2 more }

A user within the organization. `name` and `email_address` are
null when the underlying account is unavailable or has been deleted;
`deleted` is true only for deleted accounts.



deleted: boolean

True only when the underlying account has been deleted.

defaultfalse

email\_address: string or null

The user's email address. Null when the account is unavailable or has been deleted.

name: string or null

The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.



type: "user\_actor"

Actor type. Always `user_actor`.

defaultuser\_actor

user\_id: string

Tagged ID of the user.



ScopedAPIKeyActor object{ scoped\_api\_key\_id, type }

A scoped Admin API key acting on behalf of the organization.

scoped\_api\_key\_id: string



type: "scoped\_api\_key\_actor"

defaultscoped\_api\_key\_actor



spend\_summary: [SpendSummary](api/http/admin/spend_limits.md) { actor, amount, currency, 5 more } or null

Per-member effective-limit report row (`GET /spend_limits/effective`).



status: "approved" or "denied" or "pending"

One of the following:

"approved"

"denied"

"pending"



type: "spend\_limit\_increase\_request"

defaultspend\_limit\_increase\_request

next\_page: string or null

List Spend Limit Increase Requests

cURL

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
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
