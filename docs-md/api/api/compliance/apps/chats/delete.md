# Delete chat

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](manage-claude/compliance-api-access.md)

Copy page



# Delete chat

DELETE/v1/compliance/apps/chats/{claude\_chat\_id}

Permanently deletes a chat and all associated messages and
files. This is a destructive operation that cannot be undone.

##### Path parameters

claude\_chat\_id: string

The chat ID (tagged ID, e.g., claude\_chat\_abc123)

##### Headers

"x-api-key": optional string

##### Returns

id: string

The ID of the Claude chat that was deleted



type: optional "claude\_chat\_deleted"

Constant string confirming deletion

defaultclaude\_chat\_deleted

Delete chat

cURL

```shiki
curl https://api.anthropic.com/v1/compliance/apps/chats/$CLAUDE_CHAT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```shiki
{
  "id": "claude_chat_abc123",
  "type": "claude_chat_deleted"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "claude_chat_abc123",
  "type": "claude_chat_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
