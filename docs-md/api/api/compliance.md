# Compliance API

Copy page



# Compliance API

#### Compliance API[Activities](api/http/compliance/activities.md)

##### [Query compliance activities](api/http/compliance/activities/list.md)

GET/v1/compliance/activities

#### Compliance API[Organizations](api/http/compliance/organizations.md)

##### [List organizations](api/http/compliance/organizations/list.md)

GET/v1/compliance/organizations

#### Compliance APIOrganizations[Users](api/http/compliance/organizations/users.md)

##### [List organization users](api/http/compliance/organizations/users/list.md)

GET/v1/compliance/organizations/{org\_uuid}/users

#### Compliance APIOrganizations[Roles](api/http/compliance/organizations/roles.md)

##### [List Compliance Roles](api/http/compliance/organizations/roles/list.md)

GET/v1/compliance/organizations/{org\_uuid}/roles

##### [Get Compliance Role](api/http/compliance/organizations/roles/retrieve.md)

GET/v1/compliance/organizations/{org\_uuid}/roles/{role\_id}

#### Compliance APIOrganizationsRoles[Permissions](api/http/compliance/organizations/roles/permissions.md)

##### [List Compliance Role Permissions](api/http/compliance/organizations/roles/permissions/list.md)

GET/v1/compliance/organizations/{org\_uuid}/roles/{role\_id}/permissions

#### Compliance APIOrganizations[Settings](api/http/compliance/organizations/settings.md)

##### [Get effective organization settings](api/http/compliance/organizations/settings/retrieve.md)

GET/v1/compliance/organizations/{organization\_id}/settings

#### Compliance API[Groups](api/http/compliance/groups.md)

##### [List Compliance Groups](api/http/compliance/groups/list.md)

GET/v1/compliance/groups

##### [Get Compliance Group](api/http/compliance/groups/retrieve.md)

GET/v1/compliance/groups/{group\_id}

#### Compliance APIGroups[Members](api/http/compliance/groups/members.md)

##### [List Compliance Group Members](api/http/compliance/groups/members/list.md)

GET/v1/compliance/groups/{group\_id}/members

#### Compliance APIApps[Chats](api/http/compliance/apps/chats.md)

##### [List chats](api/http/compliance/apps/chats/list.md)

GET/v1/compliance/apps/chats

##### [Delete chat](api/http/compliance/apps/chats/delete.md)

DELETE/v1/compliance/apps/chats/{claude\_chat\_id}

#### Compliance APIAppsChats[Messages](api/http/compliance/apps/chats/messages.md)

##### [Get chat messages](api/http/compliance/apps/chats/messages/list.md)

GET/v1/compliance/apps/chats/{claude\_chat\_id}/messages

#### Compliance APIAppsChats[Files](api/http/compliance/apps/chats/files.md)

##### [Get file metadata](api/http/compliance/apps/chats/files/retrieve.md)

GET/v1/compliance/apps/chats/files/{claude\_file\_id}

##### [Delete file](api/http/compliance/apps/chats/files/delete.md)

DELETE/v1/compliance/apps/chats/files/{claude\_file\_id}

##### [Download file content](api/http/compliance/apps/chats/files/download.md)

GET/v1/compliance/apps/chats/files/{claude\_file\_id}/content

#### Compliance APIAppsChats[Generated Files](api/http/compliance/apps/chats/generated_files.md)

##### [Get Claude-generated file metadata](api/http/compliance/apps/chats/generated_files/retrieve.md)

GET/v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}

##### [Download a Claude-generated file](api/http/compliance/apps/chats/generated_files/download.md)

GET/v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}/content

#### Compliance APIApps[Projects](api/http/compliance/apps/projects.md)

##### [List projects](api/http/compliance/apps/projects/list.md)

GET/v1/compliance/apps/projects

##### [Get project details](api/http/compliance/apps/projects/retrieve.md)

GET/v1/compliance/apps/projects/{project\_id}

##### [Delete project](api/http/compliance/apps/projects/delete.md)

DELETE/v1/compliance/apps/projects/{project\_id}

#### Compliance APIAppsProjects[Attachments](api/http/compliance/apps/projects/attachments.md)

##### [List project attachments](api/http/compliance/apps/projects/attachments/list.md)

GET/v1/compliance/apps/projects/{project\_id}/attachments

#### Compliance APIAppsProjects[Collaborators](api/http/compliance/apps/projects/collaborators.md)

##### [List project collaborators](api/http/compliance/apps/projects/collaborators/list.md)

GET/v1/compliance/apps/projects/{project\_id}/collaborators

#### Compliance APIAppsProjects[Documents](api/http/compliance/apps/projects/documents.md)

##### [Get project document content](api/http/compliance/apps/projects/documents/retrieve.md)

GET/v1/compliance/apps/projects/documents/{document\_id}

##### [Get project document metadata](api/http/compliance/apps/projects/documents/metadata.md)

GET/v1/compliance/apps/projects/documents/{document\_id}/metadata

##### [Delete project document](api/http/compliance/apps/projects/documents/delete.md)

DELETE/v1/compliance/apps/projects/documents/{document\_id}

#### Compliance APIApps[Artifacts](api/http/compliance/apps/artifacts.md)

##### [Get artifact metadata](api/http/compliance/apps/artifacts/retrieve.md)

GET/v1/compliance/apps/artifacts/{artifact\_version\_id}

##### [Download artifact content](api/http/compliance/apps/artifacts/download.md)

GET/v1/compliance/apps/artifacts/{artifact\_version\_id}/content

#### Compliance APIAppsSessions[Local](api/http/compliance/apps/sessions/local.md)

##### [List local sessions](api/http/compliance/apps/sessions/local/list.md)

GET/v1/compliance/apps/sessions/local

##### [Retrieve a local session](api/http/compliance/apps/sessions/local/retrieve.md)

GET/v1/compliance/apps/sessions/local/{local\_session\_id}

#### Compliance APIAppsSessionsLocal[Messages](api/http/compliance/apps/sessions/local/messages.md)

##### [Retrieve local session messages](api/http/compliance/apps/sessions/local/messages/list.md)

GET/v1/compliance/apps/sessions/local/{local\_session\_id}/messages

#### Compliance APIAppsSessions[Remote](api/http/compliance/apps/sessions/remote.md)

##### [List remote sessions](api/http/compliance/apps/sessions/remote/list.md)

GET/v1/compliance/apps/sessions/remote

#### Compliance APIAppsSessionsRemote[Messages](api/http/compliance/apps/sessions/remote/messages.md)

##### [Retrieve remote session messages](api/http/compliance/apps/sessions/remote/messages/list.md)

GET/v1/compliance/apps/sessions/remote/{claude\_remote\_session\_id}/messages

#### Compliance APICode[Artifacts](api/http/compliance/code/artifacts.md)

##### [List Code Artifacts](api/http/compliance/code/artifacts/list.md)

GET/v1/compliance/apps/code/artifacts

##### [Download Code Artifact Version Content](api/http/compliance/code/artifacts/retrieve_version.md)

GET/v1/compliance/apps/code/artifacts/{artifact\_id}/versions/{version\_id}

##### [Delete Code Artifact](api/http/compliance/code/artifacts/delete.md)

DELETE/v1/compliance/apps/code/artifacts/{artifact\_id}

---

*Copyright © Anthropic. All rights reserved.*
