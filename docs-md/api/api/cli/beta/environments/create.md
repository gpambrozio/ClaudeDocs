# Create Environment

Copy page

CLI

# Create Environment

$ ant beta:environments create

POST/v1/environments

Create a new environment with the specified configuration.

##### ParametersExpand Collapse

--name: string

Body param: Human-readable name for the environment

--config: optional object { type, networking, packages }

Body param: Request params for `cloud` environment configuration.

Fields default to null; on update, omitted fields preserve the
existing value.

--description: optional string

Body param: Optional description of the environment

--metadata: optional map[string]

Body param: User-provided metadata key-value pairs

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

beta\_environment: object { id, archived\_at, config, 6 more }

Unified Environment resource for both cloud and BYOC environments.

id: string

Environment identifier (e.g., 'env\_...')

archived\_at: string

RFC 3339 timestamp when environment was archived, or null if not archived

config: object { networking, packages, type }

`cloud` environment configuration.

networking: [BetaUnrestrictedNetwork](api/beta.md) { type }  or [BetaLimitedNetwork](api/beta.md) { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Network configuration policy.

beta\_unrestricted\_network: object { type }

Unrestricted network access.

type: "unrestricted"

Network policy type

beta\_limited\_network: object { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Limited network access.

allow\_mcp\_servers: boolean

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: boolean

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: array of string

Specifies domains the container can reach.

type: "limited"

Network policy type

packages: object { apt, cargo, gem, 4 more }

Package manager configuration.

apt: array of string

Ubuntu/Debian packages to install

cargo: array of string

Rust packages to install

gem: array of string

Ruby packages to install

go: array of string

Go packages to install

npm: array of string

Node.js packages to install

pip: array of string

Python packages to install

type: optional "packages"

Package configuration type

"packages"

type: "cloud"

Environment type

created\_at: string

RFC 3339 timestamp when environment was created

description: string

User-provided description for the environment

metadata: map[string]

User-provided metadata key-value pairs

name: string

Human-readable name for the environment

type: "environment"

The type of object (always 'environment')

updated\_at: string

RFC 3339 timestamp when environment was last updated

Create Environment

CLI

```shiki
ant beta:environments create \
  --api-key my-anthropic-api-key \
  --name python-data-analysis
```

Response 200

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
  "updated_at": "2026-03-15T10:00:00Z"
}
```

##### Returns Examples

Response 200

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
  "updated_at": "2026-03-15T10:00:00Z"
}
```

---

*Copyright © Anthropic. All rights reserved.*
