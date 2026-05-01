# Environments

Copy page

Python

# Environments

##### [Create Environment](api/beta/environments/create.md)

beta.environments.create(EnvironmentCreateParams\*\*kwargs)  -> [BetaEnvironment](api/beta.md)

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

beta.environments.list(EnvironmentListParams\*\*kwargs)  -> SyncPageCursor[[BetaEnvironment](api/beta.md)]

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

beta.environments.retrieve(strenvironment\_id, EnvironmentRetrieveParams\*\*kwargs)  -> [BetaEnvironment](api/beta.md)

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

beta.environments.update(strenvironment\_id, EnvironmentUpdateParams\*\*kwargs)  -> [BetaEnvironment](api/beta.md)

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

beta.environments.delete(strenvironment\_id, EnvironmentDeleteParams\*\*kwargs)  -> [BetaEnvironmentDeleteResponse](api/beta.md)

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

beta.environments.archive(strenvironment\_id, EnvironmentArchiveParams\*\*kwargs)  -> [BetaEnvironment](api/beta.md)

POST/v1/environments/{environment\_id}/archive

##### ModelsExpand Collapse

class BetaCloudConfig: …

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

class BetaCloudConfigParams: …

Request params for `cloud` environment configuration.

Fields default to null; on update, omitted fields preserve the
existing value.

type: Literal["cloud"]

Environment type

networking: Optional[Networking]

Network configuration policy. Omit on update to preserve the existing value.

Accepts one of the following:

class BetaUnrestrictedNetwork: …

Unrestricted network access.

type: Literal["unrestricted"]

Network policy type

class BetaLimitedNetworkParams: …

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

type: Literal["limited"]

Network policy type

allow\_mcp\_servers: Optional[bool]

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allow\_package\_managers: Optional[bool]

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allowed\_hosts: Optional[List[str]]

Specifies domains the container can reach.

packages: Optional[BetaPackagesParams]

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

apt: Optional[List[str]]

Ubuntu/Debian packages to install

cargo: Optional[List[str]]

Rust packages to install

gem: Optional[List[str]]

Ruby packages to install

go: Optional[List[str]]

Go packages to install

npm: Optional[List[str]]

Node.js packages to install

pip: Optional[List[str]]

Python packages to install

type: Optional[Literal["packages"]]

Package configuration type

class BetaEnvironment: …

Unified Environment resource for both cloud and self-hosted environments.

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

class BetaEnvironmentDeleteResponse: …

Response after deleting an environment.

id: str

Environment identifier

type: Literal["environment\_deleted"]

The type of response

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

class BetaLimitedNetworkParams: …

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

type: Literal["limited"]

Network policy type

allow\_mcp\_servers: Optional[bool]

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allow\_package\_managers: Optional[bool]

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allowed\_hosts: Optional[List[str]]

Specifies domains the container can reach.

class BetaPackages: …

Packages (and their versions) available in this environment.

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

class BetaPackagesParams: …

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

apt: Optional[List[str]]

Ubuntu/Debian packages to install

cargo: Optional[List[str]]

Rust packages to install

gem: Optional[List[str]]

Ruby packages to install

go: Optional[List[str]]

Go packages to install

npm: Optional[List[str]]

Node.js packages to install

pip: Optional[List[str]]

Python packages to install

type: Optional[Literal["packages"]]

Package configuration type

class BetaUnrestrictedNetwork: …

Unrestricted network access.

type: Literal["unrestricted"]

Network policy type

---

*Copyright © Anthropic. All rights reserved.*
