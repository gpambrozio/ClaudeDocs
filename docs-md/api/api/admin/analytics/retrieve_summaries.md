# Get Activity Summaries

Copy page



# Get Activity Summaries

GET/v1/organizations/analytics/summaries

Get organization-wide activity summaries for a date range.

Returns one entry per day in [starting\_date, ending\_date). Data is
typically available with a 1-day lag and may be revised by a few percent
over the following days: when ending\_date is omitted it defaults to the
most recent available day + 1, so the last entry covers the most recent
available day. Available to organizations on a Claude Enterprise plan.
Requires an API key with the `read:analytics` scope.

##### Query ParametersExpand Collapse

starting\_date: string

UTC date in YYYY-MM-DD format. Start of the date range (inclusive). Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

ending\_date: optional string

UTC date in YYYY-MM-DD format. End of the date range (exclusive). Data is typically available with a 1-day lag, so this can be at most today — which is also the default when omitted, making the last entry cover the most recent available day. Data may be revised by a few percent over the following days. The range may span at most 366 days.

filter: optional array of string

Filters as 'dimension

'. Only rbac\_group\_id is supported (e.g. filter[]=rbac\_group\_id:<id>); repeat the param to OR across groups. Scopes the whole day series to members of the matching group(s), re-aggregated from member-level activity — org-wide seat/invite fields and the adoption rates derived from them are null on scoped rows. rbac\_group\_id accepts the tagged id (rbac\_group\_..., as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each UTC day (time-of-usage attribution). At most 100 entries.

##### ReturnsExpand Collapse



ActivitySummary object { summaries } 

Response for GET /v1/organizations/analytics/summaries.



summaries: array of object { assigned\_seat\_count, cowork\_daily\_active\_user\_count, cowork\_monthly\_active\_user\_count, 26 more } 

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

chat\_daily\_active\_user\_count: optional number

Number of users with claude.ai (chat) activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

chat\_monthly\_active\_user\_count: optional number

Number of users with claude.ai (chat) activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

chat\_weekly\_active\_user\_count: optional number

Number of users with claude.ai (chat) activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

claude\_code\_daily\_active\_user\_count: optional number

Number of users with Claude Code activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

claude\_code\_monthly\_active\_user\_count: optional number

Number of users with Claude Code activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

claude\_code\_weekly\_active\_user\_count: optional number

Number of users with Claude Code activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

claude\_design\_daily\_active\_user\_count: optional number

Number of users with Claude Design activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

claude\_design\_monthly\_active\_user\_count: optional number

Number of users with Claude Design activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

claude\_design\_weekly\_active\_user\_count: optional number

Number of users with Claude Design activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

office\_agent\_daily\_active\_user\_count: optional number

Number of users with Claude in Office activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

office\_agent\_monthly\_active\_user\_count: optional number

Number of users with Claude in Office activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

office\_agent\_weekly\_active\_user\_count: optional number

Number of users with Claude in Office activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

science\_daily\_active\_user\_count: optional number

Number of users with Claude Science activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

science\_entitled\_user\_count: optional number

Number of users with a Claude Science seat entitlement (per-seat RBAC) at the time of the daily snapshot. The funnel top; independent of the org-level Claude Science toggle. Null when the response is scoped to an RBAC group — entitlement is org-wide and has no per-group analogue. Omitted from the response while the per-product breakdown is not enabled for this organization.

science\_monthly\_active\_user\_count: optional number

Number of users with Claude Science activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

science\_weekly\_active\_user\_count: optional number

Number of users with Claude Science activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

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
      "weekly_adoption_rate": 0,
      "chat_daily_active_user_count": 0,
      "chat_monthly_active_user_count": 0,
      "chat_weekly_active_user_count": 0,
      "claude_code_daily_active_user_count": 0,
      "claude_code_monthly_active_user_count": 0,
      "claude_code_weekly_active_user_count": 0,
      "claude_design_daily_active_user_count": 0,
      "claude_design_monthly_active_user_count": 0,
      "claude_design_weekly_active_user_count": 0,
      "office_agent_daily_active_user_count": 0,
      "office_agent_monthly_active_user_count": 0,
      "office_agent_weekly_active_user_count": 0,
      "science_daily_active_user_count": 0,
      "science_entitled_user_count": 0,
      "science_monthly_active_user_count": 0,
      "science_weekly_active_user_count": 0
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
      "weekly_adoption_rate": 0,
      "chat_daily_active_user_count": 0,
      "chat_monthly_active_user_count": 0,
      "chat_weekly_active_user_count": 0,
      "claude_code_daily_active_user_count": 0,
      "claude_code_monthly_active_user_count": 0,
      "claude_code_weekly_active_user_count": 0,
      "claude_design_daily_active_user_count": 0,
      "claude_design_monthly_active_user_count": 0,
      "claude_design_weekly_active_user_count": 0,
      "office_agent_daily_active_user_count": 0,
      "office_agent_monthly_active_user_count": 0,
      "office_agent_weekly_active_user_count": 0,
      "science_daily_active_user_count": 0,
      "science_entitled_user_count": 0,
      "science_monthly_active_user_count": 0,
      "science_weekly_active_user_count": 0
    }
  ]
}
```

---

*Copyright © Anthropic. All rights reserved.*
