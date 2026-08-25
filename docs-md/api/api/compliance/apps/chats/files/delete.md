# Delete file

Copy page



# Delete file

DELETE/v1/compliance/apps/chats/files/{claude\_file\_id}

Permanently deletes a specific file. This is a destructive
operation that cannot be undone.

##### Path parameters

claude\_file\_id: string

The file ID (tagged ID, e.g., claude\_file\_abc123)

##### Headers

"x-api-key": optional string

##### Returns

id: string

The ID of the file that was deleted



type: optional "claude\_file\_deleted"

Constant string confirming deletion

defaultclaude\_file\_deleted

### Delete file

cURL



```shiki
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```shiki
{
  "id": "claude_file_xyz789",
  "type": "claude_file_deleted"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "claude_file_xyz789",
  "type": "claude_file_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
