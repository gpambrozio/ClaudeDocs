# Archive Environment

Copy page



PHP

# Archive Environment

$client->beta->environments->archive(string environmentID, ?list<AnthropicBeta> betas): [BetaEnvironment](api/beta.md)

POST/v1/environments/{environment\_id}/archive

Archive an environment by ID. Archived environments cannot be used to create new sessions.

##### ParametersExpand Collapse

environmentID: string

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



[BetaEnvironment](api/beta.md)

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

Archive Environment

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaEnvironment = $client->beta->environments->archive(
  'env_011CZkZ9X2dpNyB7HsEFoRfW', betas: ['message-batches-2024-09-24']
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
