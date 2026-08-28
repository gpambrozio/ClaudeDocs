# Webhooks

Copy page



cURL

# Webhooks

##### [Unwrap](api/http/beta/webhooks/unwrap.md)

##### [Parse Unverified](api/http/beta/webhooks/parse_unverified.md)

##### Models



BetaWebhookAgentArchivedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the agent that triggered the event.

organization\_id: string

type: "agent.archived"

workspace\_id: string



BetaWebhookAgentCreatedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the agent that triggered the event.

organization\_id: string

type: "agent.created"

workspace\_id: string



BetaWebhookAgentDeletedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the agent that triggered the event.

organization\_id: string

type: "agent.deleted"

workspace\_id: string



BetaWebhookAgentUpdatedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the agent that triggered the event.

organization\_id: string

type: "agent.updated"

workspace\_id: string



BetaWebhookDeploymentArchivedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the deployment that triggered the event.

organization\_id: string

type: "deployment.archived"

workspace\_id: string



BetaWebhookDeploymentCreatedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the deployment that triggered the event.

organization\_id: string

type: "deployment.created"

workspace\_id: string



BetaWebhookDeploymentDeletedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the deployment that triggered the event.

organization\_id: string

type: "deployment.deleted"

workspace\_id: string



BetaWebhookDeploymentPausedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the deployment that triggered the event.

organization\_id: string

type: "deployment.paused"

workspace\_id: string



BetaWebhookDeploymentRunFailedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the deployment run that triggered the event.

organization\_id: string

type: "deployment\_run.failed"

workspace\_id: string



BetaWebhookDeploymentRunStartedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the deployment run that triggered the event.

organization\_id: string

type: "deployment\_run.started"

workspace\_id: string



BetaWebhookDeploymentRunSucceededEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the deployment run that triggered the event.

organization\_id: string

type: "deployment\_run.succeeded"

workspace\_id: string



BetaWebhookDeploymentUnpausedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the deployment that triggered the event.

organization\_id: string

type: "deployment.unpaused"

workspace\_id: string



BetaWebhookDeploymentUpdatedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the deployment that triggered the event.

organization\_id: string

type: "deployment.updated"

workspace\_id: string



BetaWebhookEnvironmentArchivedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the environment that triggered the event.

organization\_id: string

type: "environment.archived"

workspace\_id: string



BetaWebhookEnvironmentCreatedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the environment that triggered the event.

organization\_id: string

type: "environment.created"

workspace\_id: string



BetaWebhookEnvironmentDeletedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the environment that triggered the event.

organization\_id: string

type: "environment.deleted"

workspace\_id: string



BetaWebhookEnvironmentUpdatedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the environment that triggered the event.

organization\_id: string

type: "environment.updated"

workspace\_id: string



BetaWebhookEvent object{ id, created\_at, data, type }

id: string

Unique event identifier for idempotency.



created\_at: string

RFC 3339 timestamp when the event occurred.

formatdate-time



data: [BetaWebhookEventData](api/http/beta/webhooks.md)

One of the following:

type: "event"

Object type. Always `event` for webhook payloads.



BetaWebhookEventData = [BetaWebhookSessionCreatedEventData](api/http/beta/webhooks.md) { id, organization\_id, type, workspace\_id } or [BetaWebhookSessionPendingEventData](api/http/beta/webhooks.md) { id, organization\_id, type, workspace\_id } or [BetaWebhookSessionRunningEventData](api/http/beta/webhooks.md) { id, organization\_id, type, workspace\_id } or 41 more

One of the following:



BetaWebhookMemoryStoreArchivedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the memory store that triggered the event.

organization\_id: string

type: "memory\_store.archived"

workspace\_id: string



BetaWebhookMemoryStoreCreatedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the memory store that triggered the event.

organization\_id: string

type: "memory\_store.created"

workspace\_id: string



BetaWebhookMemoryStoreDeletedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the memory store that triggered the event.

organization\_id: string

type: "memory\_store.deleted"

workspace\_id: string



BetaWebhookSessionArchivedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.archived"

workspace\_id: string



BetaWebhookSessionBudgetReachedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.budget\_reached"

workspace\_id: string



BetaWebhookSessionCreatedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.created"

workspace\_id: string



BetaWebhookSessionDeletedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.deleted"

workspace\_id: string



BetaWebhookSessionIdledEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.idled"

workspace\_id: string



BetaWebhookSessionOutcomeEvaluationEndedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.outcome\_evaluation\_ended"

workspace\_id: string



BetaWebhookSessionPendingEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.pending"

workspace\_id: string



BetaWebhookSessionRequiresActionEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.requires\_action"

workspace\_id: string



BetaWebhookSessionRunningEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.running"

workspace\_id: string



BetaWebhookSessionStatusIdledEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.status\_idled"

workspace\_id: string



BetaWebhookSessionStatusRescheduledEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.status\_rescheduled"

workspace\_id: string



BetaWebhookSessionStatusRunStartedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.status\_run\_started"

workspace\_id: string



BetaWebhookSessionStatusTerminatedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.status\_terminated"

workspace\_id: string



BetaWebhookSessionThreadCreatedEventData object{ id, organization\_id, session\_thread\_id, 2 more }

id: string

ID of the session that triggered the event.

organization\_id: string

session\_thread\_id: string

ID of the session thread this event refers to.

type: "session.thread\_created"

workspace\_id: string



BetaWebhookSessionThreadIdledEventData object{ id, organization\_id, session\_thread\_id, 2 more }

id: string

ID of the session that triggered the event.

organization\_id: string

session\_thread\_id: string

ID of the session thread this event refers to.

type: "session.thread\_idled"

workspace\_id: string



BetaWebhookSessionThreadTerminatedEventData object{ id, organization\_id, session\_thread\_id, 2 more }

id: string

ID of the session that triggered the event.

organization\_id: string

session\_thread\_id: string

ID of the session thread this event refers to.

type: "session.thread\_terminated"

workspace\_id: string



BetaWebhookSessionUpdatedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.updated"

workspace\_id: string



BetaWebhookVaultArchivedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the vault that triggered the event.

organization\_id: string

type: "vault.archived"

workspace\_id: string



BetaWebhookVaultCreatedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the vault that triggered the event.

organization\_id: string

type: "vault.created"

workspace\_id: string



BetaWebhookVaultCredentialArchivedEventData object{ id, organization\_id, type, 2 more }

id: string

ID of the vault credential that triggered the event.

organization\_id: string

type: "vault\_credential.archived"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string



BetaWebhookVaultCredentialCreatedEventData object{ id, organization\_id, type, 2 more }

id: string

ID of the vault credential that triggered the event.

organization\_id: string

type: "vault\_credential.created"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string



BetaWebhookVaultCredentialDeletedEventData object{ id, organization\_id, type, 2 more }

id: string

ID of the vault credential that triggered the event.

organization\_id: string

type: "vault\_credential.deleted"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string



BetaWebhookVaultCredentialRefreshFailedEventData object{ id, organization\_id, type, 2 more }

id: string

ID of the vault credential that triggered the event.

organization\_id: string

type: "vault\_credential.refresh\_failed"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string



BetaWebhookVaultDeletedEventData object{ id, organization\_id, type, workspace\_id }

id: string

ID of the vault that triggered the event.

organization\_id: string

type: "vault.deleted"

workspace\_id: string

---

*Copyright © Anthropic. All rights reserved.*
