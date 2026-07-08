# List Compliance Group Members

Copy page





To enable the Compliance API, see [Set up the Compliance API](manage-claude/compliance-api-access.md).

# List Compliance Group Members

GET/v1/compliance/groups/{group\_id}/members

List Compliance Group Members

##### Path ParametersExpand Collapse

group\_id: string

The group ID (tagged ID, e.g., rbac\_group\_abc123)

##### Query ParametersExpand Collapse

limit: optional number

Maximum results (default: 500, max: 1000)

page: optional string

Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

##### Header ParametersExpand Collapse

"x-api-key": optional string

##### ReturnsExpand Collapse



data: array of object { created\_at, email, updated\_at, user\_id } 

List of group members

created\_at: string

Membership creation timestamp (ISO 8601)

email: string

Member email address

updated\_at: string

Membership last-updated timestamp (ISO 8601)

user\_id: string

Member user identifier (tagged ID)

has\_more: boolean

Whether more records exist beyond the current result set

next\_page: string

Token to retrieve the next page. Use this as the 'page' parameter in your next request

List Compliance Group Members



```shiki
curl https://api.anthropic.com/v1/compliance/groups/$GROUP_ID/members \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```shiki
{
  "data": [
    {
      "created_at": "2025-03-12T18:22:41.123456",
      "email": "jane.doe@example.com",
      "updated_at": "2025-03-14T09:05:17.456789",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "created_at": "2025-03-12T18:22:41.123456",
      "email": "jane.doe@example.com",
      "updated_at": "2025-03-14T09:05:17.456789",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

---

*Copyright © Anthropic. All rights reserved.*
