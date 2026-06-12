# Get Session Resource

Copy page

SDK language

PHP

# Get Session Resource

$client->beta->sessions->resources->retrieve(string resourceID, string sessionID, ?list<AnthropicBeta> betas): [ResourceGetResponse](api/beta.md)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

Get Session Resource

##### ParametersExpand Collapse

sessionID: string

resourceID: string

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



[ResourceGetResponse](api/beta.md)

One of the following:



[ManagedAgentsGitHubRepositoryResource](api/beta.md)

string id

\Datetime createdAt

A timestamp in RFC 3339 format

string mountPath

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

string url

?Checkout checkout



[ManagedAgentsFileResource](api/beta.md)

string id

\Datetime createdAt

A timestamp in RFC 3339 format

string fileID

string mountPath

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format



[ManagedAgentsMemoryStoreResource](api/beta.md)

string memoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

Type type

?Access access

Access mode for an attached memory store.

?string description

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

?string instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

?string mountPath

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

?string name

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

Get Session Resource

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$resource = $client->beta->sessions->resources->retrieve(
  'sesrsc_011CZkZBJq5dWxk9fVLNcPht',
  sessionID: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  betas: ['message-batches-2024-09-24'],
);

var_dump($resource);
```

Response 200



```shiki
{
  "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
  "created_at": "2026-03-15T10:00:00Z",
  "mount_path": "/workspace/example-repo",
  "type": "github_repository",
  "updated_at": "2026-03-15T10:00:00Z",
  "url": "https://github.com/example-org/example-repo",
  "checkout": {
    "name": "main",
    "type": "branch"
  }
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
  "created_at": "2026-03-15T10:00:00Z",
  "mount_path": "/workspace/example-repo",
  "type": "github_repository",
  "updated_at": "2026-03-15T10:00:00Z",
  "url": "https://github.com/example-org/example-repo",
  "checkout": {
    "name": "main",
    "type": "branch"
  }
}
```

---

*Copyright © Anthropic. All rights reserved.*
