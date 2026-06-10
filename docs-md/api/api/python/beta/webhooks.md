# Webhooks

Copy page

SDK language

Python

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

class BetaWebhookEvent: …

id: str

Unique event identifier for idempotency.

created\_at: datetime

RFC 3339 timestamp when the event occurred.

data: [BetaWebhookEventData](api/beta.md)

One of the following:

class BetaWebhookSessionCreatedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.created"]

workspace\_id: str

class BetaWebhookSessionPendingEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.pending"]

workspace\_id: str

class BetaWebhookSessionRunningEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.running"]

workspace\_id: str

class BetaWebhookSessionIdledEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.idled"]

workspace\_id: str

class BetaWebhookSessionRequiresActionEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.requires\_action"]

workspace\_id: str

class BetaWebhookSessionArchivedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.archived"]

workspace\_id: str

class BetaWebhookSessionDeletedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.deleted"]

workspace\_id: str

class BetaWebhookSessionStatusRescheduledEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.status\_rescheduled"]

workspace\_id: str

class BetaWebhookSessionStatusRunStartedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.status\_run\_started"]

workspace\_id: str

class BetaWebhookSessionStatusIdledEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.status\_idled"]

workspace\_id: str

class BetaWebhookSessionStatusTerminatedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.status\_terminated"]

workspace\_id: str

class BetaWebhookSessionThreadCreatedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

session\_thread\_id: str

ID of the session thread this event refers to.

type: Literal["session.thread\_created"]

workspace\_id: str

class BetaWebhookSessionThreadIdledEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

session\_thread\_id: str

ID of the session thread this event refers to.

type: Literal["session.thread\_idled"]

workspace\_id: str

class BetaWebhookSessionThreadTerminatedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

session\_thread\_id: str

ID of the session thread this event refers to.

type: Literal["session.thread\_terminated"]

workspace\_id: str

class BetaWebhookSessionOutcomeEvaluationEndedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.outcome\_evaluation\_ended"]

workspace\_id: str

class BetaWebhookVaultCreatedEventData: …

id: str

ID of the vault that triggered the event.

organization\_id: str

type: Literal["vault.created"]

workspace\_id: str

class BetaWebhookVaultArchivedEventData: …

id: str

ID of the vault that triggered the event.

organization\_id: str

type: Literal["vault.archived"]

workspace\_id: str

class BetaWebhookVaultDeletedEventData: …

id: str

ID of the vault that triggered the event.

organization\_id: str

type: Literal["vault.deleted"]

workspace\_id: str

class BetaWebhookVaultCredentialCreatedEventData: …

id: str

ID of the vault credential that triggered the event.

organization\_id: str

type: Literal["vault\_credential.created"]

vault\_id: str

ID of the vault that owns this credential.

workspace\_id: str

class BetaWebhookVaultCredentialArchivedEventData: …

id: str

ID of the vault credential that triggered the event.

organization\_id: str

type: Literal["vault\_credential.archived"]

vault\_id: str

ID of the vault that owns this credential.

workspace\_id: str

class BetaWebhookVaultCredentialDeletedEventData: …

id: str

ID of the vault credential that triggered the event.

organization\_id: str

type: Literal["vault\_credential.deleted"]

vault\_id: str

ID of the vault that owns this credential.

workspace\_id: str

class BetaWebhookVaultCredentialRefreshFailedEventData: …

id: str

ID of the vault credential that triggered the event.

organization\_id: str

type: Literal["vault\_credential.refresh\_failed"]

vault\_id: str

ID of the vault that owns this credential.

workspace\_id: str

type: Literal["event"]

Object type. Always `event` for webhook payloads.

[BetaWebhookEventData](api/beta.md)

One of the following:

class BetaWebhookSessionCreatedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.created"]

workspace\_id: str

class BetaWebhookSessionPendingEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.pending"]

workspace\_id: str

class BetaWebhookSessionRunningEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.running"]

workspace\_id: str

class BetaWebhookSessionIdledEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.idled"]

workspace\_id: str

class BetaWebhookSessionRequiresActionEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.requires\_action"]

workspace\_id: str

class BetaWebhookSessionArchivedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.archived"]

workspace\_id: str

class BetaWebhookSessionDeletedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.deleted"]

workspace\_id: str

class BetaWebhookSessionStatusRescheduledEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.status\_rescheduled"]

workspace\_id: str

class BetaWebhookSessionStatusRunStartedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.status\_run\_started"]

workspace\_id: str

class BetaWebhookSessionStatusIdledEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.status\_idled"]

workspace\_id: str

class BetaWebhookSessionStatusTerminatedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.status\_terminated"]

workspace\_id: str

class BetaWebhookSessionThreadCreatedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

session\_thread\_id: str

ID of the session thread this event refers to.

type: Literal["session.thread\_created"]

workspace\_id: str

class BetaWebhookSessionThreadIdledEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

session\_thread\_id: str

ID of the session thread this event refers to.

type: Literal["session.thread\_idled"]

workspace\_id: str

class BetaWebhookSessionThreadTerminatedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

session\_thread\_id: str

ID of the session thread this event refers to.

type: Literal["session.thread\_terminated"]

workspace\_id: str

class BetaWebhookSessionOutcomeEvaluationEndedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.outcome\_evaluation\_ended"]

workspace\_id: str

class BetaWebhookVaultCreatedEventData: …

id: str

ID of the vault that triggered the event.

organization\_id: str

type: Literal["vault.created"]

workspace\_id: str

class BetaWebhookVaultArchivedEventData: …

id: str

ID of the vault that triggered the event.

organization\_id: str

type: Literal["vault.archived"]

workspace\_id: str

class BetaWebhookVaultDeletedEventData: …

id: str

ID of the vault that triggered the event.

organization\_id: str

type: Literal["vault.deleted"]

workspace\_id: str

class BetaWebhookVaultCredentialCreatedEventData: …

id: str

ID of the vault credential that triggered the event.

organization\_id: str

type: Literal["vault\_credential.created"]

vault\_id: str

ID of the vault that owns this credential.

workspace\_id: str

class BetaWebhookVaultCredentialArchivedEventData: …

id: str

ID of the vault credential that triggered the event.

organization\_id: str

type: Literal["vault\_credential.archived"]

vault\_id: str

ID of the vault that owns this credential.

workspace\_id: str

class BetaWebhookVaultCredentialDeletedEventData: …

id: str

ID of the vault credential that triggered the event.

organization\_id: str

type: Literal["vault\_credential.deleted"]

vault\_id: str

ID of the vault that owns this credential.

workspace\_id: str

class BetaWebhookVaultCredentialRefreshFailedEventData: …

id: str

ID of the vault credential that triggered the event.

organization\_id: str

type: Literal["vault\_credential.refresh\_failed"]

vault\_id: str

ID of the vault that owns this credential.

workspace\_id: str

class BetaWebhookSessionArchivedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.archived"]

workspace\_id: str

class BetaWebhookSessionCreatedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.created"]

workspace\_id: str

class BetaWebhookSessionDeletedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.deleted"]

workspace\_id: str

class BetaWebhookSessionIdledEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.idled"]

workspace\_id: str

class BetaWebhookSessionOutcomeEvaluationEndedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.outcome\_evaluation\_ended"]

workspace\_id: str

class BetaWebhookSessionPendingEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.pending"]

workspace\_id: str

class BetaWebhookSessionRequiresActionEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.requires\_action"]

workspace\_id: str

class BetaWebhookSessionRunningEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.running"]

workspace\_id: str

class BetaWebhookSessionStatusIdledEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.status\_idled"]

workspace\_id: str

class BetaWebhookSessionStatusRescheduledEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.status\_rescheduled"]

workspace\_id: str

class BetaWebhookSessionStatusRunStartedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.status\_run\_started"]

workspace\_id: str

class BetaWebhookSessionStatusTerminatedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.status\_terminated"]

workspace\_id: str

class BetaWebhookSessionThreadCreatedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

session\_thread\_id: str

ID of the session thread this event refers to.

type: Literal["session.thread\_created"]

workspace\_id: str

class BetaWebhookSessionThreadIdledEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

session\_thread\_id: str

ID of the session thread this event refers to.

type: Literal["session.thread\_idled"]

workspace\_id: str

class BetaWebhookSessionThreadTerminatedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

session\_thread\_id: str

ID of the session thread this event refers to.

type: Literal["session.thread\_terminated"]

workspace\_id: str

class BetaWebhookVaultArchivedEventData: …

id: str

ID of the vault that triggered the event.

organization\_id: str

type: Literal["vault.archived"]

workspace\_id: str

class BetaWebhookVaultCreatedEventData: …

id: str

ID of the vault that triggered the event.

organization\_id: str

type: Literal["vault.created"]

workspace\_id: str

class BetaWebhookVaultCredentialArchivedEventData: …

id: str

ID of the vault credential that triggered the event.

organization\_id: str

type: Literal["vault\_credential.archived"]

vault\_id: str

ID of the vault that owns this credential.

workspace\_id: str

class BetaWebhookVaultCredentialCreatedEventData: …

