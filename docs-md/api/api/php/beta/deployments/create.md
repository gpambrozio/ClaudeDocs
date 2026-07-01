# Create Deployment

Copy page



PHP

# Create Deployment

$client->beta->deployments->create([Agent](api/beta/deployments/create.md) agent, string environmentID, list<[BetaManagedAgentsDeploymentInitialEventParams](api/beta/deployments.md)> initialEvents, string name, ?string description, ?array<string,string> metadata, ?list<Resource> resources, ?[BetaManagedAgentsScheduleParams](api/beta/deployments.md) schedule, ?list<string> vaultIDs, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeployment](api/beta/deployments.md)

POST/v1/deployments

Create Deployment

##### ParametersExpand Collapse

agent: [Agent](api/beta/deployments/create.md)

Agent to deploy. Accepts the `agent` ID string, which pins the latest version, or an `agent` object with both id and version specified. The agent must exist and not be archived.

environmentID: string

ID of the `environment` defining the container configuration for sessions created from this deployment.

initialEvents: list<[BetaManagedAgentsDeploymentInitialEventParams](api/beta/deployments.md)>

Events to send to each session immediately after creation. At least 1, maximum 50.

name: string

Human-readable name for the deployment.

description?:optional string

Description of what the deployment does.

metadata?:optional array<string,string>

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

resources?:optional list<Resource>

Resources (e.g. repositories, files) to mount into each session's container. Maximum 500.

schedule?:optional [BetaManagedAgentsScheduleParams](api/beta/deployments.md)

5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

vaultIDs?:optional list<string>

Vault IDs for stored credentials the agent can use during sessions created from this deployment. Maximum 50.

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



[BetaManagedAgentsDeployment](api/beta/deployments.md)

string id

Unique identifier for this deployment.

[BetaManagedAgentsAgentReference](api/beta/agents.md) agent

A resolved agent reference with a concrete version.

?\Datetime archivedAt

A timestamp in RFC 3339 format

\Datetime createdAt

A timestamp in RFC 3339 format

?string description

Description of what the deployment does.

string environmentID

ID of the `environment` where sessions run.

list<[BetaManagedAgentsDeploymentInitialEvent](api/beta/deployments.md)> initialEvents

Events sent to each session immediately after creation.

array<string,string> metadata

Arbitrary key-value metadata. Maximum 16 pairs.

string name

Human-readable name.

?[BetaManagedAgentsDeploymentPausedReason](api/beta/deployments.md) pausedReason

Why a deployment is paused. Non-null exactly when `status` is `paused`.

list<[BetaManagedAgentsSessionResourceConfig](api/beta/deployments.md)> resources

Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

?[BetaManagedAgentsSchedule](api/beta/deployments.md) schedule

5-field POSIX cron schedule with computed runtime timestamps.

[BetaManagedAgentsDeploymentStatus](api/beta/deployments.md) status

Lifecycle status of a deployment.

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

list<string> vaultIDs

Vault IDs supplying stored credentials for sessions created from this deployment.

Create Deployment

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeployment = $client->beta->deployments->create(
  agent: 'string',
  environmentID: 'x',
  initialEvents: [
    [
      'content' => [['text' => 'Where is my order #1234?', 'type' => 'text']],
      'type' => 'user.message',
    ],
  ],
  name: 'x',
  description: 'description',
  metadata: ['foo' => 'string'],
  resources: [
    [
      'fileID' => 'file_011CNha8iCJcU1wXNR6q4V8w',
      'type' => 'file',
      'mountPath' => '/uploads/receipt.pdf',
    ],
  ],
  schedule: [
    'expression' => '0 9 * * 1-5',
    'timezone' => 'America/Los_Angeles',
    'type' => 'cron',
  ],
  vaultIDs: ['string'],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsDeployment);
```

Response 200



```shiki
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

---

*Copyright © Anthropic. All rights reserved.*
