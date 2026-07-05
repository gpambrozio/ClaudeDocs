# Webhooks

Copy page



Java

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

class BetaWebhookAgentArchivedEventData:

String id

ID of the agent that triggered the event.

String organizationId

JsonValue; type "agent.archived"constant"agent.archived"constant

String workspaceId



class BetaWebhookAgentCreatedEventData:

String id

ID of the agent that triggered the event.

String organizationId

JsonValue; type "agent.created"constant"agent.created"constant

String workspaceId



class BetaWebhookAgentDeletedEventData:

String id

ID of the agent that triggered the event.

String organizationId

JsonValue; type "agent.deleted"constant"agent.deleted"constant

String workspaceId



class BetaWebhookAgentUpdatedEventData:

String id

ID of the agent that triggered the event.

String organizationId

JsonValue; type "agent.updated"constant"agent.updated"constant

String workspaceId



class BetaWebhookDeploymentArchivedEventData:

String id

ID of the deployment that triggered the event.

String organizationId

JsonValue; type "deployment.archived"constant"deployment.archived"constant

String workspaceId



class BetaWebhookDeploymentCreatedEventData:

String id

ID of the deployment that triggered the event.

String organizationId

JsonValue; type "deployment.created"constant"deployment.created"constant

String workspaceId



class BetaWebhookDeploymentDeletedEventData:

String id

ID of the deployment that triggered the event.

String organizationId

JsonValue; type "deployment.deleted"constant"deployment.deleted"constant

String workspaceId



class BetaWebhookDeploymentPausedEventData:

String id

ID of the deployment that triggered the event.

String organizationId

JsonValue; type "deployment.paused"constant"deployment.paused"constant

String workspaceId



class BetaWebhookDeploymentRunFailedEventData:

String id

ID of the deployment run that triggered the event.

String organizationId

JsonValue; type "deployment\_run.failed"constant"deployment\_run.failed"constant

String workspaceId



class BetaWebhookDeploymentRunStartedEventData:

String id

ID of the deployment run that triggered the event.

String organizationId

JsonValue; type "deployment\_run.started"constant"deployment\_run.started"constant

String workspaceId



class BetaWebhookDeploymentRunSucceededEventData:

String id

ID of the deployment run that triggered the event.

String organizationId

JsonValue; type "deployment\_run.succeeded"constant"deployment\_run.succeeded"constant

String workspaceId



class BetaWebhookDeploymentUnpausedEventData:

String id

ID of the deployment that triggered the event.

String organizationId

JsonValue; type "deployment.unpaused"constant"deployment.unpaused"constant

String workspaceId



class BetaWebhookDeploymentUpdatedEventData:

String id

ID of the deployment that triggered the event.

String organizationId

JsonValue; type "deployment.updated"constant"deployment.updated"constant

String workspaceId



class BetaWebhookEnvironmentArchivedEventData:

String id

ID of the environment that triggered the event.

String organizationId

JsonValue; type "environment.archived"constant"environment.archived"constant

String workspaceId



class BetaWebhookEnvironmentCreatedEventData:

String id

ID of the environment that triggered the event.

String organizationId

JsonValue; type "environment.created"constant"environment.created"constant

String workspaceId



class BetaWebhookEnvironmentDeletedEventData:

String id

ID of the environment that triggered the event.

String organizationId

[BetaWebhookEnvironmentDeletedEventType](api/beta/webhooks.md) type

String workspaceId



enum BetaWebhookEnvironmentDeletedEventType:

ENVIRONMENT\_DELETED("environment.deleted")



class BetaWebhookEnvironmentUpdatedEventData:

String id

ID of the environment that triggered the event.

String organizationId

JsonValue; type "environment.updated"constant"environment.updated"constant

String workspaceId



class BetaWebhookEvent:

String id

Unique event identifier for idempotency.

LocalDateTime createdAt

RFC 3339 timestamp when the event occurred.



[BetaWebhookEventData](api/beta/webhooks.md) data

One of the following:



class BetaWebhookSessionCreatedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.created"constant"session.created"constant

String workspaceId



class BetaWebhookSessionPendingEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.pending"constant"session.pending"constant

String workspaceId



class BetaWebhookSessionRunningEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.running"constant"session.running"constant

String workspaceId



class BetaWebhookSessionIdledEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.idled"constant"session.idled"constant

String workspaceId



class BetaWebhookSessionRequiresActionEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.requires\_action"constant"session.requires\_action"constant

String workspaceId



class BetaWebhookSessionArchivedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.archived"constant"session.archived"constant

String workspaceId



class BetaWebhookSessionDeletedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.deleted"constant"session.deleted"constant

String workspaceId



class BetaWebhookSessionStatusRescheduledEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.status\_rescheduled"constant"session.status\_rescheduled"constant

String workspaceId



class BetaWebhookSessionStatusRunStartedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.status\_run\_started"constant"session.status\_run\_started"constant

String workspaceId



class BetaWebhookSessionStatusIdledEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.status\_idled"constant"session.status\_idled"constant

String workspaceId



class BetaWebhookSessionStatusTerminatedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.status\_terminated"constant"session.status\_terminated"constant

String workspaceId



class BetaWebhookSessionThreadCreatedEventData:

String id

ID of the session that triggered the event.

String organizationId

String sessionThreadId

ID of the session thread this event refers to.

JsonValue; type "session.thread\_created"constant"session.thread\_created"constant

String workspaceId



class BetaWebhookSessionThreadIdledEventData:

String id

ID of the session that triggered the event.

String organizationId

String sessionThreadId

ID of the session thread this event refers to.

JsonValue; type "session.thread\_idled"constant"session.thread\_idled"constant

String workspaceId



class BetaWebhookSessionThreadTerminatedEventData:

String id

ID of the session that triggered the event.

String organizationId

String sessionThreadId

ID of the session thread this event refers to.

JsonValue; type "session.thread\_terminated"constant"session.thread\_terminated"constant

String workspaceId



class BetaWebhookSessionOutcomeEvaluationEndedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.outcome\_evaluation\_ended"constant"session.outcome\_evaluation\_ended"constant

String workspaceId



class BetaWebhookVaultCreatedEventData:

String id

ID of the vault that triggered the event.

String organizationId

JsonValue; type "vault.created"constant"vault.created"constant

String workspaceId



class BetaWebhookVaultArchivedEventData:

String id

ID of the vault that triggered the event.

String organizationId

JsonValue; type "vault.archived"constant"vault.archived"constant

String workspaceId



class BetaWebhookVaultDeletedEventData:

String id

ID of the vault that triggered the event.

String organizationId

JsonValue; type "vault.deleted"constant"vault.deleted"constant

String workspaceId



class BetaWebhookVaultCredentialCreatedEventData:

String id

ID of the vault credential that triggered the event.

String organizationId

JsonValue; type "vault\_credential.created"constant"vault\_credential.created"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId



class BetaWebhookVaultCredentialArchivedEventData:

String id

ID of the vault credential that triggered the event.

String organizationId

JsonValue; type "vault\_credential.archived"constant"vault\_credential.archived"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId



class BetaWebhookVaultCredentialDeletedEventData:

String id

ID of the vault credential that triggered the event.

String organizationId

JsonValue; type "vault\_credential.deleted"constant"vault\_credential.deleted"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId



class BetaWebhookVaultCredentialRefreshFailedEventData:

String id

ID of the vault credential that triggered the event.

String organizationId

JsonValue; type "vault\_credential.refresh\_failed"constant"vault\_credential.refresh\_failed"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId



class BetaWebhookSessionUpdatedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.updated"constant"session.updated"constant

String workspaceId



class BetaWebhookAgentCreatedEventData:

String id

ID of the agent that triggered the event.

String organizationId

JsonValue; type "agent.created"constant"agent.created"constant

String workspaceId



class BetaWebhookAgentArchivedEventData:

String id

ID of the agent that triggered the event.

String organizationId

JsonValue; type "agent.archived"constant"agent.archived"constant

String workspaceId



class BetaWebhookAgentDeletedEventData:

String id

ID of the agent that triggered the event.

