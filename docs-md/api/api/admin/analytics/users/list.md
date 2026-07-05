# List User Activity

Copy page



# List User Activity

GET/v1/organizations/analytics/users

Get per-user activity for a given day, with cursor-based pagination.

Returns activity metrics for each user in the organization, sorted by email
address. Available to organizations on a Claude Enterprise plan. Requires
an API key with the `read:analytics` scope.

##### Query ParametersExpand Collapse

date: optional string

UTC date in YYYY-MM-DD format. The day to get user activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

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

UserActivity object { data, next\_page } 

Response for GET /v1/organizations/analytics/users.



data: array of object { chat\_metrics, claude\_code\_metrics, cowork\_metrics, 9 more } 



chat\_metrics: object { connectors\_used\_count, distinct\_artifacts\_created\_count, distinct\_connectors\_used\_count, 9 more } 

Claude.ai activity metrics for a single user on a given day.

connectors\_used\_count: number

Number of MCP connector invocations.

distinct\_artifacts\_created\_count: number

Number of distinct artifacts created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

distinct\_connectors\_used\_count: number

Distinct claude.ai connectors this user used. Excludes calls whose connector could not be identified and all calls from organizations with zero data retention. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

distinct\_conversation\_count: number

Number of distinct conversations the user participated in. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

distinct\_files\_uploaded\_count: number

Number of distinct files uploaded. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

distinct\_projects\_created\_count: number

Number of distinct projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

distinct\_projects\_used\_count: number

Number of distinct projects used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

distinct\_shared\_artifacts\_viewed\_count: number

Number of distinct shared artifacts the user viewed. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

distinct\_skills\_used\_count: number

Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

message\_count: number

Number of messages sent

shared\_conversations\_viewed\_count: number

Number of times the user opened a shared conversation in a project

thinking\_message\_count: number

Number of messages that used extended thinking



claude\_code\_metrics: object { core\_metrics, tool\_actions } 

Claude Code activity metrics for a single user on a given day.



core\_metrics: object { commit\_count, distinct\_session\_count, lines\_of\_code, pull\_request\_count } 

Core Claude Code activity metrics for a single user on a given day.

commit\_count: number

Number of commits made via Claude Code

distinct\_session\_count: number

Number of distinct Claude Code sessions. On aggregated rows and in date-range mode: summed per-day distinct counts. A session essentially never spans a UTC day, so the sum is in practice the true distinct count.



lines\_of\_code: object { added\_count, removed\_count } 

Lines of code added and removed via Claude Code.

added\_count: number

Lines of code added

removed\_count: number

Lines of code removed

pull\_request\_count: number

Number of pull requests created via Claude Code



tool\_actions: object { edit\_tool, multi\_edit\_tool, notebook\_edit\_tool, write\_tool } 

Per-tool accepted/rejected counts for Claude Code file modification tools.



edit\_tool: [ToolActionCounts](api/admin/analytics.md) { accepted\_count, rejected\_count } 

Accepted/rejected counts for a single Claude Code tool type.

accepted\_count: number

Number of tool proposals accepted

rejected\_count: number

Number of tool proposals rejected



multi\_edit\_tool: [ToolActionCounts](api/admin/analytics.md) { accepted\_count, rejected\_count } 

Accepted/rejected counts for a single Claude Code tool type.

accepted\_count: number

Number of tool proposals accepted

rejected\_count: number

Number of tool proposals rejected



notebook\_edit\_tool: [ToolActionCounts](api/admin/analytics.md) { accepted\_count, rejected\_count } 

Accepted/rejected counts for a single Claude Code tool type.

accepted\_count: number

Number of tool proposals accepted

rejected\_count: number

Number of tool proposals rejected



write\_tool: [ToolActionCounts](api/admin/analytics.md) { accepted\_count, rejected\_count } 

Accepted/rejected counts for a single Claude Code tool type.

accepted\_count: number

Number of tool proposals accepted

rejected\_count: number

Number of tool proposals rejected



cowork\_metrics: object { action\_count, connectors\_used\_count, dispatch\_turn\_count, 13 more } 

Cowork activity metrics for a single user on a given day.

action\_count: number

Number of tool actions completed in Cowork sessions

connectors\_used\_count: number

Total number of connector invocations in Cowork sessions

dispatch\_turn\_count: number

Number of Dispatch (background agent) turns completed

distinct\_connectors\_used\_count: number

Number of distinct connectors used in Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

distinct\_session\_count: number

Number of distinct Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

distinct\_skills\_used\_count: number

Number of distinct skills used in Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

message\_count: number

Number of messages sent in Cowork sessions

skills\_used\_count: number

Total number of skill invocations in Cowork sessions

distinct\_plugins\_used\_count: optional number

Number of distinct plugins used in Cowork sessions. Null while Cowork plugin-use metrics are not enabled for this organization. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

edit\_tool\_count: optional number

Number of successful Edit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

file\_edit\_count: optional number

