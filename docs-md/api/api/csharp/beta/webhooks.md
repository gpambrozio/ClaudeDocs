# Webhooks

Copy page

SDK language

C#

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



class BetaWebhookEvent:

required string ID

Unique event identifier for idempotency.

required DateTimeOffset CreatedAt

RFC 3339 timestamp when the event occurred.



required [BetaWebhookEventData](api/beta.md) Data

One of the following:



class BetaWebhookSessionCreatedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.created"constant

required string WorkspaceID



class BetaWebhookSessionPendingEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.pending"constant

required string WorkspaceID



class BetaWebhookSessionRunningEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.running"constant

required string WorkspaceID



class BetaWebhookSessionIdledEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.idled"constant

required string WorkspaceID



class BetaWebhookSessionRequiresActionEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.requires\_action"constant

required string WorkspaceID



class BetaWebhookSessionArchivedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.archived"constant

required string WorkspaceID



class BetaWebhookSessionDeletedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.deleted"constant

required string WorkspaceID



class BetaWebhookSessionStatusRescheduledEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.status\_rescheduled"constant

required string WorkspaceID



class BetaWebhookSessionStatusRunStartedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.status\_run\_started"constant

required string WorkspaceID



class BetaWebhookSessionStatusIdledEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.status\_idled"constant

required string WorkspaceID



class BetaWebhookSessionStatusTerminatedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.status\_terminated"constant

required string WorkspaceID



class BetaWebhookSessionThreadCreatedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

required string SessionThreadID

ID of the session thread this event refers to.

JsonElement Type "session.thread\_created"constant

required string WorkspaceID



class BetaWebhookSessionThreadIdledEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

required string SessionThreadID

ID of the session thread this event refers to.

JsonElement Type "session.thread\_idled"constant

required string WorkspaceID



class BetaWebhookSessionThreadTerminatedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

required string SessionThreadID

ID of the session thread this event refers to.

JsonElement Type "session.thread\_terminated"constant

required string WorkspaceID



class BetaWebhookSessionOutcomeEvaluationEndedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.outcome\_evaluation\_ended"constant

required string WorkspaceID



class BetaWebhookVaultCreatedEventData:

required string ID

ID of the vault that triggered the event.

required string OrganizationID

JsonElement Type "vault.created"constant

required string WorkspaceID



class BetaWebhookVaultArchivedEventData:

required string ID

ID of the vault that triggered the event.

required string OrganizationID

JsonElement Type "vault.archived"constant

required string WorkspaceID



class BetaWebhookVaultDeletedEventData:

required string ID

ID of the vault that triggered the event.

required string OrganizationID

JsonElement Type "vault.deleted"constant

required string WorkspaceID



class BetaWebhookVaultCredentialCreatedEventData:

required string ID

ID of the vault credential that triggered the event.

required string OrganizationID

JsonElement Type "vault\_credential.created"constant

required string VaultID

ID of the vault that owns this credential.

required string WorkspaceID



class BetaWebhookVaultCredentialArchivedEventData:

required string ID

ID of the vault credential that triggered the event.

required string OrganizationID

JsonElement Type "vault\_credential.archived"constant

required string VaultID

ID of the vault that owns this credential.

required string WorkspaceID



class BetaWebhookVaultCredentialDeletedEventData:

required string ID

ID of the vault credential that triggered the event.

required string OrganizationID

JsonElement Type "vault\_credential.deleted"constant

required string VaultID

ID of the vault that owns this credential.

required string WorkspaceID



class BetaWebhookVaultCredentialRefreshFailedEventData:

required string ID

ID of the vault credential that triggered the event.

required string OrganizationID

JsonElement Type "vault\_credential.refresh\_failed"constant

required string VaultID

ID of the vault that owns this credential.

required string WorkspaceID

JsonElement Type "event"constant

Object type. Always `event` for webhook payloads.



class BetaWebhookEventData: A class that can be one of several variants.union 



class BetaWebhookSessionCreatedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.created"constant

required string WorkspaceID



class BetaWebhookSessionPendingEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.pending"constant

required string WorkspaceID



class BetaWebhookSessionRunningEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.running"constant

required string WorkspaceID



class BetaWebhookSessionIdledEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.idled"constant

required string WorkspaceID



class BetaWebhookSessionRequiresActionEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.requires\_action"constant

required string WorkspaceID



class BetaWebhookSessionArchivedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.archived"constant

required string WorkspaceID



class BetaWebhookSessionDeletedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.deleted"constant

required string WorkspaceID



class BetaWebhookSessionStatusRescheduledEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.status\_rescheduled"constant

required string WorkspaceID



class BetaWebhookSessionStatusRunStartedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.status\_run\_started"constant

required string WorkspaceID



class BetaWebhookSessionStatusIdledEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.status\_idled"constant

required string WorkspaceID



class BetaWebhookSessionStatusTerminatedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.status\_terminated"constant

required string WorkspaceID



class BetaWebhookSessionThreadCreatedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

required string SessionThreadID

ID of the session thread this event refers to.

JsonElement Type "session.thread\_created"constant

required string WorkspaceID



class BetaWebhookSessionThreadIdledEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

required string SessionThreadID

ID of the session thread this event refers to.

JsonElement Type "session.thread\_idled"constant

required string WorkspaceID



class BetaWebhookSessionThreadTerminatedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

required string SessionThreadID

ID of the session thread this event refers to.

JsonElement Type "session.thread\_terminated"constant

required string WorkspaceID



class BetaWebhookSessionOutcomeEvaluationEndedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.outcome\_evaluation\_ended"constant

required string WorkspaceID



class BetaWebhookVaultCreatedEventData:

required string ID

ID of the vault that triggered the event.

required string OrganizationID

JsonElement Type "vault.created"constant

required string WorkspaceID



class BetaWebhookVaultArchivedEventData:

required string ID

ID of the vault that triggered the event.

required string OrganizationID

JsonElement Type "vault.archived"constant

required string WorkspaceID



class BetaWebhookVaultDeletedEventData:

required string ID

ID of the vault that triggered the event.

required string OrganizationID

JsonElement Type "vault.deleted"constant

required string WorkspaceID



class BetaWebhookVaultCredentialCreatedEventData:

required string ID

ID of the vault credential that triggered the event.

required string OrganizationID

JsonElement Type "vault\_credential.created"constant

required string VaultID

ID of the vault that owns this credential.

required string WorkspaceID



class BetaWebhookVaultCredentialArchivedEventData:

required string ID

ID of the vault credential that triggered the event.

required string OrganizationID

JsonElement Type "vault\_credential.archived"constant

required string VaultID

ID of the vault that owns this credential.

required string WorkspaceID



class BetaWebhookVaultCredentialDeletedEventData:

required string ID

ID of the vault credential that triggered the event.

required string OrganizationID

JsonElement Type "vault\_credential.deleted"constant

required string VaultID

ID of the vault that owns this credential.

required string WorkspaceID



class BetaWebhookVaultCredentialRefreshFailedEventData:

required string ID

ID of the vault credential that triggered the event.

required string OrganizationID

JsonElement Type "vault\_credential.refresh\_failed"constant

required string VaultID

ID of the vault that owns this credential.

required string WorkspaceID



class BetaWebhookSessionArchivedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.archived"constant

required string WorkspaceID



class BetaWebhookSessionCreatedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.created"constant

required string WorkspaceID



class BetaWebhookSessionDeletedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.deleted"constant

required string WorkspaceID



class BetaWebhookSessionIdledEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.idled"constant

required string WorkspaceID



class BetaWebhookSessionOutcomeEvaluationEndedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.outcome\_evaluation\_ended"constant

required string WorkspaceID



class BetaWebhookSessionPendingEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.pending"constant

required string WorkspaceID



class BetaWebhookSessionRequiresActionEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.requires\_action"constant

required string WorkspaceID



class BetaWebhookSessionRunningEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.running"constant

required string WorkspaceID



class BetaWebhookSessionStatusIdledEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.status\_idled"constant

required string WorkspaceID



class BetaWebhookSessionStatusRescheduledEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.status\_rescheduled"constant

required string WorkspaceID



class BetaWebhookSessionStatusRunStartedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.status\_run\_started"constant

required string WorkspaceID



class BetaWebhookSessionStatusTerminatedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.status\_terminated"constant

required string WorkspaceID



class BetaWebhookSessionThreadCreatedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

required string SessionThreadID

ID of the session thread this event refers to.

JsonElement Type "session.thread\_created"constant

required string WorkspaceID



class BetaWebhookSessionThreadIdledEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

required string SessionThreadID

ID of the session thread this event refers to.

JsonElement Type "session.thread\_idled"constant

required string WorkspaceID



class BetaWebhookSessionThreadTerminatedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

required string SessionThreadID

ID of the session thread this event refers to.

JsonElement Type "session.thread\_terminated"constant

required string WorkspaceID



class BetaWebhookVaultArchivedEventData:

required string ID

ID of the vault that triggered the event.

required string OrganizationID

JsonElement Type "vault.archived"constant

required string WorkspaceID



class BetaWebhookVaultCreatedEventData:

required string ID

ID of the vault that triggered the event.

required string OrganizationID

JsonElement Type "vault.created"constant

required string WorkspaceID



class BetaWebhookVaultCredentialArchivedEventData:

required string ID

ID of the vault credential that triggered the event.

required string OrganizationID

JsonElement Type "vault\_credential.archived"constant

required string VaultID

ID of the vault that owns this credential.

required string WorkspaceID



class BetaWebhookVaultCredentialCreatedEventData:

