# Webhooks

Copy page



Ruby

# Webhooks

Helpers for receiving and verifying webhook events. Use `unwrap` in your SDK to verify signatures and parse payloads; see the [webhooks guide](managed-agents/webhooks.md) for handler examples.

Possible `data.type` values:

- `agent.archived`
- `agent.created`
- `agent.deleted`
- `agent.updated`
- `deployment.archived`
- `deployment.created`
- `deployment.deleted`
- `deployment.paused`
- `deployment.unpaused`
- `deployment.updated`
- `deployment_run.failed`
- `deployment_run.started`
- `deployment_run.succeeded`
- `environment.archived`
- `environment.created`
- `environment.updated`
- `memory_store.archived`
- `memory_store.created`
- `memory_store.deleted`
- `session.archived`
- `session.created`
- `session.deleted`
- `session.idled`
- `session.outcome_evaluation_ended`
- `session.pending`
- `session.requires_action`
- `session.running`
- `session.status_idled`
- `session.status_rescheduled`
- `session.status_run_started`
- `session.status_terminated`
- `session.thread_created`
- `session.thread_idled`
- `session.thread_terminated`
- `session.updated`
- `vault.archived`
- `vault.created`
- `vault.deleted`
- `vault_credential.archived`
- `vault_credential.created`
- `vault_credential.deleted`
- `vault_credential.refresh_failed`

##### ModelsExpand Collapse



class BetaWebhookAgentArchivedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the agent that triggered the event.

organization\_id: String

type: :"agent.archived"

workspace\_id: String



class BetaWebhookAgentCreatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the agent that triggered the event.

organization\_id: String

type: :"agent.created"

workspace\_id: String



class BetaWebhookAgentDeletedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the agent that triggered the event.

organization\_id: String

type: :"agent.deleted"

workspace\_id: String



class BetaWebhookAgentUpdatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the agent that triggered the event.

organization\_id: String

type: :"agent.updated"

workspace\_id: String



class BetaWebhookDeploymentArchivedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment that triggered the event.

organization\_id: String

type: :"deployment.archived"

workspace\_id: String



class BetaWebhookDeploymentCreatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment that triggered the event.

organization\_id: String

type: :"deployment.created"

workspace\_id: String



class BetaWebhookDeploymentDeletedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment that triggered the event.

organization\_id: String

type: :"deployment.deleted"

workspace\_id: String



class BetaWebhookDeploymentPausedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment that triggered the event.

organization\_id: String

type: :"deployment.paused"

workspace\_id: String



class BetaWebhookDeploymentRunFailedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment run that triggered the event.

organization\_id: String

type: :"deployment\_run.failed"

workspace\_id: String



class BetaWebhookDeploymentRunStartedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment run that triggered the event.

organization\_id: String

type: :"deployment\_run.started"

workspace\_id: String



class BetaWebhookDeploymentRunSucceededEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment run that triggered the event.

organization\_id: String

type: :"deployment\_run.succeeded"

workspace\_id: String



class BetaWebhookDeploymentUnpausedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment that triggered the event.

organization\_id: String

type: :"deployment.unpaused"

workspace\_id: String



class BetaWebhookDeploymentUpdatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment that triggered the event.

organization\_id: String

type: :"deployment.updated"

workspace\_id: String



class BetaWebhookEnvironmentArchivedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the environment that triggered the event.

organization\_id: String

type: :"environment.archived"

workspace\_id: String



class BetaWebhookEnvironmentCreatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the environment that triggered the event.

organization\_id: String

type: :"environment.created"

workspace\_id: String



class BetaWebhookEnvironmentDeletedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the environment that triggered the event.

organization\_id: String

type: [BetaWebhookEnvironmentDeletedEventType](api/beta/webhooks.md)

workspace\_id: String

BetaWebhookEnvironmentDeletedEventType = :"environment.deleted"



class BetaWebhookEnvironmentUpdatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the environment that triggered the event.

organization\_id: String

type: :"environment.updated"

workspace\_id: String



class BetaWebhookEvent { id, created\_at, data, type } 

id: String

Unique event identifier for idempotency.

created\_at: Time

RFC 3339 timestamp when the event occurred.



