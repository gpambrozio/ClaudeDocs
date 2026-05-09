# Users

Copy page

The Compliance API is available only on the Claude Enterprise plan and must be enabled before use. See [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Users

##### [List organization users](api/compliance/organizations/users/list.md)

GET/v1/compliance/organizations/{org\_uuid}/users

##### ModelsExpand Collapse

UserListResponse = object { id, created\_at, email, full\_name }

User member information for compliance responses.

id: string

User identifier (tagged ID)

created\_at: string

User account creation timestamp

email: string

User's current email address

full\_name: string

User's current full name

---

*Copyright © Anthropic. All rights reserved.*
