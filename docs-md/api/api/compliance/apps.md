# Apps

Copy page



To enable the Compliance API, see [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Apps

#### AppsChats

##### [List chats](api/compliance/apps/chats/list.md)

GET/v1/compliance/apps/chats

##### [Delete chat](api/compliance/apps/chats/delete.md)

DELETE/v1/compliance/apps/chats/{claude\_chat\_id}

##### ModelsExpand Collapse



ChatListResponse object { id, created\_at, deleted\_at, 8 more } 

Chat metadata for listing chats (without messages).

id: string

Chat ID

created\_at: string

Creation timestamp

deleted\_at: string

Deletion timestamp if deleted

href: string

URL to view this chat in claude.ai

model: string

Model selected for this chat (e.g. 'claude-opus-4-7'). May be null for legacy chats that never had a model recorded.

name: string

Chat name/title

Deprecatedorganization\_id: string

Organization ID this chat belongs to

organization\_uuid: string

Organization UUID this chat belongs to

project\_id: string

Project ID this chat belongs to

updated\_at: string

Last update timestamp



user: object { id, email\_address } 

User information for the chat creator

id: string

User identifier

email\_address: string

User's email address



ChatDeleteResponse object { id, type } 

Response for deleting a Claude chat.

id: string

The ID of the Claude chat that was deleted

type: optional "claude\_chat\_deleted"

Constant string confirming deletion

#### AppsChatsMessages

##### [Get chat messages](api/compliance/apps/chats/messages/list.md)

GET/v1/compliance/apps/chats/{claude\_chat\_id}/messages

##### ModelsExpand Collapse



MessageListResponse object { id, artifacts, content, 4 more } 

A single message in a chat conversation.

id: string

Unique identifier for the message e.g. 'claude\_chat\_msg\_abcd1234'



artifacts: array of object { id, artifact\_type, title, version\_id } 

Versioned documents generated or updated by the assistant in this message. Download via `GET /v1/compliance/apps/artifacts/{artifact_version_id}/content`.

id: string

Artifact ID e.g. 'claude\_artifact\_abc123'

artifact\_type: string

MIME-like artifact type e.g. 'application/vnd.ant.code'

title: string

Artifact title

version\_id: string

Artifact version ID e.g. 'claude\_artifact\_version\_abc123'



content: array of object { text, type }  or object { id, input, integration\_name, 4 more }  or object { content, integration\_name, is\_error, 5 more } 

Content blocks within the message

One of the following:



Text object { text, type } 

Text content block.

text: string

Text content from human or assistant

type: "text"



ToolUse object { id, input, integration\_name, 4 more } 

Tool invocation requested by the assistant.

id: string

Tool-use ID, e.g. 'toolu\_01AbC...'

input: string

Arguments passed to the tool, as a JSON-encoded string. May be shortened — see the `truncated` field

integration\_name: string

Name of the integration that provides this tool, when applicable

mcp\_server\_url: string

Base URL (scheme, host, and path only) of the MCP server that provides this tool, when applicable

name: string

Name of the tool invoked

truncated: boolean

True when `input` was shortened. Pass tool\_use\_input\_max\_chars=-1 to disable the limit

type: "tool\_use"



ToolResult object { content, integration\_name, is\_error, 5 more } 

Result returned by a tool invocation.



content: array of object { text, type } 

Text content returned by the tool. Generated files are surfaced via the message's `generated_files` list; other non-text item types (including images and links) are omitted.

text: string

Text returned by the tool

type: "text"

integration\_name: string

Name of the integration that provides this tool, when applicable

is\_error: boolean

True when the tool reported an error

mcp\_server\_url: string

Base URL (scheme, host, and path only) of the MCP server that provides this tool, when applicable

name: string

Name of the tool that produced this result

tool\_use\_id: string

ID of the tool\_use block this result responds to

truncated: boolean

True when one or more text items in `content` were shortened. Pass tool\_result\_max\_chars=-1 to retrieve full content.

type: "tool\_result"

created\_at: string

Message creation timestamp - For human: when they sent the message, For assistant: when it completed the last content block



files: array of object { id, filename, mime\_type } 

Binary file attachments uploaded by the user. Download via `GET /v1/compliance/apps/chats/files/{claude_file_id}/content`.

id: string

File ID

filename: string

Display name of the file

mime\_type: string

MIME type of the file when it was uploaded (e.g. 'application/pdf')



generated\_files: array of object { id, filename, mime\_type } 

Downloadable files the assistant created via tool use (e.g. PDF, spreadsheet, slide deck). Distinct from `files`, which are uploads attached to the message. Download via `GET /v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content`.

id: string

Opaque generated-file id, e.g. 'claude\_gen\_file\_abc123'. Treat as an opaque string; the encoding may change without notice.

filename: string

Display name of the generated file

mime\_type: string

MIME type reported by the tool that produced the file



role: "assistant" or "user"

Message sender (user or assistant)

One of the following:

"assistant"

"user"

#### AppsChatsFiles

##### [Get file metadata](api/compliance/apps/chats/files/retrieve.md)

GET/v1/compliance/apps/chats/files/{claude\_file\_id}

##### [Delete file](api/compliance/apps/chats/files/delete.md)

DELETE/v1/compliance/apps/chats/files/{claude\_file\_id}

##### [Download file content](api/compliance/apps/chats/files/download.md)

GET/v1/compliance/apps/chats/files/{claude\_file\_id}/content

##### ModelsExpand Collapse



FileRetrieveResponse object { id, claude\_chat\_ids, created\_at, 5 more } 

File metadata for GET /v1/compliance/apps/chats/files/{claude\_file\_id}.

Returns metadata only. Use the sibling `/content` endpoint to download
the file bytes.

id: string

File ID

claude\_chat\_ids: array of string

Chats this file is attached to. A file can be referenced by messages across multiple chats.

created\_at: string

File creation timestamp

filename: string

Display name of the file, if set

md5: string

Lowercase hex MD5 of the file's preferred downloadable variant, as recorded at upload time. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes; when the two disagree, the header is authoritative.

message\_ids: array of string

Chat message IDs this file is attached to. A file can be referenced by multiple messages.

mime\_type: string

MIME type of the file's preferred downloadable variant (e.g. 'application/pdf'). May be null for files with no downloadable content (e.g. code-interpreter outputs).

size\_bytes: number

Size in bytes of the file's preferred downloadable variant, if known



FileDeleteResponse object { id, type } 

Response for deleting a compliance file.

id: string

The ID of the file that was deleted

type: optional "claude\_file\_deleted"

Constant string confirming deletion

#### AppsChatsGenerated Files

##### [Get Claude-generated file metadata](api/compliance/apps/chats/generated_files/retrieve.md)

GET/v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}