data: [BetaWebhookEventData](api/beta/webhooks.md)

One of the following:



class BetaWebhookSessionCreatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.created"

workspace\_id: String



class BetaWebhookSessionPendingEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.pending"

workspace\_id: String



class BetaWebhookSessionRunningEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.running"

workspace\_id: String



class BetaWebhookSessionIdledEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.idled"

workspace\_id: String



class BetaWebhookSessionRequiresActionEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.requires\_action"

workspace\_id: String



class BetaWebhookSessionArchivedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.archived"

workspace\_id: String



class BetaWebhookSessionDeletedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.deleted"

workspace\_id: String



class BetaWebhookSessionStatusRescheduledEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.status\_rescheduled"

workspace\_id: String



class BetaWebhookSessionStatusRunStartedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.status\_run\_started"

workspace\_id: String



class BetaWebhookSessionStatusIdledEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.status\_idled"

workspace\_id: String



class BetaWebhookSessionStatusTerminatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.status\_terminated"

workspace\_id: String



class BetaWebhookSessionThreadCreatedEventData { id, organization\_id, session\_thread\_id, 2 more } 

id: String

ID of the session that triggered the event.

organization\_id: String

session\_thread\_id: String

ID of the session thread this event refers to.

type: :"session.thread\_created"

workspace\_id: String



class BetaWebhookSessionThreadIdledEventData { id, organization\_id, session\_thread\_id, 2 more } 

id: String

ID of the session that triggered the event.

organization\_id: String

session\_thread\_id: String

ID of the session thread this event refers to.

type: :"session.thread\_idled"

workspace\_id: String



class BetaWebhookSessionThreadTerminatedEventData { id, organization\_id, session\_thread\_id, 2 more } 

id: String

ID of the session that triggered the event.

organization\_id: String

session\_thread\_id: String

ID of the session thread this event refers to.

type: :"session.thread\_terminated"

workspace\_id: String



class BetaWebhookSessionOutcomeEvaluationEndedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.outcome\_evaluation\_ended"

workspace\_id: String



class BetaWebhookVaultCreatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the vault that triggered the event.

organization\_id: String

type: :"vault.created"

workspace\_id: String



class BetaWebhookVaultArchivedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the vault that triggered the event.

organization\_id: String

type: :"vault.archived"

workspace\_id: String



class BetaWebhookVaultDeletedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the vault that triggered the event.

organization\_id: String

type: :"vault.deleted"

workspace\_id: String



class BetaWebhookVaultCredentialCreatedEventData { id, organization\_id, type, 2 more } 

id: String

ID of the vault credential that triggered the event.

organization\_id: String

type: :"vault\_credential.created"

vault\_id: String

ID of the vault that owns this credential.

workspace\_id: String



class BetaWebhookVaultCredentialArchivedEventData { id, organization\_id, type, 2 more } 

id: String

ID of the vault credential that triggered the event.

organization\_id: String

type: :"vault\_credential.archived"

vault\_id: String

ID of the vault that owns this credential.

workspace\_id: String



class BetaWebhookVaultCredentialDeletedEventData { id, organization\_id, type, 2 more } 

id: String

ID of the vault credential that triggered the event.

organization\_id: String

type: :"vault\_credential.deleted"

vault\_id: String

ID of the vault that owns this credential.

workspace\_id: String



class BetaWebhookVaultCredentialRefreshFailedEventData { id, organization\_id, type, 2 more } 

id: String

ID of the vault credential that triggered the event.

organization\_id: String

type: :"vault\_credential.refresh\_failed"

vault\_id: String

ID of the vault that owns this credential.

workspace\_id: String



class BetaWebhookSessionUpdatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.updated"

workspace\_id: String



class BetaWebhookAgentCreatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the agent that triggered the event.

organization\_id: String

type: :"agent.created"

workspace\_id: String



class BetaWebhookAgentArchivedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the agent that triggered the event.

organization\_id: String

type: :"agent.archived"

workspace\_id: String



class BetaWebhookAgentDeletedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the agent that triggered the event.

organization\_id: String

type: :"agent.deleted"

workspace\_id: String



class BetaWebhookDeploymentPausedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment that triggered the event.

