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

date: string

UTC date in YYYY-MM-DD format. The day to get user activity for. Must be at least 3 days in the past (data is finalized with a 3-day lag) and no earlier than 2026-01-01.

limit: optional number

Number of results per page (1-1000, default 100).

page: optional string

Opaque cursor from a previous response's next\_page field.

##### ReturnsExpand Collapse



UserActivity object { data, next\_page } 

Response for GET /v1/organizations/analytics/users.



data: array of object { bioscience\_metrics, chat\_metrics, claude\_code\_metrics, 5 more } 



bioscience\_metrics: object { delegation\_count, distinct\_session\_count, message\_count, 2 more } 

Claude Bioscience activity metrics for a single user on a given day.

delegation\_count: number

Number of delegations (handoffs to a specialized agent) in Claude Bioscience sessions

distinct\_session\_count: number

Number of distinct Claude Bioscience sessions. Null on aggregated rows where a distinct count cannot be computed.

message\_count: number

Number of messages sent in Claude Bioscience sessions

remote\_compute\_job\_count: number

Number of remote compute jobs launched from Claude Bioscience sessions

skills\_used\_count: number

Total number of skill invocations in Claude Bioscience sessions



chat\_metrics: object { connectors\_used\_count, distinct\_artifacts\_created\_count, distinct\_connectors\_used\_count, 9 more } 

Claude.ai activity metrics for a single user on a given day.

connectors\_used\_count: number

Number of MCP connector invocations.

distinct\_artifacts\_created\_count: number

Number of distinct artifacts created

distinct\_connectors\_used\_count: number

Distinct claude.ai connectors this user used. Excludes calls whose connector could not be identified and all calls from organizations with zero data retention. Null on aggregated rows where a distinct count cannot be computed.

distinct\_conversation\_count: number

Number of distinct conversations the user participated in. Null on aggregated rows where a distinct count cannot be computed.

distinct\_files\_uploaded\_count: number

Number of distinct files uploaded. Null on aggregated rows where a distinct count cannot be computed.

distinct\_projects\_created\_count: number

Number of distinct projects created

distinct\_projects\_used\_count: number

Number of distinct projects used. Null on aggregated rows where a distinct count cannot be computed.

distinct\_shared\_artifacts\_viewed\_count: number

Number of distinct shared artifacts the user viewed. Null on aggregated rows where a distinct count cannot be computed.

distinct\_skills\_used\_count: number

Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.

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

Number of distinct Claude Code sessions. Null on aggregated rows where a distinct count cannot be computed.

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

cowork\_metrics: object { action\_count, connectors\_used\_count, dispatch\_turn\_count, 5 more } 

Cowork activity metrics for a single user on a given day.

action\_count: number

Number of tool actions completed in Cowork sessions

connectors\_used\_count: number

Total number of connector invocations in Cowork sessions

dispatch\_turn\_count: number

Number of Dispatch (background agent) turns completed

distinct\_connectors\_used\_count: number

Number of distinct connectors used in Cowork sessions. Null on aggregated rows where a distinct count cannot be computed.

distinct\_session\_count: number

Number of distinct Cowork sessions. Null on aggregated rows where a distinct count cannot be computed.

distinct\_skills\_used\_count: number

Number of distinct skills used in Cowork sessions. Null on aggregated rows where a distinct count cannot be computed.

message\_count: number

Number of messages sent in Cowork sessions

skills\_used\_count: number

Total number of skill invocations in Cowork sessions



design\_metrics: object { distinct\_projects\_created\_count, distinct\_projects\_used\_count, distinct\_session\_count, message\_count } 

Claude Design activity metrics for a single user on a given day.

distinct\_projects\_created\_count: number

Number of distinct Claude Design projects created

distinct\_projects\_used\_count: number

Number of distinct Claude Design projects the user worked in. Null on aggregated rows where a distinct count cannot be computed.

distinct\_session\_count: number

Number of distinct Claude Design sessions. Null on aggregated rows where a distinct count cannot be computed.

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

Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.

distinct\_session\_count: number

Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.

distinct\_skills\_used\_count: number

Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.

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

Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.

distinct\_session\_count: number

Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.

distinct\_skills\_used\_count: number

Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.

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

Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.

distinct\_session\_count: number

Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.

distinct\_skills\_used\_count: number

Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.

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

Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.

distinct\_session\_count: number

Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.

distinct\_skills\_used\_count: number

Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.

message\_count: number

Number of messages sent

skills\_used\_count: number

Number of skill invocations

web\_search\_count: number

Number of web searches performed

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
      "bioscience_metrics": {
        "delegation_count": 0,
        "distinct_session_count": 0,
        "message_count": 0,
        "remote_compute_job_count": 0,
        "skills_used_count": 0
      },
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
        "skills_used_count": 0
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
      "web_search_count": 0,
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
      "bioscience_metrics": {
        "delegation_count": 0,
        "distinct_session_count": 0,
        "message_count": 0,
        "remote_compute_job_count": 0,
        "skills_used_count": 0
      },
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
        "skills_used_count": 0
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
      "web_search_count": 0,
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
