# Skills

Copy page



C#

# Skills

##### [Create Skill](api/beta/skills/create.md)

[SkillCreateResponse](api/beta/skills.md) Beta.Skills.Create(SkillCreateParams?parameters, CancellationTokencancellationToken = default)

POST/v1/skills

##### [List Skills](api/beta/skills/list.md)

[SkillListPageResponse](api/beta/skills.md) Beta.Skills.List(SkillListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

[SkillRetrieveResponse](api/beta/skills.md) Beta.Skills.Retrieve(SkillRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

[SkillDeleteResponse](api/beta/skills.md) Beta.Skills.Delete(SkillDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/skills/{skill\_id}

#### SkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

[VersionCreateResponse](api/beta/skills/versions.md) Beta.Skills.Versions.Create(VersionCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

[VersionListPageResponse](api/beta/skills/versions.md) Beta.Skills.Versions.List(VersionListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/skills/{skill\_id}/versions

##### [Download Skill Version Content](api/beta/skills/versions/download.md)

HttpResponse Beta.Skills.Versions.Download(VersionDownloadParamsparameters, CancellationTokencancellationToken = default)

GET/v1/skills/{skill\_id}/versions/{version}/content

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

[VersionRetrieveResponse](api/beta/skills/versions.md) Beta.Skills.Versions.Retrieve(VersionRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

[VersionDeleteResponse](api/beta/skills/versions.md) Beta.Skills.Versions.Delete(VersionDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/skills/{skill\_id}/versions/{version}

---

*Copyright © Anthropic. All rights reserved.*