String organizationId

JsonValue; type "agent.deleted"constant"agent.deleted"constant

String workspaceId



class BetaWebhookDeploymentPausedEventData:

String id

ID of the deployment that triggered the event.

String organizationId

JsonValue; type "deployment.paused"constant"deployment.paused"constant

String workspaceId



class BetaWebhookDeploymentRunFailedEventData:

String id

ID of the deployment run that triggered the event.

String organizationId

JsonValue; type "deployment\_run.failed"constant"deployment\_run.failed"constant

String workspaceId



class BetaWebhookDeploymentCreatedEventData:

String id

ID of the deployment that triggered the event.

String organizationId

JsonValue; type "deployment.created"constant"deployment.created"constant

String workspaceId



class BetaWebhookDeploymentUpdatedEventData:

String id

ID of the deployment that triggered the event.

String organizationId

JsonValue; type "deployment.updated"constant"deployment.updated"constant

String workspaceId



class BetaWebhookDeploymentUnpausedEventData:

String id

ID of the deployment that triggered the event.

String organizationId

JsonValue; type "deployment.unpaused"constant"deployment.unpaused"constant

String workspaceId



class BetaWebhookAgentUpdatedEventData:

String id

ID of the agent that triggered the event.

String organizationId

JsonValue; type "agent.updated"constant"agent.updated"constant

String workspaceId



class BetaWebhookDeploymentArchivedEventData:

String id

ID of the deployment that triggered the event.

String organizationId

JsonValue; type "deployment.archived"constant"deployment.archived"constant

String workspaceId



class BetaWebhookDeploymentRunStartedEventData:

String id

ID of the deployment run that triggered the event.

String organizationId

JsonValue; type "deployment\_run.started"constant"deployment\_run.started"constant

String workspaceId



class BetaWebhookDeploymentDeletedEventData:

String id

ID of the deployment that triggered the event.

String organizationId

JsonValue; type "deployment.deleted"constant"deployment.deleted"constant

String workspaceId



class BetaWebhookDeploymentRunSucceededEventData:

String id

ID of the deployment run that triggered the event.

String organizationId

JsonValue; type "deployment\_run.succeeded"constant"deployment\_run.succeeded"constant

String workspaceId



class BetaWebhookEnvironmentCreatedEventData:

String id

ID of the environment that triggered the event.

String organizationId

JsonValue; type "environment.created"constant"environment.created"constant

String workspaceId



class BetaWebhookEnvironmentUpdatedEventData:

String id

ID of the environment that triggered the event.

String organizationId

JsonValue; type "environment.updated"constant"environment.updated"constant

String workspaceId



class BetaWebhookEnvironmentArchivedEventData:

String id

ID of the environment that triggered the event.

String organizationId

JsonValue; type "environment.archived"constant"environment.archived"constant

String workspaceId



class BetaWebhookEnvironmentDeletedEventData:

String id

ID of the environment that triggered the event.

String organizationId

[BetaWebhookEnvironmentDeletedEventType](api/beta/webhooks.md) type

String workspaceId



class BetaWebhookMemoryStoreCreatedEventData:

String id

ID of the memory store that triggered the event.

String organizationId

JsonValue; type "memory\_store.created"constant"memory\_store.created"constant

String workspaceId



class BetaWebhookMemoryStoreArchivedEventData:

String id

ID of the memory store that triggered the event.

String organizationId

JsonValue; type "memory\_store.archived"constant"memory\_store.archived"constant

String workspaceId



class BetaWebhookMemoryStoreDeletedEventData:

String id

ID of the memory store that triggered the event.

String organizationId

JsonValue; type "memory\_store.deleted"constant"memory\_store.deleted"constant

String workspaceId

JsonValue; type "event"constant"event"constant

Object type. Always `event` for webhook payloads.



class BetaWebhookEventData: A class that can be one of several variants.union 



class BetaWebhookSessionCreatedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.created"constant"session.created"constant

String workspaceId



class BetaWebhookSessionPendingEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.pending"constant"session.pending"constant

String workspaceId



class BetaWebhookSessionRunningEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.running"constant"session.running"constant

