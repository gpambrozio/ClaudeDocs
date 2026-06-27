# Update Environment

Copy page



PHP

# Update Environment

$client->beta->environments->update(string environmentID, ?[Config](api/beta/environments/update.md) config, ?string description, ?array<string,string> metadata, ?string name, ?[Scope](api/beta/environments/update.md) scope, ?list<AnthropicBeta> betas): [BetaEnvironment](api/beta/environments.md)

POST/v1/environments/{environment\_id}

Update an existing environment's configuration.

##### ParametersExpand Collapse

environmentID: string

config?:optional [Config](api/beta/environments/update.md)

Updated environment configuration

description?:optional string

Updated description of the environment

metadata?:optional array<string,string>

User-provided metadata key-value pairs. Set a value to null or empty string to delete the key.

name?:optional string

Updated name for the environment

scope?:optional [Scope](api/beta/environments/update.md)

The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only.

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



[BetaEnvironment](api/beta/environments.md)

string id

Environment identifier (e.g., 'env\_...')

?string archivedAt

RFC 3339 timestamp when environment was archived, or null if not archived

Config config

Environment configuration (either Anthropic Cloud or self-hosted)

string createdAt

RFC 3339 timestamp when environment was created

string description

User-provided description for the environment

array<string,string> metadata

User-provided metadata key-value pairs

string name

Human-readable name for the environment

"environment" type

The type of object (always 'environment')

string updatedAt

RFC 3339 timestamp when environment was last updated

?Scope scope

The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

Update Environment

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaEnvironment = $client->beta->environments->update(
  'env_011CZkZ9X2dpNyB7HsEFoRfW',
  config: [
    'type' => 'cloud',
    'networking' => [
      'type' => 'limited',
      'allowMCPServers' => true,
      'allowPackageManagers' => true,
      'allowedHosts' => ['api.example.com'],
    ],
    'packages' => [
      'apt' => ['string'],
      'cargo' => ['string'],
      'gem' => ['string'],
      'go' => ['string'],
      'npm' => ['string'],
      'pip' => ['pandas', 'numpy'],
      'type' => 'packages',
    ],
  ],
  description: 'Python environment with data-analysis packages.',
  metadata: ['foo' => 'string'],
  name: 'x',
  scope: 'organization',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaEnvironment);
```

Response 200



```shiki
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

---

*Copyright © Anthropic. All rights reserved.*
