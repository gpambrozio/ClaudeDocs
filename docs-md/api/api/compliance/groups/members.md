# Members

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](manage-claude/compliance-activity-feed.md) only. See [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Members

##### [List Compliance Group Members](api/compliance/groups/members/list.md)

GET/v1/compliance/groups/{group\_id}/members

##### ModelsExpand Collapse

MemberListResponse object { created\_at, email, updated\_at, user\_id }

Group member for compliance responses.

created\_at: string

Membership creation timestamp (ISO 8601)

email: string

Member email address

updated\_at: string

Membership last-updated timestamp (ISO 8601)

user\_id: string

Member user identifier (tagged ID)

---

*Copyright © Anthropic. All rights reserved.*
