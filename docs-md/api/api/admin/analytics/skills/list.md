# Get Skill Usage

Copy page



# Get Skill Usage

GET/v1/organizations/analytics/skills

Get per-skill usage for a given day, with cursor-based pagination.

Returns skill usage metrics for the organization, sorted by skill name.
Available to organizations on a Claude Enterprise plan. Requires an API
key with the `read:analytics` scope.

##### Query ParametersExpand Collapse

date: optional string

UTC date in YYYY-MM-DD format. The day to get skill usage for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

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

SkillUsage object { data, next\_page } 

Response for GET /v1/organizations/analytics/skills.



data: array of object { chat\_metrics, claude\_code\_metrics, cowork\_metrics, 14 more } 



chat\_metrics: object { distinct\_conversation\_skill\_used\_count } 

Claude.ai activity metrics for a single skill on a given day.

distinct\_conversation\_skill\_used\_count: number

Number of distinct conversations in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



claude\_code\_metrics: object { distinct\_session\_skill\_used\_count } 

Claude Code activity metrics for a single skill on a given day.

distinct\_session\_skill\_used\_count: number

Number of distinct Claude Code sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



cowork\_metrics: object { distinct\_session\_skill\_used\_count } 

Cowork activity metrics for a single skill on a given day.

distinct\_session\_skill\_used\_count: number

Number of distinct Cowork sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

distinct\_user\_count: number

Number of distinct users who used the skill on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted.



office\_metrics: object { excel, outlook, powerpoint, word } 

Office Agent activity metrics for a single skill on a given day, broken out by Office product.



excel: [SkillOfficeProductMetrics](api/admin/analytics.md) { distinct\_session\_skill\_used\_count } 

Office Agent activity metrics for a single skill on a given day within one Office product.

distinct\_session\_skill\_used\_count: number

Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



outlook: [SkillOfficeProductMetrics](api/admin/analytics.md) { distinct\_session\_skill\_used\_count } 

Office Agent activity metrics for a single skill on a given day within one Office product.

distinct\_session\_skill\_used\_count: number

Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



powerpoint: [SkillOfficeProductMetrics](api/admin/analytics.md) { distinct\_session\_skill\_used\_count } 

Office Agent activity metrics for a single skill on a given day within one Office product.

distinct\_session\_skill\_used\_count: number

Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



word: [SkillOfficeProductMetrics](api/admin/analytics.md) { distinct\_session\_skill\_used\_count } 

Office Agent activity metrics for a single skill on a given day within one Office product.

distinct\_session\_skill\_used\_count: number

Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

skill\_name: string

Name of the skill

attributed\_list\_price: optional string

List-price (rate-card) value of the member requests attributed to this skill, as a decimal string in the minor unit of `currency` (cents for USD), from Claude Code, Cowork, and Office Agent request-level attribution — the value of requests that INVOLVED the skill, not the skill's incremental cost. Unlike estimated\_overage\_spend this reflects usage value regardless of how it was funded — seat-covered usage counts — but it is undiscounted and does NOT tie to billed spend or the organization's spend reporting. claude.ai chat usage carries no request-level attribution and contributes nothing: the field is null on chat product rows and on office\_agent product cuts dated before 2026-06-18 (the Office Agent attribution data-start), and on ungrouped rows it covers the Claude Code + Cowork + Office Agent share only (null when no attributable usage exists). Also null under the same conditions as estimated\_overage\_spend (spend reporting not enabled for this organization, data unavailable). "0" means attributable usage existed but none was attributed to this skill. Addable across days: date-range rollup mode returns the window's sum.

currency: optional "USD"

Currency for this row's monetary fields (estimated\_overage\_spend and attributed\_list\_price), as an uppercase ISO-4217 code. Always "USD" when either amount is populated; null whenever both amounts are null.

enable\_count: optional number

Distinct accounts that enabled this skill on the requested day (claude.ai only — the skill analog of plugin install\_count). The count is org-wide: null when enable reporting is not enabled for this organization, when the request scopes to user\_id / rbac\_group\_id / product via group\_by[] or filter[] (an org-wide count would be misleading on per-cut rows), or when enable data is temporarily unavailable. A distinct count, not an event count: summing across days double-counts members who enable the skill on more than one day, so it is also null in date-range rollup mode (starting\_date/ending\_date).

estimated\_overage\_spend: optional string

