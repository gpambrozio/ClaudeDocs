# Versions

Copy page

Ruby

# Versions

##### [Create Skill Version](api/beta/skills/versions/create.md)

beta.skills.versions.create(skill\_id, \*\*kwargs) -> [VersionCreateResponse](api/beta.md) { id, created\_at, description, 5 more }

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

beta.skills.versions.list(skill\_id, \*\*kwargs) -> PageCursor<[VersionListResponse](api/beta.md) { id, created\_at, description, 5 more } >

GET/v1/skills/{skill\_id}/versions

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

beta.skills.versions.retrieve(version, \*\*kwargs) -> [VersionRetrieveResponse](api/beta.md) { id, created\_at, description, 5 more }

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

beta.skills.versions.delete(version, \*\*kwargs) -> [VersionDeleteResponse](api/beta.md) { id, type }

DELETE/v1/skills/{skill\_id}/versions/{version}

##### ModelsExpand Collapse

class VersionCreateResponse { id, created\_at, description, 5 more }

id: String

Unique identifier for the skill version.

The format and length of IDs may change over time.

created\_at: String

ISO 8601 timestamp of when the skill version was created.

description: String

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.

directory: String

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.

name: String

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

skill\_id: String

Identifier for the skill that this version belongs to.

type: String

Object type.

For Skill Versions, this is always `"skill_version"`.

version: String

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

class VersionListResponse { id, created\_at, description, 5 more }

id: String

Unique identifier for the skill version.

The format and length of IDs may change over time.

created\_at: String

ISO 8601 timestamp of when the skill version was created.

description: String

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.

directory: String

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.

name: String

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

skill\_id: String

Identifier for the skill that this version belongs to.

type: String

Object type.

For Skill Versions, this is always `"skill_version"`.

version: String

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

class VersionRetrieveResponse { id, created\_at, description, 5 more }

id: String

Unique identifier for the skill version.

The format and length of IDs may change over time.

created\_at: String

ISO 8601 timestamp of when the skill version was created.

description: String

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.

directory: String

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.

name: String

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

skill\_id: String

Identifier for the skill that this version belongs to.

type: String

Object type.

For Skill Versions, this is always `"skill_version"`.

version: String

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

class VersionDeleteResponse { id, type }

id: String

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

type: String

Deleted object type.

For Skill Versions, this is always `"skill_version_deleted"`.

---

*Copyright © Anthropic. All rights reserved.*
