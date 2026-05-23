# Webhooks

Copy page

Java

# Webhooks

Helpers for receiving and verifying webhook events. Use `unwrap` in your SDK to verify signatures and parse payloads; see the [webhooks guide](managed-agents/webhooks.md) for handler examples.

Possible `data.type` values:

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
- `vault.archived`
- `vault.created`
- `vault.deleted`
- `vault_credential.archived`
- `vault_credential.created`
- `vault_credential.deleted`
- `vault_credential.refresh_failed`

##### ModelsExpand Collapse

class BetaWebhookEvent:

String id

Unique event identifier for idempotency.

LocalDateTime createdAt

RFC 3339 timestamp when the event occurred.

[BetaWebhookEventData](api/beta.md) data

One of the following:

class BetaWebhookSessionCreatedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.created"constant"session.created"constant

String workspaceId

class BetaWebhookSessionPendingEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.pending"constant"session.pending"constant

String workspaceId

class BetaWebhookSessionRunningEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.running"constant"session.running"constant

String workspaceId

class BetaWebhookSessionIdledEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.idled"constant"session.idled"constant

String workspaceId

class BetaWebhookSessionRequiresActionEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.requires\_action"constant"session.requires\_action"constant

String workspaceId

class BetaWebhookSessionArchivedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.archived"constant"session.archived"constant

String workspaceId

class BetaWebhookSessionDeletedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.deleted"constant"session.deleted"constant

String workspaceId

class BetaWebhookSessionStatusRescheduledEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.status\_rescheduled"constant"session.status\_rescheduled"constant

String workspaceId

class BetaWebhookSessionStatusRunStartedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.status\_run\_started"constant"session.status\_run\_started"constant

String workspaceId

class BetaWebhookSessionStatusIdledEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.status\_idled"constant"session.status\_idled"constant

String workspaceId

class BetaWebhookSessionStatusTerminatedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.status\_terminated"constant"session.status\_terminated"constant

String workspaceId

class BetaWebhookSessionThreadCreatedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.thread\_created"constant"session.thread\_created"constant

String workspaceId

class BetaWebhookSessionThreadIdledEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.thread\_idled"constant"session.thread\_idled"constant

String workspaceId

class BetaWebhookSessionThreadTerminatedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.thread\_terminated"constant"session.thread\_terminated"constant

String workspaceId

class BetaWebhookSessionOutcomeEvaluationEndedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.outcome\_evaluation\_ended"constant"session.outcome\_evaluation\_ended"constant

String workspaceId

class BetaWebhookVaultCreatedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault.created"constant"vault.created"constant

String workspaceId

class BetaWebhookVaultArchivedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault.archived"constant"vault.archived"constant

String workspaceId

class BetaWebhookVaultDeletedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault.deleted"constant"vault.deleted"constant

String workspaceId

class BetaWebhookVaultCredentialCreatedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault\_credential.created"constant"vault\_credential.created"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId

class BetaWebhookVaultCredentialArchivedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault\_credential.archived"constant"vault\_credential.archived"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId

class BetaWebhookVaultCredentialDeletedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault\_credential.deleted"constant"vault\_credential.deleted"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId

class BetaWebhookVaultCredentialRefreshFailedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault\_credential.refresh\_failed"constant"vault\_credential.refresh\_failed"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId

JsonValue; type "event"constant"event"constant

Object type. Always `event` for webhook payloads.

class BetaWebhookEventData: A class that can be one of several variants.union

class BetaWebhookSessionCreatedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.created"constant"session.created"constant

String workspaceId

class BetaWebhookSessionPendingEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.pending"constant"session.pending"constant

String workspaceId

class BetaWebhookSessionRunningEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.running"constant"session.running"constant

String workspaceId

class BetaWebhookSessionIdledEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.idled"constant"session.idled"constant

String workspaceId

class BetaWebhookSessionRequiresActionEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.requires\_action"constant"session.requires\_action"constant

String workspaceId

class BetaWebhookSessionArchivedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.archived"constant"session.archived"constant

String workspaceId

class BetaWebhookSessionDeletedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.deleted"constant"session.deleted"constant

String workspaceId

class BetaWebhookSessionStatusRescheduledEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.status\_rescheduled"constant"session.status\_rescheduled"constant

String workspaceId

class BetaWebhookSessionStatusRunStartedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.status\_run\_started"constant"session.status\_run\_started"constant

String workspaceId

class BetaWebhookSessionStatusIdledEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.status\_idled"constant"session.status\_idled"constant

String workspaceId

class BetaWebhookSessionStatusTerminatedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.status\_terminated"constant"session.status\_terminated"constant

String workspaceId

class BetaWebhookSessionThreadCreatedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.thread\_created"constant"session.thread\_created"constant

String workspaceId

class BetaWebhookSessionThreadIdledEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.thread\_idled"constant"session.thread\_idled"constant

String workspaceId

class BetaWebhookSessionThreadTerminatedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.thread\_terminated"constant"session.thread\_terminated"constant

String workspaceId

class BetaWebhookSessionOutcomeEvaluationEndedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.outcome\_evaluation\_ended"constant"session.outcome\_evaluation\_ended"constant

String workspaceId

class BetaWebhookVaultCreatedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault.created"constant"vault.created"constant

String workspaceId

class BetaWebhookVaultArchivedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault.archived"constant"vault.archived"constant

String workspaceId

class BetaWebhookVaultDeletedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault.deleted"constant"vault.deleted"constant

String workspaceId

class BetaWebhookVaultCredentialCreatedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault\_credential.created"constant"vault\_credential.created"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId

class BetaWebhookVaultCredentialArchivedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault\_credential.archived"constant"vault\_credential.archived"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId

class BetaWebhookVaultCredentialDeletedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault\_credential.deleted"constant"vault\_credential.deleted"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId

