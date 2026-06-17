# Get project document content

Copy page





To enable the Compliance API, see [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Get project document content

GET/v1/compliance/apps/projects/documents/{document\_id}

Get detailed information for a specific project document.

##### Path ParametersExpand Collapse

document\_id: string

The document ID (tagged ID, e.g., claude\_proj\_doc\_abc123)

##### Header ParametersExpand Collapse

"x-api-key": optional string

##### ReturnsExpand Collapse

id: string

Project document identifier (tagged ID)

content: string

Document text content

created\_at: string

Document creation timestamp

filename: string

Document filename

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

Get project document content



```shiki
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```shiki
{
  "id": "id",
  "content": "content",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "filename",
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
  "content": "content",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "filename",
  "user": {
    "id": "id",
    "email_address": "email_address"
  }
}
```

---

*Copyright © Anthropic. All rights reserved.*
