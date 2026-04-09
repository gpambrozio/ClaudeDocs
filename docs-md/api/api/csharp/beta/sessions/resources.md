# Resources

Copy page

C#

# Resources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

[BetaManagedAgentsFileResource](api/beta.md) Beta.Sessions.Resources.Add(ResourceAddParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

[ResourceListPageResponse](api/beta.md) Beta.Sessions.Resources.List(ResourceListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

[ResourceRetrieveResponse](api/beta.md) Beta.Sessions.Resources.Retrieve(ResourceRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

[ResourceUpdateResponse](api/beta.md) Beta.Sessions.Resources.Update(ResourceUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

[BetaManagedAgentsDeleteSessionResource](api/beta.md) Beta.Sessions.Resources.Delete(ResourceDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

##### ModelsExpand Collapse

class BetaManagedAgentsDeleteSessionResource:

Confirmation of resource deletion.

required string ID

required Type Type

class BetaManagedAgentsFileResource:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string FileID

required string MountPath

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsGitHubRepositoryResource:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string MountPath

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required string Url

Checkout? Checkout

Accepts one of the following:

class BetaManagedAgentsBranchCheckout:

required string Name

Branch name to check out.

required Type Type

class BetaManagedAgentsCommitCheckout:

required string Sha

Full commit SHA to check out.

required Type Type

class BetaManagedAgentsSessionResource: A class that can be one of several variants.union

class BetaManagedAgentsGitHubRepositoryResource:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string MountPath

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required string Url

Checkout? Checkout

Accepts one of the following:

class BetaManagedAgentsBranchCheckout:

required string Name

Branch name to check out.

required Type Type

class BetaManagedAgentsCommitCheckout:

required string Sha

Full commit SHA to check out.

required Type Type

class BetaManagedAgentsFileResource:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string FileID

required string MountPath

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

---

*Copyright © Anthropic. All rights reserved.*
