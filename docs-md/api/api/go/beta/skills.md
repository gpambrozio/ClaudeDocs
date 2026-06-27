# Skills

Copy page



Go

# Skills

##### [Create Skill](api/beta/skills/create.md)

client.Beta.Skills.New(ctx, params) (\*[BetaSkillNewResponse](api/beta/skills.md), error)

POST/v1/skills

##### [List Skills](api/beta/skills/list.md)

client.Beta.Skills.List(ctx, params) (\*PageCursor[[BetaSkillListResponse](api/beta/skills.md)], error)

GET/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

client.Beta.Skills.Get(ctx, skillID, query) (\*[BetaSkillGetResponse](api/beta/skills.md), error)

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

client.Beta.Skills.Delete(ctx, skillID, body) (\*[BetaSkillDeleteResponse](api/beta/skills.md), error)

DELETE/v1/skills/{skill\_id}

#### SkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

client.Beta.Skills.Versions.New(ctx, skillID, params) (\*[BetaSkillVersionNewResponse](api/beta/skills/versions.md), error)

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

client.Beta.Skills.Versions.List(ctx, skillID, params) (\*PageCursor[[BetaSkillVersionListResponse](api/beta/skills/versions.md)], error)

GET/v1/skills/{skill\_id}/versions

##### [Download Skill Version Content](api/beta/skills/versions/download.md)

client.Beta.Skills.Versions.Download(ctx, version, params) (\*Response, error)

GET/v1/skills/{skill\_id}/versions/{version}/content

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

client.Beta.Skills.Versions.Get(ctx, version, params) (\*[BetaSkillVersionGetResponse](api/beta/skills/versions.md), error)

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

client.Beta.Skills.Versions.Delete(ctx, version, params) (\*[BetaSkillVersionDeleteResponse](api/beta/skills/versions.md), error)

DELETE/v1/skills/{skill\_id}/versions/{version}

---

*Copyright © Anthropic. All rights reserved.*
