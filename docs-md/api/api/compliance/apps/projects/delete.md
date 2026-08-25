# Delete project

Copy page



# Delete project

DELETE/v1/compliance/apps/projects/{project\_id}

Delete a project for compliance purposes.

Hard-deletes the project and all its associated data including:

- All project documents and files
- All role assignments
- Knowledge base (if RAG is enabled)
- Sync sources

Project must have no attached chats - returns 409 if chats exist.

##### Path parameters

project\_id: string

The project ID (tagged ID, e.g., claude\_proj\_abc123)

##### Headers

"x-api-key": optional string

##### Returns

id: string

The ID of the Claude project that was deleted



type: optional "claude\_project\_deleted"

Constant string confirming deletion.

defaultclaude\_project\_deleted

### Delete project

cURL



```shiki
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```shiki
{
  "id": "id",
  "type": "claude_project_deleted"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "id",
  "type": "claude_project_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
