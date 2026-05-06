# Webhooks

Copy page

cURL

# Webhooks

##### [Unwrap](api/beta/webhooks/unwrap.md)

Function

##### ModelsExpand Collapse

BetaWebhookEvent = object { id, created\_at, data, type }

id: string

Unique event identifier for idempotency.

created\_at: string

RFC 3339 timestamp when the event occurred.

data: [BetaWebhookEventData](api/beta.md)

Accepts one of the following:

BetaWebhookSessionCreatedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.created"

workspace\_id: string

BetaWebhookSessionPendingEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.pending"

workspace\_id: string

BetaWebhookSessionRunningEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.running"

workspace\_id: string

BetaWebhookSessionIdledEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.idled"

workspace\_id: string

BetaWebhookSessionRequiresActionEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.requires\_action"

workspace\_id: string

BetaWebhookSessionArchivedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.archived"

workspace\_id: string

BetaWebhookSessionDeletedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.deleted"

workspace\_id: string

BetaWebhookSessionStatusScheduledEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_scheduled"

workspace\_id: string

BetaWebhookSessionStatusRunStartedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_run\_started"

workspace\_id: string

BetaWebhookSessionStatusIdledEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_idled"

workspace\_id: string

BetaWebhookSessionStatusTerminatedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_terminated"

workspace\_id: string

BetaWebhookSessionThreadCreatedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.thread\_created"

workspace\_id: string

BetaWebhookSessionThreadIdledEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.thread\_idled"

workspace\_id: string

BetaWebhookSessionThreadTerminatedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.thread\_terminated"

workspace\_id: string

BetaWebhookSessionOutcomeEvaluationEndedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.outcome\_evaluation\_ended"

workspace\_id: string

BetaWebhookVaultCreatedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault.created"

workspace\_id: string

BetaWebhookVaultArchivedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault.archived"

workspace\_id: string

BetaWebhookVaultDeletedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault.deleted"

workspace\_id: string

BetaWebhookVaultCredentialCreatedEventData = object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.created"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultCredentialArchivedEventData = object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.archived"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultCredentialDeletedEventData = object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.deleted"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultCredentialRefreshFailedEventData = object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.refresh\_failed"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

type: "event"

Object type. Always `event` for webhook payloads.

BetaWebhookEventData = [BetaWebhookSessionCreatedEventData](api/beta.md) { id, organization\_id, type, workspace\_id }  or [BetaWebhookSessionPendingEventData](api/beta.md) { id, organization\_id, type, workspace\_id }  or [BetaWebhookSessionRunningEventData](api/beta.md) { id, organization\_id, type, workspace\_id }  or 19 more

Accepts one of the following:

BetaWebhookSessionCreatedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.created"

workspace\_id: string

BetaWebhookSessionPendingEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.pending"

workspace\_id: string

BetaWebhookSessionRunningEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.running"

workspace\_id: string

BetaWebhookSessionIdledEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.idled"

workspace\_id: string

BetaWebhookSessionRequiresActionEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.requires\_action"

workspace\_id: string

BetaWebhookSessionArchivedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.archived"

workspace\_id: string

BetaWebhookSessionDeletedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.deleted"

workspace\_id: string

BetaWebhookSessionStatusScheduledEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_scheduled"

workspace\_id: string

BetaWebhookSessionStatusRunStartedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_run\_started"

workspace\_id: string

BetaWebhookSessionStatusIdledEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_idled"

workspace\_id: string

BetaWebhookSessionStatusTerminatedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_terminated"

workspace\_id: string

BetaWebhookSessionThreadCreatedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.thread\_created"

workspace\_id: string

BetaWebhookSessionThreadIdledEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.thread\_idled"

workspace\_id: string

BetaWebhookSessionThreadTerminatedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.thread\_terminated"

workspace\_id: string

BetaWebhookSessionOutcomeEvaluationEndedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.outcome\_evaluation\_ended"

workspace\_id: string

BetaWebhookVaultCreatedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault.created"

workspace\_id: string

BetaWebhookVaultArchivedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault.archived"

workspace\_id: string

BetaWebhookVaultDeletedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault.deleted"

workspace\_id: string