organization\_id: String

type: :"deployment.paused"

workspace\_id: String



class BetaWebhookDeploymentRunFailedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment run that triggered the event.

organization\_id: String

type: :"deployment\_run.failed"

workspace\_id: String



class BetaWebhookDeploymentCreatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment that triggered the event.

organization\_id: String

type: :"deployment.created"

workspace\_id: String



class BetaWebhookDeploymentUpdatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment that triggered the event.

organization\_id: String

type: :"deployment.updated"

workspace\_id: String



class BetaWebhookDeploymentUnpausedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment that triggered the event.

organization\_id: String

type: :"deployment.unpaused"

workspace\_id: String



class BetaWebhookAgentUpdatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the agent that triggered the event.

organization\_id: String

type: :"agent.updated"

workspace\_id: String



class BetaWebhookDeploymentArchivedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment that triggered the event.

organization\_id: String

type: :"deployment.archived"

workspace\_id: String



class BetaWebhookDeploymentRunStartedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment run that triggered the event.

organization\_id: String

type: :"deployment\_run.started"

workspace\_id: String



class BetaWebhookDeploymentDeletedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment that triggered the event.

organization\_id: String

type: :"deployment.deleted"

workspace\_id: String



class BetaWebhookDeploymentRunSucceededEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment run that triggered the event.

organization\_id: String

type: :"deployment\_run.succeeded"

workspace\_id: String



class BetaWebhookEnvironmentCreatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the environment that triggered the event.

organization\_id: String

type: :"environment.created"

workspace\_id: String



class BetaWebhookEnvironmentUpdatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the environment that triggered the event.

organization\_id: String

type: :"environment.updated"

workspace\_id: String



class BetaWebhookEnvironmentArchivedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the environment that triggered the event.

organization\_id: String

type: :"environment.archived"

workspace\_id: String



class BetaWebhookEnvironmentDeletedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the environment that triggered the event.

organization\_id: String

type: [BetaWebhookEnvironmentDeletedEventType](api/beta/webhooks.md)

workspace\_id: String



class BetaWebhookMemoryStoreCreatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the memory store that triggered the event.

organization\_id: String

type: :"memory\_store.created"

workspace\_id: String



class BetaWebhookMemoryStoreArchivedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the memory store that triggered the event.

organization\_id: String

type: :"memory\_store.archived"

workspace\_id: String



class BetaWebhookMemoryStoreDeletedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the memory store that triggered the event.

organization\_id: String

type: :"memory\_store.deleted"

workspace\_id: String

type: :event

Object type. Always `event` for webhook payloads.



BetaWebhookEventData = [BetaWebhookSessionCreatedEventData](api/beta/webhooks.md) { id, organization\_id, type, workspace\_id }  | [BetaWebhookSessionPendingEventData](api/beta/webhooks.md) { id, organization\_id, type, workspace\_id }  | [BetaWebhookSessionRunningEventData](api/beta/webhooks.md) { id, organization\_id, type, workspace\_id }  | 40 more

One of the following:



class BetaWebhookSessionCreatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.created"

workspace\_id: String



class BetaWebhookSessionPendingEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.pending"

workspace\_id: String



class BetaWebhookSessionRunningEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.running"

workspace\_id: String



class BetaWebhookSessionIdledEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.idled"

workspace\_id: String



class BetaWebhookSessionRequiresActionEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.requires\_action"

workspace\_id: String



class BetaWebhookSessionArchivedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.archived"

workspace\_id: String



class BetaWebhookSessionDeletedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.deleted"

workspace\_id: String



class BetaWebhookSessionStatusRescheduledEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.status\_rescheduled"

workspace\_id: String



class BetaWebhookSessionStatusRunStartedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.status\_run\_started"

workspace\_id: String



class BetaWebhookSessionStatusIdledEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.status\_idled"

workspace\_id: String



class BetaWebhookSessionStatusTerminatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.status\_terminated"

workspace\_id: String



class BetaWebhookSessionThreadCreatedEventData { id, organization\_id, session\_thread\_id, 2 more } 

id: String

ID of the session that triggered the event.

organization\_id: String

session\_thread\_id: String

