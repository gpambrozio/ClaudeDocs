# Files

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](manage-claude/compliance-activity-feed.md) only. See [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Files

##### [Get file metadata](api/compliance/apps/chats/files/retrieve.md)

GET/v1/compliance/apps/chats/files/{claude\_file\_id}

##### [Delete file](api/compliance/apps/chats/files/delete.md)

DELETE/v1/compliance/apps/chats/files/{claude\_file\_id}

##### [Download file content](api/compliance/apps/chats/files/download.md)

GET/v1/compliance/apps/chats/files/{claude\_file\_id}/content

##### ModelsExpand Collapse

FileRetrieveResponse = object { id, created\_at, filename, 4 more }

File metadata for GET /v1/compliance/apps/chats/files/{claude\_file\_id}.

Returns metadata only. Use the sibling `/content` endpoint to download
the file bytes.

id: string

File ID

created\_at: string

File creation timestamp

filename: string

Display name of the file, if set

md5: string

Lowercase hex MD5 of the file's preferred downloadable variant, as recorded at upload time. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes; when the two disagree, the header is authoritative.

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

---

*Copyright © Anthropic. All rights reserved.*