BetaWebhookVaultCredentialCreatedEventData = object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.created"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultCredentialArchivedEventData = object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.archived"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultCredentialDeletedEventData = object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.deleted"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultCredentialRefreshFailedEventData = object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.refresh\_failed"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookSessionArchivedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.archived"

workspace\_id: string

BetaWebhookSessionCreatedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.created"

workspace\_id: string

BetaWebhookSessionDeletedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.deleted"

workspace\_id: string

BetaWebhookSessionIdledEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.idled"

workspace\_id: string

BetaWebhookSessionOutcomeEvaluationEndedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.outcome\_evaluation\_ended"

workspace\_id: string

BetaWebhookSessionPendingEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.pending"

workspace\_id: string

BetaWebhookSessionRequiresActionEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.requires\_action"

workspace\_id: string

BetaWebhookSessionRunningEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.running"

workspace\_id: string

BetaWebhookSessionStatusIdledEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_idled"

workspace\_id: string

BetaWebhookSessionStatusRunStartedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_run\_started"

workspace\_id: string

BetaWebhookSessionStatusScheduledEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_scheduled"

workspace\_id: string

BetaWebhookSessionStatusTerminatedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_terminated"

workspace\_id: string

BetaWebhookSessionThreadCreatedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.thread\_created"

workspace\_id: string

BetaWebhookSessionThreadIdledEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.thread\_idled"

workspace\_id: string

BetaWebhookSessionThreadTerminatedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.thread\_terminated"

workspace\_id: string

BetaWebhookVaultArchivedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault.archived"

workspace\_id: string

BetaWebhookVaultCreatedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault.created"

workspace\_id: string

BetaWebhookVaultCredentialArchivedEventData = object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.archived"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultCredentialCreatedEventData = object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.created"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultCredentialDeletedEventData = object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.deleted"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultCredentialRefreshFailedEventData = object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.refresh\_failed"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultDeletedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault.deleted"

workspace\_id: string

UnwrapWebhookEvent = object { id, created\_at, data, type }

id: string

Unique event identifier for idempotency.

created\_at: string

RFC 3339 timestamp when the event occurred.

data: [BetaWebhookEventData](api/beta.md)

Accepts one of the following:

BetaWebhookSessionCreatedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.created"

workspace\_id: string

BetaWebhookSessionPendingEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.pending"

workspace\_id: string

BetaWebhookSessionRunningEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.running"

workspace\_id: string

BetaWebhookSessionIdledEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.idled"

workspace\_id: string

BetaWebhookSessionRequiresActionEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.requires\_action"

workspace\_id: string

BetaWebhookSessionArchivedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.archived"

workspace\_id: string

BetaWebhookSessionDeletedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.deleted"

workspace\_id: string

BetaWebhookSessionStatusScheduledEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_scheduled"

workspace\_id: string

BetaWebhookSessionStatusRunStartedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_run\_started"

workspace\_id: string

BetaWebhookSessionStatusIdledEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_idled"

workspace\_id: string

BetaWebhookSessionStatusTerminatedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.status\_terminated"

workspace\_id: string

BetaWebhookSessionThreadCreatedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.thread\_created"

workspace\_id: string

BetaWebhookSessionThreadIdledEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.thread\_idled"

workspace\_id: string

BetaWebhookSessionThreadTerminatedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.thread\_terminated"

workspace\_id: string

BetaWebhookSessionOutcomeEvaluationEndedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "session.outcome\_evaluation\_ended"

workspace\_id: string

BetaWebhookVaultCreatedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault.created"

workspace\_id: string

BetaWebhookVaultArchivedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault.archived"

workspace\_id: string

BetaWebhookVaultDeletedEventData = object { id, organization\_id, type, workspace\_id }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault.deleted"

workspace\_id: string

BetaWebhookVaultCredentialCreatedEventData = object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.created"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultCredentialArchivedEventData = object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.archived"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultCredentialDeletedEventData = object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.deleted"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

BetaWebhookVaultCredentialRefreshFailedEventData = object { id, organization\_id, type, 2 more }

id: string

ID of the resource that triggered the event.

organization\_id: string

type: "vault\_credential.refresh\_failed"

vault\_id: string

ID of the vault that owns this credential.

workspace\_id: string

type: "event"

Object type. Always `event` for webhook payloads.

---

*Copyright © Anthropic. All rights reserved.*
