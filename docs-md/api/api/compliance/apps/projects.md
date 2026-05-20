# Projects

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](manage-claude/compliance-activity-feed.md) only. See [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Projects

##### [List projects](api/compliance/apps/projects/list.md)

GET/v1/compliance/apps/projects

##### [Get project details](api/compliance/apps/projects/retrieve.md)

GET/v1/compliance/apps/projects/{project\_id}

##### [Delete project](api/compliance/apps/projects/delete.md)

DELETE/v1/compliance/apps/projects/{project\_id}

##### ModelsExpand Collapse

ProjectListResponse = object { id, created\_at, deleted\_at, 6 more }

Project information for compliance responses.

id: string

Project identifier (tagged ID)

created\_at: string

Project creation timestamp

deleted\_at: string

Timestamp when the project was deleted by an end user, or null otherwise

is\_private: boolean

If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

name: string

Project name

Deprecatedorganization\_id: string

Organization identifier (tagged ID)

organization\_uuid: string

Organization UUID this project belongs to

updated\_at: string

Project last update timestamp

user: object { id, email\_address }

User information for project creator.

id: string

User identifier (tagged ID)

email\_address: string

User's email address

ProjectRetrieveResponse = object { id, attachments\_count, chats\_count, 10 more }

Detailed project information for compliance responses.

id: string

Project identifier (tagged ID)

attachments\_count: number

Number of attachments contained within this project

chats\_count: number

Number of chats contained within this project

created\_at: string

Project creation timestamp

deleted\_at: string

Timestamp when the project was deleted by an end user, or null otherwise

description: string

Project description

instructions: string

Project's custom instructions / prompt

is\_private: boolean

If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

name: string

Project name

Deprecatedorganization\_id: string

Organization identifier (tagged ID)

organization\_uuid: string

Organization UUID this project belongs to

updated\_at: string

Project last update timestamp

user: object { id, email\_address }

User information for project creator.

id: string

User identifier (tagged ID)

email\_address: string

User's email address

ProjectDeleteResponse = object { id, type }

Response for deleting a Claude project.

id: string

The ID of the Claude project that was deleted

type: optional "claude\_project\_deleted"

Constant string confirming deletion.

#### ProjectsAttachments

##### [List project attachments](api/compliance/apps/projects/attachments/list.md)

GET/v1/compliance/apps/projects/{project\_id}/attachments

##### ModelsExpand Collapse

AttachmentListResponse = object { id, created\_at, filename, 2 more }  or object { id, created\_at, filename, 2 more }

File attachment reference for compliance responses.

Accepts one of the following:

ComplianceProjectFileReference = object { id, created\_at, filename, 2 more }

File attachment reference for compliance responses.

id: string

File identifier (e.g., 'claude\_file\_abcd')

created\_at: string

Creation timestamp (RFC 3339 format)

filename: string

Display name of the file (e.g., 'document.pdf')

mime\_type: string

MIME type of the file when it was uploaded (e.g., 'application/pdf')

type: "project\_file"

Discriminator marking this as a binary file

ComplianceProjectDocReference = object { id, created\_at, filename, 2 more }

Project document attachment reference for compliance responses.

id: string

Project document identifier (e.g., 'claude\_proj\_doc\_abcd')

created\_at: string

Creation timestamp (RFC 3339 format)

filename: string

Display name of the document (e.g., 'document.txt')

mime\_type: "text/plain"

MIME type of the project document, always set to plain text

type: "project\_doc"

Discriminator marking this as a plain text document

#### ProjectsDocuments

##### [Get project document content](api/compliance/apps/projects/documents/retrieve.md)

GET/v1/compliance/apps/projects/documents/{document\_id}

##### [Get project document metadata](api/compliance/apps/projects/documents/metadata.md)

GET/v1/compliance/apps/projects/documents/{document\_id}/metadata

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

DocumentMetadataResponse = object { id, claude\_project\_id, created\_at, 5 more }

Project document metadata for GET /v1/compliance/apps/projects/documents/{document\_id}/metadata.

Returns metadata only. Use the sibling endpoint (without `/metadata`)
to fetch the document text content.

id: string

Project document identifier (tagged ID)

claude\_project\_id: string

The project this document belongs to

created\_at: string

Document creation timestamp

filename: string

Document filename

md5: string

Lowercase hex MD5 of the document content (UTF-8 encoded). Matches the `content` field returned by the sibling content endpoint.

mime\_type: "text/plain"

MIME type of the document content, always plain text

size\_bytes: number

Size in bytes of the document content (UTF-8 encoded)

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
