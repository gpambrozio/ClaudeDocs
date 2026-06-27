# Delete a memory store

Copy page



PHP

# Delete a memory store

$client->beta->memoryStores->delete(string memoryStoreID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeletedMemoryStore](api/beta/memory_stores.md)

DELETE/v1/memory\_stores/{memory\_store\_id}

Delete a memory store

##### ParametersExpand Collapse

memoryStoreID: string

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



[BetaManagedAgentsDeletedMemoryStore](api/beta/memory_stores.md)

string id

ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

Type type

Delete a memory store

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeletedMemoryStore = $client->beta->memoryStores->delete(
  'memory_store_id', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsDeletedMemoryStore);
```

Response 200



```shiki
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
