# Get project document content

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](manage-claude/compliance-api-access.md)

Copy page



# Get project document content

GET/v1/compliance/apps/projects/documents/{document\_id}

Get detailed information for a specific project document.

##### Path parameters

document\_id: string

The document ID (tagged ID, e.g., claude\_proj\_doc\_abc123)

##### Headers

"x-api-key": optional string

##### Returns

id: string

Project document identifier (tagged ID)

content: string

Document text content



created\_at: string

Document creation timestamp

formatdate-time

filename: string

Document filename



user: object{ id, email\_address } or null

The user who created a project or project document.

Fields that reference this type are null when the creator's account has
been deleted or the creator is no longer a member of an organization the
key may read.

id: string

User identifier (tagged ID)

email\_address: string

User's email address

Get project document content

cURL

```shiki
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```shiki
{
  "id": "claude_proj_doc_01Qr8StUvWxYzAbCdEfGhJjK",
  "content": "# Design notes\n\n- Item one\n- Item two\n",
  "created_at": "2025-03-12T18:22:41.123456Z",
  "filename": "design-notes.txt",
  "user": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "email_address": "jane.doe@example.com"
  }
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "claude_proj_doc_01Qr8StUvWxYzAbCdEfGhJjK",
  "content": "# Design notes\n\n- Item one\n- Item two\n",
  "created_at": "2025-03-12T18:22:41.123456Z",
  "filename": "design-notes.txt",
  "user": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "email_address": "jane.doe@example.com"
  }
}
```

---

*Copyright © Anthropic. All rights reserved.*
