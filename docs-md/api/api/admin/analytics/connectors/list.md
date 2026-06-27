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

date: string

UTC date in YYYY-MM-DD format. The day to get connector usage for. Must be at least 3 days in the past (data is finalized with a 3-day lag) and no earlier than 2026-01-01.

limit: optional number

Number of results per page (1-1000, default 100).

page: optional string

Opaque cursor from a previous response's next\_page field.

##### ReturnsExpand Collapse



ConnectorUsage object { data, next\_page } 

Response for GET /v1/organizations/analytics/connectors.



data: array of object { chat\_metrics, claude\_code\_metrics, connector\_name, 3 more } 



chat\_metrics: object { distinct\_conversation\_connector\_used\_count } 

Claude.ai activity metrics for a single connector on a given day.

distinct\_conversation\_connector\_used\_count: number

Number of distinct conversations in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.



claude\_code\_metrics: object { distinct\_session\_connector\_used\_count } 

Claude Code activity metrics for a single connector on a given day.

distinct\_session\_connector\_used\_count: number

Number of distinct Claude Code sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.

connector\_name: string

Name of the connector



cowork\_metrics: object { distinct\_session\_connector\_used\_count } 

Cowork activity metrics for a single connector on a given day.

distinct\_session\_connector\_used\_count: number

Number of distinct Cowork sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.

distinct\_user\_count: number

Number of distinct users who used the connector on the requested day



office\_metrics: object { excel, outlook, powerpoint, word } 

Office Agent activity metrics for a single connector on a given day, broken out by Office product.



excel: [ConnectorOfficeProductMetrics](api/admin/analytics.md) { distinct\_session\_connector\_used\_count } 

Office Agent activity metrics for a single connector on a given day within one Office product.

distinct\_session\_connector\_used\_count: number

Number of distinct Office Agent sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.



outlook: [ConnectorOfficeProductMetrics](api/admin/analytics.md) { distinct\_session\_connector\_used\_count } 

Office Agent activity metrics for a single connector on a given day within one Office product.

distinct\_session\_connector\_used\_count: number

Number of distinct Office Agent sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.



powerpoint: [ConnectorOfficeProductMetrics](api/admin/analytics.md) { distinct\_session\_connector\_used\_count } 

Office Agent activity metrics for a single connector on a given day within one Office product.

distinct\_session\_connector\_used\_count: number

Number of distinct Office Agent sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.



word: [ConnectorOfficeProductMetrics](api/admin/analytics.md) { distinct\_session\_connector\_used\_count } 

Office Agent activity metrics for a single connector on a given day within one Office product.

distinct\_session\_connector\_used\_count: number

Number of distinct Office Agent sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.

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
      }
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
