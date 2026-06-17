# Attachments

Copy page





To enable the Compliance API, see [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Attachments

##### [List project attachments](api/compliance/apps/projects/attachments/list.md)

GET/v1/compliance/apps/projects/{project\_id}/attachments

##### ModelsExpand Collapse



AttachmentListResponse = object { id, created\_at, filename, 2 more }  or object { id, created\_at, filename, 2 more } 

File attachment reference for compliance responses.

One of the following:



ComplianceProjectFileReference object { id, created\_at, filename, 2 more } 

File attachment reference for compliance responses.

id: string

File identifier (e.g., 'claude\_file\_abcd')

created\_at: string

Creation timestamp (RFC 3339 format)

filename: string

Display name of the file (e.g., 'document.pdf')

mime\_type: string

MIME type of the file when it was uploaded (e.g., 'application/pdf')

type: "project\_file"

Discriminator marking this as a binary file



ComplianceProjectDocReference object { id, created\_at, filename, 2 more } 

Project document attachment reference for compliance responses.

id: string

Project document identifier (e.g., 'claude\_proj\_doc\_abcd')

created\_at: string

Creation timestamp (RFC 3339 format)

filename: string

Display name of the document (e.g., 'document.txt')

mime\_type: "text/plain"

MIME type of the project document, always set to plain text

type: "project\_doc"

Discriminator marking this as a plain text document

---

*Copyright © Anthropic. All rights reserved.*
