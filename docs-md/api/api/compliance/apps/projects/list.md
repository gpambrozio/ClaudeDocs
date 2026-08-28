# List projects

Copy page



# List projects

GET/v1/compliance/apps/projects

Lists project metadata with filtering capabilities. Results
are sorted chronologically (time ascending) by created\_at.

##### Query parameters



created\_at: optional object{ gt, gte, lt, lte }



gt: optional string

Filter projects created after this time (RFC 3339 format)

formatdate-time



gte: optional string

Filter projects created at or after this time (RFC 3339 format)

formatdate-time



lt: optional string

Filter projects created before this time (RFC 3339 format)

formatdate-time



lte: optional string

Filter projects created at or before this time (RFC 3339 format)

formatdate-time



limit: optional number

Maximum results (default: 20, max: 100)

default20

maximum100

minimum1

organization\_ids: optional array of string

Filter by organization IDs (accepts `org_...` or organization UUID). Enumerate IDs via `GET /v1/compliance/organizations`.

page: optional string

Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.



updated\_at: optional object{ gt, gte, lt, lte }



gt: optional string

Filter projects updated after this time (RFC 3339 format)

formatdate-time



gte: optional string

Filter projects updated at or after this time (RFC 3339 format)

formatdate-time



lt: optional string

Filter projects updated before this time (RFC 3339 format)

formatdate-time



lte: optional string

Filter projects updated at or before this time (RFC 3339 format)

formatdate-time

user\_ids: optional array of string

Filter by user IDs. Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

##### Headers

"x-api-key": optional string

##### Returns



data: array of object{ id, created\_at, deleted\_at, 6 more }

List of projects sorted by creation date ascending

id: string

Project identifier (tagged ID)



created\_at: string

Project creation timestamp

formatdate-time



deleted\_at: string or null

Timestamp when the project was deleted by an end user, or null otherwise

formatdate-time

is\_private: boolean

If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

name: string

Project name

organization\_uuid: string

Organization UUID this project belongs to



updated\_at: string

Project last update timestamp

formatdate-time



user: object{ id, email\_address } or null

The user who created a project or project document.

Fields that reference this type are null when the creator's account has
been deleted or the creator is no longer a member of an organization the
key may read.

id: string

User identifier (tagged ID)

email\_address: string

User's email address

organization\_id: string⁠Deprecated

Organization identifier (tagged ID)

has\_more: boolean

Whether more records exist beyond the current result set

next\_page: string or null

Token to retrieve the next page. Use this as the 'page' parameter in your next request



### List projects

cURL



```shiki
curl https://api.anthropic.com/v1/compliance/apps/projects \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```shiki
{
  "data": [
    {
      "id": "claude_proj_abc123",
      "name": "Q4 Product Planning",
      "created_at": "2025-06-01T10:00:00Z",
      "updated_at": "2025-06-15T14:30:00Z",
      "is_private": true,
      "organization_id": "org_abc123",
      "organization_uuid": "abc12345-6789-0abc-def0-123456789abc",
      "user": {
        "id": "user_xyz456",
        "email_address": "user@example.com"
      }
    }
  ],
  "has_more": true,
  "next_page": "page_eyJjcmVhdGVkX2F0IjoiMjAyNS0wNi0wMVQxMDowMDowMFoiLCJ1dWlkIjoiYWJjMTIzIn0="
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "id": "claude_proj_abc123",
      "name": "Q4 Product Planning",
      "created_at": "2025-06-01T10:00:00Z",
      "updated_at": "2025-06-15T14:30:00Z",
      "is_private": true,
      "organization_id": "org_abc123",
      "organization_uuid": "abc12345-6789-0abc-def0-123456789abc",
      "user": {
        "id": "user_xyz456",
        "email_address": "user@example.com"
      }
    }
  ],
  "has_more": true,
  "next_page": "page_eyJjcmVhdGVkX2F0IjoiMjAyNS0wNi0wMVQxMDowMDowMFoiLCJ1dWlkIjoiYWJjMTIzIn0="
}
```

---

*Copyright © Anthropic. All rights reserved.*
