# Resources

Copy page

Go

# Resources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

client.Beta.Sessions.Resources.Add(ctx, sessionID, params) (\*[BetaManagedAgentsFileResource](api/beta.md), error)

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

client.Beta.Sessions.Resources.List(ctx, sessionID, params) (\*PageCursor[[BetaManagedAgentsSessionResourceUnion](api/beta.md)], error)

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

client.Beta.Sessions.Resources.Get(ctx, resourceID, params) (\*[BetaSessionResourceGetResponseUnion](api/beta.md), error)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

client.Beta.Sessions.Resources.Update(ctx, resourceID, params) (\*[BetaSessionResourceUpdateResponseUnion](api/beta.md), error)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

client.Beta.Sessions.Resources.Delete(ctx, resourceID, params) (\*[BetaManagedAgentsDeleteSessionResource](api/beta.md), error)

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

##### ModelsExpand Collapse

type BetaManagedAgentsDeleteSessionResource struct{…}

Confirmation of resource deletion.

ID string

Type BetaManagedAgentsDeleteSessionResourceType

type BetaManagedAgentsFileResource struct{…}

ID string

CreatedAt Time

A timestamp in RFC 3339 format

FileID string

MountPath string

Type BetaManagedAgentsFileResourceType

UpdatedAt Time

A timestamp in RFC 3339 format

type BetaManagedAgentsGitHubRepositoryResource struct{…}

ID string

CreatedAt Time

A timestamp in RFC 3339 format

MountPath string

Type BetaManagedAgentsGitHubRepositoryResourceType

UpdatedAt Time

A timestamp in RFC 3339 format

URL string

Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnionoptional

Accepts one of the following:

type BetaManagedAgentsBranchCheckout struct{…}

Name string

Branch name to check out.

Type BetaManagedAgentsBranchCheckoutType

type BetaManagedAgentsCommitCheckout struct{…}

Sha string

Full commit SHA to check out.

Type BetaManagedAgentsCommitCheckoutType

type BetaManagedAgentsSessionResourceUnion interface{…}

Accepts one of the following:

type BetaManagedAgentsGitHubRepositoryResource struct{…}

ID string

CreatedAt Time

A timestamp in RFC 3339 format

MountPath string

Type BetaManagedAgentsGitHubRepositoryResourceType

UpdatedAt Time

A timestamp in RFC 3339 format

URL string

Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnionoptional

Accepts one of the following:

type BetaManagedAgentsBranchCheckout struct{…}

Name string

Branch name to check out.

Type BetaManagedAgentsBranchCheckoutType

type BetaManagedAgentsCommitCheckout struct{…}

Sha string

Full commit SHA to check out.

Type BetaManagedAgentsCommitCheckoutType

type BetaManagedAgentsFileResource struct{…}

ID string

CreatedAt Time

A timestamp in RFC 3339 format

FileID string

MountPath string

Type BetaManagedAgentsFileResourceType

UpdatedAt Time

A timestamp in RFC 3339 format

---

*Copyright © Anthropic. All rights reserved.*
