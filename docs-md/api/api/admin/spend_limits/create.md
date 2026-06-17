# Set Spend Limit

Copy page



# Set Spend Limit

POST/v1/organizations/spend\_limits

Set a per-user spend limit override.

Upsert keyed on (scope, period): setting a limit that already exists
overwrites it in place. Only `scope.type: "user"` is accepted; seat-tier,
group, and organization-level defaults are configured in claude.ai.

##### Body ParametersJSONExpand Collapse

amount: string



scope: object { type, user\_id } 

type: "user"

user\_id: string



period: optional "monthly" or "daily" or "weekly"

One of the following:

"monthly"

"daily"

"weekly"

##### ReturnsExpand Collapse



SpendLimit object { id, amount, created\_at, 5 more } 

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

Set Spend Limit



```shiki
curl https://api.anthropic.com/v1/organizations/spend_limits \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "amount": "amount",
          "scope": {
            "type": "user",
            "user_id": "user_id"
          }
        }'
```

Response 200



```shiki
{
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
}
```

##### Returns Examples

Response 200



```shiki
{
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
}
```

---

*Copyright © Anthropic. All rights reserved.*
