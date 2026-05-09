# Files

Copy page

The Compliance API is available only on the Claude Enterprise plan and must be enabled before use. See [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Files

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

---

*Copyright © Anthropic. All rights reserved.*
