# Archive Deployment

Copy page

SDK language

PHP

# Archive Deployment

$client->beta->deployments->archive(string deploymentID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeployment](api/beta.md)

POST/v1/deployments/{deployment\_id}/archive

Archive Deployment

##### ParametersExpand Collapse

deploymentID: string

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

[BetaManagedAgentsDeployment](api/beta.md)

string id

Unique identifier for this deployment.

[BetaManagedAgentsAgentReference](api/beta.md) agent

A resolved agent reference with a concrete version.

?\Datetime archivedAt

A timestamp in RFC 3339 format

\Datetime createdAt

A timestamp in RFC 3339 format

?string description

Description of what the deployment does.

string environmentID

ID of the `environment` where sessions run.

list<[BetaManagedAgentsDeploymentInitialEvent](api/beta.md)> initialEvents

Events sent to each session immediately after creation.

array<string,string> metadata

Arbitrary key-value metadata. Maximum 16 pairs.

string name

Human-readable name.

?[BetaManagedAgentsDeploymentPausedReason](api/beta.md) pausedReason

Why a deployment is paused. Non-null exactly when `status` is `paused`.

list<[BetaManagedAgentsSessionResourceConfig](api/beta.md)> resources

Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

?[BetaManagedAgentsSchedule](api/beta.md) schedule

5-field POSIX cron schedule with computed runtime timestamps.

[BetaManagedAgentsDeploymentStatus](api/beta.md) status

Lifecycle status of a deployment.

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

list<string> vaultIDs

Vault IDs supplying stored credentials for sessions created from this deployment.

Archive Deployment

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeployment = $client->beta->deployments->archive(
  'deployment_id', betas: ['message-batches-2024-09-24']
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
