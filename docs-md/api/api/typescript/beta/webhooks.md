# Webhooks

Copy page



TypeScript

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

BetaWebhookEvent { id, created\_at, data, type } 

id: string

Unique event identifier for idempotency.

created\_at: string

RFC 3339 timestamp when the event occurred.



data: [BetaWebhookEventData](api/beta/webhooks.md)

One of the following:



BetaWebhookSessionCreatedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.created"

workspace\_id: string



BetaWebhookSessionPendingEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.pending"

workspace\_id: string



BetaWebhookSessionRunningEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.running"

workspace\_id: string



BetaWebhookSessionIdledEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.idled"

workspace\_id: string



BetaWebhookSessionRequiresActionEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.requires\_action"

workspace\_id: string



BetaWebhookSessionArchivedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.archived"

workspace\_id: string



BetaWebhookSessionDeletedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.deleted"

workspace\_id: string



BetaWebhookSessionStatusRescheduledEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.status\_rescheduled"

workspace\_id: string



BetaWebhookSessionStatusRunStartedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.status\_run\_started"

workspace\_id: string



BetaWebhookSessionStatusIdledEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.status\_idled"

workspace\_id: string



BetaWebhookSessionStatusTerminatedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.status\_terminated"

workspace\_id: string



BetaWebhookSessionThreadCreatedEventData { id, organization\_id, session\_thread\_id, 2 more } 

id: string

ID of the session that triggered the event.

organization\_id: string

session\_thread\_id: string

ID of the session thread this event refers to.

type: "session.thread\_created"

workspace\_id: string



BetaWebhookSessionThreadIdledEventData { id, organization\_id, session\_thread\_id, 2 more } 

id: string

ID of the session that triggered the event.

organization\_id: string

session\_thread\_id: string

ID of the session thread this event refers to.

type: "session.thread\_idled"

workspace\_id: string



BetaWebhookSessionThreadTerminatedEventData { id, organization\_id, session\_thread\_id, 2 more } 

id: string

ID of the session that triggered the event.

organization\_id: string

session\_thread\_id: string

ID of the session thread this event refers to.

type: "session.thread\_terminated"

workspace\_id: string



BetaWebhookSessionOutcomeEvaluationEndedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.outcome\_evaluation\_ended"

workspace\_id: string



BetaWebhookVaultCreatedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the vault that triggered the event.

organization\_id: string

type: "vault.created"

workspace\_id: string



BetaWebhookVaultArchivedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the vault that triggered the event.

organization\_id: string

type: "vault.archived"

workspace\_id: string



BetaWebhookVaultDeletedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the vault that triggered the event.

organization\_id: string

type: "vault.deleted"

workspace\_id: string



BetaWebhookVaultCredentialCreatedEventData { id, organization\_id, type, 2 more } 

id: string

ID of the vault credential that triggered the event.

organization\_id: string

type: "vault\_credential.created"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string



BetaWebhookVaultCredentialArchivedEventData { id, organization\_id, type, 2 more } 

id: string

ID of the vault credential that triggered the event.

organization\_id: string

type: "vault\_credential.archived"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string



BetaWebhookVaultCredentialDeletedEventData { id, organization\_id, type, 2 more } 

id: string

ID of the vault credential that triggered the event.

organization\_id: string

type: "vault\_credential.deleted"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string



BetaWebhookVaultCredentialRefreshFailedEventData { id, organization\_id, type, 2 more } 

id: string

ID of the vault credential that triggered the event.

organization\_id: string

type: "vault\_credential.refresh\_failed"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string



BetaWebhookSessionUpdatedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.updated"

workspace\_id: string

type: "event"

Object type. Always `event` for webhook payloads.



BetaWebhookEventData = [BetaWebhookSessionCreatedEventData](api/beta/webhooks.md) { id, organization\_id, type, workspace\_id }  | [BetaWebhookSessionPendingEventData](api/beta/webhooks.md) { id, organization\_id, type, workspace\_id }  | [BetaWebhookSessionRunningEventData](api/beta/webhooks.md) { id, organization\_id, type, workspace\_id }  | 20 more

One of the following:



BetaWebhookSessionCreatedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.created"

workspace\_id: string



BetaWebhookSessionPendingEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.pending"

workspace\_id: string



BetaWebhookSessionRunningEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.running"

workspace\_id: string



BetaWebhookSessionIdledEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.idled"

workspace\_id: string



BetaWebhookSessionRequiresActionEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.requires\_action"

workspace\_id: string



BetaWebhookSessionArchivedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.archived"

workspace\_id: string



BetaWebhookSessionDeletedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.deleted"

workspace\_id: string



BetaWebhookSessionStatusRescheduledEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.status\_rescheduled"

workspace\_id: string



BetaWebhookSessionStatusRunStartedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.status\_run\_started"

