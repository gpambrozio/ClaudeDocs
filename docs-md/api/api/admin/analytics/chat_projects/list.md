# Get Chat Project Usage

Copy page



# Get Chat Project Usage

GET/v1/organizations/analytics/apps/chat/projects

Get per-project activity for a given day, with cursor-based pagination.

Returns activity metrics for each project in the organization, sorted by
project ID. Use group\_by[] to break projects out per member or per RBAC
group, and filter[] to scope results; the parameter descriptions list the
supported dimensions. Available to organizations on a Claude Enterprise
plan. Requires an API key with the `read:analytics` scope.

##### Query parameters



date: optional string

UTC date in YYYY-MM-DD format. The day to get project activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

formatdate



ending\_date: optional string

UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with starting\_date. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after starting\_date.

formatdate



filter: optional array of string

Filters as 'dimension:value', e.g. filter[]=rbac\_group\_id:<id>. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: project\_id, rbac\_group\_id, user\_id. Value forms: project\_id takes a tagged project id (claude\_proj\_...); rbac\_group\_id takes the tagged id (rbac\_group\_..., as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); user\_id takes a tagged user id (user\_...), as emitted in responses. An unsupported dimension returns 400. At most 100 entries.

maxItems100



group\_by: optional array of "rbac\_group\_id" or "user\_id"

Dimensions to break results out by (e.g. group\_by[]=user\_id). Supported on this endpoint: rbac\_group\_id, user\_id. Grouped rows carry the requested dimension values as additional fields and paginate like ungrouped responses via next\_page; an unsupported dimension returns 400. rbac\_group\_id attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

maxItems100

One of the following:

"rbac\_group\_id"

"user\_id"



limit: optional number

Number of results per page (1-1000, default 100).

minimum1

maximum1000



order: optional "asc" or "desc"

Sort direction: 'asc' or 'desc'. Defaults to 'asc' for the endpoint's sort column and to 'desc' when order\_by names a metric (a top-N ranking). Applies to order\_by, or to the endpoint's default sort field when order\_by is omitted.

One of the following:

"asc"

"desc"

order\_by: optional string

Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

page: optional string

Opaque cursor from a previous response's next\_page field.



starting\_date: optional string

UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either date or starting\_date, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

formatdate

##### Returns



ChatProjectUsage object{ data, next\_page }

Response for GET /v1/organizations/analytics/apps/chat/projects.

### Get Chat Project Usage

cURL



```shiki
curl https://api.anthropic.com/v1/organizations/analytics/apps/chat/projects \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

Response 200



```shiki
{
  "data": [
    {
      "distinct_user_count": 0,
      "message_count": 0,
      "project_id": "project_id",
      "project_name": "project_name",
      "created_at": "created_at",
      "created_by": {
        "id": "id",
        "email_address": "email_address",
        "type": "user"
      },
      "distinct_conversation_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "distinct_user_count": 0,
      "message_count": 0,
      "project_id": "project_id",
      "project_name": "project_name",
      "created_at": "created_at",
      "created_by": {
        "id": "id",
        "email_address": "email_address",
        "type": "user"
      },
      "distinct_conversation_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
