# Update Deployment

Copy page



PHP

# Update Deployment

$client->beta->deployments->update(string deploymentID, ?[Agent](api/beta/deployments/update.md) agent, ?string description, ?string environmentID, ?list<[BetaManagedAgentsDeploymentInitialEventParams](api/beta.md)> initialEvents, ?array<string,string> metadata, ?string name, ?list<Resource> resources, ?[BetaManagedAgentsScheduleParams](api/beta.md) schedule, ?list<string> vaultIDs, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeployment](api/beta.md)

POST/v1/deployments/{deployment\_id}

Update Deployment

##### ParametersExpand Collapse

deploymentID: string

agent?:optional [Agent](api/beta/deployments/update.md)

Agent to deploy. Accepts the `agent` ID string, which re-pins to the latest version, or an `agent` object with both id and version specified. Omit to preserve. Cannot be cleared.

description?:optional string

Description. Omit to preserve; send empty string or null to clear.

environmentID?:optional string

ID of the `environment` where sessions run. Omit to preserve. Cannot be cleared.

initialEvents?:optional list<[BetaManagedAgentsDeploymentInitialEventParams](api/beta.md)>

Initial events. Full replacement. Omit to preserve. Cannot be cleared. At least 1, maximum 50.

metadata?:optional array<string,string>

Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

name?:optional string

Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

resources?:optional list<Resource>

Session resources. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 500.

schedule?:optional [BetaManagedAgentsScheduleParams](api/beta.md)

5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

vaultIDs?:optional list<string>

Vault IDs. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 50.

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



[BetaManagedAgentsDeployment](api/beta.md)

string id

Unique identifier for this deployment.

[BetaManagedAgentsAgentReference](api/beta.md) agent

A resolved agent reference with a concrete version.

?\Datetime archivedAt

A timestamp in RFC 3339 format

\Datetime createdAt

A timestamp in RFC 3339 format

?string description

Description of what the deployment does.

string environmentID

ID of the `environment` where sessions run.

list<[BetaManagedAgentsDeploymentInitialEvent](api/beta.md)> initialEvents

Events sent to each session immediately after creation.

array<string,string> metadata

Arbitrary key-value metadata. Maximum 16 pairs.

string name

Human-readable name.

?[BetaManagedAgentsDeploymentPausedReason](api/beta.md) pausedReason

Why a deployment is paused. Non-null exactly when `status` is `paused`.

list<[BetaManagedAgentsSessionResourceConfig](api/beta.md)> resources

Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

?[BetaManagedAgentsSchedule](api/beta.md) schedule

5-field POSIX cron schedule with computed runtime timestamps.

[BetaManagedAgentsDeploymentStatus](api/beta.md) status

Lifecycle status of a deployment.

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

list<string> vaultIDs

Vault IDs supplying stored credentials for sessions created from this deployment.

Update Deployment

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeployment = $client->beta->deployments->update(
  'deployment_id',
  agent: 'string',
  description: 'description',
  environmentID: 'environment_id',
  initialEvents: [
    [
      'content' => [['text' => 'Where is my order #1234?', 'type' => 'text']],
      'type' => 'user.message',
    ],
  ],
  metadata: ['foo' => 'string'],
  name: 'name',
  resources: [
    [
      'fileID' => 'file_011CNha8iCJcU1wXNR6q4V8w',
      'type' => 'file',
      'mountPath' => '/uploads/receipt.pdf',
    ],
  ],
  schedule: ['expression' => 'x', 'timezone' => 'x', 'type' => 'cron'],
  vaultIDs: ['string'],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsDeployment);
```

Response 200



```shiki
{
  "id": "id",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "type": "agent",
    "version": 1
  },
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "environment_id": "environment_id",
  "initial_events": [
    {
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {
    "foo": "string"
  },
  "name": "name",
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
    "expression": "x",
    "timezone": "x",
    "type": "cron",
    "last_run_at": "2019-12-27T18:11:19.117Z",
    "upcoming_runs_at": [
      "2019-12-27T18:11:19.117Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "vault_ids": [
    "string"
  ]
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "id",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "type": "agent",
    "version": 1
  },
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "environment_id": "environment_id",
  "initial_events": [
    {
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {
    "foo": "string"
  },
  "name": "name",
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
    "expression": "x",
    "timezone": "x",
    "type": "cron",
    "last_run_at": "2019-12-27T18:11:19.117Z",
    "upcoming_runs_at": [
      "2019-12-27T18:11:19.117Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "vault_ids": [
    "string"
  ]
}
```

---

*Copyright © Anthropic. All rights reserved.*
