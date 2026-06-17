# Get project details

Copy page





To enable the Compliance API, see [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Get project details

GET/v1/compliance/apps/projects/{project\_id}

Get detailed information for a specific project.

##### Path ParametersExpand Collapse

project\_id: string

The project ID (tagged ID, e.g., claude\_proj\_abc123)

##### Header ParametersExpand Collapse

"x-api-key": optional string

##### ReturnsExpand Collapse

id: string

Project identifier (tagged ID)

attachments\_count: number

Number of attachments contained within this project

chats\_count: number

Number of chats contained within this project

created\_at: string

Project creation timestamp

deleted\_at: string

Timestamp when the project was deleted by an end user, or null otherwise

description: string

Project description

instructions: string

Project's custom instructions / prompt

is\_private: boolean

If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

name: string

Project name

Deprecatedorganization\_id: string

Organization identifier (tagged ID)

organization\_uuid: string

Organization UUID this project belongs to

updated\_at: string

Project last update timestamp



user: object { id, email\_address } 

The user who created a project or project document.

Fields that reference this type are null when the creator's account has
been deleted or the creator is no longer a member of any organization
under the parent organization.

id: string

User identifier (tagged ID)

email\_address: string

User's email address

Get project details



```shiki
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```shiki
{
  "id": "id",
  "attachments_count": 0,
  "chats_count": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "instructions": "instructions",
  "is_private": true,
  "name": "name",
  "organization_id": "organization_id",
  "organization_uuid": "organization_uuid",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "user": {
    "id": "id",
    "email_address": "email_address"
  }
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "id",
  "attachments_count": 0,
  "chats_count": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "instructions": "instructions",
  "is_private": true,
  "name": "name",
  "organization_id": "organization_id",
  "organization_uuid": "organization_uuid",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "user": {
    "id": "id",
    "email_address": "email_address"
  }
}
```

---

*Copyright © Anthropic. All rights reserved.*
