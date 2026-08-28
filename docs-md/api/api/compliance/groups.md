# Groups

Copy page



# Groups

##### [List Compliance Groups](api/http/compliance/groups/list.md)

GET/v1/compliance/groups

##### [Get Compliance Group](api/http/compliance/groups/retrieve.md)

GET/v1/compliance/groups/{group\_id}

##### Models



GroupRetrieveResponse object{ id, created\_at, description, 4 more }

Group information for compliance responses.

id: string

Group identifier (tagged ID)

created\_at: string or null

Group creation timestamp (ISO 8601)

description: string

Group description

name: string

Group name

roles: array of string or null

Role IDs assigned to this group.

source\_type: string

How the group was created ('direct' or 'scim')

updated\_at: string or null

Group last-updated timestamp (ISO 8601)



GroupListResponse object{ id, created\_at, description, 4 more }

Group information for compliance responses.

id: string

Group identifier (tagged ID)

created\_at: string or null

Group creation timestamp (ISO 8601)

description: string

Group description

name: string

Group name

roles: array of string or null

Role IDs assigned to this group.

source\_type: string

How the group was created ('direct' or 'scim')

updated\_at: string or null

Group last-updated timestamp (ISO 8601)

#### Groups[Members](api/http/compliance/groups/members.md)

##### [List Compliance Group Members](api/http/compliance/groups/members/list.md)

GET/v1/compliance/groups/{group\_id}/members

---

*Copyright © Anthropic. All rights reserved.*
