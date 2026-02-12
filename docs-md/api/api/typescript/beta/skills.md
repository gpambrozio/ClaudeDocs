# Skills

Copy page

TypeScript

# Skills

##### [Create Skill](api/beta/skills/create.md)

client.beta.skills.create(SkillCreateParams { display\_title, files, betas } params?, RequestOptionsoptions?): [SkillCreateResponse](api/beta.md) { id, created\_at, display\_title, 4 more }

POST/v1/skills

##### [List Skills](api/beta/skills/list.md)

client.beta.skills.list(SkillListParams { limit, page, source, betas } params?, RequestOptionsoptions?): PageCursor<[SkillListResponse](api/beta.md) { id, created\_at, display\_title, 4 more } >

GET/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

client.beta.skills.retrieve(stringskillID, SkillRetrieveParams { betas } params?, RequestOptionsoptions?): [SkillRetrieveResponse](api/beta.md) { id, created\_at, display\_title, 4 more }

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

client.beta.skills.delete(stringskillID, SkillDeleteParams { betas } params?, RequestOptionsoptions?): [SkillDeleteResponse](api/beta.md) { id, type }

DELETE/v1/skills/{skill\_id}

#### SkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

client.beta.skills.versions.create(stringskillID, VersionCreateParams { files, betas } params?, RequestOptionsoptions?): [VersionCreateResponse](api/beta.md) { id, created\_at, description, 5 more }

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

client.beta.skills.versions.list(stringskillID, VersionListParams { limit, page, betas } params?, RequestOptionsoptions?): PageCursor<[VersionListResponse](api/beta.md) { id, created\_at, description, 5 more } >

GET/v1/skills/{skill\_id}/versions

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

client.beta.skills.versions.retrieve(stringversion, VersionRetrieveParams { skill\_id, betas } params, RequestOptionsoptions?): [VersionRetrieveResponse](api/beta.md) { id, created\_at, description, 5 more }

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

client.beta.skills.versions.delete(stringversion, VersionDeleteParams { skill\_id, betas } params, RequestOptionsoptions?): [VersionDeleteResponse](api/beta.md) { id, type }

DELETE/v1/skills/{skill\_id}/versions/{version}

---

*Copyright © Anthropic. All rights reserved.*
