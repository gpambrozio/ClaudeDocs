# Versions

Copy page

Java

# Versions

##### [Create Skill Version](api/beta/skills/versions/create.md)

[VersionCreateResponse](api/beta.md) beta().skills().versions().create(VersionCreateParamsparams = VersionCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

post/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

VersionListPage beta().skills().versions().list(VersionListParamsparams = VersionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

get/v1/skills/{skill\_id}/versions

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

[VersionRetrieveResponse](api/beta.md) beta().skills().versions().retrieve(VersionRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

get/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

[VersionDeleteResponse](api/beta.md) beta().skills().versions().delete(VersionDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

delete/v1/skills/{skill\_id}/versions/{version}