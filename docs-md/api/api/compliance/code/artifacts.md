# Artifacts

Copy page



# Artifacts

##### [List Code Artifacts](api/http/compliance/code/artifacts/list.md)

GET/v1/compliance/apps/code/artifacts

##### [Download Code Artifact Version Content](api/http/compliance/code/artifacts/retrieve_version.md)

GET/v1/compliance/apps/code/artifacts/{artifact\_id}/versions/{version\_id}

##### [Delete Code Artifact](api/http/compliance/code/artifacts/delete.md)

DELETE/v1/compliance/apps/code/artifacts/{artifact\_id}

##### Models



ArtifactListResponse object{ id, organization\_uuid, owner\_user\_id, 5 more }

A hosted site published via Claude Code.



ArtifactDeleteResponse object{ id, type }

Response for deleting a Code Artifact.

id: string

The ID of the Artifact that was deleted



type: "code\_artifact\_deleted"

Constant string confirming deletion

defaultcode\_artifact\_deleted

---

*Copyright © Anthropic. All rights reserved.*
