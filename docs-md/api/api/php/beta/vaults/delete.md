# Delete Vault

Copy page



PHP

# Delete Vault

$client->beta->vaults->delete(string vaultID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeletedVault](api/beta.md)

DELETE/v1/vaults/{vault\_id}

Delete Vault

##### ParametersExpand Collapse

vaultID: string

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



[BetaManagedAgentsDeletedVault](api/beta.md)

string id

Unique identifier of the deleted vault.

Type type

Delete Vault

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeletedVault = $client->beta->vaults->delete(
  'vlt_011CZkZDLs7fYzm1hXNPeRjv', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsDeletedVault);
```

Response 200



```shiki
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "type": "vault_deleted"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "type": "vault_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
