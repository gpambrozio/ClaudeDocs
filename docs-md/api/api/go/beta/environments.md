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

One of the following:

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

Type BetaPackagesTypeOptional

Package configuration type

Type Cloud

Environment type

type BetaCloudConfigParamsResp struct{…}

Request params for `cloud` environment configuration.

Fields default to null; on update, omitted fields preserve the
existing value.

Type Cloud

Environment type

Networking BetaCloudConfigParamsNetworkingUnionRespOptional

Network configuration policy. Omit on update to preserve the existing value.

One of the following:

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

AllowMCPServers boolOptional

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

AllowPackageManagers boolOptional

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

AllowedHosts []stringOptional

Specifies domains the container can reach.

Packages [BetaPackagesParamsResp](api/beta.md)Optional

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

Apt []stringOptional

Ubuntu/Debian packages to install

Cargo []stringOptional

Rust packages to install

Gem []stringOptional

Ruby packages to install

Go []stringOptional

Go packages to install

Npm []stringOptional

Node.js packages to install

Pip []stringOptional

Python packages to install

Type BetaPackagesParamsTypeOptional

Package configuration type

type BetaEnvironment struct{…}

Unified Environment resource for both cloud and self-hosted environments.

ID string

Environment identifier (e.g., 'env\_...')

ArchivedAt string

RFC 3339 timestamp when environment was archived, or null if not archived

Config BetaEnvironmentConfigUnion

Environment configuration (either Anthropic Cloud or self-hosted)

One of the following:

type BetaCloudConfig struct{…}

`cloud` environment configuration.

Networking BetaCloudConfigNetworkingUnion

Network configuration policy.

One of the following:

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

Type BetaPackagesTypeOptional

Package configuration type

Type Cloud

Environment type

type BetaSelfHostedConfig struct{…}

Configuration for self-hosted environments.

Type SelfHosted

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

Scope BetaEnvironmentScopeOptional

The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

One of the following:

const BetaEnvironmentScopeOrganization BetaEnvironmentScope = "organization"

const BetaEnvironmentScopeAccount BetaEnvironmentScope = "account"

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

AllowMCPServers boolOptional

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

AllowPackageManagers boolOptional

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

AllowedHosts []stringOptional

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

Type BetaPackagesTypeOptional

Package configuration type

type BetaPackagesParamsResp struct{…}

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

Apt []stringOptional

Ubuntu/Debian packages to install

Cargo []stringOptional

Rust packages to install

Gem []stringOptional

Ruby packages to install

Go []stringOptional

Go packages to install

Npm []stringOptional

Node.js packages to install

Pip []stringOptional

Python packages to install

Type BetaPackagesParamsTypeOptional

Package configuration type

type BetaSelfHostedConfig struct{…}

Configuration for self-hosted environments.

Type SelfHosted

Environment type

type BetaSelfHostedConfigParamsResp struct{…}

Request params for `self_hosted` environment configuration.

Type SelfHosted

Environment type

type BetaUnrestrictedNetwork struct{…}

Unrestricted network access.

Type Unrestricted

Network policy type

#### EnvironmentsWork

##### [Get Work Item](api/beta/environments/work/retrieve.md)

client.Beta.Environments.Work.Get(ctx, workID, params) (\*[BetaSelfHostedWork](api/beta.md), error)

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

client.Beta.Environments.Work.Poll(ctx, environmentID, params) (\*[BetaSelfHostedWork](api/beta.md), error)

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

client.Beta.Environments.Work.Ack(ctx, workID, params) (\*[BetaSelfHostedWork](api/beta.md), error)

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

client.Beta.Environments.Work.Heartbeat(ctx, workID, params) (\*[BetaSelfHostedWorkHeartbeatResponse](api/beta.md), error)

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

client.Beta.Environments.Work.Stop(ctx, workID, params) (\*[BetaSelfHostedWork](api/beta.md), error)

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

client.Beta.Environments.Work.List(ctx, environmentID, params) (\*PageCursor[[BetaSelfHostedWork](api/beta.md)], error)

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

client.Beta.Environments.Work.Update(ctx, workID, params) (\*[BetaSelfHostedWork](api/beta.md), error)

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

client.Beta.Environments.Work.Stats(ctx, environmentID, query) (\*[BetaSelfHostedWorkQueueStats](api/beta.md), error)

GET/v1/environments/{environment\_id}/work/stats

##### ModelsExpand Collapse

type BetaSelfHostedWork struct{…}

Work resource representing a unit of work in a self-hosted environment.

Work items are queued when sessions are created or when long-dormant sessions
receive new messages. The environment worker polls for work to execute in a
self-hosted sandbox.

ID string

Work identifier (e.g., 'work\_...')

AcknowledgedAt string

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

CreatedAt string

RFC 3339 timestamp when work was created

Data [BetaSessionWorkData](api/beta.md)

The actual work to be performed

ID string

