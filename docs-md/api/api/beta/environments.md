# Environments

Copy page



cURL

# Environments

##### [Create Environment](api/beta/environments/create.md)

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

POST/v1/environments/{environment\_id}/archive

##### ModelsExpand Collapse



BetaCloudConfig object { networking, packages, type } 

`cloud` environment configuration.



networking: [BetaUnrestrictedNetwork](api/beta.md) { type }  or [BetaLimitedNetwork](api/beta.md) { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type } 

Network configuration policy.

One of the following:



BetaUnrestrictedNetwork object { type } 

Unrestricted network access.

type: "unrestricted"

Network policy type



BetaLimitedNetwork object { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type } 

Limited network access.

allow\_mcp\_servers: boolean

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: boolean

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: array of string

Specifies domains the container can reach.

type: "limited"

Network policy type



packages: [BetaPackages](api/beta.md) { apt, cargo, gem, 4 more } 

Package manager configuration.

apt: array of string

Ubuntu/Debian packages to install

cargo: array of string

Rust packages to install

gem: array of string

Ruby packages to install

go: array of string

Go packages to install

npm: array of string

Node.js packages to install

pip: array of string

Python packages to install

type: optional "packages"

Package configuration type

type: "cloud"

Environment type



BetaCloudConfigParams object { type, networking, packages } 

Request params for `cloud` environment configuration.

Fields default to null; on update, omitted fields preserve the
existing value.

type: "cloud"

Environment type



networking: optional [BetaUnrestrictedNetwork](api/beta.md) { type }  or [BetaLimitedNetworkParams](api/beta.md) { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts } 

Network configuration policy. Omit on update to preserve the existing value.

One of the following:



BetaUnrestrictedNetwork object { type } 

Unrestricted network access.

type: "unrestricted"

Network policy type



BetaLimitedNetworkParams object { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts } 

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

type: "limited"

Network policy type

allow\_mcp\_servers: optional boolean

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allow\_package\_managers: optional boolean

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allowed\_hosts: optional array of string

Specifies domains the container can reach.



packages: optional [BetaPackagesParams](api/beta.md) { apt, cargo, gem, 4 more } 

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

apt: optional array of string

Ubuntu/Debian packages to install

cargo: optional array of string

Rust packages to install

gem: optional array of string

Ruby packages to install

go: optional array of string

Go packages to install

npm: optional array of string

Node.js packages to install

pip: optional array of string

Python packages to install

type: optional "packages"

Package configuration type



BetaEnvironment object { id, archived\_at, config, 7 more } 

Unified Environment resource for both cloud and self-hosted environments.

id: string

Environment identifier (e.g., 'env\_...')

archived\_at: string

RFC 3339 timestamp when environment was archived, or null if not archived



config: [BetaCloudConfig](api/beta.md) { networking, packages, type }  or [BetaSelfHostedConfig](api/beta.md) { type } 

Environment configuration (either Anthropic Cloud or self-hosted)

One of the following:



BetaCloudConfig object { networking, packages, type } 

`cloud` environment configuration.



networking: [BetaUnrestrictedNetwork](api/beta.md) { type }  or [BetaLimitedNetwork](api/beta.md) { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type } 

Network configuration policy.

One of the following:



BetaUnrestrictedNetwork object { type } 

Unrestricted network access.

type: "unrestricted"

Network policy type



BetaLimitedNetwork object { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type } 

Limited network access.

allow\_mcp\_servers: boolean

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: boolean

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: array of string

Specifies domains the container can reach.

type: "limited"

Network policy type



packages: [BetaPackages](api/beta.md) { apt, cargo, gem, 4 more } 

Package manager configuration.

apt: array of string

Ubuntu/Debian packages to install

cargo: array of string

Rust packages to install

gem: array of string

Ruby packages to install

go: array of string

Go packages to install

npm: array of string

Node.js packages to install

pip: array of string

Python packages to install

type: optional "packages"

Package configuration type

type: "cloud"

Environment type



BetaSelfHostedConfig object { type } 

Configuration for self-hosted environments.

type: "self\_hosted"

Environment type

created\_at: string

RFC 3339 timestamp when environment was created

description: string

User-provided description for the environment

metadata: map[string]

User-provided metadata key-value pairs

name: string

Human-readable name for the environment

type: "environment"

The type of object (always 'environment')

updated\_at: string

RFC 3339 timestamp when environment was last updated



scope: optional "organization" or "account"

The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

One of the following:

"organization"

"account"



BetaEnvironmentDeleteResponse object { id, type } 

Response after deleting an environment.

id: string

Environment identifier

type: "environment\_deleted"

The type of response



BetaLimitedNetwork object { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type } 

Limited network access.

allow\_mcp\_servers: boolean

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: boolean

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: array of string

Specifies domains the container can reach.

type: "limited"

Network policy type



BetaLimitedNetworkParams object { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts } 

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

type: "limited"

Network policy type

allow\_mcp\_servers: optional boolean

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allow\_package\_managers: optional boolean

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allowed\_hosts: optional array of string

Specifies domains the container can reach.



BetaPackages object { apt, cargo, gem, 4 more } 

Packages (and their versions) available in this environment.

apt: array of string

Ubuntu/Debian packages to install

cargo: array of string

Rust packages to install

gem: array of string

Ruby packages to install

go: array of string

Go packages to install

