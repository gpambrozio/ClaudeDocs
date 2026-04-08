# Skills

Copy page

cURL

# Skills

##### [Create Skill](api/beta/skills/create.md)

POST/v1/skills

##### [List Skills](api/beta/skills/list.md)

GET/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

DELETE/v1/skills/{skill\_id}

##### ModelsExpand Collapse

SkillCreateResponse = object { id, created\_at, display\_title, 4 more }

id: string

Unique identifier for the skill.

The format and length of IDs may change over time.

created\_at: string

ISO 8601 timestamp of when the skill was created.

display\_title: string

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.

latest\_version: string

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.

source: string

Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic

type: string

Object type.

For Skills, this is always `"skill"`.

updated\_at: string

ISO 8601 timestamp of when the skill was last updated.

SkillListResponse = object { id, created\_at, display\_title, 4 more }

id: string

Unique identifier for the skill.

The format and length of IDs may change over time.

created\_at: string

ISO 8601 timestamp of when the skill was created.

display\_title: string

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.

latest\_version: string

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.

source: string

Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic

type: string

Object type.

For Skills, this is always `"skill"`.

updated\_at: string

ISO 8601 timestamp of when the skill was last updated.

SkillRetrieveResponse = object { id, created\_at, display\_title, 4 more }

id: string

Unique identifier for the skill.

The format and length of IDs may change over time.

created\_at: string

ISO 8601 timestamp of when the skill was created.

display\_title: string

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.

latest\_version: string

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.

source: string

Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic

type: string

Object type.

For Skills, this is always `"skill"`.

updated\_at: string

ISO 8601 timestamp of when the skill was last updated.

SkillDeleteResponse = object { id, type }

id: string

Unique identifier for the skill.

The format and length of IDs may change over time.

type: string

Deleted object type.

For Skills, this is always `"skill_deleted"`.

#### SkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

GET/v1/skills/{skill\_id}/versions

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

DELETE/v1/skills/{skill\_id}/versions/{version}

##### ModelsExpand Collapse

VersionCreateResponse = object { id, created\_at, description, 5 more }

id: string

Unique identifier for the skill version.

The format and length of IDs may change over time.

created\_at: string

ISO 8601 timestamp of when the skill version was created.

description: string

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.

directory: string

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.

name: string

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

skill\_id: string

Identifier for the skill that this version belongs to.

type: string

Object type.

For Skill Versions, this is always `"skill_version"`.

version: string

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

VersionListResponse = object { id, created\_at, description, 5 more }

id: string

Unique identifier for the skill version.

The format and length of IDs may change over time.

created\_at: string

ISO 8601 timestamp of when the skill version was created.

description: string

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.

directory: string

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.

name: string

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

skill\_id: string

Identifier for the skill that this version belongs to.

type: string

Object type.

For Skill Versions, this is always `"skill_version"`.

version: string

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

VersionRetrieveResponse = object { id, created\_at, description, 5 more }

id: string

Unique identifier for the skill version.

The format and length of IDs may change over time.

created\_at: string

ISO 8601 timestamp of when the skill version was created.

description: string

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.

directory: string

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.

name: string

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

skill\_id: string

Identifier for the skill that this version belongs to.

type: string

Object type.

For Skill Versions, this is always `"skill_version"`.

version: string

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

VersionDeleteResponse = object { id, type }

id: string

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

type: string

Deleted object type.

For Skill Versions, this is always `"skill_version_deleted"`.

---

*Copyright © Anthropic. All rights reserved.*
