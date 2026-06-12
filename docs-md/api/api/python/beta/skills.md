# Skills

Copy page

SDK language

Python

# Skills

##### [Create Skill](api/beta/skills/create.md)

beta.skills.create(SkillCreateParams\*\*kwargs)  -> [SkillCreateResponse](api/beta.md)

POST/v1/skills

##### [List Skills](api/beta/skills/list.md)

beta.skills.list(SkillListParams\*\*kwargs)  -> SyncPageCursor[[SkillListResponse](api/beta.md)]

GET/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

beta.skills.retrieve(strskill\_id, SkillRetrieveParams\*\*kwargs)  -> [SkillRetrieveResponse](api/beta.md)

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

beta.skills.delete(strskill\_id, SkillDeleteParams\*\*kwargs)  -> [SkillDeleteResponse](api/beta.md)

DELETE/v1/skills/{skill\_id}

##### ModelsExpand Collapse



class SkillCreateResponse: …



id: str

Unique identifier for the skill.

The format and length of IDs may change over time.

created\_at: str

ISO 8601 timestamp of when the skill was created.



display\_title: Optional[str]

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.



latest\_version: Optional[str]

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.



source: str

Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic



type: str

Object type.

For Skills, this is always `"skill"`.

updated\_at: str

ISO 8601 timestamp of when the skill was last updated.



class SkillListResponse: …



id: str

Unique identifier for the skill.

The format and length of IDs may change over time.

created\_at: str

ISO 8601 timestamp of when the skill was created.



display\_title: Optional[str]

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.



latest\_version: Optional[str]

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.



source: str

Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic



type: str

Object type.

For Skills, this is always `"skill"`.

updated\_at: str

ISO 8601 timestamp of when the skill was last updated.



class SkillRetrieveResponse: …



id: str

Unique identifier for the skill.

The format and length of IDs may change over time.

created\_at: str

ISO 8601 timestamp of when the skill was created.



display\_title: Optional[str]

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.



latest\_version: Optional[str]

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.



source: str

Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic



type: str

Object type.

For Skills, this is always `"skill"`.

updated\_at: str

ISO 8601 timestamp of when the skill was last updated.



class SkillDeleteResponse: …



id: str

Unique identifier for the skill.

The format and length of IDs may change over time.



type: str

Deleted object type.

For Skills, this is always `"skill_deleted"`.

#### SkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

beta.skills.versions.create(strskill\_id, VersionCreateParams\*\*kwargs)  -> [VersionCreateResponse](api/beta.md)

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

beta.skills.versions.list(strskill\_id, VersionListParams\*\*kwargs)  -> SyncPageCursor[[VersionListResponse](api/beta.md)]

GET/v1/skills/{skill\_id}/versions

##### [Download Skill Version Content](api/beta/skills/versions/download.md)

beta.skills.versions.download(strversion, VersionDownloadParams\*\*kwargs)  -> BinaryResponseContent

GET/v1/skills/{skill\_id}/versions/{version}/content

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

beta.skills.versions.retrieve(strversion, VersionRetrieveParams\*\*kwargs)  -> [VersionRetrieveResponse](api/beta.md)

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

beta.skills.versions.delete(strversion, VersionDeleteParams\*\*kwargs)  -> [VersionDeleteResponse](api/beta.md)

DELETE/v1/skills/{skill\_id}/versions/{version}

##### ModelsExpand Collapse



class VersionCreateResponse: …



id: str

Unique identifier for the skill version.

The format and length of IDs may change over time.

created\_at: str

ISO 8601 timestamp of when the skill version was created.



description: str

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.



directory: str

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.



name: str

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

skill\_id: str

Identifier for the skill that this version belongs to.



type: str

Object type.

For Skill Versions, this is always `"skill_version"`.



version: str

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").



class VersionListResponse: …



id: str

Unique identifier for the skill version.

The format and length of IDs may change over time.

created\_at: str

ISO 8601 timestamp of when the skill version was created.



description: str

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.



directory: str

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.



name: str

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

skill\_id: str

Identifier for the skill that this version belongs to.



type: str

Object type.

For Skill Versions, this is always `"skill_version"`.



version: str

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").



class VersionRetrieveResponse: …



id: str

Unique identifier for the skill version.

The format and length of IDs may change over time.

created\_at: str

ISO 8601 timestamp of when the skill version was created.



description: str

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.



directory: str

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.



name: str

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

skill\_id: str

Identifier for the skill that this version belongs to.



type: str

Object type.

For Skill Versions, this is always `"skill_version"`.



version: str

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").



class VersionDeleteResponse: …



id: str

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").



type: str

Deleted object type.

For Skill Versions, this is always `"skill_version_deleted"`.

---

*Copyright © Anthropic. All rights reserved.*
