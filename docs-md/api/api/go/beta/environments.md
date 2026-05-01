# Environments

Copy page

Go

# Environments

##### [Create Environment](api/beta/environments/create.md)

client.Beta.Environments.New(ctx, params) (\*[BetaEnvironment](api/beta.md), error)

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

client.Beta.Environments.List(ctx, params) (\*PageCursor[[BetaEnvironment](api/beta.md)], error)

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

client.Beta.Environments.Get(ctx, environmentID, query) (\*[BetaEnvironment](api/beta.md), error)

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

client.Beta.Environments.Update(ctx, environmentID, params) (\*[BetaEnvironment](api/beta.md), error)

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

client.Beta.Environments.Delete(ctx, environmentID, body) (\*[BetaEnvironmentDeleteResponse](api/beta.md), error)

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

client.Beta.Environments.Archive(ctx, environmentID, body) (\*[BetaEnvironment](api/beta.md), error)

POST/v1/environments/{environment\_id}/archive

##### ModelsExpand Collapse

type BetaCloudConfig struct{…}

`cloud` environment configuration.

Networking BetaCloudConfigNetworkingUnion

Network configuration policy.

Accepts one of the following:

type BetaUnrestrictedNetwork struct{…}

Unrestricted network access.

Type Unrestricted

Network policy type

type BetaLimitedNetwork struct{…}

Limited network access.

AllowMCPServers bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

AllowPackageManagers bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

AllowedHosts []string

Specifies domains the container can reach.

Type Limited

Network policy type

Packages [BetaPackages](api/beta.md)

Package manager configuration.

Apt []string

Ubuntu/Debian packages to install

Cargo []string

Rust packages to install

Gem []string

Ruby packages to install

Go []string

Go packages to install

Npm []string

Node.js packages to install

Pip []string

Python packages to install

Type BetaPackagesTypeoptional

Package configuration type

Type Cloud

Environment type

type BetaCloudConfigParamsResp struct{…}

Request params for `cloud` environment configuration.

Fields default to null; on update, omitted fields preserve the
existing value.

Type Cloud

Environment type

Networking BetaCloudConfigParamsNetworkingUnionRespoptional

Network configuration policy. Omit on update to preserve the existing value.

Accepts one of the following:

type BetaUnrestrictedNetwork struct{…}

Unrestricted network access.

Type Unrestricted

Network policy type

type BetaLimitedNetworkParamsResp struct{…}

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

Type Limited

Network policy type

AllowMCPServers booloptional

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

AllowPackageManagers booloptional

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

AllowedHosts []stringoptional

Specifies domains the container can reach.

Packages [BetaPackagesParamsResp](api/beta.md)optional

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

Apt []stringoptional

Ubuntu/Debian packages to install

Cargo []stringoptional

Rust packages to install

Gem []stringoptional

Ruby packages to install

Go []stringoptional

Go packages to install

Npm []stringoptional

Node.js packages to install

Pip []stringoptional

Python packages to install

Type BetaPackagesParamsTypeoptional

Package configuration type

type BetaEnvironment struct{…}

Unified Environment resource for both cloud and self-hosted environments.

ID string

Environment identifier (e.g., 'env\_...')

ArchivedAt string

RFC 3339 timestamp when environment was archived, or null if not archived

Config [BetaCloudConfig](api/beta.md)

`cloud` environment configuration.

Networking BetaCloudConfigNetworkingUnion

Network configuration policy.

Accepts one of the following:

type BetaUnrestrictedNetwork struct{…}

Unrestricted network access.

Type Unrestricted

Network policy type

type BetaLimitedNetwork struct{…}

Limited network access.

AllowMCPServers bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

AllowPackageManagers bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

AllowedHosts []string

Specifies domains the container can reach.

Type Limited

Network policy type

Packages [BetaPackages](api/beta.md)

Package manager configuration.

Apt []string

Ubuntu/Debian packages to install

Cargo []string

Rust packages to install

Gem []string

Ruby packages to install

Go []string

Go packages to install

Npm []string

Node.js packages to install

Pip []string

Python packages to install

Type BetaPackagesTypeoptional

Package configuration type

Type Cloud

Environment type

CreatedAt string

RFC 3339 timestamp when environment was created

Description string

User-provided description for the environment

Metadata map[string, string]

User-provided metadata key-value pairs

Name string

Human-readable name for the environment

Type Environment

The type of object (always 'environment')

UpdatedAt string

RFC 3339 timestamp when environment was last updated

type BetaEnvironmentDeleteResponse struct{…}

Response after deleting an environment.

ID string

Environment identifier

Type EnvironmentDeleted

The type of response

type BetaLimitedNetwork struct{…}

Limited network access.

AllowMCPServers bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

AllowPackageManagers bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

AllowedHosts []string

Specifies domains the container can reach.

Type Limited

Network policy type

type BetaLimitedNetworkParamsResp struct{…}

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

Type Limited

Network policy type

AllowMCPServers booloptional

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

AllowPackageManagers booloptional

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

AllowedHosts []stringoptional

Specifies domains the container can reach.

type BetaPackages struct{…}

Packages (and their versions) available in this environment.

Apt []string

Ubuntu/Debian packages to install

Cargo []string

Rust packages to install

Gem []string

Ruby packages to install

Go []string

Go packages to install

Npm []string

Node.js packages to install

Pip []string

Python packages to install

Type BetaPackagesTypeoptional

Package configuration type

type BetaPackagesParamsResp struct{…}

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

Apt []stringoptional

Ubuntu/Debian packages to install

Cargo []stringoptional

Rust packages to install

Gem []stringoptional

Ruby packages to install

Go []stringoptional

Go packages to install

Npm []stringoptional

Node.js packages to install

Pip []stringoptional

Python packages to install

Type BetaPackagesParamsTypeoptional

Package configuration type

type BetaUnrestrictedNetwork struct{…}

Unrestricted network access.

Type Unrestricted

Network policy type

---

*Copyright © Anthropic. All rights reserved.*
