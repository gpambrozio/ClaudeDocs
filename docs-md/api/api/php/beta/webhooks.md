# Webhooks

Copy page



PHP

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

[BetaWebhookAgentArchivedEventData](api/beta/webhooks.md)

string id

ID of the agent that triggered the event.

string organizationID

"agent.archived" type

string workspaceID



[BetaWebhookAgentCreatedEventData](api/beta/webhooks.md)

string id

ID of the agent that triggered the event.

string organizationID

"agent.created" type

string workspaceID



[BetaWebhookAgentDeletedEventData](api/beta/webhooks.md)

string id

ID of the agent that triggered the event.

string organizationID

"agent.deleted" type

string workspaceID



[BetaWebhookAgentUpdatedEventData](api/beta/webhooks.md)

string id

ID of the agent that triggered the event.

string organizationID

"agent.updated" type

string workspaceID



[BetaWebhookDeploymentArchivedEventData](api/beta/webhooks.md)

string id

ID of the deployment that triggered the event.

string organizationID

"deployment.archived" type

string workspaceID



[BetaWebhookDeploymentCreatedEventData](api/beta/webhooks.md)

string id

ID of the deployment that triggered the event.

string organizationID

"deployment.created" type

string workspaceID



[BetaWebhookDeploymentDeletedEventData](api/beta/webhooks.md)

string id

ID of the deployment that triggered the event.

string organizationID

"deployment.deleted" type

string workspaceID



[BetaWebhookDeploymentPausedEventData](api/beta/webhooks.md)

string id

ID of the deployment that triggered the event.

string organizationID

"deployment.paused" type

string workspaceID



[BetaWebhookDeploymentRunFailedEventData](api/beta/webhooks.md)

string id

ID of the deployment run that triggered the event.

string organizationID

"deployment\_run.failed" type

string workspaceID



[BetaWebhookDeploymentRunStartedEventData](api/beta/webhooks.md)

string id

ID of the deployment run that triggered the event.

string organizationID

"deployment\_run.started" type

string workspaceID



[BetaWebhookDeploymentRunSucceededEventData](api/beta/webhooks.md)

string id

ID of the deployment run that triggered the event.

string organizationID

"deployment\_run.succeeded" type

string workspaceID



[BetaWebhookDeploymentUnpausedEventData](api/beta/webhooks.md)

string id

ID of the deployment that triggered the event.

string organizationID

"deployment.unpaused" type

string workspaceID



[BetaWebhookDeploymentUpdatedEventData](api/beta/webhooks.md)

string id

ID of the deployment that triggered the event.

string organizationID

"deployment.updated" type

string workspaceID



[BetaWebhookEnvironmentArchivedEventData](api/beta/webhooks.md)

string id

ID of the environment that triggered the event.

string organizationID

"environment.archived" type

string workspaceID



[BetaWebhookEnvironmentCreatedEventData](api/beta/webhooks.md)

string id

ID of the environment that triggered the event.

string organizationID

"environment.created" type

string workspaceID



[BetaWebhookEnvironmentDeletedEventData](api/beta/webhooks.md)

string id

ID of the environment that triggered the event.

string organizationID

[BetaWebhookEnvironmentDeletedEventType](api/beta/webhooks.md) type

string workspaceID

[BetaWebhookEnvironmentDeletedEventType](api/beta/webhooks.md)



[BetaWebhookEnvironmentUpdatedEventData](api/beta/webhooks.md)

string id

ID of the environment that triggered the event.

string organizationID

"environment.updated" type

string workspaceID



[BetaWebhookEvent](api/beta/webhooks.md)

string id

Unique event identifier for idempotency.

\Datetime createdAt

RFC 3339 timestamp when the event occurred.

[BetaWebhookEventData](api/beta/webhooks.md) data

"event" type

Object type. Always `event` for webhook payloads.



[BetaWebhookEventData](api/beta/webhooks.md)

One of the following:



[BetaWebhookSessionCreatedEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.created" type

string workspaceID



[BetaWebhookSessionPendingEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.pending" type

string workspaceID



[BetaWebhookSessionRunningEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.running" type

string workspaceID



[BetaWebhookSessionIdledEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.idled" type

string workspaceID



[BetaWebhookSessionRequiresActionEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.requires\_action" type

string workspaceID



[BetaWebhookSessionArchivedEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.archived" type

string workspaceID



[BetaWebhookSessionDeletedEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.deleted" type

string workspaceID



[BetaWebhookSessionStatusRescheduledEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.status\_rescheduled" type

string workspaceID



[BetaWebhookSessionStatusRunStartedEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.status\_run\_started" type

string workspaceID



[BetaWebhookSessionStatusIdledEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.status\_idled" type

string workspaceID



[BetaWebhookSessionStatusTerminatedEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.status\_terminated" type

string workspaceID



[BetaWebhookSessionThreadCreatedEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

string sessionThreadID

ID of the session thread this event refers to.

"session.thread\_created" type

string workspaceID



[BetaWebhookSessionThreadIdledEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

string sessionThreadID

ID of the session thread this event refers to.

"session.thread\_idled" type

string workspaceID



[BetaWebhookSessionThreadTerminatedEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

string sessionThreadID

ID of the session thread this event refers to.

"session.thread\_terminated" type

string workspaceID



[BetaWebhookSessionOutcomeEvaluationEndedEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.outcome\_evaluation\_ended" type

string workspaceID



[BetaWebhookVaultCreatedEventData](api/beta/webhooks.md)

string id

ID of the vault that triggered the event.

string organizationID

"vault.created" type

string workspaceID



[BetaWebhookVaultArchivedEventData](api/beta/webhooks.md)

string id

ID of the vault that triggered the event.

string organizationID

"vault.archived" type

string workspaceID



[BetaWebhookVaultDeletedEventData](api/beta/webhooks.md)

string id

ID of the vault that triggered the event.

string organizationID

"vault.deleted" type

string workspaceID



[BetaWebhookVaultCredentialCreatedEventData](api/beta/webhooks.md)

string id

ID of the vault credential that triggered the event.

string organizationID

"vault\_credential.created" type

string vaultID

ID of the vault that owns this credential.

string workspaceID



[BetaWebhookVaultCredentialArchivedEventData](api/beta/webhooks.md)

string id

ID of the vault credential that triggered the event.

string organizationID

"vault\_credential.archived" type

string vaultID

ID of the vault that owns this credential.

string workspaceID



[BetaWebhookVaultCredentialDeletedEventData](api/beta/webhooks.md)

string id

ID of the vault credential that triggered the event.

string organizationID

"vault\_credential.deleted" type

string vaultID

ID of the vault that owns this credential.

string workspaceID



[BetaWebhookVaultCredentialRefreshFailedEventData](api/beta/webhooks.md)

string id

ID of the vault credential that triggered the event.

string organizationID

"vault\_credential.refresh\_failed" type

string vaultID

ID of the vault that owns this credential.

string workspaceID



[BetaWebhookSessionUpdatedEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.updated" type

string workspaceID



[BetaWebhookAgentCreatedEventData](api/beta/webhooks.md)

string id

ID of the agent that triggered the event.

string organizationID

"agent.created" type

string workspaceID



[BetaWebhookAgentArchivedEventData](api/beta/webhooks.md)

string id

ID of the agent that triggered the event.

string organizationID

"agent.archived" type

string workspaceID



[BetaWebhookAgentDeletedEventData](api/beta/webhooks.md)

string id

ID of the agent that triggered the event.

string organizationID

"agent.deleted" type

string workspaceID



[BetaWebhookDeploymentPausedEventData](api/beta/webhooks.md)

string id

ID of the deployment that triggered the event.

string organizationID

"deployment.paused" type

string workspaceID



[BetaWebhookDeploymentRunFailedEventData](api/beta/webhooks.md)

string id

ID of the deployment run that triggered the event.

string organizationID

"deployment\_run.failed" type

string workspaceID



[BetaWebhookDeploymentCreatedEventData](api/beta/webhooks.md)

string id

ID of the deployment that triggered the event.

string organizationID

"deployment.created" type

string workspaceID



[BetaWebhookDeploymentUpdatedEventData](api/beta/webhooks.md)

string id

ID of the deployment that triggered the event.

string organizationID

"deployment.updated" type

string workspaceID



[BetaWebhookDeploymentUnpausedEventData](api/beta/webhooks.md)

string id

ID of the deployment that triggered the event.

string organizationID

"deployment.unpaused" type

string workspaceID



[BetaWebhookAgentUpdatedEventData](api/beta/webhooks.md)

string id

ID of the agent that triggered the event.

string organizationID

"agent.updated" type

string workspaceID



[BetaWebhookDeploymentArchivedEventData](api/beta/webhooks.md)

string id

ID of the deployment that triggered the event.

string organizationID

"deployment.archived" type

string workspaceID



[BetaWebhookDeploymentRunStartedEventData](api/beta/webhooks.md)

string id

ID of the deployment run that triggered the event.

string organizationID

"deployment\_run.started" type

string workspaceID



[BetaWebhookDeploymentDeletedEventData](api/beta/webhooks.md)

string id

ID of the deployment that triggered the event.

string organizationID

"deployment.deleted" type

string workspaceID



[BetaWebhookDeploymentRunSucceededEventData](api/beta/webhooks.md)

string id

ID of the deployment run that triggered the event.

string organizationID

"deployment\_run.succeeded" type

string workspaceID



[BetaWebhookEnvironmentCreatedEventData](api/beta/webhooks.md)

string id

ID of the environment that triggered the event.

string organizationID

"environment.created" type

string workspaceID



[BetaWebhookEnvironmentUpdatedEventData](api/beta/webhooks.md)

string id

ID of the environment that triggered the event.

string organizationID

"environment.updated" type

string workspaceID



[BetaWebhookEnvironmentArchivedEventData](api/beta/webhooks.md)

string id

ID of the environment that triggered the event.

string organizationID

"environment.archived" type

string workspaceID



[BetaWebhookEnvironmentDeletedEventData](api/beta/webhooks.md)

string id

ID of the environment that triggered the event.

string organizationID

[BetaWebhookEnvironmentDeletedEventType](api/beta/webhooks.md) type

string workspaceID



[BetaWebhookMemoryStoreCreatedEventData](api/beta/webhooks.md)

string id

ID of the memory store that triggered the event.

string organizationID

"memory\_store.created" type

string workspaceID



[BetaWebhookMemoryStoreArchivedEventData](api/beta/webhooks.md)

string id

ID of the memory store that triggered the event.

string organizationID

"memory\_store.archived" type

string workspaceID



[BetaWebhookMemoryStoreDeletedEventData](api/beta/webhooks.md)

string id

ID of the memory store that triggered the event.

string organizationID

"memory\_store.deleted" type

string workspaceID



[BetaWebhookMemoryStoreArchivedEventData](api/beta/webhooks.md)

string id

ID of the memory store that triggered the event.

string organizationID

"memory\_store.archived" type

string workspaceID



[BetaWebhookMemoryStoreCreatedEventData](api/beta/webhooks.md)

string id

ID of the memory store that triggered the event.

string organizationID

"memory\_store.created" type

string workspaceID



[BetaWebhookMemoryStoreDeletedEventData](api/beta/webhooks.md)

string id

ID of the memory store that triggered the event.

string organizationID

"memory\_store.deleted" type

string workspaceID



[BetaWebhookSessionArchivedEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.archived" type

string workspaceID



[BetaWebhookSessionCreatedEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.created" type

string workspaceID



[BetaWebhookSessionDeletedEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.deleted" type

string workspaceID



[BetaWebhookSessionIdledEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.idled" type

string workspaceID



[BetaWebhookSessionOutcomeEvaluationEndedEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.outcome\_evaluation\_ended" type

string workspaceID



[BetaWebhookSessionPendingEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.pending" type

string workspaceID



[BetaWebhookSessionRequiresActionEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.requires\_action" type

string workspaceID



[BetaWebhookSessionRunningEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.running" type

string workspaceID



[BetaWebhookSessionStatusIdledEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.status\_idled" type

string workspaceID



[BetaWebhookSessionStatusRescheduledEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.status\_rescheduled" type

string workspaceID



[BetaWebhookSessionStatusRunStartedEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.status\_run\_started" type

string workspaceID



[BetaWebhookSessionStatusTerminatedEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.status\_terminated" type

string workspaceID



[BetaWebhookSessionThreadCreatedEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

string sessionThreadID

ID of the session thread this event refers to.

"session.thread\_created" type

string workspaceID



[BetaWebhookSessionThreadIdledEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

string sessionThreadID

ID of the session thread this event refers to.

"session.thread\_idled" type

string workspaceID



[BetaWebhookSessionThreadTerminatedEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

string sessionThreadID

ID of the session thread this event refers to.

"session.thread\_terminated" type

string workspaceID



[BetaWebhookSessionUpdatedEventData](api/beta/webhooks.md)

string id

ID of the session that triggered the event.

string organizationID

"session.updated" type

string workspaceID



[BetaWebhookVaultArchivedEventData](api/beta/webhooks.md)

string id

ID of the vault that triggered the event.

string organizationID

"vault.archived" type

string workspaceID



[BetaWebhookVaultCreatedEventData](api/beta/webhooks.md)

string id

ID of the vault that triggered the event.

string organizationID

"vault.created" type

string workspaceID



[BetaWebhookVaultCredentialArchivedEventData](api/beta/webhooks.md)

string id

ID of the vault credential that triggered the event.

string organizationID

"vault\_credential.archived" type

string vaultID

ID of the vault that owns this credential.

string workspaceID



[BetaWebhookVaultCredentialCreatedEventData](api/beta/webhooks.md)

string id

ID of the vault credential that triggered the event.

string organizationID

"vault\_credential.created" type

string vaultID

ID of the vault that owns this credential.

string workspaceID



[BetaWebhookVaultCredentialDeletedEventData](api/beta/webhooks.md)

string id

ID of the vault credential that triggered the event.

string organizationID

"vault\_credential.deleted" type

string vaultID

ID of the vault that owns this credential.

string workspaceID



[BetaWebhookVaultCredentialRefreshFailedEventData](api/beta/webhooks.md)

string id

ID of the vault credential that triggered the event.

string organizationID

"vault\_credential.refresh\_failed" type

string vaultID

ID of the vault that owns this credential.

string workspaceID



[BetaWebhookVaultDeletedEventData](api/beta/webhooks.md)

string id

ID of the vault that triggered the event.

string organizationID

"vault.deleted" type

string workspaceID



[UnwrapWebhookEvent](api/beta/webhooks.md)

string id

Unique event identifier for idempotency.

\Datetime createdAt

RFC 3339 timestamp when the event occurred.

[BetaWebhookEventData](api/beta/webhooks.md) data

"event" type

Object type. Always `event` for webhook payloads.

---

*Copyright © Anthropic. All rights reserved.*
