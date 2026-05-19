# Compliance API

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](manage-claude/compliance-activity-feed.md) only. See [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Compliance API

#### Compliance APIActivities

##### [Query compliance activities](api/compliance/activities/list.md)

GET/v1/compliance/activities

##### ModelsExpand Collapse

ActivityListResponse = map[unknown]

#### Compliance APIOrganizations

##### [List organizations](api/compliance/organizations/list.md)

GET/v1/compliance/organizations

##### ModelsExpand Collapse

OrganizationListResponse = object { data }

List of organizations under a parent organization.

data: array of object { created\_at, name, uuid }

List of organizations sorted by creation date, ascending

created\_at: string

Organization creation time (RFC 3339 format)

name: string

Organization name

uuid: string

Unique identifier for the organization (UUID format)

#### Compliance APIOrganizationsUsers

##### [List organization users](api/compliance/organizations/users/list.md)

GET/v1/compliance/organizations/{org\_uuid}/users

##### ModelsExpand Collapse

UserListResponse = object { id, created\_at, email, full\_name }

User member information for compliance responses.

id: string

User identifier (tagged ID)

created\_at: string

User account creation timestamp

email: string

User's current email address

full\_name: string

User's current full name

#### Compliance APIOrganizationsRoles

##### [List Compliance Roles](api/compliance/organizations/roles/list.md)

GET/v1/compliance/organizations/{org\_uuid}/roles

##### [Get Compliance Role](api/compliance/organizations/roles/retrieve.md)

GET/v1/compliance/organizations/{org\_uuid}/roles/{role\_id}

##### ModelsExpand Collapse

RoleListResponse = object { id, created\_at, description, 2 more }

Role information for compliance responses.

id: string

Role identifier (tagged ID)

created\_at: string

Role creation timestamp (ISO 8601)

description: string

Role description

name: string

Role name

updated\_at: string

Role last-updated timestamp (ISO 8601)

RoleRetrieveResponse = object { id, created\_at, description, 2 more }

Role information for compliance responses.

id: string

Role identifier (tagged ID)

created\_at: string

Role creation timestamp (ISO 8601)

description: string

Role description

name: string

Role name

updated\_at: string

Role last-updated timestamp (ISO 8601)

#### Compliance APIOrganizationsRolesPermissions

##### [List Compliance Role Permissions](api/compliance/organizations/roles/permissions/list.md)

GET/v1/compliance/organizations/{org\_uuid}/roles/{role\_id}/permissions

##### ModelsExpand Collapse

PermissionListResponse = object { action, resource\_id, resource\_type }

Permission granted by a role.

action: string

Action permitted on the resource

resource\_id: string

Identifier of the resource the permission applies to

resource\_type: string

Type of resource the permission applies to

#### Compliance APIGroups

##### [List Compliance Groups](api/compliance/groups/list.md)

GET/v1/compliance/groups

##### [Get Compliance Group](api/compliance/groups/retrieve.md)

GET/v1/compliance/groups/{group\_id}

##### ModelsExpand Collapse

GroupListResponse = object { id, created\_at, description, 4 more }

Group information for compliance responses.

id: string

Group identifier (tagged ID)

created\_at: string

Group creation timestamp (ISO 8601)

description: string

Group description

name: string

Group name

roles: array of string

Role IDs assigned to this group.

source\_type: string

How the group was created ('direct' or 'scim')

updated\_at: string

Group last-updated timestamp (ISO 8601)

GroupRetrieveResponse = object { id, created\_at, description, 4 more }

Group information for compliance responses.

id: string

Group identifier (tagged ID)

created\_at: string

Group creation timestamp (ISO 8601)

description: string

Group description

name: string

Group name

roles: array of string

Role IDs assigned to this group.

source\_type: string

How the group was created ('direct' or 'scim')

updated\_at: string

Group last-updated timestamp (ISO 8601)

#### Compliance APIGroupsMembers

##### [List Compliance Group Members](api/compliance/groups/members/list.md)

GET/v1/compliance/groups/{group\_id}/members

##### ModelsExpand Collapse

MemberListResponse = object { created\_at, email, updated\_at, user\_id }

Group member for compliance responses.

created\_at: string

Membership creation timestamp (ISO 8601)

email: string

Member email address

updated\_at: string

Membership last-updated timestamp (ISO 8601)

user\_id: string

Member user identifier (tagged ID)

#### Compliance APIApps

#### Compliance APIAppsChats

##### [List chats](api/compliance/apps/chats/list.md)

GET/v1/compliance/apps/chats

##### [Delete chat](api/compliance/apps/chats/delete.md)

DELETE/v1/compliance/apps/chats/{claude\_chat\_id}

##### [Get chat messages](api/compliance/apps/chats/messages.md)

GET/v1/compliance/apps/chats/{claude\_chat\_id}/messages

##### ModelsExpand Collapse

ChatListResponse = object { id, created\_at, deleted\_at, 8 more }

Chat metadata for listing chats (without messages).

id: string

Chat ID

created\_at: string

Creation timestamp

deleted\_at: string

Deletion timestamp if deleted

href: string

URL to view this chat in claude.ai

model: string

Model selected for this chat (e.g. 'claude-opus-4-7'). May be null for legacy chats that never had a model recorded.

name: string

Chat name/title

organization\_id: string

Organization ID this chat belongs to

organization\_uuid: string

Organization UUID this chat belongs to

project\_id: string

Project ID this chat belongs to

updated\_at: string

Last update timestamp

user: object { id, email\_address }

User information for the chat creator

id: string

User identifier

email\_address: string

User's email address

ChatDeleteResponse = object { id, type }

Response for deleting a Claude chat.

id: string

The ID of the Claude chat that was deleted

type: optional "claude\_chat\_deleted"

Constant string confirming deletion

ChatMessagesResponse = object { id, chat\_messages, created\_at, 12 more }

Complete chat conversation data for compliance purposes.

id: string

Chat ID

chat\_messages: array of object { id, artifacts, content, 4 more }

Array of chat messages in order of created\_at

id: string

Unique identifier for the message e.g. 'claude\_chat\_msg\_abcd1234'

artifacts: array of object { id, artifact\_type, title, version\_id }

Artifacts generated or updated by this message

id: string

Artifact ID e.g. 'claude\_artifact\_abc123'

artifact\_type: string

MIME-like artifact type e.g. 'application/vnd.ant.code'

title: string

Artifact title

version\_id: string

Artifact version ID e.g. 'claude\_artifact\_version\_abc123'

content: array of object { text, type }

Content blocks within the message

text: string

Text content from human or assistant

type: "text"

created\_at: string

Message creation timestamp - For human: when they sent the message, For assistant: when it completed the last content block

files: array of object { id, filename, mime\_type }

File attachments

id: string

File ID

filename: string

Display name of the file

mime\_type: string

MIME type of the file when it was uploaded (e.g. 'application/pdf')

generated\_files: array of object { id, filename, mime\_type }

Downloadable files the assistant created via tool use (e.g. PDF, spreadsheet, slide deck). Distinct from `files`, which are uploads attached to the message.

id: string

Opaque generated-file id, e.g. 'claude\_gen\_file\_abc123'. Treat as an opaque string; the encoding may change without notice.

filename: string

Display name of the generated file

mime\_type: string

MIME type reported by the tool that produced the file

role: "user" or "assistant"

Message sender (user or assistant)

Accepts one of the following:

"user"

"assistant"

created\_at: string

Creation timestamp

deleted\_at: string

Deletion timestamp if deleted

first\_id: string

Opaque pagination cursor for the first message in the current result set. Pass as `before_id` on the next request to page backwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

has\_more: boolean

Whether more chat messages exist beyond the current result set. Use `last_id` as `after_id` in a follow-up request to page forward.

href: string

URL to view this chat in claude.ai

last\_id: string

Opaque pagination cursor for the last message in the current result set. Pass as `after_id` on the next request to page forwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

model: string

Model selected for this chat (e.g. 'claude-opus-4-7'). May be null for legacy chats that never had a model recorded.

name: string

Chat name

organization\_id: string

Organization ID this chat belongs to

organization\_uuid: string

Organization UUID this chat belongs to

project\_id: string

Project ID this chat belongs to

updated\_at: string

Last update timestamp

user: object { id, email\_address }

User information

id: string

User identifier

email\_address: string

User's email address

#### Compliance APIAppsChatsFiles

##### [Get file metadata](api/compliance/apps/chats/files/retrieve.md)

GET/v1/compliance/apps/chats/files/{claude\_file\_id}

##### [Delete file](api/compliance/apps/chats/files/delete.md)

DELETE/v1/compliance/apps/chats/files/{claude\_file\_id}

##### [Download file content](api/compliance/apps/chats/files/content.md)

GET/v1/compliance/apps/chats/files/{claude\_file\_id}/content

##### ModelsExpand Collapse

FileRetrieveResponse = object { id, created\_at, filename, 3 more }

File metadata for GET /v1/compliance/apps/chats/files/{claude\_file\_id}.

Returns metadata only. Use the sibling `/content` endpoint to download
the file bytes.

id: string

File ID

created\_at: string

File creation timestamp

filename: string

Display name of the file, if set

message\_ids: array of string

Chat message IDs this file is attached to. A file can be referenced by multiple messages.

mime\_type: string

MIME type of the file's preferred downloadable variant (e.g. 'application/pdf'). May be null for files with no downloadable content (e.g. code-interpreter outputs).

size\_bytes: number

Size in bytes of the file's preferred downloadable variant, if known

FileDeleteResponse = object { id, type }

Response for deleting a compliance file.

id: string

The ID of the file that was deleted

type: optional "claude\_file\_deleted"

Constant string confirming deletion

FileContentResponse = unknown

#### Compliance APIAppsChatsGenerated Files

##### [Download a Claude-generated file](api/compliance/apps/chats/generated_files/content.md)

GET/v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}/content

##### ModelsExpand Collapse

GeneratedFileContentResponse = unknown

#### Compliance APIAppsProjects

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

#### Compliance APIAppsProjectsDocuments

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

#### Compliance APIAppsArtifacts

##### [Download artifact content](api/compliance/apps/artifacts/content.md)

GET/v1/compliance/apps/artifacts/{artifact\_version\_id}/content

##### ModelsExpand Collapse

ArtifactContentResponse = unknown

---

*Copyright © Anthropic. All rights reserved.*
