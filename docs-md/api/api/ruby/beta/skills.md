# Skills

Copy page

Ruby

# Skills

##### [Create Skill](api/beta/skills/create.md)

beta.skills.create(\*\*kwargs) -> [SkillCreateResponse](api/beta.md) { id, created\_at, display\_title, 4 more }

post/v1/skills

##### [List Skills](api/beta/skills/list.md)

beta.skills.list(\*\*kwargs) -> PageCursor<[SkillListResponse](api/beta.md) { id, created\_at, display\_title, 4 more } >

get/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

beta.skills.retrieve(skill\_id, \*\*kwargs) -> [SkillRetrieveResponse](api/beta.md) { id, created\_at, display\_title, 4 more }

get/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

beta.skills.delete(skill\_id, \*\*kwargs) -> [SkillDeleteResponse](api/beta.md) { id, type }

delete/v1/skills/{skill\_id}

#### SkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

beta.skills.versions.create(skill\_id, \*\*kwargs) -> [VersionCreateResponse](api/beta.md) { id, created\_at, description, 5 more }

post/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

beta.skills.versions.list(skill\_id, \*\*kwargs) -> PageCursor<[VersionListResponse](api/beta.md) { id, created\_at, description, 5 more } >

get/v1/skills/{skill\_id}/versions

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

beta.skills.versions.retrieve(version, \*\*kwargs) -> [VersionRetrieveResponse](api/beta.md) { id, created\_at, description, 5 more }

get/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

beta.skills.versions.delete(version, \*\*kwargs) -> [VersionDeleteResponse](api/beta.md) { id, type }

delete/v1/skills/{skill\_id}/versions/{version}