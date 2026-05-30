# Validate Credential

Copy page

SDK language

PHP

# Validate Credential

$client->beta->vaults->credentials->mcpOAuthValidate(string credentialID, string vaultID, ?list<AnthropicBeta> betas): [ManagedAgentsCredentialValidation](api/beta.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

Validate Credential

##### ParametersExpand Collapse

vaultID: string

credentialID: string

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

[ManagedAgentsCredentialValidation](api/beta.md)

string credentialID

Unique identifier of the credential that was validated.

bool hasRefreshToken

Whether the credential has a refresh token configured.

?[ManagedAgentsMCPProbe](api/beta.md) mcpProbe

The failing step of an MCP validation probe.

?[ManagedAgentsRefreshObject](api/beta.md) refresh

Outcome of a refresh-token exchange attempted during credential validation.

[ManagedAgentsCredentialValidationStatus](api/beta.md) status

Overall verdict of a credential validation probe.

Type type

\Datetime validatedAt

A timestamp in RFC 3339 format

string vaultID

Identifier of the vault containing the credential.

Validate Credential

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsCredentialValidation = $client
  ->beta
  ->vaults
  ->credentials
  ->mcpOAuthValidate(
  'vcrd_011CZkZEMt8gZan2iYOQfSkw',
  vaultID: 'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsCredentialValidation);
```

Response 200

```shiki
{
  "credential_id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "has_refresh_token": true,
  "mcp_probe": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "method": "method"
  },
  "refresh": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "status": "succeeded"
  },
  "status": "valid",
  "type": "vault_credential_validation",
  "validated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv"
}
```

##### Returns Examples

Response 200

```shiki
{
  "credential_id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "has_refresh_token": true,
  "mcp_probe": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "method": "method"
  },
  "refresh": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "status": "succeeded"
  },
  "status": "valid",
  "type": "vault_credential_validation",
  "validated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv"
}
```

---

*Copyright © Anthropic. All rights reserved.*
