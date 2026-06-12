# Retrieve a memory store

Copy page

SDK language

PHP

# Retrieve a memory store

$client->beta->memoryStores->retrieve(string memoryStoreID, ?list<AnthropicBeta> betas): [BetaManagedAgentsMemoryStore](api/beta.md)

GET/v1/memory\_stores/{memory\_store\_id}

Retrieve a memory store

##### ParametersExpand Collapse

memoryStoreID: string

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



[BetaManagedAgentsMemoryStore](api/beta.md)

string id

Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

\Datetime createdAt

A timestamp in RFC 3339 format

string name

Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

?\Datetime archivedAt

A timestamp in RFC 3339 format

?string description

Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

?array<string,string> metadata

Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

Retrieve a memory store

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsMemoryStore = $client->beta->memoryStores->retrieve(
  'memory_store_id', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsMemoryStore);
```

Response 200



```shiki
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  }
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  }
}
```

---

*Copyright © Anthropic. All rights reserved.*
