# Artifacts

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](manage-claude/compliance-api-access.md)

Copy page



# Artifacts

##### [Get artifact metadata](api/http/compliance/apps/artifacts/retrieve.md)

GET/v1/compliance/apps/artifacts/{artifact\_version\_id}

##### [Download artifact content](api/http/compliance/apps/artifacts/download.md)

GET/v1/compliance/apps/artifacts/{artifact\_version\_id}/content

##### Models



ArtifactRetrieveResponse object{ id, artifact\_type, claude\_chat\_id, 5 more }

Artifact version metadata for GET /v1/compliance/apps/artifacts/{artifact\_version\_id}.

Returns metadata only. Use the sibling `/content` endpoint to fetch the
artifact body.

id: string

Artifact ID e.g. 'claude\_artifact\_abc123'

artifact\_type: string or null

MIME-like artifact type e.g. 'application/vnd.ant.code'

claude\_chat\_id: string

The chat this artifact belongs to



created\_at: string

Artifact version creation timestamp

formatdate-time

md5: string

Lowercase hex MD5 of the artifact content (UTF-8 encoded). Matches the `content` field returned by the sibling `/content` endpoint.

size\_bytes: number

Size in bytes of the artifact content (UTF-8 encoded)

title: string or null

Artifact title

version\_id: string

Artifact version ID e.g. 'claude\_artifact\_version\_abc123'

---

*Copyright © Anthropic. All rights reserved.*
