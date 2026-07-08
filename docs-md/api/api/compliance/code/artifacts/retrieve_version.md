# Download Code Artifact Version Content

Copy page





To enable the Compliance API, see [Set up the Compliance API](manage-claude/compliance-api-access.md).

# Download Code Artifact Version Content

GET/v1/compliance/apps/code/artifacts/{artifact\_id}/versions/{version\_id}

Streams the content of one version of a Claude Code Artifact as the
response body.

Returns 404 for Artifacts that don't exist or belong to another parent
organization. A listed version id can start returning 404 if subsequent
publishes rotated it out of retained history — re-list on 404. Returns
503 while the version's content upload is
still in flight or was abandoned — retry with backoff. Oversized
encoded content aborts mid-stream: headers and initial bytes arrive
but the body terminates early — an aborted chunked transfer is the
only truncation signal for encoded content. `Content-MD5` is emitted
only for identity-stored content; validate against it when present.

##### Path ParametersExpand Collapse

artifact\_id: string

The Artifact ID (tagged ID, e.g., cart\_abc123)

version\_id: string

Opaque version identifier from the Artifact's `versions` list

##### Header ParametersExpand Collapse

"x-api-key": optional string

Download Code Artifact Version Content



```shiki
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts/$ARTIFACT_ID/versions/$VERSION_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