ID of the session thread this event refers to.

type: :"session.thread\_created"

workspace\_id: String



class BetaWebhookSessionThreadIdledEventData { id, organization\_id, session\_thread\_id, 2 more } 

id: String

ID of the session that triggered the event.

organization\_id: String

session\_thread\_id: String

ID of the session thread this event refers to.

type: :"session.thread\_idled"

workspace\_id: String



class BetaWebhookSessionThreadTerminatedEventData { id, organization\_id, session\_thread\_id, 2 more } 

id: String

ID of the session that triggered the event.

organization\_id: String

session\_thread\_id: String

ID of the session thread this event refers to.

type: :"session.thread\_terminated"

workspace\_id: String



class BetaWebhookSessionOutcomeEvaluationEndedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.outcome\_evaluation\_ended"

workspace\_id: String



class BetaWebhookVaultCreatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the vault that triggered the event.

organization\_id: String

type: :"vault.created"

workspace\_id: String



class BetaWebhookVaultArchivedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the vault that triggered the event.

organization\_id: String

type: :"vault.archived"

workspace\_id: String



class BetaWebhookVaultDeletedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the vault that triggered the event.

organization\_id: String

type: :"vault.deleted"

workspace\_id: String



class BetaWebhookVaultCredentialCreatedEventData { id, organization\_id, type, 2 more } 

id: String

ID of the vault credential that triggered the event.

organization\_id: String

type: :"vault\_credential.created"

vault\_id: String

ID of the vault that owns this credential.

workspace\_id: String



class BetaWebhookVaultCredentialArchivedEventData { id, organization\_id, type, 2 more } 

id: String

ID of the vault credential that triggered the event.

organization\_id: String

type: :"vault\_credential.archived"

vault\_id: String

ID of the vault that owns this credential.

workspace\_id: String



class BetaWebhookVaultCredentialDeletedEventData { id, organization\_id, type, 2 more } 

id: String

ID of the vault credential that triggered the event.

organization\_id: String

type: :"vault\_credential.deleted"

vault\_id: String

ID of the vault that owns this credential.

workspace\_id: String



class BetaWebhookVaultCredentialRefreshFailedEventData { id, organization\_id, type, 2 more } 

id: String

ID of the vault credential that triggered the event.

organization\_id: String

type: :"vault\_credential.refresh\_failed"

vault\_id: String

ID of the vault that owns this credential.

workspace\_id: String



class BetaWebhookSessionUpdatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.updated"

workspace\_id: String



class BetaWebhookAgentCreatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the agent that triggered the event.

organization\_id: String

type: :"agent.created"

workspace\_id: String



class BetaWebhookAgentArchivedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the agent that triggered the event.

organization\_id: String

type: :"agent.archived"

workspace\_id: String



class BetaWebhookAgentDeletedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the agent that triggered the event.

organization\_id: String

type: :"agent.deleted"

workspace\_id: String



class BetaWebhookDeploymentPausedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment that triggered the event.

organization\_id: String

type: :"deployment.paused"

workspace\_id: String



class BetaWebhookDeploymentRunFailedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment run that triggered the event.

organization\_id: String

type: :"deployment\_run.failed"

workspace\_id: String



class BetaWebhookDeploymentCreatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment that triggered the event.

organization\_id: String

type: :"deployment.created"

workspace\_id: String



class BetaWebhookDeploymentUpdatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment that triggered the event.

organization\_id: String

type: :"deployment.updated"

workspace\_id: String



class BetaWebhookDeploymentUnpausedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment that triggered the event.

organization\_id: String

type: :"deployment.unpaused"

workspace\_id: String



class BetaWebhookAgentUpdatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the agent that triggered the event.

organization\_id: String

type: :"agent.updated"

workspace\_id: String



class BetaWebhookDeploymentArchivedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment that triggered the event.

organization\_id: String

type: :"deployment.archived"

workspace\_id: String



class BetaWebhookDeploymentRunStartedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment run that triggered the event.

organization\_id: String

type: :"deployment\_run.started"

workspace\_id: String



class BetaWebhookDeploymentDeletedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment that triggered the event.

organization\_id: String

type: :"deployment.deleted"

