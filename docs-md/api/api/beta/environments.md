# Environments

Copy page



cURL

# Environments

##### [Create Environment](api/http/beta/environments/create.md)

POST/v1/environments

##### [List Environments](api/http/beta/environments/list.md)

GET/v1/environments

##### [Get Environment](api/http/beta/environments/retrieve.md)

GET/v1/environments/{environment\_id}

##### [Update Environment](api/http/beta/environments/update.md)

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/http/beta/environments/delete.md)

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/http/beta/environments/archive.md)

POST/v1/environments/{environment\_id}/archive

##### Models



BetaCloudConfig object{ networking, packages, type }

`cloud` environment configuration.



BetaCloudConfigParams object{ type, networking, packages }

Request params for `cloud` environment configuration.

Fields default to null; on update, omitted fields preserve the
existing value.



BetaEnvironment object{ id, archived\_at, config, 7 more }

Unified Environment resource for both cloud and self-hosted environments.



BetaEnvironmentDeleteResponse object{ id, type }

Response after deleting an environment.

id: string

Environment identifier



type: "environment\_deleted"

The type of response

defaultenvironment\_deleted



BetaLimitedNetwork object{ allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Limited network access.

allow\_mcp\_servers: boolean

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: boolean

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: array of string

Specifies domains the container can reach.

type: "limited"

Network policy type



BetaLimitedNetworkParams object{ type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts }

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

type: "limited"

Network policy type

allow\_mcp\_servers: optional boolean or null

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allow\_package\_managers: optional boolean or null

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allowed\_hosts: optional array of string or null

Specifies domains the container can reach.



BetaPackages object{ apt, cargo, gem, 4 more }

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



type: optional "packages"

Package configuration type

defaultpackages



BetaPackagesParams object{ apt, cargo, gem, 4 more }

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

apt: optional array of string or null

Ubuntu/Debian packages to install

cargo: optional array of string or null

Rust packages to install

gem: optional array of string or null

Ruby packages to install

go: optional array of string or null

Go packages to install

npm: optional array of string or null

Node.js packages to install

pip: optional array of string or null

Python packages to install



type: optional "packages"

Package configuration type

defaultpackages



BetaSelfHostedConfig object{ type }

Configuration for self-hosted environments.

type: "self\_hosted"

Environment type



BetaSelfHostedConfigParams object{ type }

Request params for `self_hosted` environment configuration.

type: "self\_hosted"

Environment type



BetaUnrestrictedNetwork object{ type }

Unrestricted network access.

type: "unrestricted"

Network policy type

#### Environments[Work](api/http/beta/environments/work.md)

##### [Get Work Item](api/http/beta/environments/work/retrieve.md)

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/http/beta/environments/work/poll.md)

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/http/beta/environments/work/ack.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/http/beta/environments/work/heartbeat.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/http/beta/environments/work/stop.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/http/beta/environments/work/list.md)

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/http/beta/environments/work/update.md)

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/http/beta/environments/work/stats.md)

GET/v1/environments/{environment\_id}/work/stats

---

*Copyright © Anthropic. All rights reserved.*
