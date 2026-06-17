# Delete a memory

Copy page



PHP

# Delete a memory

$client->beta->memoryStores->memories->delete(string memoryID, string memoryStoreID, ?string expectedContentSha256, ?list<AnthropicBeta> betas): [ManagedAgentsDeletedMemory](api/beta.md)

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

Delete a memory

##### ParametersExpand Collapse

memoryStoreID: string

memoryID: string

expectedContentSha256?:optional string

Query parameter for expected\_content\_sha256

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



[ManagedAgentsDeletedMemory](api/beta.md)

string id

ID of the deleted memory (a `mem_...` value).

Type type

Delete a memory

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeletedMemory = $client->beta->memoryStores->memories->delete(
  'memory_id',
  memoryStoreID: 'memory_store_id',
  expectedContentSha256: 'expected_content_sha256',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsDeletedMemory);
```

Response 200



```shiki
{
  "id": "id",
  "type": "memory_deleted"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "id",
  "type": "memory_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
