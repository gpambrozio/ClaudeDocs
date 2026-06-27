# Skills

Copy page



Python

# Skills

##### [Create Skill](api/beta/skills/create.md)

beta.skills.create(SkillCreateParams\*\*kwargs)  -> [SkillCreateResponse](api/beta/skills.md)

POST/v1/skills

##### [List Skills](api/beta/skills/list.md)

beta.skills.list(SkillListParams\*\*kwargs)  -> SyncPageCursor[[SkillListResponse](api/beta/skills.md)]

GET/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

beta.skills.retrieve(strskill\_id, SkillRetrieveParams\*\*kwargs)  -> [SkillRetrieveResponse](api/beta/skills.md)

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

beta.skills.delete(strskill\_id, SkillDeleteParams\*\*kwargs)  -> [SkillDeleteResponse](api/beta/skills.md)

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

beta.skills.versions.create(strskill\_id, VersionCreateParams\*\*kwargs)  -> [VersionCreateResponse](api/beta/skills/versions.md)

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

beta.skills.versions.list(strskill\_id, VersionListParams\*\*kwargs)  -> SyncPageCursor[[VersionListResponse](api/beta/skills/versions.md)]

GET/v1/skills/{skill\_id}/versions

##### [Download Skill Version Content](api/beta/skills/versions/download.md)

beta.skills.versions.download(strversion, VersionDownloadParams\*\*kwargs)  -> BinaryResponseContent

GET/v1/skills/{skill\_id}/versions/{version}/content

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

beta.skills.versions.retrieve(strversion, VersionRetrieveParams\*\*kwargs)  -> [VersionRetrieveResponse](api/beta/skills/versions.md)

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

beta.skills.versions.delete(strversion, VersionDeleteParams\*\*kwargs)  -> [VersionDeleteResponse](api/beta/skills/versions.md)

DELETE/v1/skills/{skill\_id}/versions/{version}

---

*Copyright © Anthropic. All rights reserved.*
