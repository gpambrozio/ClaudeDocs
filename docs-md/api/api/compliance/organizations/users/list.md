# List organization users

Copy page



# List organization users

GET/v1/compliance/organizations/{org\_uuid}/users

List current user members of an organization.

##### Path parameters

org\_uuid: string

The organization UUID

##### Query parameters



limit: optional number

Maximum results (default: 500, max: 1000)

default500

maximum1000

minimum1

page: optional string

Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

##### Headers

"x-api-key": optional string

##### Returns



data: array of object{ id, created\_at, email, 2 more }

List of current organization members sorted by organization join date ascending

id: string

User identifier (tagged ID)



created\_at: string

User account creation timestamp

formatdate-time

email: string

User's current email address

full\_name: string

User's current full name



organization\_role: "admin" or "billing" or "claude\_code\_user" or 6 more

User's built-in role within the organization. This is distinct from any custom RBAC roles that may also be assigned.

One of the following:

"admin"

"billing"

"claude\_code\_user"

"developer"

"managed"

"membership\_admin"

"owner"

"primary\_owner"

"user"

has\_more: boolean

Whether more records exist beyond the current result set

next\_page: string or null

Token to retrieve the next page. Use this as the 'page' parameter in your next request

### List organization users

cURL



```shiki
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/users \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```shiki
{
  "data": [
    {
      "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "created_at": "2025-03-12T18:22:41.123456Z",
      "email": "jane.doe@example.com",
      "full_name": "Jane Doe",
      "organization_role": "admin"
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
      "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "created_at": "2025-03-12T18:22:41.123456Z",
      "email": "jane.doe@example.com",
      "full_name": "Jane Doe",
      "organization_role": "admin"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

---

*Copyright © Anthropic. All rights reserved.*
