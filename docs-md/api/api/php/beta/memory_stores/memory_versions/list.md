# List memory versions

Copy page

SDK language

PHP

# List memory versions

$client->beta->memoryStores->memoryVersions->list(string memoryStoreID, ?string apiKeyID, ?\Datetime createdAtGte, ?\Datetime createdAtLte, ?int limit, ?string memoryID, ?[ManagedAgentsMemoryVersionOperation](api/beta.md) operation, ?string page, ?string sessionID, ?[ManagedAgentsMemoryView](api/beta.md) view, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsMemoryVersion](api/beta.md)>

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

List memory versions

##### ParametersExpand Collapse

memoryStoreID: string

apiKeyID?:optional string

Query parameter for api\_key\_id

createdAtGte?:optional \Datetime

Return versions created at or after this time (inclusive).

createdAtLte?:optional \Datetime

Return versions created at or before this time (inclusive).

limit?:optional int

Query parameter for limit

memoryID?:optional string

Query parameter for memory\_id

operation?:optional [ManagedAgentsMemoryVersionOperation](api/beta.md)

Query parameter for operation

page?:optional string

Query parameter for page

sessionID?:optional string

Query parameter for session\_id

view?:optional [ManagedAgentsMemoryView](api/beta.md)

Query parameter for view

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



[ManagedAgentsMemoryVersion](api/beta.md)

string id

Unique identifier for this version (a `memver_...` value).

\Datetime createdAt

A timestamp in RFC 3339 format

string memoryID

ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](api/beta/memory_stores/memory_versions/list.md) to retrieve the full lineage including the `deleted` row.

string memoryStoreID

ID of the memory store this version belongs to (a `memstore_...` value).

[ManagedAgentsMemoryVersionOperation](api/beta.md) operation

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

Type type

?string content

The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

?string contentSha256

Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

?int contentSizeBytes

Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

?[ManagedAgentsActor](api/beta.md) createdBy

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

?string path

The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

?\Datetime redactedAt

A timestamp in RFC 3339 format

?[ManagedAgentsActor](api/beta.md) redactedBy

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

List memory versions

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->memoryStores->memoryVersions->list(
  'memory_store_id',
  apiKeyID: 'api_key_id',
  createdAtGte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  limit: 0,
  memoryID: 'memory_id',
  operation: ManagedAgentsMemoryVersionOperation::CREATED,
  page: 'page',
  sessionID: 'session_id',
  view: ManagedAgentsMemoryView::BASIC,
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

Response 200



```shiki
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "memory_id": "memory_id",
      "memory_store_id": "memory_store_id",
      "operation": "created",
      "type": "memory_version",
      "content": "content",
      "content_sha256": "content_sha256",
      "content_size_bytes": 0,
      "created_by": {
        "session_id": "x",
        "type": "session_actor"
      },
      "path": "path",
      "redacted_at": "2019-12-27T18:11:19.117Z",
      "redacted_by": {
        "session_id": "x",
        "type": "session_actor"
      }
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "memory_id": "memory_id",
      "memory_store_id": "memory_store_id",
      "operation": "created",
      "type": "memory_version",
      "content": "content",
      "content_sha256": "content_sha256",
      "content_size_bytes": 0,
      "created_by": {
        "session_id": "x",
        "type": "session_actor"
      },
      "path": "path",
      "redacted_at": "2019-12-27T18:11:19.117Z",
      "redacted_by": {
        "session_id": "x",
        "type": "session_actor"
      }
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
