# List Environments

Copy page



Python

# List Environments

beta.environments.list(EnvironmentListParams\*\*kwargs)  -> SyncPageCursor[[BetaEnvironment](api/beta.md)]

GET/v1/environments

List environments with pagination support.

##### ParametersExpand Collapse

include\_archived: Optional[[bool](api/beta/environments/list.md)]

Include archived environments in the response

limit: Optional[int]

Maximum number of environments to return

page: Optional[str]

Opaque cursor from previous response for pagination. Pass the `next_page` value from the previous response.



betas: Optional[List[[AnthropicBetaParam](api/beta.md)]]

Optional header to specify the beta version(s) you want to use.

One of the following:

str



Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]

One of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"fallback-credit-2026-06-01"

##### ReturnsExpand Collapse



class BetaEnvironment: …

Unified Environment resource for both cloud and self-hosted environments.

id: str

Environment identifier (e.g., 'env\_...')

archived\_at: Optional[str]

RFC 3339 timestamp when environment was archived, or null if not archived



config: Config

Environment configuration (either Anthropic Cloud or self-hosted)

One of the following:



class BetaCloudConfig: …

`cloud` environment configuration.



networking: Networking

Network configuration policy.

One of the following:



class BetaUnrestrictedNetwork: …

Unrestricted network access.

type: Literal["unrestricted"]

Network policy type



class BetaLimitedNetwork: …

Limited network access.

allow\_mcp\_servers: bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: List[str]

Specifies domains the container can reach.

type: Literal["limited"]

Network policy type



packages: [BetaPackages](api/beta.md)

Package manager configuration.

apt: List[str]

Ubuntu/Debian packages to install

cargo: List[str]

Rust packages to install

gem: List[str]

Ruby packages to install

go: List[str]

Go packages to install

npm: List[str]

Node.js packages to install

pip: List[str]

Python packages to install

type: Optional[Literal["packages"]]

Package configuration type

type: Literal["cloud"]

Environment type



class BetaSelfHostedConfig: …

Configuration for self-hosted environments.

type: Literal["self\_hosted"]

Environment type

created\_at: str

RFC 3339 timestamp when environment was created

description: str

User-provided description for the environment

metadata: Dict[str, str]

User-provided metadata key-value pairs

name: str

Human-readable name for the environment

type: Literal["environment"]

The type of object (always 'environment')

updated\_at: str

RFC 3339 timestamp when environment was last updated



scope: Optional[Literal["organization", "account"]]

The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

One of the following:

"organization"

"account"

List Environments

Python

```shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.environments.list()
page = page.data[0]
print(page.id)
```

Response 200



```shiki
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

---

*Copyright © Anthropic. All rights reserved.*
