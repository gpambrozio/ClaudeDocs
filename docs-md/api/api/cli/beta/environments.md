# Environments

Copy page

CLI

# Environments

##### [Create Environment](api/beta/environments/create.md)

$ ant beta:environments create

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

$ ant beta:environments list

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

$ ant beta:environments retrieve

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

$ ant beta:environments update

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

$ ant beta:environments delete

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

$ ant beta:environments archive

POST/v1/environments/{environment\_id}/archive

##### ModelsExpand Collapse

beta\_cloud\_config: object { networking, packages, type }

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

beta\_cloud\_config\_params: object { type, networking, packages }

Request params for `cloud` environment configuration.

Fields default to null; on update, omitted fields preserve the
existing value.

type: "cloud"

Environment type

networking: optional [BetaUnrestrictedNetwork](api/beta.md) { type }  or [BetaLimitedNetworkParams](api/beta.md) { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts }

Network configuration policy. Omit on update to preserve the existing value.

beta\_unrestricted\_network: object { type }

Unrestricted network access.

type: "unrestricted"

Network policy type

beta\_limited\_network\_params: object { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts }

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

type: "limited"

Network policy type

allow\_mcp\_servers: optional boolean

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allow\_package\_managers: optional boolean

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allowed\_hosts: optional array of string

Specifies domains the container can reach.

packages: optional object { apt, cargo, gem, 4 more }

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

apt: optional array of string

Ubuntu/Debian packages to install

cargo: optional array of string

Rust packages to install

gem: optional array of string

Ruby packages to install

go: optional array of string

Go packages to install

npm: optional array of string

Node.js packages to install

pip: optional array of string

Python packages to install

type: optional "packages"

Package configuration type

"packages"

beta\_environment: object { id, archived\_at, config, 6 more }

Unified Environment resource for both cloud and self-hosted environments.

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

beta\_environment\_delete\_response: object { id, type }

Response after deleting an environment.

id: string

Environment identifier

type: "environment\_deleted"

The type of response

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

beta\_limited\_network\_params: object { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts }

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

type: "limited"

Network policy type

allow\_mcp\_servers: optional boolean

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allow\_package\_managers: optional boolean

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allowed\_hosts: optional array of string

Specifies domains the container can reach.

beta\_packages: object { apt, cargo, gem, 4 more }

Packages (and their versions) available in this environment.

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

beta\_packages\_params: object { apt, cargo, gem, 4 more }

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

apt: optional array of string

Ubuntu/Debian packages to install

cargo: optional array of string

Rust packages to install

gem: optional array of string

Ruby packages to install

go: optional array of string

Go packages to install

npm: optional array of string

Node.js packages to install

pip: optional array of string

Python packages to install

type: optional "packages"

Package configuration type

"packages"

beta\_unrestricted\_network: object { type }

Unrestricted network access.

type: "unrestricted"

Network policy type

---

*Copyright © Anthropic. All rights reserved.*
