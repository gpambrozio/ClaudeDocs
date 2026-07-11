# Skills

Copy page



TypeScript

# Skills

##### [Create Skill](api/beta/skills/create.md)

client.beta.skills.create(SkillCreateParams { files, display\_title, betas } params, RequestOptionsoptions?): [SkillCreateResponse](api/beta/skills.md) { id, created\_at, display\_title, 4 more }

POST/v1/skills

##### [List Skills](api/beta/skills/list.md)

client.beta.skills.list(SkillListParams { limit, page, source, betas } params?, RequestOptionsoptions?): PageCursor<[SkillListResponse](api/beta/skills.md) { id, created\_at, display\_title, 4 more } >

GET/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

client.beta.skills.retrieve(stringskillID, SkillRetrieveParams { betas } params?, RequestOptionsoptions?): [SkillRetrieveResponse](api/beta/skills.md) { id, created\_at, display\_title, 4 more }

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

client.beta.skills.delete(stringskillID, SkillDeleteParams { betas } params?, RequestOptionsoptions?): [SkillDeleteResponse](api/beta/skills.md) { id, type }

DELETE/v1/skills/{skill\_id}

##### ModelsExpand Collapse



SkillCreateResponse { id, created\_at, display\_title, 4 more } 



id: string

Unique identifier for the skill.

The format and length of IDs may change over time.

created\_at: string

ISO 8601 timestamp of when the skill was created.



display\_title: string | null

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.



latest\_version: string | null

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.



source: string

Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic



type: string

Object type.

For Skills, this is always `"skill"`.

updated\_at: string

ISO 8601 timestamp of when the skill was last updated.



SkillListResponse { id, created\_at, display\_title, 4 more } 



id: string

Unique identifier for the skill.

The format and length of IDs may change over time.

created\_at: string

ISO 8601 timestamp of when the skill was created.



display\_title: string | null

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.



latest\_version: string | null

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.



source: string

Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic



type: string

Object type.

For Skills, this is always `"skill"`.

updated\_at: string

ISO 8601 timestamp of when the skill was last updated.



SkillRetrieveResponse { id, created\_at, display\_title, 4 more } 



id: string

Unique identifier for the skill.

The format and length of IDs may change over time.

created\_at: string

ISO 8601 timestamp of when the skill was created.



display\_title: string | null

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.



latest\_version: string | null

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.



source: string

Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic



type: string

Object type.

For Skills, this is always `"skill"`.

updated\_at: string

ISO 8601 timestamp of when the skill was last updated.



SkillDeleteResponse { id, type } 



id: string

Unique identifier for the skill.

The format and length of IDs may change over time.



type: string

Deleted object type.

For Skills, this is always `"skill_deleted"`.

#### SkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

client.beta.skills.versions.create(stringskillID, VersionCreateParams { files, betas } params, RequestOptionsoptions?): [VersionCreateResponse](api/beta/skills/versions.md) { id, created\_at, description, 5 more }

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

client.beta.skills.versions.list(stringskillID, VersionListParams { limit, page, betas } params?, RequestOptionsoptions?): PageCursor<[VersionListResponse](api/beta/skills/versions.md) { id, created\_at, description, 5 more } >

GET/v1/skills/{skill\_id}/versions

##### [Download Skill Version Content](api/beta/skills/versions/download.md)

client.beta.skills.versions.download(stringversion, VersionDownloadParams { skill\_id, betas } params, RequestOptionsoptions?): Response

GET/v1/skills/{skill\_id}/versions/{version}/content

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

client.beta.skills.versions.retrieve(stringversion, VersionRetrieveParams { skill\_id, betas } params, RequestOptionsoptions?): [VersionRetrieveResponse](api/beta/skills/versions.md) { id, created\_at, description, 5 more }

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

client.beta.skills.versions.delete(stringversion, VersionDeleteParams { skill\_id, betas } params, RequestOptionsoptions?): [VersionDeleteResponse](api/beta/skills/versions.md) { id, type }

DELETE/v1/skills/{skill\_id}/versions/{version}

---

*Copyright © Anthropic. All rights reserved.*
