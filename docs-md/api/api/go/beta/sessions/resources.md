# Resources

Copy page



Go

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



type BetaManagedAgentsDeleteSessionResource struct{…}

Confirmation of resource deletion.

ID string

Type BetaManagedAgentsDeleteSessionResourceType



type BetaManagedAgentsFileResource struct{…}

ID string

CreatedAt Time

A timestamp in RFC 3339 format

FileID string

MountPath string

Type BetaManagedAgentsFileResourceType

UpdatedAt Time

A timestamp in RFC 3339 format



type BetaManagedAgentsGitHubRepositoryResource struct{…}

ID string

CreatedAt Time

A timestamp in RFC 3339 format

MountPath string

Type BetaManagedAgentsGitHubRepositoryResourceType

UpdatedAt Time

A timestamp in RFC 3339 format

URL string



Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnionOptional

One of the following:



type BetaManagedAgentsBranchCheckout struct{…}

Name string

Branch name to check out.

Type BetaManagedAgentsBranchCheckoutType



type BetaManagedAgentsCommitCheckout struct{…}

Sha string

Full commit SHA to check out.

Type BetaManagedAgentsCommitCheckoutType



type BetaManagedAgentsMemoryStoreResource struct{…}

A memory store attached to an agent session.

MemoryStoreID string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type BetaManagedAgentsMemoryStoreResourceType



Access BetaManagedAgentsMemoryStoreResourceAccessOptional

Access mode for an attached memory store.

One of the following:

const BetaManagedAgentsMemoryStoreResourceAccessReadWrite BetaManagedAgentsMemoryStoreResourceAccess = "read\_write"

const BetaManagedAgentsMemoryStoreResourceAccessReadOnly BetaManagedAgentsMemoryStoreResourceAccess = "read\_only"

Description stringOptional

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

Instructions stringOptional

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

MountPath stringOptional

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

Name stringOptional

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.



type BetaManagedAgentsSessionResourceUnion interface{…}

A memory store attached to an agent session.

One of the following:



type BetaManagedAgentsGitHubRepositoryResource struct{…}

ID string

CreatedAt Time

A timestamp in RFC 3339 format

MountPath string

Type BetaManagedAgentsGitHubRepositoryResourceType

UpdatedAt Time

A timestamp in RFC 3339 format

URL string



Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnionOptional

One of the following:



type BetaManagedAgentsBranchCheckout struct{…}

Name string

Branch name to check out.

Type BetaManagedAgentsBranchCheckoutType



type BetaManagedAgentsCommitCheckout struct{…}

Sha string

Full commit SHA to check out.

Type BetaManagedAgentsCommitCheckoutType



type BetaManagedAgentsFileResource struct{…}

ID string

CreatedAt Time

A timestamp in RFC 3339 format

FileID string

MountPath string

Type BetaManagedAgentsFileResourceType

UpdatedAt Time

A timestamp in RFC 3339 format



type BetaManagedAgentsMemoryStoreResource struct{…}

A memory store attached to an agent session.

MemoryStoreID string

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type BetaManagedAgentsMemoryStoreResourceType



Access BetaManagedAgentsMemoryStoreResourceAccessOptional

Access mode for an attached memory store.

One of the following:

const BetaManagedAgentsMemoryStoreResourceAccessReadWrite BetaManagedAgentsMemoryStoreResourceAccess = "read\_write"

const BetaManagedAgentsMemoryStoreResourceAccessReadOnly BetaManagedAgentsMemoryStoreResourceAccess = "read\_only"

Description stringOptional

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

Instructions stringOptional

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

MountPath stringOptional

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

Name stringOptional

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

---

*Copyright © Anthropic. All rights reserved.*
