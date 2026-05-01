# Environments

Copy page

Java

# Environments

##### [Create Environment](api/beta/environments/create.md)

[BetaEnvironment](api/beta.md) beta().environments().create(EnvironmentCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

EnvironmentListPage beta().environments().list(EnvironmentListParamsparams = EnvironmentListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

[BetaEnvironment](api/beta.md) beta().environments().retrieve(EnvironmentRetrieveParamsparams = EnvironmentRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

[BetaEnvironment](api/beta.md) beta().environments().update(EnvironmentUpdateParamsparams = EnvironmentUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

[BetaEnvironmentDeleteResponse](api/beta.md) beta().environments().delete(EnvironmentDeleteParamsparams = EnvironmentDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

[BetaEnvironment](api/beta.md) beta().environments().archive(EnvironmentArchiveParamsparams = EnvironmentArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/environments/{environment\_id}/archive

##### ModelsExpand Collapse

class BetaCloudConfig:

`cloud` environment configuration.

Networking networking

Network configuration policy.

Accepts one of the following:

class BetaUnrestrictedNetwork:

Unrestricted network access.

JsonValue; type "unrestricted"constant"unrestricted"constant

Network policy type

class BetaLimitedNetwork:

Limited network access.

boolean allowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

boolean allowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

List<String> allowedHosts

Specifies domains the container can reach.

JsonValue; type "limited"constant"limited"constant

Network policy type

[BetaPackages](api/beta.md) packages

Package manager configuration.

List<String> apt

Ubuntu/Debian packages to install

List<String> cargo

Rust packages to install

List<String> gem

Ruby packages to install

List<String> go

Go packages to install

List<String> npm

Node.js packages to install

List<String> pip

Python packages to install

Optional<Type> type

Package configuration type

JsonValue; type "cloud"constant"cloud"constant

Environment type

class BetaCloudConfigParams:

Request params for `cloud` environment configuration.

Fields default to null; on update, omitted fields preserve the
existing value.

JsonValue; type "cloud"constant"cloud"constant

Environment type

Optional<Networking> networking

Network configuration policy. Omit on update to preserve the existing value.

Accepts one of the following:

class BetaUnrestrictedNetwork:

Unrestricted network access.

JsonValue; type "unrestricted"constant"unrestricted"constant

Network policy type

class BetaLimitedNetworkParams:

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

JsonValue; type "limited"constant"limited"constant

Network policy type

Optional<Boolean> allowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

Optional<Boolean> allowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

Optional<List<String>> allowedHosts

Specifies domains the container can reach.

Optional<[BetaPackagesParams](api/beta.md)> packages

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

Optional<List<String>> apt

Ubuntu/Debian packages to install

Optional<List<String>> cargo

Rust packages to install

Optional<List<String>> gem

Ruby packages to install

Optional<List<String>> go

Go packages to install

Optional<List<String>> npm

Node.js packages to install

Optional<List<String>> pip

Python packages to install

Optional<Type> type

Package configuration type

class BetaEnvironment:

Unified Environment resource for both cloud and self-hosted environments.

String id

Environment identifier (e.g., 'env\_...')

Optional<String> archivedAt

RFC 3339 timestamp when environment was archived, or null if not archived

[BetaCloudConfig](api/beta.md) config

`cloud` environment configuration.

Networking networking

Network configuration policy.

Accepts one of the following:

class BetaUnrestrictedNetwork:

Unrestricted network access.

JsonValue; type "unrestricted"constant"unrestricted"constant

Network policy type

class BetaLimitedNetwork:

Limited network access.

boolean allowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

boolean allowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

List<String> allowedHosts

Specifies domains the container can reach.

JsonValue; type "limited"constant"limited"constant

Network policy type

[BetaPackages](api/beta.md) packages

Package manager configuration.

List<String> apt

Ubuntu/Debian packages to install

List<String> cargo

Rust packages to install

List<String> gem

Ruby packages to install

List<String> go

Go packages to install

List<String> npm

Node.js packages to install

List<String> pip

Python packages to install

Optional<Type> type

Package configuration type

JsonValue; type "cloud"constant"cloud"constant

Environment type

String createdAt

RFC 3339 timestamp when environment was created

String description

User-provided description for the environment

Metadata metadata

User-provided metadata key-value pairs

String name

Human-readable name for the environment

JsonValue; type "environment"constant"environment"constant

The type of object (always 'environment')

String updatedAt

RFC 3339 timestamp when environment was last updated

class BetaEnvironmentDeleteResponse:

Response after deleting an environment.

String id

Environment identifier

JsonValue; type "environment\_deleted"constant"environment\_deleted"constant

The type of response

class BetaLimitedNetwork:

Limited network access.

boolean allowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

boolean allowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

List<String> allowedHosts

Specifies domains the container can reach.

JsonValue; type "limited"constant"limited"constant

Network policy type

class BetaLimitedNetworkParams:

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

JsonValue; type "limited"constant"limited"constant

Network policy type

Optional<Boolean> allowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

Optional<Boolean> allowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

Optional<List<String>> allowedHosts

Specifies domains the container can reach.

class BetaPackages:

Packages (and their versions) available in this environment.

List<String> apt

Ubuntu/Debian packages to install

List<String> cargo

Rust packages to install

List<String> gem

Ruby packages to install

List<String> go

Go packages to install

List<String> npm

Node.js packages to install

List<String> pip

Python packages to install

Optional<Type> type

Package configuration type

class BetaPackagesParams:

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

Optional<List<String>> apt

Ubuntu/Debian packages to install

Optional<List<String>> cargo

Rust packages to install

Optional<List<String>> gem

Ruby packages to install

Optional<List<String>> go

Go packages to install

Optional<List<String>> npm

Node.js packages to install

Optional<List<String>> pip

Python packages to install

Optional<Type> type

Package configuration type

class BetaUnrestrictedNetwork:

Unrestricted network access.

JsonValue; type "unrestricted"constant"unrestricted"constant

Network policy type

---

*Copyright © Anthropic. All rights reserved.*