workspace\_id: string



BetaWebhookSessionStatusIdledEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.status\_idled"

workspace\_id: string



BetaWebhookSessionStatusTerminatedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.status\_terminated"

workspace\_id: string



BetaWebhookSessionThreadCreatedEventData { id, organization\_id, session\_thread\_id, 2 more } 

id: string

ID of the session that triggered the event.

organization\_id: string

session\_thread\_id: string

ID of the session thread this event refers to.

type: "session.thread\_created"

workspace\_id: string



BetaWebhookSessionThreadIdledEventData { id, organization\_id, session\_thread\_id, 2 more } 

id: string

ID of the session that triggered the event.

organization\_id: string

session\_thread\_id: string

ID of the session thread this event refers to.

type: "session.thread\_idled"

workspace\_id: string



BetaWebhookSessionThreadTerminatedEventData { id, organization\_id, session\_thread\_id, 2 more } 

id: string

ID of the session that triggered the event.

organization\_id: string

session\_thread\_id: string

ID of the session thread this event refers to.

type: "session.thread\_terminated"

workspace\_id: string



BetaWebhookSessionOutcomeEvaluationEndedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.outcome\_evaluation\_ended"

workspace\_id: string



BetaWebhookVaultCreatedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the vault that triggered the event.

organization\_id: string

type: "vault.created"

workspace\_id: string



BetaWebhookVaultArchivedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the vault that triggered the event.

organization\_id: string

type: "vault.archived"

workspace\_id: string



BetaWebhookVaultDeletedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the vault that triggered the event.

organization\_id: string

type: "vault.deleted"

workspace\_id: string



BetaWebhookVaultCredentialCreatedEventData { id, organization\_id, type, 2 more } 

id: string

ID of the vault credential that triggered the event.

organization\_id: string

type: "vault\_credential.created"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string



BetaWebhookVaultCredentialArchivedEventData { id, organization\_id, type, 2 more } 

id: string

ID of the vault credential that triggered the event.

organization\_id: string

type: "vault\_credential.archived"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string



BetaWebhookVaultCredentialDeletedEventData { id, organization\_id, type, 2 more } 

id: string

ID of the vault credential that triggered the event.

organization\_id: string

type: "vault\_credential.deleted"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string



BetaWebhookVaultCredentialRefreshFailedEventData { id, organization\_id, type, 2 more } 

id: string

ID of the vault credential that triggered the event.

organization\_id: string

type: "vault\_credential.refresh\_failed"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string



BetaWebhookSessionUpdatedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.updated"

workspace\_id: string



BetaWebhookSessionArchivedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.archived"

workspace\_id: string



BetaWebhookSessionCreatedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.created"

workspace\_id: string



BetaWebhookSessionDeletedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.deleted"

workspace\_id: string



BetaWebhookSessionIdledEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.idled"

workspace\_id: string



BetaWebhookSessionOutcomeEvaluationEndedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.outcome\_evaluation\_ended"

workspace\_id: string



BetaWebhookSessionPendingEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.pending"

workspace\_id: string



BetaWebhookSessionRequiresActionEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.requires\_action"

workspace\_id: string



BetaWebhookSessionRunningEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.running"

workspace\_id: string



BetaWebhookSessionStatusIdledEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.status\_idled"

workspace\_id: string



BetaWebhookSessionStatusRescheduledEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.status\_rescheduled"

workspace\_id: string



BetaWebhookSessionStatusRunStartedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.status\_run\_started"

workspace\_id: string



BetaWebhookSessionStatusTerminatedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.status\_terminated"

workspace\_id: string



BetaWebhookSessionThreadCreatedEventData { id, organization\_id, session\_thread\_id, 2 more } 

id: string

ID of the session that triggered the event.

organization\_id: string

session\_thread\_id: string

ID of the session thread this event refers to.

type: "session.thread\_created"

workspace\_id: string



BetaWebhookSessionThreadIdledEventData { id, organization\_id, session\_thread\_id, 2 more } 

id: string

ID of the session that triggered the event.

organization\_id: string

session\_thread\_id: string

ID of the session thread this event refers to.

type: "session.thread\_idled"

workspace\_id: string



BetaWebhookSessionThreadTerminatedEventData { id, organization\_id, session\_thread\_id, 2 more } 

id: string

ID of the session that triggered the event.

organization\_id: string

session\_thread\_id: string

ID of the session thread this event refers to.

type: "session.thread\_terminated"

workspace\_id: string



BetaWebhookSessionUpdatedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.updated"

workspace\_id: string



BetaWebhookVaultArchivedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the vault that triggered the event.

organization\_id: string

type: "vault.archived"

workspace\_id: string



BetaWebhookVaultCreatedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the vault that triggered the event.

organization\_id: string

type: "vault.created"

