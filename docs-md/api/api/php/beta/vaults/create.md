# Create Vault

Copy page

SDK language

PHP

# Create Vault

$client->beta->vaults->create(string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): [BetaManagedAgentsVault](api/beta.md)

POST/v1/vaults

Create Vault

##### ParametersExpand Collapse

displayName: string

Human-readable name for the vault. 1-255 characters.

metadata?:optional array<string,string>

Arbitrary key-value metadata to attach to the vault. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



[BetaManagedAgentsVault](api/beta.md)

string id

Unique identifier for the vault.

?\Datetime archivedAt

A timestamp in RFC 3339 format

\Datetime createdAt

A timestamp in RFC 3339 format

string displayName

Human-readable name for the vault.

array<string,string> metadata

Arbitrary key-value metadata attached to the vault.

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

Create Vault

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsVault = $client->beta->vaults->create(
  displayName: 'Example vault',
  metadata: ['environment' => 'production'],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsVault);
```

Response 200



```shiki
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

---

*Copyright © Anthropic. All rights reserved.*
