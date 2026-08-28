# Documents

Copy page



# Documents

##### [Get project document content](api/http/compliance/apps/projects/documents/retrieve.md)

GET/v1/compliance/apps/projects/documents/{document\_id}

##### [Get project document metadata](api/http/compliance/apps/projects/documents/metadata.md)

GET/v1/compliance/apps/projects/documents/{document\_id}/metadata

##### [Delete project document](api/http/compliance/apps/projects/documents/delete.md)

DELETE/v1/compliance/apps/projects/documents/{document\_id}

##### Models



DocumentRetrieveResponse object{ id, content, created\_at, 2 more }

Project document information for compliance responses.

id: string

Project document identifier (tagged ID)

content: string

Document text content



created\_at: string

Document creation timestamp

formatdate-time

filename: string

Document filename

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



DocumentDeleteResponse object{ id, type }

Response for deleting a project document.

id: string

The ID of the project document that was deleted



type: "claude\_project\_document\_deleted"

Constant string confirming deletion.

defaultclaude\_project\_document\_deleted



DocumentMetadataResponse object{ id, claude\_project\_id, created\_at, 5 more }

Project document metadata for GET /v1/compliance/apps/projects/documents/{document\_id}/metadata.

Returns metadata only. Use the sibling endpoint (without `/metadata`)
to fetch the document text content.

---

*Copyright © Anthropic. All rights reserved.*
