# Get file metadata

Copy page

The Compliance API is available only on the Claude Enterprise plan and must be enabled before use. See [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Get file metadata

GET/v1/compliance/apps/chats/files/{claude\_file\_id}

Retrieves metadata for a file referenced in chat messages, without
downloading the file content. Use the sibling `/content` endpoint to
download the bytes.

##### Path ParametersExpand Collapse

claude\_file\_id: string

The file ID (tagged ID, e.g., claude\_file\_abc123)

##### Header ParametersExpand Collapse

"x-api-key": optional string

##### ReturnsExpand Collapse

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

Get file metadata

```shiki
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200

```shiki
{
  "id": "claude_file_xyz789",
  "filename": "quarterly_report.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 1048576,
  "created_at": "2024-01-15T10:30:00Z",
  "message_ids": [
    "claude_chat_msg_abc123"
  ]
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "claude_file_xyz789",
  "filename": "quarterly_report.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 1048576,
  "created_at": "2024-01-15T10:30:00Z",
  "message_ids": [
    "claude_chat_msg_abc123"
  ]
}
```

---

*Copyright © Anthropic. All rights reserved.*
