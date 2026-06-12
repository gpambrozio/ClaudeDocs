# Deployment Runs

Copy page

SDK language

CLI

# Deployment Runs

##### [List Deployment Runs](api/beta/deployment_runs/list.md)

$ ant beta:deployment-runs list

GET/v1/deployment\_runs

##### [Get Deployment Run](api/beta/deployment_runs/retrieve.md)

$ ant beta:deployment-runs retrieve

GET/v1/deployment\_runs/{deployment\_run\_id}

##### ModelsExpand Collapse



beta\_managed\_agents\_agent\_archived\_run\_error: object { message, type } 

The deployment's agent was archived.

message: string

Human-readable error description.



type: "agent\_archived\_error"

"agent\_archived\_error"



beta\_managed\_agents\_deployment\_run: object { id, agent, created\_at, 5 more } 

A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

id: string

Unique identifier for this run (`drun_...`).



agent: object { id, type, version } 

A resolved agent reference with a concrete version.

id: string



type: "agent"

"agent"

version: number

created\_at: string

A timestamp in RFC 3339 format

deployment\_id: string

ID of the deployment that produced this run.



error: [BetaManagedAgentsEnvironmentArchivedRunError](api/beta.md) { message, type }  or [BetaManagedAgentsAgentArchivedRunError](api/beta.md) { message, type }  or [BetaManagedAgentsEnvironmentNotFoundRunError](api/beta.md) { message, type }  or 13 more

Why the run failed to create a session. The type identifies the failure; message is human-readable detail.



beta\_managed\_agents\_environment\_archived\_run\_error: object { message, type } 

The deployment's environment was archived.

message: string

Human-readable error description.



type: "environment\_archived\_error"

"environment\_archived\_error"



beta\_managed\_agents\_agent\_archived\_run\_error: object { message, type } 

The deployment's agent was archived.

message: string

Human-readable error description.



type: "agent\_archived\_error"

"agent\_archived\_error"



beta\_managed\_agents\_environment\_not\_found\_run\_error: object { message, type } 

The deployment's environment no longer exists.

message: string

Human-readable error description.



type: "environment\_not\_found\_error"

"environment\_not\_found\_error"



beta\_managed\_agents\_vault\_not\_found\_run\_error: object { message, type } 

A vault referenced by the deployment no longer exists.

message: string

Human-readable error description.



type: "vault\_not\_found\_error"

"vault\_not\_found\_error"



beta\_managed\_agents\_vault\_archived\_run\_error: object { message, type } 

A vault referenced by the deployment is archived.

message: string

Human-readable error description.



type: "vault\_archived\_error"

"vault\_archived\_error"



beta\_managed\_agents\_file\_not\_found\_run\_error: object { message, type } 

A file resource referenced by the deployment no longer exists.

message: string

Human-readable error description.



type: "file\_not\_found\_error"

"file\_not\_found\_error"



beta\_managed\_agents\_memory\_store\_archived\_run\_error: object { message, type } 

A memory store referenced by the deployment is archived.

message: string

Human-readable error description.



type: "memory\_store\_archived\_error"

"memory\_store\_archived\_error"



beta\_managed\_agents\_skill\_not\_found\_run\_error: object { message, type } 

A skill referenced by the deployment's agent no longer exists.

message: string

Human-readable error description.



type: "skill\_not\_found\_error"

"skill\_not\_found\_error"



beta\_managed\_agents\_session\_resource\_not\_found\_run\_error: object { message, type } 

A referenced resource no longer exists and its kind was not reported.

message: string

Human-readable error description.



type: "session\_resource\_not\_found\_error"

"session\_resource\_not\_found\_error"



beta\_managed\_agents\_workspace\_archived\_run\_error: object { message, type } 

The deployment's workspace was archived.

message: string

Human-readable error description.



type: "workspace\_archived\_error"

"workspace\_archived\_error"



beta\_managed\_agents\_organization\_disabled\_run\_error: object { message, type } 

The deployment's organization is disabled.

message: string

Human-readable error description.



type: "organization\_disabled\_error"

"organization\_disabled\_error"



beta\_managed\_agents\_session\_rate\_limited\_run\_error: object { message, type } 

Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

message: string

Human-readable error description.



type: "session\_rate\_limited\_error"

"session\_rate\_limited\_error"



beta\_managed\_agents\_session\_creation\_rejected\_run\_error: object { message, type } 

The session create request was rejected with a non-retryable validation error.

message: string

Human-readable error description.



type: "session\_creation\_rejected\_error"

"session\_creation\_rejected\_error"



beta\_managed\_agents\_unknown\_run\_error: object { message, type } 

An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

message: string

Human-readable error description.



type: "unknown\_error"

"unknown\_error"



beta\_managed\_agents\_self\_hosted\_resources\_unsupported\_run\_error: object { message, type } 

The deployment configures resources, but its environment is self-hosted and cannot mount them.

message: string

Human-readable error description.



type: "self\_hosted\_resources\_unsupported\_error"

"self\_hosted\_resources\_unsupported\_error"



beta\_managed\_agents\_mcp\_egress\_blocked\_run\_error: object { message, type } 

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

message: string

Human-readable error description.



type: "mcp\_egress\_blocked\_error"

"mcp\_egress\_blocked\_error"

session\_id: string

Populated on success. Null on creation failure. Exactly one of session\_id or error is non-null.



trigger\_context: [BetaManagedAgentsScheduleTriggerContext](api/beta.md) { scheduled\_at, type }  or [BetaManagedAgentsManualTriggerContext](api/beta.md) { type } 