Number of successful file-edit tool calls (Edit, MultiEdit, Write, NotebookEdit) in Cowork sessions. Null, never 0, while the file-edit metrics are not enabled for this organization.

multi\_edit\_tool\_count: optional number

Number of successful MultiEdit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

notebook\_edit\_tool\_count: optional number

Number of successful NotebookEdit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

plugins\_used\_count: optional number

Total number of plugin invocations in Cowork sessions. Null while Cowork plugin-use metrics are not enabled for this organization.

sessions\_with\_file\_edits\_count: optional number

Number of distinct Cowork sessions with at least one successful file-edit tool call. Null while the file-edit metrics are not enabled for this organization. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

write\_tool\_count: optional number

Number of successful Write tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.



design\_metrics: object { distinct\_projects\_created\_count, distinct\_projects\_used\_count, distinct\_session\_count, message\_count } 

Claude Design activity metrics for a single user on a given day.

distinct\_projects\_created\_count: number

Number of distinct Claude Design projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

distinct\_projects\_used\_count: number

Number of distinct Claude Design projects the user worked in. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

distinct\_session\_count: number

Number of distinct Claude Design sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

message\_count: number

Number of messages sent in Claude Design sessions



office\_metrics: object { excel, outlook, powerpoint, word } 

Office Agent activity metrics for a single user on a given day, broken out by Office product.



excel: [OfficeProductMetrics](api/admin/analytics.md) { connectors\_used\_count, distinct\_connectors\_used\_count, distinct\_session\_count, 3 more } 

Office Agent activity metrics for a single user on a given day within one Office product.

connectors\_used\_count: number

Number of MCP connector invocations

distinct\_connectors\_used\_count: number

Number of distinct MCP connectors used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

distinct\_session\_count: number

Number of distinct Office Agent sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

distinct\_skills\_used\_count: number

Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

message\_count: number

Number of messages sent

skills\_used\_count: number

Number of skill invocations



outlook: [OfficeProductMetrics](api/admin/analytics.md) { connectors\_used\_count, distinct\_connectors\_used\_count, distinct\_session\_count, 3 more } 

Office Agent activity metrics for a single user on a given day within one Office product.

connectors\_used\_count: number

Number of MCP connector invocations

distinct\_connectors\_used\_count: number

Number of distinct MCP connectors used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

distinct\_session\_count: number

Number of distinct Office Agent sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

distinct\_skills\_used\_count: number

Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

message\_count: number

Number of messages sent

skills\_used\_count: number

Number of skill invocations



powerpoint: [OfficeProductMetrics](api/admin/analytics.md) { connectors\_used\_count, distinct\_connectors\_used\_count, distinct\_session\_count, 3 more } 

Office Agent activity metrics for a single user on a given day within one Office product.

connectors\_used\_count: number

Number of MCP connector invocations

distinct\_connectors\_used\_count: number

Number of distinct MCP connectors used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

distinct\_session\_count: number

Number of distinct Office Agent sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

distinct\_skills\_used\_count: number

Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

message\_count: number

Number of messages sent

skills\_used\_count: number

Number of skill invocations



word: [OfficeProductMetrics](api/admin/analytics.md) { connectors\_used\_count, distinct\_connectors\_used\_count, distinct\_session\_count, 3 more } 

Office Agent activity metrics for a single user on a given day within one Office product.

connectors\_used\_count: number

Number of MCP connector invocations

distinct\_connectors\_used\_count: number

Number of distinct MCP connectors used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

distinct\_session\_count: number

Number of distinct Office Agent sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

distinct\_skills\_used\_count: number

Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

message\_count: number

Number of messages sent

skills\_used\_count: number

Number of skill invocations



science\_metrics: object { delegation\_count, distinct\_session\_count, message\_count, 2 more } 

Claude Science activity metrics for a single user on a given day.

delegation\_count: number

Number of delegations (handoffs to a specialized agent) in Claude Science sessions

distinct\_session\_count: number

Number of distinct Claude Science sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

message\_count: number

Number of messages sent in Claude Science sessions

remote\_compute\_job\_count: number

Number of remote compute jobs launched from Claude Science sessions

skills\_used\_count: number

Total number of skill invocations in Claude Science sessions

web\_search\_count: number

Number of web searches performed

distinct\_user\_count: optional number

Number of distinct active users represented by this row. Only set for grouped rollups (group\_by[]); null for per-user rows. In date-range mode, recomputed as an exact distinct count of the group's active members over the requested window, never a sum of per-day values.

last\_activity\_date: optional string

Most recent UTC day (YYYY-MM-DD) on which the user had any counted activity, within the requested window: equal to the requested date in single-day mode, and to the latest active day in [starting\_date, ending\_date) in date-range rollup mode — never a day earlier than the window start. On filtered requests (filter[]) only days matching the filter count: with filter[]=rbac\_group\_id it is the last day the user was active while a member of that group, consistent with the row's other metrics. Null on grouped (group\_by[]) rows. Omitted from the response while last-activity reporting is not enabled for this organization.

