# Download a Claude-generated file

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](manage-claude/compliance-api-access.md)

Copy page



# Download a Claude-generated file

GET/v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}/content

Downloads the binary content of a file the assistant created via tool use.

##### Path parameters

claude\_gen\_file\_id: string

The generated-file id (e.g., 'claude\_gen\_file\_abc123') as returned in `chat_messages[].generated_files[].id` from GET /apps/chats/{claude\_chat\_id}/messages.

##### Headers

"x-api-key": optional string

Download a Claude-generated file

cURL

```shiki
curl https://api.anthropic.com/v1/compliance/apps/chats/generated-files/$CLAUDE_GEN_FILE_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

---

*Copyright © Anthropic. All rights reserved.*