class BetaWebhookVaultCredentialRefreshFailedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault\_credential.refresh\_failed"constant"vault\_credential.refresh\_failed"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId

class BetaWebhookSessionArchivedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.archived"constant"session.archived"constant

String workspaceId

class BetaWebhookSessionCreatedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.created"constant"session.created"constant

String workspaceId

class BetaWebhookSessionDeletedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.deleted"constant"session.deleted"constant

String workspaceId

class BetaWebhookSessionIdledEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.idled"constant"session.idled"constant

String workspaceId

class BetaWebhookSessionOutcomeEvaluationEndedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.outcome\_evaluation\_ended"constant"session.outcome\_evaluation\_ended"constant

String workspaceId

class BetaWebhookSessionPendingEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.pending"constant"session.pending"constant

String workspaceId

class BetaWebhookSessionRequiresActionEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.requires\_action"constant"session.requires\_action"constant

String workspaceId

class BetaWebhookSessionRunningEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.running"constant"session.running"constant

String workspaceId

class BetaWebhookSessionStatusIdledEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.status\_idled"constant"session.status\_idled"constant

String workspaceId

class BetaWebhookSessionStatusRescheduledEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.status\_rescheduled"constant"session.status\_rescheduled"constant

String workspaceId

class BetaWebhookSessionStatusRunStartedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.status\_run\_started"constant"session.status\_run\_started"constant

String workspaceId

class BetaWebhookSessionStatusTerminatedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.status\_terminated"constant"session.status\_terminated"constant

String workspaceId

class BetaWebhookSessionThreadCreatedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.thread\_created"constant"session.thread\_created"constant

String workspaceId

class BetaWebhookSessionThreadIdledEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.thread\_idled"constant"session.thread\_idled"constant

String workspaceId

class BetaWebhookSessionThreadTerminatedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.thread\_terminated"constant"session.thread\_terminated"constant

String workspaceId

class BetaWebhookVaultArchivedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault.archived"constant"vault.archived"constant

String workspaceId

class BetaWebhookVaultCreatedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault.created"constant"vault.created"constant

String workspaceId

class BetaWebhookVaultCredentialArchivedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault\_credential.archived"constant"vault\_credential.archived"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId

class BetaWebhookVaultCredentialCreatedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault\_credential.created"constant"vault\_credential.created"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId

class BetaWebhookVaultCredentialDeletedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault\_credential.deleted"constant"vault\_credential.deleted"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId

class BetaWebhookVaultCredentialRefreshFailedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault\_credential.refresh\_failed"constant"vault\_credential.refresh\_failed"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId

class BetaWebhookVaultDeletedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault.deleted"constant"vault.deleted"constant

String workspaceId

class UnwrapWebhookEvent:

String id

Unique event identifier for idempotency.

LocalDateTime createdAt

RFC 3339 timestamp when the event occurred.

[BetaWebhookEventData](api/beta.md) data

One of the following:

class BetaWebhookSessionCreatedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.created"constant"session.created"constant

String workspaceId

class BetaWebhookSessionPendingEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.pending"constant"session.pending"constant

String workspaceId

class BetaWebhookSessionRunningEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.running"constant"session.running"constant

String workspaceId

class BetaWebhookSessionIdledEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.idled"constant"session.idled"constant

String workspaceId

class BetaWebhookSessionRequiresActionEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.requires\_action"constant"session.requires\_action"constant

String workspaceId

class BetaWebhookSessionArchivedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.archived"constant"session.archived"constant

String workspaceId

class BetaWebhookSessionDeletedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.deleted"constant"session.deleted"constant

String workspaceId

class BetaWebhookSessionStatusRescheduledEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.status\_rescheduled"constant"session.status\_rescheduled"constant

String workspaceId

class BetaWebhookSessionStatusRunStartedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.status\_run\_started"constant"session.status\_run\_started"constant

String workspaceId

class BetaWebhookSessionStatusIdledEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.status\_idled"constant"session.status\_idled"constant

String workspaceId

class BetaWebhookSessionStatusTerminatedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.status\_terminated"constant"session.status\_terminated"constant

String workspaceId

class BetaWebhookSessionThreadCreatedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.thread\_created"constant"session.thread\_created"constant

String workspaceId

class BetaWebhookSessionThreadIdledEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.thread\_idled"constant"session.thread\_idled"constant

String workspaceId

class BetaWebhookSessionThreadTerminatedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.thread\_terminated"constant"session.thread\_terminated"constant

String workspaceId

class BetaWebhookSessionOutcomeEvaluationEndedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "session.outcome\_evaluation\_ended"constant"session.outcome\_evaluation\_ended"constant

String workspaceId

class BetaWebhookVaultCreatedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault.created"constant"vault.created"constant

String workspaceId

class BetaWebhookVaultArchivedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault.archived"constant"vault.archived"constant

String workspaceId

class BetaWebhookVaultDeletedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault.deleted"constant"vault.deleted"constant

String workspaceId

class BetaWebhookVaultCredentialCreatedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault\_credential.created"constant"vault\_credential.created"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId

class BetaWebhookVaultCredentialArchivedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault\_credential.archived"constant"vault\_credential.archived"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId

class BetaWebhookVaultCredentialDeletedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault\_credential.deleted"constant"vault\_credential.deleted"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId

class BetaWebhookVaultCredentialRefreshFailedEventData:

String id

ID of the resource that triggered the event.

String organizationId

JsonValue; type "vault\_credential.refresh\_failed"constant"vault\_credential.refresh\_failed"constant

String vaultId

ID of the vault that owns this credential.

String workspaceId

JsonValue; type "event"constant"event"constant

Object type. Always `event` for webhook payloads.

---

*Copyright © Anthropic. All rights reserved.*
