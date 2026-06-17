# Environments

Copy page



C#

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



class BetaCloudConfig:

`cloud` environment configuration.



required Networking Networking

Network configuration policy.

One of the following:



class BetaUnrestrictedNetwork:

Unrestricted network access.

JsonElement Type "unrestricted"constant

Network policy type



class BetaLimitedNetwork:

Limited network access.

required Boolean AllowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

required Boolean AllowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

required IReadOnlyList<string> AllowedHosts

Specifies domains the container can reach.

JsonElement Type "limited"constant

Network policy type



required [BetaPackages](api/beta.md) Packages

Package manager configuration.

required IReadOnlyList<string> Apt

Ubuntu/Debian packages to install

required IReadOnlyList<string> Cargo

Rust packages to install

required IReadOnlyList<string> Gem

Ruby packages to install

required IReadOnlyList<string> Go

Go packages to install

required IReadOnlyList<string> Npm

Node.js packages to install

required IReadOnlyList<string> Pip

Python packages to install

Type Type

Package configuration type

JsonElement Type "cloud"constant

Environment type



class BetaCloudConfigParams:

Request params for `cloud` environment configuration.

Fields default to null; on update, omitted fields preserve the
existing value.

JsonElement Type "cloud"constant

Environment type



Networking? Networking

Network configuration policy. Omit on update to preserve the existing value.

One of the following:



class BetaUnrestrictedNetwork:

Unrestricted network access.

JsonElement Type "unrestricted"constant

Network policy type



class BetaLimitedNetworkParams:

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

JsonElement Type "limited"constant

Network policy type

Boolean? AllowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

Boolean? AllowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

IReadOnlyList<string>? AllowedHosts

Specifies domains the container can reach.



[BetaPackagesParams](api/beta.md)? Packages

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

IReadOnlyList<string>? Apt

Ubuntu/Debian packages to install

IReadOnlyList<string>? Cargo

Rust packages to install

IReadOnlyList<string>? Gem

Ruby packages to install

IReadOnlyList<string>? Go

Go packages to install

IReadOnlyList<string>? Npm

Node.js packages to install

IReadOnlyList<string>? Pip

Python packages to install

Type Type

Package configuration type



class BetaEnvironment:

Unified Environment resource for both cloud and self-hosted environments.

required string ID

Environment identifier (e.g., 'env\_...')

required string? ArchivedAt

RFC 3339 timestamp when environment was archived, or null if not archived



required Config Config

Environment configuration (either Anthropic Cloud or self-hosted)

One of the following:



class BetaCloudConfig:

`cloud` environment configuration.



required Networking Networking

Network configuration policy.

One of the following:



class BetaUnrestrictedNetwork:

Unrestricted network access.

JsonElement Type "unrestricted"constant

Network policy type



class BetaLimitedNetwork:

Limited network access.

required Boolean AllowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

required Boolean AllowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

required IReadOnlyList<string> AllowedHosts

Specifies domains the container can reach.

JsonElement Type "limited"constant

Network policy type



required [BetaPackages](api/beta.md) Packages

Package manager configuration.

required IReadOnlyList<string> Apt

Ubuntu/Debian packages to install

required IReadOnlyList<string> Cargo

Rust packages to install

required IReadOnlyList<string> Gem

Ruby packages to install

required IReadOnlyList<string> Go

Go packages to install

required IReadOnlyList<string> Npm

Node.js packages to install

required IReadOnlyList<string> Pip

Python packages to install

Type Type

Package configuration type

JsonElement Type "cloud"constant

Environment type



class BetaSelfHostedConfig:

Configuration for self-hosted environments.

JsonElement Type "self\_hosted"constant

Environment type

required string CreatedAt

RFC 3339 timestamp when environment was created

required string Description

User-provided description for the environment

required IReadOnlyDictionary<string, string> Metadata

User-provided metadata key-value pairs

required string Name

Human-readable name for the environment

