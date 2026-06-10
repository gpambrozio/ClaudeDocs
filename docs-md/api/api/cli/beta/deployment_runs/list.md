# List Deployment Runs

Copy page

SDK language

CLI

# List Deployment Runs

$ ant beta:deployment-runs list

GET/v1/deployment\_runs

List Deployment Runs

##### ParametersExpand Collapse

--created-at-gt: optional string

Query param: Return runs created strictly after this time (exclusive).

--created-at-gte: optional string

Query param: Return runs created at or after this time (inclusive).

--created-at-lt: optional string

Query param: Return runs created strictly before this time (exclusive).

--created-at-lte: optional string

Query param: Return runs created at or before this time (inclusive).

--deployment-id: optional string

Query param: Filter to a specific deployment. Omit to list across all deployments in the workspace. Filtering by a non-existent deployment\_id returns 200 with empty data.

--has-error: optional boolean

Query param: Filter: true for runs with non-null error, false for runs with non-null session\_id. Omit for all.

--limit: optional number

Query param: Maximum results per page. Default 20, maximum 1000.

--page: optional string

Query param: Opaque pagination cursor. Pass next\_page from the previous response. Invalid or expired cursors return 400.

--trigger-type: optional "schedule" or "manual"

Query param: Filter runs by what triggered them. Omit to return all runs.

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

BetaManagedAgentsListDeploymentRunsData: object { data, next\_page }

Paginated list of deployment runs. Sorted by created\_at descending (most recent first).

data: array of [BetaManagedAgentsDeploymentRun](api/beta.md) { id, agent, created\_at, 5 more }

List of deployment runs.

id: string

Unique identifier for this run (`drun_...`).

agent: object { id, type, version }

A resolved agent reference with a concrete version.

id: string

type: "agent"

"agent"

version: number

created\_at: string

A timestamp in RFC 3339 format

deployment\_id: string

ID of the deployment that produced this run.

error: [BetaManagedAgentsEnvironmentArchivedRunError](api/beta.md) { message, type }  or [BetaManagedAgentsAgentArchivedRunError](api/beta.md) { message, type }  or [BetaManagedAgentsEnvironmentNotFoundRunError](api/beta.md) { message, type }  or 13 more

Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

beta\_managed\_agents\_environment\_archived\_run\_error: object { message, type }

The deployment's environment was archived.

message: string

Human-readable error description.

type: "environment\_archived\_error"

"environment\_archived\_error"

beta\_managed\_agents\_agent\_archived\_run\_error: object { message, type }

The deployment's agent was archived.

message: string

Human-readable error description.

type: "agent\_archived\_error"

"agent\_archived\_error"

beta\_managed\_agents\_environment\_not\_found\_run\_error: object { message, type }

The deployment's environment no longer exists.

message: string

Human-readable error description.

type: "environment\_not\_found\_error"

"environment\_not\_found\_error"

beta\_managed\_agents\_vault\_not\_found\_run\_error: object { message, type }

A vault referenced by the deployment no longer exists.

message: string

Human-readable error description.

type: "vault\_not\_found\_error"

"vault\_not\_found\_error"

beta\_managed\_agents\_vault\_archived\_run\_error: object { message, type }

A vault referenced by the deployment is archived.

message: string

Human-readable error description.

type: "vault\_archived\_error"

"vault\_archived\_error"

beta\_managed\_agents\_file\_not\_found\_run\_error: object { message, type }

A file resource referenced by the deployment no longer exists.

message: string

Human-readable error description.

type: "file\_not\_found\_error"

"file\_not\_found\_error"

beta\_managed\_agents\_memory\_store\_archived\_run\_error: object { message, type }

A memory store referenced by the deployment is archived.

message: string

Human-readable error description.

type: "memory\_store\_archived\_error"

"memory\_store\_archived\_error"

beta\_managed\_agents\_skill\_not\_found\_run\_error: object { message, type }

A skill referenced by the deployment's agent no longer exists.

message: string

Human-readable error description.

type: "skill\_not\_found\_error"

"skill\_not\_found\_error"

beta\_managed\_agents\_session\_resource\_not\_found\_run\_error: object { message, type }

A referenced resource no longer exists and its kind was not reported.

message: string

Human-readable error description.

type: "session\_resource\_not\_found\_error"

"session\_resource\_not\_found\_error"

beta\_managed\_agents\_workspace\_archived\_run\_error: object { message, type }

The deployment's workspace was archived.

message: string

Human-readable error description.

type: "workspace\_archived\_error"

"workspace\_archived\_error"

beta\_managed\_agents\_organization\_disabled\_run\_error: object { message, type }

The deployment's organization is disabled.

message: string

Human-readable error description.

type: "organization\_disabled\_error"

"organization\_disabled\_error"

beta\_managed\_agents\_session\_rate\_limited\_run\_error: object { message, type }

Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

message: string

Human-readable error description.

type: "session\_rate\_limited\_error"

"session\_rate\_limited\_error"

beta\_managed\_agents\_session\_creation\_rejected\_run\_error: object { message, type }

The session create request was rejected with a non-retryable validation error.

message: string

Human-readable error description.

type: "session\_creation\_rejected\_error"

"session\_creation\_rejected\_error"

beta\_managed\_agents\_unknown\_run\_error: object { message, type }

An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

message: string

Human-readable error description.

type: "unknown\_error"

"unknown\_error"

beta\_managed\_agents\_self\_hosted\_resources\_unsupported\_run\_error: object { message, type }

The deployment configures resources, but its environment is self-hosted and cannot mount them.

message: string

Human-readable error description.

type: "self\_hosted\_resources\_unsupported\_error"

"self\_hosted\_resources\_unsupported\_error"

beta\_managed\_agents\_mcp\_egress\_blocked\_run\_error: object { message, type }

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

message: string

Human-readable error description.

type: "mcp\_egress\_blocked\_error"

"mcp\_egress\_blocked\_error"

session\_id: string

Populated on success. Null on creation failure. Exactly one of session\_id or error is non-null.

trigger\_context: [BetaManagedAgentsScheduleTriggerContext](api/beta.md) { scheduled\_at, type }  or [BetaManagedAgentsManualTriggerContext](api/beta.md) { type }

Describes what triggered a deployment run, with trigger-specific metadata.

beta\_managed\_agents\_schedule\_trigger\_context: object { scheduled\_at, type }

The run was fired by the deployment's cron schedule.

scheduled\_at: string

A timestamp in RFC 3339 format

type: "schedule"

"schedule"

beta\_managed\_agents\_manual\_trigger\_context: object { type }

The run was started manually by creating a session directly against the deployment.

type: "manual"

"manual"

type: "deployment\_run"

"deployment\_run"

next\_page: optional string

Opaque cursor for the next page. Null when no more results.

List Deployment Runs

CLI

```shiki
ant beta:deployment-runs list \
  --api-key my-anthropic-api-key
```

Response 200



```shiki
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
