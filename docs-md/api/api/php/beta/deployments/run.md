# Run Deployment Now

Copy page

SDK language

PHP

# Run Deployment Now

$client->beta->deployments->run(string deploymentID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeploymentRun](api/beta.md)

POST/v1/deployments/{deployment\_id}/run

Run Deployment Now

##### ParametersExpand Collapse

deploymentID: string

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



[BetaManagedAgentsDeploymentRun](api/beta.md)

string id

Unique identifier for this run (`drun_...`).

[BetaManagedAgentsAgentReference](api/beta.md) agent

A resolved agent reference with a concrete version.

\Datetime createdAt

A timestamp in RFC 3339 format

string deploymentID

ID of the deployment that produced this run.

?Error error

Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

?string sessionID

Populated on success. Null on creation failure. Exactly one of session\_id or error is non-null.

[BetaManagedAgentsTriggerContext](api/beta.md) triggerContext

Describes what triggered a deployment run, with trigger-specific metadata.

Type type

Run Deployment Now

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeploymentRun = $client->beta->deployments->run(
  'deployment_id', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsDeploymentRun);
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
  "created_at": "2019-12-27T18:11:19.117Z",
  "deployment_id": "deployment_id",
  "error": {
    "message": "message",
    "type": "environment_archived_error"
  },
  "session_id": "session_id",
  "trigger_context": {
    "scheduled_at": "2019-12-27T18:11:19.117Z",
    "type": "schedule"
  },
  "type": "deployment_run"
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
  "created_at": "2019-12-27T18:11:19.117Z",
  "deployment_id": "deployment_id",
  "error": {
    "message": "message",
    "type": "environment_archived_error"
  },
  "session_id": "session_id",
  "trigger_context": {
    "scheduled_at": "2019-12-27T18:11:19.117Z",
    "type": "schedule"
  },
  "type": "deployment_run"
}
```

---

*Copyright © Anthropic. All rights reserved.*
