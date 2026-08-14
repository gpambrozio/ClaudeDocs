# Increase Requests

Copy page



# Increase Requests

##### [List Spend Limit Increase Requests](api/admin/spend_limits/increase_requests/list.md)

GET/v1/organizations/spend\_limit\_increase\_requests

##### [Get Spend Limit Increase Request](api/admin/spend_limits/increase_requests/retrieve.md)

GET/v1/organizations/spend\_limit\_increase\_requests/{spend\_limit\_increase\_request\_id}

##### [Approve Spend Limit Increase Request](api/admin/spend_limits/increase_requests/approve.md)

POST/v1/organizations/spend\_limit\_increase\_requests/{spend\_limit\_increase\_request\_id}/approve

##### [Deny Spend Limit Increase Request](api/admin/spend_limits/increase_requests/deny.md)

POST/v1/organizations/spend\_limit\_increase\_requests/{spend\_limit\_increase\_request\_id}/deny

##### ModelsExpand Collapse



SpendLimitIncreaseRequest object { id, actor, created\_at, 6 more } 

id: string



actor: object { deleted, email\_address, name, 2 more } 

A user within the organization. `name` and `email_address` are
null when the underlying account is unavailable or has been deleted;
`deleted` is true only for deleted accounts.

deleted: boolean

email\_address: string or null

name: string or null

type: "user\_actor"

user\_id: string

created\_at: string



period: "daily" or "monthly" or "weekly"

One of the following:

"daily"

"monthly"

"weekly"

resolved\_at: string or null



resolved\_by: object { deleted, email\_address, name, 2 more }  or object { scoped\_api\_key\_id, type }  or null

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

email\_address: string or null

name: string or null

type: "user\_actor"

user\_id: string



ScopedAPIKeyActor object { scoped\_api\_key\_id, type } 

A scoped Admin API key acting on behalf of the organization.

scoped\_api\_key\_id: string

type: "scoped\_api\_key\_actor"



spend\_summary: [SpendSummary](api/admin/spend_limits.md) { actor, amount, currency, 5 more }  or null

Per-member effective-limit report row (GET /spend\_limits/effective).



actor: object { deleted, email\_address, name, 2 more } 

A user within the organization. `name` and `email_address` are
null when the underlying account is unavailable or has been deleted;
`deleted` is true only for deleted accounts.

deleted: boolean

email\_address: string or null

name: string or null

type: "user\_actor"

user\_id: string

amount: string or null

Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

currency: string

ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.



period: "daily" or "monthly" or "weekly"

One of the following:

"daily"

"monthly"

"weekly"

period\_to\_date\_spend: string

The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

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

status: "approved" or "denied" or "pending"

One of the following:

"approved"

"denied"

"pending"

type: "spend\_limit\_increase\_request"



IncreaseRequestApproveResponse object { id, actor, created\_at, 7 more } 

id: string



actor: object { deleted, email\_address, name, 2 more } 

A user within the organization. `name` and `email_address` are
null when the underlying account is unavailable or has been deleted;
`deleted` is true only for deleted accounts.

deleted: boolean

email\_address: string or null

name: string or null

type: "user\_actor"

user\_id: string

created\_at: string



period: "daily" or "monthly" or "weekly"

One of the following:

"daily"

"monthly"

"weekly"

resolved\_at: string or null



resolved\_by: object { deleted, email\_address, name, 2 more }  or object { scoped\_api\_key\_id, type }  or null

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

email\_address: string or null

name: string or null

type: "user\_actor"

user\_id: string



ScopedAPIKeyActor object { scoped\_api\_key\_id, type } 

A scoped Admin API key acting on behalf of the organization.

scoped\_api\_key\_id: string

type: "scoped\_api\_key\_actor"



spend\_limit: [SpendLimit](api/admin/spend_limits.md) { id, amount, created\_at, 5 more } 

id: string

amount: string or null

Limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD): "50000" is $500.00. `null` means no numeric cap is configured at this scope — see the effective report for whether a limit applies.

created\_at: string

currency: string

ISO 4217 code of the organization's billing currency; the unit for `amount`.

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

spend\_summary: [SpendSummary](api/admin/spend_limits.md) { actor, amount, currency, 5 more }  or null

Per-member effective-limit report row (GET /spend\_limits/effective).



actor: object { deleted, email\_address, name, 2 more } 

A user within the organization. `name` and `email_address` are
null when the underlying account is unavailable or has been deleted;
`deleted` is true only for deleted accounts.

deleted: boolean

email\_address: string or null

name: string or null

type: "user\_actor"

user\_id: string

amount: string or null

Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

currency: string

ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.



period: "daily" or "monthly" or "weekly"

One of the following:

"daily"

"monthly"

"weekly"

period\_to\_date\_spend: string

The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

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

status: "approved" or "denied" or "pending"

One of the following:

"approved"

"denied"

"pending"

type: "spend\_limit\_increase\_request"

---

*Copyright © Anthropic. All rights reserved.*
