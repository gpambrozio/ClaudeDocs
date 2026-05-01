# Environments

Copy page

TypeScript

# Environments

##### [Create Environment](api/beta/environments/create.md)

client.beta.environments.create(EnvironmentCreateParams { name, config, description, 2 more } params, RequestOptionsoptions?): [BetaEnvironment](api/beta.md) { id, archived\_at, config, 6 more }

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

client.beta.environments.list(EnvironmentListParams { include\_archived, limit, page, betas } params?, RequestOptionsoptions?): PageCursor<[BetaEnvironment](api/beta.md) { id, archived\_at, config, 6 more } >

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

client.beta.environments.retrieve(stringenvironmentID, EnvironmentRetrieveParams { betas } params?, RequestOptionsoptions?): [BetaEnvironment](api/beta.md) { id, archived\_at, config, 6 more }

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

client.beta.environments.update(stringenvironmentID, EnvironmentUpdateParams { config, description, metadata, 2 more } params, RequestOptionsoptions?): [BetaEnvironment](api/beta.md) { id, archived\_at, config, 6 more }

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

client.beta.environments.delete(stringenvironmentID, EnvironmentDeleteParams { betas } params?, RequestOptionsoptions?): [BetaEnvironmentDeleteResponse](api/beta.md) { id, type }

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

client.beta.environments.archive(stringenvironmentID, EnvironmentArchiveParams { betas } params?, RequestOptionsoptions?): [BetaEnvironment](api/beta.md) { id, archived\_at, config, 6 more }

POST/v1/environments/{environment\_id}/archive

##### ModelsExpand Collapse

BetaCloudConfig { networking, packages, type }

`cloud` environment configuration.

networking: [BetaUnrestrictedNetwork](api/beta.md) { type }  | [BetaLimitedNetwork](api/beta.md) { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Network configuration policy.

Accepts one of the following:

BetaUnrestrictedNetwork { type }

Unrestricted network access.

type: "unrestricted"

Network policy type

BetaLimitedNetwork { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Limited network access.

allow\_mcp\_servers: boolean

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: boolean

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: Array<string>

Specifies domains the container can reach.

type: "limited"

Network policy type

packages: [BetaPackages](api/beta.md) { apt, cargo, gem, 4 more }

Package manager configuration.

apt: Array<string>

Ubuntu/Debian packages to install

cargo: Array<string>

Rust packages to install

gem: Array<string>

Ruby packages to install

go: Array<string>

Go packages to install

npm: Array<string>

Node.js packages to install

pip: Array<string>

Python packages to install

type?: "packages"

Package configuration type

type: "cloud"

Environment type

BetaCloudConfigParams { type, networking, packages }

Request params for `cloud` environment configuration.

Fields default to null; on update, omitted fields preserve the
existing value.

type: "cloud"

Environment type

networking?: [BetaUnrestrictedNetwork](api/beta.md) { type }  | [BetaLimitedNetworkParams](api/beta.md) { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts }  | null

Network configuration policy. Omit on update to preserve the existing value.

Accepts one of the following:

BetaUnrestrictedNetwork { type }

Unrestricted network access.

type: "unrestricted"

Network policy type

BetaLimitedNetworkParams { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts }

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

type: "limited"

Network policy type

allow\_mcp\_servers?: boolean | null

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allow\_package\_managers?: boolean | null

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allowed\_hosts?: Array<string> | null

Specifies domains the container can reach.

packages?: [BetaPackagesParams](api/beta.md) { apt, cargo, gem, 4 more }  | null

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

apt?: Array<string> | null

Ubuntu/Debian packages to install

cargo?: Array<string> | null

Rust packages to install

gem?: Array<string> | null

Ruby packages to install

go?: Array<string> | null

Go packages to install

npm?: Array<string> | null

Node.js packages to install

pip?: Array<string> | null

Python packages to install

type?: "packages"

Package configuration type

BetaEnvironment { id, archived\_at, config, 6 more }

Unified Environment resource for both cloud and self-hosted environments.

id: string

Environment identifier (e.g., 'env\_...')

archived\_at: string | null

RFC 3339 timestamp when environment was archived, or null if not archived

config: [BetaCloudConfig](api/beta.md) { networking, packages, type }

`cloud` environment configuration.

networking: [BetaUnrestrictedNetwork](api/beta.md) { type }  | [BetaLimitedNetwork](api/beta.md) { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Network configuration policy.

Accepts one of the following:

BetaUnrestrictedNetwork { type }

Unrestricted network access.

type: "unrestricted"

Network policy type

BetaLimitedNetwork { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Limited network access.

allow\_mcp\_servers: boolean

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: boolean

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: Array<string>

Specifies domains the container can reach.

type: "limited"

Network policy type

packages: [BetaPackages](api/beta.md) { apt, cargo, gem, 4 more }

Package manager configuration.

apt: Array<string>

Ubuntu/Debian packages to install

cargo: Array<string>

Rust packages to install

gem: Array<string>

Ruby packages to install

go: Array<string>

Go packages to install

npm: Array<string>

Node.js packages to install

pip: Array<string>

Python packages to install

type?: "packages"

Package configuration type

type: "cloud"

Environment type

created\_at: string

RFC 3339 timestamp when environment was created

description: string

User-provided description for the environment

metadata: Record<string, string>

User-provided metadata key-value pairs

name: string

Human-readable name for the environment

type: "environment"

The type of object (always 'environment')

updated\_at: string

RFC 3339 timestamp when environment was last updated

BetaEnvironmentDeleteResponse { id, type }

Response after deleting an environment.

id: string

Environment identifier

type: "environment\_deleted"

The type of response

BetaLimitedNetwork { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Limited network access.

allow\_mcp\_servers: boolean

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: boolean

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: Array<string>

Specifies domains the container can reach.

type: "limited"

Network policy type

BetaLimitedNetworkParams { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts }

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

type: "limited"

Network policy type

allow\_mcp\_servers?: boolean | null

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allow\_package\_managers?: boolean | null

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allowed\_hosts?: Array<string> | null

Specifies domains the container can reach.

BetaPackages { apt, cargo, gem, 4 more }

Packages (and their versions) available in this environment.

apt: Array<string>

Ubuntu/Debian packages to install

cargo: Array<string>

Rust packages to install

gem: Array<string>

Ruby packages to install

go: Array<string>

Go packages to install

npm: Array<string>

Node.js packages to install

pip: Array<string>

Python packages to install

type?: "packages"

Package configuration type

BetaPackagesParams { apt, cargo, gem, 4 more }

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

apt?: Array<string> | null

Ubuntu/Debian packages to install

cargo?: Array<string> | null

Rust packages to install

gem?: Array<string> | null

Ruby packages to install

go?: Array<string> | null

Go packages to install

npm?: Array<string> | null

Node.js packages to install

pip?: Array<string> | null

Python packages to install

type?: "packages"

Package configuration type

BetaUnrestrictedNetwork { type }

Unrestricted network access.

type: "unrestricted"

Network policy type

---

*Copyright © Anthropic. All rights reserved.*
