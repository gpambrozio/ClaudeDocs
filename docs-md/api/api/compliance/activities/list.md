# Query compliance activities

Copy page



# Query compliance activities

GET/v1/compliance/activities

List compliance activities for the authenticated tenant.

The tenant is the caller's parent organization, or — for an organization
with no parent — the organization itself. Returns a paginated list of
compliance activities that can be filtered by various criteria.

##### Query parameters



activity\_types: optional array of "abuse\_decision\_received" or "account\_deleted" or "admin\_api\_key\_created" or 480 more

Filter activities by type. See the response `data` schema for the additional fields each type returns. Cannot be combined with `exclude_activity_types[]`.

One of the following:

"abuse\_decision\_received"

An external anti-abuse service reported a consequential decision about a sign-in or sign-up attempt.

"account\_deleted"

User-initiated self-service account deletion.

"admin\_api\_key\_created"

An admin API key was created.

"admin\_api\_key\_deleted"

An admin API key was deleted.

"admin\_api\_key\_updated"

An admin API key was updated (renamed or activated/deactivated).

"admin\_connector\_request\_resolved"

Admin approved or dismissed pending member requests to enable an MCP connector.

"admin\_request\_created"

Admin request created by an org member (seat upgrade, limit increase, join org, end-user invite).

"age\_verified"

User age was verified.

"anonymous\_mobile\_login\_attempted"

Anonymous mobile login was attempted.

"api\_key\_created"

Activity logged when a new API key is created.

"audit\_log\_export\_accessed"

Audit log export file was accessed/downloaded via signed URL.

"audit\_log\_export\_started"

Audit log export was initiated.

"billing\_emails\_updated"

The organization's billing email recipients were updated.

"ccr\_agent\_created"

A Claude Code agent was created.

"ccr\_agent\_deleted"

A Claude Code agent was deleted.

"ccr\_agent\_proxy\_credential\_created"

A Claude Code agent proxy credential was created. Credentials hold the secrets the agent proxy injects into requests Claude Code sessions send to approved external services; each credential belongs to an agent proxy profile. Audit events carry only credential names and settings, never the secret material itself.

"ccr\_agent\_proxy\_credential\_deleted"

A Claude Code agent proxy credential was deleted. Its secret material was removed and can no longer be sent to any host.

"ccr\_agent\_proxy\_credential\_rotated"

A Claude Code agent proxy credential's secret material was replaced. The replacement keeps the same name, profile, and allowed hosts under a new credential identifier, and everything that referenced the old credential now uses the replacement.

"ccr\_agent\_proxy\_credential\_updated"

A Claude Code agent proxy credential's settings were updated. Only the display name and the allowed host patterns can be updated; the secret material can only be replaced through a rotation.

"ccr\_agent\_proxy\_destination\_deleted"

An agent proxy destination was deleted.

"ccr\_agent\_proxy\_network\_events\_listed"

A Claude Code network activity export was accessed for the given hour.

"ccr\_agent\_proxy\_profile\_bound"

A Claude Code agent proxy profile was bound to a scope, applying its policy to Claude Code sessions in that scope.

"ccr\_agent\_proxy\_profile\_created"

A Claude Code agent proxy profile was created. Agent proxy profiles are named, reusable bundles of access policy that administrators bind to parts of the organization.

"ccr\_agent\_proxy\_profile\_deleted"

A Claude Code agent proxy profile was deleted, removing its policy from everything it was bound to.

"ccr\_agent\_proxy\_profile\_unbound"

A Claude Code agent proxy profile was unbound from a scope, removing its policy from Claude Code sessions in that scope.

"ccr\_agent\_proxy\_profile\_updated"

A Claude Code agent proxy profile's configuration was updated.

"ccr\_agent\_proxy\_provisioning\_credential\_rejected"

An organization owner rejected a credential that a teammate submitted via an agent proxy provisioning link: the credential and its disabled rule were deleted and the link was revoked. The actor is the owner; the submitter is recorded for attribution.

"ccr\_agent\_proxy\_provisioning\_link\_enabled"

An organization owner enabled a credential that a teammate submitted via an agent proxy provisioning link: the disabled rule created at submission was switched to enforce, so the credential now takes traffic. The actor is the owner; the submitter is the actor on the prior ccr\_agent\_proxy\_provisioning\_link\_submitted event.

"ccr\_agent\_proxy\_provisioning\_link\_generated"

An organization owner generated a one-time agent proxy credential provisioning link so a teammate can submit a credential into the target agent proxy profile without holding the owner role.

"ccr\_agent\_proxy\_provisioning\_link\_revoked"

An organization owner revoked an unfilled agent proxy provisioning link.

"ccr\_agent\_proxy\_provisioning\_link\_submitted"

A teammate submitted a credential via an agent proxy provisioning link. The credential and a disabled rule are created; the credential takes traffic only after an organization owner enables the submitted credential. This event records the link-mediated lifecycle; the credential itself additionally emits ccr\_agent\_proxy\_credential\_created.

"ccr\_agent\_proxy\_rule\_deleted"

An agent proxy rule was deleted.

"ccr\_agent\_slack\_access\_scope\_created"

A Claude Code agent was granted access to read or write in an additional Slack channel beyond the one it is assigned to.

"ccr\_agent\_slack\_access\_scope\_deleted"

A Claude Code agent's access to an additional Slack channel was revoked.

"ccr\_agent\_slack\_binding\_created"

A Claude Code agent was assigned to a Slack channel or workspace as its dedicated agent.

"ccr\_agent\_slack\_binding\_deleted"

A Claude Code agent's assignment to a Slack channel or workspace was removed.

"ccr\_agent\_updated"

A Claude Code agent's configuration was updated. Also emitted with updated\_fields ["is\_virtual"] alone when an auto-provisioned agent is promoted to a configured one, whether by an update request targeting it or by binding an agent proxy profile to it.

"ccr\_role\_channel\_assignment\_deleted"

CcrRoleChannelAssignmentDeleted is emitted when an org owner/admin removes an RBAC role's channel assignment row (the role reverts to granting zero channels).

"ccr\_role\_channel\_assignment\_updated"

CcrRoleChannelAssignmentUpdated is emitted when an org owner/admin sets or replaces the list of Slack channels an RBAC role's holders may configure via the delegated Claude-in-Slack channel-manage surface.

"ccr\_session\_created"

A Claude Code session was created. A session is one coding interaction with Claude.

"ccr\_session\_deleted"

A Claude Code session was deleted.

"ccr\_session\_updated"

A Claude Code session's settings were updated.

"claude\_artifact\_access\_failed"

An attempt to access an artifact failed.

"claude\_artifact\_commented"

Comment activity on a published artifact: a comment was added, a thread's resolved state was changed, or a thread was deleted. The actor is the user who performed the action; the comment text itself is stored with the artifact and is not part of this record.

"claude\_artifact\_comments\_viewed"

An artifact's comments were viewed.

"claude\_artifact\_created"

An artifact was created.

"claude\_artifact\_duplicated"

A user duplicated an artifact they could view into a new artifact that they own. The actor is the user who created the copy; the source artifact is not modified.

"claude\_artifact\_published"

A new version of an artifact was published — for an artifact created in a chat this is the action that made it publicly viewable; for an artifact created outside a chat it is recorded on every save, including saves of private artifacts, and changes to who can access the artifact are recorded separately as claude\_artifact\_sharing\_updated.

"claude\_artifact\_sharing\_updated"

An artifact's sharing settings were updated.

"claude\_artifact\_viewed"

An artifact was viewed.

"claude\_chat\_access\_failed"

A user was denied access to a Claude.ai chat conversation.

"claude\_chat\_created"

User created a chat.

"claude\_chat\_deleted"

A user deleted a Claude.ai chat conversation.

"claude\_chat\_deletion\_failed"

A request to delete a Claude.ai chat conversation failed.

"claude\_chat\_settings\_updated"

User updated the settings for a conversation.

"claude\_chat\_snapshot\_created"

User created/shared a chat snapshot.

"claude\_chat\_snapshot\_deleted"

User deleted/unshared a chat snapshot.

"claude\_chat\_snapshot\_viewed"

User viewed a chat snapshot (authenticated or public/unauthenticated).

"claude\_chat\_sync\_source\_created"

A sync source was connected for syncing external content into Claude chats.

"claude\_chat\_sync\_source\_deleted"

A sync source was disconnected from Claude chats.

"claude\_chat\_sync\_source\_updated"

A Claude chat sync source's configuration was updated.

"claude\_chat\_updated"

User updated the chat metadata (e.g name, model).

"claude\_chat\_viewed"

A user viewed a Claude.ai chat conversation.

"claude\_code\_credential\_revoked"

A Claude Code credential (runner pool key, runner token, or session token) was revoked. The credential itself is never recorded.

"claude\_code\_review\_config\_updated"

Claude Code Review configuration was enabled/disabled for an org.

"claude\_code\_review\_repository\_added"

A repository was added to org-level Claude Code Review configuration.

"claude\_code\_review\_repository\_removed"

A repository was removed from org-level Claude Code Review configuration.

"claude\_code\_review\_repository\_updated"

A Claude Code Review repository configuration was updated.

"claude\_code\_runner\_deleted"

A self-hosted runner was forcibly removed from its pool. Sessions assigned to the runner were returned to the pool queue, unless a session had already been requeued repeatedly, in which case it was marked stuck instead of being requeued again.

"claude\_code\_runner\_pool\_created"

A self-hosted runner pool for Claude Code was created.

"claude\_code\_runner\_pool\_deleted"

A self-hosted runner pool was deleted.

"claude\_code\_runner\_pool\_secret\_minted"

A registration key for a self-hosted runner pool was minted. Runners present this key to join the pool. The key itself is never recorded.

"claude\_code\_runner\_pool\_session\_queue\_updated"

An admin changed a session's position in its self-hosted runner pool's queue: requeued it onto a different runner, dismissed it from the queue, or re-admitted it for another runner provisioning attempt.

"claude\_code\_runner\_pool\_updated"

A self-hosted runner pool's settings were updated.

"claude\_code\_security\_center\_config\_updated"

Claude Code Security Center scanning was enabled/disabled for an org.

"claude\_code\_security\_scan\_cancelled"

In-flight Claude Code Security scans were cancelled for a project.

"claude\_code\_security\_scan\_created"

A Claude Code Security scan was started.

"claude\_code\_security\_scan\_project\_member\_updated"

A person's access to a Claude Code Security scan project was granted, changed, or revoked.

"claude\_code\_security\_scan\_project\_updated"

A Claude Code Security scan project was archived, unarchived, created, or migrated to a new product experience.

"claude\_code\_security\_scan\_project\_visibility\_updated"

A Claude Code Security scan project was shared with the organization or made private.

"claude\_code\_security\_scan\_run\_updated"

A single Claude Code Security scan run was archived, unarchived, or resumed after a billing pause.

"claude\_code\_security\_scan\_schedule\_deleted"

A recurring scan schedule was deleted for a Claude Code Security project.

"claude\_code\_security\_scan\_schedule\_updated"

A recurring scan schedule was set or replaced for a Claude Code Security project.

"claude\_code\_security\_vulnerability\_fix\_session\_created"

A Claude Code remediation session was created for a Claude Code Security vulnerability finding.

"claude\_code\_security\_vulnerability\_updated"

A Claude Code Security vulnerability finding was dismissed, restored, marked fixed, or reopened.

"claude\_code\_security\_webhook\_created"

A Claude Code Security outbound webhook was created.

"claude\_code\_security\_webhook\_deleted"

A Claude Code Security outbound webhook was deleted.

"claude\_code\_security\_webhook\_secret\_updated"

The HMAC signing secret for a Claude Code Security webhook was rotated.

"claude\_code\_security\_webhook\_updated"

A Claude Code Security outbound webhook was updated.

"claude\_code\_team\_memory\_acl\_updated"

An RBAC group was added to or removed from the Claude Code team-memory ACL.

"claude\_code\_team\_memory\_updated"

Claude Code team memory shared with the organization was updated.

"claude\_code\_team\_onboarding\_guide\_updated"

A Claude Code team onboarding guide was created, updated, or deleted.

"claude\_code\_user\_marketplaces\_updated"

A user's Claude Code plugin marketplace selections were updated on Anthropic servers.

"claude\_code\_user\_memory\_updated"

A user's synced private Claude Code memory was updated or deleted on Anthropic servers.

"claude\_code\_user\_plugins\_updated"

A user's Claude Code plugin selections — which plugins are installed and enabled — were updated on Anthropic servers.

"claude\_code\_user\_settings\_updated"

A user's synced Claude Code settings were updated or deleted on Anthropic servers.

"claude\_command\_created"

Command was created.

"claude\_command\_deleted"

Command was deleted.

"claude\_command\_replaced"

Command was replaced.

"claude\_enterprise\_upgrade\_credit\_updated"

An organization admin cancelled, or turned back on, the monthly usage credit the organization receives for upgrading from the Team plan to the Enterprise plan, together with the recurring monthly charge that accompanies it.

"claude\_file\_access\_failed"

A user was denied access to a file in Claude.ai.

"claude\_file\_deleted"

A file was deleted.

"claude\_file\_exported"

A file was exported from Claude to an external storage destination.

"claude\_file\_uploaded"

A file was uploaded.

"claude\_file\_viewed"

A user viewed a file in Claude.ai.

"claude\_gdrive\_integration\_created"

A Google Drive integration was enabled for the organization.

"claude\_gdrive\_integration\_deleted"

A Google Drive integration was disabled for the organization.

"claude\_gdrive\_integration\_updated"

A Google Drive integration's configuration was updated.

"claude\_github\_integration\_created"

A GitHub integration was enabled for the organization.

"claude\_github\_integration\_deleted"

A GitHub integration was disabled for the organization.

"claude\_github\_integration\_updated"

A GitHub integration's configuration was updated.

"claude\_organization\_settings\_updated"

Organization settings were updated.

"claude\_plugin\_created"

Plugin was created.

"claude\_plugin\_deleted"

Plugin was deleted.

"claude\_plugin\_disabled"

User disabled a plugin for their account.

"claude\_plugin\_enabled"

User enabled a plugin for their account.

"claude\_plugin\_replaced"

Plugin was replaced.

"claude\_plugin\_updated"

Plugin was updated.

"claude\_project\_archived"

A Claude project was archived.

"claude\_project\_created"

A Claude project was created.

"claude\_project\_deleted"

A Claude project was deleted.

"claude\_project\_document\_access\_failed"

An attempt to access a document in a Claude project failed.

"claude\_project\_document\_bulk\_deletion\_audit\_truncated"

A bulk request to delete documents from a Claude project failed with more documents requested than were individually recorded in the audit log.

"claude\_project\_document\_deleted"

A document was deleted from a Claude project.

"claude\_project\_document\_deletion\_failed"

A request to delete a document from a Claude project failed.

"claude\_project\_document\_updated"

The content of a document in a Claude project was replaced in place.

"claude\_project\_document\_uploaded"

A document was uploaded to a Claude project.

"claude\_project\_document\_viewed"

A document in a Claude project was viewed.

"claude\_project\_file\_access\_failed"

An attempt to access a file in a Claude project failed.

"claude\_project\_file\_bulk\_deletion\_audit\_truncated"

A bulk request to delete files from a Claude project failed with more files requested than were individually recorded in the audit log.

"claude\_project\_file\_deleted"

A file was deleted from a Claude project.

"claude\_project\_file\_deletion\_failed"

A request to delete a file from a Claude project failed.

"claude\_project\_file\_uploaded"

A file was uploaded to a Claude project.

"claude\_project\_reported"

A Claude project was reported.

"claude\_project\_sharing\_updated"

A Claude project's sharing settings were updated.

"claude\_project\_sync\_source\_created"

A sync source was connected to a Claude project's knowledge base.

"claude\_project\_sync\_source\_deleted"

A sync source was disconnected from a Claude project's knowledge base.

"claude\_project\_sync\_source\_updated"

A Claude project sync source's configuration was updated.

"claude\_project\_viewed"

A Claude project was viewed.

"claude\_published\_artifact\_deleted"

A published artifact was deleted or unpublished — by its creator, by an organization admin, or by Anthropic (for example, when it was removed for a policy violation).

"claude\_pubsec\_identity\_configured"

SAML IdP configuration updated for a public sector organization.

"claude\_skill\_created"

Skill was created.

"claude\_skill\_deleted"

Skill was deleted.

"claude\_skill\_disabled"

User disabled a skill for their account.

"claude\_skill\_enabled"

User enabled a skill for their account.

"claude\_skill\_replaced"

Skill was replaced.

"claude\_user\_role\_updated"

A user's role within the organization was changed, or the user was added to or removed from the organization.

"claude\_user\_seat\_tier\_updated"

An organization member's seat tier was changed. A null `previous_seat_tier` means the member previously had no seat assigned; a null `current_seat_tier` means the seat was removed.

"claude\_user\_settings\_updated"

User updated their personal settings.

"cli\_plugin\_exec\_policy\_updated"

Admin set or cleared the per-op permission ceiling for a plugin CLI.

"compliance\_api\_accessed"

Logging event auto-generated for each compliance API request.

"cowork\_session\_updated"

A Cowork session was updated.

"design\_project\_artifact\_published"

A Claude Design project's content was published as a claude.ai artifact, making a snapshot of one of its files viewable outside the project's sharing settings.

"design\_project\_created"

A Claude Design project was created.

"design\_project\_deleted"

A Claude Design project was deleted.

"design\_project\_member\_added"

A member was granted access to a Claude Design project.

"design\_project\_member\_removed"

A member's access to a Claude Design project was revoked.

"design\_project\_member\_role\_updated"

A Claude Design project member's role was changed.

"design\_project\_published"

A Claude Design template or design system was published, making it discoverable by everyone in its organization.

"design\_project\_sharing\_updated"

A Claude Design project's link-sharing settings were changed — who the project's link works for, and what people opening it through the link may do. Access granted to individual members is reported separately (see design\_project\_member\_added).

"design\_project\_unpublished"

A Claude Design template or design system was unpublished, removing it from its organization's shared gallery.

"design\_project\_updated"

A Claude Design project's metadata was updated.

"design\_project\_version\_restored"

A Claude Design project's working tree was rolled back to a previously saved version, replacing its current files with that version's files.



"design\_project\_viewed"

A Claude Design project's content was read. The surface field records which kind of read — a project open, a full-content read, a single-file read, a saved-version read, or an export request. The actor is the reader.

This activity type is retired: project content reads are no longer
recorded. Events of this type may still appear in feeds for reads that
occurred while it was active.

"desktop\_extension\_allowlisted"

A desktop extension was added to an org's allowlist.

"desktop\_extension\_blocklisted"

A desktop extension was added to the global blocklist.

"desktop\_extension\_deleted"

A desktop extension was deleted, either globally by an admin or org-scoped by an org owner.

"desktop\_extension\_removed\_from\_allowlist"

A desktop extension was removed from an org's allowlist.

"desktop\_extension\_unblocked"

A desktop extension was removed from the global blocklist.

"desktop\_extension\_uploaded"

A desktop extension was uploaded, either globally by an admin or org-scoped by an org owner.

"desktop\_extension\_version\_uploaded"

A new version of an existing org-owned desktop extension was uploaded.

"domain\_claim\_initiated"

Domain capture claim initiated over personal accounts on verified domains.

"end\_user\_invite\_requested"

Non-admin member submitted an invite request for a new org member.

"extra\_usage\_billing\_enabled"

Usage credit billing was enabled for an organization.

"extra\_usage\_credit\_granted"

A promotional usage credit grant was claimed.

"extra\_usage\_spend\_limit\_created"

Usage credit spend limit was created.

"extra\_usage\_spend\_limit\_deleted"

Usage credit spend limit was deleted.

"extra\_usage\_spend\_limit\_increase\_request\_approved"

A usage credit spend limit increase request was approved.

"extra\_usage\_spend\_limit\_increase\_request\_denied"

A usage credit spend limit increase request was denied.

"extra\_usage\_spend\_limit\_updated"

Usage credit spend limit was updated.

"ghe\_configuration\_created"

Admin created a GHE configuration.

"ghe\_configuration\_deleted"

Admin deleted a GHE configuration.

"ghe\_configuration\_updated"

Admin updated a GHE configuration. Previous/new field pairs are recorded only for settings that changed in the update; secret credentials are never recorded, only whether they were replaced.

"ghe\_user\_connected"

User connected to a GHE instance.

"ghe\_user\_disconnected"

User disconnected from a GHE instance.

"ghe\_webhook\_signature\_invalid"

Webhook signature validation failed.

"github\_token\_import"

A user attempted to import a personal GitHub access token for use with Claude Code. The `result` field indicates the outcome of the import (imported, rejected, or failed).

"group\_created"

