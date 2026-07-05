# Get Connector Usage

Copy page



# Get Connector Usage

GET/v1/organizations/analytics/connectors

Get per-connector usage for a given day, with cursor-based pagination.

Returns connector usage metrics for the organization, sorted by connector
name. Connector names are normalized from their various sources — for
example, "Atlassian MCP server" and "mcp-atlassian" both appear as
"atlassian". Available to organizations on a Claude Enterprise plan.
Requires an API key with the `read:analytics` scope.

##### Query ParametersExpand Collapse

date: optional string

UTC date in YYYY-MM-DD format. The day to get connector usage for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

ending\_date: optional string

UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with starting\_date. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after starting\_date.

filter: optional array of string

Filters as 'dimension

', e.g. filter[]=rbac\_group\_id:<id>. Repeat the param for OR within a dimension and across dimensions for AND. Unsupported dimensions return 400. rbac\_group\_id accepts the tagged id (rbac\_group\_..., as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution). At most 100 entries.

group\_by: optional array of string

Dimensions to break results out by, e.g. group\_by[]=rbac\_group\_id. Supported dimensions vary by endpoint; an unsupported dimension returns 400. Grouped responses paginate like ungrouped ones via next\_page. rbac\_group\_id attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

limit: optional number

Number of results per page (1-1000, default 100).



order: optional "asc" or "desc"

Sort direction: 'asc' or 'desc'. Defaults to 'asc' for the endpoint's sort column and to 'desc' when order\_by names a metric (a top-N ranking). Applies to order\_by, or to the endpoint's default sort field when order\_by is omitted.

One of the following:

"asc"

"desc"

order\_by: optional string

Sort field. Restricted to the endpoint's sort column, plus — in date-range mode (starting\_date/ending\_date) — the endpoint's rankable metrics (metrics default to descending).

page: optional string

Opaque cursor from a previous response's next\_page field.

starting\_date: optional string

UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either date or starting\_date, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

##### ReturnsExpand Collapse



ConnectorUsage object { data, next\_page } 

Response for GET /v1/organizations/analytics/connectors.



data: array of object { chat\_metrics, claude\_code\_metrics, connector\_name, 10 more } 



chat\_metrics: object { distinct\_conversation\_connector\_used\_count } 

Claude.ai activity metrics for a single connector on a given day.

distinct\_conversation\_connector\_used\_count: number

Number of distinct conversations in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



claude\_code\_metrics: object { distinct\_session\_connector\_used\_count } 

Claude Code activity metrics for a single connector on a given day.

distinct\_session\_connector\_used\_count: number

Number of distinct Claude Code sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

connector\_name: string

Name of the connector



cowork\_metrics: object { distinct\_session\_connector\_used\_count } 

Cowork activity metrics for a single connector on a given day.

distinct\_session\_connector\_used\_count: number

Number of distinct Cowork sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

distinct\_user\_count: number

Number of distinct users who used the connector on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.



office\_metrics: object { excel, outlook, powerpoint, word } 

Office Agent activity metrics for a single connector on a given day, broken out by Office product.



excel: [ConnectorOfficeProductMetrics](api/admin/analytics.md) { distinct\_session\_connector\_used\_count } 

Office Agent activity metrics for a single connector on a given day within one Office product.

distinct\_session\_connector\_used\_count: number

Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



outlook: [ConnectorOfficeProductMetrics](api/admin/analytics.md) { distinct\_session\_connector\_used\_count } 

Office Agent activity metrics for a single connector on a given day within one Office product.

distinct\_session\_connector\_used\_count: number

Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



powerpoint: [ConnectorOfficeProductMetrics](api/admin/analytics.md) { distinct\_session\_connector\_used\_count } 

Office Agent activity metrics for a single connector on a given day within one Office product.

distinct\_session\_connector\_used\_count: number

Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



word: [ConnectorOfficeProductMetrics](api/admin/analytics.md) { distinct\_session\_connector\_used\_count } 

Office Agent activity metrics for a single connector on a given day within one Office product.

