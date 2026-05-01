# Environments

Copy page

C#

# Environments

##### [Create Environment](api/beta/environments/create.md)

[BetaEnvironment](api/beta.md) Beta.Environments.Create(EnvironmentCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

[EnvironmentListPageResponse](api/beta.md) Beta.Environments.List(EnvironmentListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

[BetaEnvironment](api/beta.md) Beta.Environments.Retrieve(EnvironmentRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

[BetaEnvironment](api/beta.md) Beta.Environments.Update(EnvironmentUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

[BetaEnvironmentDeleteResponse](api/beta.md) Beta.Environments.Delete(EnvironmentDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

[BetaEnvironment](api/beta.md) Beta.Environments.Archive(EnvironmentArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/environments/{environment\_id}/archive

##### ModelsExpand Collapse

class BetaCloudConfig:

`cloud` environment configuration.

required Networking Networking

Network configuration policy.

Accepts one of the following:

class BetaUnrestrictedNetwork:

Unrestricted network access.

JsonElement Type "unrestricted"constant

Network policy type

class BetaLimitedNetwork:

Limited network access.

required Boolean AllowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

required Boolean AllowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

required IReadOnlyList<string> AllowedHosts

Specifies domains the container can reach.

JsonElement Type "limited"constant

Network policy type

required [BetaPackages](api/beta.md) Packages

Package manager configuration.

required IReadOnlyList<string> Apt

Ubuntu/Debian packages to install

required IReadOnlyList<string> Cargo

Rust packages to install

required IReadOnlyList<string> Gem

Ruby packages to install

required IReadOnlyList<string> Go

Go packages to install

required IReadOnlyList<string> Npm

Node.js packages to install

required IReadOnlyList<string> Pip

Python packages to install

Type Type

Package configuration type

JsonElement Type "cloud"constant

Environment type

class BetaCloudConfigParams:

Request params for `cloud` environment configuration.

Fields default to null; on update, omitted fields preserve the
existing value.

JsonElement Type "cloud"constant

Environment type

Networking? Networking

Network configuration policy. Omit on update to preserve the existing value.

Accepts one of the following:

class BetaUnrestrictedNetwork:

Unrestricted network access.

JsonElement Type "unrestricted"constant

Network policy type

class BetaLimitedNetworkParams:

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

JsonElement Type "limited"constant

Network policy type

Boolean? AllowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

Boolean? AllowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

IReadOnlyList<string>? AllowedHosts

Specifies domains the container can reach.

[BetaPackagesParams](api/beta.md)? Packages

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

IReadOnlyList<string>? Apt

Ubuntu/Debian packages to install

IReadOnlyList<string>? Cargo

Rust packages to install

IReadOnlyList<string>? Gem

Ruby packages to install

IReadOnlyList<string>? Go

Go packages to install

IReadOnlyList<string>? Npm

Node.js packages to install

IReadOnlyList<string>? Pip

Python packages to install

Type Type

Package configuration type

class BetaEnvironment:

Unified Environment resource for both cloud and self-hosted environments.

required string ID

Environment identifier (e.g., 'env\_...')

required string? ArchivedAt

RFC 3339 timestamp when environment was archived, or null if not archived

required [BetaCloudConfig](api/beta.md) Config

`cloud` environment configuration.

required Networking Networking

Network configuration policy.

Accepts one of the following:

class BetaUnrestrictedNetwork:

Unrestricted network access.

JsonElement Type "unrestricted"constant

Network policy type

class BetaLimitedNetwork:

Limited network access.

required Boolean AllowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

required Boolean AllowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

required IReadOnlyList<string> AllowedHosts

Specifies domains the container can reach.

JsonElement Type "limited"constant

Network policy type

required [BetaPackages](api/beta.md) Packages

Package manager configuration.

required IReadOnlyList<string> Apt

Ubuntu/Debian packages to install

required IReadOnlyList<string> Cargo

Rust packages to install

required IReadOnlyList<string> Gem

Ruby packages to install

required IReadOnlyList<string> Go

Go packages to install

required IReadOnlyList<string> Npm

Node.js packages to install

required IReadOnlyList<string> Pip

Python packages to install

Type Type

Package configuration type

JsonElement Type "cloud"constant

Environment type

required string CreatedAt

RFC 3339 timestamp when environment was created

required string Description

User-provided description for the environment

required IReadOnlyDictionary<string, string> Metadata

User-provided metadata key-value pairs

required string Name

Human-readable name for the environment

JsonElement Type "environment"constant

The type of object (always 'environment')

required string UpdatedAt

RFC 3339 timestamp when environment was last updated

class BetaEnvironmentDeleteResponse:

Response after deleting an environment.

required string ID

Environment identifier

JsonElement Type "environment\_deleted"constant

The type of response

class BetaLimitedNetwork:

Limited network access.

required Boolean AllowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

required Boolean AllowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

required IReadOnlyList<string> AllowedHosts

Specifies domains the container can reach.

JsonElement Type "limited"constant

Network policy type

class BetaLimitedNetworkParams:

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

JsonElement Type "limited"constant

Network policy type

Boolean? AllowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

Boolean? AllowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

IReadOnlyList<string>? AllowedHosts

Specifies domains the container can reach.

class BetaPackages:

Packages (and their versions) available in this environment.

required IReadOnlyList<string> Apt

Ubuntu/Debian packages to install

required IReadOnlyList<string> Cargo

Rust packages to install

required IReadOnlyList<string> Gem

Ruby packages to install

required IReadOnlyList<string> Go

Go packages to install

required IReadOnlyList<string> Npm

Node.js packages to install

required IReadOnlyList<string> Pip

Python packages to install

Type Type

Package configuration type

class BetaPackagesParams:

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

IReadOnlyList<string>? Apt

Ubuntu/Debian packages to install

IReadOnlyList<string>? Cargo

Rust packages to install

IReadOnlyList<string>? Gem

Ruby packages to install

IReadOnlyList<string>? Go

Go packages to install

IReadOnlyList<string>? Npm

Node.js packages to install

IReadOnlyList<string>? Pip

Python packages to install

Type Type

Package configuration type

class BetaUnrestrictedNetwork:

Unrestricted network access.

JsonElement Type "unrestricted"constant

Network policy type

---

*Copyright © Anthropic. All rights reserved.*
