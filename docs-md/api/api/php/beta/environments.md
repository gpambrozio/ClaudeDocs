# Environments

Copy page

PHP

# Environments

##### [Create Environment](api/beta/environments/create.md)

$client->beta->environments->create(string name, ?[Config](api/beta/environments/create.md) config, ?string description, ?array<string,string> metadata, ?[Scope](api/beta/environments/create.md) scope, ?list<AnthropicBeta> betas): [BetaEnvironment](api/beta.md)

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

$client->beta->environments->list(?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[BetaEnvironment](api/beta.md)>

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

$client->beta->environments->retrieve(string environmentID, ?list<AnthropicBeta> betas): [BetaEnvironment](api/beta.md)

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

$client->beta->environments->update(string environmentID, ?[Config](api/beta/environments/update.md) config, ?string description, ?array<string,string> metadata, ?string name, ?[Scope](api/beta/environments/update.md) scope, ?list<AnthropicBeta> betas): [BetaEnvironment](api/beta.md)

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

$client->beta->environments->delete(string environmentID, ?list<AnthropicBeta> betas): [BetaEnvironmentDeleteResponse](api/beta.md)

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

$client->beta->environments->archive(string environmentID, ?list<AnthropicBeta> betas): [BetaEnvironment](api/beta.md)

POST/v1/environments/{environment\_id}/archive

##### ModelsExpand Collapse

[BetaCloudConfig](api/beta.md)

Networking networking

Network configuration policy.

[BetaPackages](api/beta.md) packages

Package manager configuration.

"cloud" type

Environment type

[BetaCloudConfigParams](api/beta.md)

"cloud" type

Environment type

?Networking networking

Network configuration policy. Omit on update to preserve the existing value.

?[BetaPackagesParams](api/beta.md) packages

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

[BetaEnvironment](api/beta.md)

string id

Environment identifier (e.g., 'env\_...')

?string archivedAt

RFC 3339 timestamp when environment was archived, or null if not archived

Config config

Environment configuration (either Anthropic Cloud or self-hosted)

string createdAt

RFC 3339 timestamp when environment was created

string description

User-provided description for the environment

array<string,string> metadata

User-provided metadata key-value pairs

string name

Human-readable name for the environment

"environment" type

The type of object (always 'environment')

string updatedAt

RFC 3339 timestamp when environment was last updated

?Scope scope

The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

[BetaEnvironmentDeleteResponse](api/beta.md)

string id

Environment identifier

"environment\_deleted" type

The type of response

[BetaLimitedNetwork](api/beta.md)

bool allowMCPServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

bool allowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

list<string> allowedHosts

Specifies domains the container can reach.

"limited" type

Network policy type

[BetaLimitedNetworkParams](api/beta.md)

"limited" type

Network policy type

?bool allowMCPServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

?bool allowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

?list<string> allowedHosts

Specifies domains the container can reach.

[BetaPackages](api/beta.md)

list<string> apt

Ubuntu/Debian packages to install

list<string> cargo

Rust packages to install

list<string> gem

Ruby packages to install

list<string> go

Go packages to install

list<string> npm

Node.js packages to install

list<string> pip

Python packages to install

?Type type

Package configuration type

[BetaPackagesParams](api/beta.md)

?list<string> apt

Ubuntu/Debian packages to install

?list<string> cargo

Rust packages to install

?list<string> gem

Ruby packages to install

?list<string> go

Go packages to install

?list<string> npm

Node.js packages to install

?list<string> pip

Python packages to install

?Type type

Package configuration type

[BetaSelfHostedConfig](api/beta.md)

"self\_hosted" type

Environment type

[BetaSelfHostedConfigParams](api/beta.md)

"self\_hosted" type

Environment type

[BetaUnrestrictedNetwork](api/beta.md)

"unrestricted" type

Network policy type

#### EnvironmentsWork

##### [Get Work Item](api/beta/environments/work/retrieve.md)

$client->beta->environments->work->retrieve(string workID, string environmentID, ?list<AnthropicBeta> betas): [SelfHostedWork](api/beta.md)

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

$client->beta->environments->work->poll(string environmentID, ?int blockMs, ?int reclaimOlderThanMs, ?list<AnthropicBeta> betas, ?string anthropicWorkerID): [SelfHostedWork](api/beta.md)

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

$client->beta->environments->work->ack(string workID, string environmentID, ?list<AnthropicBeta> betas): [SelfHostedWork](api/beta.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

$client->beta->environments->work->heartbeat(string workID, string environmentID, ?int desiredTTLSeconds, ?string expectedLastHeartbeat, ?list<AnthropicBeta> betas): [SelfHostedWorkHeartbeatResponse](api/beta.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

$client->beta->environments->work->stop(string workID, string environmentID, ?bool force, ?list<AnthropicBeta> betas): [SelfHostedWork](api/beta.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

$client->beta->environments->work->list(string environmentID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[SelfHostedWork](api/beta.md)>

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

$client->beta->environments->work->update(string workID, string environmentID, array<string,string> metadata, ?list<AnthropicBeta> betas): [SelfHostedWork](api/beta.md)

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

$client->beta->environments->work->stats(string environmentID, ?list<AnthropicBeta> betas): [SelfHostedWorkQueueStats](api/beta.md)

GET/v1/environments/{environment\_id}/work/stats

##### ModelsExpand Collapse

[SelfHostedWork](api/beta.md)

string id

Work identifier (e.g., 'work\_...')

?string acknowledgedAt

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

string createdAt

RFC 3339 timestamp when work was created

[SessionWorkData](api/beta.md) data

The actual work to be performed

string environmentID

Environment identifier this work belongs to (e.g., `env_...`)

?string latestHeartbeatAt

RFC 3339 timestamp of the most recent heartbeat

array<string,string> metadata

User-provided metadata key-value pairs associated with this work item

?string startedAt

RFC 3339 timestamp when work execution started

State state

Current state of the work item

?string stopRequestedAt

RFC 3339 timestamp when stop was requested

?string stoppedAt

RFC 3339 timestamp when work execution stopped

"work" type

The type of object (always 'work')

[SelfHostedWorkHeartbeatResponse](api/beta.md)

string lastHeartbeat

RFC 3339 timestamp of the actual heartbeat from DB

bool leaseExtended

Whether the heartbeat succeeded in extending the lease

State state

Current state of the work item (active/stopping/stopped)

int ttlSeconds

Effective TTL applied to the lease

"work\_heartbeat" type

The type of response

[SelfHostedWorkListResponse](api/beta.md)

list<[SelfHostedWork](api/beta.md)> data

List of work items

?string nextPage

Opaque cursor for fetching the next page of results

[SelfHostedWorkQueueStats](api/beta.md)

int depth

Number of work items waiting to be picked up (lag from consumer group)

?string oldestQueuedAt

RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

int pending

Number of work items being processed (polled but not acknowledged)

"work\_queue\_stats" type

The type of object

?int workersPolling

Number of workers that have polled for work in the last 30 seconds. Requires worker\_id to be sent with poll requests.

[SelfHostedWorkStopRequest](api/beta.md)

?bool force

If true, immediately stop work without graceful shutdown

[SelfHostedWorkUpdateRequest](api/beta.md)

array<string,string> metadata

Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

[SessionWorkData](api/beta.md)

string id

Session identifier (e.g., 'session\_...')

"session" type

Type of work data

---

*Copyright © Anthropic. All rights reserved.*