A group was created (RBAC admin or SCIM provisioning).

"group\_deleted"

A group was deleted (RBAC admin or SCIM provisioning).

"group\_list\_viewed"

Admin viewed the list of RBAC groups.

"group\_member\_added"

One or more members were added to a group.

"group\_member\_addition\_failed"

A request to add members to a group failed. Some of the requested members may have been added before the failure.

"group\_member\_list\_viewed"

Admin viewed the members of an RBAC group.

"group\_member\_removal\_failed"

A request to remove members from a group failed. Some of the requested members may have been removed before the failure.

"group\_member\_removed"

One or more members were removed from a group.

"group\_project\_shares\_revoked"

An RBAC group's project shares in one organization were revoked in bulk.

"group\_skill\_shares\_revoked"

An RBAC group's skill shares in one organization were revoked in bulk.

"group\_updated"

A group was updated (RBAC admin or SCIM provisioning).

"group\_viewed"

A group was viewed.

"group\_visibility\_updated"

An RBAC group's visibility policy was updated.

"inference\_hooks\_circuit\_breaker\_tripped"

The organization's Inference hooks circuit breaker tripped automatically: calls to the organization's Inference hooks endpoint crossed a failure threshold, and inspection was suspended to protect live traffic. While tripped, requests are handled according to the organization's failure handling setting — allowed through uninspected (fail open) or rejected (fail closed) — and no per-request Inference hooks activities are recorded. The tripped state persists until an administrator re-enables Inference hooks inspection (or explicitly resets the circuit breaker).

"inference\_hooks\_config\_deleted"

Inference hooks configuration was removed for the
organization.

"inference\_hooks\_config\_updated"

Inference hooks configuration was created or updated for the
organization.

"inference\_hooks\_request\_denied"

Inference hooks inspection denied a request. The request was blocked and no model response was produced.

"inference\_hooks\_request\_failed\_open"

A request proceeded without Inference hooks inspection because a verdict could not be obtained and the organization's Inference hooks configuration is set to fail open.

"inference\_hooks\_signing\_secret\_generated"

A request signing secret was generated for the organization's
Inference hooks configuration.

"integration\_user\_connected"

User connected to an integration.

"integration\_user\_disconnected"

User disconnected from an integration.

"invoice\_collection\_method\_updated"

Invoice collection method was changed.

"lti\_launch\_initiated"

LTI launch was initiated.

"lti\_launch\_success"

LTI launch completed successfully.

"lti\_platform\_created"

Anthropic staff created an LTI platform integration on behalf of an org.

"lti\_platform\_updated"

Anthropic staff updated an LTI platform integration on behalf of an org.

"magic\_link\_login\_failed"

A magic link sign-in attempt failed.

"magic\_link\_login\_initiated"

A user requested a magic link sign-in email.

"magic\_link\_login\_succeeded"

A user successfully signed in with a magic link email.

"managed\_organization\_setup\_completed"

Managed (AWS Marketplace) organization setup was completed.

"marketplace\_created"

Admin created an organization marketplace.

"marketplace\_deleted"

Admin deleted an organization marketplace.

"marketplace\_updated"

Admin updated an organization marketplace.

"marketplace\_webhook\_deleted"

Admin removed the GitHub push webhook for a marketplace.

"marketplace\_webhook\_provisioned"

Admin provisioned a GitHub push webhook for a marketplace.

"mcp\_directory\_server\_published"

The organization published its approved MCP directory listing.

"mcp\_server\_created"

An MCP server was added to the organization.

"mcp\_server\_deleted"

An MCP server was removed from the organization.

"mcp\_server\_managed\_auth\_token\_exchanged"

A user attempted to obtain an access token for an MCP server via enterprise managed authorization. This event reports the outcomes of attempted token exchanges. Repeated failures with the same cause may be reported once until the cause changes, and requests denied by organization policy before a token exchange is attempted are not reported, with the exception of the "connector\_scope\_not\_granted" failures described under error\_type.

"mcp\_server\_managed\_auth\_updated"

An MCP server's enterprise managed authorization settings were set, changed, or cleared, including when they were supplied while the server was being added or edited. Fields without a "previous\_" prefix describe the settings after the change and are null when the server has no managed authorization settings afterwards; "previous\_" fields describe the settings before the change and are null when the server had none before (always the case for a newly added server).

"mcp\_server\_updated"

An MCP server's configuration was updated.

"mcp\_tool\_policy\_updated"

The permission restriction for an MCP tool was set or cleared.

"org\_analytics\_api\_capability\_updated"

Organization analytics\_api capability was enabled or disabled.

"org\_bulk\_delete\_initiated"

Organization bulk deletion was initiated.

"org\_capability\_grant\_added"

A capability grant was added to a workspace or role.

"org\_capability\_grant\_removed"

A capability grant was removed from a workspace or role.

"org\_claude\_code\_data\_sharing\_disabled"

Organization Claude Code data sharing was disabled.

"org\_claude\_code\_data\_sharing\_enabled"

Organization Claude Code data sharing was enabled.

"org\_claude\_code\_desktop\_disabled"

Organization Claude Code Desktop was disabled.

"org\_claude\_code\_desktop\_enabled"

Organization Claude Code Desktop was enabled.

"org\_claude\_code\_zero\_data\_retention\_disabled"

A primary owner disabled zero data retention for Claude Code, so Claude
Code content is retained according to the organization's data retention
settings.

"org\_compliance\_api\_settings\_updated"

Organization compliance API settings were updated.

"org\_connector\_domain\_guard\_updated"

Enterprise admin changed whether connectors are restricted to verified domains.

"org\_cowork\_act\_without\_asking\_mode\_disabled"

The "Act without asking" mode in Cowork was disabled for the organization, so members can no longer let Claude act without asking for approval.

"org\_cowork\_act\_without\_asking\_mode\_enabled"

The "Act without asking" mode in Cowork was enabled for the organization, allowing members to let Claude act without asking for approval.

"org\_cowork\_agent\_disabled"

Organization Cowork Agent was disabled.

"org\_cowork\_agent\_enabled"

Organization Cowork Agent was enabled.

"org\_cowork\_auto\_mode\_disabled"

The "Auto" permission mode in Cowork was disabled for the organization, so members can no longer let Claude approve its own actions after a safety check.

"org\_cowork\_auto\_mode\_enabled"

The "Auto" permission mode in Cowork was enabled for the organization, allowing members to let Claude approve its own actions after a safety check.

"org\_cowork\_disabled"

Organization cowork was disabled.

"org\_cowork\_enabled"

Organization cowork was enabled.

"org\_cowork\_mcp\_always\_allow\_disabled"

The "Always allow" option for connector tools in Cowork was disabled for the organization, so each use of a connector tool that can make changes requires approval. Read-only connector tools are not affected by this setting.

"org\_cowork\_mcp\_always\_allow\_enabled"

The "Always allow" option for connector tools in Cowork was enabled for the organization, letting members approve a connector tool that can make changes once and allow its later uses automatically. Read-only connector tools are not affected by this setting.

"org\_cowork\_otlp\_settings\_updated"

The organization's Cowork OpenTelemetry monitoring export settings were updated.

"org\_cowork\_remote\_disabled"

Running Cowork in the cloud was disabled for the organization, so members can no longer run Cowork sessions in Anthropic-hosted remote environments.

"org\_cowork\_remote\_enabled"

Running Cowork in the cloud was enabled for the organization, allowing members to run Cowork sessions in Anthropic-hosted remote environments.

"org\_creation\_blocked"

Organization creation was blocked.

"org\_data\_export\_accessed"

Organization data export file was accessed/downloaded via signed URL.

"org\_data\_export\_completed"

Organization data export was completed.

"org\_data\_export\_started"

Organization data export was started.

"org\_data\_residency\_updated"

The organization's inference data residency settings were updated.

"org\_deleted\_via\_bulk"

Organization was deleted via bulk operation.

"org\_deletion\_requested"

Organization deletion was requested.

"org\_directory\_resync\_completed"

Organization directory resync completed successfully.

"org\_directory\_resync\_failed"

Organization directory resync failed.

"org\_directory\_resync\_started"

Organization directory resync was started asynchronously.

"org\_directory\_sync\_activated"

Organization directory sync was activated.

"org\_directory\_sync\_add\_initiated"

Organization directory sync setup was initiated.

"org\_directory\_sync\_deleted"

Organization directory sync was deleted.

"org\_discoverability\_disabled"

Admin disabled organization discoverability.

"org\_discoverability\_enabled"

Admin enabled organization discoverability.

"org\_discoverability\_settings\_updated"

Admin updated organization discoverability settings.

"org\_domain\_add\_initiated"

Organization domain verification was initiated.

"org\_domain\_removed"

Organization domain was removed.

"org\_domain\_verified"

Organization domain was verified.

"org\_external\_key\_created"

A CMEK external key config was created.

"org\_external\_key\_deleted"

A CMEK external key config was deleted.

"org\_external\_key\_updated"

A CMEK external key config was updated.

"org\_external\_key\_validated"

A CMEK external key config was validated against the customer's KMS.

"org\_hipaa\_self\_serve\_enabled"

A primary owner click-accepted the BAA and enabled HIPAA protections
for the organization via the self-serve flow.

"org\_invite\_link\_disabled"

Organization invite link was disabled.

"org\_invite\_link\_generated"

Organization invite link was generated.

"org\_invite\_link\_regenerated"

Organization invite link was regenerated (previous link invalidated).

"org\_invite\_viewed"

An organization invite was viewed.

"org\_invites\_listed"

Organization invites were listed.

"org\_ip\_restriction\_created"

Organization IP restriction was created.

"org\_ip\_restriction\_deleted"

Organization IP restriction was deleted.

"org\_ip\_restriction\_updated"

Organization IP restriction was updated.

"org\_join\_proposal\_decided"

Approve or reject decision on a parent-org join proposal.

"org\_join\_request\_approved"

Admin approved a join request.

"org\_join\_request\_created"

User requested to join an organization.

"org\_join\_request\_dismissed"

Admin dismissed a join request.

"org\_join\_request\_instant\_approved"

Join request was instantly approved.

"org\_join\_requests\_bulk\_dismissed"

Admin bulk-dismissed join requests.

"org\_magic\_link\_second\_factor\_toggled"

Organization magic link second factor was toggled.

"org\_member\_invites\_disabled"

Admin disabled member invites for the organization.

"org\_member\_invites\_enabled"

Admin enabled member invites for the organization.

"org\_members\_exported"

Organization members list was exported as CSV.

"org\_model\_default\_updated"

An organization or role default model setting was changed by an administrator.

"org\_parent\_join\_proposal\_created"

Organization parent join proposal was created.

"org\_parent\_search\_performed"

Organization parent search was performed.

"org\_sso\_add\_initiated"

Organization SSO setup was initiated.

"org\_sso\_connection\_activated"

Organization SSO connection was activated.

"org\_sso\_connection\_deactivated"

Organization SSO connection was deactivated.

"org\_sso\_connection\_deleted"

Organization SSO connection was deleted.

"org\_sso\_group\_role\_mappings\_updated"

Organization SSO group role mappings were updated.

"org\_sso\_provisioning\_mode\_changed"

Organization SSO provisioning mode was changed.

"org\_sso\_scim\_welcome\_email\_toggled"

Organization SCIM-provisioned welcome email was toggled.

"org\_sso\_seat\_tier\_assignment\_toggled"

Organization SSO seat tier assignment was toggled.

"org\_sso\_seat\_tier\_mappings\_updated"

Organization SSO seat tier mappings were updated.

"org\_sso\_toggled"

Organization SSO was toggled on or off.

"org\_sync\_deleting\_synchronized\_files\_started"

Organization started deleting synchronized files.

"org\_sync\_synchronized\_files\_deleted"

Organization synchronized files were deleted.

"org\_taint\_added"

A taint was added to an organization.

"org\_taint\_removed"

A taint was removed from an organization.

"org\_user\_deleted"

User was removed from organization.

"org\_user\_invite\_accepted"

Organization user invite was accepted.

"org\_user\_invite\_deleted"

Organization user invite was deleted.

"org\_user\_invite\_re\_sent"

Organization user invite was re-sent.

"org\_user\_invite\_rejected"

Organization user invite was rejected.

"org\_user\_invite\_sent"

Organization user invite was sent.

"org\_user\_left"

User removed themselves from organization.

"org\_user\_trusted\_devices\_revoked"

An organization admin revoked a member's trusted devices and signed the member out of all active sessions.

"org\_user\_viewed"

An organization user was viewed.

"org\_users\_listed"

Organization users were listed.

"org\_work\_across\_apps\_disabled"

The organization's "Let Claude work across apps" setting was turned off.

"org\_work\_across\_apps\_enabled"

The organization's "Let Claude work across apps" setting was turned on.

"organization\_address\_updated"

The organization's billing or shipping address was updated.

"organization\_icon\_deleted"

Organization's custom icon deleted.

"organization\_icon\_updated"

Organization's custom icon uploaded or replaced.

"owned\_projects\_access\_restored"

Access to owned projects was restored.

"payment\_method\_updated"

The organization's default payment method was updated.

"pending\_share\_created"

A pending share of a project or skill was created for an email address that is not yet an organization member.

"pending\_share\_revoked"

A pending share of a project or skill was revoked before the invitee joined the organization.

"phone\_code\_sent"

User requested a phone verification code.

"phone\_code\_verified"

User successfully verified their phone code.

"platform\_agent\_archived"

An agent was archived on the API platform.

"platform\_agent\_created"

An agent was created on the API platform.

"platform\_agent\_deleted"

An agent was deleted from the API platform.

"platform\_agent\_deployment\_archived"

An agent deployment was archived on the API platform.

"platform\_agent\_deployment\_created"

An agent deployment was created on the API platform.

"platform\_agent\_deployment\_deleted"

An agent deployment was deleted from the API platform.

"platform\_agent\_deployment\_paused"

An agent deployment was paused on the API platform.

"platform\_agent\_deployment\_run\_triggered"

An agent deployment was run on demand on the API platform.

"platform\_agent\_deployment\_unpaused"

An agent deployment was resumed on the API platform.

"platform\_agent\_deployment\_updated"

An agent deployment was updated on the API platform.

"platform\_agent\_session\_archived"

An agent session was archived on the API platform.

"platform\_agent\_session\_created"

An agent session was created on the API platform.

"platform\_agent\_session\_deleted"

An agent session was deleted from the API platform.

"platform\_agent\_session\_resource\_added"

A resource was attached to an agent session.

"platform\_agent\_session\_resource\_deleted"

A resource attached to an agent session was removed.

"platform\_agent\_session\_resource\_updated"

A resource attached to an agent session was updated.

"platform\_agent\_session\_thread\_archived"

A thread within an agent session was archived.

"platform\_agent\_session\_updated"

An agent session was updated on the API platform.

"platform\_agent\_updated"

An agent was updated on the API platform.

"platform\_api\_key\_created"

An API key was created.

"platform\_api\_key\_updated"

An API key was updated.

"platform\_app\_attest\_authentication"

An attested mobile device attempted to exchange an Apple App Attest assertion for Anthropic API credentials.

"platform\_billing\_upgraded\_to\_prepaid"

The organization's API billing was upgraded to the prepaid plan.

"platform\_clearance\_workspace\_program\_request\_cleared"

A workspace's clearance program assignment was removed.

"platform\_clearance\_workspace\_program\_request\_set"

A workspace's clearance program assignment was created or updated.

"platform\_cost\_report\_viewed"

The cost report was viewed.

"platform\_dream\_archived"

A Dream (asynchronous memory-consolidation job) was archived.

"platform\_dream\_cancelled"

A Dream (asynchronous memory-consolidation job) was cancelled before it completed.

"platform\_dream\_created"

A Dream (asynchronous memory-consolidation job) was created.

"platform\_federated\_authentication"

A federated workload identity attempted to exchange an OIDC token for Anthropic API credentials.

"platform\_federation\_issuer\_archived"

An OIDC federation issuer was archived.

"platform\_federation\_issuer\_updated"

An OIDC federation issuer was updated.

"platform\_federation\_rule\_archived"

An OIDC federation rule was archived.

"platform\_federation\_rule\_updated"

An OIDC federation rule was updated.

"platform\_federation\_rule\_workspace\_added"

A federation rule was enabled for a workspace.

"platform\_federation\_rule\_workspace\_removed"

A federation rule was disabled for a workspace.

"platform\_file\_content\_downloaded"

Activity logged when file content is downloaded via GET /v1/files/{file\_id}/content.

"platform\_file\_deleted"

Activity logged when a file is deleted via DELETE /v1/files/{file\_id}.

"platform\_file\_uploaded"

Activity logged when a file is uploaded via POST /v1/files.

"platform\_memory\_created"

An agent memory document was created.

"platform\_memory\_deleted"

An agent memory document was deleted.

"platform\_memory\_store\_archived"

An agent memory store was archived. Archived stores reject new memory writes and cannot be attached to new sessions; deletion and redaction remain permitted for privacy scrubbing.

"platform\_memory\_store\_created"

An agent memory store was created.

"platform\_memory\_store\_deleted"

An agent memory store was deleted. Memory content removal may complete asynchronously for very large stores.

"platform\_memory\_store\_updated"

An agent memory store's name, description, or metadata was updated.

"platform\_memory\_updated"

An agent memory document's content or path was updated.

"platform\_memory\_version\_redacted"

A historical version of an agent memory document was redacted. Redaction scrubs the stored content of a specific version while preserving the version's existence in the history.

"platform\_oauth\_app\_created"

An OAuth app was created.

"platform\_oauth\_app\_revoked"

An OAuth app was revoked.

"platform\_oauth\_app\_updated"

An OAuth app was updated.

"platform\_plugin\_directory\_submission\_created"

A plugin directory submission was created on the API platform. A plugin directory submission is a request to list a plugin in the public plugin directory.

"platform\_plugin\_directory\_submission\_deleted"

A plugin directory submission was deleted on the API platform.

"platform\_plugin\_directory\_submission\_updated"

A plugin directory submission was updated on the API platform.

"platform\_service\_account\_archived"

A service account was archived.

"platform\_service\_account\_updated"

A service account was updated.

"platform\_service\_account\_workspace\_member\_added"

A service account was added as a member of a workspace.

"platform\_service\_account\_workspace\_member\_removed"

A service account was removed from a workspace.

"platform\_service\_account\_workspace\_member\_updated"

A service account's workspace membership role was updated.

"platform\_signing\_key\_created"

Activity logged when a new request-signing key is registered for the org.

"platform\_signing\_key\_deleted"

Activity logged when a signing key is permanently deleted.

"platform\_signing\_key\_rotated"

Activity logged when an in-memory signing key is rotated.

"platform\_skill\_version\_created"

Activity logged when a skill version is created via POST /v1/skills/{skill\_id}/versions.

"platform\_skill\_version\_deleted"

Activity logged when a skill version is deleted via DELETE /v1/skills/{skill\_id}/versions/{version}.

"platform\_spend\_limit\_alert\_emails\_updated"

Spend limit alert email addresses and role targets were updated for an org.

"platform\_spend\_limit\_created"

An org-level fixed-dollar spend limit was created.

"platform\_spend\_limit\_deleted"

An org-level spend limit was removed.

"platform\_spend\_limit\_updated"

An org-level spend limit snooze/ignore state was changed.

"platform\_usage\_report\_claude\_code\_viewed"

The Claude Code usage report was viewed.

"platform\_usage\_report\_messages\_viewed"

The messages usage report was viewed.

"platform\_workspace\_archived"

A workspace was archived.

"platform\_workspace\_created"

A workspace was created.

"platform\_workspace\_inference\_data\_retention\_disabled"

The zero data retention override was disabled for a workspace.

"platform\_workspace\_inference\_data\_retention\_enabled"

The zero data retention override was enabled for a workspace.

"platform\_workspace\_member\_added"

A member was added to a workspace.

"platform\_workspace\_member\_removed"

A member was removed from a workspace.

"platform\_workspace\_member\_updated"

A workspace member was updated.

"platform\_workspace\_member\_viewed"

A workspace member was viewed.

"platform\_workspace\_members\_listed"

Workspace members were listed.

"platform\_workspace\_rate\_limit\_deleted"

A workspace rate limit was deleted.

"platform\_workspace\_rate\_limit\_updated"

A workspace rate limit was created or updated.

"platform\_workspace\_updated"

A workspace was updated.

"plugin\_installation\_preference\_updated"

An org admin changed the installation preference for a plugin.

"prepaid\_auto\_recharge\_disabled"

Auto-recharge was disabled for API prepaid org.

"prepaid\_auto\_recharge\_updated"

Auto-recharge settings were updated for API prepaid org.

"prepaid\_extra\_usage\_auto\_reload\_disabled"

Prepaid usage credit auto-reload was disabled.

