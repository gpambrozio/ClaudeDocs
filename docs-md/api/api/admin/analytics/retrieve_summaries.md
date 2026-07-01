# Get Activity Summaries

Copy page



# Get Activity Summaries

GET/v1/organizations/analytics/summaries

Get organization-wide activity summaries for a date range.

Returns one entry per day in [starting\_date, ending\_date). Data is
finalized with a 3-day lag: when ending\_date is omitted it defaults to
2 days before today, so the last entry covers the most recent day with
finalized data. Available to organizations on a Claude Enterprise plan.
Requires an API key with the `read:analytics` scope.

##### Query ParametersExpand Collapse

starting\_date: string

UTC date in YYYY-MM-DD format. Start of the date range (inclusive). Must be at least 3 days in the past (data is finalized with a 3-day lag) and no earlier than 2026-01-01.

ending\_date: optional string

UTC date in YYYY-MM-DD format. End of the date range (exclusive). Data is finalized with a 3-day lag, so this can be at most 2 days before today — which is also the default when omitted, making the last entry cover the most recent day with finalized data. The range may span at most 366 days.

##### ReturnsExpand Collapse



ActivitySummary object { summaries } 

Response for GET /v1/organizations/analytics/summaries.



summaries: array of object { assigned\_seat\_count, cowork\_daily\_active\_user\_count, cowork\_monthly\_active\_user\_count, 10 more } 

assigned\_seat\_count: number

Number of seats currently assigned to members. Null when the response is scoped to an RBAC group — seat assignment is org-wide and has no per-group analogue.

cowork\_daily\_active\_user\_count: number

Number of users with Cowork activity on the requested day

cowork\_monthly\_active\_user\_count: number

Number of users with Cowork activity in the 30-day rolling window

cowork\_weekly\_active\_user\_count: number

Number of users with Cowork activity in the 7-day rolling window

daily\_active\_user\_count: number

Number of users with token consumption on the requested day

daily\_adoption\_rate: number

Percentage of assigned seats with activity on the requested day (DAU / assigned\_seat\_count \* 100). Null when the response is scoped to an RBAC group.

ending\_at: string

End time in UTC of aggregation period (e.g. 2026-01-16T00:00

)

monthly\_active\_user\_count: number

Number of users with token consumption in the 30-day rolling window

monthly\_adoption\_rate: number

Percentage of assigned seats with activity in the 30-day rolling window (MAU / assigned\_seat\_count \* 100). Null when the response is scoped to an RBAC group.

pending\_invite\_count: number

Number of pending invitations to join the organization. Null when the response is scoped to an RBAC group.

starting\_at: string

Start time in UTC of aggregation period (e.g. 2026-01-15T00:00

)

weekly\_active\_user\_count: number

Number of users with token consumption in the 7-day rolling window

weekly\_adoption\_rate: number

Percentage of assigned seats with activity in the 7-day rolling window (WAU / assigned\_seat\_count \* 100). Null when the response is scoped to an RBAC group.

Get Activity Summaries



```shiki
curl https://api.anthropic.com/v1/organizations/analytics/summaries \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "summaries": [
    {
      "assigned_seat_count": 0,
      "cowork_daily_active_user_count": 0,
      "cowork_monthly_active_user_count": 0,
      "cowork_weekly_active_user_count": 0,
      "daily_active_user_count": 0,
      "daily_adoption_rate": 0,
      "ending_at": "ending_at",
      "monthly_active_user_count": 0,
      "monthly_adoption_rate": 0,
      "pending_invite_count": 0,
      "starting_at": "starting_at",
      "weekly_active_user_count": 0,
      "weekly_adoption_rate": 0
    }
  ]
}
```

##### Returns Examples

Response 200



```shiki
{
  "summaries": [
    {
      "assigned_seat_count": 0,
      "cowork_daily_active_user_count": 0,
      "cowork_monthly_active_user_count": 0,
      "cowork_weekly_active_user_count": 0,
      "daily_active_user_count": 0,
      "daily_adoption_rate": 0,
      "ending_at": "ending_at",
      "monthly_active_user_count": 0,
      "monthly_adoption_rate": 0,
      "pending_invite_count": 0,
      "starting_at": "starting_at",
      "weekly_active_user_count": 0,
      "weekly_adoption_rate": 0
    }
  ]
}
```

---

*Copyright © Anthropic. All rights reserved.*
