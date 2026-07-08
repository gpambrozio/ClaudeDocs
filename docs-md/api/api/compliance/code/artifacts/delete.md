# Delete Code Artifact

Copy page





To enable the Compliance API, see [Set up the Compliance API](manage-claude/compliance-api-access.md).

# Delete Code Artifact

DELETE/v1/compliance/apps/code/artifacts/{artifact\_id}

Permanently deletes a Code Artifact and all its versions. This is a
destructive operation that cannot be undone. A 200 response means the
deletion is initiated and the Artifact is claimed; content removal
completes asynchronously.

Returns 404 for Artifacts that don't exist or belong to another parent
organization. Returns 404 on a repeated delete of an already-deleted
Artifact.

##### Path ParametersExpand Collapse

artifact\_id: string

The Artifact ID (tagged ID, e.g., cart\_abc123)

##### Header ParametersExpand Collapse

"x-api-key": optional string

##### ReturnsExpand Collapse

id: string

The ID of the Artifact that was deleted

type: "code\_artifact\_deleted"

Constant string confirming deletion

Delete Code Artifact



```shiki
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts/$ARTIFACT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```shiki
{
  "id": "cart_xyz789",
  "type": "code_artifact_deleted"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "cart_xyz789",
  "type": "code_artifact_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
