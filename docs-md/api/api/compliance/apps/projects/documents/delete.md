# Delete project document

Copy page



# Delete project document

DELETE/v1/compliance/apps/projects/documents/{document\_id}

Delete a project document for compliance purposes.

Hard-deletes the project document permanently.

##### Path parameters

document\_id: string

The document ID (tagged ID, e.g., claude\_proj\_doc\_abc123)

##### Headers

"x-api-key": optional string

##### Returns

id: string

The ID of the project document that was deleted



type: "claude\_project\_document\_deleted"

Constant string confirming deletion.

defaultclaude\_project\_document\_deleted

### Delete project document

cURL



```shiki
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```shiki
{
  "id": "id",
  "type": "claude_project_document_deleted"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "id",
  "type": "claude_project_document_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
