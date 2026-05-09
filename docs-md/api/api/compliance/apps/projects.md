# Projects

Copy page

The Compliance API is available only on the Claude Enterprise plan and must be enabled before use. See [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Projects

##### [List projects](api/compliance/apps/projects/list.md)

GET/v1/compliance/apps/projects

##### [Get project details](api/compliance/apps/projects/retrieve.md)

GET/v1/compliance/apps/projects/{project\_id}

##### [Delete project](api/compliance/apps/projects/delete.md)

DELETE/v1/compliance/apps/projects/{project\_id}

##### [List project attachments](api/compliance/apps/projects/attachments.md)

GET/v1/compliance/apps/projects/{project\_id}/attachments

##### ModelsExpand Collapse

ProjectListResponse = object { id, created\_at, is\_private, 4 more }

Project information for compliance responses.

id: string

Project identifier (tagged ID)

created\_at: string

Project creation timestamp

is\_private: boolean

If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

name: string

Project name

organization\_id: string

Organization identifier (tagged ID)

updated\_at: string

Project last update timestamp

user: object { id, email\_address }

User information for project creator.

id: string

User identifier (tagged ID)

email\_address: string

User's email address

ProjectRetrieveResponse = object { id, attachments\_count, chats\_count, 8 more }

Detailed project information for compliance responses.

id: string

Project identifier (tagged ID)

attachments\_count: number

Number of attachments contained within this project

chats\_count: number

Number of chats contained within this project

created\_at: string

Project creation timestamp

description: string

Project description

instructions: string

Project's custom instructions / prompt

is\_private: boolean

If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

name: string

Project name

organization\_id: string

Organization identifier (tagged ID)

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

ProjectAttachmentsResponse = object { data, has\_more, next\_page }

List of project attachments with pagination info.

data: array of object { id, created\_at, filename, 2 more }  or object { id, created\_at, filename, 2 more }

List of attachments sorted chronologically by created\_at, tie break by id

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

has\_more: boolean

Whether more records exist beyond the current result set

next\_page: string

To get the next page, use the 'next\_page' from the current response as the 'page' in your next request

#### ProjectsDocuments

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
