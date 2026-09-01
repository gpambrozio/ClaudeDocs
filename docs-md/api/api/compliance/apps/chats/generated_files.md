# Generated Files

Copy page



# Generated Files

##### [Get Claude-generated file metadata](api/http/compliance/apps/chats/generated_files/retrieve.md)

GET/v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}

##### [Download a Claude-generated file](api/http/compliance/apps/chats/generated_files/download.md)

GET/v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}/content

##### Models



GeneratedFileRetrieveResponse object{ id, claude\_chat\_id, created\_at, 4 more }

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



created\_at: string or null

File creation timestamp, when available

formatdate-time

filename: string

Display name of the generated file

md5: string or null

Lowercase hex MD5 of the stored file. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes.

mime\_type: string or null

MIME type of the stored file, when available

size\_bytes: number or null

Size in bytes of the stored file, when available

---

*Copyright © Anthropic. All rights reserved.*
