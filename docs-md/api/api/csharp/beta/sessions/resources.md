# Resources

Copy page



C#

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



class BetaManagedAgentsDeleteSessionResource:

Confirmation of resource deletion.

required string ID

required Type Type



class BetaManagedAgentsFileResource:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string FileID

required string MountPath

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsGitHubRepositoryResource:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string MountPath

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required string Url



Checkout? Checkout

One of the following:



class BetaManagedAgentsBranchCheckout:

required string Name

Branch name to check out.

required Type Type



class BetaManagedAgentsCommitCheckout:

required string Sha

Full commit SHA to check out.

required Type Type



class BetaManagedAgentsMemoryStoreResource:

A memory store attached to an agent session.

required string MemoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

required Type Type



Access? Access

Access mode for an attached memory store.

One of the following:

"read\_write"ReadWrite

"read\_only"ReadOnly

string Description

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

string? Instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

string? MountPath

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

string? Name

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.



class BetaManagedAgentsSessionResource: A class that can be one of several variants.union 

A memory store attached to an agent session.



class BetaManagedAgentsGitHubRepositoryResource:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string MountPath

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required string Url



Checkout? Checkout

One of the following:



class BetaManagedAgentsBranchCheckout:

required string Name

Branch name to check out.

required Type Type



class BetaManagedAgentsCommitCheckout:

required string Sha

Full commit SHA to check out.

required Type Type



class BetaManagedAgentsFileResource:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string FileID

required string MountPath

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsMemoryStoreResource:

A memory store attached to an agent session.

required string MemoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

required Type Type



Access? Access

Access mode for an attached memory store.

One of the following:

"read\_write"ReadWrite

"read\_only"ReadOnly

string Description

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

string? Instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

string? MountPath

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

string? Name

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

---

*Copyright © Anthropic. All rights reserved.*