String workspaceId



class BetaWebhookSessionIdledEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.idled"constant"session.idled"constant

String workspaceId



class BetaWebhookSessionRequiresActionEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.requires\_action"constant"session.requires\_action"constant

String workspaceId



class BetaWebhookSessionArchivedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.archived"constant"session.archived"constant

String workspaceId



class BetaWebhookSessionDeletedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.deleted"constant"session.deleted"constant

String workspaceId



class BetaWebhookSessionStatusRescheduledEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.status\_rescheduled"constant"session.status\_rescheduled"constant

String workspaceId



class BetaWebhookSessionStatusRunStartedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.status\_run\_started"constant"session.status\_run\_started"constant

String workspaceId



class BetaWebhookSessionStatusIdledEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.status\_idled"constant"session.status\_idled"constant

String workspaceId



class BetaWebhookSessionStatusTerminatedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.status\_terminated"constant"session.status\_terminated"constant

String workspaceId



class BetaWebhookSessionThreadCreatedEventData:

String id

ID of the session that triggered the event.

String organizationId

String sessionThreadId

ID of the session thread this event refers to.

JsonValue; type "session.thread\_created"constant"session.thread\_created"constant

String workspaceId



class BetaWebhookSessionThreadIdledEventData:

String id

ID of the session that triggered the event.

String organizationId

String sessionThreadId

ID of the session thread this event refers to.

JsonValue; type "session.thread\_idled"constant"session.thread\_idled"constant

String workspaceId



class BetaWebhookSessionThreadTerminatedEventData:

String id

ID of the session that triggered the event.

String organizationId

String sessionThreadId

ID of the session thread this event refers to.

JsonValue; type "session.thread\_terminated"constant"session.thread\_terminated"constant

String workspaceId



class BetaWebhookSessionOutcomeEvaluationEndedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.outcome\_evaluation\_ended"constant"session.outcome\_evaluation\_ended"constant

String workspaceId



class BetaWebhookVaultCreatedEventData:

String id

ID of the vault that triggered the event.

String organizationId

JsonValue; type "vault.created"constant"vault.created"constant

String workspaceId



class BetaWebhookVaultArchivedEventData:

String id

ID of the vault that triggered the event.

String organizationId

JsonValue; type "vault.archived"constant"vault.archived"constant

String workspaceId



class BetaWebhookVaultDeletedEventData:

String id

ID of the vault that triggered the event.

String organizationId

JsonValue; type "vault.deleted"constant"vault.deleted"constant

String workspaceId



class BetaWebhookVaultCredentialCreatedEventData:

String id

ID of the vault credential that triggered the event.

String organizationId

JsonValue; type "vault\_credential.created"constant"vault\_credential.created"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId



class BetaWebhookVaultCredentialArchivedEventData:

String id

ID of the vault credential that triggered the event.

String organizationId

JsonValue; type "vault\_credential.archived"constant"vault\_credential.archived"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId



class BetaWebhookVaultCredentialDeletedEventData:

String id

ID of the vault credential that triggered the event.

String organizationId

JsonValue; type "vault\_credential.deleted"constant"vault\_credential.deleted"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId



class BetaWebhookVaultCredentialRefreshFailedEventData:

String id

ID of the vault credential that triggered the event.

String organizationId

JsonValue; type "vault\_credential.refresh\_failed"constant"vault\_credential.refresh\_failed"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId



class BetaWebhookSessionUpdatedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.updated"constant"session.updated"constant

String workspaceId



class BetaWebhookAgentCreatedEventData:

String id

ID of the agent that triggered the event.

String organizationId

JsonValue; type "agent.created"constant"agent.created"constant

String workspaceId



class BetaWebhookAgentArchivedEventData:

String id

ID of the agent that triggered the event.

String organizationId

JsonValue; type "agent.archived"constant"agent.archived"constant

String workspaceId



class BetaWebhookAgentDeletedEventData:

String id

ID of the agent that triggered the event.

String organizationId

JsonValue; type "agent.deleted"constant"agent.deleted"constant

String workspaceId



