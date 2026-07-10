# Create Environment

Copy page



Ruby

# Create Environment

beta.environments.create(\*\*kwargs) -> [BetaEnvironment](api/beta/environments.md) { id, archived\_at, config, 7 more }

POST/v1/environments

Create a new environment with the specified configuration.

##### ParametersExpand Collapse

name: String

Human-readable name for the environment



config: [BetaCloudConfigParams](api/beta/environments.md) { type, networking, packages }  | [BetaSelfHostedConfigParams](api/beta/environments.md) { type } 

Environment configuration

One of the following:



class BetaCloudConfigParams { type, networking, packages } 

Request params for `cloud` environment configuration.

Fields default to null; on update, omitted fields preserve the
existing value.

type: :cloud

Environment type



networking: [BetaUnrestrictedNetwork](api/beta/environments.md) { type }  | [BetaLimitedNetworkParams](api/beta/environments.md) { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts } 

Network configuration policy. Omit on update to preserve the existing value.

One of the following:



class BetaUnrestrictedNetwork { type } 

Unrestricted network access.

type: :unrestricted

Network policy type



class BetaLimitedNetworkParams { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts } 

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

type: :limited

Network policy type

allow\_mcp\_servers: bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allow\_package\_managers: bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allowed\_hosts: Array[String]

Specifies domains the container can reach.



packages: [BetaPackagesParams](api/beta/environments.md) { apt, cargo, gem\_, 4 more } 

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

apt: Array[String]

Ubuntu/Debian packages to install

cargo: Array[String]

Rust packages to install

gem\_: Array[String]

Ruby packages to install

go: Array[String]

Go packages to install

npm: Array[String]

Node.js packages to install

pip: Array[String]

Python packages to install

type: :packages

Package configuration type



class BetaSelfHostedConfigParams { type } 

Request params for `self_hosted` environment configuration.

type: :self\_hosted

Environment type

description: String

Optional description of the environment

metadata: Hash[Symbol, String]

User-provided metadata key-value pairs



scope: :organization | :account

The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only. Only applicable for self-hosted environments. If not specified, defaults based on organization type.

One of the following:

:organization

:account



betas: Array[[AnthropicBeta](api/beta.md)]

Optional header to specify the beta version(s) you want to use.

One of the following:

String = String



AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 26 more

One of the following:

:"message-batches-2024-09-24"

:"prompt-caching-2024-07-31"

:"computer-use-2024-10-22"

:"computer-use-2025-01-24"

:"pdfs-2024-09-25"

:"token-counting-2024-11-01"

:"token-efficient-tools-2025-02-19"

:"output-128k-2025-02-19"

:"files-api-2025-04-14"

:"mcp-client-2025-04-04"

:"mcp-client-2025-11-20"

:"dev-full-thinking-2025-05-14"

:"interleaved-thinking-2025-05-14"

:"code-execution-2025-05-22"

:"extended-cache-ttl-2025-04-11"

:"context-1m-2025-08-07"

:"context-management-2025-06-27"

:"model-context-window-exceeded-2025-08-26"

:"skills-2025-10-02"

:"fast-mode-2026-02-01"

:"output-300k-2026-03-24"

:"user-profiles-2026-03-24"

:"advisor-tool-2026-03-01"

:"managed-agents-2026-04-01"

:"cache-diagnosis-2026-04-07"

:"thinking-token-count-2026-05-13"

:"server-side-fallback-2026-06-01"

:"fallback-credit-2026-06-01"

:"agent-memory-2026-07-22"

##### ReturnsExpand Collapse



class BetaEnvironment { id, archived\_at, config, 7 more } 

Unified Environment resource for both cloud and self-hosted environments.

id: String

Environment identifier (e.g., 'env\_...')

archived\_at: String

RFC 3339 timestamp when environment was archived, or null if not archived



config: [BetaCloudConfig](api/beta/environments.md) { networking, packages, type }  | [BetaSelfHostedConfig](api/beta/environments.md) { type } 

Environment configuration (either Anthropic Cloud or self-hosted)

One of the following:



class BetaCloudConfig { networking, packages, type } 

`cloud` environment configuration.



networking: [BetaUnrestrictedNetwork](api/beta/environments.md) { type }  | [BetaLimitedNetwork](api/beta/environments.md) { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type } 

Network configuration policy.

One of the following:



class BetaUnrestrictedNetwork { type } 

Unrestricted network access.

type: :unrestricted

Network policy type



class BetaLimitedNetwork { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type } 

Limited network access.

allow\_mcp\_servers: bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: Array[String]

Specifies domains the container can reach.

type: :limited

Network policy type



packages: [BetaPackages](api/beta/environments.md) { apt, cargo, gem\_, 4 more } 

Package manager configuration.

apt: Array[String]

Ubuntu/Debian packages to install

cargo: Array[String]

Rust packages to install

gem\_: Array[String]

Ruby packages to install

go: Array[String]

Go packages to install

npm: Array[String]

Node.js packages to install

pip: Array[String]

Python packages to install

type: :packages

Package configuration type

type: :cloud

Environment type



class BetaSelfHostedConfig { type } 

Configuration for self-hosted environments.

type: :self\_hosted

Environment type

created\_at: String

RFC 3339 timestamp when environment was created

description: String

User-provided description for the environment

metadata: Hash[Symbol, String]

User-provided metadata key-value pairs

name: String

Human-readable name for the environment

type: :environment

The type of object (always 'environment')

updated\_at: String

RFC 3339 timestamp when environment was last updated



scope: :organization | :account

The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

One of the following:

:organization

:account

Create Environment

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_environment = anthropic.beta.environments.create(name: "python-data-analysis")

puts(beta_environment)
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
