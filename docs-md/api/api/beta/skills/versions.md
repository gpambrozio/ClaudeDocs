# Versions

Copy page



cURL

# Versions

##### [Create Skill Version](api/beta/skills/versions/create.md)

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

GET/v1/skills/{skill\_id}/versions

##### [Download Skill Version Content](api/beta/skills/versions/download.md)

GET/v1/skills/{skill\_id}/versions/{version}/content

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

DELETE/v1/skills/{skill\_id}/versions/{version}

##### ModelsExpand Collapse



VersionCreateResponse object { id, created\_at, description, 5 more } 



id: string

Unique identifier for the skill version.

The format and length of IDs may change over time.

created\_at: string

ISO 8601 timestamp of when the skill version was created.



description: string

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.



directory: string

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.



name: string

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

skill\_id: string

Identifier for the skill that this version belongs to.



type: string

Object type.

For Skill Versions, this is always `"skill_version"`.



version: string

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").



VersionListResponse object { id, created\_at, description, 5 more } 



id: string

Unique identifier for the skill version.

The format and length of IDs may change over time.

created\_at: string

ISO 8601 timestamp of when the skill version was created.



description: string

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.



directory: string

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.



name: string

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

skill\_id: string

Identifier for the skill that this version belongs to.



type: string

Object type.

For Skill Versions, this is always `"skill_version"`.



version: string

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").



VersionRetrieveResponse object { id, created\_at, description, 5 more } 



id: string

Unique identifier for the skill version.

The format and length of IDs may change over time.

created\_at: string

ISO 8601 timestamp of when the skill version was created.



description: string

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.



directory: string

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.



name: string

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

skill\_id: string

Identifier for the skill that this version belongs to.



type: string

Object type.

For Skill Versions, this is always `"skill_version"`.



version: string

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").



VersionDeleteResponse object { id, type } 



id: string

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").



type: string

Deleted object type.

For Skill Versions, this is always `"skill_version_deleted"`.

---

*Copyright © Anthropic. All rights reserved.*
