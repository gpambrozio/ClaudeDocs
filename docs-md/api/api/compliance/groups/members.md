# Members

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](manage-claude/compliance-api-access.md)

Copy page



# Members

##### [List Compliance Group Members](api/http/compliance/groups/members/list.md)

GET/v1/compliance/groups/{group\_id}/members

##### Models



MemberListResponse object{ created\_at, email, updated\_at, user\_id }

Group member for compliance responses.

created\_at: string or null

Membership creation timestamp (ISO 8601)

email: string

Member email address

updated\_at: string or null

Membership last-updated timestamp (ISO 8601)

user\_id: string

Member user identifier (tagged ID)

---

*Copyright © Anthropic. All rights reserved.*