Describes what triggered a deployment run, with trigger-specific metadata.



beta\_managed\_agents\_schedule\_trigger\_context: object { scheduled\_at, type } 

The run was fired by the deployment's cron schedule.

scheduled\_at: string

A timestamp in RFC 3339 format



type: "schedule"

"schedule"



beta\_managed\_agents\_manual\_trigger\_context: object { type } 

The run was started manually by creating a session directly against the deployment.



type: "manual"

"manual"



type: "deployment\_run"

"deployment\_run"



beta\_managed\_agents\_environment\_archived\_run\_error: object { message, type } 

The deployment's environment was archived.

message: string

Human-readable error description.



type: "environment\_archived\_error"

"environment\_archived\_error"



beta\_managed\_agents\_environment\_not\_found\_run\_error: object { message, type } 

The deployment's environment no longer exists.

message: string

Human-readable error description.



type: "environment\_not\_found\_error"

"environment\_not\_found\_error"



beta\_managed\_agents\_file\_not\_found\_run\_error: object { message, type } 

A file resource referenced by the deployment no longer exists.

message: string

Human-readable error description.



type: "file\_not\_found\_error"

"file\_not\_found\_error"



beta\_managed\_agents\_manual\_trigger\_context: object { type } 

The run was started manually by creating a session directly against the deployment.



type: "manual"

"manual"



beta\_managed\_agents\_mcp\_egress\_blocked\_run\_error: object { message, type } 

An MCP server host used by the deployment's agent is blocked by the environment's network policy.

message: string

Human-readable error description.



type: "mcp\_egress\_blocked\_error"

"mcp\_egress\_blocked\_error"



beta\_managed\_agents\_memory\_store\_archived\_run\_error: object { message, type } 

A memory store referenced by the deployment is archived.

message: string

Human-readable error description.



type: "memory\_store\_archived\_error"

"memory\_store\_archived\_error"



beta\_managed\_agents\_organization\_disabled\_run\_error: object { message, type } 

The deployment's organization is disabled.

message: string

Human-readable error description.



type: "organization\_disabled\_error"

"organization\_disabled\_error"



beta\_managed\_agents\_schedule\_trigger\_context: object { scheduled\_at, type } 

The run was fired by the deployment's cron schedule.

scheduled\_at: string

A timestamp in RFC 3339 format



type: "schedule"

"schedule"



beta\_managed\_agents\_self\_hosted\_resources\_unsupported\_run\_error: object { message, type } 

The deployment configures resources, but its environment is self-hosted and cannot mount them.

message: string

Human-readable error description.



type: "self\_hosted\_resources\_unsupported\_error"

"self\_hosted\_resources\_unsupported\_error"



beta\_managed\_agents\_session\_creation\_rejected\_run\_error: object { message, type } 

The session create request was rejected with a non-retryable validation error.

message: string

Human-readable error description.



type: "session\_creation\_rejected\_error"

"session\_creation\_rejected\_error"



beta\_managed\_agents\_session\_rate\_limited\_run\_error: object { message, type } 

Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

message: string

Human-readable error description.



type: "session\_rate\_limited\_error"

"session\_rate\_limited\_error"



beta\_managed\_agents\_session\_resource\_not\_found\_run\_error: object { message, type } 

A referenced resource no longer exists and its kind was not reported.

message: string

Human-readable error description.



type: "session\_resource\_not\_found\_error"

"session\_resource\_not\_found\_error"



beta\_managed\_agents\_skill\_not\_found\_run\_error: object { message, type } 

A skill referenced by the deployment's agent no longer exists.

message: string

Human-readable error description.



type: "skill\_not\_found\_error"

"skill\_not\_found\_error"



beta\_managed\_agents\_trigger\_context: [BetaManagedAgentsScheduleTriggerContext](api/beta.md) { scheduled\_at, type }  or [BetaManagedAgentsManualTriggerContext](api/beta.md) { type } 

Describes what triggered a deployment run, with trigger-specific metadata.



beta\_managed\_agents\_schedule\_trigger\_context: object { scheduled\_at, type } 

The run was fired by the deployment's cron schedule.

scheduled\_at: string

A timestamp in RFC 3339 format



type: "schedule"

"schedule"



beta\_managed\_agents\_manual\_trigger\_context: object { type } 

The run was started manually by creating a session directly against the deployment.



type: "manual"

"manual"



beta\_managed\_agents\_trigger\_type: "schedule" or "manual"

What triggered a deployment run.

"schedule"

"manual"



beta\_managed\_agents\_unknown\_run\_error: object { message, type } 

An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

message: string

Human-readable error description.



type: "unknown\_error"

"unknown\_error"



beta\_managed\_agents\_vault\_archived\_run\_error: object { message, type } 

A vault referenced by the deployment is archived.

message: string

Human-readable error description.



type: "vault\_archived\_error"

"vault\_archived\_error"



beta\_managed\_agents\_vault\_not\_found\_run\_error: object { message, type } 

A vault referenced by the deployment no longer exists.

message: string

Human-readable error description.



type: "vault\_not\_found\_error"

"vault\_not\_found\_error"



beta\_managed\_agents\_workspace\_archived\_run\_error: object { message, type } 

The deployment's workspace was archived.

message: string

Human-readable error description.



type: "workspace\_archived\_error"

"workspace\_archived\_error"

---

*Copyright © Anthropic. All rights reserved.*
