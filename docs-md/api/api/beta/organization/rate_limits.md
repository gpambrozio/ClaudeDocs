# Rate Limits

Copy page



cURL

# Rate Limits

##### [List Organization Rate Limits](api/http/beta/organization/rate_limits/list.md)

GET/v1/organizations/rate\_limits

##### Models



BetaOrganizationRateLimit object{ id, group\_type, limits, 2 more }



BetaOrganizationRateLimitValue object{ type, value }

type: string

The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

value: number

The configured limit value for this limiter type.

---

*Copyright © Anthropic. All rights reserved.*