id: str

ID of the vault credential that triggered the event.

organization\_id: str

type: Literal["vault\_credential.created"]

vault\_id: str

ID of the vault that owns this credential.

workspace\_id: str

class BetaWebhookVaultCredentialDeletedEventData: …

id: str

ID of the vault credential that triggered the event.

organization\_id: str

type: Literal["vault\_credential.deleted"]

vault\_id: str

ID of the vault that owns this credential.

workspace\_id: str

class BetaWebhookVaultCredentialRefreshFailedEventData: …

id: str

ID of the vault credential that triggered the event.

organization\_id: str

type: Literal["vault\_credential.refresh\_failed"]

vault\_id: str

ID of the vault that owns this credential.

workspace\_id: str

class BetaWebhookVaultDeletedEventData: …

id: str

ID of the vault that triggered the event.

organization\_id: str

type: Literal["vault.deleted"]

workspace\_id: str

class UnwrapWebhookEvent: …

id: str

Unique event identifier for idempotency.

created\_at: datetime

RFC 3339 timestamp when the event occurred.

data: [BetaWebhookEventData](api/beta.md)

One of the following:

class BetaWebhookSessionCreatedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.created"]

workspace\_id: str

class BetaWebhookSessionPendingEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.pending"]

workspace\_id: str

class BetaWebhookSessionRunningEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.running"]

workspace\_id: str

class BetaWebhookSessionIdledEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.idled"]

workspace\_id: str

class BetaWebhookSessionRequiresActionEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.requires\_action"]

workspace\_id: str

class BetaWebhookSessionArchivedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.archived"]

workspace\_id: str

class BetaWebhookSessionDeletedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.deleted"]

workspace\_id: str

class BetaWebhookSessionStatusRescheduledEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.status\_rescheduled"]

workspace\_id: str

class BetaWebhookSessionStatusRunStartedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.status\_run\_started"]

workspace\_id: str

class BetaWebhookSessionStatusIdledEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.status\_idled"]

workspace\_id: str

class BetaWebhookSessionStatusTerminatedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.status\_terminated"]

workspace\_id: str

class BetaWebhookSessionThreadCreatedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

session\_thread\_id: str

ID of the session thread this event refers to.

type: Literal["session.thread\_created"]

workspace\_id: str

class BetaWebhookSessionThreadIdledEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

session\_thread\_id: str

ID of the session thread this event refers to.

type: Literal["session.thread\_idled"]

workspace\_id: str

class BetaWebhookSessionThreadTerminatedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

session\_thread\_id: str

ID of the session thread this event refers to.

type: Literal["session.thread\_terminated"]

workspace\_id: str

class BetaWebhookSessionOutcomeEvaluationEndedEventData: …

id: str

ID of the session that triggered the event.

organization\_id: str

type: Literal["session.outcome\_evaluation\_ended"]

workspace\_id: str

class BetaWebhookVaultCreatedEventData: …

id: str

ID of the vault that triggered the event.

organization\_id: str

type: Literal["vault.created"]

workspace\_id: str

class BetaWebhookVaultArchivedEventData: …

id: str

ID of the vault that triggered the event.

organization\_id: str

type: Literal["vault.archived"]

workspace\_id: str

class BetaWebhookVaultDeletedEventData: …

id: str

ID of the vault that triggered the event.

organization\_id: str

type: Literal["vault.deleted"]

workspace\_id: str

class BetaWebhookVaultCredentialCreatedEventData: …

id: str

ID of the vault credential that triggered the event.

organization\_id: str

type: Literal["vault\_credential.created"]

vault\_id: str

ID of the vault that owns this credential.

workspace\_id: str

class BetaWebhookVaultCredentialArchivedEventData: …

id: str

ID of the vault credential that triggered the event.

organization\_id: str

type: Literal["vault\_credential.archived"]

vault\_id: str

ID of the vault that owns this credential.

workspace\_id: str

class BetaWebhookVaultCredentialDeletedEventData: …

id: str

ID of the vault credential that triggered the event.

organization\_id: str

type: Literal["vault\_credential.deleted"]

vault\_id: str

ID of the vault that owns this credential.

workspace\_id: str

class BetaWebhookVaultCredentialRefreshFailedEventData: …

id: str

ID of the vault credential that triggered the event.

organization\_id: str

type: Literal["vault\_credential.refresh\_failed"]

vault\_id: str

ID of the vault that owns this credential.

workspace\_id: str

type: Literal["event"]

Object type. Always `event` for webhook payloads.

---

*Copyright © Anthropic. All rights reserved.*