npm: array of string

Node.js packages to install

pip: array of string

Python packages to install

type: optional "packages"

Package configuration type



BetaPackagesParams object { apt, cargo, gem, 4 more } 

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

apt: optional array of string

Ubuntu/Debian packages to install

cargo: optional array of string

Rust packages to install

gem: optional array of string

Ruby packages to install

go: optional array of string

Go packages to install

npm: optional array of string

Node.js packages to install

pip: optional array of string

Python packages to install

type: optional "packages"

Package configuration type



BetaSelfHostedConfig object { type } 

Configuration for self-hosted environments.

type: "self\_hosted"

Environment type



BetaSelfHostedConfigParams object { type } 

Request params for `self_hosted` environment configuration.

type: "self\_hosted"

Environment type



BetaUnrestrictedNetwork object { type } 

Unrestricted network access.

type: "unrestricted"

Network policy type

#### EnvironmentsWork

##### [Get Work Item](api/beta/environments/work/retrieve.md)

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

GET/v1/environments/{environment\_id}/work/stats

##### ModelsExpand Collapse



BetaSelfHostedWork object { id, acknowledged\_at, created\_at, 9 more } 

Work resource representing a unit of work in a self-hosted environment.

Work items are queued when sessions are created or when long-dormant sessions
receive new messages. The environment worker polls for work to execute in a
self-hosted sandbox.

id: string

Work identifier (e.g., 'work\_...')

acknowledged\_at: string

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

created\_at: string

RFC 3339 timestamp when work was created



data: [BetaSessionWorkData](api/beta.md) { id, type } 

The actual work to be performed

id: string

Session identifier (e.g., 'session\_...')

type: "session"

Type of work data

environment\_id: string

Environment identifier this work belongs to (e.g., `env_...`)

latest\_heartbeat\_at: string

RFC 3339 timestamp of the most recent heartbeat

metadata: map[string]

User-provided metadata key-value pairs associated with this work item

started\_at: string

RFC 3339 timestamp when work execution started



state: "queued" or "starting" or "active" or 2 more

Current state of the work item

One of the following:

"queued"

"starting"

"active"

"stopping"

"stopped"

stop\_requested\_at: string

RFC 3339 timestamp when stop was requested

stopped\_at: string

RFC 3339 timestamp when work execution stopped

type: "work"

The type of object (always 'work')



BetaSelfHostedWorkHeartbeatResponse object { last\_heartbeat, lease\_extended, state, 2 more } 

Response after recording a heartbeat for a work item.

last\_heartbeat: string

RFC 3339 timestamp of the actual heartbeat from DB

lease\_extended: boolean

Whether the heartbeat succeeded in extending the lease



state: "queued" or "starting" or "active" or 2 more

Current state of the work item (active/stopping/stopped)

One of the following:

"queued"

"starting"

"active"

"stopping"

"stopped"

ttl\_seconds: number

Effective TTL applied to the lease

type: "work\_heartbeat"

The type of response



BetaSelfHostedWorkListResponse object { data, next\_page } 

Response when listing work items with cursor-based pagination.



data: array of [BetaSelfHostedWork](api/beta.md) { id, acknowledged\_at, created\_at, 9 more } 

List of work items

id: string

Work identifier (e.g., 'work\_...')

acknowledged\_at: string

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

created\_at: string

RFC 3339 timestamp when work was created



data: [BetaSessionWorkData](api/beta.md) { id, type } 

The actual work to be performed

id: string

Session identifier (e.g., 'session\_...')

type: "session"

Type of work data

environment\_id: string

Environment identifier this work belongs to (e.g., `env_...`)

latest\_heartbeat\_at: string

RFC 3339 timestamp of the most recent heartbeat

metadata: map[string]

User-provided metadata key-value pairs associated with this work item

started\_at: string

RFC 3339 timestamp when work execution started



state: "queued" or "starting" or "active" or 2 more

Current state of the work item

One of the following:

"queued"

"starting"

"active"

"stopping"

"stopped"

stop\_requested\_at: string

RFC 3339 timestamp when stop was requested

stopped\_at: string

RFC 3339 timestamp when work execution stopped

type: "work"

The type of object (always 'work')

next\_page: string

Opaque cursor for fetching the next page of results



BetaSelfHostedWorkQueueStats object { depth, oldest\_queued\_at, pending, 2 more } 

Statistics about the work queue for an environment.

Uses Redis Stream consumer group metrics for O(1) queries.

depth: number

Number of work items waiting to be picked up (lag from consumer group)

oldest\_queued\_at: string

RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

pending: number

Number of work items being processed (polled but not acknowledged)

type: "work\_queue\_stats"

The type of object

workers\_polling: number

Number of workers that have polled for work in the last 30 seconds. Requires worker\_id to be sent with poll requests.



BetaSelfHostedWorkStopRequest object { force } 

Request to stop a work item.

force: optional boolean

If true, immediately stop work without graceful shutdown



BetaSelfHostedWorkUpdateRequest object { metadata } 

Request to update work item metadata.

metadata: map[string]

Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.



BetaSessionWorkData object { id, type } 

Work data for session work items.

This resource type is used when work represents a session that needs to be executed
in a self-hosted environment.

id: string

Session identifier (e.g., 'session\_...')

type: "session"

Type of work data

---

*Copyright © Anthropic. All rights reserved.*
