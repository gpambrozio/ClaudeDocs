# Projects

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](manage-claude/compliance-api-access.md)

Copy page



# Projects

##### [List projects](api/http/compliance/apps/projects/list.md)

GET/v1/compliance/apps/projects

##### [Get project details](api/http/compliance/apps/projects/retrieve.md)

GET/v1/compliance/apps/projects/{project\_id}

##### [Delete project](api/http/compliance/apps/projects/delete.md)

DELETE/v1/compliance/apps/projects/{project\_id}

##### Models



ProjectRetrieveResponse object{ id, attachments\_count, chats\_count, 10 more }

Detailed project information for compliance responses.



ProjectListResponse object{ id, created\_at, deleted\_at, 6 more }

Project information for compliance responses.



ProjectDeleteResponse object{ id, type }

Response for deleting a Claude project.

id: string

The ID of the Claude project that was deleted



type: optional "claude\_project\_deleted"

Constant string confirming deletion.

defaultclaude\_project\_deleted

#### Projects[Attachments](api/http/compliance/apps/projects/attachments.md)

##### [List project attachments](api/http/compliance/apps/projects/attachments/list.md)

GET/v1/compliance/apps/projects/{project\_id}/attachments

#### Projects[Collaborators](api/http/compliance/apps/projects/collaborators.md)

##### [List project collaborators](api/http/compliance/apps/projects/collaborators/list.md)

GET/v1/compliance/apps/projects/{project\_id}/collaborators

#### Projects[Documents](api/http/compliance/apps/projects/documents.md)

##### [Get project document content](api/http/compliance/apps/projects/documents/retrieve.md)

GET/v1/compliance/apps/projects/documents/{document\_id}

##### [Get project document metadata](api/http/compliance/apps/projects/documents/metadata.md)

GET/v1/compliance/apps/projects/documents/{document\_id}/metadata

##### [Delete project document](api/http/compliance/apps/projects/documents/delete.md)

DELETE/v1/compliance/apps/projects/documents/{document\_id}

---

*Copyright © Anthropic. All rights reserved.*
