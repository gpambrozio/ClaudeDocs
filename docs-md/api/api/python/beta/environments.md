# Environments

Copy page

SDK language

Python

# Environments

##### [Create Environment](api/beta/environments/create.md)

beta.environments.create(EnvironmentCreateParams\*\*kwargs)  -> [BetaEnvironment](api/beta.md)

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

beta.environments.list(EnvironmentListParams\*\*kwargs)  -> SyncPageCursor[[BetaEnvironment](api/beta.md)]

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

beta.environments.retrieve(strenvironment\_id, EnvironmentRetrieveParams\*\*kwargs)  -> [BetaEnvironment](api/beta.md)

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

beta.environments.update(strenvironment\_id, EnvironmentUpdateParams\*\*kwargs)  -> [BetaEnvironment](api/beta.md)

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

beta.environments.delete(strenvironment\_id, EnvironmentDeleteParams\*\*kwargs)  -> [BetaEnvironmentDeleteResponse](api/beta.md)

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

beta.environments.archive(strenvironment\_id, EnvironmentArchiveParams\*\*kwargs)  -> [BetaEnvironment](api/beta.md)

POST/v1/environments/{environment\_id}/archive

##### ModelsExpand Collapse



class BetaCloudConfig: …

`cloud` environment configuration.



networking: Networking

Network configuration policy.

One of the following:



class BetaUnrestrictedNetwork: …

Unrestricted network access.

type: Literal["unrestricted"]

Network policy type



class BetaLimitedNetwork: …

Limited network access.

allow\_mcp\_servers: bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: List[str]

Specifies domains the container can reach.

type: Literal["limited"]

Network policy type



packages: [BetaPackages](api/beta.md)

Package manager configuration.

apt: List[str]

Ubuntu/Debian packages to install

cargo: List[str]

Rust packages to install

gem: List[str]

Ruby packages to install

go: List[str]

Go packages to install

npm: List[str]

Node.js packages to install

pip: List[str]

Python packages to install

type: Optional[Literal["packages"]]

Package configuration type

type: Literal["cloud"]

Environment type



class BetaCloudConfigParams: …

Request params for `cloud` environment configuration.

Fields default to null; on update, omitted fields preserve the
existing value.

type: Literal["cloud"]

Environment type



networking: Optional[Networking]

Network configuration policy. Omit on update to preserve the existing value.

One of the following:



class BetaUnrestrictedNetwork: …

Unrestricted network access.

type: Literal["unrestricted"]

Network policy type



class BetaLimitedNetworkParams: …

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

type: Literal["limited"]

Network policy type

allow\_mcp\_servers: Optional[bool]

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allow\_package\_managers: Optional[bool]

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allowed\_hosts: Optional[List[str]]

Specifies domains the container can reach.



packages: Optional[BetaPackagesParams]

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

apt: Optional[List[str]]

Ubuntu/Debian packages to install

cargo: Optional[List[str]]

Rust packages to install

gem: Optional[List[str]]

Ruby packages to install

go: Optional[List[str]]

Go packages to install

npm: Optional[List[str]]

Node.js packages to install

pip: Optional[List[str]]

Python packages to install

type: Optional[Literal["packages"]]

Package configuration type



class BetaEnvironment: …

Unified Environment resource for both cloud and self-hosted environments.

id: str

Environment identifier (e.g., 'env\_...')

archived\_at: Optional[str]

RFC 3339 timestamp when environment was archived, or null if not archived



config: Config

Environment configuration (either Anthropic Cloud or self-hosted)

One of the following:



class BetaCloudConfig: …

`cloud` environment configuration.



networking: Networking

Network configuration policy.

One of the following:



class BetaUnrestrictedNetwork: …

Unrestricted network access.

type: Literal["unrestricted"]

Network policy type



class BetaLimitedNetwork: …

Limited network access.

allow\_mcp\_servers: bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: List[str]

Specifies domains the container can reach.

type: Literal["limited"]

Network policy type



packages: [BetaPackages](api/beta.md)

Package manager configuration.

apt: List[str]

Ubuntu/Debian packages to install

cargo: List[str]

Rust packages to install

gem: List[str]

Ruby packages to install

go: List[str]

Go packages to install

npm: List[str]

Node.js packages to install

pip: List[str]

Python packages to install

type: Optional[Literal["packages"]]

Package configuration type

type: Literal["cloud"]

Environment type



class BetaSelfHostedConfig: …

