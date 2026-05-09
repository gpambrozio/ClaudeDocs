# Groups

Copy page

The Compliance API is available only on the Claude Enterprise plan and must be enabled before use. See [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Groups

##### [List Compliance Groups](api/compliance/groups/list.md)

GET/v1/compliance/groups

##### [Get Compliance Group](api/compliance/groups/retrieve.md)

GET/v1/compliance/groups/{group\_id}

##### ModelsExpand Collapse

GroupListResponse = object { id, created\_at, description, 4 more }

Group information for compliance responses.

id: string

Group identifier (tagged ID)

created\_at: string

Group creation timestamp (ISO 8601)

description: string

Group description

name: string

Group name

roles: array of string

Role IDs assigned to this group.

source\_type: string

How the group was created ('direct' or 'scim')

updated\_at: string

Group last-updated timestamp (ISO 8601)

GroupRetrieveResponse = object { id, created\_at, description, 4 more }

Group information for compliance responses.

id: string

Group identifier (tagged ID)

created\_at: string

Group creation timestamp (ISO 8601)

description: string

Group description

name: string

Group name

roles: array of string

Role IDs assigned to this group.

source\_type: string

How the group was created ('direct' or 'scim')

updated\_at: string

Group last-updated timestamp (ISO 8601)

#### GroupsMembers

##### [List Compliance Group Members](api/compliance/groups/members/list.md)

GET/v1/compliance/groups/{group\_id}/members

##### ModelsExpand Collapse

MemberListResponse = object { created\_at, email, updated\_at, user\_id }

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
