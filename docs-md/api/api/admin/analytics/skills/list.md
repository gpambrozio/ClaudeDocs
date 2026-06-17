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

date: string

UTC date in YYYY-MM-DD format. The day to get skill usage for. Must be at least 3 days in the past (data is finalized with a 3-day lag) and no earlier than 2026-01-01.

limit: optional number

Number of results per page (1-1000, default 100).

page: optional string

Opaque cursor from a previous response's next\_page field.

##### ReturnsExpand Collapse



SkillUsage object { data, next\_page } 

Response for GET /v1/organizations/analytics/skills.



data: array of object { chat\_metrics, claude\_code\_metrics, cowork\_metrics, 3 more } 



chat\_metrics: object { distinct\_conversation\_skill\_used\_count } 

Claude.ai activity metrics for a single skill on a given day.

distinct\_conversation\_skill\_used\_count: number

Number of distinct conversations in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.



claude\_code\_metrics: object { distinct\_session\_skill\_used\_count } 

Claude Code activity metrics for a single skill on a given day.

distinct\_session\_skill\_used\_count: number

Number of distinct Claude Code sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.



cowork\_metrics: object { distinct\_session\_skill\_used\_count } 

Cowork activity metrics for a single skill on a given day.

distinct\_session\_skill\_used\_count: number

Number of distinct Cowork sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.

distinct\_user\_count: number

Number of distinct users who used the skill on the requested day



office\_metrics: object { excel, outlook, powerpoint, word } 

Office Agent activity metrics for a single skill on a given day, broken out by Office product.



excel: [SkillOfficeProductMetrics](api/admin.md) { distinct\_session\_skill\_used\_count } 

Office Agent activity metrics for a single skill on a given day within one Office product.

distinct\_session\_skill\_used\_count: number

Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.



outlook: [SkillOfficeProductMetrics](api/admin.md) { distinct\_session\_skill\_used\_count } 

Office Agent activity metrics for a single skill on a given day within one Office product.

distinct\_session\_skill\_used\_count: number

Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.



powerpoint: [SkillOfficeProductMetrics](api/admin.md) { distinct\_session\_skill\_used\_count } 

Office Agent activity metrics for a single skill on a given day within one Office product.

distinct\_session\_skill\_used\_count: number

Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.



word: [SkillOfficeProductMetrics](api/admin.md) { distinct\_session\_skill\_used\_count } 

Office Agent activity metrics for a single skill on a given day within one Office product.

distinct\_session\_skill\_used\_count: number

Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.

skill\_name: string

Name of the skill

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
      "skill_name": "skill_name"
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
      "skill_name": "skill_name"
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
