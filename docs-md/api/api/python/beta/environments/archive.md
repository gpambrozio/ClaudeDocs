# Archive Environment

Copy page

Python

# Archive Environment

beta.environments.archive(strenvironment\_id, EnvironmentArchiveParams\*\*kwargs)  -> [BetaEnvironment](api/beta.md)

POST/v1/environments/{environment\_id}/archive

Archive an environment by ID. Archived environments cannot be used to create new sessions.

##### ParametersExpand Collapse

environment\_id: str

betas: Optional[List[[AnthropicBetaParam](api/beta.md)]]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

str

Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 18 more]

Accepts one of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

##### ReturnsExpand Collapse

class BetaEnvironment: …

Unified Environment resource for both cloud and BYOC environments.

id: str

Environment identifier (e.g., 'env\_...')

archived\_at: Optional[str]

RFC 3339 timestamp when environment was archived, or null if not archived

config: [BetaCloudConfig](api/beta.md)

`cloud` environment configuration.

networking: Networking

Network configuration policy.

Accepts one of the following:

class BetaUnrestrictedNetwork: …

Unrestricted network access.

type: Literal["unrestricted"]

Network policy type

class BetaLimitedNetwork: …

Limited network access.

allow\_mcp\_servers: bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: List[str]

Specifies domains the container can reach.

type: Literal["limited"]

Network policy type

packages: [BetaPackages](api/beta.md)

Package manager configuration.

apt: List[str]

Ubuntu/Debian packages to install

cargo: List[str]

Rust packages to install

gem: List[str]

Ruby packages to install

go: List[str]

Go packages to install

npm: List[str]

Node.js packages to install

pip: List[str]

Python packages to install

type: Optional[Literal["packages"]]

Package configuration type

type: Literal["cloud"]

Environment type

created\_at: str

RFC 3339 timestamp when environment was created

description: str

User-provided description for the environment

metadata: Dict[str, str]

User-provided metadata key-value pairs

name: str

Human-readable name for the environment

type: Literal["environment"]

The type of object (always 'environment')

updated\_at: str

RFC 3339 timestamp when environment was last updated

Archive Environment

Python

```shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_environment = client.beta.environments.archive(
    environment_id="env_011CZkZ9X2dpNyB7HsEFoRfW",
)
print(beta_environment.id)
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
