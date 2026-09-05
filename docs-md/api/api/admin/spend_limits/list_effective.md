# List Effective Spend Limits

Copy page



# List Effective Spend Limits

GET/v1/organizations/spend\_limits/effective

List each member's effective spend limit and period-to-date spend.

Returns one row per (member, period) the member resolves a spend limit
for, with the `source` scope the spend limit was inherited from.
Paginates by member, so a member's periods never split across pages.

##### Query parameters



limit: optional number

Maximum number of members per page. A member's period rows never split across pages, so a page may carry more rows than this. Defaults to `20`.

default20

maximum1000

minimum1

page: optional string

Opaque cursor from a previous response's `next_page` field.



period: optional array of "daily" or "monthly" or "weekly"

Restrict the report to these limit periods. Omit to return one row per period each member resolves a spend limit for.

maxItems3

One of the following:

"daily"

"monthly"

"weekly"



user\_ids: optional array of string

Restrict the report to these members, by tagged user ID (`user_...`). At most 100 entries.

maxItems100

##### Returns



data: array of [SpendSummary](api/http/admin/spend_limits.md) { actor, amount, currency, 5 more }

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

amount: string or null

Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

currency: string

ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.



period: "daily" or "monthly" or "weekly"

Period this row's effective limit and spend are reported for.

One of the following:

"daily"

"monthly"

"weekly"

period\_to\_date\_spend: string

The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.



scope: object{ type, user\_id }

Scope selecting a single member of the organization.



type: "user"

Scope type. Always `user` for this scope.

defaultuser

user\_id: string

Tagged ID of the member the spend limit applies to.



source: object{ type, user\_id } or object{ seat\_tier, type } or object{ rbac\_group\_id, type } or 2 more

Scope selecting a single member of the organization.

One of the following:



User object{ type, user\_id }

Scope selecting a single member of the organization.



type: "user"

Scope type. Always `user` for this scope.

defaultuser

user\_id: string

Tagged ID of the member the spend limit applies to.



SeatTier object{ seat\_tier, type }

seat\_tier: string



type: "seat\_tier"

defaultseat\_tier



RbacGroup object{ rbac\_group\_id, type }

rbac\_group\_id: string



type: "rbac\_group"

defaultrbac\_group



OrganizationService object{ service, type }

service: string



type: "organization\_service"

defaultorganization\_service



Organization object{ type }



type: "organization"

defaultorganization

spend\_limit\_id: string

next\_page: string or null

List Effective Spend Limits

cURL

```shiki
curl https://api.anthropic.com/v1/organizations/spend_limits/effective \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN"
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
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
