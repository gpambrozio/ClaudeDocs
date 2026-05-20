# Download file content

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](manage-claude/compliance-activity-feed.md) only. See [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Download file content

GET/v1/compliance/apps/chats/files/{claude\_file\_id}/content

Downloads the binary content of a file referenced in chat messages.

##### Path ParametersExpand Collapse

claude\_file\_id: string

The file ID (tagged ID, e.g., claude\_file\_abc123)

##### Header ParametersExpand Collapse

"x-api-key": optional string

Download file content

```shiki
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
