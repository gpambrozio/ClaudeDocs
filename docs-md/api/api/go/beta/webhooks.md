# Webhooks

Copy page

Go

# Webhooks

##### [Unwrap](api/beta/webhooks/unwrap.md)

client.Beta.Webhooks.Unwrap(ctx) error

Function

##### ModelsExpand Collapse

type BetaWebhookEvent struct{…}

ID string

Unique event identifier for idempotency.

CreatedAt Time

RFC 3339 timestamp when the event occurred.

Data [BetaWebhookEventDataUnion](api/beta.md)

Accepts one of the following:

type BetaWebhookSessionCreatedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionCreated

WorkspaceID string

type BetaWebhookSessionPendingEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionPending

WorkspaceID string

type BetaWebhookSessionRunningEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionRunning

WorkspaceID string

type BetaWebhookSessionIdledEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionIdled

WorkspaceID string

type BetaWebhookSessionRequiresActionEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionRequiresAction

WorkspaceID string

type BetaWebhookSessionArchivedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionArchived

WorkspaceID string

type BetaWebhookSessionDeletedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionDeleted

WorkspaceID string

type BetaWebhookSessionStatusScheduledEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionStatusScheduled

WorkspaceID string

type BetaWebhookSessionStatusRunStartedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionStatusRunStarted

WorkspaceID string

type BetaWebhookSessionStatusIdledEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionStatusIdled

WorkspaceID string

type BetaWebhookSessionStatusTerminatedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionStatusTerminated

WorkspaceID string

type BetaWebhookSessionThreadCreatedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionThreadCreated

WorkspaceID string

type BetaWebhookSessionThreadIdledEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionThreadIdled

WorkspaceID string

type BetaWebhookSessionThreadTerminatedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionThreadTerminated

WorkspaceID string

type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionOutcomeEvaluationEnded

WorkspaceID string

type BetaWebhookVaultCreatedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultCreated

WorkspaceID string

type BetaWebhookVaultArchivedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultArchived

WorkspaceID string

type BetaWebhookVaultDeletedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultDeleted

WorkspaceID string

type BetaWebhookVaultCredentialCreatedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultCredentialCreated

VaultID string

ID of the vault that owns this credential.

WorkspaceID string

type BetaWebhookVaultCredentialArchivedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultCredentialArchived

VaultID string

ID of the vault that owns this credential.

WorkspaceID string

type BetaWebhookVaultCredentialDeletedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultCredentialDeleted

VaultID string

ID of the vault that owns this credential.

WorkspaceID string

type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultCredentialRefreshFailed

VaultID string

ID of the vault that owns this credential.

WorkspaceID string

Type Event

Object type. Always `event` for webhook payloads.

type BetaWebhookEventDataUnion interface{…}

Accepts one of the following:

type BetaWebhookSessionCreatedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionCreated

WorkspaceID string

type BetaWebhookSessionPendingEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionPending

WorkspaceID string

type BetaWebhookSessionRunningEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionRunning

WorkspaceID string

type BetaWebhookSessionIdledEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionIdled

WorkspaceID string

type BetaWebhookSessionRequiresActionEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionRequiresAction

WorkspaceID string

type BetaWebhookSessionArchivedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionArchived

WorkspaceID string

type BetaWebhookSessionDeletedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionDeleted

WorkspaceID string

type BetaWebhookSessionStatusScheduledEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionStatusScheduled

WorkspaceID string

type BetaWebhookSessionStatusRunStartedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionStatusRunStarted

WorkspaceID string

type BetaWebhookSessionStatusIdledEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionStatusIdled

WorkspaceID string

type BetaWebhookSessionStatusTerminatedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionStatusTerminated

WorkspaceID string

type BetaWebhookSessionThreadCreatedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionThreadCreated

WorkspaceID string

type BetaWebhookSessionThreadIdledEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionThreadIdled

WorkspaceID string

type BetaWebhookSessionThreadTerminatedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionThreadTerminated

WorkspaceID string

type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionOutcomeEvaluationEnded

WorkspaceID string

type BetaWebhookVaultCreatedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultCreated

WorkspaceID string

type BetaWebhookVaultArchivedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultArchived

WorkspaceID string

type BetaWebhookVaultDeletedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultDeleted

WorkspaceID string

type BetaWebhookVaultCredentialCreatedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultCredentialCreated

VaultID string

ID of the vault that owns this credential.

WorkspaceID string

type BetaWebhookVaultCredentialArchivedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultCredentialArchived

VaultID string

ID of the vault that owns this credential.

WorkspaceID string

type BetaWebhookVaultCredentialDeletedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultCredentialDeleted

VaultID string

ID of the vault that owns this credential.