rbac\_group\_id: optional string

Tagged RBAC group identifier (rbac\_group\_...), matching the spend-limits API spelling. Present only when the request grouped by rbac\_group\_id.

rbac\_group\_name: optional string

Resolved RBAC group display name, alongside rbac\_group\_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac\_group\_id remains the stable key.



user: optional [AnalyticsUser](api/admin/analytics.md) { id, email\_address } 

User identifier.

id: string

Tagged user identifier (e.g. user\_...)

email\_address: string

Email address of the user

next\_page: string

Opaque cursor for the next page, or null if no more results

List User Activity



```shiki
curl https://api.anthropic.com/v1/organizations/analytics/users \
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
        "connectors_used_count": 0,
        "distinct_artifacts_created_count": 0,
        "distinct_connectors_used_count": 0,
        "distinct_conversation_count": 0,
        "distinct_files_uploaded_count": 0,
        "distinct_projects_created_count": 0,
        "distinct_projects_used_count": 0,
        "distinct_shared_artifacts_viewed_count": 0,
        "distinct_skills_used_count": 0,
        "message_count": 0,
        "shared_conversations_viewed_count": 0,
        "thinking_message_count": 0
      },
      "claude_code_metrics": {
        "core_metrics": {
          "commit_count": 0,
          "distinct_session_count": 0,
          "lines_of_code": {
            "added_count": 0,
            "removed_count": 0
          },
          "pull_request_count": 0
        },
        "tool_actions": {
          "edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "multi_edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "notebook_edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "write_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          }
        }
      },
      "cowork_metrics": {
        "action_count": 0,
        "connectors_used_count": 0,
        "dispatch_turn_count": 0,
        "distinct_connectors_used_count": 0,
        "distinct_session_count": 0,
        "distinct_skills_used_count": 0,
        "message_count": 0,
        "skills_used_count": 0,
        "distinct_plugins_used_count": 0,
        "edit_tool_count": 0,
        "file_edit_count": 0,
        "multi_edit_tool_count": 0,
        "notebook_edit_tool_count": 0,
        "plugins_used_count": 0,
        "sessions_with_file_edits_count": 0,
        "write_tool_count": 0
      },
      "design_metrics": {
        "distinct_projects_created_count": 0,
        "distinct_projects_used_count": 0,
        "distinct_session_count": 0,
        "message_count": 0
      },
      "office_metrics": {
        "excel": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "outlook": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "powerpoint": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "word": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        }
      },
      "science_metrics": {
        "delegation_count": 0,
        "distinct_session_count": 0,
        "message_count": 0,
        "remote_compute_job_count": 0,
        "skills_used_count": 0
      },
      "web_search_count": 0,
      "distinct_user_count": 0,
      "last_activity_date": "last_activity_date",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user": {
        "id": "id",
        "email_address": "email_address"
      }
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
        "connectors_used_count": 0,
        "distinct_artifacts_created_count": 0,
        "distinct_connectors_used_count": 0,
        "distinct_conversation_count": 0,
        "distinct_files_uploaded_count": 0,
        "distinct_projects_created_count": 0,
        "distinct_projects_used_count": 0,
        "distinct_shared_artifacts_viewed_count": 0,
        "distinct_skills_used_count": 0,
        "message_count": 0,
        "shared_conversations_viewed_count": 0,
        "thinking_message_count": 0
      },
      "claude_code_metrics": {
        "core_metrics": {
          "commit_count": 0,
          "distinct_session_count": 0,
          "lines_of_code": {
            "added_count": 0,
            "removed_count": 0
          },
          "pull_request_count": 0
        },
        "tool_actions": {
          "edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "multi_edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "notebook_edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "write_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          }
        }
      },
      "cowork_metrics": {
        "action_count": 0,
        "connectors_used_count": 0,
        "dispatch_turn_count": 0,
        "distinct_connectors_used_count": 0,
        "distinct_session_count": 0,
        "distinct_skills_used_count": 0,
        "message_count": 0,
        "skills_used_count": 0,
        "distinct_plugins_used_count": 0,
        "edit_tool_count": 0,
        "file_edit_count": 0,
        "multi_edit_tool_count": 0,
        "notebook_edit_tool_count": 0,
        "plugins_used_count": 0,
        "sessions_with_file_edits_count": 0,
        "write_tool_count": 0
      },
      "design_metrics": {
        "distinct_projects_created_count": 0,
        "distinct_projects_used_count": 0,
        "distinct_session_count": 0,
        "message_count": 0
      },
      "office_metrics": {
        "excel": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "outlook": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "powerpoint": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "word": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        }
      },
      "science_metrics": {
        "delegation_count": 0,
        "distinct_session_count": 0,
        "message_count": 0,
        "remote_compute_job_count": 0,
        "skills_used_count": 0
      },
      "web_search_count": 0,
      "distinct_user_count": 0,
      "last_activity_date": "last_activity_date",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user": {
        "id": "id",
        "email_address": "email_address"
      }
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
