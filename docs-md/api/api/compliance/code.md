# Code

Copy page





To enable the Compliance API, see [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Code

#### CodeArtifacts

##### [List Code Artifacts](api/compliance/code/artifacts/list.md)

GET/v1/compliance/code/artifacts

##### [Download Code Artifact Version Content](api/compliance/code/artifacts/retrieve_version.md)

GET/v1/compliance/code/artifacts/{artifact\_id}/versions/{version\_id}

##### [Delete Code Artifact](api/compliance/code/artifacts/delete.md)

DELETE/v1/compliance/code/artifacts/{artifact\_id}

##### ModelsExpand Collapse



ArtifactListResponse object { id, organization\_id, organization\_uuid, 6 more } 

A hosted site published via Claude Code.

id: string

Artifact identifier (tagged ID)

Deprecatedorganization\_id: string

Organization identifier (tagged ID)

organization\_uuid: string

Organization UUID this Artifact belongs to

owner\_user\_id: string

Artifact owner's user identifier (tagged ID). Always set, so attribution survives after the owner's account is deleted or the owner leaves every organization under the parent.

published\_version\_id: string

Identifier of the version a non-owner viewer would render when `read_mode` permits them — the version the owner has pinned for non-owner readers if one is pinned, otherwise the owner's latest. When `read_mode` is `owner` no non-owner renders any version; the field still reports which version would be served were read\_mode widened.



read\_mode: "org" or "owner" or "users"

Who can view this Artifact: only its owner, a named set of users, or every member of its organization

One of the following:

"org"

"owner"

"users"

updated\_at: string

Artifact last update timestamp, or null for Artifacts published before this field was recorded



user: object { id, email\_address } 

The user who owns a Code Artifact.

Fields that reference this type are null when the owner's account has
been deleted or the owner is no longer a member of any organization
under the parent organization.

id: string

User identifier (tagged ID)

email\_address: string

User's email address



versions: array of object { id, created\_at, name } 

Up to roughly 20 most-recently-published versions of this Artifact (older versions are not retained). Metadata only — use `GET /v1/compliance/code/artifacts/{artifact_id}/versions/{version_id}` to download a version's content.

id: string

Opaque version identifier

created\_at: string

When this version was published

name: string

Artifact title at this version. Falls back to the version identifier when the title for an older version is no longer retained.



ArtifactDeleteResponse object { id, type } 

Response for deleting a Code Artifact.

id: string

The ID of the Artifact that was deleted

type: "code\_artifact\_deleted"

Constant string confirming deletion

---

*Copyright © Anthropic. All rights reserved.*
