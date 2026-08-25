# Spend Limits

Copy page



# Spend Limits

##### [Set Spend Limit](api/http/admin/spend_limits/create.md)

POST/v1/organizations/spend\_limits

##### [Get Spend Limit](api/http/admin/spend_limits/retrieve.md)

GET/v1/organizations/spend\_limits/{spend\_limit\_id}

##### [Delete Spend Limit](api/http/admin/spend_limits/delete.md)

DELETE/v1/organizations/spend\_limits/{spend\_limit\_id}

##### [List Effective Spend Limits](api/http/admin/spend_limits/list_effective.md)

GET/v1/organizations/spend\_limits/effective

##### Models



SpendLimit object{ id, amount, created\_at, 5 more }



SpendSummary object{ actor, amount, currency, 5 more }

Per-member effective-limit report row (GET /spend\_limits/effective).



SpendLimitDeleteResponse object{ id, type }

id: string



type: "spend\_limit\_deleted"

defaultspend\_limit\_deleted

#### Spend Limits[Increase Requests](api/http/admin/spend_limits/increase_requests.md)

##### [List Spend Limit Increase Requests](api/http/admin/spend_limits/increase_requests/list.md)

GET/v1/organizations/spend\_limit\_increase\_requests

##### [Get Spend Limit Increase Request](api/http/admin/spend_limits/increase_requests/retrieve.md)

GET/v1/organizations/spend\_limit\_increase\_requests/{spend\_limit\_increase\_request\_id}

##### [Approve Spend Limit Increase Request](api/http/admin/spend_limits/increase_requests/approve.md)

POST/v1/organizations/spend\_limit\_increase\_requests/{spend\_limit\_increase\_request\_id}/approve

##### [Deny Spend Limit Increase Request](api/http/admin/spend_limits/increase_requests/deny.md)

POST/v1/organizations/spend\_limit\_increase\_requests/{spend\_limit\_increase\_request\_id}/deny

---

*Copyright © Anthropic. All rights reserved.*
