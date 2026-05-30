# Webhooks

Copy page

SDK language

PHP

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

[BetaWebhookEvent](api/beta.md)

string id

Unique event identifier for idempotency.

\Datetime createdAt

RFC 3339 timestamp when the event occurred.

[BetaWebhookEventData](api/beta.md) data

"event" type

Object type. Always `event` for webhook payloads.

[BetaWebhookEventData](api/beta.md)

One of the following:

[BetaWebhookSessionCreatedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.created" type

string workspaceID

[BetaWebhookSessionPendingEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.pending" type

string workspaceID

[BetaWebhookSessionRunningEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.running" type

string workspaceID

[BetaWebhookSessionIdledEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.idled" type

string workspaceID

[BetaWebhookSessionRequiresActionEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.requires\_action" type

string workspaceID

[BetaWebhookSessionArchivedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.archived" type

string workspaceID

[BetaWebhookSessionDeletedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.deleted" type

string workspaceID

[BetaWebhookSessionStatusRescheduledEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.status\_rescheduled" type

string workspaceID

[BetaWebhookSessionStatusRunStartedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.status\_run\_started" type

string workspaceID

[BetaWebhookSessionStatusIdledEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.status\_idled" type

string workspaceID

[BetaWebhookSessionStatusTerminatedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.status\_terminated" type

string workspaceID

[BetaWebhookSessionThreadCreatedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.thread\_created" type

string workspaceID

[BetaWebhookSessionThreadIdledEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.thread\_idled" type

string workspaceID

[BetaWebhookSessionThreadTerminatedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.thread\_terminated" type

string workspaceID

[BetaWebhookSessionOutcomeEvaluationEndedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.outcome\_evaluation\_ended" type

string workspaceID

[BetaWebhookVaultCreatedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"vault.created" type

string workspaceID

[BetaWebhookVaultArchivedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"vault.archived" type

string workspaceID

[BetaWebhookVaultDeletedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"vault.deleted" type

string workspaceID

[BetaWebhookVaultCredentialCreatedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"vault\_credential.created" type

string vaultID

ID of the vault that owns this credential.

string workspaceID

[BetaWebhookVaultCredentialArchivedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"vault\_credential.archived" type

string vaultID

ID of the vault that owns this credential.

string workspaceID

[BetaWebhookVaultCredentialDeletedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"vault\_credential.deleted" type

string vaultID

ID of the vault that owns this credential.

string workspaceID

[BetaWebhookVaultCredentialRefreshFailedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"vault\_credential.refresh\_failed" type

string vaultID

ID of the vault that owns this credential.

string workspaceID

[BetaWebhookSessionArchivedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.archived" type

string workspaceID

[BetaWebhookSessionCreatedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.created" type

string workspaceID

[BetaWebhookSessionDeletedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.deleted" type

string workspaceID

[BetaWebhookSessionIdledEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.idled" type

string workspaceID

[BetaWebhookSessionOutcomeEvaluationEndedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.outcome\_evaluation\_ended" type

string workspaceID

[BetaWebhookSessionPendingEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.pending" type

string workspaceID

[BetaWebhookSessionRequiresActionEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.requires\_action" type

string workspaceID

[BetaWebhookSessionRunningEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.running" type

string workspaceID

[BetaWebhookSessionStatusIdledEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.status\_idled" type

string workspaceID

[BetaWebhookSessionStatusRescheduledEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.status\_rescheduled" type

string workspaceID

[BetaWebhookSessionStatusRunStartedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.status\_run\_started" type

string workspaceID

[BetaWebhookSessionStatusTerminatedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.status\_terminated" type

string workspaceID

[BetaWebhookSessionThreadCreatedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.thread\_created" type

string workspaceID

[BetaWebhookSessionThreadIdledEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.thread\_idled" type

string workspaceID

[BetaWebhookSessionThreadTerminatedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"session.thread\_terminated" type

string workspaceID

[BetaWebhookVaultArchivedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"vault.archived" type

string workspaceID

[BetaWebhookVaultCreatedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"vault.created" type

string workspaceID

[BetaWebhookVaultCredentialArchivedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"vault\_credential.archived" type

string vaultID

ID of the vault that owns this credential.

string workspaceID

[BetaWebhookVaultCredentialCreatedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"vault\_credential.created" type

string vaultID

ID of the vault that owns this credential.

string workspaceID

[BetaWebhookVaultCredentialDeletedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"vault\_credential.deleted" type

string vaultID

ID of the vault that owns this credential.

string workspaceID

[BetaWebhookVaultCredentialRefreshFailedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"vault\_credential.refresh\_failed" type

string vaultID

ID of the vault that owns this credential.

string workspaceID

[BetaWebhookVaultDeletedEventData](api/beta.md)

string id

ID of the resource that triggered the event.

string organizationID

"vault.deleted" type

string workspaceID

[UnwrapWebhookEvent](api/beta.md)

string id

Unique event identifier for idempotency.

\Datetime createdAt

RFC 3339 timestamp when the event occurred.

[BetaWebhookEventData](api/beta.md) data

"event" type

Object type. Always `event` for webhook payloads.

---

*Copyright © Anthropic. All rights reserved.*
