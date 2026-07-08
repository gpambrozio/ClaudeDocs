# Attachments

Copy page





To enable the Compliance API, see [Set up the Compliance API](manage-claude/compliance-api-access.md).

# Attachments

##### [List project attachments](api/compliance/apps/projects/attachments/list.md)

GET/v1/compliance/apps/projects/{project\_id}/attachments

##### ModelsExpand Collapse



AttachmentListResponse = object { id, created\_at, filename, 4 more }  or object { id, created\_at, filename, 3 more } 

File attachment reference for compliance responses.

One of the following:



ComplianceProjectFileReference object { id, created\_at, filename, 4 more } 

File attachment reference for compliance responses.

id: string

File identifier (e.g., 'claude\_file\_abcd')

created\_at: string

Creation timestamp (RFC 3339 format)

filename: string

Display name of the file (e.g., 'document.pdf')

md5: string

Lowercase hex MD5 of the file's preferred downloadable variant, when recorded. Null otherwise. Use the per-file `/metadata` endpoint for the authoritative value.

mime\_type: string

MIME type of the file's preferred downloadable variant when one is recorded, else 'application/octet-stream'. Use the per-file `/metadata` endpoint for the authoritative value.

size\_bytes: number

Size in bytes of the file's preferred downloadable variant, when recorded. Null otherwise. Use the per-file `/metadata` endpoint for the authoritative value.

type: "project\_file"

Discriminator marking this as a binary file



ComplianceProjectDocReference object { id, created\_at, filename, 3 more } 

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

updated\_at: string

Last-modified timestamp of the document. Reserved for future use — currently always null.

---

*Copyright © Anthropic. All rights reserved.*
