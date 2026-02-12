# Versions

Copy page

Go

# Versions

##### [Create Skill Version](api/beta/skills/versions/create.md)

client.Beta.Skills.Versions.New(ctx, skillID, params) (\*[BetaSkillVersionNewResponse](api/beta.md), error)

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

client.Beta.Skills.Versions.List(ctx, skillID, params) (\*PageCursor[[BetaSkillVersionListResponse](api/beta.md)], error)

GET/v1/skills/{skill\_id}/versions

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

client.Beta.Skills.Versions.Get(ctx, version, params) (\*[BetaSkillVersionGetResponse](api/beta.md), error)

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

client.Beta.Skills.Versions.Delete(ctx, version, params) (\*[BetaSkillVersionDeleteResponse](api/beta.md), error)

DELETE/v1/skills/{skill\_id}/versions/{version}

---

*Copyright © Anthropic. All rights reserved.*
