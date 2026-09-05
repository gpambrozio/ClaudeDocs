# Apps

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](manage-claude/compliance-api-access.md)

Copy page



# Apps

#### Apps[Chats](api/http/compliance/apps/chats.md)

##### [List chats](api/http/compliance/apps/chats/list.md)

GET/v1/compliance/apps/chats

##### [Delete chat](api/http/compliance/apps/chats/delete.md)

DELETE/v1/compliance/apps/chats/{claude\_chat\_id}

#### AppsChats[Messages](api/http/compliance/apps/chats/messages.md)

##### [Get chat messages](api/http/compliance/apps/chats/messages/list.md)

GET/v1/compliance/apps/chats/{claude\_chat\_id}/messages

#### AppsChats[Files](api/http/compliance/apps/chats/files.md)

##### [Get file metadata](api/http/compliance/apps/chats/files/retrieve.md)

GET/v1/compliance/apps/chats/files/{claude\_file\_id}

##### [Delete file](api/http/compliance/apps/chats/files/delete.md)

DELETE/v1/compliance/apps/chats/files/{claude\_file\_id}

##### [Download file content](api/http/compliance/apps/chats/files/download.md)

GET/v1/compliance/apps/chats/files/{claude\_file\_id}/content

#### AppsChats[Generated Files](api/http/compliance/apps/chats/generated_files.md)

##### [Get Claude-generated file metadata](api/http/compliance/apps/chats/generated_files/retrieve.md)

GET/v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}

##### [Download a Claude-generated file](api/http/compliance/apps/chats/generated_files/download.md)

GET/v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}/content

#### Apps[Projects](api/http/compliance/apps/projects.md)

##### [List projects](api/http/compliance/apps/projects/list.md)

GET/v1/compliance/apps/projects

##### [Get project details](api/http/compliance/apps/projects/retrieve.md)

GET/v1/compliance/apps/projects/{project\_id}

##### [Delete project](api/http/compliance/apps/projects/delete.md)

DELETE/v1/compliance/apps/projects/{project\_id}

#### AppsProjects[Attachments](api/http/compliance/apps/projects/attachments.md)

##### [List project attachments](api/http/compliance/apps/projects/attachments/list.md)

GET/v1/compliance/apps/projects/{project\_id}/attachments

#### AppsProjects[Collaborators](api/http/compliance/apps/projects/collaborators.md)

##### [List project collaborators](api/http/compliance/apps/projects/collaborators/list.md)

GET/v1/compliance/apps/projects/{project\_id}/collaborators

#### AppsProjects[Documents](api/http/compliance/apps/projects/documents.md)

##### [Get project document content](api/http/compliance/apps/projects/documents/retrieve.md)

GET/v1/compliance/apps/projects/documents/{document\_id}

##### [Get project document metadata](api/http/compliance/apps/projects/documents/metadata.md)

GET/v1/compliance/apps/projects/documents/{document\_id}/metadata

##### [Delete project document](api/http/compliance/apps/projects/documents/delete.md)

DELETE/v1/compliance/apps/projects/documents/{document\_id}

#### Apps[Artifacts](api/http/compliance/apps/artifacts.md)

##### [Get artifact metadata](api/http/compliance/apps/artifacts/retrieve.md)

GET/v1/compliance/apps/artifacts/{artifact\_version\_id}

##### [Download artifact content](api/http/compliance/apps/artifacts/download.md)

GET/v1/compliance/apps/artifacts/{artifact\_version\_id}/content

#### AppsSessions[Local](api/http/compliance/apps/sessions/local.md)

##### [List local sessions](api/http/compliance/apps/sessions/local/list.md)

GET/v1/compliance/apps/sessions/local

##### [Retrieve a local session](api/http/compliance/apps/sessions/local/retrieve.md)

GET/v1/compliance/apps/sessions/local/{local\_session\_id}

#### AppsSessionsLocal[Messages](api/http/compliance/apps/sessions/local/messages.md)

##### [Retrieve local session messages](api/http/compliance/apps/sessions/local/messages/list.md)

GET/v1/compliance/apps/sessions/local/{local\_session\_id}/messages

#### AppsSessions[Remote](api/http/compliance/apps/sessions/remote.md)

##### [List remote sessions](api/http/compliance/apps/sessions/remote/list.md)

GET/v1/compliance/apps/sessions/remote

#### AppsSessionsRemote[Messages](api/http/compliance/apps/sessions/remote/messages.md)

##### [Retrieve remote session messages](api/http/compliance/apps/sessions/remote/messages/list.md)

GET/v1/compliance/apps/sessions/remote/{claude\_remote\_session\_id}/messages

---

*Copyright © Anthropic. All rights reserved.*
