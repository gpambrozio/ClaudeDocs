# Resources

Copy page

Java

# Resources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

[BetaManagedAgentsFileResource](api/beta.md) beta().sessions().resources().add(ResourceAddParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

ResourceListPage beta().sessions().resources().list(ResourceListParamsparams = ResourceListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

[ResourceRetrieveResponse](api/beta.md) beta().sessions().resources().retrieve(ResourceRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

[ResourceUpdateResponse](api/beta.md) beta().sessions().resources().update(ResourceUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

[BetaManagedAgentsDeleteSessionResource](api/beta.md) beta().sessions().resources().delete(ResourceDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

##### ModelsExpand Collapse

class BetaManagedAgentsDeleteSessionResource:

Confirmation of resource deletion.

String id

Type type

class BetaManagedAgentsFileResource:

String id

LocalDateTime createdAt

A timestamp in RFC 3339 format

String fileId

String mountPath

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsGitHubRepositoryResource:

String id

LocalDateTime createdAt

A timestamp in RFC 3339 format

String mountPath

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

String url

Optional<Checkout> checkout

Accepts one of the following:

class BetaManagedAgentsBranchCheckout:

String name

Branch name to check out.

Type type

class BetaManagedAgentsCommitCheckout:

String sha

Full commit SHA to check out.

Type type

class BetaManagedAgentsSessionResource: A class that can be one of several variants.union

class BetaManagedAgentsGitHubRepositoryResource:

String id

LocalDateTime createdAt

A timestamp in RFC 3339 format

String mountPath

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

String url

Optional<Checkout> checkout

Accepts one of the following:

class BetaManagedAgentsBranchCheckout:

String name

Branch name to check out.

Type type

class BetaManagedAgentsCommitCheckout:

String sha

Full commit SHA to check out.

Type type

class BetaManagedAgentsFileResource:

String id

LocalDateTime createdAt

A timestamp in RFC 3339 format

String fileId

String mountPath

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

---

*Copyright © Anthropic. All rights reserved.*
