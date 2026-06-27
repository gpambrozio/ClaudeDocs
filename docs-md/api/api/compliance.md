# Compliance API

Copy page





To enable the Compliance API, see [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Compliance API

#### Compliance APIActivities

##### [Query compliance activities](api/compliance/activities/list.md)

GET/v1/compliance/activities

#### Compliance APIOrganizations

##### [List organizations](api/compliance/organizations/list.md)

GET/v1/compliance/organizations

#### Compliance APIOrganizationsUsers

##### [List organization users](api/compliance/organizations/users/list.md)

GET/v1/compliance/organizations/{org\_uuid}/users

#### Compliance APIOrganizationsRoles

##### [List Compliance Roles](api/compliance/organizations/roles/list.md)

GET/v1/compliance/organizations/{org\_uuid}/roles

##### [Get Compliance Role](api/compliance/organizations/roles/retrieve.md)

GET/v1/compliance/organizations/{org\_uuid}/roles/{role\_id}

#### Compliance APIOrganizationsRolesPermissions

##### [List Compliance Role Permissions](api/compliance/organizations/roles/permissions/list.md)

GET/v1/compliance/organizations/{org\_uuid}/roles/{role\_id}/permissions

#### Compliance APIOrganizationsSettings

##### [Get effective organization settings](api/compliance/organizations/settings/retrieve.md)

GET/v1/compliance/organizations/{organization\_id}/settings

#### Compliance APIGroups

##### [List Compliance Groups](api/compliance/groups/list.md)

GET/v1/compliance/groups

##### [Get Compliance Group](api/compliance/groups/retrieve.md)

GET/v1/compliance/groups/{group\_id}

#### Compliance APIGroupsMembers

##### [List Compliance Group Members](api/compliance/groups/members/list.md)

GET/v1/compliance/groups/{group\_id}/members

#### Compliance APIApps

#### Compliance APIAppsChats

##### [List chats](api/compliance/apps/chats/list.md)

GET/v1/compliance/apps/chats

##### [Delete chat](api/compliance/apps/chats/delete.md)

DELETE/v1/compliance/apps/chats/{claude\_chat\_id}

#### Compliance APIAppsChatsMessages

##### [Get chat messages](api/compliance/apps/chats/messages/list.md)

GET/v1/compliance/apps/chats/{claude\_chat\_id}/messages

#### Compliance APIAppsChatsFiles

##### [Get file metadata](api/compliance/apps/chats/files/retrieve.md)

GET/v1/compliance/apps/chats/files/{claude\_file\_id}

##### [Delete file](api/compliance/apps/chats/files/delete.md)

DELETE/v1/compliance/apps/chats/files/{claude\_file\_id}

##### [Download file content](api/compliance/apps/chats/files/download.md)

GET/v1/compliance/apps/chats/files/{claude\_file\_id}/content

#### Compliance APIAppsChatsGenerated Files

##### [Get Claude-generated file metadata](api/compliance/apps/chats/generated_files/retrieve.md)

GET/v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}

##### [Download a Claude-generated file](api/compliance/apps/chats/generated_files/download.md)

GET/v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}/content

#### Compliance APIAppsProjects

##### [List projects](api/compliance/apps/projects/list.md)

GET/v1/compliance/apps/projects

##### [Get project details](api/compliance/apps/projects/retrieve.md)

GET/v1/compliance/apps/projects/{project\_id}

##### [Delete project](api/compliance/apps/projects/delete.md)

DELETE/v1/compliance/apps/projects/{project\_id}

#### Compliance APIAppsProjectsAttachments

##### [List project attachments](api/compliance/apps/projects/attachments/list.md)

GET/v1/compliance/apps/projects/{project\_id}/attachments

#### Compliance APIAppsProjectsCollaborators

##### [List project collaborators](api/compliance/apps/projects/collaborators/list.md)

GET/v1/compliance/apps/projects/{project\_id}/collaborators

#### Compliance APIAppsProjectsDocuments

##### [Get project document content](api/compliance/apps/projects/documents/retrieve.md)

GET/v1/compliance/apps/projects/documents/{document\_id}

##### [Get project document metadata](api/compliance/apps/projects/documents/metadata.md)

GET/v1/compliance/apps/projects/documents/{document\_id}/metadata

##### [Delete project document](api/compliance/apps/projects/documents/delete.md)

DELETE/v1/compliance/apps/projects/documents/{document\_id}

#### Compliance APIAppsArtifacts

##### [Get artifact metadata](api/compliance/apps/artifacts/retrieve.md)

GET/v1/compliance/apps/artifacts/{artifact\_version\_id}

##### [Download artifact content](api/compliance/apps/artifacts/download.md)

GET/v1/compliance/apps/artifacts/{artifact\_version\_id}/content

#### Compliance APICode

#### Compliance APICodeArtifacts

##### [List Code Artifacts](api/compliance/code/artifacts/list.md)

GET/v1/compliance/code/artifacts

##### [Download Code Artifact Version Content](api/compliance/code/artifacts/retrieve_version.md)

GET/v1/compliance/code/artifacts/{artifact\_id}/versions/{version\_id}

##### [Delete Code Artifact](api/compliance/code/artifacts/delete.md)

DELETE/v1/compliance/code/artifacts/{artifact\_id}

---

*Copyright © Anthropic. All rights reserved.*