class BetaWebhookDeploymentPausedEventData:

String id

ID of the deployment that triggered the event.

String organizationId

JsonValue; type "deployment.paused"constant"deployment.paused"constant

String workspaceId



class BetaWebhookDeploymentRunFailedEventData:

String id

ID of the deployment run that triggered the event.

String organizationId

JsonValue; type "deployment\_run.failed"constant"deployment\_run.failed"constant

String workspaceId



class BetaWebhookDeploymentCreatedEventData:

String id

ID of the deployment that triggered the event.

String organizationId

JsonValue; type "deployment.created"constant"deployment.created"constant

String workspaceId



class BetaWebhookDeploymentUpdatedEventData:

String id

ID of the deployment that triggered the event.

String organizationId

JsonValue; type "deployment.updated"constant"deployment.updated"constant

String workspaceId



class BetaWebhookDeploymentUnpausedEventData:

String id

ID of the deployment that triggered the event.

String organizationId

JsonValue; type "deployment.unpaused"constant"deployment.unpaused"constant

String workspaceId



class BetaWebhookAgentUpdatedEventData:

String id

ID of the agent that triggered the event.

String organizationId

JsonValue; type "agent.updated"constant"agent.updated"constant

String workspaceId



class BetaWebhookDeploymentArchivedEventData:

String id

ID of the deployment that triggered the event.

String organizationId

JsonValue; type "deployment.archived"constant"deployment.archived"constant

String workspaceId



class BetaWebhookDeploymentRunStartedEventData:

String id

ID of the deployment run that triggered the event.

String organizationId

JsonValue; type "deployment\_run.started"constant"deployment\_run.started"constant

String workspaceId



class BetaWebhookDeploymentDeletedEventData:

String id

ID of the deployment that triggered the event.

String organizationId

JsonValue; type "deployment.deleted"constant"deployment.deleted"constant

String workspaceId



class BetaWebhookDeploymentRunSucceededEventData:

String id

ID of the deployment run that triggered the event.

String organizationId

JsonValue; type "deployment\_run.succeeded"constant"deployment\_run.succeeded"constant

String workspaceId



class BetaWebhookEnvironmentCreatedEventData:

String id

ID of the environment that triggered the event.

String organizationId

JsonValue; type "environment.created"constant"environment.created"constant

String workspaceId



class BetaWebhookEnvironmentUpdatedEventData:

String id

ID of the environment that triggered the event.

String organizationId

JsonValue; type "environment.updated"constant"environment.updated"constant

String workspaceId



class BetaWebhookEnvironmentArchivedEventData:

String id

ID of the environment that triggered the event.

String organizationId

JsonValue; type "environment.archived"constant"environment.archived"constant

String workspaceId



class BetaWebhookEnvironmentDeletedEventData:

String id

ID of the environment that triggered the event.

String organizationId

[BetaWebhookEnvironmentDeletedEventType](api/beta/webhooks.md) type

String workspaceId



class BetaWebhookMemoryStoreCreatedEventData:

String id

ID of the memory store that triggered the event.

String organizationId

JsonValue; type "memory\_store.created"constant"memory\_store.created"constant

String workspaceId



class BetaWebhookMemoryStoreArchivedEventData:

String id

ID of the memory store that triggered the event.

String organizationId

JsonValue; type "memory\_store.archived"constant"memory\_store.archived"constant

String workspaceId



class BetaWebhookMemoryStoreDeletedEventData:

String id

ID of the memory store that triggered the event.

String organizationId

JsonValue; type "memory\_store.deleted"constant"memory\_store.deleted"constant

String workspaceId



class BetaWebhookMemoryStoreArchivedEventData:

String id

ID of the memory store that triggered the event.

String organizationId

JsonValue; type "memory\_store.archived"constant"memory\_store.archived"constant

String workspaceId



class BetaWebhookMemoryStoreCreatedEventData:

String id

ID of the memory store that triggered the event.

String organizationId

JsonValue; type "memory\_store.created"constant"memory\_store.created"constant

String workspaceId



class BetaWebhookMemoryStoreDeletedEventData:

String id