Configuration for self-hosted environments.

type: Literal["self\_hosted"]

Environment type

created\_at: str

RFC 3339 timestamp when environment was created

description: str

User-provided description for the environment

metadata: Dict[str, str]

User-provided metadata key-value pairs

name: str

Human-readable name for the environment

type: Literal["environment"]

The type of object (always 'environment')

updated\_at: str

RFC 3339 timestamp when environment was last updated



scope: Optional[Literal["organization", "account"]]

The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

One of the following:

"organization"

"account"



class BetaEnvironmentDeleteResponse: …

Response after deleting an environment.

id: str

Environment identifier

type: Literal["environment\_deleted"]

The type of response



class BetaLimitedNetwork: …

Limited network access.

allow\_mcp\_servers: bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: List[str]

Specifies domains the container can reach.

type: Literal["limited"]

Network policy type



class BetaLimitedNetworkParams: …

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

type: Literal["limited"]

Network policy type

allow\_mcp\_servers: Optional[bool]

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allow\_package\_managers: Optional[bool]

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allowed\_hosts: Optional[List[str]]

Specifies domains the container can reach.



class BetaPackages: …

Packages (and their versions) available in this environment.

apt: List[str]

Ubuntu/Debian packages to install

cargo: List[str]

Rust packages to install

gem: List[str]

Ruby packages to install

go: List[str]

Go packages to install

npm: List[str]

Node.js packages to install

pip: List[str]

Python packages to install

type: Optional[Literal["packages"]]

Package configuration type



class BetaPackagesParams: …

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

apt: Optional[List[str]]

Ubuntu/Debian packages to install

cargo: Optional[List[str]]

Rust packages to install

gem: Optional[List[str]]

Ruby packages to install

go: Optional[List[str]]

Go packages to install

npm: Optional[List[str]]

Node.js packages to install

pip: Optional[List[str]]

Python packages to install

type: Optional[Literal["packages"]]

Package configuration type



class BetaSelfHostedConfig: …

Configuration for self-hosted environments.

type: Literal["self\_hosted"]

Environment type



class BetaSelfHostedConfigParams: …

Request params for `self_hosted` environment configuration.

type: Literal["self\_hosted"]

Environment type



class BetaUnrestrictedNetwork: …

Unrestricted network access.

type: Literal["unrestricted"]

Network policy type

#### EnvironmentsWork

##### [Get Work Item](api/beta/environments/work/retrieve.md)

beta.environments.work.retrieve(strwork\_id, WorkRetrieveParams\*\*kwargs)  -> [BetaSelfHostedWork](api/beta.md)

GET/v1/environments/{environment\_id}/work/{work\_id}

##### [Poll for Work](api/beta/environments/work/poll.md)

beta.environments.work.poll(strenvironment\_id, WorkPollParams\*\*kwargs)  -> [BetaSelfHostedWork](api/beta.md)

GET/v1/environments/{environment\_id}/work/poll

##### [Acknowledge Work](api/beta/environments/work/ack.md)