workspace\_id: String



class BetaWebhookDeploymentRunSucceededEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment run that triggered the event.

organization\_id: String

type: :"deployment\_run.succeeded"

workspace\_id: String



class BetaWebhookEnvironmentCreatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the environment that triggered the event.

organization\_id: String

type: :"environment.created"

workspace\_id: String



class BetaWebhookEnvironmentUpdatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the environment that triggered the event.

organization\_id: String

type: :"environment.updated"

workspace\_id: String



class BetaWebhookEnvironmentArchivedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the environment that triggered the event.

organization\_id: String

type: :"environment.archived"

workspace\_id: String



class BetaWebhookEnvironmentDeletedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the environment that triggered the event.

organization\_id: String

type: [BetaWebhookEnvironmentDeletedEventType](api/beta/webhooks.md)

workspace\_id: String



class BetaWebhookMemoryStoreCreatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the memory store that triggered the event.

organization\_id: String

type: :"memory\_store.created"

workspace\_id: String



class BetaWebhookMemoryStoreArchivedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the memory store that triggered the event.

organization\_id: String

type: :"memory\_store.archived"

workspace\_id: String



class BetaWebhookMemoryStoreDeletedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the memory store that triggered the event.

organization\_id: String

type: :"memory\_store.deleted"

workspace\_id: String



class BetaWebhookMemoryStoreArchivedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the memory store that triggered the event.

organization\_id: String

type: :"memory\_store.archived"

workspace\_id: String



class BetaWebhookMemoryStoreCreatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the memory store that triggered the event.

organization\_id: String

type: :"memory\_store.created"

workspace\_id: String



class BetaWebhookMemoryStoreDeletedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the memory store that triggered the event.

organization\_id: String

type: :"memory\_store.deleted"

workspace\_id: String



class BetaWebhookSessionArchivedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.archived"

workspace\_id: String



class BetaWebhookSessionCreatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.created"

workspace\_id: String



class BetaWebhookSessionDeletedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.deleted"

workspace\_id: String



class BetaWebhookSessionIdledEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.idled"

workspace\_id: String



class BetaWebhookSessionOutcomeEvaluationEndedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.outcome\_evaluation\_ended"

workspace\_id: String



class BetaWebhookSessionPendingEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.pending"

workspace\_id: String



class BetaWebhookSessionRequiresActionEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.requires\_action"

workspace\_id: String



class BetaWebhookSessionRunningEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.running"

workspace\_id: String



class BetaWebhookSessionStatusIdledEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.status\_idled"

workspace\_id: String



class BetaWebhookSessionStatusRescheduledEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.status\_rescheduled"

workspace\_id: String



class BetaWebhookSessionStatusRunStartedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.status\_run\_started"

workspace\_id: String



class BetaWebhookSessionStatusTerminatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.status\_terminated"

workspace\_id: String



class BetaWebhookSessionThreadCreatedEventData { id, organization\_id, session\_thread\_id, 2 more } 

id: String

ID of the session that triggered the event.

organization\_id: String

session\_thread\_id: String

ID of the session thread this event refers to.

type: :"session.thread\_created"

workspace\_id: String



class BetaWebhookSessionThreadIdledEventData { id, organization\_id, session\_thread\_id, 2 more } 

id: String

ID of the session that triggered the event.

organization\_id: String

session\_thread\_id: String

ID of the session thread this event refers to.

type: :"session.thread\_idled"

workspace\_id: String



class BetaWebhookSessionThreadTerminatedEventData { id, organization\_id, session\_thread\_id, 2 more } 

id: String

ID of the session that triggered the event.

organization\_id: String

session\_thread\_id: String

ID of the session thread this event refers to.

type: :"session.thread\_terminated"

workspace\_id: String



class BetaWebhookSessionUpdatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.updated"

workspace\_id: String



class BetaWebhookVaultArchivedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the vault that triggered the event.

organization\_id: String

type: :"vault.archived"

workspace\_id: String



class BetaWebhookVaultCreatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the vault that triggered the event.

organization\_id: String

type: :"vault.created"

workspace\_id: String



class BetaWebhookVaultCredentialArchivedEventData { id, organization\_id, type, 2 more } 