"prepaid\_extra\_usage\_auto\_reload\_enabled"

Prepaid usage credit auto-reload was enabled.

"prepaid\_extra\_usage\_auto\_reload\_settings\_updated"

Prepaid usage credit auto-reload settings were updated.

"primary\_owner\_transferred"

Primary owner role was transferred to another org member.

"rbac\_role\_assigned"

Admin assigned an RBAC custom role to a principal.

"rbac\_role\_created"

Admin created an RBAC custom role.

"rbac\_role\_deleted"

Admin deleted an RBAC custom role.



"rbac\_role\_permission\_added"

Admin added a permission to an RBAC custom role.

Emitted once per requested permission, including permissions the role
already had, so a retried request still produces a complete audit record.



"rbac\_role\_permission\_removed"

Admin removed a permission from an RBAC custom role.

Emitted once per requested permission, including permissions the role
already lacked, so a retried request still produces a complete audit
record.

"rbac\_role\_unassigned"

Admin unassigned an RBAC custom role from a principal.

"rbac\_role\_updated"

Admin updated an RBAC custom role.

"role\_assignment\_granted"

Role assignment was granted.

"role\_assignment\_revoked"

Role assignment was revoked.

"scim\_user\_created"

A SCIM user was provisioned.

"scim\_user\_deleted"

A SCIM user was deleted.

"scim\_user\_updated"

A SCIM user was updated.

"scoped\_api\_key\_deleted"

A scoped API key was deleted.

"scoped\_api\_key\_updated"

A scoped API key was renamed or its activation state changed.

"seat\_tier\_changes\_cancelled"

Scheduled seat tier downgrades were cancelled.

"seat\_tiers\_purchased"

Seat tiers were purchased or upgraded on a subscription.

"service\_created"

Activity logged when an org service is explicitly created.

"service\_deleted"

Activity logged when an org service is deleted.

"service\_key\_created"

Activity logged when a new org service key is created.

"service\_key\_revoked"

Activity logged when an org service key is revoked.

"session\_revoked"

User revoked a specific session.

"session\_share\_accessed"

Session share was accessed.

"session\_share\_created"

Session share was created.

"session\_share\_revoked"

Session share was revoked.

"slack\_workspace\_claim\_revoked"

A Slack workspace or Enterprise Grid organization was disconnected
from the organization for Claude in Slack.

"slack\_workspace\_claimed"

A Slack workspace or Enterprise Grid organization was connected to
the organization for Claude in Slack.

"social\_login\_succeeded"

A user successfully signed in with a social identity provider (Google, Apple, or Microsoft).

"sso\_login\_failed"

An SSO sign-in attempt failed.

"sso\_login\_initiated"

A user started an SSO sign-in flow.

"sso\_login\_succeeded"

A user successfully signed in with SSO.

"sso\_second\_factor\_magic\_link"

SSO second factor magic link was used.

"step\_up\_authentication\_failed"

An additional identity check failed.

"step\_up\_authentication\_succeeded"

The user completed an additional identity check to confirm a sensitive action.

"step\_up\_credential\_enrolled"

A user enrolled a passkey for confirming sensitive actions on their account.

"subscription\_cancellation\_scheduled"

Subscription cancellation was scheduled at end of billing period.

"subscription\_quantity\_updated"

Contracted subscription seat quantity was updated.

"subscription\_renewed"

A cancelled subscription was renewed.

"subscription\_resumed"

A scheduled subscription cancellation was reversed.

"subscription\_started"

A new subscription was created (Team or Enterprise).

"subscription\_upgraded"

Subscription plan was upgraded (e.g. Team to Enterprise).

"trusted\_device\_credential\_rotated"

The identity-verification credential of a trusted device was rotated to a new key.

"trusted\_device\_enrolled"

A device was enrolled as a trusted device for the user's account. Trusted devices can be used to confirm the user's identity for sensitive actions.

"trusted\_device\_revoked"

A trusted device was removed from the user's account.

"tunnel\_archived"

An MCP tunnel was archived.

"tunnel\_certificate\_added"

An inner-TLS CA certificate was added to a tunnel.

"tunnel\_certificate\_revoked"

An inner-TLS CA certificate was revoked from a tunnel.

"tunnel\_created"

An MCP tunnel was created.

"tunnel\_token\_minted"

An OAuth bearer token for the tunnel management API was minted.

"tunnel\_token\_revealed"

The Cloudflare connector secret for a tunnel was revealed to the caller.

"tunnel\_token\_revoked"

An OAuth bearer token for the tunnel management API was revoked.



"tunnel\_token\_rotated"

The Cloudflare connector secret for a tunnel was rotated.

`tunnel_token_id` is the id of the *newly-issued* token. The previous
token is invalidated by the rotation and its id is not recorded here.

"user\_consent\_recorded"

User granted a consent for a specific entity (e.g. consumer health consent for an MCP server).

"user\_consent\_revoked"

User revoked a previously granted consent for a specific entity.

"user\_logged\_out"

A user signed out of one or all sessions.

"verification\_evidence\_submitted"

Verification evidence was submitted for an organization's verification.

"verification\_program\_application\_created"

An organization applied to a verification program.

"workspace\_member\_spend\_limit\_created"

A per-member or workspace-default Claude Code spend limit was created.

"workspace\_member\_spend\_limit\_deleted"

A per-member or workspace-default Claude Code spend limit was deleted.

"workspace\_member\_spend\_limit\_updated"

A per-member Claude Code spend limit amount was updated.

"workspace\_spend\_limit\_alert\_emails\_updated"

Spend limit alert email recipients were updated for a workspace.

"workspace\_spend\_limit\_created"

A workspace-level API spend limit was created.

"workspace\_spend\_limit\_deleted"

A workspace-level API spend limit was deleted.

actor\_ids: optional array of string

Filter activities by actor IDs (currently only `user_...` IDs are supported). Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

after\_id: optional string

Pagination cursor for retrieving the next page of results. To paginate, pass the `last_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

before\_id: optional string

Pagination cursor for retrieving the previous page of results. To paginate, pass the `first_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.



created\_at: optional object{ gt, gte, lt, lte }



gt: optional string

Filter activities created after this time (RFC 3339 format)

formatdate-time



gte: optional string

Filter activities created at or after this time (RFC 3339 format)

formatdate-time



lt: optional string

Filter activities created before this time (RFC 3339 format)

formatdate-time



lte: optional string

Filter activities created at or before this time (RFC 3339 format)

formatdate-time



exclude\_activity\_types: optional array of "abuse\_decision\_received" or "account\_deleted" or "admin\_api\_key\_created" or 480 more

Exclude activities of these types. Cannot be combined with `activity_types[]`.

One of the following:

"abuse\_decision\_received"

An external anti-abuse service reported a consequential decision about a sign-in or sign-up attempt.

"account\_deleted"

User-initiated self-service account deletion.

"admin\_api\_key\_created"

An admin API key was created.

"admin\_api\_key\_deleted"

An admin API key was deleted.

"admin\_api\_key\_updated"

An admin API key was updated (renamed or activated/deactivated).

"admin\_connector\_request\_resolved"

Admin approved or dismissed pending member requests to enable an MCP connector.

"admin\_request\_created"

Admin request created by an org member (seat upgrade, limit increase, join org, end-user invite).

"age\_verified"

User age was verified.

"anonymous\_mobile\_login\_attempted"

Anonymous mobile login was attempted.

"api\_key\_created"

Activity logged when a new API key is created.

"audit\_log\_export\_accessed"

Audit log export file was accessed/downloaded via signed URL.

"audit\_log\_export\_started"

Audit log export was initiated.

"billing\_emails\_updated"

The organization's billing email recipients were updated.

"ccr\_agent\_created"

A Claude Code agent was created.

"ccr\_agent\_deleted"

A Claude Code agent was deleted.

"ccr\_agent\_proxy\_credential\_created"

A Claude Code agent proxy credential was created. Credentials hold the secrets the agent proxy injects into requests Claude Code sessions send to approved external services; each credential belongs to an agent proxy profile. Audit events carry only credential names and settings, never the secret material itself.

"ccr\_agent\_proxy\_credential\_deleted"

A Claude Code agent proxy credential was deleted. Its secret material was removed and can no longer be sent to any host.

"ccr\_agent\_proxy\_credential\_rotated"

A Claude Code agent proxy credential's secret material was replaced. The replacement keeps the same name, profile, and allowed hosts under a new credential identifier, and everything that referenced the old credential now uses the replacement.

"ccr\_agent\_proxy\_credential\_updated"

A Claude Code agent proxy credential's settings were updated. Only the display name and the allowed host patterns can be updated; the secret material can only be replaced through a rotation.

"ccr\_agent\_proxy\_destination\_deleted"

An agent proxy destination was deleted.

"ccr\_agent\_proxy\_network\_events\_listed"

A Claude Code network activity export was accessed for the given hour.

"ccr\_agent\_proxy\_profile\_bound"

A Claude Code agent proxy profile was bound to a scope, applying its policy to Claude Code sessions in that scope.

"ccr\_agent\_proxy\_profile\_created"

A Claude Code agent proxy profile was created. Agent proxy profiles are named, reusable bundles of access policy that administrators bind to parts of the organization.

"ccr\_agent\_proxy\_profile\_deleted"

A Claude Code agent proxy profile was deleted, removing its policy from everything it was bound to.

"ccr\_agent\_proxy\_profile\_unbound"

A Claude Code agent proxy profile was unbound from a scope, removing its policy from Claude Code sessions in that scope.

"ccr\_agent\_proxy\_profile\_updated"

A Claude Code agent proxy profile's configuration was updated.

"ccr\_agent\_proxy\_provisioning\_credential\_rejected"

An organization owner rejected a credential that a teammate submitted via an agent proxy provisioning link: the credential and its disabled rule were deleted and the link was revoked. The actor is the owner; the submitter is recorded for attribution.

"ccr\_agent\_proxy\_provisioning\_link\_enabled"

An organization owner enabled a credential that a teammate submitted via an agent proxy provisioning link: the disabled rule created at submission was switched to enforce, so the credential now takes traffic. The actor is the owner; the submitter is the actor on the prior ccr\_agent\_proxy\_provisioning\_link\_submitted event.

"ccr\_agent\_proxy\_provisioning\_link\_generated"

An organization owner generated a one-time agent proxy credential provisioning link so a teammate can submit a credential into the target agent proxy profile without holding the owner role.

"ccr\_agent\_proxy\_provisioning\_link\_revoked"

An organization owner revoked an unfilled agent proxy provisioning link.

"ccr\_agent\_proxy\_provisioning\_link\_submitted"

A teammate submitted a credential via an agent proxy provisioning link. The credential and a disabled rule are created; the credential takes traffic only after an organization owner enables the submitted credential. This event records the link-mediated lifecycle; the credential itself additionally emits ccr\_agent\_proxy\_credential\_created.

"ccr\_agent\_proxy\_rule\_deleted"

An agent proxy rule was deleted.

"ccr\_agent\_slack\_access\_scope\_created"

A Claude Code agent was granted access to read or write in an additional Slack channel beyond the one it is assigned to.

"ccr\_agent\_slack\_access\_scope\_deleted"

A Claude Code agent's access to an additional Slack channel was revoked.

"ccr\_agent\_slack\_binding\_created"

A Claude Code agent was assigned to a Slack channel or workspace as its dedicated agent.

"ccr\_agent\_slack\_binding\_deleted"

A Claude Code agent's assignment to a Slack channel or workspace was removed.

"ccr\_agent\_updated"

A Claude Code agent's configuration was updated. Also emitted with updated\_fields ["is\_virtual"] alone when an auto-provisioned agent is promoted to a configured one, whether by an update request targeting it or by binding an agent proxy profile to it.

"ccr\_role\_channel\_assignment\_deleted"

CcrRoleChannelAssignmentDeleted is emitted when an org owner/admin removes an RBAC role's channel assignment row (the role reverts to granting zero channels).

"ccr\_role\_channel\_assignment\_updated"

CcrRoleChannelAssignmentUpdated is emitted when an org owner/admin sets or replaces the list of Slack channels an RBAC role's holders may configure via the delegated Claude-in-Slack channel-manage surface.

"ccr\_session\_created"

A Claude Code session was created. A session is one coding interaction with Claude.

"ccr\_session\_deleted"

A Claude Code session was deleted.

"ccr\_session\_updated"

A Claude Code session's settings were updated.

"claude\_artifact\_access\_failed"

An attempt to access an artifact failed.

"claude\_artifact\_commented"

Comment activity on a published artifact: a comment was added, a thread's resolved state was changed, or a thread was deleted. The actor is the user who performed the action; the comment text itself is stored with the artifact and is not part of this record.

"claude\_artifact\_comments\_viewed"

An artifact's comments were viewed.

"claude\_artifact\_created"

An artifact was created.

"claude\_artifact\_duplicated"

A user duplicated an artifact they could view into a new artifact that they own. The actor is the user who created the copy; the source artifact is not modified.

"claude\_artifact\_published"

A new version of an artifact was published — for an artifact created in a chat this is the action that made it publicly viewable; for an artifact created outside a chat it is recorded on every save, including saves of private artifacts, and changes to who can access the artifact are recorded separately as claude\_artifact\_sharing\_updated.

"claude\_artifact\_sharing\_updated"

An artifact's sharing settings were updated.

"claude\_artifact\_viewed"

An artifact was viewed.

"claude\_chat\_access\_failed"

A user was denied access to a Claude.ai chat conversation.

"claude\_chat\_created"

User created a chat.

"claude\_chat\_deleted"

A user deleted a Claude.ai chat conversation.

"claude\_chat\_deletion\_failed"

A request to delete a Claude.ai chat conversation failed.

"claude\_chat\_settings\_updated"

User updated the settings for a conversation.

"claude\_chat\_snapshot\_created"

User created/shared a chat snapshot.

"claude\_chat\_snapshot\_deleted"

User deleted/unshared a chat snapshot.

"claude\_chat\_snapshot\_viewed"

User viewed a chat snapshot (authenticated or public/unauthenticated).

"claude\_chat\_sync\_source\_created"

A sync source was connected for syncing external content into Claude chats.

"claude\_chat\_sync\_source\_deleted"

A sync source was disconnected from Claude chats.

"claude\_chat\_sync\_source\_updated"

A Claude chat sync source's configuration was updated.

"claude\_chat\_updated"

User updated the chat metadata (e.g name, model).

"claude\_chat\_viewed"

A user viewed a Claude.ai chat conversation.

"claude\_code\_credential\_revoked"

A Claude Code credential (runner pool key, runner token, or session token) was revoked. The credential itself is never recorded.

"claude\_code\_review\_config\_updated"

Claude Code Review configuration was enabled/disabled for an org.

"claude\_code\_review\_repository\_added"

A repository was added to org-level Claude Code Review configuration.

"claude\_code\_review\_repository\_removed"

A repository was removed from org-level Claude Code Review configuration.

"claude\_code\_review\_repository\_updated"

A Claude Code Review repository configuration was updated.

"claude\_code\_runner\_deleted"

A self-hosted runner was forcibly removed from its pool. Sessions assigned to the runner were returned to the pool queue, unless a session had already been requeued repeatedly, in which case it was marked stuck instead of being requeued again.

"claude\_code\_runner\_pool\_created"

A self-hosted runner pool for Claude Code was created.

"claude\_code\_runner\_pool\_deleted"

A self-hosted runner pool was deleted.

"claude\_code\_runner\_pool\_secret\_minted"

A registration key for a self-hosted runner pool was minted. Runners present this key to join the pool. The key itself is never recorded.

"claude\_code\_runner\_pool\_session\_queue\_updated"

An admin changed a session's position in its self-hosted runner pool's queue: requeued it onto a different runner, dismissed it from the queue, or re-admitted it for another runner provisioning attempt.

"claude\_code\_runner\_pool\_updated"

A self-hosted runner pool's settings were updated.

"claude\_code\_security\_center\_config\_updated"

Claude Code Security Center scanning was enabled/disabled for an org.

"claude\_code\_security\_scan\_cancelled"

In-flight Claude Code Security scans were cancelled for a project.

"claude\_code\_security\_scan\_created"

A Claude Code Security scan was started.

"claude\_code\_security\_scan\_project\_member\_updated"

A person's access to a Claude Code Security scan project was granted, changed, or revoked.

"claude\_code\_security\_scan\_project\_updated"

A Claude Code Security scan project was archived, unarchived, created, or migrated to a new product experience.

"claude\_code\_security\_scan\_project\_visibility\_updated"

A Claude Code Security scan project was shared with the organization or made private.

"claude\_code\_security\_scan\_run\_updated"

A single Claude Code Security scan run was archived, unarchived, or resumed after a billing pause.

"claude\_code\_security\_scan\_schedule\_deleted"

A recurring scan schedule was deleted for a Claude Code Security project.

"claude\_code\_security\_scan\_schedule\_updated"

A recurring scan schedule was set or replaced for a Claude Code Security project.

"claude\_code\_security\_vulnerability\_fix\_session\_created"

A Claude Code remediation session was created for a Claude Code Security vulnerability finding.

"claude\_code\_security\_vulnerability\_updated"

A Claude Code Security vulnerability finding was dismissed, restored, marked fixed, or reopened.

"claude\_code\_security\_webhook\_created"

A Claude Code Security outbound webhook was created.

"claude\_code\_security\_webhook\_deleted"

A Claude Code Security outbound webhook was deleted.

"claude\_code\_security\_webhook\_secret\_updated"

The HMAC signing secret for a Claude Code Security webhook was rotated.

"claude\_code\_security\_webhook\_updated"

A Claude Code Security outbound webhook was updated.

"claude\_code\_team\_memory\_acl\_updated"

An RBAC group was added to or removed from the Claude Code team-memory ACL.

"claude\_code\_team\_memory\_updated"

Claude Code team memory shared with the organization was updated.

"claude\_code\_team\_onboarding\_guide\_updated"

A Claude Code team onboarding guide was created, updated, or deleted.

"claude\_code\_user\_marketplaces\_updated"

A user's Claude Code plugin marketplace selections were updated on Anthropic servers.

"claude\_code\_user\_memory\_updated"

A user's synced private Claude Code memory was updated or deleted on Anthropic servers.

"claude\_code\_user\_plugins\_updated"

A user's Claude Code plugin selections — which plugins are installed and enabled — were updated on Anthropic servers.

"claude\_code\_user\_settings\_updated"

A user's synced Claude Code settings were updated or deleted on Anthropic servers.

"claude\_command\_created"

Command was created.

"claude\_command\_deleted"

Command was deleted.

"claude\_command\_replaced"

Command was replaced.

"claude\_enterprise\_upgrade\_credit\_updated"

An organization admin cancelled, or turned back on, the monthly usage credit the organization receives for upgrading from the Team plan to the Enterprise plan, together with the recurring monthly charge that accompanies it.

"claude\_file\_access\_failed"

A user was denied access to a file in Claude.ai.

"claude\_file\_deleted"

A file was deleted.

"claude\_file\_exported"

A file was exported from Claude to an external storage destination.

"claude\_file\_uploaded"

A file was uploaded.

"claude\_file\_viewed"

A user viewed a file in Claude.ai.

"claude\_gdrive\_integration\_created"

A Google Drive integration was enabled for the organization.

"claude\_gdrive\_integration\_deleted"

A Google Drive integration was disabled for the organization.

"claude\_gdrive\_integration\_updated"

A Google Drive integration's configuration was updated.

"claude\_github\_integration\_created"

A GitHub integration was enabled for the organization.

"claude\_github\_integration\_deleted"

A GitHub integration was disabled for the organization.

"claude\_github\_integration\_updated"

A GitHub integration's configuration was updated.

"claude\_organization\_settings\_updated"

Organization settings were updated.

"claude\_plugin\_created"

Plugin was created.

"claude\_plugin\_deleted"

Plugin was deleted.

"claude\_plugin\_disabled"

User disabled a plugin for their account.

"claude\_plugin\_enabled"

User enabled a plugin for their account.

"claude\_plugin\_replaced"

Plugin was replaced.

"claude\_plugin\_updated"

Plugin was updated.

"claude\_project\_archived"

A Claude project was archived.

"claude\_project\_created"

A Claude project was created.

"claude\_project\_deleted"

A Claude project was deleted.

"claude\_project\_document\_access\_failed"

An attempt to access a document in a Claude project failed.

"claude\_project\_document\_bulk\_deletion\_audit\_truncated"

A bulk request to delete documents from a Claude project failed with more documents requested than were individually recorded in the audit log.

"claude\_project\_document\_deleted"

A document was deleted from a Claude project.

"claude\_project\_document\_deletion\_failed"

A request to delete a document from a Claude project failed.

"claude\_project\_document\_updated"

The content of a document in a Claude project was replaced in place.

"claude\_project\_document\_uploaded"

