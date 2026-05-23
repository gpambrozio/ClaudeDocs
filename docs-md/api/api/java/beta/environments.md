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

One of the following:

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

One of the following:

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

Config config

Environment configuration (either Anthropic Cloud or self-hosted)

One of the following:

class BetaCloudConfig:

`cloud` environment configuration.

Networking networking

Network configuration policy.

One of the following:

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

class BetaSelfHostedConfig:

Configuration for self-hosted environments.

JsonValue; type "self\_hosted"constant"self\_hosted"constant

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

Optional<Scope> scope

The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

One of the following:

ORGANIZATION("organization")

ACCOUNT("account")

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

class BetaSelfHostedConfig:

Configuration for self-hosted environments.

JsonValue; type "self\_hosted"constant"self\_hosted"constant

Environment type

class BetaSelfHostedConfigParams:

Request params for `self_hosted` environment configuration.

JsonValue; type "self\_hosted"constant"self\_hosted"constant

Environment type

class BetaUnrestrictedNetwork:

Unrestricted network access.

JsonValue; type "unrestricted"constant"unrestricted"constant

Network policy type

#### EnvironmentsWork

##### [Get Work Item](api/beta/environments/work/retrieve.md)

[BetaSelfHostedWork](api/beta.md) beta().environments().work().retrieve(WorkRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

[BetaSelfHostedWork](api/beta.md) beta().environments().work().poll(WorkPollParamsparams = WorkPollParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

[BetaSelfHostedWork](api/beta.md) beta().environments().work().ack(WorkAckParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

[BetaSelfHostedWorkHeartbeatResponse](api/beta.md) beta().environments().work().heartbeat(WorkHeartbeatParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

[BetaSelfHostedWork](api/beta.md) beta().environments().work().stop(WorkStopParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

WorkListPage beta().environments().work().list(WorkListParamsparams = WorkListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

[BetaSelfHostedWork](api/beta.md) beta().environments().work().update(WorkUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

[BetaSelfHostedWorkQueueStats](api/beta.md) beta().environments().work().stats(WorkStatsParamsparams = WorkStatsParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/environments/{environment\_id}/work/stats

##### ModelsExpand Collapse

class BetaSelfHostedWork:

Work resource representing a unit of work in a self-hosted environment.

Work items are queued when sessions are created or when long-dormant sessions
receive new messages. The environment worker polls for work to execute in a
self-hosted sandbox.

String id

Work identifier (e.g., 'work\_...')

Optional<String> acknowledgedAt

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

String createdAt

RFC 3339 timestamp when work was created

[BetaSessionWorkData](api/beta.md) data

The actual work to be performed

String id

Session identifier (e.g., 'session\_...')

JsonValue; type "session"constant"session"constant

Type of work data

String environmentId

Environment identifier this work belongs to (e.g., `env_...`)

Optional<String> latestHeartbeatAt

RFC 3339 timestamp of the most recent heartbeat

Metadata metadata

User-provided metadata key-value pairs associated with this work item

Optional<String> startedAt

RFC 3339 timestamp when work execution started

State state

Current state of the work item

One of the following:

QUEUED("queued")

STARTING("starting")

ACTIVE("active")

STOPPING("stopping")

STOPPED("stopped")

Optional<String> stopRequestedAt

RFC 3339 timestamp when stop was requested

Optional<String> stoppedAt

RFC 3339 timestamp when work execution stopped

JsonValue; type "work"constant"work"constant

The type of object (always 'work')

class BetaSelfHostedWorkHeartbeatResponse:

Response after recording a heartbeat for a work item.

String lastHeartbeat

RFC 3339 timestamp of the actual heartbeat from DB

boolean leaseExtended

Whether the heartbeat succeeded in extending the lease

State state

Current state of the work item (active/stopping/stopped)

One of the following:

QUEUED("queued")

STARTING("starting")

ACTIVE("active")

STOPPING("stopping")

STOPPED("stopped")

long ttlSeconds

Effective TTL applied to the lease

JsonValue; type "work\_heartbeat"constant"work\_heartbeat"constant

The type of response

class BetaSelfHostedWorkListResponse:

Response when listing work items with cursor-based pagination.

List<[BetaSelfHostedWork](api/beta.md)> data

List of work items

String id

Work identifier (e.g., 'work\_...')

Optional<String> acknowledgedAt

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

String createdAt

RFC 3339 timestamp when work was created

[BetaSessionWorkData](api/beta.md) data

The actual work to be performed

String id

Session identifier (e.g., 'session\_...')

JsonValue; type "session"constant"session"constant

Type of work data

String environmentId

Environment identifier this work belongs to (e.g., `env_...`)

Optional<String> latestHeartbeatAt

RFC 3339 timestamp of the most recent heartbeat

Metadata metadata

User-provided metadata key-value pairs associated with this work item

Optional<String> startedAt

RFC 3339 timestamp when work execution started

State state

Current state of the work item

One of the following:

QUEUED("queued")

STARTING("starting")

ACTIVE("active")

STOPPING("stopping")

STOPPED("stopped")

Optional<String> stopRequestedAt

RFC 3339 timestamp when stop was requested

Optional<String> stoppedAt

RFC 3339 timestamp when work execution stopped

JsonValue; type "work"constant"work"constant

The type of object (always 'work')

Optional<String> nextPage

Opaque cursor for fetching the next page of results

class BetaSelfHostedWorkQueueStats:

Statistics about the work queue for an environment.

Uses Redis Stream consumer group metrics for O(1) queries.

long depth

Number of work items waiting to be picked up (lag from consumer group)

Optional<String> oldestQueuedAt

RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

long pending

Number of work items being processed (polled but not acknowledged)

JsonValue; type "work\_queue\_stats"constant"work\_queue\_stats"constant

The type of object

Optional<Long> workersPolling

Number of workers that have polled for work in the last 30 seconds. Requires worker\_id to be sent with poll requests.

class BetaSelfHostedWorkStopRequest:

Request to stop a work item.

Optional<Boolean> force

If true, immediately stop work without graceful shutdown

class BetaSelfHostedWorkUpdateRequest:

Request to update work item metadata.

Metadata metadata

Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

class BetaSessionWorkData:

Work data for session work items.

This resource type is used when work represents a session that needs to be executed
in a self-hosted environment.

String id

Session identifier (e.g., 'session\_...')

JsonValue; type "session"constant"session"constant

Type of work data

---

*Copyright © Anthropic. All rights reserved.*