WorkspaceID string

type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultCredentialRefreshFailed

VaultID string

ID of the vault that owns this credential.

WorkspaceID string

type BetaWebhookSessionArchivedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionArchived

WorkspaceID string

type BetaWebhookSessionCreatedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionCreated

WorkspaceID string

type BetaWebhookSessionDeletedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionDeleted

WorkspaceID string

type BetaWebhookSessionIdledEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionIdled

WorkspaceID string

type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionOutcomeEvaluationEnded

WorkspaceID string

type BetaWebhookSessionPendingEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionPending

WorkspaceID string

type BetaWebhookSessionRequiresActionEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionRequiresAction

WorkspaceID string

type BetaWebhookSessionRunningEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionRunning

WorkspaceID string

type BetaWebhookSessionStatusIdledEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionStatusIdled

WorkspaceID string

type BetaWebhookSessionStatusRunStartedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionStatusRunStarted

WorkspaceID string

type BetaWebhookSessionStatusScheduledEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionStatusScheduled

WorkspaceID string

type BetaWebhookSessionStatusTerminatedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionStatusTerminated

WorkspaceID string

type BetaWebhookSessionThreadCreatedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionThreadCreated

WorkspaceID string

type BetaWebhookSessionThreadIdledEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionThreadIdled

WorkspaceID string

type BetaWebhookSessionThreadTerminatedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionThreadTerminated

WorkspaceID string

type BetaWebhookVaultArchivedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultArchived

WorkspaceID string

type BetaWebhookVaultCreatedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultCreated

WorkspaceID string

type BetaWebhookVaultCredentialArchivedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultCredentialArchived

VaultID string

ID of the vault that owns this credential.

WorkspaceID string

type BetaWebhookVaultCredentialCreatedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultCredentialCreated

VaultID string

ID of the vault that owns this credential.

WorkspaceID string

type BetaWebhookVaultCredentialDeletedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultCredentialDeleted

VaultID string

ID of the vault that owns this credential.

WorkspaceID string

type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultCredentialRefreshFailed

VaultID string

ID of the vault that owns this credential.

WorkspaceID string

type BetaWebhookVaultDeletedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultDeleted

WorkspaceID string

type UnwrapWebhookEvent struct{…}

ID string

Unique event identifier for idempotency.

CreatedAt Time

RFC 3339 timestamp when the event occurred.

Data [BetaWebhookEventDataUnion](api/beta.md)

Accepts one of the following:

type BetaWebhookSessionCreatedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionCreated

WorkspaceID string

type BetaWebhookSessionPendingEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionPending

WorkspaceID string

type BetaWebhookSessionRunningEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionRunning

WorkspaceID string

type BetaWebhookSessionIdledEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionIdled

WorkspaceID string

type BetaWebhookSessionRequiresActionEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionRequiresAction

WorkspaceID string

type BetaWebhookSessionArchivedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionArchived

WorkspaceID string

type BetaWebhookSessionDeletedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionDeleted

WorkspaceID string

type BetaWebhookSessionStatusScheduledEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionStatusScheduled

WorkspaceID string

type BetaWebhookSessionStatusRunStartedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionStatusRunStarted

WorkspaceID string

type BetaWebhookSessionStatusIdledEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionStatusIdled

WorkspaceID string

type BetaWebhookSessionStatusTerminatedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionStatusTerminated

WorkspaceID string

type BetaWebhookSessionThreadCreatedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionThreadCreated

WorkspaceID string

type BetaWebhookSessionThreadIdledEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionThreadIdled

WorkspaceID string

type BetaWebhookSessionThreadTerminatedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionThreadTerminated

WorkspaceID string

type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type SessionOutcomeEvaluationEnded

WorkspaceID string

type BetaWebhookVaultCreatedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultCreated

WorkspaceID string

type BetaWebhookVaultArchivedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultArchived

WorkspaceID string

type BetaWebhookVaultDeletedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultDeleted

WorkspaceID string

type BetaWebhookVaultCredentialCreatedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultCredentialCreated

VaultID string

ID of the vault that owns this credential.

WorkspaceID string

type BetaWebhookVaultCredentialArchivedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultCredentialArchived

VaultID string

ID of the vault that owns this credential.

WorkspaceID string

type BetaWebhookVaultCredentialDeletedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultCredentialDeleted

VaultID string

ID of the vault that owns this credential.

WorkspaceID string

type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}

ID string

ID of the resource that triggered the event.

OrganizationID string

Type VaultCredentialRefreshFailed

VaultID string

ID of the vault that owns this credential.

WorkspaceID string

Type Event

Object type. Always `event` for webhook payloads.

---

*Copyright © Anthropic. All rights reserved.*