A document was uploaded to a Claude project.

"claude\_project\_document\_viewed"

A document in a Claude project was viewed.

"claude\_project\_file\_access\_failed"

An attempt to access a file in a Claude project failed.

"claude\_project\_file\_bulk\_deletion\_audit\_truncated"

A bulk request to delete files from a Claude project failed with more files requested than were individually recorded in the audit log.

"claude\_project\_file\_deleted"

A file was deleted from a Claude project.

"claude\_project\_file\_deletion\_failed"

A request to delete a file from a Claude project failed.

"claude\_project\_file\_uploaded"

A file was uploaded to a Claude project.

"claude\_project\_reported"

A Claude project was reported.

"claude\_project\_sharing\_updated"

A Claude project's sharing settings were updated.

"claude\_project\_sync\_source\_created"

A sync source was connected to a Claude project's knowledge base.

"claude\_project\_sync\_source\_deleted"

A sync source was disconnected from a Claude project's knowledge base.

"claude\_project\_sync\_source\_updated"

A Claude project sync source's configuration was updated.

"claude\_project\_viewed"

A Claude project was viewed.

"claude\_published\_artifact\_deleted"

A published artifact was deleted or unpublished — by its creator, by an organization admin, or by Anthropic (for example, when it was removed for a policy violation).

"claude\_pubsec\_identity\_configured"

SAML IdP configuration updated for a public sector organization.

"claude\_skill\_created"

Skill was created.

"claude\_skill\_deleted"

Skill was deleted.

"claude\_skill\_disabled"

User disabled a skill for their account.

"claude\_skill\_enabled"

User enabled a skill for their account.

"claude\_skill\_replaced"

Skill was replaced.

"claude\_user\_role\_updated"

A user's role within the organization was changed, or the user was added to or removed from the organization.

"claude\_user\_seat\_tier\_updated"

An organization member's seat tier was changed. A null `previous_seat_tier` means the member previously had no seat assigned; a null `current_seat_tier` means the seat was removed.

"claude\_user\_settings\_updated"

User updated their personal settings.

"cli\_plugin\_exec\_policy\_updated"

Admin set or cleared the per-op permission ceiling for a plugin CLI.

"compliance\_api\_accessed"

Logging event auto-generated for each compliance API request.

"cowork\_session\_updated"

A Cowork session was updated.

"design\_project\_artifact\_published"

A Claude Design project's content was published as a claude.ai artifact, making a snapshot of one of its files viewable outside the project's sharing settings.

"design\_project\_created"

A Claude Design project was created.

"design\_project\_deleted"

A Claude Design project was deleted.

"design\_project\_member\_added"

A member was granted access to a Claude Design project.

"design\_project\_member\_removed"

A member's access to a Claude Design project was revoked.

"design\_project\_member\_role\_updated"

A Claude Design project member's role was changed.

"design\_project\_published"

A Claude Design template or design system was published, making it discoverable by everyone in its organization.

"design\_project\_sharing\_updated"

A Claude Design project's link-sharing settings were changed — who the project's link works for, and what people opening it through the link may do. Access granted to individual members is reported separately (see design\_project\_member\_added).

"design\_project\_unpublished"

A Claude Design template or design system was unpublished, removing it from its organization's shared gallery.

"design\_project\_updated"

A Claude Design project's metadata was updated.

"design\_project\_version\_restored"

A Claude Design project's working tree was rolled back to a previously saved version, replacing its current files with that version's files.



"design\_project\_viewed"

A Claude Design project's content was read. The surface field records which kind of read — a project open, a full-content read, a single-file read, a saved-version read, or an export request. The actor is the reader.

This activity type is retired: project content reads are no longer
recorded. Events of this type may still appear in feeds for reads that
occurred while it was active.

"desktop\_extension\_allowlisted"

A desktop extension was added to an org's allowlist.

"desktop\_extension\_blocklisted"

A desktop extension was added to the global blocklist.

"desktop\_extension\_deleted"

A desktop extension was deleted, either globally by an admin or org-scoped by an org owner.

"desktop\_extension\_removed\_from\_allowlist"

A desktop extension was removed from an org's allowlist.

"desktop\_extension\_unblocked"

A desktop extension was removed from the global blocklist.

"desktop\_extension\_uploaded"

A desktop extension was uploaded, either globally by an admin or org-scoped by an org owner.

"desktop\_extension\_version\_uploaded"

A new version of an existing org-owned desktop extension was uploaded.

"domain\_claim\_initiated"

Domain capture claim initiated over personal accounts on verified domains.

"end\_user\_invite\_requested"

Non-admin member submitted an invite request for a new org member.

"extra\_usage\_billing\_enabled"

Usage credit billing was enabled for an organization.

"extra\_usage\_credit\_granted"

A promotional usage credit grant was claimed.

"extra\_usage\_spend\_limit\_created"

Usage credit spend limit was created.

"extra\_usage\_spend\_limit\_deleted"

Usage credit spend limit was deleted.

"extra\_usage\_spend\_limit\_increase\_request\_approved"

A usage credit spend limit increase request was approved.

"extra\_usage\_spend\_limit\_increase\_request\_denied"

A usage credit spend limit increase request was denied.

"extra\_usage\_spend\_limit\_updated"

Usage credit spend limit was updated.

"ghe\_configuration\_created"

Admin created a GHE configuration.

"ghe\_configuration\_deleted"

Admin deleted a GHE configuration.

"ghe\_configuration\_updated"

Admin updated a GHE configuration. Previous/new field pairs are recorded only for settings that changed in the update; secret credentials are never recorded, only whether they were replaced.

"ghe\_user\_connected"

User connected to a GHE instance.

"ghe\_user\_disconnected"

User disconnected from a GHE instance.

"ghe\_webhook\_signature\_invalid"

Webhook signature validation failed.

"github\_token\_import"

A user attempted to import a personal GitHub access token for use with Claude Code. The `result` field indicates the outcome of the import (imported, rejected, or failed).

"group\_created"

A group was created (RBAC admin or SCIM provisioning).

"group\_deleted"

A group was deleted (RBAC admin or SCIM provisioning).

"group\_list\_viewed"

Admin viewed the list of RBAC groups.

"group\_member\_added"

One or more members were added to a group.

"group\_member\_addition\_failed"

A request to add members to a group failed. Some of the requested members may have been added before the failure.

"group\_member\_list\_viewed"

Admin viewed the members of an RBAC group.

"group\_member\_removal\_failed"

A request to remove members from a group failed. Some of the requested members may have been removed before the failure.

"group\_member\_removed"

One or more members were removed from a group.

"group\_project\_shares\_revoked"

An RBAC group's project shares in one organization were revoked in bulk.

"group\_skill\_shares\_revoked"

An RBAC group's skill shares in one organization were revoked in bulk.

"group\_updated"

A group was updated (RBAC admin or SCIM provisioning).

"group\_viewed"

A group was viewed.

"group\_visibility\_updated"

An RBAC group's visibility policy was updated.

"inference\_hooks\_circuit\_breaker\_tripped"

The organization's Inference hooks circuit breaker tripped automatically: calls to the organization's Inference hooks endpoint crossed a failure threshold, and inspection was suspended to protect live traffic. While tripped, requests are handled according to the organization's failure handling setting — allowed through uninspected (fail open) or rejected (fail closed) — and no per-request Inference hooks activities are recorded. The tripped state persists until an administrator re-enables Inference hooks inspection (or explicitly resets the circuit breaker).

"inference\_hooks\_config\_deleted"

Inference hooks configuration was removed for the
organization.

"inference\_hooks\_config\_updated"

Inference hooks configuration was created or updated for the
organization.

"inference\_hooks\_request\_denied"

Inference hooks inspection denied a request. The request was blocked and no model response was produced.

"inference\_hooks\_request\_failed\_open"

A request proceeded without Inference hooks inspection because a verdict could not be obtained and the organization's Inference hooks configuration is set to fail open.

"inference\_hooks\_signing\_secret\_generated"

A request signing secret was generated for the organization's
Inference hooks configuration.

"integration\_user\_connected"

User connected to an integration.

"integration\_user\_disconnected"

User disconnected from an integration.

"invoice\_collection\_method\_updated"

Invoice collection method was changed.

"lti\_launch\_initiated"

LTI launch was initiated.

"lti\_launch\_success"

LTI launch completed successfully.

"lti\_platform\_created"

Anthropic staff created an LTI platform integration on behalf of an org.

"lti\_platform\_updated"

Anthropic staff updated an LTI platform integration on behalf of an org.

"magic\_link\_login\_failed"

A magic link sign-in attempt failed.

"magic\_link\_login\_initiated"

A user requested a magic link sign-in email.

"magic\_link\_login\_succeeded"

A user successfully signed in with a magic link email.

"managed\_organization\_setup\_completed"

Managed (AWS Marketplace) organization setup was completed.

"marketplace\_created"

Admin created an organization marketplace.

"marketplace\_deleted"

Admin deleted an organization marketplace.

"marketplace\_updated"

Admin updated an organization marketplace.

"marketplace\_webhook\_deleted"

Admin removed the GitHub push webhook for a marketplace.

"marketplace\_webhook\_provisioned"

Admin provisioned a GitHub push webhook for a marketplace.

"mcp\_directory\_server\_published"

The organization published its approved MCP directory listing.

"mcp\_server\_created"

An MCP server was added to the organization.

"mcp\_server\_deleted"

An MCP server was removed from the organization.

"mcp\_server\_managed\_auth\_token\_exchanged"

A user attempted to obtain an access token for an MCP server via enterprise managed authorization. This event reports the outcomes of attempted token exchanges. Repeated failures with the same cause may be reported once until the cause changes, and requests denied by organization policy before a token exchange is attempted are not reported, with the exception of the "connector\_scope\_not\_granted" failures described under error\_type.

"mcp\_server\_managed\_auth\_updated"

An MCP server's enterprise managed authorization settings were set, changed, or cleared, including when they were supplied while the server was being added or edited. Fields without a "previous\_" prefix describe the settings after the change and are null when the server has no managed authorization settings afterwards; "previous\_" fields describe the settings before the change and are null when the server had none before (always the case for a newly added server).

"mcp\_server\_updated"

An MCP server's configuration was updated.

"mcp\_tool\_policy\_updated"

The permission restriction for an MCP tool was set or cleared.

"org\_analytics\_api\_capability\_updated"

Organization analytics\_api capability was enabled or disabled.

"org\_bulk\_delete\_initiated"

Organization bulk deletion was initiated.

"org\_capability\_grant\_added"

A capability grant was added to a workspace or role.

"org\_capability\_grant\_removed"

A capability grant was removed from a workspace or role.

"org\_claude\_code\_data\_sharing\_disabled"

Organization Claude Code data sharing was disabled.

"org\_claude\_code\_data\_sharing\_enabled"

Organization Claude Code data sharing was enabled.

"org\_claude\_code\_desktop\_disabled"

Organization Claude Code Desktop was disabled.

"org\_claude\_code\_desktop\_enabled"

Organization Claude Code Desktop was enabled.

"org\_claude\_code\_zero\_data\_retention\_disabled"

A primary owner disabled zero data retention for Claude Code, so Claude
Code content is retained according to the organization's data retention
settings.

"org\_compliance\_api\_settings\_updated"

Organization compliance API settings were updated.

"org\_connector\_domain\_guard\_updated"

Enterprise admin changed whether connectors are restricted to verified domains.

"org\_cowork\_act\_without\_asking\_mode\_disabled"

The "Act without asking" mode in Cowork was disabled for the organization, so members can no longer let Claude act without asking for approval.

"org\_cowork\_act\_without\_asking\_mode\_enabled"

The "Act without asking" mode in Cowork was enabled for the organization, allowing members to let Claude act without asking for approval.

"org\_cowork\_agent\_disabled"

Organization Cowork Agent was disabled.

"org\_cowork\_agent\_enabled"

Organization Cowork Agent was enabled.

"org\_cowork\_auto\_mode\_disabled"

The "Auto" permission mode in Cowork was disabled for the organization, so members can no longer let Claude approve its own actions after a safety check.

"org\_cowork\_auto\_mode\_enabled"

The "Auto" permission mode in Cowork was enabled for the organization, allowing members to let Claude approve its own actions after a safety check.

"org\_cowork\_disabled"

Organization cowork was disabled.

"org\_cowork\_enabled"

Organization cowork was enabled.

"org\_cowork\_mcp\_always\_allow\_disabled"

The "Always allow" option for connector tools in Cowork was disabled for the organization, so each use of a connector tool that can make changes requires approval. Read-only connector tools are not affected by this setting.

"org\_cowork\_mcp\_always\_allow\_enabled"

The "Always allow" option for connector tools in Cowork was enabled for the organization, letting members approve a connector tool that can make changes once and allow its later uses automatically. Read-only connector tools are not affected by this setting.

"org\_cowork\_otlp\_settings\_updated"

The organization's Cowork OpenTelemetry monitoring export settings were updated.

"org\_cowork\_remote\_disabled"

Running Cowork in the cloud was disabled for the organization, so members can no longer run Cowork sessions in Anthropic-hosted remote environments.

"org\_cowork\_remote\_enabled"

Running Cowork in the cloud was enabled for the organization, allowing members to run Cowork sessions in Anthropic-hosted remote environments.

"org\_creation\_blocked"

Organization creation was blocked.

"org\_data\_export\_accessed"

Organization data export file was accessed/downloaded via signed URL.

"org\_data\_export\_completed"

Organization data export was completed.

"org\_data\_export\_started"

Organization data export was started.

"org\_data\_residency\_updated"

The organization's inference data residency settings were updated.

"org\_deleted\_via\_bulk"

Organization was deleted via bulk operation.

"org\_deletion\_requested"

Organization deletion was requested.

"org\_directory\_resync\_completed"

Organization directory resync completed successfully.

"org\_directory\_resync\_failed"

Organization directory resync failed.

"org\_directory\_resync\_started"

Organization directory resync was started asynchronously.

"org\_directory\_sync\_activated"

Organization directory sync was activated.

"org\_directory\_sync\_add\_initiated"

Organization directory sync setup was initiated.

"org\_directory\_sync\_deleted"

Organization directory sync was deleted.

"org\_discoverability\_disabled"

Admin disabled organization discoverability.

"org\_discoverability\_enabled"

Admin enabled organization discoverability.

"org\_discoverability\_settings\_updated"

Admin updated organization discoverability settings.

"org\_domain\_add\_initiated"

Organization domain verification was initiated.

"org\_domain\_removed"

Organization domain was removed.

"org\_domain\_verified"

Organization domain was verified.

"org\_external\_key\_created"

A CMEK external key config was created.

"org\_external\_key\_deleted"

A CMEK external key config was deleted.

"org\_external\_key\_updated"

A CMEK external key config was updated.

"org\_external\_key\_validated"

A CMEK external key config was validated against the customer's KMS.

"org\_hipaa\_self\_serve\_enabled"

A primary owner click-accepted the BAA and enabled HIPAA protections
for the organization via the self-serve flow.

"org\_invite\_link\_disabled"

Organization invite link was disabled.

"org\_invite\_link\_generated"

Organization invite link was generated.

"org\_invite\_link\_regenerated"

Organization invite link was regenerated (previous link invalidated).

"org\_invite\_viewed"

An organization invite was viewed.

"org\_invites\_listed"

Organization invites were listed.

"org\_ip\_restriction\_created"

Organization IP restriction was created.

"org\_ip\_restriction\_deleted"

Organization IP restriction was deleted.

"org\_ip\_restriction\_updated"

Organization IP restriction was updated.

"org\_join\_proposal\_decided"

Approve or reject decision on a parent-org join proposal.

"org\_join\_request\_approved"

Admin approved a join request.

"org\_join\_request\_created"

User requested to join an organization.

"org\_join\_request\_dismissed"

Admin dismissed a join request.

"org\_join\_request\_instant\_approved"

Join request was instantly approved.

"org\_join\_requests\_bulk\_dismissed"

Admin bulk-dismissed join requests.

"org\_magic\_link\_second\_factor\_toggled"

Organization magic link second factor was toggled.

"org\_member\_invites\_disabled"

Admin disabled member invites for the organization.

"org\_member\_invites\_enabled"

Admin enabled member invites for the organization.

"org\_members\_exported"

Organization members list was exported as CSV.

"org\_model\_default\_updated"

An organization or role default model setting was changed by an administrator.

"org\_parent\_join\_proposal\_created"

Organization parent join proposal was created.

"org\_parent\_search\_performed"

Organization parent search was performed.

"org\_sso\_add\_initiated"

Organization SSO setup was initiated.

"org\_sso\_connection\_activated"

Organization SSO connection was activated.

"org\_sso\_connection\_deactivated"

Organization SSO connection was deactivated.

"org\_sso\_connection\_deleted"

Organization SSO connection was deleted.

"org\_sso\_group\_role\_mappings\_updated"

Organization SSO group role mappings were updated.

"org\_sso\_provisioning\_mode\_changed"

Organization SSO provisioning mode was changed.

"org\_sso\_scim\_welcome\_email\_toggled"

Organization SCIM-provisioned welcome email was toggled.

"org\_sso\_seat\_tier\_assignment\_toggled"

Organization SSO seat tier assignment was toggled.

"org\_sso\_seat\_tier\_mappings\_updated"

Organization SSO seat tier mappings were updated.

"org\_sso\_toggled"

Organization SSO was toggled on or off.

"org\_sync\_deleting\_synchronized\_files\_started"

Organization started deleting synchronized files.

"org\_sync\_synchronized\_files\_deleted"

Organization synchronized files were deleted.

"org\_taint\_added"

A taint was added to an organization.

"org\_taint\_removed"

A taint was removed from an organization.

"org\_user\_deleted"

User was removed from organization.

"org\_user\_invite\_accepted"

Organization user invite was accepted.

"org\_user\_invite\_deleted"

Organization user invite was deleted.

"org\_user\_invite\_re\_sent"

Organization user invite was re-sent.

"org\_user\_invite\_rejected"

Organization user invite was rejected.

"org\_user\_invite\_sent"

Organization user invite was sent.

"org\_user\_left"

User removed themselves from organization.

"org\_user\_trusted\_devices\_revoked"

An organization admin revoked a member's trusted devices and signed the member out of all active sessions.

"org\_user\_viewed"

An organization user was viewed.

"org\_users\_listed"

Organization users were listed.

"org\_work\_across\_apps\_disabled"

The organization's "Let Claude work across apps" setting was turned off.

"org\_work\_across\_apps\_enabled"

The organization's "Let Claude work across apps" setting was turned on.

"organization\_address\_updated"

The organization's billing or shipping address was updated.

"organization\_icon\_deleted"

Organization's custom icon deleted.

"organization\_icon\_updated"

Organization's custom icon uploaded or replaced.

"owned\_projects\_access\_restored"

Access to owned projects was restored.

"payment\_method\_updated"

The organization's default payment method was updated.

"pending\_share\_created"

A pending share of a project or skill was created for an email address that is not yet an organization member.

"pending\_share\_revoked"

A pending share of a project or skill was revoked before the invitee joined the organization.

"phone\_code\_sent"

User requested a phone verification code.

"phone\_code\_verified"

User successfully verified their phone code.

"platform\_agent\_archived"

An agent was archived on the API platform.

"platform\_agent\_created"

An agent was created on the API platform.

"platform\_agent\_deleted"

An agent was deleted from the API platform.

"platform\_agent\_deployment\_archived"

An agent deployment was archived on the API platform.

"platform\_agent\_deployment\_created"

An agent deployment was created on the API platform.

"platform\_agent\_deployment\_deleted"

An agent deployment was deleted from the API platform.

"platform\_agent\_deployment\_paused"

An agent deployment was paused on the API platform.

"platform\_agent\_deployment\_run\_triggered"

An agent deployment was run on demand on the API platform.

"platform\_agent\_deployment\_unpaused"

An agent deployment was resumed on the API platform.

"platform\_agent\_deployment\_updated"

An agent deployment was updated on the API platform.

"platform\_agent\_session\_archived"

An agent session was archived on the API platform.

"platform\_agent\_session\_created"

An agent session was created on the API platform.

"platform\_agent\_session\_deleted"

An agent session was deleted from the API platform.

"platform\_agent\_session\_resource\_added"

A resource was attached to an agent session.

"platform\_agent\_session\_resource\_deleted"

A resource attached to an agent session was removed.

"platform\_agent\_session\_resource\_updated"

A resource attached to an agent session was updated.

"platform\_agent\_session\_thread\_archived"

A thread within an agent session was archived.

"platform\_agent\_session\_updated"

An agent session was updated on the API platform.

"platform\_agent\_updated"

An agent was updated on the API platform.

"platform\_api\_key\_created"

An API key was created.

"platform\_api\_key\_updated"

