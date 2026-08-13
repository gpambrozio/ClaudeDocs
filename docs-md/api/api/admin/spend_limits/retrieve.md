# Get Spend Limit

Copy page



# Get Spend Limit

GET/v1/organizations/spend\_limits/{spend\_limit\_id}

Retrieve a spend limit by ID.

##### Path ParametersExpand Collapse

spend\_limit\_id: string

ID of the Spend Limit.

##### ReturnsExpand Collapse



SpendLimit object { id, amount, created\_at, 5 more } 

id: string

amount: string

created\_at: string

currency: string



period: "daily" or "monthly" or "weekly"

One of the following:

"daily"

"monthly"

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

Get Spend Limit



```shiki
curl https://api.anthropic.com/v1/organizations/spend_limits/$SPEND_LIMIT_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
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
  "amount": "50000",
  "created_at": "2019-12-27T18:11:19.117Z",
  "currency": "USD",
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
