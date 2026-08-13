# Spend Limits

Copy page



# Spend Limits

##### [Set Spend Limit](api/admin/spend_limits/create.md)

POST/v1/organizations/spend\_limits

##### [Get Spend Limit](api/admin/spend_limits/retrieve.md)

GET/v1/organizations/spend\_limits/{spend\_limit\_id}

##### [Delete Spend Limit](api/admin/spend_limits/delete.md)

DELETE/v1/organizations/spend\_limits/{spend\_limit\_id}

##### [List Effective Spend Limits](api/admin/spend_limits/list_effective.md)

GET/v1/organizations/spend\_limits/effective

##### ModelsExpand Collapse

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



SpendSummary object { actor, amount, currency, 5 more } 

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

period: "daily" or "monthly" or "weekly"

One of the following:

"daily"

"monthly"

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

SpendLimitDeleteResponse object { id, type } 

id: string

type: "spend\_limit\_deleted"

#### Spend LimitsIncrease Requests

##### [List Spend Limit Increase Requests](api/admin/spend_limits/increase_requests/list.md)

GET/v1/organizations/spend\_limit\_increase\_requests

##### [Get Spend Limit Increase Request](api/admin/spend_limits/increase_requests/retrieve.md)

GET/v1/organizations/spend\_limit\_increase\_requests/{spend\_limit\_increase\_request\_id}

##### [Approve Spend Limit Increase Request](api/admin/spend_limits/increase_requests/approve.md)

POST/v1/organizations/spend\_limit\_increase\_requests/{spend\_limit\_increase\_request\_id}/approve

##### [Deny Spend Limit Increase Request](api/admin/spend_limits/increase_requests/deny.md)

POST/v1/organizations/spend\_limit\_increase\_requests/{spend\_limit\_increase\_request\_id}/deny

---

*Copyright © Anthropic. All rights reserved.*
