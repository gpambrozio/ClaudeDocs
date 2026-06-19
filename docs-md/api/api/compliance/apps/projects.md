# Projects

Copy page





To enable the Compliance API, see [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Projects

##### [List projects](api/compliance/apps/projects/list.md)

GET/v1/compliance/apps/projects

##### [Get project details](api/compliance/apps/projects/retrieve.md)

GET/v1/compliance/apps/projects/{project\_id}

##### [Delete project](api/compliance/apps/projects/delete.md)

DELETE/v1/compliance/apps/projects/{project\_id}

##### ModelsExpand Collapse



ProjectListResponse object { id, created\_at, deleted\_at, 6 more } 

Project information for compliance responses.

id: string

Project identifier (tagged ID)

created\_at: string

Project creation timestamp

deleted\_at: string

Timestamp when the project was deleted by an end user, or null otherwise

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



ProjectRetrieveResponse object { id, attachments\_count, chats\_count, 10 more } 

Detailed project information for compliance responses.

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



ProjectDeleteResponse object { id, type } 

Response for deleting a Claude project.

id: string

The ID of the Claude project that was deleted

type: optional "claude\_project\_deleted"

Constant string confirming deletion.

#### ProjectsAttachments

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

#### ProjectsCollaborators

##### [List project collaborators](api/compliance/apps/projects/collaborators/list.md)

GET/v1/compliance/apps/projects/{project\_id}/collaborators

##### ModelsExpand Collapse



CollaboratorListResponse = object { granted\_at, role, type, user\_id }  or object { granted\_at, group\_id, role, type }  or object { granted\_at, organization\_uuid, role, type }  or object { granted\_at, organization\_role, role, type } 

An individual user granted a role on a project.

One of the following:



ComplianceProjectUserCollaborator object { granted\_at, role, type, user\_id } 

An individual user granted a role on a project.

granted\_at: string

When this collaborator was granted access (RFC 3339 format)



role: "admin" or "editor" or "owner" or "viewer"

Role granted on the project

One of the following:

"admin"

"editor"

"owner"

"viewer"

type: "user"

Discriminator marking this as an individual user collaborator

user\_id: string

Identifier of the user granted access (tagged ID), or null if their account has since been deleted



ComplianceProjectGroupCollaborator object { granted\_at, group\_id, role, type } 

An RBAC group granted a role on a project.

granted\_at: string

When this collaborator was granted access (RFC 3339 format)

group\_id: string

Identifier of the group granted access (tagged ID)



role: "admin" or "editor" or "owner" or "viewer"

Role granted on the project

One of the following:

"admin"

"editor"

"owner"

"viewer"

type: "group"

Discriminator marking this as a group collaborator



ComplianceProjectOrganizationCollaborator object { granted\_at, organization\_uuid, role, type } 

An entire organization granted a role on a project.

granted\_at: string

When this collaborator was granted access (RFC 3339 format)

organization\_uuid: string

UUID of the organization granted access



role: "admin" or "editor" or "owner" or "viewer"

Role granted on the project

One of the following:

"admin"

"editor"

"owner"

"viewer"

type: "organization"

Discriminator marking this as an organization-wide grant



ComplianceProjectOrganizationRoleCollaborator object { granted\_at, organization\_role, role, type } 

All holders of an organization-level role granted a role on a project.

granted\_at: string

When this collaborator was granted access (RFC 3339 format)

organization\_role: string

The organization-level role whose holders are granted access



role: "admin" or "editor" or "owner" or "viewer"

Role granted on the project

One of the following:

"admin"

"editor"

"owner"

"viewer"

type: "organization\_role"

Discriminator marking this as a grant to all organization members holding a specific org-level role

#### ProjectsDocuments

##### [Get project document content](api/compliance/apps/projects/documents/retrieve.md)

GET/v1/compliance/apps/projects/documents/{document\_id}

##### [Get project document metadata](api/compliance/apps/projects/documents/metadata.md)

GET/v1/compliance/apps/projects/documents/{document\_id}/metadata

##### [Delete project document](api/compliance/apps/projects/documents/delete.md)

DELETE/v1/compliance/apps/projects/documents/{document\_id}

##### ModelsExpand Collapse



DocumentRetrieveResponse object { id, content, created\_at, 2 more } 

Project document information for compliance responses.

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



DocumentMetadataResponse object { id, claude\_project\_id, created\_at, 5 more } 

Project document metadata for GET /v1/compliance/apps/projects/documents/{document\_id}/metadata.

Returns metadata only. Use the sibling endpoint (without `/metadata`)
to fetch the document text content.

id: string

Project document identifier (tagged ID)

claude\_project\_id: string

The project this document belongs to

created\_at: string

Document creation timestamp

filename: string

Document filename

md5: string

Lowercase hex MD5 of the document content (UTF-8 encoded). Matches the `content` field returned by the sibling content endpoint.

mime\_type: "text/plain"

MIME type of the document content, always plain text

size\_bytes: number

Size in bytes of the document content (UTF-8 encoded)

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



DocumentDeleteResponse object { id, type } 

Response for deleting a project document.

id: string

The ID of the project document that was deleted

type: "claude\_project\_document\_deleted"

Constant string confirming deletion.

---

*Copyright © Anthropic. All rights reserved.*