distinct\_session\_connector\_used\_count: number

Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

product: optional string

Product that produced this row's activity: one of chat, claude\_code, cowork, or office\_agent (the canonical Cost & Usage product naming; an office\_agent row's per-surface breakdown is in its office\_metrics). On /plugins only cowork and claude\_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group\_by[] or filter[] there is rejected). Present only when the request grouped by product.

rbac\_group\_id: optional string

Tagged RBAC group identifier (rbac\_group\_...), matching the spend-limits API spelling. Present only when the request grouped by rbac\_group\_id.

rbac\_group\_name: optional string

Resolved RBAC group display name, alongside rbac\_group\_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac\_group\_id remains the stable key.

read\_call\_count: optional number

Number of connector tool calls on the requested day whose trusted read-only annotation marked them read-only. Call count, not distinct users. Every call recorded on a classified surface lands in exactly one of read\_call\_count, write\_call\_count, or unclassified\_call\_count, so the three sum to the day's classified calls. Classification is forward-only per surface: claude.ai from 2026-06-01, Claude Code from 2026-05-30, Claude in Office from 2026-05-29, Cowork from 2026-06-02 (Cowork clients predating annotation forwarding land in unclassified\_call\_count). Null, never 0, when the value cannot be stated: the read/write split is not enabled for this organization, or the day predates 2026-05-29. For a date-range total, sum the per-day values, but treat a window that extends before 2026-05-29 as null rather than summing only its covered days — date-range rollup mode (starting\_date/ending\_date) applies both rules server-side.

unclassified\_call\_count: optional number

Number of connector tool calls on the requested day with no trusted read-only annotation — the annotation is optional in the MCP spec and is discarded when connector access controls are active, so unclassified calls are common. This field shows how much of the day's classified activity the read/write split actually covers. Call count, not distinct users. One of the three call-classification buckets; see read\_call\_count for the per-surface data-start dates, null conditions, and date-range guidance.

user\_id: optional string

Tagged user identifier (e.g. user\_...). Present only when the request grouped by user\_id.

write\_call\_count: optional number

Number of connector tool calls on the requested day whose trusted read-only annotation marked them not read-only. Call count, not distinct users. One of the three call-classification buckets; see read\_call\_count for the per-surface data-start dates, null conditions, and date-range guidance.

next\_page: string

Opaque cursor for the next page, or null if no more results

Get Connector Usage



```shiki
curl https://api.anthropic.com/v1/organizations/analytics/connectors \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "data": [
    {
      "chat_metrics": {
        "distinct_conversation_connector_used_count": 0
      },
      "claude_code_metrics": {
        "distinct_session_connector_used_count": 0
      },
      "connector_name": "connector_name",
      "cowork_metrics": {
        "distinct_session_connector_used_count": 0
      },
      "distinct_user_count": 0,
      "office_metrics": {
        "excel": {
          "distinct_session_connector_used_count": 0
        },
        "outlook": {
          "distinct_session_connector_used_count": 0
        },
        "powerpoint": {
          "distinct_session_connector_used_count": 0
        },
        "word": {
          "distinct_session_connector_used_count": 0
        }
      },
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "read_call_count": 0,
      "unclassified_call_count": 0,
      "user_id": "user_id",
      "write_call_count": 0
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
      "chat_metrics": {
        "distinct_conversation_connector_used_count": 0
      },
      "claude_code_metrics": {
        "distinct_session_connector_used_count": 0
      },
      "connector_name": "connector_name",
      "cowork_metrics": {
        "distinct_session_connector_used_count": 0
      },
      "distinct_user_count": 0,
      "office_metrics": {
        "excel": {
          "distinct_session_connector_used_count": 0
        },
        "outlook": {
          "distinct_session_connector_used_count": 0
        },
        "powerpoint": {
          "distinct_session_connector_used_count": 0
        },
        "word": {
          "distinct_session_connector_used_count": 0
        }
      },
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "read_call_count": 0,
      "unclassified_call_count": 0,
      "user_id": "user_id",
      "write_call_count": 0
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