workspace\_id: string



BetaWebhookVaultCredentialArchivedEventData { id, organization\_id, type, 2 more } 

id: string

ID of the vault credential that triggered the event.

organization\_id: string

type: "vault\_credential.archived"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string



BetaWebhookVaultCredentialCreatedEventData { id, organization\_id, type, 2 more } 

id: string

ID of the vault credential that triggered the event.

organization\_id: string

type: "vault\_credential.created"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string



BetaWebhookVaultCredentialDeletedEventData { id, organization\_id, type, 2 more } 

id: string

ID of the vault credential that triggered the event.

organization\_id: string

type: "vault\_credential.deleted"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string



BetaWebhookVaultCredentialRefreshFailedEventData { id, organization\_id, type, 2 more } 

id: string

ID of the vault credential that triggered the event.

organization\_id: string

type: "vault\_credential.refresh\_failed"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string



BetaWebhookVaultDeletedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the vault that triggered the event.

organization\_id: string

type: "vault.deleted"

workspace\_id: string



UnwrapWebhookEvent { id, created\_at, data, type } 

id: string

Unique event identifier for idempotency.

created\_at: string

RFC 3339 timestamp when the event occurred.



data: [BetaWebhookEventData](api/beta/webhooks.md)

One of the following:



BetaWebhookSessionCreatedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.created"

workspace\_id: string



BetaWebhookSessionPendingEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.pending"

workspace\_id: string



BetaWebhookSessionRunningEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.running"

workspace\_id: string



BetaWebhookSessionIdledEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.idled"

workspace\_id: string



BetaWebhookSessionRequiresActionEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.requires\_action"

workspace\_id: string



BetaWebhookSessionArchivedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.archived"

workspace\_id: string



BetaWebhookSessionDeletedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.deleted"

workspace\_id: string



BetaWebhookSessionStatusRescheduledEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.status\_rescheduled"

workspace\_id: string



BetaWebhookSessionStatusRunStartedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.status\_run\_started"

workspace\_id: string



BetaWebhookSessionStatusIdledEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.status\_idled"

workspace\_id: string



BetaWebhookSessionStatusTerminatedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.status\_terminated"

workspace\_id: string



BetaWebhookSessionThreadCreatedEventData { id, organization\_id, session\_thread\_id, 2 more } 

id: string

ID of the session that triggered the event.

organization\_id: string

session\_thread\_id: string

ID of the session thread this event refers to.

type: "session.thread\_created"

workspace\_id: string



BetaWebhookSessionThreadIdledEventData { id, organization\_id, session\_thread\_id, 2 more } 

id: string

ID of the session that triggered the event.

organization\_id: string

session\_thread\_id: string

ID of the session thread this event refers to.

type: "session.thread\_idled"

workspace\_id: string



BetaWebhookSessionThreadTerminatedEventData { id, organization\_id, session\_thread\_id, 2 more } 

id: string

ID of the session that triggered the event.

organization\_id: string

session\_thread\_id: string

ID of the session thread this event refers to.

type: "session.thread\_terminated"

workspace\_id: string



BetaWebhookSessionOutcomeEvaluationEndedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.outcome\_evaluation\_ended"

workspace\_id: string



BetaWebhookVaultCreatedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the vault that triggered the event.

organization\_id: string

type: "vault.created"

workspace\_id: string



BetaWebhookVaultArchivedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the vault that triggered the event.

organization\_id: string

type: "vault.archived"

workspace\_id: string



BetaWebhookVaultDeletedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the vault that triggered the event.

organization\_id: string

type: "vault.deleted"

workspace\_id: string



BetaWebhookVaultCredentialCreatedEventData { id, organization\_id, type, 2 more } 

id: string

ID of the vault credential that triggered the event.

organization\_id: string

type: "vault\_credential.created"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string



BetaWebhookVaultCredentialArchivedEventData { id, organization\_id, type, 2 more } 

id: string

ID of the vault credential that triggered the event.

organization\_id: string

type: "vault\_credential.archived"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string



BetaWebhookVaultCredentialDeletedEventData { id, organization\_id, type, 2 more } 

id: string

ID of the vault credential that triggered the event.

organization\_id: string

type: "vault\_credential.deleted"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string



BetaWebhookVaultCredentialRefreshFailedEventData { id, organization\_id, type, 2 more } 

id: string

ID of the vault credential that triggered the event.

organization\_id: string

type: "vault\_credential.refresh\_failed"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string



BetaWebhookSessionUpdatedEventData { id, organization\_id, type, workspace\_id } 

id: string

ID of the session that triggered the event.

organization\_id: string

type: "session.updated"

workspace\_id: string

type: "event"

Object type. Always `event` for webhook payloads.

---

*Copyright © Anthropic. All rights reserved.*