Estimated OVERAGE spend attributed to this skill, as a decimal string in the minor unit of `currency` (cents for USD; "1250" is $12.50, fractional cents possible) — an allocation of each member's daily post-discount, pre-credit metered overage spend (the same cost basis as the organization's spend reporting and the Cost & Usage API, so per-skill figures are directly comparable; spend with no skill attribution — including any member-day without skill invocations — is not represented, so skill rows sum to at most those totals) across the skills the member used. Overage only: usage covered by included seat allowances bills nothing and allocates $0 here — see attributed\_list\_price for the funding-independent usage-value companion. Claude Code, Cowork, and Office Agent spend use request-level skill attribution; claude.ai chat spend is approximated proportionally to skill-invoking messages. An estimate, not a billing number — and the cost of the requests/messages that INVOLVED the skill, not the skill's incremental cost (the same request would still have cost something without the skill active). "0" means no overage spend was attributed; null when spend reporting is not enabled for this organization, on office\_agent product cuts dated before 2026-06-18 (the Office Agent attribution data-start), or when spend data is temporarily unavailable. Addable across days: date-range rollup mode (starting\_date/ending\_date) returns the window's sum. With group\_by[]=user\_id each row carries the user's own attributed spend.

invocation\_count: optional number

Total number of times this skill was invoked on the requested day (the skill analog of plugin invocation\_count). Unlike distinct\_user\_count — which answers '# of users' — this is the true '# of uses'. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Null when invocation reporting is not enabled for this organization. Sum across a date range for total uses in the window — date-range rollup mode (starting\_date/ending\_date) returns this sum directly.

product: optional string

Product that produced this row's activity: one of chat, claude\_code, cowork, or office\_agent (the canonical Cost & Usage product naming; an office\_agent row's per-surface breakdown is in its office\_metrics). On /plugins only cowork and claude\_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group\_by[] or filter[] there is rejected). Present only when the request grouped by product.

rbac\_group\_id: optional string

Tagged RBAC group identifier (rbac\_group\_...), matching the spend-limits API spelling. Present only when the request grouped by rbac\_group\_id.

rbac\_group\_name: optional string

Resolved RBAC group display name, alongside rbac\_group\_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac\_group\_id remains the stable key.

share\_status: optional string

Skill share status (claude.ai only): one of 'private', 'organization', or 'public'. Null for skills used only in Claude Code or Office (no per-skill share-status concept) and when share-status reporting is not yet available for the organization. Filterable via filter[]=share\_status:<value>.

skill\_display\_name: optional string

Human-readable display name for rows whose skill\_name is an opaque skill id (user/organization skill types — user-defined names are withheld from the analytics pipeline). Only organization-shared skills resolve; the literal 'unknown' bucket row also gets a fixed 'Unknown skill' label. Null for private (user-defined) skills — their names are not disclosed to analytics-key holders — and null when skill\_name is already a display name, when the skill was deleted, or when display-name resolution is not enabled for this organization.

user\_id: optional string

Tagged user identifier (e.g. user\_...). Present only when the request grouped by user\_id.

next\_page: string

Opaque cursor for the next page, or null if no more results

Get Skill Usage



```shiki
curl https://api.anthropic.com/v1/organizations/analytics/skills \
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
        "distinct_conversation_skill_used_count": 0
      },
      "claude_code_metrics": {
        "distinct_session_skill_used_count": 0
      },
      "cowork_metrics": {
        "distinct_session_skill_used_count": 0
      },
      "distinct_user_count": 0,
      "office_metrics": {
        "excel": {
          "distinct_session_skill_used_count": 0
        },
        "outlook": {
          "distinct_session_skill_used_count": 0
        },
        "powerpoint": {
          "distinct_session_skill_used_count": 0
        },
        "word": {
          "distinct_session_skill_used_count": 0
        }
      },
      "skill_name": "skill_name",
      "attributed_list_price": "attributed_list_price",
      "currency": "USD",
      "enable_count": 0,
      "estimated_overage_spend": "estimated_overage_spend",
      "invocation_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "share_status": "share_status",
      "skill_display_name": "skill_display_name",
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
      "chat_metrics": {
        "distinct_conversation_skill_used_count": 0
      },
      "claude_code_metrics": {
        "distinct_session_skill_used_count": 0
      },
      "cowork_metrics": {
        "distinct_session_skill_used_count": 0
      },
      "distinct_user_count": 0,
      "office_metrics": {
        "excel": {
          "distinct_session_skill_used_count": 0
        },
        "outlook": {
          "distinct_session_skill_used_count": 0
        },
        "powerpoint": {
          "distinct_session_skill_used_count": 0
        },
        "word": {
          "distinct_session_skill_used_count": 0
        }
      },
      "skill_name": "skill_name",
      "attributed_list_price": "attributed_list_price",
      "currency": "USD",
      "enable_count": 0,
      "estimated_overage_spend": "estimated_overage_spend",
      "invocation_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "share_status": "share_status",
      "skill_display_name": "skill_display_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
