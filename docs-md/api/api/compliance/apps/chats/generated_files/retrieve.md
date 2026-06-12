# Get Claude-generated file metadata

Copy page



To enable the Compliance API, see [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Get Claude-generated file metadata

GET/v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}

Returns metadata for a file the assistant created via tool use.

Metadata is read from Filestore (the durable backing store for
per-conversation tool outputs). Use the sibling `/content` endpoint to
download the bytes.

##### Path ParametersExpand Collapse

claude\_gen\_file\_id: string

The generated-file id (e.g., 'claude\_gen\_file\_abc123') as returned in `chat_messages[].generated_files[].id` from GET /apps/chats/{claude\_chat\_id}/messages.

##### Header ParametersExpand Collapse

"x-api-key": optional string

##### ReturnsExpand Collapse

id: string

Opaque generated-file id, e.g. 'claude\_gen\_file\_abc123'.

claude\_chat\_id: string

The chat this generated file belongs to

created\_at: string

File creation timestamp from Filestore

filename: string

Display name of the generated file

md5: string

Lowercase hex MD5 of the stored file, as recorded by Filestore. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes.

mime\_type: string

MIME type as recorded by Filestore, when available

size\_bytes: number

Size in bytes of the stored file, when available

Get Claude-generated file metadata



```shiki
curl https://api.anthropic.com/v1/compliance/apps/chats/generated-files/$CLAUDE_GEN_FILE_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```shiki
{
  "id": "id",
  "claude_chat_id": "claude_chat_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "filename",
  "md5": "md5",
  "mime_type": "mime_type",
  "size_bytes": 0
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "id",
  "claude_chat_id": "claude_chat_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "filename",
  "md5": "md5",
  "mime_type": "mime_type",
  "size_bytes": 0
}
```

---

*Copyright © Anthropic. All rights reserved.*