id: String

ID of the vault credential that triggered the event.

organization\_id: String

type: :"vault\_credential.archived"

vault\_id: String

ID of the vault that owns this credential.

workspace\_id: String



class BetaWebhookVaultCredentialCreatedEventData { id, organization\_id, type, 2 more } 

id: String

ID of the vault credential that triggered the event.

organization\_id: String

type: :"vault\_credential.created"

vault\_id: String

ID of the vault that owns this credential.

workspace\_id: String



class BetaWebhookVaultCredentialDeletedEventData { id, organization\_id, type, 2 more } 

id: String

ID of the vault credential that triggered the event.

organization\_id: String

type: :"vault\_credential.deleted"

vault\_id: String

ID of the vault that owns this credential.

workspace\_id: String



class BetaWebhookVaultCredentialRefreshFailedEventData { id, organization\_id, type, 2 more } 

id: String

ID of the vault credential that triggered the event.

organization\_id: String

type: :"vault\_credential.refresh\_failed"

vault\_id: String

ID of the vault that owns this credential.

workspace\_id: String



class BetaWebhookVaultDeletedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the vault that triggered the event.

organization\_id: String

type: :"vault.deleted"

workspace\_id: String



class UnwrapWebhookEvent { id, created\_at, data, type } 

id: String

Unique event identifier for idempotency.

created\_at: Time

RFC 3339 timestamp when the event occurred.



data: [BetaWebhookEventData](api/beta/webhooks.md)

One of the following:



class BetaWebhookSessionCreatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.created"

workspace\_id: String



class BetaWebhookSessionPendingEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.pending"

workspace\_id: String



class BetaWebhookSessionRunningEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.running"

workspace\_id: String



class BetaWebhookSessionIdledEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.idled"

workspace\_id: String



class BetaWebhookSessionRequiresActionEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.requires\_action"

workspace\_id: String



class BetaWebhookSessionArchivedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.archived"

workspace\_id: String



class BetaWebhookSessionDeletedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.deleted"

workspace\_id: String



class BetaWebhookSessionStatusRescheduledEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.status\_rescheduled"

workspace\_id: String



class BetaWebhookSessionStatusRunStartedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.status\_run\_started"

workspace\_id: String



class BetaWebhookSessionStatusIdledEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.status\_idled"

workspace\_id: String



class BetaWebhookSessionStatusTerminatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.status\_terminated"

workspace\_id: String



class BetaWebhookSessionThreadCreatedEventData { id, organization\_id, session\_thread\_id, 2 more } 

id: String

ID of the session that triggered the event.

organization\_id: String

session\_thread\_id: String

ID of the session thread this event refers to.

type: :"session.thread\_created"

workspace\_id: String



class BetaWebhookSessionThreadIdledEventData { id, organization\_id, session\_thread\_id, 2 more } 

id: String

ID of the session that triggered the event.

organization\_id: String

session\_thread\_id: String

ID of the session thread this event refers to.

type: :"session.thread\_idled"

workspace\_id: String



class BetaWebhookSessionThreadTerminatedEventData { id, organization\_id, session\_thread\_id, 2 more } 

id: String

ID of the session that triggered the event.

organization\_id: String

session\_thread\_id: String

ID of the session thread this event refers to.

type: :"session.thread\_terminated"

workspace\_id: String



class BetaWebhookSessionOutcomeEvaluationEndedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.outcome\_evaluation\_ended"

workspace\_id: String



class BetaWebhookVaultCreatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the vault that triggered the event.

organization\_id: String

type: :"vault.created"

workspace\_id: String



class BetaWebhookVaultArchivedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the vault that triggered the event.

organization\_id: String

type: :"vault.archived"

workspace\_id: String



class BetaWebhookVaultDeletedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the vault that triggered the event.

organization\_id: String

type: :"vault.deleted"

workspace\_id: String



class BetaWebhookVaultCredentialCreatedEventData { id, organization\_id, type, 2 more } 

id: String

ID of the vault credential that triggered the event.

organization\_id: String

type: :"vault\_credential.created"

vault\_id: String

ID of the vault that owns this credential.

workspace\_id: String



