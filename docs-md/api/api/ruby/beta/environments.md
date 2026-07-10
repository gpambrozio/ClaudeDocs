# Environments

Copy page



Ruby

# Environments

##### [Create Environment](api/beta/environments/create.md)

beta.environments.create(\*\*kwargs) -> [BetaEnvironment](api/beta/environments.md) { id, archived\_at, config, 7 more }

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

beta.environments.list(\*\*kwargs) -> PageCursor<[BetaEnvironment](api/beta/environments.md) { id, archived\_at, config, 7 more } >

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

beta.environments.retrieve(environment\_id, \*\*kwargs) -> [BetaEnvironment](api/beta/environments.md) { id, archived\_at, config, 7 more }

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

beta.environments.update(environment\_id, \*\*kwargs) -> [BetaEnvironment](api/beta/environments.md) { id, archived\_at, config, 7 more }

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

beta.environments.delete(environment\_id, \*\*kwargs) -> [BetaEnvironmentDeleteResponse](api/beta/environments.md) { id, type }

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

beta.environments.archive(environment\_id, \*\*kwargs) -> [BetaEnvironment](api/beta/environments.md) { id, archived\_at, config, 7 more }

POST/v1/environments/{environment\_id}/archive

##### ModelsExpand Collapse



class BetaCloudConfig { networking, packages, type } 

`cloud` environment configuration.



networking: [BetaUnrestrictedNetwork](api/beta/environments.md) { type }  | [BetaLimitedNetwork](api/beta/environments.md) { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type } 

Network configuration policy.

One of the following:



class BetaUnrestrictedNetwork { type } 

Unrestricted network access.

type: :unrestricted

Network policy type



class BetaLimitedNetwork { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type } 

Limited network access.

allow\_mcp\_servers: bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: Array[String]

Specifies domains the container can reach.

type: :limited

Network policy type



packages: [BetaPackages](api/beta/environments.md) { apt, cargo, gem\_, 4 more } 

Package manager configuration.

apt: Array[String]

Ubuntu/Debian packages to install

cargo: Array[String]

Rust packages to install

gem\_: Array[String]

Ruby packages to install

go: Array[String]

Go packages to install

npm: Array[String]

Node.js packages to install

pip: Array[String]

Python packages to install

type: :packages

Package configuration type

type: :cloud

Environment type



class BetaCloudConfigParams { type, networking, packages } 

Request params for `cloud` environment configuration.

Fields default to null; on update, omitted fields preserve the
existing value.

type: :cloud

Environment type



networking: [BetaUnrestrictedNetwork](api/beta/environments.md) { type }  | [BetaLimitedNetworkParams](api/beta/environments.md) { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts } 

Network configuration policy. Omit on update to preserve the existing value.

One of the following:



class BetaUnrestrictedNetwork { type } 

Unrestricted network access.

type: :unrestricted

Network policy type



class BetaLimitedNetworkParams { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts } 

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

type: :limited

Network policy type

allow\_mcp\_servers: bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allow\_package\_managers: bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allowed\_hosts: Array[String]

Specifies domains the container can reach.



packages: [BetaPackagesParams](api/beta/environments.md) { apt, cargo, gem\_, 4 more } 

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

apt: Array[String]

Ubuntu/Debian packages to install

cargo: Array[String]

Rust packages to install

gem\_: Array[String]

Ruby packages to install

go: Array[String]

Go packages to install

npm: Array[String]

Node.js packages to install

pip: Array[String]

Python packages to install

type: :packages

Package configuration type



class BetaEnvironment { id, archived\_at, config, 7 more } 

Unified Environment resource for both cloud and self-hosted environments.

id: String

Environment identifier (e.g., 'env\_...')

archived\_at: String

RFC 3339 timestamp when environment was archived, or null if not archived



config: [BetaCloudConfig](api/beta/environments.md) { networking, packages, type }  | [BetaSelfHostedConfig](api/beta/environments.md) { type } 

Environment configuration (either Anthropic Cloud or self-hosted)

One of the following:



class BetaCloudConfig { networking, packages, type } 

`cloud` environment configuration.



networking: [BetaUnrestrictedNetwork](api/beta/environments.md) { type }  | [BetaLimitedNetwork](api/beta/environments.md) { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type } 

Network configuration policy.

One of the following:



class BetaUnrestrictedNetwork { type } 