An API key was updated.

"platform\_app\_attest\_authentication"

An attested mobile device attempted to exchange an Apple App Attest assertion for Anthropic API credentials.

"platform\_billing\_upgraded\_to\_prepaid"

The organization's API billing was upgraded to the prepaid plan.

"platform\_clearance\_workspace\_program\_request\_cleared"

A workspace's clearance program assignment was removed.

"platform\_clearance\_workspace\_program\_request\_set"

A workspace's clearance program assignment was created or updated.

"platform\_cost\_report\_viewed"

The cost report was viewed.

"platform\_dream\_archived"

A Dream (asynchronous memory-consolidation job) was archived.

"platform\_dream\_cancelled"

A Dream (asynchronous memory-consolidation job) was cancelled before it completed.

"platform\_dream\_created"

A Dream (asynchronous memory-consolidation job) was created.

"platform\_federated\_authentication"

A federated workload identity attempted to exchange an OIDC token for Anthropic API credentials.

"platform\_federation\_issuer\_archived"

An OIDC federation issuer was archived.

"platform\_federation\_issuer\_updated"

An OIDC federation issuer was updated.

"platform\_federation\_rule\_archived"

An OIDC federation rule was archived.

"platform\_federation\_rule\_updated"

An OIDC federation rule was updated.

"platform\_federation\_rule\_workspace\_added"

A federation rule was enabled for a workspace.

"platform\_federation\_rule\_workspace\_removed"

A federation rule was disabled for a workspace.

"platform\_file\_content\_downloaded"

Activity logged when file content is downloaded via GET /v1/files/{file\_id}/content.

"platform\_file\_deleted"

Activity logged when a file is deleted via DELETE /v1/files/{file\_id}.

"platform\_file\_uploaded"

Activity logged when a file is uploaded via POST /v1/files.

"platform\_memory\_created"

An agent memory document was created.

"platform\_memory\_deleted"

An agent memory document was deleted.

"platform\_memory\_store\_archived"

An agent memory store was archived. Archived stores reject new memory writes and cannot be attached to new sessions; deletion and redaction remain permitted for privacy scrubbing.

"platform\_memory\_store\_created"

An agent memory store was created.

"platform\_memory\_store\_deleted"

An agent memory store was deleted. Memory content removal may complete asynchronously for very large stores.

"platform\_memory\_store\_updated"

An agent memory store's name, description, or metadata was updated.

"platform\_memory\_updated"

An agent memory document's content or path was updated.

"platform\_memory\_version\_redacted"

A historical version of an agent memory document was redacted. Redaction scrubs the stored content of a specific version while preserving the version's existence in the history.

"platform\_oauth\_app\_created"

An OAuth app was created.

"platform\_oauth\_app\_revoked"

An OAuth app was revoked.

"platform\_oauth\_app\_updated"

An OAuth app was updated.

"platform\_plugin\_directory\_submission\_created"

A plugin directory submission was created on the API platform. A plugin directory submission is a request to list a plugin in the public plugin directory.

"platform\_plugin\_directory\_submission\_deleted"

A plugin directory submission was deleted on the API platform.

"platform\_plugin\_directory\_submission\_updated"

A plugin directory submission was updated on the API platform.

"platform\_service\_account\_archived"

A service account was archived.

"platform\_service\_account\_updated"

A service account was updated.

"platform\_service\_account\_workspace\_member\_added"

A service account was added as a member of a workspace.

"platform\_service\_account\_workspace\_member\_removed"

A service account was removed from a workspace.

"platform\_service\_account\_workspace\_member\_updated"

A service account's workspace membership role was updated.

"platform\_signing\_key\_created"

Activity logged when a new request-signing key is registered for the org.

"platform\_signing\_key\_deleted"

Activity logged when a signing key is permanently deleted.

"platform\_signing\_key\_rotated"

Activity logged when an in-memory signing key is rotated.

"platform\_skill\_version\_created"

Activity logged when a skill version is created via POST /v1/skills/{skill\_id}/versions.

"platform\_skill\_version\_deleted"

Activity logged when a skill version is deleted via DELETE /v1/skills/{skill\_id}/versions/{version}.

"platform\_spend\_limit\_alert\_emails\_updated"

Spend limit alert email addresses and role targets were updated for an org.

"platform\_spend\_limit\_created"

An org-level fixed-dollar spend limit was created.

"platform\_spend\_limit\_deleted"

An org-level spend limit was removed.

"platform\_spend\_limit\_updated"

An org-level spend limit snooze/ignore state was changed.

"platform\_usage\_report\_claude\_code\_viewed"

The Claude Code usage report was viewed.

"platform\_usage\_report\_messages\_viewed"

The messages usage report was viewed.

"platform\_workspace\_archived"

A workspace was archived.

"platform\_workspace\_created"

A workspace was created.

"platform\_workspace\_inference\_data\_retention\_disabled"

The zero data retention override was disabled for a workspace.

"platform\_workspace\_inference\_data\_retention\_enabled"

The zero data retention override was enabled for a workspace.

"platform\_workspace\_member\_added"

A member was added to a workspace.

"platform\_workspace\_member\_removed"

A member was removed from a workspace.

"platform\_workspace\_member\_updated"

A workspace member was updated.

"platform\_workspace\_member\_viewed"

A workspace member was viewed.

"platform\_workspace\_members\_listed"

Workspace members were listed.

"platform\_workspace\_rate\_limit\_deleted"

A workspace rate limit was deleted.

"platform\_workspace\_rate\_limit\_updated"

A workspace rate limit was created or updated.

"platform\_workspace\_updated"

A workspace was updated.

"plugin\_installation\_preference\_updated"

An org admin changed the installation preference for a plugin.

"prepaid\_auto\_recharge\_disabled"

Auto-recharge was disabled for API prepaid org.

"prepaid\_auto\_recharge\_updated"

Auto-recharge settings were updated for API prepaid org.

"prepaid\_extra\_usage\_auto\_reload\_disabled"

Prepaid usage credit auto-reload was disabled.

"prepaid\_extra\_usage\_auto\_reload\_enabled"

Prepaid usage credit auto-reload was enabled.

"prepaid\_extra\_usage\_auto\_reload\_settings\_updated"

Prepaid usage credit auto-reload settings were updated.

"primary\_owner\_transferred"

Primary owner role was transferred to another org member.

"rbac\_role\_assigned"

Admin assigned an RBAC custom role to a principal.

"rbac\_role\_created"

Admin created an RBAC custom role.

"rbac\_role\_deleted"

Admin deleted an RBAC custom role.



"rbac\_role\_permission\_added"

Admin added a permission to an RBAC custom role.

Emitted once per requested permission, including permissions the role
already had, so a retried request still produces a complete audit record.



"rbac\_role\_permission\_removed"

Admin removed a permission from an RBAC custom role.

Emitted once per requested permission, including permissions the role
already lacked, so a retried request still produces a complete audit
record.

"rbac\_role\_unassigned"

Admin unassigned an RBAC custom role from a principal.

"rbac\_role\_updated"

Admin updated an RBAC custom role.

"role\_assignment\_granted"

Role assignment was granted.

"role\_assignment\_revoked"

Role assignment was revoked.

"scim\_user\_created"

A SCIM user was provisioned.

"scim\_user\_deleted"

A SCIM user was deleted.

"scim\_user\_updated"

A SCIM user was updated.

"scoped\_api\_key\_deleted"

A scoped API key was deleted.

"scoped\_api\_key\_updated"

A scoped API key was renamed or its activation state changed.

"seat\_tier\_changes\_cancelled"

Scheduled seat tier downgrades were cancelled.

"seat\_tiers\_purchased"

Seat tiers were purchased or upgraded on a subscription.

"service\_created"

Activity logged when an org service is explicitly created.

"service\_deleted"

Activity logged when an org service is deleted.

"service\_key\_created"

Activity logged when a new org service key is created.

"service\_key\_revoked"

Activity logged when an org service key is revoked.

"session\_revoked"

User revoked a specific session.

"session\_share\_accessed"

Session share was accessed.

"session\_share\_created"

Session share was created.

"session\_share\_revoked"

Session share was revoked.

"slack\_workspace\_claim\_revoked"

A Slack workspace or Enterprise Grid organization was disconnected
from the organization for Claude in Slack.

"slack\_workspace\_claimed"

A Slack workspace or Enterprise Grid organization was connected to
the organization for Claude in Slack.

"social\_login\_succeeded"

A user successfully signed in with a social identity provider (Google, Apple, or Microsoft).

"sso\_login\_failed"

An SSO sign-in attempt failed.

"sso\_login\_initiated"

A user started an SSO sign-in flow.

"sso\_login\_succeeded"

A user successfully signed in with SSO.

"sso\_second\_factor\_magic\_link"

SSO second factor magic link was used.

"step\_up\_authentication\_failed"

An additional identity check failed.

"step\_up\_authentication\_succeeded"

The user completed an additional identity check to confirm a sensitive action.

"step\_up\_credential\_enrolled"

A user enrolled a passkey for confirming sensitive actions on their account.

"subscription\_cancellation\_scheduled"

Subscription cancellation was scheduled at end of billing period.

"subscription\_quantity\_updated"

Contracted subscription seat quantity was updated.

"subscription\_renewed"

A cancelled subscription was renewed.

"subscription\_resumed"

A scheduled subscription cancellation was reversed.

"subscription\_started"

A new subscription was created (Team or Enterprise).

"subscription\_upgraded"

Subscription plan was upgraded (e.g. Team to Enterprise).

"trusted\_device\_credential\_rotated"

The identity-verification credential of a trusted device was rotated to a new key.

"trusted\_device\_enrolled"

A device was enrolled as a trusted device for the user's account. Trusted devices can be used to confirm the user's identity for sensitive actions.

"trusted\_device\_revoked"

A trusted device was removed from the user's account.

"tunnel\_archived"

An MCP tunnel was archived.

"tunnel\_certificate\_added"

An inner-TLS CA certificate was added to a tunnel.

"tunnel\_certificate\_revoked"

An inner-TLS CA certificate was revoked from a tunnel.

"tunnel\_created"

An MCP tunnel was created.

"tunnel\_token\_minted"

An OAuth bearer token for the tunnel management API was minted.

"tunnel\_token\_revealed"

The Cloudflare connector secret for a tunnel was revealed to the caller.

"tunnel\_token\_revoked"

An OAuth bearer token for the tunnel management API was revoked.



"tunnel\_token\_rotated"

The Cloudflare connector secret for a tunnel was rotated.

`tunnel_token_id` is the id of the *newly-issued* token. The previous
token is invalidated by the rotation and its id is not recorded here.

"user\_consent\_recorded"

User granted a consent for a specific entity (e.g. consumer health consent for an MCP server).

"user\_consent\_revoked"

User revoked a previously granted consent for a specific entity.

"user\_logged\_out"

A user signed out of one or all sessions.

"verification\_evidence\_submitted"

Verification evidence was submitted for an organization's verification.

"verification\_program\_application\_created"

An organization applied to a verification program.

"workspace\_member\_spend\_limit\_created"

A per-member or workspace-default Claude Code spend limit was created.

"workspace\_member\_spend\_limit\_deleted"

A per-member or workspace-default Claude Code spend limit was deleted.

"workspace\_member\_spend\_limit\_updated"

A per-member Claude Code spend limit amount was updated.

"workspace\_spend\_limit\_alert\_emails\_updated"

Spend limit alert email recipients were updated for a workspace.

"workspace\_spend\_limit\_created"

A workspace-level API spend limit was created.

"workspace\_spend\_limit\_deleted"

A workspace-level API spend limit was deleted.



limit: optional number

Maximum results (default: 100, max: 5000)

default100

maximum5000

minimum1



order: optional "asc" or "desc"

Sort direction by `created_at`. `desc` (default) returns newest-first; `asc` returns oldest-first for incremental sync. Activities become queryable after a short asynchronous ingestion delay. When using `asc` with `after_id` for incremental sync, late-arriving rows with timestamps behind the cursor will be skipped; consumers that need at-least-once delivery should periodically re-poll an overlap window via `created_at.gte` and deduplicate by `id`. `after_id` and `before_id` are relative to this order.

defaultdesc

One of the following:

"asc"

"desc"

organization\_ids: optional array of string

Filter activities by organization IDs (accepts `org_...` or organization UUID). Enumerate IDs via `GET /v1/compliance/organizations`.

user\_ids: optional array of string

Alias for `actor_ids[]`, for consistency with other compliance routes. If both are provided, the lists are merged.

##### Headers

"x-api-key": optional string

##### Returns



data: optional array of object{ actor, decision, id, 5 more } or object{ actor, id, created\_at, 3 more } or object{ actor, admin\_api\_key\_id, scopes, 5 more } or 480 more

List of activity records. Each element's `type` field identifies which activity it is and which additional fields are present.

One of the following:



AbuseDecisionReceived object{ actor, decision, id, 5 more }

An external anti-abuse service reported a consequential decision about a sign-in or sign-up attempt.



AccountDeleted object{ actor, id, created\_at, 3 more }

User-initiated self-service account deletion.



AdminAPIKeyCreated object{ actor, admin\_api\_key\_id, scopes, 5 more }

An admin API key was created.



AdminAPIKeyDeleted object{ actor, admin\_api\_key\_id, id, 4 more }

An admin API key was deleted.



AdminAPIKeyUpdated object{ actor, admin\_api\_key\_id, updates, 5 more }

An admin API key was updated (renamed or activated/deactivated).



AdminConnectorRequestResolved object{ actor, decision, mcp\_server\_id, 6 more }

Admin approved or dismissed pending member requests to enable an MCP connector.



AdminRequestCreated object{ actor, request\_type, id, 4 more }

Admin request created by an org member (seat upgrade, limit increase, join org, end-user invite).



AgeVerified object{ actor, id, created\_at, 3 more }

User age was verified.



AnonymousMobileLoginAttempted object{ actor, id, created\_at, 3 more }

Anonymous mobile login was attempted.



APIKeyCreated object{ actor, api\_key\_id, scopes, 6 more }

Activity logged when a new API key is created.



ClaudeArtifactAccessFailed object{ actor, id, claude\_artifact\_id, 6 more }

An attempt to access an artifact failed.



ClaudeArtifactCommented object{ actor, claude\_artifact\_id, comment\_action, 8 more }

Comment activity on a published artifact: a comment was added, a thread's resolved state was changed, or a thread was deleted. The actor is the user who performed the action; the comment text itself is stored with the artifact and is not part of this record.



ClaudeArtifactCommentsViewed object{ actor, claude\_artifact\_id, id, 5 more }

An artifact's comments were viewed.



ClaudeArtifactCreated object{ actor, claude\_artifact\_id, id, 4 more }

An artifact was created.



ClaudePublishedArtifactDeleted object{ actor, claude\_published\_artifact\_id, id, 4 more }

A published artifact was deleted or unpublished — by its creator, by an organization admin, or by Anthropic (for example, when it was removed for a policy violation).



ClaudeArtifactPublished object{ actor, artifact\_type, claude\_published\_artifact\_id, 9 more }

A new version of an artifact was published — for an artifact created in a chat this is the action that made it publicly viewable; for an artifact created outside a chat it is recorded on every save, including saves of private artifacts, and changes to who can access the artifact are recorded separately as claude\_artifact\_sharing\_updated.



ClaudeArtifactSharingUpdated object{ actor, audience, claude\_artifact\_id, 14 more }

An artifact's sharing settings were updated.



ClaudeArtifactViewed object{ actor, claude\_artifact\_id, id, 5 more }

An artifact was viewed.



AuditLogExportAccessed object{ actor, id, created\_at, 3 more }

Audit log export file was accessed/downloaded via signed URL.



AuditLogExportStarted object{ actor, id, created\_at, 5 more }

Audit log export was initiated.



BillingEmailsUpdated object{ actor, id, cc\_email\_count, 6 more }

The organization's billing email recipients were updated.



CcrAgentCreated object{ actor, agent\_id, default\_source\_urls\_truncated, 11 more }

A Claude Code agent was created.



CcrAgentDeleted object{ actor, agent\_id, cascaded\_agent\_ids\_truncated, 7 more }

A Claude Code agent was deleted.



CcrAgentProxyCredentialCreated object{ actor, credential\_id, credential\_type, 10 more }

A Claude Code agent proxy credential was created. Credentials hold the secrets the agent proxy injects into requests Claude Code sessions send to approved external services; each credential belongs to an agent proxy profile. Audit events carry only credential names and settings, never the secret material itself.



CcrAgentProxyCredentialDeleted object{ actor, credential\_id, profile\_id, 6 more }

A Claude Code agent proxy credential was deleted. Its secret material was removed and can no longer be sent to any host.



CcrAgentProxyCredentialRotated object{ actor, credential\_id, credential\_type, 11 more }

A Claude Code agent proxy credential's secret material was replaced. The replacement keeps the same name, profile, and allowed hosts under a new credential identifier, and everything that referenced the old credential now uses the replacement.



CcrAgentProxyCredentialUpdated object{ actor, credential\_id, display\_name, 10 more }

A Claude Code agent proxy credential's settings were updated. Only the display name and the allowed host patterns can be updated; the secret material can only be replaced through a rotation.



CcrAgentProxyDestinationDeleted object{ actor, deleted\_with\_profile, destination\_id, 7 more }

An agent proxy destination was deleted.



CcrAgentProxyNetworkEventsListed object{ actor, failed, id, 5 more }

A Claude Code network activity export was accessed for the given hour.



CcrAgentProxyProfileBound object{ actor, profile\_id, scope\_id, 6 more }

A Claude Code agent proxy profile was bound to a scope, applying its policy to Claude Code sessions in that scope.



CcrAgentProxyProfileCreated object{ actor, display\_name, profile\_id, 7 more }

A Claude Code agent proxy profile was created. Agent proxy profiles are named, reusable bundles of access policy that administrators bind to parts of the organization.



CcrAgentProxyProfileDeleted object{ actor, deleted\_credential\_count, deleted\_credentials\_unknown, 10 more }

A Claude Code agent proxy profile was deleted, removing its policy from everything it was bound to.



CcrAgentProxyProfileUnbound object{ actor, profile\_id, scope\_id, 6 more }

A Claude Code agent proxy profile was unbound from a scope, removing its policy from Claude Code sessions in that scope.



CcrAgentProxyProfileUpdated object{ actor, profile\_id, id, 6 more }

A Claude Code agent proxy profile's configuration was updated.



CcrAgentProxyProvisioningCredentialRejected object{ actor, credential\_id, link\_id, 8 more }

An organization owner rejected a credential that a teammate submitted via an agent proxy provisioning link: the credential and its disabled rule were deleted and the link was revoked. The actor is the owner; the submitter is recorded for attribution.



CcrAgentProxyProvisioningLinkEnabled object{ actor, credential\_id, link\_id, 7 more }

An organization owner enabled a credential that a teammate submitted via an agent proxy provisioning link: the disabled rule created at submission was switched to enforce, so the credential now takes traffic. The actor is the owner; the submitter is the actor on the prior ccr\_agent\_proxy\_provisioning\_link\_submitted event.



CcrAgentProxyProvisioningLinkGenerated object{ actor, link\_id, profile\_id, 5 more }

An organization owner generated a one-time agent proxy credential provisioning link so a teammate can submit a credential into the target agent proxy profile without holding the owner role.



CcrAgentProxyProvisioningLinkRevoked object{ actor, link\_id, profile\_id, 5 more }

An organization owner revoked an unfilled agent proxy provisioning link.



CcrAgentProxyProvisioningLinkSubmitted object{ actor, credential\_id, credential\_type, 8 more }

A teammate submitted a credential via an agent proxy provisioning link. The credential and a disabled rule are created; the credential takes traffic only after an organization owner enables the submitted credential. This event records the link-mediated lifecycle; the credential itself additionally emits ccr\_agent\_proxy\_credential\_created.



CcrAgentProxyRuleDeleted object{ actor, deleted\_with\_profile, profile\_id, 7 more }

An agent proxy rule was deleted.



CcrAgentSlackAccessScopeCreated object{ actor, agent\_id, can\_write, 7 more }

A Claude Code agent was granted access to read or write in an additional Slack channel beyond the one it is assigned to.



CcrAgentSlackAccessScopeDeleted object{ actor, agent\_id, slack\_channel\_id, 6 more }

A Claude Code agent's access to an additional Slack channel was revoked.



CcrAgentSlackBindingCreated object{ actor, agent\_id, slack\_channel\_id, 6 more }

A Claude Code agent was assigned to a Slack channel or workspace as its dedicated agent.



CcrAgentSlackBindingDeleted object{ actor, agent\_id, slack\_channel\_id, 6 more }

A Claude Code agent's assignment to a Slack channel or workspace was removed.



CcrAgentUpdated object{ actor, agent\_id, default\_source\_urls\_truncated, 10 more }

