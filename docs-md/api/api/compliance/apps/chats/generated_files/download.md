# Download a Claude-generated file

Copy page





To enable the Compliance API, see [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Download a Claude-generated file

GET/v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}/content

Downloads the binary content of a file the assistant created via tool use.

##### Path ParametersExpand Collapse

claude\_gen\_file\_id: string

The generated-file id (e.g., 'claude\_gen\_file\_abc123') as returned in `chat_messages[].generated_files[].id` from GET /apps/chats/{claude\_chat\_id}/messages.

##### Header ParametersExpand Collapse

"x-api-key": optional string

Download a Claude-generated file



```shiki
curl https://api.anthropic.com/v1/compliance/apps/chats/generated-files/$CLAUDE_GEN_FILE_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