ID of the memory store that triggered the event.

String organizationId

JsonValue; type "memory\_store.deleted"constant"memory\_store.deleted"constant

String workspaceId



class BetaWebhookSessionArchivedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.archived"constant"session.archived"constant

String workspaceId



class BetaWebhookSessionCreatedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.created"constant"session.created"constant

String workspaceId



class BetaWebhookSessionDeletedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.deleted"constant"session.deleted"constant

String workspaceId



class BetaWebhookSessionIdledEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.idled"constant"session.idled"constant

String workspaceId



class BetaWebhookSessionOutcomeEvaluationEndedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.outcome\_evaluation\_ended"constant"session.outcome\_evaluation\_ended"constant

String workspaceId



class BetaWebhookSessionPendingEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.pending"constant"session.pending"constant

String workspaceId



class BetaWebhookSessionRequiresActionEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.requires\_action"constant"session.requires\_action"constant

String workspaceId



class BetaWebhookSessionRunningEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.running"constant"session.running"constant

String workspaceId



class BetaWebhookSessionStatusIdledEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.status\_idled"constant"session.status\_idled"constant

String workspaceId



class BetaWebhookSessionStatusRescheduledEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.status\_rescheduled"constant"session.status\_rescheduled"constant

String workspaceId



class BetaWebhookSessionStatusRunStartedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.status\_run\_started"constant"session.status\_run\_started"constant

String workspaceId



class BetaWebhookSessionStatusTerminatedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.status\_terminated"constant"session.status\_terminated"constant

String workspaceId



class BetaWebhookSessionThreadCreatedEventData:

String id

ID of the session that triggered the event.

String organizationId

String sessionThreadId

ID of the session thread this event refers to.

JsonValue; type "session.thread\_created"constant"session.thread\_created"constant

String workspaceId



class BetaWebhookSessionThreadIdledEventData:

String id

ID of the session that triggered the event.

String organizationId

String sessionThreadId

ID of the session thread this event refers to.

JsonValue; type "session.thread\_idled"constant"session.thread\_idled"constant

String workspaceId



class BetaWebhookSessionThreadTerminatedEventData:

String id

ID of the session that triggered the event.

String organizationId

String sessionThreadId

ID of the session thread this event refers to.

JsonValue; type "session.thread\_terminated"constant"session.thread\_terminated"constant

String workspaceId



class BetaWebhookSessionUpdatedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.updated"constant"session.updated"constant

String workspaceId



class BetaWebhookVaultArchivedEventData:

String id

ID of the vault that triggered the event.

String organizationId

JsonValue; type "vault.archived"constant"vault.archived"constant

String workspaceId



class BetaWebhookVaultCreatedEventData:

String id

ID of the vault that triggered the event.

String organizationId

JsonValue; type "vault.created"constant"vault.created"constant

String workspaceId



class BetaWebhookVaultCredentialArchivedEventData:

String id

ID of the vault credential that triggered the event.

String organizationId

JsonValue; type "vault\_credential.archived"constant"vault\_credential.archived"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId



class BetaWebhookVaultCredentialCreatedEventData:

String id

ID of the vault credential that triggered the event.

String organizationId

JsonValue; type "vault\_credential.created"constant"vault\_credential.created"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId



class BetaWebhookVaultCredentialDeletedEventData:

String id

ID of the vault credential that triggered the event.

String organizationId

JsonValue; type "vault\_credential.deleted"constant"vault\_credential.deleted"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId



class BetaWebhookVaultCredentialRefreshFailedEventData:

String id

ID of the vault credential that triggered the event.

String organizationId

JsonValue; type "vault\_credential.refresh\_failed"constant"vault\_credential.refresh\_failed"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId



class BetaWebhookVaultDeletedEventData:

String id

ID of the vault that triggered the event.

String organizationId

JsonValue; type "vault.deleted"constant"vault.deleted"constant

String workspaceId



class UnwrapWebhookEvent:

String id

Unique event identifier for idempotency.

LocalDateTime createdAt

RFC 3339 timestamp when the event occurred.



[BetaWebhookEventData](api/beta/webhooks.md) data