A Claude Code agent's configuration was updated. Also emitted with updated\_fields ["is\_virtual"] alone when an auto-provisioned agent is promoted to a configured one, whether by an update request targeting it or by binding an agent proxy profile to it.



CcrRoleChannelAssignmentDeleted object{ actor, previous\_channel\_count, role\_id, 5 more }

CcrRoleChannelAssignmentDeleted is emitted when an org owner/admin removes an RBAC role's channel assignment row (the role reverts to granting zero channels).



CcrRoleChannelAssignmentUpdated object{ actor, channel\_count, previous\_channel\_count, 7 more }

CcrRoleChannelAssignmentUpdated is emitted when an org owner/admin sets or replaces the list of Slack channels an RBAC role's holders may configure via the delegated Claude-in-Slack channel-manage surface.



CcrSessionCreated object{ actor, session\_id, id, 5 more }

A Claude Code session was created. A session is one coding interaction with Claude.



CcrSessionDeleted object{ actor, session\_id, id, 4 more }

A Claude Code session was deleted.



CcrSessionUpdated object{ actor, session\_id, id, 5 more }

A Claude Code session's settings were updated.



ClaudeChatSettingsUpdated object{ actor, claude\_chat\_id, id, 5 more }

User updated the settings for a conversation.



ClaudeChatSnapshotCreated object{ actor, claude\_chat\_id, claude\_chat\_snapshot\_id, 5 more }

User created/shared a chat snapshot.



ClaudeChatSnapshotDeleted object{ actor, claude\_chat\_snapshot\_id, id, 5 more }

User deleted/unshared a chat snapshot.



ClaudeChatSnapshotViewed object{ actor, claude\_chat\_snapshot\_id, id, 5 more }

User viewed a chat snapshot (authenticated or public/unauthenticated).



ClaudeArtifactDuplicated object{ actor, claude\_artifact\_id, source\_claude\_artifact\_id, 6 more }

A user duplicated an artifact they could view into a new artifact that they own. The actor is the user who created the copy; the source artifact is not modified.



ClaudeChatAccessFailed object{ actor, claude\_chat\_id, id, 4 more }

A user was denied access to a Claude.ai chat conversation.



ClaudeChatCreated object{ actor, claude\_chat\_id, id, 5 more }

User created a chat.



ClaudeChatDeleted object{ actor, claude\_chat\_id, id, 5 more }

A user deleted a Claude.ai chat conversation.



ClaudeChatDeletionFailed object{ actor, claude\_chat\_id, id, 4 more }

A request to delete a Claude.ai chat conversation failed.



ClaudeChatSyncSourceCreated object{ actor, claude\_chat\_sync\_source\_id, provider, 6 more }

A sync source was connected for syncing external content into Claude chats.



ClaudeChatSyncSourceDeleted object{ actor, claude\_chat\_sync\_source\_id, provider, 5 more }

A sync source was disconnected from Claude chats.



ClaudeChatSyncSourceUpdated object{ actor, claude\_chat\_sync\_source\_id, provider, 7 more }

A Claude chat sync source's configuration was updated.



ClaudeChatUpdated object{ actor, claude\_chat\_id, id, 5 more }

User updated the chat metadata (e.g name, model).



ClaudeChatViewed object{ actor, claude\_chat\_id, id, 5 more }

A user viewed a Claude.ai chat conversation.



ClaudeCodeCredentialRevoked object{ actor, credential\_type, id, 11 more }

A Claude Code credential (runner pool key, runner token, or session token) was revoked. The credential itself is never recorded.



ClaudeCodeReviewConfigUpdated object{ actor, enabled, id, 15 more }

Claude Code Review configuration was enabled/disabled for an org.



ClaudeCodeReviewRepositoryAdded object{ actor, config\_id, repo\_name, 7 more }

A repository was added to org-level Claude Code Review configuration.



ClaudeCodeReviewRepositoryRemoved object{ actor, config\_id, repo\_name, 6 more }

A repository was removed from org-level Claude Code Review configuration.



ClaudeCodeReviewRepositoryUpdated object{ actor, config\_id, repo\_name, 8 more }

A Claude Code Review repository configuration was updated.



ClaudeCodeRunnerDeleted object{ actor, runner\_id, id, 5 more }

A self-hosted runner was forcibly removed from its pool. Sessions assigned to the runner were returned to the pool queue, unless a session had already been requeued repeatedly, in which case it was marked stuck instead of being requeued again.



ClaudeCodeRunnerPoolCreated object{ actor, display\_name, runner\_pool\_id, 5 more }

A self-hosted runner pool for Claude Code was created.



ClaudeCodeRunnerPoolDeleted object{ actor, runner\_pool\_id, id, 5 more }

A self-hosted runner pool was deleted.



ClaudeCodeRunnerPoolSecretMinted object{ actor, jti, runner\_pool\_id, 7 more }

A registration key for a self-hosted runner pool was minted. Runners present this key to join the pool. The key itself is never recorded.



ClaudeCodeRunnerPoolSessionQueueUpdated object{ action, actor, session\_id, 7 more }

An admin changed a session's position in its self-hosted runner pool's queue: requeued it onto a different runner, dismissed it from the queue, or re-admitted it for another runner provisioning attempt.



ClaudeCodeRunnerPoolUpdated object{ actor, display\_name, runner\_pool\_id, 6 more }

A self-hosted runner pool's settings were updated.



ClaudeCodeSecurityCenterConfigUpdated object{ actor, enabled, id, 5 more }

Claude Code Security Center scanning was enabled/disabled for an org.



ClaudeCodeSecurityScanCancelled object{ actor, scan\_project\_id, scans\_cancelled, 5 more }

In-flight Claude Code Security scans were cancelled for a project.



ClaudeCodeSecurityScanCreated object{ actor, scan\_id, scan\_project\_id, 5 more }

A Claude Code Security scan was started.



ClaudeCodeSecurityScanProjectMemberUpdated object{ action, actor, member\_id, 7 more }

A person's access to a Claude Code Security scan project was granted, changed, or revoked.



ClaudeCodeSecurityScanProjectUpdated object{ action, actor, scan\_project\_id, 5 more }

A Claude Code Security scan project was archived, unarchived, created, or migrated to a new product experience.



ClaudeCodeSecurityScanProjectVisibilityUpdated object{ action, actor, scan\_project\_id, 6 more }

A Claude Code Security scan project was shared with the organization or made private.



ClaudeCodeSecurityScanRunUpdated object{ action, actor, scan\_id, 5 more }

A single Claude Code Security scan run was archived, unarchived, or resumed after a billing pause.



ClaudeCodeSecurityScanScheduleDeleted object{ actor, scan\_project\_id, id, 4 more }

A recurring scan schedule was deleted for a Claude Code Security project.



ClaudeCodeSecurityScanScheduleUpdated object{ actor, cadence, scan\_project\_id, 5 more }

A recurring scan schedule was set or replaced for a Claude Code Security project.



ClaudeCodeSecurityVulnerabilityFixSessionCreated object{ actor, scan\_id, session\_id, 5 more }

A Claude Code remediation session was created for a Claude Code Security vulnerability finding.



ClaudeCodeSecurityVulnerabilityUpdated object{ action, actor, scan\_id, 6 more }

A Claude Code Security vulnerability finding was dismissed, restored, marked fixed, or reopened.



ClaudeCodeSecurityWebhookCreated object{ actor, url, webhook\_id, 6 more }

A Claude Code Security outbound webhook was created.



ClaudeCodeSecurityWebhookDeleted object{ actor, webhook\_id, id, 5 more }

A Claude Code Security outbound webhook was deleted.



ClaudeCodeSecurityWebhookSecretUpdated object{ actor, webhook\_id, id, 5 more }

The HMAC signing secret for a Claude Code Security webhook was rotated.



ClaudeCodeSecurityWebhookUpdated object{ actor, webhook\_id, id, 5 more }

A Claude Code Security outbound webhook was updated.



ClaudeCodeTeamMemoryACLUpdated object{ action, actor, group\_id, 7 more }

An RBAC group was added to or removed from the Claude Code team-memory ACL.



ClaudeCodeTeamMemoryUpdated object{ actor, deleted\_all, id, 12 more }

Claude Code team memory shared with the organization was updated.



ClaudeCodeTeamOnboardingGuideUpdated object{ action, actor, guide\_short\_code, 9 more }

A Claude Code team onboarding guide was created, updated, or deleted.



ClaudeCodeUserMarketplacesUpdated object{ actor, deleted\_all, id, 10 more }

A user's Claude Code plugin marketplace selections were updated on Anthropic servers.



ClaudeCodeUserMemoryUpdated object{ actor, deleted\_all, id, 11 more }

A user's synced private Claude Code memory was updated or deleted on Anthropic servers.



ClaudeCodeUserPluginsUpdated object{ actor, deleted\_all, id, 10 more }

A user's Claude Code plugin selections — which plugins are installed and enabled — were updated on Anthropic servers.



ClaudeCodeUserSettingsUpdated object{ actor, deleted\_all, id, 10 more }

A user's synced Claude Code settings were updated or deleted on Anthropic servers.



ClaudeEnterpriseUpgradeCreditUpdated object{ action, actor, id, 4 more }

An organization admin cancelled, or turned back on, the monthly usage credit the organization receives for upgrading from the Team plan to the Enterprise plan, together with the recurring monthly charge that accompanies it.



ClaudeFileAccessFailed object{ actor, claude\_file\_id, id, 7 more }

A user was denied access to a file in Claude.ai.



ClaudeFileExported object{ actor, export\_destination, filename, 7 more }

A file was exported from Claude to an external storage destination.



ClaudeFileViewed object{ actor, claude\_file\_id, id, 7 more }

A user viewed a file in Claude.ai.



ClaudeProjectSyncSourceCreated object{ actor, claude\_project\_id, claude\_project\_sync\_source\_id, 7 more }

A sync source was connected to a Claude project's knowledge base.



ClaudeProjectSyncSourceDeleted object{ actor, claude\_project\_id, claude\_project\_sync\_source\_id, 6 more }

A sync source was disconnected from a Claude project's knowledge base.



ClaudeProjectSyncSourceUpdated object{ actor, claude\_project\_id, claude\_project\_sync\_source\_id, 8 more }

A Claude project sync source's configuration was updated.



ClaudeUserSeatTierUpdated object{ actor, user\_email, user\_id, 7 more }

An organization member's seat tier was changed. A null `previous_seat_tier` means the member previously had no seat assigned; a null `current_seat_tier` means the seat was removed.



CliPluginExecPolicyUpdated object{ actor, cli\_name, marketplace\_id, 10 more }

Admin set or cleared the per-op permission ceiling for a plugin CLI.



ClaudeCommandCreated object{ actor, id, command\_id, 5 more }

Command was created.



ClaudeCommandDeleted object{ actor, id, command\_id, 5 more }

Command was deleted.



ClaudeCommandReplaced object{ actor, id, command\_id, 5 more }

Command was replaced.



ComplianceAPIAccessed object{ actor, request\_id, request\_method, 8 more }

Logging event auto-generated for each compliance API request.



CoworkSessionUpdated object{ actor, cowork\_session\_id, id, 5 more }

A Cowork session was updated.



DesignProjectArtifactPublished object{ actor, design\_project\_id, id, 6 more }

A Claude Design project's content was published as a claude.ai artifact, making a snapshot of one of its files viewable outside the project's sharing settings.



DesignProjectCreated object{ actor, creation\_method, design\_project\_id, 7 more }

A Claude Design project was created.



DesignProjectDeleted object{ actor, design\_project\_id, id, 4 more }

A Claude Design project was deleted.



DesignProjectMemberAdded object{ actor, design\_project\_id, principal\_id, 8 more }

A member was granted access to a Claude Design project.



DesignProjectMemberRemoved object{ actor, design\_project\_id, principal\_id, 7 more }

A member's access to a Claude Design project was revoked.



DesignProjectMemberRoleUpdated object{ actor, design\_project\_id, principal\_id, 9 more }

A Claude Design project member's role was changed.



DesignProjectPublished object{ actor, design\_project\_id, id, 5 more }

A Claude Design template or design system was published, making it discoverable by everyone in its organization.



DesignProjectSharingUpdated object{ actor, design\_project\_id, new\_link\_permission, 9 more }

A Claude Design project's link-sharing settings were changed — who the project's link works for, and what people opening it through the link may do. Access granted to individual members is reported separately (see design\_project\_member\_added).



DesignProjectUnpublished object{ actor, design\_project\_id, id, 5 more }

A Claude Design template or design system was unpublished, removing it from its organization's shared gallery.



DesignProjectUpdated object{ actor, design\_project\_id, id, 6 more }

A Claude Design project's metadata was updated.



DesignProjectVersionRestored object{ actor, design\_project\_id, id, 5 more }

A Claude Design project's working tree was rolled back to a previously saved version, replacing its current files with that version's files.



DesignProjectViewed object{ actor, design\_project\_id, surface, 7 more }

A Claude Design project's content was read. The surface field records which kind of read — a project open, a full-content read, a single-file read, a saved-version read, or an export request. The actor is the reader.

This activity type is retired: project content reads are no longer
recorded. Events of this type may still appear in feeds for reads that
occurred while it was active.



DesktopExtensionAllowlisted object{ actor, extension\_id, id, 4 more }

A desktop extension was added to an org's allowlist.



DesktopExtensionBlocklisted object{ actor, extension\_id, id, 4 more }

A desktop extension was added to the global blocklist.



DesktopExtensionDeleted object{ actor, extension\_id, id, 5 more }

A desktop extension was deleted, either globally by an admin or org-scoped by an org owner.



DesktopExtensionRemovedFromAllowlist object{ actor, extension\_id, id, 4 more }

A desktop extension was removed from an org's allowlist.



DesktopExtensionUnblocked object{ actor, extension\_id, id, 4 more }

A desktop extension was removed from the global blocklist.



DesktopExtensionUploaded object{ actor, extension\_id, version, 5 more }

A desktop extension was uploaded, either globally by an admin or org-scoped by an org owner.



DesktopExtensionVersionUploaded object{ actor, extension\_id, version, 5 more }

A new version of an existing org-owned desktop extension was uploaded.



InferenceHooksConfigDeleted object{ actor, id, created\_at, 3 more }

Inference hooks configuration was removed for the
organization.



InferenceHooksConfigUpdated object{ actor, enabled, enforcement\_mode, 15 more }

Inference hooks configuration was created or updated for the
organization.



InferenceHooksSigningSecretGenerated object{ actor, rotated, id, 4 more }

A request signing secret was generated for the organization's
Inference hooks configuration.



DomainClaimInitiated object{ actor, id, created\_at, 3 more }

Domain capture claim initiated over personal accounts on verified domains.



EndUserInviteRequested object{ actor, invitee\_email, id, 4 more }

Non-admin member submitted an invite request for a new org member.



ExtraUsageBillingEnabled object{ actor, id, created\_at, 3 more }

Usage credit billing was enabled for an organization.



ExtraUsageCreditGranted object{ actor, id, created\_at, 3 more }

A promotional usage credit grant was claimed.



ExtraUsageSpendLimitCreated object{ actor, id, amount, 8 more }

Usage credit spend limit was created.



ExtraUsageSpendLimitDeleted object{ actor, id, created\_at, 5 more }

Usage credit spend limit was deleted.



ExtraUsageSpendLimitIncreaseRequestApproved object{ actor, id, amount, 7 more }

A usage credit spend limit increase request was approved.



ExtraUsageSpendLimitIncreaseRequestDenied object{ actor, id, created\_at, 5 more }

A usage credit spend limit increase request was denied.



ExtraUsageSpendLimitUpdated object{ actor, id, amount, 8 more }

Usage credit spend limit was updated.



ClaudeFileDeleted object{ actor, claude\_file\_id, filename, 5 more }

A file was deleted.



ClaudeFileUploaded object{ actor, claude\_file\_id, filename, 7 more }

A file was uploaded.



GheConfigurationCreated object{ actor, ghe\_configuration\_id, id, 7 more }

Admin created a GHE configuration.



GheConfigurationDeleted object{ actor, ghe\_configuration\_id, id, 7 more }

Admin deleted a GHE configuration.



GheConfigurationUpdated object{ actor, ghe\_configuration\_id, id, 20 more }

Admin updated a GHE configuration. Previous/new field pairs are recorded only for settings that changed in the update; secret credentials are never recorded, only whether they were replaced.



GheUserConnected object{ actor, id, created\_at, 4 more }

User connected to a GHE instance.



GheUserDisconnected object{ actor, id, created\_at, 4 more }

User disconnected from a GHE instance.



GheWebhookSignatureInvalid object{ actor, ghe\_configuration\_id, id, 4 more }

Webhook signature validation failed.



ClaudeGitHubIntegrationCreated object{ actor, integration\_id, id, 8 more }

A GitHub integration was enabled for the organization.



ClaudeGitHubIntegrationDeleted object{ actor, integration\_id, id, 8 more }

A GitHub integration was disabled for the organization.



ClaudeGitHubIntegrationUpdated object{ actor, integration\_id, id, 6 more }

A GitHub integration's configuration was updated.



GitHubTokenImport object{ actor, result, source, 8 more }

A user attempted to import a personal GitHub access token for use with Claude Code. The `result` field indicates the outcome of the import (imported, rejected, or failed).



ClaudeGdriveIntegrationCreated object{ actor, integration\_id, id, 5 more }

A Google Drive integration was enabled for the organization.



ClaudeGdriveIntegrationDeleted object{ actor, integration\_id, id, 5 more }

A Google Drive integration was disabled for the organization.



ClaudeGdriveIntegrationUpdated object{ actor, integration\_id, id, 5 more }

A Google Drive integration's configuration was updated.



GroupCreated object{ actor, group\_id, group\_name, 5 more }

A group was created (RBAC admin or SCIM provisioning).



GroupDeleted object{ actor, group\_id, id, 4 more }

A group was deleted (RBAC admin or SCIM provisioning).



GroupListViewed object{ actor, id, created\_at, 3 more }

Admin viewed the list of RBAC groups.



GroupMemberAdded object{ actor, group\_id, id, 5 more }

One or more members were added to a group.



GroupMemberAdditionFailed object{ actor, group\_id, id, 5 more }

A request to add members to a group failed. Some of the requested members may have been added before the failure.



GroupMemberListViewed object{ actor, group\_id, id, 4 more }

Admin viewed the members of an RBAC group.



GroupMemberRemovalFailed object{ actor, group\_id, id, 5 more }

A request to remove members from a group failed. Some of the requested members may have been removed before the failure.



GroupMemberRemoved object{ actor, group\_id, id, 5 more }

One or more members were removed from a group.



GroupProjectSharesRevoked object{ actor, group\_id, revoked\_count, 6 more }

An RBAC group's project shares in one organization were revoked in bulk.



GroupSkillSharesRevoked object{ actor, group\_id, revoked\_count, 7 more }

An RBAC group's skill shares in one organization were revoked in bulk.



GroupUpdated object{ actor, group\_id, id, 4 more }

A group was updated (RBAC admin or SCIM provisioning).



GroupViewed object{ actor, group\_id, id, 4 more }

A group was viewed.



GroupVisibilityUpdated object{ actor, group\_id, id, 6 more }

An RBAC group's visibility policy was updated.



InferenceHooksCircuitBreakerTripped object{ actor, fail\_mode, trigger\_reason, 6 more }

The organization's Inference hooks circuit breaker tripped automatically: calls to the organization's Inference hooks endpoint crossed a failure threshold, and inspection was suspended to protect live traffic. While tripped, requests are handled according to the organization's failure handling setting — allowed through uninspected (fail open) or rejected (fail closed) — and no per-request Inference hooks activities are recorded. The tripped state persists until an administrator re-enables Inference hooks inspection (or explicitly resets the circuit breaker).



InferenceHooksRequestDenied object{ actor, id, conversation\_id, 7 more }

Inference hooks inspection denied a request. The request was blocked and no model response was produced.



InferenceHooksRequestFailedOpen object{ actor, reason, id, 6 more }

A request proceeded without Inference hooks inspection because a verdict could not be obtained and the organization's Inference hooks configuration is set to fail open.



IntegrationUserConnected object{ actor, id, created\_at, 7 more }

User connected to an integration.



IntegrationUserDisconnected object{ actor, id, created\_at, 6 more }

User disconnected from an integration.



InvoiceCollectionMethodUpdated object{ actor, id, created\_at, 4 more }

Invoice collection method was changed.



UserLoggedOut object{ actor, id, created\_at, 3 more }

A user signed out of one or all sessions.



LtiLaunchInitiated object{ actor, id, created\_at, 3 more }

LTI launch was initiated.



LtiLaunchSuccess object{ actor, id, created\_at, 3 more }

