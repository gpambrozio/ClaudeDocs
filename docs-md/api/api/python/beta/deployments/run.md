# Run Deployment Now

Copy page

SDK language

Python

# Run Deployment Now

beta.deployments.run(strdeployment\_id, DeploymentRunParams\*\*kwargs)  -> [BetaManagedAgentsDeploymentRun](api/beta.md)

POST/v1/deployments/{deployment\_id}/run

Run Deployment Now

##### ParametersExpand Collapse

deployment\_id: str

betas: Optional[List[[AnthropicBetaParam](api/beta.md)]]

Optional header to specify the beta version(s) you want to use.

One of the following:

str

Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]

One of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"fallback-credit-2026-06-01"

##### ReturnsExpand Collapse

class BetaManagedAgentsDeploymentRun: …

A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

id: str

Unique identifier for this run (`drun_...`).

agent: [BetaManagedAgentsAgentReference](api/beta.md)

A resolved agent reference with a concrete version.

id: str

type: Literal["agent"]

version: int

created\_at: datetime

A timestamp in RFC 3339 format

deployment\_id: str

ID of the deployment that produced this run.

error: Optional[Error]

Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

One of the following:

class BetaManagedAgentsEnvironmentArchivedRunError: …

The deployment's environment was archived.

message: str

Human-readable error description.

type: Literal["environment\_archived\_error"]

class BetaManagedAgentsAgentArchivedRunError: …

The deployment's agent was archived.

message: str

Human-readable error description.

type: Literal["agent\_archived\_error"]

class BetaManagedAgentsEnvironmentNotFoundRunError: …

The deployment's environment no longer exists.

message: str

Human-readable error description.

type: Literal["environment\_not\_found\_error"]

class BetaManagedAgentsVaultNotFoundRunError: …

A vault referenced by the deployment no longer exists.

message: str

Human-readable error description.

type: Literal["vault\_not\_found\_error"]

class BetaManagedAgentsVaultArchivedRunError: …

A vault referenced by the deployment is archived.

message: str

Human-readable error description.

type: Literal["vault\_archived\_error"]

class BetaManagedAgentsFileNotFoundRunError: …

A file resource referenced by the deployment no longer exists.

message: str

Human-readable error description.

type: Literal["file\_not\_found\_error"]

class BetaManagedAgentsMemoryStoreArchivedRunError: …

A memory store referenced by the deployment is archived.

message: str

Human-readable error description.

type: Literal["memory\_store\_archived\_error"]

class BetaManagedAgentsSkillNotFoundRunError: …

A skill referenced by the deployment's agent no longer exists.

message: str

Human-readable error description.

type: Literal["skill\_not\_found\_error"]

class BetaManagedAgentsSessionResourceNotFoundRunError: …

A referenced resource no longer exists and its kind was not reported.

message: str

Human-readable error description.

type: Literal["session\_resource\_not\_found\_error"]

class BetaManagedAgentsWorkspaceArchivedRunError: …

The deployment's workspace was archived.

message: str

Human-readable error description.

type: Literal["workspace\_archived\_error"]

class BetaManagedAgentsOrganizationDisabledRunError: …

The deployment's organization is disabled.

message: str

Human-readable error description.

type: Literal["organization\_disabled\_error"]

class BetaManagedAgentsSessionRateLimitedRunError: …

Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

message: str

Human-readable error description.

type: Literal["session\_rate\_limited\_error"]

class BetaManagedAgentsSessionCreationRejectedRunError: …

The session create request was rejected with a non-retryable validation error.

message: str

Human-readable error description.

type: Literal["session\_creation\_rejected\_error"]

class BetaManagedAgentsUnknownRunError: …

An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

message: str

Human-readable error description.

type: Literal["unknown\_error"]

class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError: …

The deployment configures resources, but its environment is self-hosted and cannot mount them.

message: str

Human-readable error description.

type: Literal["self\_hosted\_resources\_unsupported\_error"]

class BetaManagedAgentsMCPEgressBlockedRunError: …

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

message: str

Human-readable error description.

type: Literal["mcp\_egress\_blocked\_error"]

session\_id: Optional[str]

Populated on success. Null on creation failure. Exactly one of session\_id or error is non-null.

trigger\_context: [BetaManagedAgentsTriggerContext](api/beta.md)

Describes what triggered a deployment run, with trigger-specific metadata.

One of the following:

class BetaManagedAgentsScheduleTriggerContext: …

The run was fired by the deployment's cron schedule.

scheduled\_at: datetime

A timestamp in RFC 3339 format

type: Literal["schedule"]

class BetaManagedAgentsManualTriggerContext: …

The run was started manually by creating a session directly against the deployment.

type: Literal["manual"]

type: Literal["deployment\_run"]

Run Deployment Now

Python

```shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_deployment_run = client.beta.deployments.run(
    deployment_id="deployment_id",
)
print(beta_managed_agents_deployment_run.id)
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