One of the following:



class BetaWebhookSessionCreatedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.created"constant"session.created"constant

String workspaceId



class BetaWebhookSessionPendingEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.pending"constant"session.pending"constant

String workspaceId



class BetaWebhookSessionRunningEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.running"constant"session.running"constant

String workspaceId



class BetaWebhookSessionIdledEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.idled"constant"session.idled"constant

String workspaceId



class BetaWebhookSessionRequiresActionEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.requires\_action"constant"session.requires\_action"constant

String workspaceId



class BetaWebhookSessionArchivedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.archived"constant"session.archived"constant

String workspaceId



class BetaWebhookSessionDeletedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.deleted"constant"session.deleted"constant

String workspaceId



class BetaWebhookSessionStatusRescheduledEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.status\_rescheduled"constant"session.status\_rescheduled"constant

String workspaceId



class BetaWebhookSessionStatusRunStartedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.status\_run\_started"constant"session.status\_run\_started"constant

String workspaceId



class BetaWebhookSessionStatusIdledEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.status\_idled"constant"session.status\_idled"constant

String workspaceId



class BetaWebhookSessionStatusTerminatedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.status\_terminated"constant"session.status\_terminated"constant

String workspaceId



class BetaWebhookSessionThreadCreatedEventData:

String id

ID of the session that triggered the event.

String organizationId

String sessionThreadId

ID of the session thread this event refers to.

JsonValue; type "session.thread\_created"constant"session.thread\_created"constant

String workspaceId



class BetaWebhookSessionThreadIdledEventData:

String id

ID of the session that triggered the event.

String organizationId

String sessionThreadId

ID of the session thread this event refers to.

JsonValue; type "session.thread\_idled"constant"session.thread\_idled"constant

String workspaceId



class BetaWebhookSessionThreadTerminatedEventData:

String id

ID of the session that triggered the event.

String organizationId

String sessionThreadId

ID of the session thread this event refers to.

JsonValue; type "session.thread\_terminated"constant"session.thread\_terminated"constant

String workspaceId



class BetaWebhookSessionOutcomeEvaluationEndedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.outcome\_evaluation\_ended"constant"session.outcome\_evaluation\_ended"constant

String workspaceId



class BetaWebhookVaultCreatedEventData:

String id

ID of the vault that triggered the event.

String organizationId

JsonValue; type "vault.created"constant"vault.created"constant

String workspaceId



class BetaWebhookVaultArchivedEventData:

String id

ID of the vault that triggered the event.

String organizationId

JsonValue; type "vault.archived"constant"vault.archived"constant

String workspaceId



class BetaWebhookVaultDeletedEventData:

String id

ID of the vault that triggered the event.

String organizationId

JsonValue; type "vault.deleted"constant"vault.deleted"constant

String workspaceId



class BetaWebhookVaultCredentialCreatedEventData:

String id

ID of the vault credential that triggered the event.

String organizationId

JsonValue; type "vault\_credential.created"constant"vault\_credential.created"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId



class BetaWebhookVaultCredentialArchivedEventData:

String id

ID of the vault credential that triggered the event.

String organizationId

JsonValue; type "vault\_credential.archived"constant"vault\_credential.archived"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId



class BetaWebhookVaultCredentialDeletedEventData:

String id

ID of the vault credential that triggered the event.

String organizationId

JsonValue; type "vault\_credential.deleted"constant"vault\_credential.deleted"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId



class BetaWebhookVaultCredentialRefreshFailedEventData:

String id

ID of the vault credential that triggered the event.

String organizationId

JsonValue; type "vault\_credential.refresh\_failed"constant"vault\_credential.refresh\_failed"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId



class BetaWebhookSessionUpdatedEventData:

String id

ID of the session that triggered the event.

String organizationId

JsonValue; type "session.updated"constant"session.updated"constant

String workspaceId



class BetaWebhookAgentCreatedEventData:

String id

ID of the agent that triggered the event.

String organizationId

JsonValue; type "agent.created"constant"agent.created"constant

String workspaceId



class BetaWebhookAgentArchivedEventData:

String id

ID of the agent that triggered the event.

String organizationId

JsonValue; type "agent.archived"constant"agent.archived"constant

String workspaceId



class BetaWebhookAgentDeletedEventData:

String id

ID of the agent that triggered the event.

String organizationId

JsonValue; type "agent.deleted"constant"agent.deleted"constant

String workspaceId



class BetaWebhookDeploymentPausedEventData:

String id

ID of the deployment that triggered the event.

String organizationId

JsonValue; type "deployment.paused"constant"deployment.paused"constant

String workspaceId



class BetaWebhookDeploymentRunFailedEventData:

String id

ID of the deployment run that triggered the event.

String organizationId

JsonValue; type "deployment\_run.failed"constant"deployment\_run.failed"constant

String workspaceId



class BetaWebhookDeploymentCreatedEventData:

String id

ID of the deployment that triggered the event.

String organizationId

JsonValue; type "deployment.created"constant"deployment.created"constant

String workspaceId



class BetaWebhookDeploymentUpdatedEventData:

String id

ID of the deployment that triggered the event.

String organizationId

JsonValue; type "deployment.updated"constant"deployment.updated"constant

String workspaceId



class BetaWebhookDeploymentUnpausedEventData:

String id

ID of the deployment that triggered the event.

String organizationId

JsonValue; type "deployment.unpaused"constant"deployment.unpaused"constant

String workspaceId



class BetaWebhookAgentUpdatedEventData:

String id

ID of the agent that triggered the event.

String organizationId

JsonValue; type "agent.updated"constant"agent.updated"constant

String workspaceId



class BetaWebhookDeploymentArchivedEventData:

String id

ID of the deployment that triggered the event.

String organizationId

JsonValue; type "deployment.archived"constant"deployment.archived"constant

String workspaceId



class BetaWebhookDeploymentRunStartedEventData:

String id

ID of the deployment run that triggered the event.

String organizationId

JsonValue; type "deployment\_run.started"constant"deployment\_run.started"constant

String workspaceId



class BetaWebhookDeploymentDeletedEventData:

String id

ID of the deployment that triggered the event.

String organizationId

JsonValue; type "deployment.deleted"constant"deployment.deleted"constant

String workspaceId



class BetaWebhookDeploymentRunSucceededEventData:

String id

ID of the deployment run that triggered the event.

String organizationId

JsonValue; type "deployment\_run.succeeded"constant"deployment\_run.succeeded"constant

String workspaceId



class BetaWebhookEnvironmentCreatedEventData:

String id

ID of the environment that triggered the event.

String organizationId

JsonValue; type "environment.created"constant"environment.created"constant

String workspaceId



class BetaWebhookEnvironmentUpdatedEventData:

String id

ID of the environment that triggered the event.

String organizationId

JsonValue; type "environment.updated"constant"environment.updated"constant

String workspaceId



class BetaWebhookEnvironmentArchivedEventData:

String id

ID of the environment that triggered the event.

String organizationId

JsonValue; type "environment.archived"constant"environment.archived"constant

String workspaceId



class BetaWebhookEnvironmentDeletedEventData:

String id

ID of the environment that triggered the event.

String organizationId

[BetaWebhookEnvironmentDeletedEventType](api/beta/webhooks.md) type

String workspaceId



class BetaWebhookMemoryStoreCreatedEventData:

String id

ID of the memory store that triggered the event.

String organizationId

JsonValue; type "memory\_store.created"constant"memory\_store.created"constant

String workspaceId



class BetaWebhookMemoryStoreArchivedEventData:

String id

ID of the memory store that triggered the event.

String organizationId

JsonValue; type "memory\_store.archived"constant"memory\_store.archived"constant

String workspaceId



class BetaWebhookMemoryStoreDeletedEventData:

String id

ID of the memory store that triggered the event.

String organizationId

JsonValue; type "memory\_store.deleted"constant"memory\_store.deleted"constant

String workspaceId

JsonValue; type "event"constant"event"constant

Object type. Always `event` for webhook payloads.

---

*Copyright © Anthropic. All rights reserved.*