JsonElement Type "environment"constant

The type of object (always 'environment')

required string UpdatedAt

RFC 3339 timestamp when environment was last updated



Scope Scope

The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

One of the following:

"organization"Organization

"account"Account



class BetaEnvironmentDeleteResponse:

Response after deleting an environment.

required string ID

Environment identifier

JsonElement Type "environment\_deleted"constant

The type of response



class BetaLimitedNetwork:

Limited network access.

required Boolean AllowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

required Boolean AllowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

required IReadOnlyList<string> AllowedHosts

Specifies domains the container can reach.

JsonElement Type "limited"constant

Network policy type



class BetaLimitedNetworkParams:

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

JsonElement Type "limited"constant

Network policy type

Boolean? AllowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

Boolean? AllowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

IReadOnlyList<string>? AllowedHosts

Specifies domains the container can reach.



class BetaPackages:

Packages (and their versions) available in this environment.

required IReadOnlyList<string> Apt

Ubuntu/Debian packages to install

required IReadOnlyList<string> Cargo

Rust packages to install

required IReadOnlyList<string> Gem

Ruby packages to install

required IReadOnlyList<string> Go

Go packages to install

required IReadOnlyList<string> Npm

Node.js packages to install

required IReadOnlyList<string> Pip

Python packages to install

Type Type

Package configuration type



class BetaPackagesParams:

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

IReadOnlyList<string>? Apt

Ubuntu/Debian packages to install

IReadOnlyList<string>? Cargo

Rust packages to install

IReadOnlyList<string>? Gem

Ruby packages to install

IReadOnlyList<string>? Go

Go packages to install

IReadOnlyList<string>? Npm

Node.js packages to install

IReadOnlyList<string>? Pip

Python packages to install

Type Type

Package configuration type



class BetaSelfHostedConfig:

Configuration for self-hosted environments.

JsonElement Type "self\_hosted"constant

Environment type



class BetaSelfHostedConfigParams:

Request params for `self_hosted` environment configuration.

JsonElement Type "self\_hosted"constant

Environment type



class BetaUnrestrictedNetwork:

Unrestricted network access.

JsonElement Type "unrestricted"constant

Network policy type

#### EnvironmentsWork

##### [Get Work Item](api/beta/environments/work/retrieve.md)

