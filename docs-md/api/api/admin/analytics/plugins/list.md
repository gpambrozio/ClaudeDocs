# Get Plugin Usage

Copy page



# Get Plugin Usage

GET/v1/organizations/analytics/plugins

Get per-plugin install + invocation usage for a given day, with pagination.

Returns plugin usage metrics for the organization across Cowork and Claude
Code, sorted by plugin name. The `plugin_name` value `third-party` is
an aggregate bucket, not a plugin: it collects plugin activity, from
either surface, for which the reporting client did not provide a plugin
name — so an organization's own plugins can contribute both to their own
named rows and to this bucket. Use `group_by[]` to break usage out per
member, per RBAC group, or per product surface (Cowork / Claude Code),
and `filter[]` to scope results; the parameter descriptions list the
supported dimensions. Requires an API key with the
`read:analytics` scope. `starting_date` / `ending_date` select
range-rollup mode like `/skills`.

##### Query parameters



date: optional string

UTC date in YYYY-MM-DD format. The day to get plugin usage for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

formatdate



ending\_date: optional string

UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with `starting_date`. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after `starting_date`.

formatdate



filter: optional array of string

Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `plugin_name`, `product`, `rbac_group_id`, `user_id`. Value forms: `plugin_name` matches case-insensitively; `product` is `claude_code` or `cowork` (the only surfaces with plugin attribution); `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries.

maxItems100



group\_by: optional array of "product" or "rbac\_group\_id" or "user\_id"

Dimensions to break results out by (e.g. `group_by[]=user_id`). Supported on this endpoint: `product`, `rbac_group_id`, `user_id`. On this endpoint `product` takes the values `claude_code` or `cowork` only (the surfaces with plugin attribution). Grouped rows carry the requested dimension values as additional fields and paginate like ungrouped responses via `next_page`; an unsupported dimension returns 400. `rbac_group_id` attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

maxItems100

One of the following:

"product"

"rbac\_group\_id"

"user\_id"



limit: optional number

Number of results per page (1-1000, default 100).

minimum1

maximum1000



order: optional "asc" or "desc"

Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

One of the following:

"asc"

"desc"

order\_by: optional string

Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

page: optional string

Opaque cursor from a previous response's `next_page` field.



starting\_date: optional string

UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either `date` or `starting_date`, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

formatdate

##### Returns



PluginUsage object{ data, next\_page }

Response for GET /v1/organizations/analytics/plugins.



### Get Plugin Usage

cURL



```shiki
curl https://api.anthropic.com/v1/organizations/analytics/plugins \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

Response 200



```shiki
{
  "data": [
    {
      "claude_code_metrics": {
        "distinct_session_plugin_used_count": 0
      },
      "cowork_metrics": {
        "distinct_session_plugin_used_count": 0
      },
      "distinct_user_count": 0,
      "install_count": 0,
      "invocation_count": 0,
      "plugin_name": "plugin_name",
      "plugin_id": "plugin_id",
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
      "claude_code_metrics": {
        "distinct_session_plugin_used_count": 0
      },
      "cowork_metrics": {
        "distinct_session_plugin_used_count": 0
      },
      "distinct_user_count": 0,
      "install_count": 0,
      "invocation_count": 0,
      "plugin_name": "plugin_name",
      "plugin_id": "plugin_id",
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