LTI launch completed successfully.



LtiPlatformCreated object{ actor, lti\_platform\_id, lti\_platform\_issuer, 5 more }

Anthropic staff created an LTI platform integration on behalf of an org.



LtiPlatformUpdated object{ actor, lti\_platform\_id, id, 5 more }

Anthropic staff updated an LTI platform integration on behalf of an org.



MagicLinkLoginFailed object{ actor, id, created\_at, 3 more }

A magic link sign-in attempt failed.



MagicLinkLoginInitiated object{ actor, id, created\_at, 3 more }

A user requested a magic link sign-in email.



MagicLinkLoginSucceeded object{ actor, id, auth\_method, 5 more }

A user successfully signed in with a magic link email.



ManagedOrganizationSetupCompleted object{ actor, id, created\_at, 3 more }

Managed (AWS Marketplace) organization setup was completed.



MarketplaceCreated object{ actor, marketplace\_id, id, 4 more }

Admin created an organization marketplace.



MarketplaceDeleted object{ actor, marketplace\_id, id, 4 more }

Admin deleted an organization marketplace.



MarketplaceUpdated object{ actor, marketplace\_id, id, 4 more }

Admin updated an organization marketplace.



MarketplaceWebhookDeleted object{ actor, marketplace\_id, id, 4 more }

Admin removed the GitHub push webhook for a marketplace.



MarketplaceWebhookProvisioned object{ actor, marketplace\_id, id, 5 more }

Admin provisioned a GitHub push webhook for a marketplace.



McpDirectoryServerPublished object{ actor, mcp\_directory\_server\_id, mcp\_directory\_server\_name, 5 more }

The organization published its approved MCP directory listing.



McpServerCreated object{ actor, mcp\_server\_id, mcp\_server\_name, 5 more }

An MCP server was added to the organization.



McpServerDeleted object{ actor, mcp\_server\_id, mcp\_server\_name, 5 more }

An MCP server was removed from the organization.



McpServerManagedAuthTokenExchanged object{ actor, managed\_auth\_mode, mcp\_server\_id, 12 more }

A user attempted to obtain an access token for an MCP server via enterprise managed authorization. This event reports the outcomes of attempted token exchanges. Repeated failures with the same cause may be reported once until the cause changes, and requests denied by organization policy before a token exchange is attempted are not reported, with the exception of the "connector\_scope\_not\_granted" failures described under error\_type.



McpServerManagedAuthUpdated object{ actor, mcp\_server\_id, mcp\_server\_name, 15 more }

An MCP server's enterprise managed authorization settings were set, changed, or cleared, including when they were supplied while the server was being added or edited. Fields without a "previous\_" prefix describe the settings after the change and are null when the server has no managed authorization settings afterwards; "previous\_" fields describe the settings before the change and are null when the server had none before (always the case for a newly added server).



McpServerUpdated object{ actor, mcp\_server\_id, mcp\_server\_name, 5 more }

An MCP server's configuration was updated.



McpToolPolicyUpdated object{ actor, mcp\_server\_id, mcp\_server\_name, 7 more }

The permission restriction for an MCP tool was set or cleared.



OrgAnalyticsAPICapabilityUpdated object{ actor, id, created\_at, 5 more }

Organization analytics\_api capability was enabled or disabled.



OrgBulkDeleteInitiated object{ actor, id, created\_at, 3 more }

Organization bulk deletion was initiated.



OrgCapabilityGrantAdded object{ actor, grant\_type, principal\_id, 6 more }

A capability grant was added to a workspace or role.



OrgCapabilityGrantRemoved object{ actor, grant\_type, principal\_id, 6 more }

A capability grant was removed from a workspace or role.



OrgClaudeCodeDataSharingDisabled object{ actor, id, created\_at, 5 more }

Organization Claude Code data sharing was disabled.



OrgClaudeCodeDataSharingEnabled object{ actor, id, created\_at, 5 more }

Organization Claude Code data sharing was enabled.



OrgClaudeCodeDesktopDisabled object{ actor, id, created\_at, 5 more }

Organization Claude Code Desktop was disabled.



OrgClaudeCodeDesktopEnabled object{ actor, id, created\_at, 5 more }

Organization Claude Code Desktop was enabled.



OrgClaudeCodeZeroDataRetentionDisabled object{ actor, id, created\_at, 3 more }

A primary owner disabled zero data retention for Claude Code, so Claude
Code content is retained according to the organization's data retention
settings.



OrgComplianceAPISettingsUpdated object{ actor, id, compliance\_api\_enabled, 5 more }

Organization compliance API settings were updated.



OrgConnectorDomainGuardUpdated object{ actor, enforced, id, 4 more }

Enterprise admin changed whether connectors are restricted to verified domains.



OrgCoworkActWithoutAskingModeDisabled object{ actor, id, created\_at, 3 more }

The "Act without asking" mode in Cowork was disabled for the organization, so members can no longer let Claude act without asking for approval.



OrgCoworkActWithoutAskingModeEnabled object{ actor, id, created\_at, 3 more }

The "Act without asking" mode in Cowork was enabled for the organization, allowing members to let Claude act without asking for approval.



OrgCoworkAgentDisabled object{ actor, id, created\_at, 5 more }

Organization Cowork Agent was disabled.



OrgCoworkAgentEnabled object{ actor, id, created\_at, 5 more }

Organization Cowork Agent was enabled.



OrgCoworkAutoModeDisabled object{ actor, id, created\_at, 3 more }

The "Auto" permission mode in Cowork was disabled for the organization, so members can no longer let Claude approve its own actions after a safety check.



OrgCoworkAutoModeEnabled object{ actor, id, created\_at, 3 more }

The "Auto" permission mode in Cowork was enabled for the organization, allowing members to let Claude approve its own actions after a safety check.



OrgCoworkDisabled object{ actor, id, created\_at, 5 more }

Organization cowork was disabled.



OrgCoworkEnabled object{ actor, id, created\_at, 5 more }

Organization cowork was enabled.



OrgCoworkMcpAlwaysAllowDisabled object{ actor, id, created\_at, 3 more }

The "Always allow" option for connector tools in Cowork was disabled for the organization, so each use of a connector tool that can make changes requires approval. Read-only connector tools are not affected by this setting.



OrgCoworkMcpAlwaysAllowEnabled object{ actor, id, created\_at, 3 more }

The "Always allow" option for connector tools in Cowork was enabled for the organization, letting members approve a connector tool that can make changes once and allow its later uses automatically. Read-only connector tools are not affected by this setting.



OrgCoworkOtlpSettingsUpdated object{ actor, id, created\_at, 12 more }

The organization's Cowork OpenTelemetry monitoring export settings were updated.



OrgCoworkRemoteDisabled object{ actor, id, created\_at, 3 more }

Running Cowork in the cloud was disabled for the organization, so members can no longer run Cowork sessions in Anthropic-hosted remote environments.



OrgCoworkRemoteEnabled object{ actor, id, created\_at, 3 more }

Running Cowork in the cloud was enabled for the organization, allowing members to run Cowork sessions in Anthropic-hosted remote environments.



OrgCreationBlocked object{ actor, id, created\_at, 4 more }

Organization creation was blocked.



OrgDataExportAccessed object{ actor, id, created\_at, 4 more }

Organization data export file was accessed/downloaded via signed URL.



OrgDataExportCompleted object{ actor, id, created\_at, 4 more }

Organization data export was completed.



OrgDataExportStarted object{ actor, id, created\_at, 5 more }

Organization data export was started.



OrgDataResidencyUpdated object{ actor, updates, id, 4 more }

The organization's inference data residency settings were updated.



OrgDeletedViaBulk object{ actor, id, created\_at, 3 more }

Organization was deleted via bulk operation.



OrgDeletionRequested object{ actor, id, created\_at, 3 more }

Organization deletion was requested.



OrgDirectoryResyncCompleted object{ actor, resync\_uuid, id, 4 more }

Organization directory resync completed successfully.



OrgDirectoryResyncFailed object{ actor, resync\_uuid, id, 4 more }

Organization directory resync failed.



OrgDirectoryResyncStarted object{ actor, resync\_uuid, sync\_destinations, 5 more }

Organization directory resync was started asynchronously.



OrgDirectorySyncActivated object{ actor, id, created\_at, 3 more }

Organization directory sync was activated.



OrgDirectorySyncAddInitiated object{ actor, id, created\_at, 3 more }

Organization directory sync setup was initiated.



OrgDirectorySyncDeleted object{ actor, id, created\_at, 3 more }

Organization directory sync was deleted.



OrgDiscoverabilityDisabled object{ actor, id, created\_at, 3 more }

Admin disabled organization discoverability.



OrgDiscoverabilityEnabled object{ actor, id, created\_at, 3 more }

Admin enabled organization discoverability.



OrgDiscoverabilitySettingsUpdated object{ actor, id, created\_at, 3 more }

Admin updated organization discoverability settings.



OrgDomainAddInitiated object{ actor, id, created\_at, 3 more }

Organization domain verification was initiated.



OrgDomainRemoved object{ actor, id, created\_at, 4 more }

Organization domain was removed.



OrgDomainVerified object{ actor, id, created\_at, 4 more }

Organization domain was verified.



OrgExternalKeyCreated object{ actor, external\_key\_id, provider, 5 more }

A CMEK external key config was created.



OrgExternalKeyDeleted object{ actor, external\_key\_id, id, 4 more }

A CMEK external key config was deleted.



OrgExternalKeyUpdated object{ actor, external\_key\_id, id, 5 more }

A CMEK external key config was updated.



OrgExternalKeyValidated object{ actor, external\_key\_id, validation\_result, 5 more }

A CMEK external key config was validated against the customer's KMS.



OrgHipaaSelfServeEnabled object{ actor, baa\_content\_hash, baa\_version\_label, 6 more }

A primary owner click-accepted the BAA and enabled HIPAA protections
for the organization via the self-serve flow.



OrgIPRestrictionCreated object{ actor, id, created\_at, 3 more }

Organization IP restriction was created.



OrgIPRestrictionDeleted object{ actor, id, created\_at, 3 more }

Organization IP restriction was deleted.



OrgIPRestrictionUpdated object{ actor, id, created\_at, 3 more }

Organization IP restriction was updated.



OrgInviteLinkDisabled object{ actor, id, created\_at, 3 more }

Organization invite link was disabled.



OrgInviteLinkGenerated object{ actor, id, created\_at, 3 more }

Organization invite link was generated.



OrgInviteLinkRegenerated object{ actor, id, created\_at, 3 more }

Organization invite link was regenerated (previous link invalidated).



OrgInviteViewed object{ actor, invite\_id, id, 4 more }

An organization invite was viewed.



OrgInvitesListed object{ actor, id, created\_at, 3 more }

Organization invites were listed.



OrgJoinProposalDecided object{ actor, approved, id, 4 more }

Approve or reject decision on a parent-org join proposal.



OrgJoinRequestApproved object{ actor, id, created\_at, 3 more }

Admin approved a join request.



OrgJoinRequestCreated object{ actor, id, created\_at, 3 more }

User requested to join an organization.



OrgJoinRequestDismissed object{ actor, id, created\_at, 3 more }

Admin dismissed a join request.



OrgJoinRequestInstantApproved object{ actor, id, created\_at, 3 more }

Join request was instantly approved.



OrgJoinRequestsBulkDismissed object{ actor, id, created\_at, 3 more }

Admin bulk-dismissed join requests.



OrgMagicLinkSecondFactorToggled object{ actor, enabled, id, 4 more }

Organization magic link second factor was toggled.



OrgMemberInvitesDisabled object{ actor, id, created\_at, 3 more }

Admin disabled member invites for the organization.



OrgMemberInvitesEnabled object{ actor, id, created\_at, 3 more }

Admin enabled member invites for the organization.



OrgMembersExported object{ actor, id, created\_at, 3 more }

Organization members list was exported as CSV.



OrgModelDefaultUpdated object{ action, actor, override\_user\_selection, 9 more }

An organization or role default model setting was changed by an administrator.



OrgParentJoinProposalCreated object{ actor, id, created\_at, 3 more }

Organization parent join proposal was created.



OrgParentSearchPerformed object{ actor, id, created\_at, 3 more }

Organization parent search was performed.



OrgSSOAddInitiated object{ actor, id, created\_at, 3 more }

Organization SSO setup was initiated.



OrgSSOConnectionActivated object{ actor, id, connection\_id, 5 more }

Organization SSO connection was activated.



OrgSSOConnectionDeactivated object{ actor, id, connection\_id, 4 more }

Organization SSO connection was deactivated.



OrgSSOConnectionDeleted object{ actor, id, connection\_id, 4 more }

Organization SSO connection was deleted.



OrgSSOGroupRoleMappingsUpdated object{ actor, id, created\_at, 3 more }

Organization SSO group role mappings were updated.



OrgSSOProvisioningModeChanged object{ actor, id, created\_at, 5 more }

Organization SSO provisioning mode was changed.



OrgSSOScimWelcomeEmailToggled object{ actor, enabled, id, 5 more }

Organization SCIM-provisioned welcome email was toggled.



OrgSSOSeatTierAssignmentToggled object{ actor, enabled, id, 5 more }

Organization SSO seat tier assignment was toggled.



OrgSSOSeatTierMappingsUpdated object{ actor, id, created\_at, 5 more }

Organization SSO seat tier mappings were updated.



OrgSSOToggled object{ actor, enabled, id, 4 more }

Organization SSO was toggled on or off.



OrgSyncDeletingSynchronizedFilesStarted object{ actor, id, created\_at, 3 more }

Organization started deleting synchronized files.



OrgSyncSynchronizedFilesDeleted object{ actor, id, created\_at, 3 more }

Organization synchronized files were deleted.



OrgTaintAdded object{ actor, id, created\_at, 5 more }

A taint was added to an organization.



OrgTaintRemoved object{ actor, id, created\_at, 4 more }

A taint was removed from an organization.



OrgUserDeleted object{ actor, id, created\_at, 5 more }

User was removed from organization.



OrgUserInviteAccepted object{ actor, id, created\_at, 5 more }

Organization user invite was accepted.



OrgUserInviteDeleted object{ actor, id, created\_at, 4 more }

Organization user invite was deleted.



OrgUserInviteReSent object{ actor, id, created\_at, 6 more }

Organization user invite was re-sent.



OrgUserInviteRejected object{ actor, id, created\_at, 4 more }

Organization user invite was rejected.



OrgUserInviteSent object{ actor, id, created\_at, 7 more }

Organization user invite was sent.



OrgUserLeft object{ actor, id, created\_at, 4 more }

User removed themselves from organization.



OrgUserTrustedDevicesRevoked object{ actor, completed, devices\_revoked\_count, 7 more }

An organization admin revoked a member's trusted devices and signed the member out of all active sessions.



OrgUserViewed object{ actor, user\_id, id, 4 more }

An organization user was viewed.



OrgUsersListed object{ actor, id, created\_at, 3 more }

Organization users were listed.



OrgWorkAcrossAppsDisabled object{ actor, id, created\_at, 5 more }

The organization's "Let Claude work across apps" setting was turned off.



OrgWorkAcrossAppsEnabled object{ actor, id, created\_at, 5 more }

The organization's "Let Claude work across apps" setting was turned on.



OrganizationAddressUpdated object{ actor, id, billing\_address\_updated, 7 more }

The organization's billing or shipping address was updated.



OrganizationIconDeleted object{ actor, id, created\_at, 3 more }

Organization's custom icon deleted.



OrganizationIconUpdated object{ actor, id, created\_at, 3 more }

Organization's custom icon uploaded or replaced.



ClaudeOrganizationSettingsUpdated object{ actor, updates, id, 4 more }

Organization settings were updated.



OwnedProjectsAccessRestored object{ actor, id, created\_at, 4 more }

Access to owned projects was restored.



PaymentMethodUpdated object{ actor, id, created\_at, 3 more }

The organization's default payment method was updated.



PendingShareCreated object{ actor, invitee\_email, resource\_id, 7 more }

A pending share of a project or skill was created for an email address that is not yet an organization member.



PendingShareRevoked object{ actor, invitee\_email, resource\_id, 6 more }

A pending share of a project or skill was revoked before the invitee joined the organization.



PhoneCodeSent object{ actor, id, created\_at, 3 more }

User requested a phone verification code.



PhoneCodeVerified object{ actor, id, created\_at, 3 more }

User successfully verified their phone code.



PlatformAgentArchived object{ actor, agent\_id, id, 5 more }

An agent was archived on the API platform.



PlatformAgentCreated object{ actor, agent\_id, id, 5 more }

An agent was created on the API platform.



PlatformAgentDeleted object{ actor, agent\_id, id, 5 more }

An agent was deleted from the API platform.



PlatformAgentDeploymentArchived object{ actor, deployment\_id, id, 5 more }

An agent deployment was archived on the API platform.



PlatformAgentDeploymentCreated object{ actor, deployment\_id, id, 5 more }

An agent deployment was created on the API platform.



PlatformAgentDeploymentDeleted object{ actor, deployment\_id, id, 5 more }

An agent deployment was deleted from the API platform.



PlatformAgentDeploymentPaused object{ actor, deployment\_id, id, 5 more }

An agent deployment was paused on the API platform.



PlatformAgentDeploymentRunTriggered object{ actor, deployment\_id, id, 5 more }

An agent deployment was run on demand on the API platform.



PlatformAgentDeploymentUnpaused object{ actor, deployment\_id, id, 5 more }

An agent deployment was resumed on the API platform.



PlatformAgentDeploymentUpdated object{ actor, deployment\_id, id, 5 more }

An agent deployment was updated on the API platform.



PlatformAgentSessionArchived object{ actor, session\_id, id, 5 more }

An agent session was archived on the API platform.



PlatformAgentSessionCreated object{ actor, session\_id, id, 5 more }

An agent session was created on the API platform.



PlatformAgentSessionDeleted object{ actor, session\_id, id, 5 more }

An agent session was deleted from the API platform.



PlatformAgentSessionResourceAdded object{ actor, resource\_id, session\_id, 6 more }

A resource was attached to an agent session.



PlatformAgentSessionResourceDeleted object{ actor, resource\_id, session\_id, 6 more }

A resource attached to an agent session was removed.



PlatformAgentSessionResourceUpdated object{ actor, resource\_id, session\_id, 6 more }

A resource attached to an agent session was updated.



PlatformAgentSessionThreadArchived object{ actor, session\_id, thread\_id, 6 more }

A thread within an agent session was archived.



PlatformAgentSessionUpdated object{ actor, session\_id, id, 5 more }

An agent session was updated on the API platform.



PlatformAgentUpdated object{ actor, agent\_id, id, 5 more }

An agent was updated on the API platform.



PlatformAPIKeyCreated object{ actor, api\_key\_id, id, 4 more }

An API key was created.



PlatformAPIKeyUpdated object{ actor, api\_key\_id, updates, 5 more }

An API key was updated.



PlatformAppAttestAuthentication object{ actor, id, created\_at, 6 more }

An attested mobile device attempted to exchange an Apple App Attest assertion for Anthropic API credentials.



PlatformBillingUpgradedToPrepaid object{ actor, previous\_billing\_type, id, 4 more }

The organization's API billing was upgraded to the prepaid plan.



PlatformClearanceWorkspaceProgramRequestCleared object{ actor, program\_slug, workspace\_id, 5 more }

A workspace's clearance program assignment was removed.



PlatformClearanceWorkspaceProgramRequestSet object{ actor, opt\_decision, program\_slug, 6 more }

A workspace's clearance program assignment was created or updated.



PlatformCostReportViewed object{ actor, id, created\_at, 3 more }

The cost report was viewed.



PlatformDreamArchived object{ actor, dream\_id, id, 5 more }

A Dream (asynchronous memory-consolidation job) was archived.



PlatformDreamCancelled object{ actor, dream\_id, id, 5 more }

A Dream (asynchronous memory-consolidation job) was cancelled before it completed.



PlatformDreamCreated object{ actor, dream\_id, id, 5 more }

A Dream (asynchronous memory-consolidation job) was created.



PlatformFederatedAuthentication object{ actor, id, created\_at, 7 more }

A federated workload identity attempted to exchange an OIDC token for Anthropic API credentials.



PlatformFederationIssuerArchived object{ actor, federation\_issuer\_id, id, 4 more }

An OIDC federation issuer was archived.



PlatformFederationIssuerUpdated object{ actor, federation\_issuer\_id, updates, 5 more }

An OIDC federation issuer was updated.



PlatformFederationRuleArchived object{ actor, federation\_rule\_id, id, 4 more }

An OIDC federation rule was archived.



PlatformFederationRuleUpdated object{ actor, federation\_rule\_id, updates, 5 more }

An OIDC federation rule was updated.