required string ID

ID of the vault credential that triggered the event.

required string OrganizationID

JsonElement Type "vault\_credential.created"constant

required string VaultID

ID of the vault that owns this credential.

required string WorkspaceID



class BetaWebhookVaultCredentialDeletedEventData:

required string ID

ID of the vault credential that triggered the event.

required string OrganizationID

JsonElement Type "vault\_credential.deleted"constant

required string VaultID

ID of the vault that owns this credential.

required string WorkspaceID



class BetaWebhookVaultCredentialRefreshFailedEventData:

required string ID

ID of the vault credential that triggered the event.

required string OrganizationID

JsonElement Type "vault\_credential.refresh\_failed"constant

required string VaultID

ID of the vault that owns this credential.

required string WorkspaceID



class BetaWebhookVaultDeletedEventData:

required string ID

ID of the vault that triggered the event.

required string OrganizationID

JsonElement Type "vault.deleted"constant

required string WorkspaceID



class UnwrapWebhookEvent:

required string ID

Unique event identifier for idempotency.

required DateTimeOffset CreatedAt

RFC 3339 timestamp when the event occurred.



required [BetaWebhookEventData](api/beta.md) Data

One of the following:



class BetaWebhookSessionCreatedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.created"constant

required string WorkspaceID



class BetaWebhookSessionPendingEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.pending"constant

required string WorkspaceID



class BetaWebhookSessionRunningEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.running"constant

required string WorkspaceID



class BetaWebhookSessionIdledEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.idled"constant

required string WorkspaceID



class BetaWebhookSessionRequiresActionEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.requires\_action"constant

required string WorkspaceID



class BetaWebhookSessionArchivedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.archived"constant

required string WorkspaceID



class BetaWebhookSessionDeletedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.deleted"constant

required string WorkspaceID



class BetaWebhookSessionStatusRescheduledEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.status\_rescheduled"constant

required string WorkspaceID



class BetaWebhookSessionStatusRunStartedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.status\_run\_started"constant

required string WorkspaceID



class BetaWebhookSessionStatusIdledEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.status\_idled"constant

required string WorkspaceID



class BetaWebhookSessionStatusTerminatedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.status\_terminated"constant

required string WorkspaceID



class BetaWebhookSessionThreadCreatedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

required string SessionThreadID

ID of the session thread this event refers to.

JsonElement Type "session.thread\_created"constant

required string WorkspaceID



class BetaWebhookSessionThreadIdledEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

required string SessionThreadID

ID of the session thread this event refers to.

JsonElement Type "session.thread\_idled"constant

required string WorkspaceID



class BetaWebhookSessionThreadTerminatedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

required string SessionThreadID

ID of the session thread this event refers to.

JsonElement Type "session.thread\_terminated"constant

required string WorkspaceID



class BetaWebhookSessionOutcomeEvaluationEndedEventData:

required string ID

ID of the session that triggered the event.

required string OrganizationID

JsonElement Type "session.outcome\_evaluation\_ended"constant

required string WorkspaceID



class BetaWebhookVaultCreatedEventData:

required string ID

ID of the vault that triggered the event.

required string OrganizationID

JsonElement Type "vault.created"constant

required string WorkspaceID



class BetaWebhookVaultArchivedEventData:

required string ID

ID of the vault that triggered the event.

required string OrganizationID

JsonElement Type "vault.archived"constant

required string WorkspaceID



class BetaWebhookVaultDeletedEventData:

required string ID

ID of the vault that triggered the event.

required string OrganizationID

JsonElement Type "vault.deleted"constant

required string WorkspaceID



class BetaWebhookVaultCredentialCreatedEventData:

required string ID

ID of the vault credential that triggered the event.

required string OrganizationID

JsonElement Type "vault\_credential.created"constant

required string VaultID

ID of the vault that owns this credential.

required string WorkspaceID



class BetaWebhookVaultCredentialArchivedEventData:

required string ID

ID of the vault credential that triggered the event.

required string OrganizationID

JsonElement Type "vault\_credential.archived"constant

required string VaultID

ID of the vault that owns this credential.

required string WorkspaceID



class BetaWebhookVaultCredentialDeletedEventData:

required string ID

ID of the vault credential that triggered the event.

required string OrganizationID

JsonElement Type "vault\_credential.deleted"constant

required string VaultID

ID of the vault that owns this credential.

required string WorkspaceID



class BetaWebhookVaultCredentialRefreshFailedEventData:

required string ID

ID of the vault credential that triggered the event.

required string OrganizationID

JsonElement Type "vault\_credential.refresh\_failed"constant

required string VaultID

ID of the vault that owns this credential.

required string WorkspaceID

JsonElement Type "event"constant

Object type. Always `event` for webhook payloads.

---

*Copyright © Anthropic. All rights reserved.*
