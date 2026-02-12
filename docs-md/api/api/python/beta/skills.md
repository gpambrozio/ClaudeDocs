# Skills

Copy page

Python

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

#### SkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

beta.skills.versions.create(strskill\_id, VersionCreateParams\*\*kwargs)  -> [VersionCreateResponse](api/beta.md)

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

beta.skills.versions.list(strskill\_id, VersionListParams\*\*kwargs)  -> SyncPageCursor[[VersionListResponse](api/beta.md)]

GET/v1/skills/{skill\_id}/versions

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

beta.skills.versions.retrieve(strversion, VersionRetrieveParams\*\*kwargs)  -> [VersionRetrieveResponse](api/beta.md)

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

beta.skills.versions.delete(strversion, VersionDeleteParams\*\*kwargs)  -> [VersionDeleteResponse](api/beta.md)

DELETE/v1/skills/{skill\_id}/versions/{version}

---

*Copyright © Anthropic. All rights reserved.*
