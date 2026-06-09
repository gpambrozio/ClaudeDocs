# Delete Credential

Copy page

SDK language

PHP

# Delete Credential

$client->beta->vaults->credentials->delete(string credentialID, string vaultID, ?list<AnthropicBeta> betas): [ManagedAgentsDeletedCredential](api/beta.md)

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

Delete Credential

##### ParametersExpand Collapse

vaultID: string

credentialID: string

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

[ManagedAgentsDeletedCredential](api/beta.md)

string id

Unique identifier of the deleted credential.

Type type

Delete Credential

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeletedCredential = $client
  ->beta
  ->vaults
  ->credentials
  ->delete(
  'vcrd_011CZkZEMt8gZan2iYOQfSkw',
  vaultID: 'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsDeletedCredential);
```

Response 200



```shiki
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "type": "vault_credential_deleted"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "type": "vault_credential_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
