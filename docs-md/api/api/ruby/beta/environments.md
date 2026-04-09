# Environments

Copy page

Ruby

# Environments

##### [Create Environment](api/beta/environments/create.md)

beta.environments.create(\*\*kwargs) -> [BetaEnvironment](api/beta.md) { id, archived\_at, config, 6 more }

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

beta.environments.list(\*\*kwargs) -> PageCursor<[BetaEnvironment](api/beta.md) { id, archived\_at, config, 6 more } >

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

beta.environments.retrieve(environment\_id, \*\*kwargs) -> [BetaEnvironment](api/beta.md) { id, archived\_at, config, 6 more }

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

beta.environments.update(environment\_id, \*\*kwargs) -> [BetaEnvironment](api/beta.md) { id, archived\_at, config, 6 more }

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

beta.environments.delete(environment\_id, \*\*kwargs) -> [BetaEnvironmentDeleteResponse](api/beta.md) { id, type }

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

beta.environments.archive(environment\_id, \*\*kwargs) -> [BetaEnvironment](api/beta.md) { id, archived\_at, config, 6 more }

POST/v1/environments/{environment\_id}/archive

##### ModelsExpand Collapse

class BetaCloudConfig { networking, packages, type }

`cloud` environment configuration.

networking: [BetaUnrestrictedNetwork](api/beta.md) { type }  | [BetaLimitedNetwork](api/beta.md) { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Network configuration policy.

Accepts one of the following:

class BetaUnrestrictedNetwork { type }

Unrestricted network access.

type: :unrestricted

Network policy type

class BetaLimitedNetwork { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Limited network access.

allow\_mcp\_servers: bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: Array[String]

Specifies domains the container can reach.

type: :limited

Network policy type

packages: [BetaPackages](api/beta.md) { apt, cargo, gem\_, 4 more }

Package manager configuration.

apt: Array[String]

Ubuntu/Debian packages to install

cargo: Array[String]

Rust packages to install

gem\_: Array[String]

Ruby packages to install

go: Array[String]

Go packages to install

npm: Array[String]

Node.js packages to install

pip: Array[String]

Python packages to install

type: :packages

Package configuration type

type: :cloud

Environment type

class BetaCloudConfigParams { type, networking, packages }

Request params for `cloud` environment configuration.

Fields default to null; on update, omitted fields preserve the
existing value.

type: :cloud

Environment type

networking: [BetaUnrestrictedNetwork](api/beta.md) { type }  | [BetaLimitedNetworkParams](api/beta.md) { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts }

Network configuration policy. Omit on update to preserve the existing value.

Accepts one of the following:

class BetaUnrestrictedNetwork { type }

Unrestricted network access.

type: :unrestricted

Network policy type

class BetaLimitedNetworkParams { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts }

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

type: :limited

Network policy type

allow\_mcp\_servers: bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allow\_package\_managers: bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allowed\_hosts: Array[String]

Specifies domains the container can reach.

packages: [BetaPackagesParams](api/beta.md) { apt, cargo, gem\_, 4 more }

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

apt: Array[String]

Ubuntu/Debian packages to install

cargo: Array[String]

Rust packages to install

gem\_: Array[String]

Ruby packages to install

go: Array[String]

Go packages to install

npm: Array[String]

Node.js packages to install

pip: Array[String]

Python packages to install

type: :packages

Package configuration type

class BetaEnvironment { id, archived\_at, config, 6 more }

Unified Environment resource for both cloud and BYOC environments.

id: String

Environment identifier (e.g., 'env\_...')

archived\_at: String

RFC 3339 timestamp when environment was archived, or null if not archived

config: [BetaCloudConfig](api/beta.md) { networking, packages, type }

`cloud` environment configuration.

networking: [BetaUnrestrictedNetwork](api/beta.md) { type }  | [BetaLimitedNetwork](api/beta.md) { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Network configuration policy.

Accepts one of the following:

class BetaUnrestrictedNetwork { type }

Unrestricted network access.

type: :unrestricted

Network policy type

class BetaLimitedNetwork { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Limited network access.

allow\_mcp\_servers: bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: Array[String]

Specifies domains the container can reach.

type: :limited

Network policy type

packages: [BetaPackages](api/beta.md) { apt, cargo, gem\_, 4 more }

Package manager configuration.

apt: Array[String]

Ubuntu/Debian packages to install

cargo: Array[String]

Rust packages to install

gem\_: Array[String]

Ruby packages to install

go: Array[String]

Go packages to install

npm: Array[String]

Node.js packages to install

pip: Array[String]

Python packages to install

type: :packages

Package configuration type

type: :cloud

Environment type

created\_at: String

RFC 3339 timestamp when environment was created

description: String

User-provided description for the environment

metadata: Hash[Symbol, String]

User-provided metadata key-value pairs

name: String

Human-readable name for the environment

type: :environment

The type of object (always 'environment')

updated\_at: String

RFC 3339 timestamp when environment was last updated

class BetaEnvironmentDeleteResponse { id, type }

Response after deleting an environment.

id: String

Environment identifier

type: :environment\_deleted

The type of response

class BetaLimitedNetwork { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Limited network access.

allow\_mcp\_servers: bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: Array[String]

Specifies domains the container can reach.

type: :limited

Network policy type

class BetaLimitedNetworkParams { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts }

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

type: :limited

Network policy type

allow\_mcp\_servers: bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allow\_package\_managers: bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allowed\_hosts: Array[String]

Specifies domains the container can reach.

class BetaPackages { apt, cargo, gem\_, 4 more }

Packages (and their versions) available in this environment.

apt: Array[String]

Ubuntu/Debian packages to install

cargo: Array[String]

Rust packages to install

gem\_: Array[String]

Ruby packages to install

go: Array[String]

Go packages to install

npm: Array[String]

Node.js packages to install

pip: Array[String]

Python packages to install

type: :packages

Package configuration type

class BetaPackagesParams { apt, cargo, gem\_, 4 more }

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

apt: Array[String]

Ubuntu/Debian packages to install

cargo: Array[String]

Rust packages to install

gem\_: Array[String]

Ruby packages to install

go: Array[String]

Go packages to install

npm: Array[String]

Node.js packages to install

pip: Array[String]

Python packages to install

type: :packages

Package configuration type

class BetaUnrestrictedNetwork { type }

Unrestricted network access.

type: :unrestricted

Network policy type

---

*Copyright © Anthropic. All rights reserved.*
