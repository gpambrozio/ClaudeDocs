# Files

Copy page



# Files

##### [Get file metadata](api/http/compliance/apps/chats/files/retrieve.md)

GET/v1/compliance/apps/chats/files/{claude\_file\_id}

##### [Delete file](api/http/compliance/apps/chats/files/delete.md)

DELETE/v1/compliance/apps/chats/files/{claude\_file\_id}

##### [Download file content](api/http/compliance/apps/chats/files/download.md)

GET/v1/compliance/apps/chats/files/{claude\_file\_id}/content

##### Models



FileRetrieveResponse object{ id, claude\_chat\_ids, created\_at, 5 more }

File metadata for GET /v1/compliance/apps/chats/files/{claude\_file\_id}.

Returns metadata only. Use the sibling `/content` endpoint to download
the file bytes.

id: string

File ID

claude\_chat\_ids: array of string

Chats this file is attached to. A file can be referenced by messages across multiple chats.



created\_at: string

File creation timestamp

formatdate-time

filename: string or null

Display name of the file, if set

md5: string or null

Lowercase hex MD5 of the file's preferred downloadable variant, as recorded at upload time. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes; when the two disagree, the header is authoritative.

message\_ids: array of string

Chat message IDs this file is attached to. A file can be referenced by multiple messages.

mime\_type: string or null

MIME type of the file's preferred downloadable variant (e.g. 'application/pdf'). May be null for files with no downloadable content (e.g. code-interpreter outputs).

size\_bytes: number or null

Size in bytes of the file's preferred downloadable variant, if known



FileDeleteResponse object{ id, type }

Response for deleting a compliance file.

id: string

The ID of the file that was deleted



type: optional "claude\_file\_deleted"

Constant string confirming deletion

defaultclaude\_file\_deleted

---

*Copyright © Anthropic. All rights reserved.*