PlatformFederationRuleWorkspaceAdded object{ actor, federation\_rule\_id, workspace\_id, 5 more }

A federation rule was enabled for a workspace.



PlatformFederationRuleWorkspaceRemoved object{ actor, federation\_rule\_id, workspace\_id, 5 more }

A federation rule was disabled for a workspace.



PlatformFileContentDownloaded object{ actor, file\_id, id, 4 more }

Activity logged when file content is downloaded via GET /v1/files/{file\_id}/content.



PlatformFileDeleted object{ actor, file\_id, id, 4 more }

Activity logged when a file is deleted via DELETE /v1/files/{file\_id}.



PlatformFileUploaded object{ actor, file\_id, id, 5 more }

Activity logged when a file is uploaded via POST /v1/files.



PlatformMemoryCreated object{ actor, memory\_id, memory\_store\_id, 7 more }

An agent memory document was created.



PlatformMemoryDeleted object{ actor, memory\_id, memory\_store\_id, 7 more }

An agent memory document was deleted.



PlatformMemoryStoreArchived object{ actor, memory\_store\_id, id, 5 more }

An agent memory store was archived. Archived stores reject new memory writes and cannot be attached to new sessions; deletion and redaction remain permitted for privacy scrubbing.



PlatformMemoryStoreCreated object{ actor, memory\_store\_id, id, 5 more }

An agent memory store was created.



PlatformMemoryStoreDeleted object{ actor, memory\_store\_id, id, 5 more }

An agent memory store was deleted. Memory content removal may complete asynchronously for very large stores.



PlatformMemoryStoreUpdated object{ actor, memory\_store\_id, id, 5 more }

An agent memory store's name, description, or metadata was updated.



PlatformMemoryUpdated object{ actor, memory\_id, memory\_store\_id, 7 more }

An agent memory document's content or path was updated.



PlatformMemoryVersionRedacted object{ actor, memory\_id, memory\_store\_id, 7 more }

A historical version of an agent memory document was redacted. Redaction scrubs the stored content of a specific version while preserving the version's existence in the history.



PlatformOAuthAppCreated object{ actor, oauth\_app\_id, workspace\_id, 5 more }

An OAuth app was created.



PlatformOAuthAppRevoked object{ actor, oauth\_app\_id, id, 4 more }

An OAuth app was revoked.



PlatformOAuthAppUpdated object{ actor, oauth\_app\_id, updates, 5 more }

An OAuth app was updated.



PlatformPluginDirectorySubmissionCreated object{ actor, plugin\_name, submission\_id, 5 more }

A plugin directory submission was created on the API platform. A plugin directory submission is a request to list a plugin in the public plugin directory.



PlatformPluginDirectorySubmissionDeleted object{ actor, submission\_id, id, 4 more }

A plugin directory submission was deleted on the API platform.



PlatformPluginDirectorySubmissionUpdated object{ actor, status, submission\_id, 5 more }

A plugin directory submission was updated on the API platform.



PlatformServiceAccountArchived object{ actor, service\_account\_id, id, 4 more }

A service account was archived.



PlatformServiceAccountUpdated object{ actor, service\_account\_id, updates, 5 more }

A service account was updated.



PlatformServiceAccountWorkspaceMemberAdded object{ actor, service\_account\_id, workspace\_id, 5 more }

A service account was added as a member of a workspace.



PlatformServiceAccountWorkspaceMemberRemoved object{ actor, service\_account\_id, workspace\_id, 5 more }

A service account was removed from a workspace.



PlatformServiceAccountWorkspaceMemberUpdated object{ actor, service\_account\_id, updates, 6 more }

A service account's workspace membership role was updated.



PlatformSigningKeyCreated object{ actor, algorithm, key\_backing\_type, 7 more }

Activity logged when a new request-signing key is registered for the org.



PlatformSigningKeyDeleted object{ actor, algorithm, key\_backing\_type, 7 more }

Activity logged when a signing key is permanently deleted.



PlatformSigningKeyRotated object{ actor, algorithm, key\_group\_identifier, 7 more }

Activity logged when an in-memory signing key is rotated.



PlatformSkillVersionCreated object{ actor, skill\_id, version, 5 more }

Activity logged when a skill version is created via POST /v1/skills/{skill\_id}/versions.



PlatformSkillVersionDeleted object{ actor, skill\_id, version, 5 more }

Activity logged when a skill version is deleted via DELETE /v1/skills/{skill\_id}/versions/{version}.



PlatformSpendLimitAlertEmailsUpdated object{ actor, id, alert\_emails, 5 more }

Spend limit alert email addresses and role targets were updated for an org.



PlatformSpendLimitCreated object{ actor, id, created\_at, 5 more }

An org-level fixed-dollar spend limit was created.



PlatformSpendLimitDeleted object{ actor, id, created\_at, 4 more }

An org-level spend limit was removed.



PlatformSpendLimitUpdated object{ actor, id, created\_at, 5 more }

An org-level spend limit snooze/ignore state was changed.



PlatformUsageReportClaudeCodeViewed object{ actor, id, created\_at, 3 more }

The Claude Code usage report was viewed.



PlatformUsageReportMessagesViewed object{ actor, id, created\_at, 3 more }

The messages usage report was viewed.



PlatformWorkspaceArchived object{ actor, workspace\_id, id, 4 more }

A workspace was archived.



PlatformWorkspaceCreated object{ actor, workspace\_id, id, 4 more }

A workspace was created.



PlatformWorkspaceInferenceDataRetentionDisabled object{ actor, workspace\_id, id, 5 more }

The zero data retention override was disabled for a workspace.



PlatformWorkspaceInferenceDataRetentionEnabled object{ actor, workspace\_id, id, 5 more }

The zero data retention override was enabled for a workspace.



PlatformWorkspaceMemberAdded object{ actor, user\_id, workspace\_id, 5 more }

A member was added to a workspace.



PlatformWorkspaceMemberRemoved object{ actor, user\_id, workspace\_id, 5 more }

A member was removed from a workspace.



PlatformWorkspaceMemberUpdated object{ actor, updates, user\_id, 6 more }

A workspace member was updated.



PlatformWorkspaceMemberViewed object{ actor, user\_id, workspace\_id, 5 more }

A workspace member was viewed.



PlatformWorkspaceMembersListed object{ actor, workspace\_id, id, 4 more }

Workspace members were listed.



PlatformWorkspaceRateLimitDeleted object{ actor, limiter\_type, model\_group, 6 more }

A workspace rate limit was deleted.



PlatformWorkspaceRateLimitUpdated object{ actor, limiter\_type, model\_group, 7 more }

A workspace rate limit was created or updated.



PlatformWorkspaceUpdated object{ actor, workspace\_id, id, 5 more }

A workspace was updated.



ClaudePluginCreated object{ actor, id, created\_at, 5 more }

Plugin was created.



ClaudePluginDeleted object{ actor, id, created\_at, 5 more }

Plugin was deleted.



ClaudePluginDisabled object{ actor, id, created\_at, 6 more }

User disabled a plugin for their account.



ClaudePluginEnabled object{ actor, id, created\_at, 6 more }

User enabled a plugin for their account.



PluginInstallationPreferenceUpdated object{ actor, marketplace\_id, plugin\_name, 9 more }

An org admin changed the installation preference for a plugin.



ClaudePluginReplaced object{ actor, id, created\_at, 5 more }

Plugin was replaced.



ClaudePluginUpdated object{ actor, id, created\_at, 5 more }

Plugin was updated.



PrepaidAutoRechargeDisabled object{ actor, id, created\_at, 3 more }

Auto-recharge was disabled for API prepaid org.



PrepaidAutoRechargeUpdated object{ actor, id, created\_at, 5 more }

Auto-recharge settings were updated for API prepaid org.



PrepaidExtraUsageAutoReloadDisabled object{ actor, id, created\_at, 3 more }

Prepaid usage credit auto-reload was disabled.



PrepaidExtraUsageAutoReloadEnabled object{ actor, id, created\_at, 3 more }

Prepaid usage credit auto-reload was enabled.



PrepaidExtraUsageAutoReloadSettingsUpdated object{ actor, id, created\_at, 3 more }

Prepaid usage credit auto-reload settings were updated.



PrimaryOwnerTransferred object{ actor, new\_owner\_id, previous\_owner\_id, 5 more }

Primary owner role was transferred to another org member.



ClaudeProjectArchived object{ actor, claude\_project\_id, id, 4 more }

A Claude project was archived.



ClaudeProjectCreated object{ actor, claude\_project\_id, id, 4 more }

A Claude project was created.



ClaudeProjectDeleted object{ actor, claude\_project\_id, id, 4 more }

A Claude project was deleted.



ClaudeProjectDocumentAccessFailed object{ actor, claude\_project\_document\_id, claude\_project\_id, 6 more }

An attempt to access a document in a Claude project failed.



ClaudeProjectDocumentBulkDeletionAuditTruncated object{ actor, audited\_count, claude\_project\_id, 6 more }

A bulk request to delete documents from a Claude project failed with more documents requested than were individually recorded in the audit log.



ClaudeProjectDocumentDeleted object{ actor, claude\_project\_document\_id, claude\_project\_id, 6 more }

A document was deleted from a Claude project.



ClaudeProjectDocumentDeletionFailed object{ actor, claude\_project\_document\_id, claude\_project\_id, 6 more }

A request to delete a document from a Claude project failed.



ClaudeProjectDocumentUpdated object{ actor, claude\_project\_document\_id, claude\_project\_id, 6 more }

The content of a document in a Claude project was replaced in place.



ClaudeProjectDocumentUploaded object{ actor, claude\_project\_document\_id, claude\_project\_id, 6 more }

A document was uploaded to a Claude project.



ClaudeProjectDocumentViewed object{ actor, claude\_project\_document\_id, claude\_project\_id, 6 more }

A document in a Claude project was viewed.



ClaudeProjectFileAccessFailed object{ actor, claude\_file\_id, claude\_project\_id, 5 more }

An attempt to access a file in a Claude project failed.



ClaudeProjectFileBulkDeletionAuditTruncated object{ actor, audited\_count, claude\_project\_id, 6 more }

A bulk request to delete files from a Claude project failed with more files requested than were individually recorded in the audit log.



ClaudeProjectFileDeleted object{ actor, claude\_file\_id, claude\_project\_id, 5 more }

A file was deleted from a Claude project.



ClaudeProjectFileDeletionFailed object{ actor, claude\_file\_id, claude\_project\_id, 5 more }

A request to delete a file from a Claude project failed.



ClaudeProjectFileUploaded object{ actor, claude\_file\_id, claude\_project\_id, 6 more }

A file was uploaded to a Claude project.



ClaudeProjectReported object{ actor, claude\_project\_id, id, 4 more }

A Claude project was reported.



ClaudeProjectSharingUpdated object{ actor, audience, claude\_project\_id, 5 more }

A Claude project's sharing settings were updated.



ClaudeProjectViewed object{ actor, claude\_project\_id, id, 5 more }

A Claude project was viewed.



ClaudePubsecIdentityConfigured object{ actor, idp\_saml\_config\_updated, magic\_link\_toggled, 6 more }

SAML IdP configuration updated for a public sector organization.



RbacRoleAssigned object{ actor, principal\_id, principal\_type, 6 more }

Admin assigned an RBAC custom role to a principal.



RbacRoleCreated object{ actor, role\_id, role\_name, 5 more }

Admin created an RBAC custom role.



RbacRoleDeleted object{ actor, role\_id, id, 4 more }

Admin deleted an RBAC custom role.



RbacRolePermissionAdded object{ action, actor, resource\_id, 7 more }

Admin added a permission to an RBAC custom role.

Emitted once per requested permission, including permissions the role
already had, so a retried request still produces a complete audit record.



RbacRolePermissionRemoved object{ action, actor, resource\_id, 7 more }

Admin removed a permission from an RBAC custom role.

Emitted once per requested permission, including permissions the role
already lacked, so a retried request still produces a complete audit
record.



RbacRoleUnassigned object{ actor, principal\_id, principal\_type, 6 more }

Admin unassigned an RBAC custom role from a principal.



RbacRoleUpdated object{ actor, role\_id, id, 4 more }

Admin updated an RBAC custom role.



RoleAssignmentGranted object{ actor, id, created\_at, 8 more }

Role assignment was granted.



RoleAssignmentRevoked object{ actor, id, created\_at, 8 more }

Role assignment was revoked.



SSOLoginFailed object{ actor, id, created\_at, 3 more }

An SSO sign-in attempt failed.



SSOLoginInitiated object{ actor, id, created\_at, 3 more }

A user started an SSO sign-in flow.



SSOLoginSucceeded object{ actor, id, auth\_method, 5 more }

A user successfully signed in with SSO.



SSOSecondFactorMagicLink object{ actor, id, created\_at, 3 more }

SSO second factor magic link was used.



ScimUserCreated object{ actor, user\_id, id, 4 more }

A SCIM user was provisioned.



ScimUserDeleted object{ actor, user\_id, id, 4 more }

A SCIM user was deleted.



ScimUserUpdated object{ actor, user\_id, id, 4 more }

A SCIM user was updated.



ScopedAPIKeyDeleted object{ actor, api\_key\_id, api\_key\_name, 6 more }

A scoped API key was deleted.



ScopedAPIKeyUpdated object{ actor, api\_key\_id, updates, 5 more }

A scoped API key was renamed or its activation state changed.



SeatTierChangesCancelled object{ actor, id, created\_at, 3 more }

Scheduled seat tier downgrades were cancelled.



SeatTiersPurchased object{ actor, id, created\_at, 4 more }

Seat tiers were purchased or upgraded on a subscription.



ServiceCreated object{ actor, service\_name, id, 4 more }

Activity logged when an org service is explicitly created.



ServiceDeleted object{ actor, service\_name, id, 4 more }

Activity logged when an org service is deleted.



ServiceKeyCreated object{ actor, is\_service\_created, key\_name, 8 more }

Activity logged when a new org service key is created.



ServiceKeyRevoked object{ actor, service\_key\_id, service\_name, 5 more }

Activity logged when an org service key is revoked.



SessionRevoked object{ actor, id, created\_at, 3 more }

User revoked a specific session.



SessionShareAccessed object{ actor, id, created\_at, 4 more }

Session share was accessed.



SessionShareCreated object{ actor, id, access\_level, 5 more }

Session share was created.



SessionShareRevoked object{ actor, id, created\_at, 5 more }

Session share was revoked.



ClaudeSkillCreated object{ actor, id, created\_at, 5 more }

Skill was created.



ClaudeSkillDeleted object{ actor, id, created\_at, 7 more }

Skill was deleted.



ClaudeSkillDisabled object{ actor, id, created\_at, 5 more }

User disabled a skill for their account.



ClaudeSkillEnabled object{ actor, id, created\_at, 5 more }

User enabled a skill for their account.



ClaudeSkillReplaced object{ actor, id, created\_at, 5 more }

Skill was replaced.



SlackWorkspaceClaimRevoked object{ actor, slack\_team\_id, id, 5 more }

A Slack workspace or Enterprise Grid organization was disconnected
from the organization for Claude in Slack.



SlackWorkspaceClaimed object{ actor, slack\_team\_id, id, 5 more }

A Slack workspace or Enterprise Grid organization was connected to
the organization for Claude in Slack.



SocialLoginSucceeded object{ actor, provider, id, 6 more }

A user successfully signed in with a social identity provider (Google, Apple, or Microsoft).



StepUpAuthenticationFailed object{ actor, method, reason, 6 more }

An additional identity check failed.



StepUpAuthenticationSucceeded object{ actor, method, id, 5 more }

The user completed an additional identity check to confirm a sensitive action.



StepUpCredentialEnrolled object{ actor, credential\_id, id, 4 more }

A user enrolled a passkey for confirming sensitive actions on their account.



SubscriptionCancellationScheduled object{ actor, id, created\_at, 3 more }

Subscription cancellation was scheduled at end of billing period.



SubscriptionQuantityUpdated object{ actor, added\_seats, new\_quantity, 6 more }

Contracted subscription seat quantity was updated.



SubscriptionRenewed object{ actor, id, billing\_interval, 5 more }

A cancelled subscription was renewed.



SubscriptionResumed object{ actor, id, created\_at, 3 more }

A scheduled subscription cancellation was reversed.



SubscriptionStarted object{ actor, id, billing\_interval, 6 more }

A new subscription was created (Team or Enterprise).



SubscriptionUpgraded object{ actor, id, created\_at, 5 more }

Subscription plan was upgraded (e.g. Team to Enterprise).



TrustedDeviceCredentialRotated object{ actor, trusted\_device\_id, id, 4 more }

The identity-verification credential of a trusted device was rotated to a new key.



TrustedDeviceEnrolled object{ actor, enrollment\_method, platform, 6 more }

A device was enrolled as a trusted device for the user's account. Trusted devices can be used to confirm the user's identity for sensitive actions.



TrustedDeviceRevoked object{ actor, reason, id, 6 more }

A trusted device was removed from the user's account.



TunnelArchived object{ actor, tunnel\_id, id, 4 more }

An MCP tunnel was archived.



TunnelCertificateAdded object{ actor, certificate\_id, tunnel\_id, 6 more }

An inner-TLS CA certificate was added to a tunnel.



TunnelCertificateRevoked object{ actor, certificate\_id, tunnel\_id, 6 more }

An inner-TLS CA certificate was revoked from a tunnel.



TunnelCreated object{ actor, tunnel\_id, id, 4 more }

An MCP tunnel was created.



TunnelTokenMinted object{ actor, token\_id, id, 5 more }

An OAuth bearer token for the tunnel management API was minted.



TunnelTokenRevealed object{ actor, tunnel\_id, tunnel\_token\_id, 5 more }

The Cloudflare connector secret for a tunnel was revealed to the caller.



TunnelTokenRevoked object{ actor, token\_id, id, 5 more }

An OAuth bearer token for the tunnel management API was revoked.



TunnelTokenRotated object{ actor, tunnel\_id, tunnel\_token\_id, 6 more }

The Cloudflare connector secret for a tunnel was rotated.

`tunnel_token_id` is the id of the *newly-issued* token. The previous
token is invalidated by the rotation and its id is not recorded here.



UserConsentRecorded object{ actor, consent\_type, entity\_id, 6 more }

User granted a consent for a specific entity (e.g. consumer health consent for an MCP server).



UserConsentRevoked object{ actor, id, consent\_id, 7 more }

User revoked a previously granted consent for a specific entity.



ClaudeUserRoleUpdated object{ actor, current\_role, previous\_role, 7 more }

A user's role within the organization was changed, or the user was added to or removed from the organization.



ClaudeUserSettingsUpdated object{ actor, updates, id, 4 more }

User updated their personal settings.



VerificationEvidenceSubmitted object{ actor, verification\_id, verification\_type, 5 more }

Verification evidence was submitted for an organization's verification.



VerificationProgramApplicationCreated object{ actor, program\_slug, id, 4 more }

An organization applied to a verification program.



WorkspaceMemberSpendLimitCreated object{ actor, id, account\_id, 7 more }

A per-member or workspace-default Claude Code spend limit was created.



WorkspaceMemberSpendLimitDeleted object{ actor, id, account\_id, 6 more }

A per-member or workspace-default Claude Code spend limit was deleted.



WorkspaceMemberSpendLimitUpdated object{ actor, id, account\_id, 7 more }

A per-member Claude Code spend limit amount was updated.



WorkspaceSpendLimitAlertEmailsUpdated object{ actor, id, alert\_emails, 5 more }

Spend limit alert email recipients were updated for a workspace.



WorkspaceSpendLimitCreated object{ actor, id, created\_at, 6 more }

A workspace-level API spend limit was created.



WorkspaceSpendLimitDeleted object{ actor, id, created\_at, 5 more }

A workspace-level API spend limit was deleted.

first\_id: optional string or null



has\_more: optional boolean

defaultfalse

last\_id: optional string or null



### Query compliance activities

cURL



```shiki
curl https://api.anthropic.com/v1/compliance/activities \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```shiki
{
  "data": [
    {
      "actor": {
        "api_key_id": "api_key_id",
        "ip_address": "ip_address",
        "user_agent": "user_agent",
        "type": "api_actor"
      },
      "decision": "blocked",
      "id": "id",
      "abuse_session_id": "abuse_session_id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "organization_id": "organization_id",
      "organization_uuid": "organization_uuid",
      "type": "abuse_decision_received"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "actor": {
        "api_key_id": "api_key_id",
        "ip_address": "ip_address",
        "user_agent": "user_agent",
        "type": "api_actor"
      },
      "decision": "blocked",
      "id": "id",
      "abuse_session_id": "abuse_session_id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "organization_id": "organization_id",
      "organization_uuid": "organization_uuid",
      "type": "abuse_decision_received"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

---

*Copyright © Anthropic. All rights reserved.*
