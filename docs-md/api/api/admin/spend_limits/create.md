# Set Spend Limit

Copy page



# Set Spend Limit

POST/v1/organizations/spend\_limits

Set a per-user spend limit override.

Upsert keyed on (scope, period): setting a limit that already exists
overwrites it in place. Only `scope.type: "user"` is accepted; seat-tier,
group, and organization-level defaults are configured in claude.ai.

##### Body

amount: string or null

Limit amount as a non-negative integer decimal string in the minor unit of the organization's billing currency (cents for USD): "50000" is $500.00. `null` sets an explicit no-limit override for this scope and `period` only — each period resolves independently, so caps for other periods still apply.

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

period: optional "daily" or "monthly" or "weekly"

One of the following:

"daily"

"monthly"

"weekly"

##### Returns



SpendLimit object{ id, amount, created\_at, 5 more }

A configured spend limit: a cap on metered spend for one scope and period.

Set Spend Limit

cURL

```shiki
curl https://api.anthropic.com/v1/organizations/spend_limits \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -d '{
          "amount": "50000",
          "scope": {
            "type": "user",
            "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
          },
          "period": "monthly"
        }'
```

Response 200



```shiki
{
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
}
```

##### Returns Examples

Response 200



```shiki
{
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
}
```

---

*Copyright © Anthropic. All rights reserved.*