Unrestricted network access.

type: :unrestricted

Network policy type



class BetaLimitedNetwork { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type } 

Limited network access.

allow\_mcp\_servers: bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: Array[String]

Specifies domains the container can reach.

type: :limited

Network policy type



packages: [BetaPackages](api/beta/environments.md) { apt, cargo, gem\_, 4 more } 

Package manager configuration.

apt: Array[String]

Ubuntu/Debian packages to install

cargo: Array[String]

Rust packages to install

gem\_: Array[String]

Ruby packages to install

go: Array[String]

Go packages to install

npm: Array[String]

Node.js packages to install

pip: Array[String]

Python packages to install

type: :packages

Package configuration type

type: :cloud

Environment type



class BetaSelfHostedConfig { type } 

Configuration for self-hosted environments.

type: :self\_hosted

Environment type

created\_at: String

RFC 3339 timestamp when environment was created

description: String

User-provided description for the environment

metadata: Hash[Symbol, String]

User-provided metadata key-value pairs

name: String

Human-readable name for the environment

type: :environment

The type of object (always 'environment')

updated\_at: String

RFC 3339 timestamp when environment was last updated



scope: :organization | :account

The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

One of the following:

:organization

:account



class BetaEnvironmentDeleteResponse { id, type } 

Response after deleting an environment.

id: String

Environment identifier

type: :environment\_deleted

The type of response



class BetaLimitedNetwork { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type } 

Limited network access.

allow\_mcp\_servers: bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: Array[String]

Specifies domains the container can reach.

type: :limited

Network policy type



class BetaLimitedNetworkParams { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts } 

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

type: :limited

Network policy type

allow\_mcp\_servers: bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allow\_package\_managers: bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allowed\_hosts: Array[String]

Specifies domains the container can reach.



class BetaPackages { apt, cargo, gem\_, 4 more } 

Packages (and their versions) available in this environment.

apt: Array[String]

Ubuntu/Debian packages to install

cargo: Array[String]

Rust packages to install

gem\_: Array[String]

Ruby packages to install

go: Array[String]

Go packages to install

npm: Array[String]

Node.js packages to install

pip: Array[String]

Python packages to install

type: :packages

Package configuration type



class BetaPackagesParams { apt, cargo, gem\_, 4 more } 

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

apt: Array[String]

Ubuntu/Debian packages to install

cargo: Array[String]

Rust packages to install

gem\_: Array[String]

Ruby packages to install

go: Array[String]

Go packages to install

npm: Array[String]

Node.js packages to install

pip: Array[String]

Python packages to install

type: :packages

Package configuration type



class BetaSelfHostedConfig { type } 

Configuration for self-hosted environments.

type: :self\_hosted

Environment type



class BetaSelfHostedConfigParams { type } 

Request params for `self_hosted` environment configuration.

type: :self\_hosted

Environment type



class BetaUnrestrictedNetwork { type } 

Unrestricted network access.

type: :unrestricted

Network policy type

#### EnvironmentsWork

##### [Get Work Item](api/beta/environments/work/retrieve.md)

beta.environments.work.retrieve(work\_id, \*\*kwargs) -> [BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 9 more }

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

beta.environments.work.poll(environment\_id, \*\*kwargs) -> [BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 9 more }

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

beta.environments.work.ack(work\_id, \*\*kwargs) -> [BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 9 more }

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

beta.environments.work.heartbeat(work\_id, \*\*kwargs) -> [BetaSelfHostedWorkHeartbeatResponse](api/beta/environments/work.md) { last\_heartbeat, lease\_extended, state, 2 more }

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

beta.environments.work.stop(work\_id, \*\*kwargs) -> [BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 9 more }

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

beta.environments.work.list(environment\_id, \*\*kwargs) -> PageCursor<[BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 9 more } >

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

beta.environments.work.update(work\_id, \*\*kwargs) -> [BetaSelfHostedWork](api/beta/environments/work.md) { id, acknowledged\_at, created\_at, 9 more }

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

beta.environments.work.stats(environment\_id, \*\*kwargs) -> [BetaSelfHostedWorkQueueStats](api/beta/environments/work.md) { depth, oldest\_queued\_at, pending, 2 more }

GET/v1/environments/{environment\_id}/work/stats

---

*Copyright © Anthropic. All rights reserved.*