[BetaSelfHostedWork](api/beta.md) Beta.Environments.Work.Retrieve(WorkRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

[BetaSelfHostedWork](api/beta.md)? Beta.Environments.Work.Poll(WorkPollParamsparameters, CancellationTokencancellationToken = default)

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

[BetaSelfHostedWork](api/beta.md) Beta.Environments.Work.Ack(WorkAckParamsparameters, CancellationTokencancellationToken = default)

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

[BetaSelfHostedWorkHeartbeatResponse](api/beta.md) Beta.Environments.Work.Heartbeat(WorkHeartbeatParamsparameters, CancellationTokencancellationToken = default)

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

[BetaSelfHostedWork](api/beta.md) Beta.Environments.Work.Stop(WorkStopParamsparameters, CancellationTokencancellationToken = default)

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

[BetaSelfHostedWorkListResponse](api/beta.md) Beta.Environments.Work.List(WorkListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

[BetaSelfHostedWork](api/beta.md) Beta.Environments.Work.Update(WorkUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

[BetaSelfHostedWorkQueueStats](api/beta.md) Beta.Environments.Work.Stats(WorkStatsParamsparameters, CancellationTokencancellationToken = default)

GET/v1/environments/{environment\_id}/work/stats

##### ModelsExpand Collapse



class BetaSelfHostedWork:

Work resource representing a unit of work in a self-hosted environment.

Work items are queued when sessions are created or when long-dormant sessions
receive new messages. The environment worker polls for work to execute in a
self-hosted sandbox.

required string ID

Work identifier (e.g., 'work\_...')

required string? AcknowledgedAt

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

required string CreatedAt

RFC 3339 timestamp when work was created



required [BetaSessionWorkData](api/beta.md) Data

The actual work to be performed

required string ID

Session identifier (e.g., 'session\_...')

JsonElement Type "session"constant

Type of work data

required string EnvironmentID

Environment identifier this work belongs to (e.g., `env_...`)

required string? LatestHeartbeatAt

RFC 3339 timestamp of the most recent heartbeat

required IReadOnlyDictionary<string, string> Metadata

User-provided metadata key-value pairs associated with this work item

required string? StartedAt

RFC 3339 timestamp when work execution started



required State State

Current state of the work item

One of the following:

"queued"Queued

"starting"Starting

"active"Active

"stopping"Stopping

"stopped"Stopped

required string? StopRequestedAt

RFC 3339 timestamp when stop was requested

required string? StoppedAt

RFC 3339 timestamp when work execution stopped

JsonElement Type "work"constant

The type of object (always 'work')



class BetaSelfHostedWorkHeartbeatResponse:

Response after recording a heartbeat for a work item.

required string LastHeartbeat

RFC 3339 timestamp of the actual heartbeat from DB

required Boolean LeaseExtended

Whether the heartbeat succeeded in extending the lease



required State State

Current state of the work item (active/stopping/stopped)

One of the following:

"queued"Queued

"starting"Starting

"active"Active

"stopping"Stopping

"stopped"Stopped

required Long TtlSeconds

Effective TTL applied to the lease

JsonElement Type "work\_heartbeat"constant

The type of response



class BetaSelfHostedWorkListResponse:

Response when listing work items with cursor-based pagination.



required IReadOnlyList<[BetaSelfHostedWork](api/beta.md)> Data

List of work items

required string ID

Work identifier (e.g., 'work\_...')

required string? AcknowledgedAt

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

required string CreatedAt

RFC 3339 timestamp when work was created



required [BetaSessionWorkData](api/beta.md) Data

The actual work to be performed

required string ID

Session identifier (e.g., 'session\_...')

JsonElement Type "session"constant

Type of work data

required string EnvironmentID

Environment identifier this work belongs to (e.g., `env_...`)

required string? LatestHeartbeatAt

RFC 3339 timestamp of the most recent heartbeat

required IReadOnlyDictionary<string, string> Metadata

User-provided metadata key-value pairs associated with this work item

required string? StartedAt

RFC 3339 timestamp when work execution started



required State State

Current state of the work item

One of the following:

"queued"Queued

"starting"Starting

"active"Active

"stopping"Stopping

"stopped"Stopped

required string? StopRequestedAt

RFC 3339 timestamp when stop was requested

required string? StoppedAt

RFC 3339 timestamp when work execution stopped

JsonElement Type "work"constant

The type of object (always 'work')

required string? NextPage

Opaque cursor for fetching the next page of results



class BetaSelfHostedWorkQueueStats:

Statistics about the work queue for an environment.

Uses Redis Stream consumer group metrics for O(1) queries.

required Long Depth

Number of work items waiting to be picked up (lag from consumer group)

required string? OldestQueuedAt

RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

required Long Pending

Number of work items being processed (polled but not acknowledged)

JsonElement Type "work\_queue\_stats"constant

The type of object

required Long? WorkersPolling

Number of workers that have polled for work in the last 30 seconds. Requires worker\_id to be sent with poll requests.



class BetaSelfHostedWorkStopRequest:

Request to stop a work item.

Boolean Force

If true, immediately stop work without graceful shutdown



class BetaSelfHostedWorkUpdateRequest:

Request to update work item metadata.

required IReadOnlyDictionary<string, string> Metadata

Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.



class BetaSessionWorkData:

Work data for session work items.

This resource type is used when work represents a session that needs to be executed
in a self-hosted environment.

required string ID

Session identifier (e.g., 'session\_...')

JsonElement Type "session"constant

Type of work data

---

*Copyright © Anthropic. All rights reserved.*
