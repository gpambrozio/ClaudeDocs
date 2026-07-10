# Skills

Copy page



PHP

# Skills

##### [Create Skill](api/beta/skills/create.md)

$client->beta->skills->create(list<string> files, ?string displayTitle, ?list<AnthropicBeta> betas): [SkillNewResponse](api/beta/skills.md)

POST/v1/skills

##### [List Skills](api/beta/skills/list.md)

$client->beta->skills->list(?int limit, ?string page, ?string source, ?list<AnthropicBeta> betas): PageCursor<[SkillListResponse](api/beta/skills.md)>

GET/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

$client->beta->skills->retrieve(string skillID, ?list<AnthropicBeta> betas): [SkillGetResponse](api/beta/skills.md)

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

$client->beta->skills->delete(string skillID, ?list<AnthropicBeta> betas): [SkillDeleteResponse](api/beta/skills.md)

DELETE/v1/skills/{skill\_id}

#### SkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

$client->beta->skills->versions->create(string skillID, list<string> files, ?list<AnthropicBeta> betas): [VersionNewResponse](api/beta/skills/versions.md)

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

$client->beta->skills->versions->list(string skillID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[VersionListResponse](api/beta/skills/versions.md)>

GET/v1/skills/{skill\_id}/versions

##### [Download Skill Version Content](api/beta/skills/versions/download.md)

$client->beta->skills->versions->download(string version, string skillID, ?list<AnthropicBeta> betas): download

GET/v1/skills/{skill\_id}/versions/{version}/content

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

$client->beta->skills->versions->retrieve(string version, string skillID, ?list<AnthropicBeta> betas): [VersionGetResponse](api/beta/skills/versions.md)

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

$client->beta->skills->versions->delete(string version, string skillID, ?list<AnthropicBeta> betas): [VersionDeleteResponse](api/beta/skills/versions.md)

DELETE/v1/skills/{skill\_id}/versions/{version}

---

*Copyright © Anthropic. All rights reserved.*