beta.environments.work.ack(strwork\_id, WorkAckParams\*\*kwargs)  -> [BetaSelfHostedWork](api/beta.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/ack

##### [Record Heartbeat](api/beta/environments/work/heartbeat.md)

beta.environments.work.heartbeat(strwork\_id, WorkHeartbeatParams\*\*kwargs)  -> [BetaSelfHostedWorkHeartbeatResponse](api/beta.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/heartbeat

##### [Stop Work](api/beta/environments/work/stop.md)

beta.environments.work.stop(strwork\_id, WorkStopParams\*\*kwargs)  -> [BetaSelfHostedWork](api/beta.md)

POST/v1/environments/{environment\_id}/work/{work\_id}/stop

##### [List Work Items](api/beta/environments/work/list.md)

beta.environments.work.list(strenvironment\_id, WorkListParams\*\*kwargs)  -> SyncPageCursor[[BetaSelfHostedWork](api/beta.md)]

GET/v1/environments/{environment\_id}/work

##### [Update Work Item](api/beta/environments/work/update.md)

beta.environments.work.update(strwork\_id, WorkUpdateParams\*\*kwargs)  -> [BetaSelfHostedWork](api/beta.md)

POST/v1/environments/{environment\_id}/work/{work\_id}

##### [Get Queue Statistics](api/beta/environments/work/stats.md)

beta.environments.work.stats(strenvironment\_id, WorkStatsParams\*\*kwargs)  -> [BetaSelfHostedWorkQueueStats](api/beta.md)

GET/v1/environments/{environment\_id}/work/stats

##### ModelsExpand Collapse



class BetaSelfHostedWork: …

Work resource representing a unit of work in a self-hosted environment.

Work items are queued when sessions are created or when long-dormant sessions
receive new messages. The environment worker polls for work to execute in a
self-hosted sandbox.

id: str

Work identifier (e.g., 'work\_...')

acknowledged\_at: Optional[str]

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

created\_at: str

RFC 3339 timestamp when work was created



data: [BetaSessionWorkData](api/beta.md)

The actual work to be performed

id: str

Session identifier (e.g., 'session\_...')

type: Literal["session"]

Type of work data

environment\_id: str

Environment identifier this work belongs to (e.g., `env_...`)

latest\_heartbeat\_at: Optional[str]

RFC 3339 timestamp of the most recent heartbeat

metadata: Dict[str, str]

User-provided metadata key-value pairs associated with this work item

started\_at: Optional[str]

RFC 3339 timestamp when work execution started



state: Literal["queued", "starting", "active", 2 more]

Current state of the work item

One of the following:

"queued"

"starting"

"active"

"stopping"

"stopped"

stop\_requested\_at: Optional[str]

RFC 3339 timestamp when stop was requested

stopped\_at: Optional[str]

RFC 3339 timestamp when work execution stopped

type: Literal["work"]

The type of object (always 'work')



class BetaSelfHostedWorkHeartbeatResponse: …

Response after recording a heartbeat for a work item.

last\_heartbeat: str

RFC 3339 timestamp of the actual heartbeat from DB

lease\_extended: bool

Whether the heartbeat succeeded in extending the lease



state: Literal["queued", "starting", "active", 2 more]

Current state of the work item (active/stopping/stopped)

One of the following:

"queued"

"starting"

"active"

"stopping"

"stopped"

ttl\_seconds: int

Effective TTL applied to the lease

type: Literal["work\_heartbeat"]

The type of response



class BetaSelfHostedWorkListResponse: …

Response when listing work items with cursor-based pagination.



data: List[[BetaSelfHostedWork](api/beta.md)]

List of work items

id: str

Work identifier (e.g., 'work\_...')

acknowledged\_at: Optional[str]

RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

created\_at: str

RFC 3339 timestamp when work was created



data: [BetaSessionWorkData](api/beta.md)

The actual work to be performed

id: str

Session identifier (e.g., 'session\_...')

type: Literal["session"]

Type of work data

environment\_id: str

Environment identifier this work belongs to (e.g., `env_...`)

latest\_heartbeat\_at: Optional[str]

RFC 3339 timestamp of the most recent heartbeat

metadata: Dict[str, str]

User-provided metadata key-value pairs associated with this work item

started\_at: Optional[str]

RFC 3339 timestamp when work execution started



state: Literal["queued", "starting", "active", 2 more]

Current state of the work item

One of the following:

"queued"

"starting"

"active"

"stopping"

"stopped"

stop\_requested\_at: Optional[str]

RFC 3339 timestamp when stop was requested

stopped\_at: Optional[str]

RFC 3339 timestamp when work execution stopped

type: Literal["work"]

The type of object (always 'work')

next\_page: Optional[str]

Opaque cursor for fetching the next page of results



class BetaSelfHostedWorkQueueStats: …

Statistics about the work queue for an environment.

Uses Redis Stream consumer group metrics for O(1) queries.

depth: int

Number of work items waiting to be picked up (lag from consumer group)

oldest\_queued\_at: Optional[str]

RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

pending: int

Number of work items being processed (polled but not acknowledged)

type: Literal["work\_queue\_stats"]

The type of object

workers\_polling: Optional[int]

Number of workers that have polled for work in the last 30 seconds. Requires worker\_id to be sent with poll requests.



class BetaSelfHostedWorkStopRequest: …

Request to stop a work item.

force: Optional[bool]

If true, immediately stop work without graceful shutdown



class BetaSelfHostedWorkUpdateRequest: …

Request to update work item metadata.

metadata: Dict[str, Optional[str]]

Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.



class BetaSessionWorkData: …

Work data for session work items.

This resource type is used when work represents a session that needs to be executed
in a self-hosted environment.

id: str

Session identifier (e.g., 'session\_...')

type: Literal["session"]

Type of work data

---

*Copyright © Anthropic. All rights reserved.*