Session identifier (e.g., 'session\_...')

Type Session

Type of work data

EnvironmentID string

Environment identifier this work belongs to (e.g., `env_...`)

LatestHeartbeatAt string

RFC 3339 timestamp of the most recent heartbeat

Metadata map[string, string]

User-provided metadata key-value pairs associated with this work item

StartedAt string

RFC 3339 timestamp when work execution started

State BetaSelfHostedWorkState

Current state of the work item

One of the following:

const BetaSelfHostedWorkStateQueued BetaSelfHostedWorkState = "queued"

const BetaSelfHostedWorkStateStarting BetaSelfHostedWorkState = "starting"

const BetaSelfHostedWorkStateActive BetaSelfHostedWorkState = "active"

const BetaSelfHostedWorkStateStopping BetaSelfHostedWorkState = "stopping"

const BetaSelfHostedWorkStateStopped BetaSelfHostedWorkState = "stopped"

StopRequestedAt string

RFC 3339 timestamp when stop was requested

StoppedAt string

RFC 3339 timestamp when work execution stopped

Type Work

The type of object (always 'work')

type BetaSelfHostedWorkHeartbeatResponse struct{…}

Response after recording a heartbeat for a work item.

LastHeartbeat string

RFC 3339 timestamp of the actual heartbeat from DB

LeaseExtended bool

Whether the heartbeat succeeded in extending the lease

State BetaSelfHostedWorkHeartbeatResponseState

Current state of the work item (active/stopping/stopped)

One of the following:

const BetaSelfHostedWorkHeartbeatResponseStateQueued BetaSelfHostedWorkHeartbeatResponseState = "queued"

const BetaSelfHostedWorkHeartbeatResponseStateStarting BetaSelfHostedWorkHeartbeatResponseState = "starting"

const BetaSelfHostedWorkHeartbeatResponseStateActive BetaSelfHostedWorkHeartbeatResponseState = "active"

const BetaSelfHostedWorkHeartbeatResponseStateStopping BetaSelfHostedWorkHeartbeatResponseState = "stopping"

const BetaSelfHostedWorkHeartbeatResponseStateStopped BetaSelfHostedWorkHeartbeatResponseState = "stopped"

TTLSeconds int64

Effective TTL applied to the lease

Type WorkHeartbeat

The type of response

type BetaSelfHostedWorkListResponse struct{…}

Response when listing work items with cursor-based pagination.

Data [][BetaSelfHostedWork](api/beta.md)

List of work items

ID string

Work identifier (e.g., 'work\_...')

AcknowledgedAt string

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

CreatedAt string

RFC 3339 timestamp when work was created

Data [BetaSessionWorkData](api/beta.md)

The actual work to be performed

ID string

Session identifier (e.g., 'session\_...')

Type Session

Type of work data

EnvironmentID string

Environment identifier this work belongs to (e.g., `env_...`)

LatestHeartbeatAt string

RFC 3339 timestamp of the most recent heartbeat

Metadata map[string, string]

User-provided metadata key-value pairs associated with this work item

StartedAt string

RFC 3339 timestamp when work execution started

State BetaSelfHostedWorkState

Current state of the work item

One of the following:

const BetaSelfHostedWorkStateQueued BetaSelfHostedWorkState = "queued"

const BetaSelfHostedWorkStateStarting BetaSelfHostedWorkState = "starting"

const BetaSelfHostedWorkStateActive BetaSelfHostedWorkState = "active"

const BetaSelfHostedWorkStateStopping BetaSelfHostedWorkState = "stopping"

const BetaSelfHostedWorkStateStopped BetaSelfHostedWorkState = "stopped"

StopRequestedAt string

RFC 3339 timestamp when stop was requested

StoppedAt string

RFC 3339 timestamp when work execution stopped

Type Work

The type of object (always 'work')

NextPage string

Opaque cursor for fetching the next page of results

type BetaSelfHostedWorkQueueStats struct{…}

Statistics about the work queue for an environment.

Uses Redis Stream consumer group metrics for O(1) queries.

Depth int64

Number of work items waiting to be picked up (lag from consumer group)

OldestQueuedAt string

RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

Pending int64

Number of work items being processed (polled but not acknowledged)

Type WorkQueueStats

The type of object

WorkersPolling int64

Number of workers that have polled for work in the last 30 seconds. Requires worker\_id to be sent with poll requests.

type BetaSelfHostedWorkStopRequest struct{…}

Request to stop a work item.

Force boolOptional

If true, immediately stop work without graceful shutdown

type BetaSelfHostedWorkUpdateRequest struct{…}

Request to update work item metadata.

Metadata map[string, string]

Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

type BetaSessionWorkData struct{…}

Work data for session work items.

This resource type is used when work represents a session that needs to be executed
in a self-hosted environment.

ID string

Session identifier (e.g., 'session\_...')

Type Session

Type of work data

---

*Copyright © Anthropic. All rights reserved.*
