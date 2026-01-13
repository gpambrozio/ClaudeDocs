# Skills

Copy page

Kotlin

# Skills

##### [Create Skill](api/beta/skills/create.md)

beta().skills().create(SkillCreateParamsparams = SkillCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : [SkillCreateResponse](api/beta.md)

post/v1/skills

##### [List Skills](api/beta/skills/list.md)

beta().skills().list(SkillListParamsparams = SkillListParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : SkillListPage

get/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

beta().skills().retrieve(SkillRetrieveParamsparams = SkillRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : [SkillRetrieveResponse](api/beta.md)

get/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

beta().skills().delete(SkillDeleteParamsparams = SkillDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : [SkillDeleteResponse](api/beta.md)

delete/v1/skills/{skill\_id}

#### SkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

beta().skills().versions().create(VersionCreateParamsparams = VersionCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : [VersionCreateResponse](api/beta.md)

post/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

beta().skills().versions().list(VersionListParamsparams = VersionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : VersionListPage

get/v1/skills/{skill\_id}/versions

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

beta().skills().versions().retrieve(VersionRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none()) : [VersionRetrieveResponse](api/beta.md)

get/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

beta().skills().versions().delete(VersionDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none()) : [VersionDeleteResponse](api/beta.md)

delete/v1/skills/{skill\_id}/versions/{version}