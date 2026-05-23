# Generated Files

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](manage-claude/compliance-activity-feed.md) only. See [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Generated Files

##### [Get Claude-generated file metadata](api/compliance/apps/chats/generated_files/retrieve.md)

GET/v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}

##### [Download a Claude-generated file](api/compliance/apps/chats/generated_files/download.md)

GET/v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}/content

##### ModelsExpand Collapse

GeneratedFileRetrieveResponse object { id, claude\_chat\_id, created\_at, 4 more }

Metadata for GET /v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}.

Returns metadata only. Use the sibling `/content` endpoint to download
the bytes. The owning chat is included since the id is opaque; to find the
specific message that produced the file, fetch
`/v1/compliance/apps/chats/{claude_chat_id}/messages` and match on
`generated_files[].id`.

id: string

Opaque generated-file id, e.g. 'claude\_gen\_file\_abc123'.

claude\_chat\_id: string

The chat this generated file belongs to

created\_at: string

File creation timestamp from Filestore

filename: string

Display name of the generated file

md5: string

Lowercase hex MD5 of the stored file, as recorded by Filestore. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes.

mime\_type: string

MIME type as recorded by Filestore, when available

size\_bytes: number

Size in bytes of the stored file, when available

---

*Copyright © Anthropic. All rights reserved.*
