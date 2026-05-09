# Documents

Copy page

The Compliance API is available only on the Claude Enterprise plan and must be enabled before use. See [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Documents

##### [Get project document content](api/compliance/apps/projects/documents/retrieve.md)

GET/v1/compliance/apps/projects/documents/{document\_id}

##### [Delete project document](api/compliance/apps/projects/documents/delete.md)

DELETE/v1/compliance/apps/projects/documents/{document\_id}

##### ModelsExpand Collapse

DocumentRetrieveResponse = object { id, content, created\_at, 2 more }

Project document information for compliance responses.

id: string

Project document identifier (tagged ID)

content: string

Document text content

created\_at: string

Document creation timestamp

filename: string

Document filename

user: object { id, email\_address }

User information for project creator.

id: string

User identifier (tagged ID)

email\_address: string

User's email address

DocumentDeleteResponse = object { id, type }

Response for deleting a project document.

id: string

The ID of the project document that was deleted

type: "claude\_project\_document\_deleted"

Constant string confirming deletion.

---

*Copyright © Anthropic. All rights reserved.*
