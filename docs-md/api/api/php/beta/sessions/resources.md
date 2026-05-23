# Resources

Copy page

PHP

# Resources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

$client->beta->sessions->resources->add(string sessionID, string fileID, [Type](api/beta/sessions/resources/add.md) type, ?string mountPath, ?list<AnthropicBeta> betas): [ManagedAgentsFileResource](api/beta.md)

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

$client->beta->sessions->resources->list(string sessionID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsSessionResource](api/beta.md)>

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

$client->beta->sessions->resources->retrieve(string resourceID, string sessionID, ?list<AnthropicBeta> betas): [ResourceGetResponse](api/beta.md)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

$client->beta->sessions->resources->update(string resourceID, string sessionID, string authorizationToken, ?list<AnthropicBeta> betas): [ResourceUpdateResponse](api/beta.md)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

$client->beta->sessions->resources->delete(string resourceID, string sessionID, ?list<AnthropicBeta> betas): [ManagedAgentsDeleteSessionResource](api/beta.md)

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

##### ModelsExpand Collapse

[ManagedAgentsDeleteSessionResource](api/beta.md)

string id

Type type

[ManagedAgentsFileResource](api/beta.md)

string id

\Datetime createdAt

A timestamp in RFC 3339 format

string fileID

string mountPath

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

[ManagedAgentsGitHubRepositoryResource](api/beta.md)

string id

\Datetime createdAt

A timestamp in RFC 3339 format

string mountPath

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

string url

?Checkout checkout

[ManagedAgentsMemoryStoreResource](api/beta.md)

string memoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type type

?Access access

Access mode for an attached memory store.

?string description

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

?string instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

?string mountPath

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

?string name

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

[ManagedAgentsSessionResource](api/beta.md)

One of the following:

[ManagedAgentsGitHubRepositoryResource](api/beta.md)

string id

\Datetime createdAt

A timestamp in RFC 3339 format

string mountPath

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

string url

?Checkout checkout

[ManagedAgentsFileResource](api/beta.md)

string id

\Datetime createdAt

A timestamp in RFC 3339 format

string fileID

string mountPath

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

[ManagedAgentsMemoryStoreResource](api/beta.md)

string memoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type type

?Access access

Access mode for an attached memory store.

?string description

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

?string instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

?string mountPath

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

?string name

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

---

*Copyright © Anthropic. All rights reserved.*