##### [Download a Claude-generated file](api/compliance/apps/chats/generated_files/download.md)

GET/v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}/content

##### ModelsExpand Collapse



GeneratedFileRetrieveResponse object { id, claude\_chat\_id, created\_at, 4 more } 

Metadata for GET /v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}.

Returns metadata only. Use the sibling `/content` endpoint to download
the bytes. The owning chat is included since the id is opaque; to find the
specific message that produced the file, fetch
`/v1/compliance/apps/chats/{claude_chat_id}/messages` and match on
`generated_files[].id`.

id: string

Opaque generated-file id, e.g. 'claude\_gen\_file\_abc123'.

claude\_chat\_id: string

The chat this generated file belongs to

created\_at: string

File creation timestamp from Filestore

filename: string

Display name of the generated file

md5: string

Lowercase hex MD5 of the stored file, as recorded by Filestore. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes.

mime\_type: string

MIME type as recorded by Filestore, when available

size\_bytes: number

Size in bytes of the stored file, when available

#### AppsProjects

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

#### AppsProjectsAttachments

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

#### AppsProjectsCollaborators

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

#### AppsProjectsDocuments

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

#### AppsArtifacts

##### [Get artifact metadata](api/compliance/apps/artifacts/retrieve.md)

GET/v1/compliance/apps/artifacts/{artifact\_version\_id}

##### [Download artifact content](api/compliance/apps/artifacts/download.md)

GET/v1/compliance/apps/artifacts/{artifact\_version\_id}/content

##### ModelsExpand Collapse



ArtifactRetrieveResponse object { id, artifact\_type, claude\_chat\_id, 5 more } 

Artifact version metadata for GET /v1/compliance/apps/artifacts/{artifact\_version\_id}.

Returns metadata only. Use the sibling `/content` endpoint to fetch the
artifact body.

id: string

Artifact ID e.g. 'claude\_artifact\_abc123'

artifact\_type: string

MIME-like artifact type e.g. 'application/vnd.ant.code'

claude\_chat\_id: string

The chat this artifact belongs to

created\_at: string

Artifact version creation timestamp

md5: string

Lowercase hex MD5 of the artifact content (UTF-8 encoded). Matches the `content` field returned by the sibling `/content` endpoint.

size\_bytes: number

Size in bytes of the artifact content (UTF-8 encoded)

title: string

Artifact title

version\_id: string

Artifact version ID e.g. 'claude\_artifact\_version\_abc123'

---

*Copyright © Anthropic. All rights reserved.*
