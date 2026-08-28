# Rate Limits

Copy page



cURL

# Rate Limits

##### [List Workspace Rate Limits](api/http/beta/organization/workspaces/rate_limits/list.md)

GET/v1/organizations/workspaces/{workspace\_id}/rate\_limits

##### Models



BetaWorkspaceRateLimit object{ group\_type, limits, models, 3 more }



BetaWorkspaceRateLimitValue object{ org\_limit, type, value }

org\_limit: number or null

The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

type: string

The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

value: number

The workspace-level override value for this limiter type.

---

*Copyright © Anthropic. All rights reserved.*