class BetaWebhookVaultCredentialArchivedEventData { id, organization\_id, type, 2 more } 

id: String

ID of the vault credential that triggered the event.

organization\_id: String

type: :"vault\_credential.archived"

vault\_id: String

ID of the vault that owns this credential.

workspace\_id: String



class BetaWebhookVaultCredentialDeletedEventData { id, organization\_id, type, 2 more } 

id: String

ID of the vault credential that triggered the event.

organization\_id: String

type: :"vault\_credential.deleted"

vault\_id: String

ID of the vault that owns this credential.

workspace\_id: String



class BetaWebhookVaultCredentialRefreshFailedEventData { id, organization\_id, type, 2 more } 

id: String

ID of the vault credential that triggered the event.

organization\_id: String

type: :"vault\_credential.refresh\_failed"

vault\_id: String

ID of the vault that owns this credential.

workspace\_id: String



class BetaWebhookSessionUpdatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the session that triggered the event.

organization\_id: String

type: :"session.updated"

workspace\_id: String



class BetaWebhookAgentCreatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the agent that triggered the event.

organization\_id: String

type: :"agent.created"

workspace\_id: String



class BetaWebhookAgentArchivedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the agent that triggered the event.

organization\_id: String

type: :"agent.archived"

workspace\_id: String



class BetaWebhookAgentDeletedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the agent that triggered the event.

organization\_id: String

type: :"agent.deleted"

workspace\_id: String



class BetaWebhookDeploymentPausedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment that triggered the event.

organization\_id: String

type: :"deployment.paused"

workspace\_id: String



class BetaWebhookDeploymentRunFailedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment run that triggered the event.

organization\_id: String

type: :"deployment\_run.failed"

workspace\_id: String



class BetaWebhookDeploymentCreatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment that triggered the event.

organization\_id: String

type: :"deployment.created"

workspace\_id: String



class BetaWebhookDeploymentUpdatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment that triggered the event.

organization\_id: String

type: :"deployment.updated"

workspace\_id: String



class BetaWebhookDeploymentUnpausedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment that triggered the event.

organization\_id: String

type: :"deployment.unpaused"

workspace\_id: String



class BetaWebhookAgentUpdatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the agent that triggered the event.

organization\_id: String

type: :"agent.updated"

workspace\_id: String



class BetaWebhookDeploymentArchivedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment that triggered the event.

organization\_id: String

type: :"deployment.archived"

workspace\_id: String



class BetaWebhookDeploymentRunStartedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment run that triggered the event.

organization\_id: String

type: :"deployment\_run.started"

workspace\_id: String



class BetaWebhookDeploymentDeletedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment that triggered the event.

organization\_id: String

type: :"deployment.deleted"

workspace\_id: String



class BetaWebhookDeploymentRunSucceededEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the deployment run that triggered the event.

organization\_id: String

type: :"deployment\_run.succeeded"

workspace\_id: String



class BetaWebhookEnvironmentCreatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the environment that triggered the event.

organization\_id: String

type: :"environment.created"

workspace\_id: String



class BetaWebhookEnvironmentUpdatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the environment that triggered the event.

organization\_id: String

type: :"environment.updated"

workspace\_id: String



class BetaWebhookEnvironmentArchivedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the environment that triggered the event.

organization\_id: String

type: :"environment.archived"

workspace\_id: String



class BetaWebhookEnvironmentDeletedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the environment that triggered the event.

organization\_id: String

type: [BetaWebhookEnvironmentDeletedEventType](api/beta/webhooks.md)

workspace\_id: String



class BetaWebhookMemoryStoreCreatedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the memory store that triggered the event.

organization\_id: String

type: :"memory\_store.created"

workspace\_id: String



class BetaWebhookMemoryStoreArchivedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the memory store that triggered the event.

organization\_id: String

type: :"memory\_store.archived"

workspace\_id: String



class BetaWebhookMemoryStoreDeletedEventData { id, organization\_id, type, workspace\_id } 

id: String

ID of the memory store that triggered the event.

organization\_id: String

type: :"memory\_store.deleted"

workspace\_id: String

type: :event

Object type. Always `event` for webhook payloads.

---

*Copyright © Anthropic. All rights reserved.*
