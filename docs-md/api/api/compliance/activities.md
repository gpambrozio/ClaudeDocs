# Activities

Copy page





To enable the Compliance API, see [Set up the Compliance API](manage-claude/compliance-api-access.md).

# Activities

##### [Query compliance activities](api/compliance/activities/list.md)

GET/v1/compliance/activities

##### ModelsExpand Collapse



ActivityListResponse = object { actor, decision, id, 5 more }  or object { actor, id, created\_at, 3 more }  or object { actor, admin\_api\_key\_id, scopes, 5 more }  or 381 more

An external anti-abuse service reported a consequential decision about a sign-in or sign-up attempt.

One of the following:



AbuseDecisionReceived object { actor, decision, id, 5 more } 

An external anti-abuse service reported a consequential decision about a sign-in or sign-up attempt.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string



decision: "blocked" or "unspecified"

The decision applied to the session.

One of the following:

"blocked"

"unspecified"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

abuse\_session\_id: optional string

The anti-abuse service's opaque session identifier for correlation.

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "abuse\_decision\_received"



AccountDeleted object { actor, id, created\_at, 3 more } 

User-initiated self-service account deletion.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "account\_deleted"



AdminAPIKeyCreated object { actor, admin\_api\_key\_id, scopes, 5 more } 

An admin API key was created.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

admin\_api\_key\_id: string

Tagged ID of the created admin API key

scopes: array of string

Scopes granted to the key (empty for legacy non-scoped admin keys)

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "admin\_api\_key\_created"



AdminAPIKeyDeleted object { actor, admin\_api\_key\_id, id, 4 more } 

An admin API key was deleted.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

admin\_api\_key\_id: string

Tagged ID of the deleted admin API key

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "admin\_api\_key\_deleted"



AdminAPIKeyUpdated object { actor, admin\_api\_key\_id, updates, 5 more } 

An admin API key was updated (renamed or activated/deactivated).



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

admin\_api\_key\_id: string

Tagged ID of the updated admin API key



updates: array of object { current\_value, previous\_value, type } 

current\_value: string

previous\_value: string



type: "name" or "status"

One of the following:

"name"

"status"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "admin\_api\_key\_updated"



AdminConnectorRequestResolved object { actor, decision, mcp\_server\_id, 6 more } 

Admin approved or dismissed pending member requests to enable an MCP connector.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string



decision: "approved" or "dismissed" or "unspecified"

One of the following:

"approved"

"dismissed"

"unspecified"

mcp\_server\_id: string

resolved\_count: number

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "admin\_connector\_request\_resolved"



AdminRequestCreated object { actor, request\_type, id, 4 more } 

Admin request created by an org member (seat upgrade, limit increase, join org, end-user invite).



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

request\_type: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "admin\_request\_created"



AgeVerified object { actor, id, created\_at, 3 more } 

User age was verified.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "age\_verified"



AnonymousMobileLoginAttempted object { actor, id, created\_at, 3 more } 

Anonymous mobile login was attempted.



actor: object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "anonymous\_mobile\_login\_attempted"



APIKeyCreated object { actor, api\_key\_id, scopes, 6 more } 

Activity logged when a new API key is created.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

api\_key\_id: string

The tagged ID of the created API key

scopes: array of string

The scopes for this API key

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

restricted\_to\_organization: optional boolean

Whether the key was restricted to the creating organization, rather than granted access across the whole parent organization

type: optional "api\_key\_created"



ClaudeArtifactAccessFailed object { actor, id, claude\_artifact\_id, 6 more } 

An attempt to access an artifact failed.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

claude\_artifact\_id: optional string

The artifact's identifier, when known.

claude\_artifact\_version\_id: optional string

The version of the artifact the user attempted to access, when known.

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

reason: optional string

The reason access was denied, when recorded.

type: optional "claude\_artifact\_access\_failed"



ClaudeArtifactCreated object { actor, claude\_artifact\_id, id, 4 more } 

An artifact was created.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_artifact\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_artifact\_created"



ClaudePublishedArtifactDeleted object { actor, claude\_published\_artifact\_id, id, 4 more } 

A published artifact was unpublished/deleted by its creator.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

claude\_published\_artifact\_id: string

The published artifact's identifier.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_published\_artifact\_deleted"



ClaudeArtifactPublished object { actor, artifact\_type, claude\_published\_artifact\_id, 9 more } 

An artifact was published and made publicly accessible.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

artifact\_type: string

Artifact type (code, html, react, etc.)

claude\_published\_artifact\_id: string

The published artifact's identifier.

title: string

Title of the published artifact

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

claude\_artifact\_version\_id: optional string

The version identifier recorded as live by this publish.

created\_at: optional string

When this activity occurred.

description: optional string

Optional gallery-card description supplied at publish time. Same provenance as title (caller-authored, reader-visible).

is\_redeploy: optional boolean

True when the publish updated an existing artifact; false when the publish created the artifact.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_artifact\_published"



ClaudeArtifactSharingUpdated object { actor, audience, claude\_artifact\_id, 10 more } 

An artifact's sharing settings were updated.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string



audience: array of object { type }  or object { type } 

Sharing audience for the project. If empty, this it's only visible to the creating user.

One of the following:



ArtifactSharingAudienceOrganization object { type } 

Sharing audience: visible to the owning organization.

type: optional "organization"



ArtifactSharingAudienceUsers object { type } 

Sharing audience: visible to an explicit allowlist of users.

type: optional "users"

claude\_artifact\_id: string

The artifact's identifier.

claude\_artifact\_version\_id: string

The artifact version's identifier.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

new\_mode: optional string

The sharing mode after the change: `owner`, `users`, or `org`.

new\_user\_count: optional number

The number of accounts on the explicit allowlist after the change. Only meaningful when `new_mode` is `users`.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

previous\_mode: optional string

The sharing mode before the change: `owner`, `users`, or `org`.

previous\_user\_count: optional number

The number of accounts on the explicit allowlist before the change. Only meaningful when `previous_mode` is `users`.

type: optional "claude\_artifact\_sharing\_updated"



ClaudeArtifactViewed object { actor, claude\_artifact\_id, id, 5 more } 

An artifact was viewed.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

claude\_artifact\_id: string

The artifact's identifier.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

claude\_artifact\_version\_id: optional string

The version of the artifact the user was served, when known.

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_artifact\_viewed"



AuditLogExportAccessed object { actor, id, created\_at, 3 more } 

Audit log export file was accessed/downloaded via signed URL.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "audit\_log\_export\_accessed"



AuditLogExportStarted object { actor, id, created\_at, 5 more } 

Audit log export was initiated.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

from\_date: optional string

Start date of the export range

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

to\_date: optional string

End date of the export range

type: optional "audit\_log\_export\_started"



BillingEmailsUpdated object { actor, id, cc\_email\_count, 6 more } 

The organization's billing email recipients were updated.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

cc\_email\_count: optional number

Number of 'cc' email recipients.

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

primary\_email\_set: optional boolean

Whether a primary billing email is configured.

to\_email\_count: optional number

Number of 'to' email recipients.

type: optional "billing\_emails\_updated"



CcrAgentCreated object { actor, agent\_id, default\_source\_urls\_truncated, 11 more } 

A Claude Code agent was created.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

agent\_id: string

The agent that was created, e.g. "cagt\_01HX...".

default\_source\_urls\_truncated: boolean

Whether default\_source\_urls was capped and omits some of the granted repositories.

display\_name: string

The agent's display name at creation time.

omitted\_source\_url\_count: number

Number of default repository entries that could not be safely rendered as a credential-free URL and were omitted from default\_source\_urls. A non-zero value with an empty list means repositories were granted but could not be displayed — not that all repositories were removed.

slug: string

The agent's URL-safe identifier, unique within the organization.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

default\_source\_urls: optional array of string

The repository URLs the agent works on by default, reduced to scheme, host, and path — credentials and query parameters are never included. Empty with a zero omitted\_source\_url\_count means the agent was created without any default repositories; empty with a non-zero count means repositories were granted but could not be safely rendered. At most 100 entries are included; default\_source\_urls\_truncated indicates when more were granted.

guest\_policy: optional string

Whether the agent responds in Slack channels that include guest users: "allow" or "restrict". Omitted when the agent inherits the default policy.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

slack\_alias: optional string

The Slack trigger word that routes mentions to this agent. An empty value means the agent responds to bare "@Claude" mentions. Omitted when the agent is not addressable from Slack.

type: optional "ccr\_agent\_created"



CcrAgentDeleted object { actor, agent\_id, cascaded\_agent\_ids\_truncated, 7 more } 

A Claude Code agent was deleted.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

agent\_id: string

The agent that was deleted, e.g. "cagt\_01HX...".

cascaded\_agent\_ids\_truncated: boolean

True when more agents were deleted in this cascade than are individually recorded. On a cascade parent event (cascaded\_from\_agent\_id unset), cascaded\_agent\_ids is capped at 100. On a cascade child event (cascaded\_from\_agent\_id set, emitted when the parent deletion failed after committing child deletions), one event is emitted per deleted child up to 100, and this field indicates additional children were deleted in the same cascade.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

cascaded\_agent\_ids: optional array of string

Agents assigned to individual Slack channels that were also deleted because agent\_id was the agent assigned to their entire Slack workspace. Empty when no such agents were deleted, and always empty on a cascade child event (cascaded\_from\_agent\_id set) — the child's siblings are recorded as their own events, not listed here. Capped at 100 entries; cascaded\_agent\_ids\_truncated is set when the actual count exceeded the cap.

cascaded\_from\_agent\_id: optional string

When set, the Slack workspace's dedicated agent whose deletion attempt caused this agent to be deleted. The parent's own deletion may have failed after the cascade committed — check for a separate event with agent\_id = cascaded\_from\_agent\_id to confirm. Unset on a direct deletion.

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "ccr\_agent\_deleted"



CcrAgentProxyCredentialCreated object { actor, credential\_id, credential\_type, 9 more } 

A Claude Code agent proxy credential was created. Credentials hold the secrets the agent proxy injects into requests Claude Code sessions send to approved external services; each credential belongs to an agent proxy profile. Audit events carry only credential names and settings, never the secret material itself.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

credential\_id: string

The credential that was created, e.g. "apc\_01HX...".

credential\_type: string

The kind of credential, e.g. "bearer", "basic", "github\_app", "mtls".

display\_name: string

The credential's display name.

host\_constraint\_truncated: boolean

Whether host\_constraint was capped and omits some of the configured host name patterns.

profile\_id: string

The agent proxy profile the credential belongs to, e.g. "capp\_01HX...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

host\_constraint: optional array of string

The host name patterns the credential may be sent to, e.g. "api.example.com" or "\*.example.com". At most 100 entries are included; host\_constraint\_truncated indicates when the configured set is larger.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "ccr\_agent\_proxy\_credential\_created"



CcrAgentProxyCredentialDeleted object { actor, credential\_id, profile\_id, 5 more } 

A Claude Code agent proxy credential was deleted. Its secret material was removed and can no longer be sent to any host.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

credential\_id: string

The credential that was deleted, e.g. "apc\_01HX...".

profile\_id: string

The agent proxy profile the credential belonged to, e.g. "capp\_01HX...". Carried so the deletion can be correlated with the profile's other audit events after the credential row no longer exists.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "ccr\_agent\_proxy\_credential\_deleted"



CcrAgentProxyCredentialRotated object { actor, credential\_id, credential\_type, 10 more } 

A Claude Code agent proxy credential's secret material was replaced. The replacement keeps the same name, profile, and allowed hosts under a new credential identifier, and everything that referenced the old credential now uses the replacement.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

credential\_id: string

The replacement credential, e.g. "apc\_01HX...".

credential\_type: string

The kind of credential, e.g. "bearer", "basic", "github\_app", "mtls".

destinations\_repointed: number

The number of agent proxy destinations that referenced the old credential and now reference the replacement.

display\_name: string

The credential's display name.

previous\_credential\_id: string

The credential that was replaced, e.g. "apc\_01HX...".

profile\_id: string

The agent proxy profile the credential belongs to, e.g. "capp\_01HX...".

rules\_repointed: number

The number of agent proxy rules that referenced the old credential and now reference the replacement.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "ccr\_agent\_proxy\_credential\_rotated"



CcrAgentProxyCredentialUpdated object { actor, credential\_id, display\_name, 9 more } 

A Claude Code agent proxy credential's settings were updated. Only the display name and the allowed host patterns can be updated; the secret material can only be replaced through a rotation.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

credential\_id: string

The credential that was updated, e.g. "apc\_01HX...".

display\_name: string

The credential's display name after the update.

host\_constraint\_truncated: boolean

Whether host\_constraint was capped and omits some of the configured host name patterns.

profile\_id: string

The agent proxy profile the credential belongs to, e.g. "capp\_01HX...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

host\_constraint: optional array of string

The host name patterns the credential may be sent to after the update, e.g. "api.example.com" or "\*.example.com". Populated only when the update changed them. At most 100 entries are included; host\_constraint\_truncated indicates when the configured set is larger.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "ccr\_agent\_proxy\_credential\_updated"

updated\_fields: optional array of string

Names of the settings included in the update: "display\_name", "host\_constraint".



CcrAgentProxyNetworkEventsListed object { actor, failed, id, 5 more } 

A Claude Code network activity export was accessed for the given hour.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

failed: boolean

True when the export request did not complete successfully.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

hour: optional string

The UTC hour that was exported.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "ccr\_agent\_proxy\_network\_events\_listed"



CcrAgentProxyProfileBound object { actor, profile\_id, scope\_id, 6 more } 

A Claude Code agent proxy profile was bound to a scope, applying its policy to Claude Code sessions in that scope.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

profile\_id: string

The profile that was bound, e.g. "capp\_01HX...".

scope\_id: string

The identifier of the scope the profile was bound to.

scope\_kind: string

The kind of scope the profile was bound to: "organization", "environment", "account", or "agent".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "ccr\_agent\_proxy\_profile\_bound"



CcrAgentProxyProfileCreated object { actor, display\_name, profile\_id, 7 more } 

A Claude Code agent proxy profile was created. Agent proxy profiles are named, reusable bundles of access policy that administrators bind to parts of the organization.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

display\_name: string

The profile's display name at creation time.

profile\_id: string

The profile that was created, e.g. "capp\_01HX...".

slug: string

The profile's URL-safe identifier, unique within the organization.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.



github\_access: optional array of object { access\_mode, github\_installation\_id, repo\_count, 4 more } 

The GitHub repository access the profile grants, one entry per GitHub App installation. Empty when the profile grants no GitHub access.

access\_mode: string

How repository access is granted: "none" (no access), "list" (exactly the repositories in repos), or "all" — a legacy value for policies created before per-repository grants were required; it can no longer be assigned.

github\_installation\_id: number

The GitHub App installation the access applies to.

repo\_count: number

The total number of repositories granted, including any omitted from repos.

repos\_truncated: boolean

Whether repos was capped and omits some of the granted repositories.

ghe\_configuration\_id: optional number

The GitHub host configuration this installation belongs to. Distinguishes installations with the same numeric installation ID across github.com and GitHub Enterprise Server hosts. Absent for github.com installations.

repo\_ids: optional array of number

The numeric GitHub repository IDs the profile grants access to, in the same order as repos (and subject to the same 100-entry cap). These IDs are the authoritative identity of the granted repositories — access is enforced against them, not against the display names in repos.

repos: optional array of string

Repository names (owner/name) the profile grants access to, populated when access\_mode is "list". Names are display-only labels resolved when the event was recorded and may lag a repository rename; the entries in repo\_ids are the authoritative identity of the granted repositories. A repository whose name is unavailable is listed as its numeric GitHub repository ID instead. At most 100 entries are included; repos\_truncated indicates when the granted set is larger.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "ccr\_agent\_proxy\_profile\_created"



CcrAgentProxyProfileDeleted object { actor, deleted\_credential\_count, deleted\_credentials\_unknown, 6 more } 

A Claude Code agent proxy profile was deleted, removing its policy from everything it was bound to.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

deleted\_credential\_count: number

Number of credentials deleted together with the profile — deleting a profile also deletes the credentials attached to it. Each deleted credential additionally emits its own ccr\_agent\_proxy\_credential\_deleted activity, at most 100 per profile deletion. Best-effort: when deleted\_credentials\_unknown is true the count could not be determined and 0 here does not mean the profile had no credentials.

deleted\_credentials\_unknown: boolean

Whether the number of credentials deleted with the profile could not be determined. When true, deleted\_credential\_count is 0 and no per-credential deletion activities were emitted, even though the deletion may have destroyed credentials.

profile\_id: string

The profile that was deleted, e.g. "capp\_01HX...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "ccr\_agent\_proxy\_profile\_deleted"



CcrAgentProxyProfileUnbound object { actor, profile\_id, scope\_id, 6 more } 

A Claude Code agent proxy profile was unbound from a scope, removing its policy from Claude Code sessions in that scope.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

profile\_id: string

The profile that was unbound, e.g. "capp\_01HX...".

scope\_id: string

The identifier of the scope the profile was unbound from.

scope\_kind: string

The kind of scope the profile was unbound from: "organization", "environment", "account", or "agent".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "ccr\_agent\_proxy\_profile\_unbound"



CcrAgentProxyProfileUpdated object { actor, profile\_id, id, 6 more } 

A Claude Code agent proxy profile's configuration was updated.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

profile\_id: string

The profile that was updated, e.g. "capp\_01HX...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.



github\_access\_changes: optional array of object { access\_mode, github\_installation\_id, repo\_count, 7 more } 

How the profile's GitHub repository access changed, one entry per GitHub App installation whose access changed. Empty when the update did not change GitHub access.

access\_mode: string

How repository access is granted after the change: "none" (no access), "list" (access is restricted to an explicit repository list — repos\_added/repos\_removed carry this change's delta and repo\_count the post-change total), or "all" — a legacy value for policies created before per-repository grants were required; it can no longer be assigned.

github\_installation\_id: number

The GitHub App installation the change applies to.

repo\_count: number

The total number of repositories granted after the change.

repos\_truncated: boolean

Whether repos\_added or repos\_removed was capped and omits some of the changed repositories.

ghe\_configuration\_id: optional number

The GitHub host configuration this installation belongs to. Distinguishes installations with the same numeric installation ID across github.com and GitHub Enterprise Server hosts. Absent for github.com installations.

previous\_access\_mode: optional string

How repository access was granted before the change. Present only when the access mode changed.

repo\_ids\_added: optional array of number

The numeric GitHub repository IDs added to the granted set, in the same order as repos\_added (and subject to the same 100-entry cap). These IDs are the authoritative identity of the added repositories — access is enforced against them, not against the display names in repos\_added.

repo\_ids\_removed: optional array of number

The numeric GitHub repository IDs removed from the granted set, in the same order as repos\_removed (and subject to the same 100-entry cap). These IDs are the authoritative identity of the removed repositories.

repos\_added: optional array of string

Repository names (owner/name) added to the granted set. Names are display-only labels resolved when the event was recorded and may lag a repository rename; the entries in repo\_ids\_added are the authoritative identity of the added repositories. A repository whose name is unavailable is listed as its numeric GitHub repository ID instead. At most 100 entries are included; repos\_truncated indicates when more were added. Empty when the change involves "all" access, which grants every repository regardless of any explicit list.

repos\_removed: optional array of string

Repository names (owner/name) removed from the granted set. Same rendering, cap, and "all" handling as repos\_added; repo\_ids\_removed carries the authoritative identity of the removed repositories.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "ccr\_agent\_proxy\_profile\_updated"

updated\_fields: optional array of string

Names of the configuration fields included in the update, e.g. "display\_name", "github\_installation\_permissions".



CcrAgentSlackAccessScopeCreated object { actor, agent\_id, can\_write, 7 more } 

A Claude Code agent was granted access to read or write in an additional Slack channel beyond the one it is assigned to.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

agent\_id: string

The agent that was granted access, e.g. "cagt\_01HX...".

can\_write: boolean

Whether the grant includes permission to post messages in the channel, in addition to reading it.

slack\_channel\_id: string

The Slack channel the agent was granted access to, e.g. "C01ABC...". Empty when the grant covers the entire workspace.

slack\_team\_id: string

The Slack workspace containing the channel, e.g. "T01ABC...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "ccr\_agent\_slack\_access\_scope\_created"



CcrAgentSlackAccessScopeDeleted object { actor, agent\_id, slack\_channel\_id, 6 more } 

A Claude Code agent's access to an additional Slack channel was revoked.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

agent\_id: string

The agent whose access was revoked, e.g. "cagt\_01HX...".

slack\_channel\_id: string

The Slack channel the agent's access was revoked from, e.g. "C01ABC...". Empty when the revoked grant covered the entire workspace.

slack\_team\_id: string

The Slack workspace containing the channel, e.g. "T01ABC...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "ccr\_agent\_slack\_access\_scope\_deleted"



CcrAgentSlackBindingCreated object { actor, agent\_id, slack\_channel\_id, 6 more } 

A Claude Code agent was assigned to a Slack channel or workspace as its dedicated agent.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

agent\_id: string

The agent the binding was created for, e.g. "cagt\_01HX...".

slack\_channel\_id: string

The Slack channel the agent was assigned to, e.g. "C01ABC...". Empty when the agent was assigned to the entire workspace.

slack\_team\_id: string

The Slack workspace the agent was assigned to, e.g. "T01ABC...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "ccr\_agent\_slack\_binding\_created"



CcrAgentSlackBindingDeleted object { actor, agent\_id, slack\_channel\_id, 6 more } 

A Claude Code agent's assignment to a Slack channel or workspace was removed.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

agent\_id: string

The agent the binding was removed from, e.g. "cagt\_01HX...".

slack\_channel\_id: string

The Slack channel the agent was unassigned from, e.g. "C01ABC...". Empty when the assignment covered the entire workspace.

slack\_team\_id: string

The Slack workspace the agent was unassigned from, e.g. "T01ABC...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "ccr\_agent\_slack\_binding\_deleted"



CcrAgentUpdated object { actor, agent\_id, default\_source\_urls\_truncated, 10 more } 

A Claude Code agent's configuration was updated. Also emitted with updated\_fields ["is\_virtual"] alone when an auto-provisioned agent is promoted to a configured one, whether by an update request targeting it or by binding an agent proxy profile to it.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

agent\_id: string

The agent that was updated, e.g. "cagt\_01HX...".

default\_source\_urls\_truncated: boolean

Whether default\_source\_urls was capped and omits some of the granted repositories.

omitted\_source\_url\_count: number

Number of default repository entries that could not be safely rendered as a credential-free URL and were omitted from default\_source\_urls. A non-zero value with an empty list means repositories were granted but could not be displayed — not that all repositories were removed.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

default\_source\_urls: optional array of string

The agent's default repository URLs after the update, reduced to scheme, host, and path — credentials and query parameters are never included. Populated only when the update changed them — "default\_source\_urls" appears in updated\_fields. Empty while listed in updated\_fields AND omitted\_source\_url\_count is 0 means all default repositories were removed. At most 100 entries are included; default\_source\_urls\_truncated indicates when more were granted.

guest\_policy: optional string

The agent's guest-user response policy after the update: "allow", "restrict", or "default" when the update removed the agent-specific policy so the agent inherits the surrounding default. Present only when the update changed it.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

slack\_alias: optional string

The agent's Slack trigger word after the update. Present only when the update changed it. An empty value means the agent responds to bare "@Claude" mentions.

type: optional "ccr\_agent\_updated"

updated\_fields: optional array of string

Names of the configuration fields included in the update, e.g. "display\_name", "system\_prompt\_addendum", "guest\_policy". Includes "is\_virtual" when this update was the first administrator action on an auto-provisioned agent — a durable state change even when no other field was supplied.



ClaudeChatSettingsUpdated object { actor, claude\_chat\_id, id, 5 more } 

User updated the settings for a conversation.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_chat\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

claude\_project\_id: optional string

Project ID this chat belongs to, if any

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_chat\_settings\_updated"



ClaudeChatSnapshotCreated object { actor, claude\_chat\_id, claude\_chat\_snapshot\_id, 5 more } 

User created/shared a chat snapshot.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

claude\_chat\_id: string

claude\_chat\_snapshot\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_chat\_snapshot\_created"



ClaudeChatSnapshotDeleted object { actor, claude\_chat\_snapshot\_id, id, 5 more } 

User deleted/unshared a chat snapshot.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

claude\_chat\_snapshot\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

claude\_chat\_id: optional string

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_chat\_snapshot\_deleted"



ClaudeChatSnapshotViewed object { actor, claude\_chat\_snapshot\_id, id, 5 more } 

User viewed a chat snapshot (authenticated or public/unauthenticated).



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

claude\_chat\_snapshot\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

claude\_chat\_id: optional string

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_chat\_snapshot\_viewed"



ClaudeChatAccessFailed object { actor, claude\_chat\_id, id, 4 more } 

A user was denied access to a Claude.ai chat conversation.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

claude\_chat\_id: string

The chat conversation the user was denied access to, e.g. "claude\_chat\_01Ab...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_chat\_access\_failed"



ClaudeChatCreated object { actor, claude\_chat\_id, id, 5 more } 

User created a chat.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

claude\_chat\_id: string

Tagged ID of the created conversation, e.g. "claude\_chat\_01HX...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

claude\_project\_id: optional string

Tagged ID of the project the chat was created in, if any, e.g. "claude\_proj\_01HX...".

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_chat\_created"



ClaudeChatDeleted object { actor, claude\_chat\_id, id, 5 more } 

A user deleted a Claude.ai chat conversation.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

claude\_chat\_id: string

The chat conversation that was deleted, e.g. "claude\_chat\_01HX...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

claude\_project\_id: optional string

The project the chat belonged to, if any, e.g. "claude\_proj\_01HX...".

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_chat\_deleted"



ClaudeChatDeletionFailed object { actor, claude\_chat\_id, id, 4 more } 

A request to delete a Claude.ai chat conversation failed.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

claude\_chat\_id: string

The chat conversation the user attempted to delete, e.g. "claude\_chat\_01HX...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_chat\_deletion\_failed"



ClaudeChatUpdated object { actor, claude\_chat\_id, id, 5 more } 

User updated the chat metadata (e.g name, model).



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

claude\_chat\_id: string

Tagged ID of the updated conversation, e.g. "claude\_chat\_01HX...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

claude\_project\_id: optional string

Tagged ID of the project the chat belongs to, if any, e.g. "claude\_proj\_01HX...".

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_chat\_updated"



ClaudeChatViewed object { actor, claude\_chat\_id, id, 5 more } 

A user viewed a Claude.ai chat conversation.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

claude\_chat\_id: string

The chat conversation that was viewed, e.g. "claude\_chat\_01Ab...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

claude\_project\_id: optional string

The project the chat belongs to, if any, e.g. "claude\_proj\_01Ab...".

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_chat\_viewed"



ClaudeCodeReviewConfigUpdated object { actor, enabled, id, 13 more } 

Claude Code Review configuration was enabled/disabled for an org.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

enabled: boolean

Whether code review is now enabled

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

environment\_id: optional string

Environment used for code review

model: optional string

Model configured for code review

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

per\_review\_limit\_usd: optional string

Per-review spend limit in USD

previous\_enabled: optional boolean

Whether code review was enabled before the change. Absent when no configuration existed before this update.

previous\_environment\_id: optional string

Environment used for code review before the change. Absent when no configuration existed before this update or no environment was set.

previous\_model: optional string

Model configured for code review before the change. Absent when no configuration existed before this update or no model was set.

previous\_per\_review\_limit\_usd: optional string

Per-review spend limit in USD before the change. Absent when no configuration existed before this update or no limit was set.

previous\_show\_tips: optional boolean

Whether tip-style pull-request comments were enabled before the change. Absent when no configuration existed before this update.

show\_tips: optional boolean

Whether tip-style pull-request comments are now enabled

type: optional "claude\_code\_review\_config\_updated"



ClaudeCodeReviewRepositoryAdded object { actor, config\_id, repo\_name, 7 more } 

A repository was added to org-level Claude Code Review configuration.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

config\_id: string

ID of the repository configuration

repo\_name: string

Repository name

repo\_owner: string

Repository owner (GitHub org/user)

trigger\_mode: string

When code review is triggered

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_code\_review\_repository\_added"



ClaudeCodeReviewRepositoryRemoved object { actor, config\_id, repo\_name, 6 more } 

A repository was removed from org-level Claude Code Review configuration.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

config\_id: string

ID of the deleted repository configuration

repo\_name: string

Repository name at deletion time

repo\_owner: string

Repository owner at deletion time

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_code\_review\_repository\_removed"



ClaudeCodeReviewRepositoryUpdated object { actor, config\_id, repo\_name, 8 more } 

A Claude Code Review repository configuration was updated.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

config\_id: string

ID of the repository configuration

repo\_name: string

Repository name

repo\_owner: string

Repository owner

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

status: optional string

Updated status (ACTIVE/INACTIVE)

trigger\_mode: optional string

Updated trigger mode

type: optional "claude\_code\_review\_repository\_updated"



ClaudeCodeSecurityCenterConfigUpdated object { actor, enabled, id, 5 more } 

Claude Code Security Center scanning was enabled/disabled for an org.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

enabled: boolean

Whether Security Center is now enabled

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

environment\_id: optional string

Environment used for security scanning

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_code\_security\_center\_config\_updated"



ClaudeCodeSecurityScanCancelled object { actor, scan\_project\_id, scans\_cancelled, 5 more } 

In-flight Claude Code Security scans were cancelled for a project.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

scan\_project\_id: string

Tagged ID of the scan project

scans\_cancelled: number

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_code\_security\_scan\_cancelled"



ClaudeCodeSecurityScanCreated object { actor, scan\_id, scan\_project\_id, 5 more } 

A Claude Code Security scan was started.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

scan\_id: string

Tagged ID of the created scan

scan\_project\_id: string

Tagged ID of the scan project the scan belongs to

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_code\_security\_scan\_created"



ClaudeCodeSecurityScanProjectUpdated object { action, actor, scan\_project\_id, 5 more } 

A Claude Code Security scan project was archived or unarchived.



action: "archived" or "unarchived" or "unspecified"

The state change applied to the scan project.

One of the following:

"archived"

"unarchived"

"unspecified"



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

scan\_project\_id: string

Tagged ID of the scan project

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_code\_security\_scan\_project\_updated"



ClaudeCodeSecurityScanProjectVisibilityUpdated object { action, actor, scan\_project\_id, 6 more } 

A Claude Code Security scan project was shared with the organization or made private.



action: "shared" or "unshared" or "unspecified"

Whether the project was shared with the organization or made private

One of the following:

"shared"

"unshared"

"unspecified"



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

scan\_project\_id: string

Tagged ID of the scan project

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

access\_level: optional string

Access level granted to organization members (read\_only or full); only set when shared

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_code\_security\_scan\_project\_visibility\_updated"



ClaudeCodeSecurityScanRunUpdated object { action, actor, scan\_id, 5 more } 

A single Claude Code Security scan run was archived or unarchived.



action: "archived" or "unarchived" or "unspecified"

The state change applied to the scan run

One of the following:

"archived"

"unarchived"

"unspecified"



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

scan\_id: string

Tagged ID of the scan the request named — any scan in the archived run, not necessarily its canonical (run\_index=0) scan

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_code\_security\_scan\_run\_updated"



ClaudeCodeSecurityScanScheduleDeleted object { actor, scan\_project\_id, id, 4 more } 

A recurring scan schedule was deleted for a Claude Code Security project.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

scan\_project\_id: string

Tagged ID of the scan project

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_code\_security\_scan\_schedule\_deleted"



ClaudeCodeSecurityScanScheduleUpdated object { actor, cadence, scan\_project\_id, 5 more } 

A recurring scan schedule was set or replaced for a Claude Code Security project.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

cadence: string

scan\_project\_id: string

Tagged ID of the scan project

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_code\_security\_scan\_schedule\_updated"



ClaudeCodeSecurityVulnerabilityFixSessionCreated object { actor, scan\_id, session\_id, 5 more } 

A Claude Code remediation session was created for a Claude Code Security vulnerability finding.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

scan\_id: string

Tagged ID of the scan the finding belongs to

session\_id: string

ID of the created remediation session

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_code\_security\_vulnerability\_fix\_session\_created"



ClaudeCodeSecurityVulnerabilityUpdated object { action, actor, scan\_id, 6 more } 

A Claude Code Security vulnerability finding was dismissed, restored, marked fixed, or reopened.



action: "dismissed" or "fixed" or "restored" or 2 more

The state change applied to the finding

One of the following:

"dismissed"

"fixed"

"restored"

"unfixed"

"unspecified"



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

scan\_id: string

Tagged ID of the scan the finding belongs to

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

dismissal\_reason: optional string

The categorized dismissal reason (only set when the finding was dismissed)

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_code\_security\_vulnerability\_updated"



ClaudeCodeSecurityWebhookCreated object { actor, url, webhook\_id, 6 more } 

A Claude Code Security outbound webhook was created.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

url: string

webhook\_id: string

Tagged ID of the webhook

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

scan\_project\_id: optional string

Tagged ID of the scan project (null for organization-wide webhooks)

type: optional "claude\_code\_security\_webhook\_created"



ClaudeCodeSecurityWebhookDeleted object { actor, webhook\_id, id, 5 more } 

A Claude Code Security outbound webhook was deleted.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

webhook\_id: string

Tagged ID of the webhook

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

scan\_project\_id: optional string

Tagged ID of the scan project (null for organization-wide webhooks)

type: optional "claude\_code\_security\_webhook\_deleted"



ClaudeCodeSecurityWebhookSecretUpdated object { actor, webhook\_id, id, 5 more } 

The HMAC signing secret for a Claude Code Security webhook was rotated.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

webhook\_id: string

Tagged ID of the webhook

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

scan\_project\_id: optional string

Tagged ID of the scan project (null for organization-wide webhooks)

type: optional "claude\_code\_security\_webhook\_secret\_updated"



ClaudeCodeSecurityWebhookUpdated object { actor, webhook\_id, id, 5 more } 

A Claude Code Security outbound webhook was updated.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

webhook\_id: string

Tagged ID of the webhook

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

scan\_project\_id: optional string

Tagged ID of the scan project (null for organization-wide webhooks)

type: optional "claude\_code\_security\_webhook\_updated"



ClaudeCodeTeamMemoryACLUpdated object { action, actor, group\_id, 7 more } 

An RBAC group was added to or removed from the Claude Code team-memory ACL.



action: "removed" or "set" or "unspecified"

Whether the group was set (added/updated) or removed

One of the following:

"removed"

"set"

"unspecified"



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

group\_id: string

Tagged ID of the RBAC group

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

access\_level: optional string

Access level granted (when action=set)

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

previous\_access\_level: optional string

Access level the group had before this change; absent when the group was not previously in the access list. For removals this is the access level that was removed.

type: optional "claude\_code\_team\_memory\_acl\_updated"



ClaudeCodeTeamMemoryUpdated object { actor, deleted\_all, id, 12 more } 

Claude Code team memory shared with the organization was updated.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

deleted\_all: boolean

True when the entire team memory store for this scope was deleted in one request.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

keys\_deleted: optional array of string

Withdrawn — never populated. See `keys_deleted_count`.

keys\_deleted\_count: optional number

Number of team memory entries removed.

keys\_written: optional array of string

Withdrawn — never populated. See `keys_written_count`.

keys\_written\_count: optional number

Number of team memory entries created or updated.

new\_checksum: optional string

Checksum of the team memory after this change.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

previous\_checksum: optional string

Checksum of the team memory before this change; null when it did not exist.

repo: optional string

Withdrawn — never populated.

type: optional "claude\_code\_team\_memory\_updated"

version: optional number

Version number of the team memory store after this change.



ClaudeCodeTeamOnboardingGuideUpdated object { action, actor, guide\_short\_code, 9 more } 

A Claude Code team onboarding guide was created, updated, or deleted.



action: "created" or "deleted" or "unspecified" or "updated"

The state change applied to the onboarding guide.

One of the following:

"created"

"deleted"

"unspecified"

"updated"



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

guide\_short\_code: string

Short code identifying the onboarding guide — the public URL handle shown in the share link.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

guide\_id: optional string

Tagged ID of the onboarding guide.

guide\_name: optional string

Withdrawn — never populated.

new\_checksum: optional string

Checksum of the guide content after this change; null when the guide was deleted.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

previous\_checksum: optional string

Checksum of the guide content before this change; null when the guide did not exist.

type: optional "claude\_code\_team\_onboarding\_guide\_updated"



ClaudeCodeUserMarketplacesUpdated object { actor, deleted\_all, id, 10 more } 

A user's Claude Code plugin marketplace selections were updated on Anthropic servers.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

deleted\_all: boolean

True when all of the user's marketplace selections were removed in one request.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

keys\_deleted: optional array of string

Withdrawn — never populated. See `keys_deleted_count`.

keys\_deleted\_count: optional number

Number of marketplace selections removed.

keys\_written: optional array of string

Withdrawn — never populated. See `keys_written_count`.

keys\_written\_count: optional number

Number of marketplace selections added or whose source changed.

new\_value: optional string

Withdrawn — never populated.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

previous\_value: optional string

Withdrawn — never populated.

type: optional "claude\_code\_user\_marketplaces\_updated"



ClaudeCodeUserMemoryUpdated object { actor, deleted\_all, id, 11 more } 

A user's synced private Claude Code memory was updated or deleted on Anthropic servers.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

deleted\_all: boolean

True when the user's entire synced memory for this scope was deleted in one request.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

keys\_deleted: optional array of string

Withdrawn — never populated. See `keys_deleted_count`.

keys\_deleted\_count: optional number

Number of memory file paths removed.

keys\_written: optional array of string

Withdrawn — never populated. See `keys_written_count`.

keys\_written\_count: optional number

Number of memory file paths created or updated.

new\_checksum: optional string

Checksum of the user's synced memory after this change.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

previous\_checksum: optional string

Checksum of the user's synced memory before this change; null when the store did not exist.

repo: optional string

Withdrawn — never populated.

type: optional "claude\_code\_user\_memory\_updated"



ClaudeCodeUserPluginsUpdated object { actor, deleted\_all, id, 10 more } 

A user's Claude Code plugin selections — which plugins are installed and enabled — were updated on Anthropic servers.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

deleted\_all: boolean

True when all of the user's plugin selections were removed in one request.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

keys\_deleted: optional array of string

Withdrawn — never populated. See `keys_deleted_count`.

keys\_deleted\_count: optional number

Number of plugin selections removed.

keys\_written: optional array of string

Withdrawn — never populated. See `keys_written_count`.

keys\_written\_count: optional number

Number of plugin selections added or whose enabled state changed.

new\_value: optional string

The targeted plugin's new enabled state, when a single plugin's state changed.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

previous\_value: optional string

The targeted plugin's previous enabled state, when a single plugin's state changed; null when the plugin did not previously exist or multiple plugins changed.

type: optional "claude\_code\_user\_plugins\_updated"



ClaudeCodeUserSettingsUpdated object { actor, deleted\_all, id, 10 more } 

A user's synced Claude Code settings were updated or deleted on Anthropic servers.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

deleted\_all: boolean

True when the user's entire synced settings store was deleted in one request.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

keys\_deleted: optional array of string

Withdrawn — never populated. See `keys_deleted_count`.

keys\_deleted\_count: optional number

Number of settings entries removed.

keys\_written: optional array of string

Withdrawn — never populated. See `keys_written_count`.

keys\_written\_count: optional number

Number of settings entries created or updated.

new\_checksum: optional string

Checksum of the user's synced settings after this change.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

previous\_checksum: optional string

Checksum of the user's synced settings before this change; null when the store did not exist.

type: optional "claude\_code\_user\_settings\_updated"



ClaudeFileAccessFailed object { actor, claude\_file\_id, id, 7 more } 

A user was denied access to a file in Claude.ai.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

claude\_file\_id: string

The file the user was denied access to, e.g. "claude\_file\_01HX...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

claude\_artifact\_id: optional string

The artifact the file was accessed through, if any, e.g. "claude\_artifact\_01HX...".

claude\_project\_id: optional string

The project the file was accessed through, if any, e.g. "claude\_proj\_01HX...".

created\_at: optional string

When this activity occurred.

Deprecatedfilename: optional string

Deprecated — DO NOT USE. Always empty; the file's display name is intentionally omitted.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_file\_access\_failed"



ClaudeFileExported object { actor, export\_destination, filename, 7 more } 

A file was exported from Claude to an external storage destination.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string



export\_destination: "google\_drive" or "unspecified"

The external destination the file was exported to.

One of the following:

"google\_drive"

"unspecified"

filename: string

Name of the exported file.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

claude\_chat\_id: optional string

The chat conversation the file was exported from, if the export originated in a chat, e.g. "claude\_chat\_01HX...".

claude\_file\_id: optional string

The exported file, e.g. "claude\_file\_01HX...", if the file has a stored file record; files that exist only inside a session have no file ID.

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_file\_exported"



ClaudeFileViewed object { actor, claude\_file\_id, id, 7 more } 

A user viewed a file in Claude.ai.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

claude\_file\_id: string

The file that was viewed, e.g. "claude\_file\_01HX...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

claude\_artifact\_id: optional string

The artifact the file was accessed through, if any, e.g. "claude\_artifact\_01HX...".

claude\_project\_id: optional string

The project the file was accessed through, if any, e.g. "claude\_proj\_01HX...".

created\_at: optional string

When this activity occurred.

Deprecatedfilename: optional string

Deprecated — DO NOT USE. Always empty; the file's display name is intentionally omitted.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_file\_viewed"



ClaudeProjectSyncSourceCreated object { actor, claude\_project\_id, claude\_project\_sync\_source\_id, 7 more } 

A sync source was connected to a Claude project's knowledge base.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

claude\_project\_id: string

Tagged ID of the project the sync source was connected to.

claude\_project\_sync\_source\_id: string

Tagged ID of the per-project sync source that was created.

provider: string

The external provider backing the sync source, e.g. `github`, `google_drive`, `outline`, `slack`, `salesforce`, `google_calendar`, `gmail`, `asana`, or `mcp_resources`.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

resource\_descriptor: optional string

A short provider-specific identifier for the external resource that was connected, e.g. `owner/repo` for GitHub or a file ID for Google Drive.

type: optional "claude\_project\_sync\_source\_created"



ClaudeProjectSyncSourceDeleted object { actor, claude\_project\_id, claude\_project\_sync\_source\_id, 6 more } 

A sync source was disconnected from a Claude project's knowledge base.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

claude\_project\_id: string

Tagged ID of the project the sync source was disconnected from.

claude\_project\_sync\_source\_id: string

Tagged ID of the per-project sync source that was deleted.

provider: string

The external provider backing the sync source. Always `unspecified` for deletion events.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_project\_sync\_source\_deleted"



ClaudeProjectSyncSourceUpdated object { actor, claude\_project\_id, claude\_project\_sync\_source\_id, 8 more } 

A Claude project sync source's configuration was updated.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

claude\_project\_id: string

Tagged ID of the project the sync source belongs to.

claude\_project\_sync\_source\_id: string

Tagged ID of the per-project sync source that was updated.

provider: string

The external provider backing the sync source, e.g. `github`, `google_drive`, `outline`, `slack`, `salesforce`, `google_calendar`, `gmail`, `asana`, or `mcp_resources`.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

config\_changed: optional boolean

Whether the update changed the stored sync-source configuration, including sync settings such as path filters. False for a re-sync or a metadata-only refresh of the same resource.

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

resource\_descriptor: optional string

A short provider-specific identifier for the external resource after the update, e.g. `owner/repo` for GitHub or a file ID for Google Drive.

type: optional "claude\_project\_sync\_source\_updated"



ClaudeUserSeatTierUpdated object { actor, user\_email, user\_id, 7 more } 

An organization member's seat tier was changed. A null `previous_seat_tier` means the member previously had no seat assigned; a null `current_seat_tier` means the seat was removed.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

user\_email: string

Email address of the member at the time of the change.

user\_id: string

Tagged ID of the member whose seat tier changed.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

current\_seat\_tier: optional string

The member's seat tier after this change, or null if the seat was removed.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

previous\_seat\_tier: optional string

The member's seat tier before this change, or null if no seat was assigned.

type: optional "claude\_user\_seat\_tier\_updated"



CliPluginExecPolicyUpdated object { actor, cli\_name, marketplace\_id, 9 more } 

Admin set or cleared the per-op permission ceiling for a plugin CLI.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

cli\_name: string

CLI name as declared by the plugin manifest

marketplace\_id: string

Marketplace ID owning the plugin

op\_name: string

Op name (or '\*' for the per-CLI default)

plugin\_id: string

Plugin ID resolved from the URL

plugin\_name: string

Plugin name within its marketplace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

max\_permission: optional string

New max\_permission value ('allow' | 'ask' | 'blocked'), or null when cleared

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "cli\_plugin\_exec\_policy\_updated"



ClaudeCommandCreated object { actor, id, command\_id, 5 more } 

Command was created.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

command\_id: optional string

command\_name: optional string

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_command\_created"



ClaudeCommandDeleted object { actor, id, command\_id, 5 more } 

Command was deleted.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

command\_id: optional string

command\_name: optional string

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_command\_deleted"



ClaudeCommandReplaced object { actor, id, command\_id, 5 more } 

Command was replaced.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

command\_id: optional string

command\_name: optional string

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_command\_replaced"



ComplianceAPIAccessed object { actor, request\_id, request\_method, 8 more } 

Logging event auto-generated for each compliance API request.



actor: object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

request\_id: string



request\_method: "DELETE" or "GET" or "POST" or "PUT"

One of the following:

"DELETE"

"GET"

"POST"

"PUT"

status\_code: number

HTTP status code

url: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

request\_body: optional string

Serialized JSON request body

type: optional "compliance\_api\_accessed"



DesignProjectCreated object { actor, creation\_method, design\_project\_id, 7 more } 

A Claude Design project was created.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

creation\_method: string

How the project was created: "direct", "duplicate", "remix", or "template\_from\_project".

design\_project\_id: string

The Design project that was created, e.g. "design\_proj\_01HX...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

project\_type: optional string

The project type: "project", "template", or "design\_system". May be unset for projects created by duplicating or remixing another project.

source\_project\_id: optional string

The source project this was created from, when created via duplicate, remix, or template-from-project. Unset for direct creation.

type: optional "design\_project\_created"



DesignProjectDeleted object { actor, design\_project\_id, id, 4 more } 

A Claude Design project was deleted.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

design\_project\_id: string

The Design project that was deleted, e.g. "design\_proj\_01HX...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "design\_project\_deleted"



DesignProjectUpdated object { actor, design\_project\_id, id, 6 more } 

A Claude Design project's metadata was updated.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

design\_project\_id: string

The Design project that was updated, e.g. "design\_proj\_01HX...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

project\_type: optional string

The project's type after the update: "project", "template", or "design\_system". Present only when the update changed it.

type: optional "design\_project\_updated"

updated\_fields: optional array of string

Names of the fields changed by this update, e.g. "name", "description", "project\_type", "design\_systems".



DesktopExtensionAllowlisted object { actor, extension\_id, id, 4 more } 

A desktop extension was added to an org's allowlist.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

extension\_id: string

Allowlisted DXT extension ID

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "desktop\_extension\_allowlisted"



DesktopExtensionBlocklisted object { actor, extension\_id, id, 4 more } 

A desktop extension was added to the global blocklist.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

extension\_id: string

Blocklisted DXT extension ID

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "desktop\_extension\_blocklisted"



DesktopExtensionDeleted object { actor, extension\_id, id, 5 more } 

A desktop extension was deleted, either globally by an admin or org-scoped by an org owner.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

extension\_id: string

DXT extension ID

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "desktop\_extension\_deleted"

version: optional string

Specific version deleted (null if all versions)



DesktopExtensionRemovedFromAllowlist object { actor, extension\_id, id, 4 more } 

A desktop extension was removed from an org's allowlist.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

extension\_id: string

DXT extension ID removed from allowlist

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "desktop\_extension\_removed\_from\_allowlist"



DesktopExtensionUnblocked object { actor, extension\_id, id, 4 more } 

A desktop extension was removed from the global blocklist.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

extension\_id: string

Unblocked DXT extension ID

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "desktop\_extension\_unblocked"



DesktopExtensionUploaded object { actor, extension\_id, version, 5 more } 

A desktop extension was uploaded, either globally by an admin or org-scoped by an org owner.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

extension\_id: string

DXT extension ID

version: string

Version string from the manifest

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "desktop\_extension\_uploaded"



DesktopExtensionVersionUploaded object { actor, extension\_id, version, 5 more } 

A new version of an existing org-owned desktop extension was uploaded.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

extension\_id: string

DXT extension ID

version: string

Version string from the manifest

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "desktop\_extension\_version\_uploaded"



DomainClaimInitiated object { actor, id, created\_at, 3 more } 

Domain capture claim initiated over personal accounts on verified domains.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "domain\_claim\_initiated"



EndUserInviteRequested object { actor, invitee\_email, id, 4 more } 

Non-admin member submitted an invite request for a new org member.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

invitee\_email: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "end\_user\_invite\_requested"



ExtraUsageBillingEnabled object { actor, id, created\_at, 3 more } 

Usage credit billing was enabled for an organization.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "extra\_usage\_billing\_enabled"



ExtraUsageCreditGranted object { actor, id, created\_at, 3 more } 

A promotional usage credit grant was claimed.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "extra\_usage\_credit\_granted"



ExtraUsageSpendLimitCreated object { actor, id, amount, 8 more } 

Usage credit spend limit was created.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { api\_key\_id, ip\_address, user\_agent, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

amount: optional number

The monthly credit limit amount in minor units (e.g. cents).

created\_at: optional string

When this activity occurred.

is\_enabled: optional boolean

Whether the spend limit is enabled.

limit\_type: optional string

The type of spend limit created (e.g. organization, seat\_tier, member, service, group).

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

spend\_limit\_id: optional string

Tagged ID of the spend limit.

type: optional "extra\_usage\_spend\_limit\_created"

Deprecateduser\_id: optional string

Deprecated. Tagged ID of the admin who performed the action — not the target member. Use `spend_limit_id` to look up the target member.



ExtraUsageSpendLimitDeleted object { actor, id, created\_at, 5 more } 

Usage credit spend limit was deleted.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { api\_key\_id, ip\_address, user\_agent, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

spend\_limit\_id: optional string

Tagged ID of the spend limit.

type: optional "extra\_usage\_spend\_limit\_deleted"

Deprecateduser\_id: optional string

Deprecated. Tagged ID of the admin who performed the action — not the target member. Use `spend_limit_id` to look up the target member.



ExtraUsageSpendLimitIncreaseRequestApproved object { actor, id, amount, 7 more } 

A usage credit spend limit increase request was approved.



actor: object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

amount: optional number

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

requester\_user\_id: optional string

spend\_limit\_id: optional string

spend\_limit\_increase\_request\_id: optional string

type: optional "extra\_usage\_spend\_limit\_increase\_request\_approved"



ExtraUsageSpendLimitIncreaseRequestDenied object { actor, id, created\_at, 5 more } 

A usage credit spend limit increase request was denied.



actor: object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

requester\_user\_id: optional string

spend\_limit\_increase\_request\_id: optional string

type: optional "extra\_usage\_spend\_limit\_increase\_request\_denied"



ExtraUsageSpendLimitUpdated object { actor, id, amount, 8 more } 

Usage credit spend limit was updated.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { api\_key\_id, ip\_address, user\_agent, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

amount: optional number

The new monthly credit limit amount in minor units (e.g. cents).

created\_at: optional string

When this activity occurred.

is\_enabled: optional boolean

Whether the spend limit is enabled.

limit\_type: optional string

The type of spend limit updated (e.g. organization, seat\_tier, member, service, group).

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

spend\_limit\_id: optional string

Tagged ID of the spend limit.

type: optional "extra\_usage\_spend\_limit\_updated"

Deprecateduser\_id: optional string

Deprecated. Tagged ID of the admin who performed the action — not the target member. Use `spend_limit_id` to look up the target member.



ClaudeFileDeleted object { actor, claude\_file\_id, filename, 5 more } 

A file was deleted.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_file\_id: string

filename: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_file\_deleted"



ClaudeFileUploaded object { actor, claude\_file\_id, filename, 7 more } 

A file was uploaded.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_file\_id: string

filename: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

claude\_chat\_id: optional string

Chat ID if known at upload time (null for the upload-then-attach flow). To find which chats a file was later attached to, use `GET /v1/compliance/apps/chats/files/{claude_file_id}`.

claude\_project\_id: optional string

Project ID if file was uploaded to a project

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_file\_uploaded"



GheConfigurationCreated object { actor, ghe\_configuration\_id, id, 4 more } 

Admin created a GHE configuration.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

ghe\_configuration\_id: string

ID of the GHE configuration

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "ghe\_configuration\_created"



GheConfigurationDeleted object { actor, ghe\_configuration\_id, id, 4 more } 

Admin deleted a GHE configuration.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

ghe\_configuration\_id: string

ID of the GHE configuration

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "ghe\_configuration\_deleted"



GheConfigurationUpdated object { actor, ghe\_configuration\_id, id, 4 more } 

Admin updated a GHE configuration.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

ghe\_configuration\_id: string

ID of the GHE configuration

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "ghe\_configuration\_updated"



GheUserConnected object { actor, id, created\_at, 4 more } 

User connected to a GHE instance.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

ghe\_configuration\_id: optional string

ID of the GHE configuration

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "ghe\_user\_connected"



GheUserDisconnected object { actor, id, created\_at, 4 more } 

User disconnected from a GHE instance.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

ghe\_configuration\_id: optional string

ID of the GHE configuration

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "ghe\_user\_disconnected"



GheWebhookSignatureInvalid object { actor, ghe\_configuration\_id, id, 4 more } 

Webhook signature validation failed.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

ghe\_configuration\_id: string

ID of the GHE configuration

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "ghe\_webhook\_signature\_invalid"



ClaudeGitHubIntegrationCreated object { actor, integration\_id, id, 6 more } 

A GitHub integration was enabled for the organization.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

integration\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_name: optional string

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

repository\_name: optional string

type: optional "claude\_github\_integration\_created"



ClaudeGitHubIntegrationDeleted object { actor, integration\_id, id, 6 more } 

A GitHub integration was disabled for the organization.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

integration\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_name: optional string

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

repository\_name: optional string

type: optional "claude\_github\_integration\_deleted"



ClaudeGitHubIntegrationUpdated object { actor, integration\_id, id, 6 more } 

A GitHub integration's configuration was updated.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

integration\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_name: optional string

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

repository\_name: optional string

type: optional "claude\_github\_integration\_updated"



ClaudeGdriveIntegrationCreated object { actor, integration\_id, id, 5 more } 

A Google Drive integration was enabled for the organization.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

integration\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

folder\_id: optional string

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_gdrive\_integration\_created"



ClaudeGdriveIntegrationDeleted object { actor, integration\_id, id, 5 more } 

A Google Drive integration was disabled for the organization.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

integration\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

folder\_id: optional string

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_gdrive\_integration\_deleted"



ClaudeGdriveIntegrationUpdated object { actor, integration\_id, id, 5 more } 

A Google Drive integration's configuration was updated.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

integration\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

folder\_id: optional string

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_gdrive\_integration\_updated"



GroupCreated object { actor, group\_id, group\_name, 5 more } 

A group was created (RBAC admin or SCIM provisioning).



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

group\_id: string

Tagged ID of the created group

group\_name: string

Name of the created group

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "group\_created"



GroupDeleted object { actor, group\_id, id, 4 more } 

A group was deleted (RBAC admin or SCIM provisioning).



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

group\_id: string

Tagged ID of the deleted group

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "group\_deleted"



GroupListViewed object { actor, id, created\_at, 3 more } 

Admin viewed the list of RBAC groups.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "group\_list\_viewed"



GroupMemberAdded object { actor, group\_id, id, 5 more } 

One or more members were added to a group.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

group\_id: string

Tagged ID of the group

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

member\_ids: optional array of string

Tagged IDs of the members added

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "group\_member\_added"



GroupMemberAdditionFailed object { actor, group\_id, id, 5 more } 

A request to add members to a group failed. Some of the requested members may have been added before the failure.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

group\_id: string

Tagged ID of the group

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

member\_ids: optional array of string

Tagged IDs of the members the request attempted to add

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "group\_member\_addition\_failed"



GroupMemberListViewed object { actor, group\_id, id, 4 more } 

Admin viewed the members of an RBAC group.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

group\_id: string

Tagged ID of the group

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "group\_member\_list\_viewed"



GroupMemberRemovalFailed object { actor, group\_id, id, 5 more } 

A request to remove members from a group failed. Some of the requested members may have been removed before the failure.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

group\_id: string

Tagged ID of the group

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

member\_ids: optional array of string

Tagged IDs of the members the request attempted to remove

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "group\_member\_removal\_failed"



GroupMemberRemoved object { actor, group\_id, id, 5 more } 

One or more members were removed from a group.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

group\_id: string

Tagged ID of the group

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

member\_ids: optional array of string

Tagged IDs of the members removed

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "group\_member\_removed"



GroupUpdated object { actor, group\_id, id, 4 more } 

A group was updated (RBAC admin or SCIM provisioning).



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

group\_id: string

Tagged ID of the updated group

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "group\_updated"



GroupViewed object { actor, group\_id, id, 4 more } 

A group was viewed.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

group\_id: string

Tagged ID of the viewed group

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "group\_viewed"



IntegrationUserConnected object { actor, id, created\_at, 4 more } 

User connected to an integration.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

integration\_type: optional string

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "integration\_user\_connected"



IntegrationUserDisconnected object { actor, id, created\_at, 4 more } 

User disconnected from an integration.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

integration\_type: optional string

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "integration\_user\_disconnected"



InvoiceCollectionMethodUpdated object { actor, id, created\_at, 4 more } 

Invoice collection method was changed.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

new\_collection\_method: optional string

New collection method (e.g. charge\_automatically, send\_invoice).

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "invoice\_collection\_method\_updated"



UserLoggedOut object { actor, id, created\_at, 3 more } 

A user signed out of one or all sessions.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "user\_logged\_out"



LtiLaunchInitiated object { actor, id, created\_at, 3 more } 

LTI launch was initiated.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "lti\_launch\_initiated"



LtiLaunchSuccess object { actor, id, created\_at, 3 more } 

LTI launch completed successfully.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "lti\_launch\_success"



LtiPlatformCreated object { actor, lti\_platform\_id, lti\_platform\_issuer, 5 more } 

Anthropic staff created an LTI platform integration on behalf of an org.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

lti\_platform\_id: string

UUID of the LTI platform

lti\_platform\_issuer: string

Platform issuer URL

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "lti\_platform\_created"



LtiPlatformUpdated object { actor, lti\_platform\_id, id, 5 more } 

Anthropic staff updated an LTI platform integration on behalf of an org.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

lti\_platform\_id: string

UUID of the LTI platform

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

lti\_platform\_issuer: optional string

Platform issuer URL

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "lti\_platform\_updated"



MagicLinkLoginFailed object { actor, id, created\_at, 3 more } 

A magic link sign-in attempt failed.



actor: object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "magic\_link\_login\_failed"



MagicLinkLoginInitiated object { actor, id, created\_at, 3 more } 

A user requested a magic link sign-in email.



actor: object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "magic\_link\_login\_initiated"



MagicLinkLoginSucceeded object { actor, id, auth\_method, 5 more } 

A user successfully signed in with a magic link email.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

auth\_method: optional "magic\_link"

The method the user used to authenticate. May be absent on activities recorded before this field was introduced.

created\_at: optional string

When this activity occurred.

mfa\_method: optional "not\_used"

The second authentication factor performed during this login, if any. `null` when the second-factor status is not recorded on this event — for example, when authentication was delegated to an external identity provider and any second factor is not visible to Anthropic, or when this event is one step of a multi-step login whose MFA is reported on another activity. May be absent on activities recorded before this field was introduced.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "magic\_link\_login\_succeeded"



ManagedOrganizationSetupCompleted object { actor, id, created\_at, 3 more } 

Managed (AWS Marketplace) organization setup was completed.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "managed\_organization\_setup\_completed"



MarketplaceCreated object { actor, marketplace\_id, id, 4 more } 

Admin created an organization marketplace.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

marketplace\_id: string

Tagged ID of the marketplace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "marketplace\_created"



MarketplaceDeleted object { actor, marketplace\_id, id, 4 more } 

Admin deleted an organization marketplace.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

marketplace\_id: string

Tagged ID of the marketplace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "marketplace\_deleted"



MarketplaceUpdated object { actor, marketplace\_id, id, 4 more } 

Admin updated an organization marketplace.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

marketplace\_id: string

Tagged ID of the marketplace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "marketplace\_updated"



MarketplaceWebhookDeleted object { actor, marketplace\_id, id, 4 more } 

Admin removed the GitHub push webhook for a marketplace.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

marketplace\_id: string

Tagged ID of the marketplace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "marketplace\_webhook\_deleted"



MarketplaceWebhookProvisioned object { actor, marketplace\_id, id, 5 more } 

Admin provisioned a GitHub push webhook for a marketplace.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

marketplace\_id: string

Tagged ID of the marketplace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

github\_webhook\_id: optional number

GitHub-assigned webhook ID returned by the hooks API

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "marketplace\_webhook\_provisioned"



McpServerCreated object { actor, mcp\_server\_id, mcp\_server\_name, 5 more } 

An MCP server was added to the organization.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

mcp\_server\_id: string

Tagged ID of the MCP server

mcp\_server\_name: string

Display name of the MCP server

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "mcp\_server\_created"



McpServerDeleted object { actor, mcp\_server\_id, mcp\_server\_name, 5 more } 

An MCP server was removed from the organization.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

mcp\_server\_id: string

Tagged ID of the MCP server

mcp\_server\_name: string

Display name of the MCP server

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "mcp\_server\_deleted"



McpServerUpdated object { actor, mcp\_server\_id, mcp\_server\_name, 5 more } 

An MCP server's configuration was updated.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

mcp\_server\_id: string

Tagged ID of the MCP server

mcp\_server\_name: string

Display name of the MCP server

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "mcp\_server\_updated"



McpToolPolicyUpdated object { actor, mcp\_server\_id, mcp\_server\_name, 7 more } 

The permission restriction for an MCP tool was set or cleared.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

mcp\_server\_id: string

Tagged ID of the MCP server

mcp\_server\_name: string

Display name of the MCP server

tool\_name: string

Tool name (or '\*' for the MCP-server-wide default)

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

max\_permission: optional string

New max\_permission value ('allow' | 'ask' | 'blocked'), or null when cleared

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "mcp\_tool\_policy\_updated"



OrgAnalyticsAPICapabilityUpdated object { actor, id, created\_at, 5 more } 

Organization analytics\_api capability was enabled or disabled.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

current\_value: optional boolean

Whether the analytics API capability is enabled immediately after this change

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

previous\_value: optional boolean

Whether the analytics API capability was enabled immediately before this change

type: optional "org\_analytics\_api\_capability\_updated"



OrgBulkDeleteInitiated object { actor, id, created\_at, 3 more } 

Organization bulk deletion was initiated.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_bulk\_delete\_initiated"



OrgCapabilityGrantAdded object { actor, grant\_type, principal\_id, 6 more } 

A capability grant was added to a workspace or role.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

grant\_type: string

The type of capability grant that was added.

principal\_id: string

Tagged ID of the principal the grant was added to.



principal\_type: "rbac\_role" or "unspecified" or "workspace"

The kind of principal the grant was added to.

One of the following:

"rbac\_role"

"unspecified"

"workspace"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_capability\_grant\_added"



OrgCapabilityGrantRemoved object { actor, grant\_type, principal\_id, 6 more } 

A capability grant was removed from a workspace or role.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

grant\_type: string

The type of capability grant that was removed.

principal\_id: string

Tagged ID of the principal the grant was removed from.



principal\_type: "rbac\_role" or "unspecified" or "workspace"

The kind of principal the grant was removed from.

One of the following:

"rbac\_role"

"unspecified"

"workspace"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_capability\_grant\_removed"



OrgClaudeCodeDataSharingDisabled object { actor, id, created\_at, 5 more } 

Organization Claude Code data sharing was disabled.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

current\_value: optional boolean

Setting value immediately after this change

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

previous\_value: optional boolean

Setting value immediately before this change

type: optional "org\_claude\_code\_data\_sharing\_disabled"



OrgClaudeCodeDataSharingEnabled object { actor, id, created\_at, 5 more } 

Organization Claude Code data sharing was enabled.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

current\_value: optional boolean

Setting value immediately after this change

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

previous\_value: optional boolean

Setting value immediately before this change

type: optional "org\_claude\_code\_data\_sharing\_enabled"



OrgClaudeCodeDesktopDisabled object { actor, id, created\_at, 5 more } 

Organization Claude Code Desktop was disabled.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

current\_value: optional boolean

Setting value immediately after this change

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

previous\_value: optional boolean

Setting value immediately before this change

type: optional "org\_claude\_code\_desktop\_disabled"



OrgClaudeCodeDesktopEnabled object { actor, id, created\_at, 5 more } 

Organization Claude Code Desktop was enabled.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

current\_value: optional boolean

Setting value immediately after this change

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

previous\_value: optional boolean

Setting value immediately before this change

type: optional "org\_claude\_code\_desktop\_enabled"



OrgClaudeCodeZeroDataRetentionDisabled object { actor, id, created\_at, 3 more } 

A primary owner disabled zero data retention for Claude Code, so Claude
Code content is retained according to the organization's data retention
settings.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_claude\_code\_zero\_data\_retention\_disabled"



OrgComplianceAPISettingsUpdated object { actor, id, compliance\_api\_enabled, 5 more } 

Organization compliance API settings were updated.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

compliance\_api\_enabled: optional boolean

compliance\_api\_logging\_enabled: optional boolean

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_compliance\_api\_settings\_updated"



OrgConnectorDomainGuardUpdated object { actor, enforced, id, 4 more } 

Enterprise admin changed whether connectors are restricted to verified domains.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

enforced: boolean

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_connector\_domain\_guard\_updated"



OrgCoworkActWithoutAskingModeDisabled object { actor, id, created\_at, 3 more } 

The "Act without asking" mode in Cowork was disabled for the organization, so members can no longer let Claude act without asking for approval.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_cowork\_act\_without\_asking\_mode\_disabled"



OrgCoworkActWithoutAskingModeEnabled object { actor, id, created\_at, 3 more } 

The "Act without asking" mode in Cowork was enabled for the organization, allowing members to let Claude act without asking for approval.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_cowork\_act\_without\_asking\_mode\_enabled"



OrgCoworkAgentDisabled object { actor, id, created\_at, 5 more } 

Organization Cowork Agent was disabled.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

current\_value: optional boolean

Setting value immediately after this change

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

previous\_value: optional boolean

Setting value immediately before this change

type: optional "org\_cowork\_agent\_disabled"



OrgCoworkAgentEnabled object { actor, id, created\_at, 5 more } 

Organization Cowork Agent was enabled.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

current\_value: optional boolean

Setting value immediately after this change

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

previous\_value: optional boolean

Setting value immediately before this change

type: optional "org\_cowork\_agent\_enabled"



OrgCoworkDisabled object { actor, id, created\_at, 5 more } 

Organization cowork was disabled.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

current\_value: optional boolean

Setting value immediately after this change

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

previous\_value: optional boolean

Setting value immediately before this change

type: optional "org\_cowork\_disabled"



OrgCoworkEnabled object { actor, id, created\_at, 5 more } 

Organization cowork was enabled.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

current\_value: optional boolean

Setting value immediately after this change

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

previous\_value: optional boolean

Setting value immediately before this change

type: optional "org\_cowork\_enabled"



OrgCoworkMcpAlwaysAllowDisabled object { actor, id, created\_at, 3 more } 

The "Always allow" option for connector tools in Cowork was disabled for the organization, so each use of a connector tool that can make changes requires approval. Read-only connector tools are not affected by this setting.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_cowork\_mcp\_always\_allow\_disabled"



OrgCoworkMcpAlwaysAllowEnabled object { actor, id, created\_at, 3 more } 

The "Always allow" option for connector tools in Cowork was enabled for the organization, letting members approve a connector tool that can make changes once and allow its later uses automatically. Read-only connector tools are not affected by this setting.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_cowork\_mcp\_always\_allow\_enabled"



OrgCoworkOtlpSettingsUpdated object { actor, id, created\_at, 10 more } 

The organization's Cowork OpenTelemetry monitoring export settings were updated.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

new\_otlp\_endpoint: optional string

The OpenTelemetry export endpoint after the change. Credentials in the URL userinfo or query string are removed; path segments are retained. Null if the endpoint is unset or was not itself modified by this update.

new\_otlp\_protocol: optional string

The OpenTelemetry export protocol after the change. Null if the protocol is unset or was not itself modified by this update.

new\_otlp\_resource\_attributes: optional string

The OpenTelemetry resource attributes after the change. Null if the attributes are unset or were not themselves modified by this update.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).



otlp\_headers\_change: optional "cleared" or "set"

Whether the OpenTelemetry export headers were set or cleared. 'set' is recorded for any non-empty submission, including resubmission of an unchanged value. Header values are never included.

One of the following:

"cleared"

"set"

previous\_otlp\_endpoint: optional string

The OpenTelemetry export endpoint before the change. Credentials in the URL userinfo or query string are removed; path segments are retained. Null if the endpoint was previously unset or was not itself modified by this update.

previous\_otlp\_protocol: optional string

The OpenTelemetry export protocol before the change. Null if the protocol was previously unset or was not itself modified by this update.

previous\_otlp\_resource\_attributes: optional string

The OpenTelemetry resource attributes before the change. Null if the attributes were previously unset or were not themselves modified by this update.

type: optional "org\_cowork\_otlp\_settings\_updated"



OrgCreationBlocked object { actor, id, created\_at, 4 more } 

Organization creation was blocked.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

reason: optional string

type: optional "org\_creation\_blocked"



OrgDataExportAccessed object { actor, id, created\_at, 4 more } 

Organization data export file was accessed/downloaded via signed URL.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.



export\_type: optional "conversations" or "workbench"

Which data set was downloaded. Absent on records written before this field was introduced.

One of the following:

"conversations"

"workbench"

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_data\_export\_accessed"



OrgDataExportCompleted object { actor, id, created\_at, 4 more } 

Organization data export was completed.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.



export\_type: optional "conversations" or "workbench"

Which data set was exported. Absent on records written before this field was introduced.

One of the following:

"conversations"

"workbench"

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_data\_export\_completed"



OrgDataExportStarted object { actor, id, created\_at, 4 more } 

Organization data export was started.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.



export\_type: optional "conversations" or "workbench"

Which data set was exported. Absent on records written before this field was introduced.

One of the following:

"conversations"

"workbench"

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_data\_export\_started"



OrgDataResidencyUpdated object { actor, updates, id, 4 more } 

The organization's inference data residency settings were updated.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



updates: array of object { current\_value, previous\_value, type } 

current\_value: string

Setting value immediately after this change. For allowed\_inference\_geos: a comma-separated list of geo codes (e.g. 'global,us'), or the literal 'unrestricted'. For default\_inference\_geo: a single geo code.

previous\_value: string

Setting value immediately before this change. For allowed\_inference\_geos: a comma-separated list of geo codes (e.g. 'global,us'), or the literal 'unrestricted'. For default\_inference\_geo: a single geo code.



type: "allowed\_inference\_geos" or "default\_inference\_geo"

One of the following:

"allowed\_inference\_geos"

"default\_inference\_geo"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_data\_residency\_updated"



OrgDeletedViaBulk object { actor, id, created\_at, 3 more } 

Organization was deleted via bulk operation.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_deleted\_via\_bulk"



OrgDeletionRequested object { actor, id, created\_at, 3 more } 

Organization deletion was requested.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_deletion\_requested"



OrgDirectoryResyncCompleted object { actor, resync\_uuid, id, 4 more } 

Organization directory resync completed successfully.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

resync\_uuid: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_directory\_resync\_completed"



OrgDirectoryResyncFailed object { actor, resync\_uuid, id, 4 more } 

Organization directory resync failed.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

resync\_uuid: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_directory\_resync\_failed"



OrgDirectoryResyncStarted object { actor, resync\_uuid, sync\_destinations, 5 more } 

Organization directory resync was started asynchronously.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

resync\_uuid: string

sync\_destinations: array of string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_directory\_resync\_started"



OrgDirectorySyncActivated object { actor, id, created\_at, 3 more } 

Organization directory sync was activated.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_directory\_sync\_activated"



OrgDirectorySyncAddInitiated object { actor, id, created\_at, 3 more } 

Organization directory sync setup was initiated.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_directory\_sync\_add\_initiated"



OrgDirectorySyncDeleted object { actor, id, created\_at, 3 more } 

Organization directory sync was deleted.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_directory\_sync\_deleted"



OrgDiscoverabilityDisabled object { actor, id, created\_at, 3 more } 

Admin disabled organization discoverability.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_discoverability\_disabled"



OrgDiscoverabilityEnabled object { actor, id, created\_at, 3 more } 

Admin enabled organization discoverability.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_discoverability\_enabled"



OrgDiscoverabilitySettingsUpdated object { actor, id, created\_at, 3 more } 

Admin updated organization discoverability settings.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_discoverability\_settings\_updated"



OrgDomainAddInitiated object { actor, id, created\_at, 3 more } 

Organization domain verification was initiated.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_domain\_add\_initiated"



OrgDomainRemoved object { actor, id, created\_at, 4 more } 

Organization domain was removed.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

domain: optional string

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_domain\_removed"



OrgDomainVerified object { actor, id, created\_at, 4 more } 

Organization domain was verified.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

domain: optional string

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_domain\_verified"



OrgExternalKeyCreated object { actor, external\_key\_id, provider, 5 more } 

A CMEK external key config was created.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

external\_key\_id: string

Tagged ID of the created external key config



provider: "aws" or "azure" or "gcp"

KMS provider backing the key

One of the following:

"aws"

"azure"

"gcp"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_external\_key\_created"



OrgExternalKeyDeleted object { actor, external\_key\_id, id, 4 more } 

A CMEK external key config was deleted.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

external\_key\_id: string

Tagged ID of the deleted external key config

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_external\_key\_deleted"



OrgExternalKeyUpdated object { actor, external\_key\_id, updates, 5 more } 

A CMEK external key config was updated.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

external\_key\_id: string

Tagged ID of the updated external key config



updates: array of object { current\_value, previous\_value, type } 

current\_value: string

previous\_value: string



type: "display\_name" or "geo" or "provider\_config"

One of the following:

"display\_name"

"geo"

"provider\_config"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_external\_key\_updated"



OrgExternalKeyValidated object { actor, external\_key\_id, validation\_result, 5 more } 

A CMEK external key config was validated against the customer's KMS.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

external\_key\_id: string

Tagged ID of the validated external key config



validation\_result: "failure" or "success"

Outcome of the encrypt/decrypt roundtrip

One of the following:

"failure"

"success"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_external\_key\_validated"



OrgHipaaSelfServeEnabled object { actor, baa\_content\_hash, baa\_version\_label, 6 more } 

A primary owner click-accepted the BAA and enabled HIPAA protections
for the organization via the self-serve flow.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

baa\_content\_hash: string

baa\_version\_label: string

setup\_guide\_content\_hash: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_hipaa\_self\_serve\_enabled"



OrgIPRestrictionCreated object { actor, id, created\_at, 3 more } 

Organization IP restriction was created.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_ip\_restriction\_created"



OrgIPRestrictionDeleted object { actor, id, created\_at, 3 more } 

Organization IP restriction was deleted.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_ip\_restriction\_deleted"



OrgIPRestrictionUpdated object { actor, id, created\_at, 3 more } 

Organization IP restriction was updated.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_ip\_restriction\_updated"



OrgInviteLinkDisabled object { actor, id, created\_at, 3 more } 

Organization invite link was disabled.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_invite\_link\_disabled"



OrgInviteLinkGenerated object { actor, id, created\_at, 3 more } 

Organization invite link was generated.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_invite\_link\_generated"



OrgInviteLinkRegenerated object { actor, id, created\_at, 3 more } 

Organization invite link was regenerated (previous link invalidated).



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_invite\_link\_regenerated"



OrgInviteViewed object { actor, invite\_id, id, 4 more } 

An organization invite was viewed.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

invite\_id: string

Tagged ID of the viewed invite

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_invite\_viewed"



OrgInvitesListed object { actor, id, created\_at, 3 more } 

Organization invites were listed.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_invites\_listed"



OrgJoinProposalDecided object { actor, approved, id, 4 more } 

Approve or reject decision on a parent-org join proposal.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

approved: boolean

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_join\_proposal\_decided"



OrgJoinRequestApproved object { actor, id, created\_at, 3 more } 

Admin approved a join request.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_join\_request\_approved"



OrgJoinRequestCreated object { actor, id, created\_at, 3 more } 

User requested to join an organization.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_join\_request\_created"



OrgJoinRequestDismissed object { actor, id, created\_at, 3 more } 

Admin dismissed a join request.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_join\_request\_dismissed"



OrgJoinRequestInstantApproved object { actor, id, created\_at, 3 more } 

Join request was instantly approved.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_join\_request\_instant\_approved"



OrgJoinRequestsBulkDismissed object { actor, id, created\_at, 3 more } 

Admin bulk-dismissed join requests.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_join\_requests\_bulk\_dismissed"



OrgMagicLinkSecondFactorToggled object { actor, enabled, id, 4 more } 

Organization magic link second factor was toggled.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

enabled: boolean

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_magic\_link\_second\_factor\_toggled"



OrgMemberInvitesDisabled object { actor, id, created\_at, 3 more } 

Admin disabled member invites for the organization.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_member\_invites\_disabled"



OrgMemberInvitesEnabled object { actor, id, created\_at, 3 more } 

Admin enabled member invites for the organization.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_member\_invites\_enabled"



OrgMembersExported object { actor, id, created\_at, 3 more } 

Organization members list was exported as CSV.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_members\_exported"



OrgModelDefaultUpdated object { action, actor, override\_user\_selection, 9 more } 

An organization or role default model setting was changed by an administrator.



action: "cleared" or "set" or "unspecified"

Whether the default model was set or cleared

One of the following:

"cleared"

"set"

"unspecified"



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

override\_user\_selection: boolean

Whether the default is enforced as a fixed default, resetting members' own model selections at the start of each new conversation

principal\_id: string

Tagged ID of the organization or role the default applies to



principal\_type: "org" or "rbac\_role" or "unspecified"

Whether the default applies to the whole organization or to a single role

One of the following:

"org"

"rbac\_role"

"unspecified"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

default\_model: optional string

The model set as the default, when the action is set



model\_access: optional array of object { api\_name, enabled, max\_effort\_level } 

The per-model access overrides set for this principal; absent when no overrides are configured

api\_name: string

The model the decision applies to

enabled: boolean

Whether members with this principal may select the model

max\_effort\_level: optional string

The highest effort level members may select for this model, when capped

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_model\_default\_updated"



OrgParentJoinProposalCreated object { actor, id, created\_at, 3 more } 

Organization parent join proposal was created.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_parent\_join\_proposal\_created"



OrgParentSearchPerformed object { actor, id, created\_at, 3 more } 

Organization parent search was performed.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_parent\_search\_performed"



OrgSSOAddInitiated object { actor, id, created\_at, 3 more } 

Organization SSO setup was initiated.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_sso\_add\_initiated"



OrgSSOConnectionActivated object { actor, id, connection\_id, 5 more } 

Organization SSO connection was activated.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

connection\_id: optional string

connection\_type: optional string

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_sso\_connection\_activated"



OrgSSOConnectionDeactivated object { actor, id, connection\_id, 4 more } 

Organization SSO connection was deactivated.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

connection\_id: optional string

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_sso\_connection\_deactivated"



OrgSSOConnectionDeleted object { actor, id, connection\_id, 4 more } 

Organization SSO connection was deleted.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

connection\_id: optional string

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_sso\_connection\_deleted"



OrgSSOGroupRoleMappingsUpdated object { actor, id, created\_at, 3 more } 

Organization SSO group role mappings were updated.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_sso\_group\_role\_mappings\_updated"



OrgSSOProvisioningModeChanged object { actor, id, created\_at, 5 more } 

Organization SSO provisioning mode was changed.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

new\_mode: optional string

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

previous\_mode: optional string

type: optional "org\_sso\_provisioning\_mode\_changed"



OrgSSOSeatTierAssignmentToggled object { actor, enabled, id, 5 more } 

Organization SSO seat tier assignment was toggled.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

enabled: boolean

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

previous\_enabled: optional boolean

Whether SSO seat tier assignment was enabled before this change.

type: optional "org\_sso\_seat\_tier\_assignment\_toggled"



OrgSSOSeatTierMappingsUpdated object { actor, id, created\_at, 5 more } 

Organization SSO seat tier mappings were updated.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.



current\_mappings: optional array of object { idp\_group\_name, seat\_tier } 

Identity provider group to seat tier mappings after this change.

idp\_group\_name: string

Name of the identity provider group.

seat\_tier: optional string

Seat tier assigned to members of the identity provider group, or null if the mapping assigns no seat.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).



previous\_mappings: optional array of object { idp\_group\_name, seat\_tier } 

Identity provider group to seat tier mappings before this change.

idp\_group\_name: string

Name of the identity provider group.

seat\_tier: optional string

Seat tier assigned to members of the identity provider group, or null if the mapping assigns no seat.

type: optional "org\_sso\_seat\_tier\_mappings\_updated"



OrgSSOToggled object { actor, enabled, id, 4 more } 

Organization SSO was toggled on or off.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

enabled: boolean

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_sso\_toggled"



OrgSyncDeletingSynchronizedFilesStarted object { actor, id, created\_at, 3 more } 

Organization started deleting synchronized files.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_sync\_deleting\_synchronized\_files\_started"



OrgSyncSynchronizedFilesDeleted object { actor, id, created\_at, 3 more } 

Organization synchronized files were deleted.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_sync\_synchronized\_files\_deleted"



OrgTaintAdded object { actor, id, created\_at, 4 more } 

A taint was added to an organization.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

taint: optional string

type: optional "org\_taint\_added"



OrgTaintRemoved object { actor, id, created\_at, 4 more } 

A taint was removed from an organization.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

taint: optional string

type: optional "org\_taint\_removed"



OrgUserDeleted object { actor, id, created\_at, 5 more } 

User was removed from organization.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or 2 more

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

deleted\_user\_email: optional string

deleted\_user\_id: optional string

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_user\_deleted"



OrgUserInviteAccepted object { actor, id, created\_at, 4 more } 

Organization user invite was accepted.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

invite\_id: optional string

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_user\_invite\_accepted"



OrgUserInviteDeleted object { actor, id, created\_at, 4 more } 

Organization user invite was deleted.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or 2 more

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

invite\_id: optional string

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_user\_invite\_deleted"



OrgUserInviteReSent object { actor, id, created\_at, 6 more } 

Organization user invite was re-sent.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

invited\_email: optional string

invited\_role: optional string

Role the invited user will receive on joining

invited\_seat\_tier: optional string

Seat tier the invited user will receive on joining

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_user\_invite\_re\_sent"



OrgUserInviteRejected object { actor, id, created\_at, 4 more } 

Organization user invite was rejected.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

invite\_id: optional string

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_user\_invite\_rejected"



OrgUserInviteSent object { actor, id, created\_at, 7 more } 

Organization user invite was sent.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type }  or object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or 2 more

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

invited\_email: optional string

invited\_rbac\_group\_ids: optional array of string

RBAC group IDs the invited user will be added to on joining

invited\_role: optional string

invited\_seat\_tier: optional string

Seat tier the invited user will receive on joining

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_user\_invite\_sent"



OrgUserLeft object { actor, id, created\_at, 4 more } 

User removed themselves from organization.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

previous\_role: optional string

type: optional "org\_user\_left"



OrgUserTrustedDevicesRevoked object { actor, completed, devices\_revoked\_count, 7 more } 

An organization admin revoked a member's trusted devices and signed the member out of all active sessions.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

completed: boolean

Whether the operation completed fully. False records an attempt that revoked the counted credentials but failed before finishing.

devices\_revoked\_count: number

Number of trusted devices revoked

sessions\_revoked\_count: number

Number of active sessions the member was signed out of

user\_id: string

Tagged ID of the member whose trusted devices were revoked

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_user\_trusted\_devices\_revoked"



OrgUserViewed object { actor, user\_id, id, 4 more } 

An organization user was viewed.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

user\_id: string

Tagged ID of the viewed user

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_user\_viewed"



OrgUsersListed object { actor, id, created\_at, 3 more } 

Organization users were listed.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "org\_users\_listed"



OrgWorkAcrossAppsDisabled object { actor, id, created\_at, 5 more } 

Organization Work Across Apps was disabled.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

current\_value: optional boolean

Setting value immediately after this change

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

previous\_value: optional boolean

Setting value immediately before this change

type: optional "org\_work\_across\_apps\_disabled"



OrgWorkAcrossAppsEnabled object { actor, id, created\_at, 5 more } 

Organization Work Across Apps was enabled.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

current\_value: optional boolean

Setting value immediately after this change

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

previous\_value: optional boolean

Setting value immediately before this change

type: optional "org\_work\_across\_apps\_enabled"



OrganizationAddressUpdated object { actor, id, billing\_address\_updated, 7 more } 

The organization's billing or shipping address was updated.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

billing\_address\_updated: optional boolean

billing\_name\_updated: optional boolean

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

shipping\_address\_updated: optional boolean

shipping\_name\_updated: optional boolean

type: optional "organization\_address\_updated"



OrganizationIconDeleted object { actor, id, created\_at, 3 more } 

Organization's custom icon deleted.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "organization\_icon\_deleted"



OrganizationIconUpdated object { actor, id, created\_at, 3 more } 

Organization's custom icon uploaded or replaced.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "organization\_icon\_updated"



ClaudeOrganizationSettingsUpdated object { actor, updates, id, 4 more } 

Organization settings were updated.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



updates: array of object { current\_value, previous\_value, type }  or object { current\_value, previous\_value, type }  or object { current\_value, previous\_value, type }  or 61 more

One of the following:



OrganizationName object { current\_value, previous\_value, type } 

The organization name setting was changed.

current\_value: string

Setting value immediately after this change

previous\_value: string

Setting value immediately before this change

type: optional "name"



OrganizationCapabilities object { current\_value, previous\_value, type } 

The organization capabilities setting was changed.

current\_value: array of string

Setting value immediately after this change

previous\_value: array of string

Setting value immediately before this change

type: optional "capabilities"



OrganizationRedactContent object { current\_value, previous\_value, type } 

The organization content-redaction setting was changed.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "redact\_content"



PublicProjectsEnabled object { current\_value, previous\_value, type } 

The public projects setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "public\_projects\_enabled"



WebSearchEnabled object { current\_value, previous\_value, type } 

The web search setting was changed.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "web\_search\_enabled"



GeolocationEnabled object { current\_value, previous\_value, type } 

The geolocation setting was changed.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "geolocation\_enabled"



OrgMemoryEnabledSetting object { current\_value, previous\_value, type } 

The memory setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "enabled\_saffron"



DataRetentionPeriods object { current\_value, previous\_value, type } 

The data retention periods setting was changed for the organization.



current\_value: array of object { data\_type, duration, timescale } 

Setting value immediately after this change



data\_type: "all" or "artifact\_private" or "artifact\_shared" or 2 more

One of the following:

"all"

"artifact\_private"

"artifact\_shared"

"chat"

"project"

duration: number



timescale: "day" or "indefinite" or "month"

One of the following:

"day"

"indefinite"

"month"



previous\_value: array of object { data\_type, duration, timescale } 

Setting value immediately before this change



data\_type: "all" or "artifact\_private" or "artifact\_shared" or 2 more

One of the following:

"all"

"artifact\_private"

"artifact\_shared"

"chat"

"project"

duration: number



timescale: "day" or "indefinite" or "month"

One of the following:

"day"

"indefinite"

"month"

type: optional "data\_retention\_periods"



MembersLimit object { current\_value, previous\_value, type } 

The members limit setting was changed for the organization.

current\_value: number

Setting value immediately after this change

previous\_value: number

Setting value immediately before this change

type: optional "members\_limit"



ClaudeAPIInArtifactsEnabled object { current\_value, previous\_value, type } 

The Claude API in Artifacts setting was changed.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "claude\_api\_in\_artifacts\_enabled"



SupportContactMode object { current\_value, previous\_value, type } 

The support contact routing mode setting was changed for the organization.



current\_value: "ai\_support\_only" or "human\_support\_restricted"

Setting value immediately after this change

One of the following:

"ai\_support\_only"

"human\_support\_restricted"



previous\_value: "ai\_support\_only" or "human\_support\_restricted"

Setting value immediately before this change

One of the following:

"ai\_support\_only"

"human\_support\_restricted"

type: optional "support\_contact\_mode"



SupportContactAlwaysIncludeAdminsOwners object { current\_value, previous\_value, type } 

The support contact always-include-admins-owners setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "support\_contact\_always\_include\_admins\_owners"



SupportContactDesignatedGroups object { current\_value, previous\_value, type } 

The support contact designated groups setting was changed for the organization.

current\_value: array of string

Setting value immediately after this change

previous\_value: array of string

Setting value immediately before this change

type: optional "support\_contact\_designated\_groups"



SubscriptionItemQuotas object { current\_value, previous\_value, type } 

The organization's subscription seat quotas were changed.

current\_value: map[number]

Seat-type to quantity mapping immediately after this change. A null quantity means the item is unlimited/unmetered.

previous\_value: map[number]

Seat-type to quantity mapping immediately before this change. A null quantity means the item was unlimited/unmetered.

type: optional "subscription\_item\_quotas"



MembersBulkSeatTierAssignment object { current\_value, member\_count, previous\_value, type } 

All organization members were assigned the specified seat tier.

current\_value: string

The seat tier every member was assigned to

member\_count: optional number

Number of members whose seat tier was changed

previous\_value: optional string

Not populated; members may have held differing seat tiers before the bulk assignment

type: optional "members\_bulk\_seat\_tier\_assignment"



ClaudeCodeWebEnabled object { current\_value, previous\_value, type } 

The Claude Code on the web setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "claude\_code\_web\_enabled"



ClaudeCodeDesktopBypassPermissionsEnabled object { current\_value, previous\_value, type } 

The Claude Code Desktop bypass-permissions mode setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "claude\_code\_desktop\_bypass\_permissions\_enabled"



ClaudeCodeDesktopAutoPermissionsEnabled object { current\_value, previous\_value, type } 

The Claude Code Desktop auto-permissions mode setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "claude\_code\_desktop\_auto\_permissions\_enabled"



WorkbenchCompletionFeedbackEnabled object { current\_value, previous\_value, type } 

The Workbench completion feedback setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "workbench\_completion\_feedback\_enabled"



ClaudeAICompletionFeedbackEnabled object { current\_value, previous\_value, type } 

The Claude.ai completion feedback setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "claude\_ai\_completion\_feedback\_enabled"



ClaudeAIIntegrationSharingEnabled object { current\_value, previous\_value, type } 

The Claude.ai integration sharing setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "claude\_ai\_integration\_sharing\_enabled"



ClaudeAIChatSharingEnabled object { current\_value, previous\_value, type } 

The Claude.ai chat sharing setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "claude\_ai\_chat\_sharing\_enabled"



ClaudeAiccrSharingEnabled object { current\_value, previous\_value, type } 

The Claude.ai remote Claude Code session sharing setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "claude\_ai\_ccr\_sharing\_enabled"



BatchesDownloadUiVisibility object { current\_value, previous\_value, type } 

The batches download UI visibility setting was changed for the organization.



current\_value: "all" or "none" or "selected"

Setting value immediately after this change

One of the following:

"all"

"none"

"selected"



previous\_value: "all" or "none" or "selected"

Setting value immediately before this change

One of the following:

"all"

"none"

"selected"

type: optional "batches\_download\_ui\_visibility"



AllowedInviteDomains object { current\_value, previous\_value, type } 

The allowed invite domains setting was changed for the organization.

current\_value: array of string

Setting value immediately after this change

previous\_value: array of string

Setting value immediately before this change

type: optional "allowed\_invite\_domains"



WebSearchAPISettingsChanged object { current\_value, previous\_value, type } 

The web search API setting was changed for the organization.



current\_value: object { domain\_filters, is\_enabled } 

Setting value immediately after this change



domain\_filters: object { allowed\_domains, blocked\_domains } 

Allowed/blocked domain filters shared by web\_search and web\_fetch tools.

allowed\_domains: optional array of string

blocked\_domains: optional array of string

is\_enabled: boolean



previous\_value: object { domain\_filters, is\_enabled } 

Setting value immediately before this change



domain\_filters: object { allowed\_domains, blocked\_domains } 

Allowed/blocked domain filters shared by web\_search and web\_fetch tools.

allowed\_domains: optional array of string

blocked\_domains: optional array of string

is\_enabled: boolean

type: optional "web\_search\_api\_settings"



WebFetchAPISettingsChanged object { current\_value, previous\_value, type } 

The web fetch API setting was changed for the organization.



current\_value: object { domain\_filters, is\_enabled } 

Setting value immediately after this change



domain\_filters: object { allowed\_domains, blocked\_domains } 

Allowed/blocked domain filters shared by web\_search and web\_fetch tools.

allowed\_domains: optional array of string

blocked\_domains: optional array of string

is\_enabled: boolean



previous\_value: object { domain\_filters, is\_enabled } 

Setting value immediately before this change



domain\_filters: object { allowed\_domains, blocked\_domains } 

Allowed/blocked domain filters shared by web\_search and web\_fetch tools.

allowed\_domains: optional array of string

blocked\_domains: optional array of string

is\_enabled: boolean

type: optional "web\_fetch\_api\_settings"



DefaultWorkspaceSettings object { current\_value, previous\_value, type } 

The default workspace setting was changed for the organization.



current\_value: object { enable\_api\_keys } 

Setting value immediately after this change

enable\_api\_keys: optional boolean



previous\_value: object { enable\_api\_keys } 

Setting value immediately before this change

enable\_api\_keys: optional boolean

type: optional "default\_workspace\_settings"



BatchesDownloadUiEnabledWorkspaceIDs object { current\_value, previous\_value, type } 

The batches download UI enabled workspace IDs setting was changed for the organization.

current\_value: array of string

Setting value immediately after this change

previous\_value: array of string

Setting value immediately before this change

type: optional "batches\_download\_ui\_enabled\_workspace\_ids"



ClaudeCodeManagedSettings object { current\_value, current\_version, previous\_value, 3 more } 

The organization's Claude Code managed settings were changed.

The full previous and current settings content is provided in the
`previous_value` and `current_value` fields.

current\_value: optional map[unknown]

current\_version: optional number

previous\_value: optional map[unknown]

previous\_version: optional number

settings\_uuid: optional string

type: optional "claude\_code\_managed\_settings"



AccountSessionDurationSeconds object { current\_value, previous\_value, type } 

Tracks changes to the enterprise account session duration setting (in seconds).

current\_value: number

Setting value immediately after this change

previous\_value: number

Setting value immediately before this change

type: optional "account\_session\_duration\_seconds"



VcsConnections object { current\_value, previous\_value, type } 

Tracks changes to VCS (GitHub, etc.) organization connections.



current\_value: array of object { org\_name, type, metadata, org\_id } 

Setting value immediately after this change

org\_name: string

type: "github"

Supported Version Control System providers.

metadata: optional map[string]

org\_id: optional string



previous\_value: array of object { org\_name, type, metadata, org\_id } 

Setting value immediately before this change

org\_name: string

type: "github"

Supported Version Control System providers.

metadata: optional map[string]

org\_id: optional string

type: optional "vcs\_connections"



DisabledAdminRequestTypes object { current\_value, previous\_value, type } 

Tracks changes to which admin request types are disabled.

current\_value: array of string

Setting value immediately after this change

previous\_value: array of string

Setting value immediately before this change

type: optional "disabled\_admin\_request\_types"



MemberUsageDashboardVisible object { current\_value, previous\_value, type } 

The member usage dashboard visibility setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "member\_usage\_dashboard\_visible"



CodeExecutionNetworkEgressEnabled object { current\_value, previous\_value, type } 

The code execution network egress setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "code\_execution\_network\_egress\_enabled"



CodeExecutionDomainAllowlistChanged object { current\_value, previous\_value, type } 

The code execution domain allowlist setting was changed for the organization.

current\_value: array of string

Setting value immediately after this change

previous\_value: array of string

Setting value immediately before this change

type: optional "code\_execution\_domain\_allowlist\_changed"



CodeExecutionDomainAllowlistTemplateChanged object { current\_value, previous\_value, type } 

The code execution domain allowlist template setting was changed for the organization.



current\_value: "custom" or "full\_egress" or "package\_managers"

Setting value immediately after this change

One of the following:

"custom"

"full\_egress"

"package\_managers"



previous\_value: "custom" or "full\_egress" or "package\_managers"

Setting value immediately before this change

One of the following:

"custom"

"full\_egress"

"package\_managers"

type: optional "code\_execution\_domain\_allowlist\_template\_changed"



ChatEnabled object { current\_value, previous\_value, type } 

The chat setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "chat\_enabled"



ClaudeCodeQuickWebSetupEnabled object { current\_value, previous\_value, type } 

The Claude Code quick web setup setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "claude\_code\_quick\_web\_setup\_enabled"



ClaudeCodeTeamMemoryMode object { current\_value, previous\_value, type } 

The Claude Code team memory mode setting was changed for the organization.



current\_value: "all\_org\_members" or "github\_repo" or "off" or "specific\_groups"

Setting value immediately after this change

One of the following:

"all\_org\_members"

"github\_repo"

"off"

"specific\_groups"



previous\_value: "all\_org\_members" or "github\_repo" or "off" or "specific\_groups"

Setting value immediately before this change

One of the following:

"all\_org\_members"

"github\_repo"

"off"

"specific\_groups"

type: optional "claude\_code\_team\_memory\_mode"



BrowserExtensionSettingsUpdated object { current\_value, previous\_value, type } 

The browser extension setting was changed for the organization.

current\_value: map[unknown]

Setting value immediately after this change

previous\_value: map[unknown]

Setting value immediately before this change

type: optional "browser\_extension\_settings"



DesktopExtensionAllowlistEnabled object { current\_value, previous\_value, type } 

The desktop extension allowlist setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "is\_desktop\_extension\_allowlist\_enabled"



ClaudeDesignEnabled object { current\_value, previous\_value, type } 

The Claude Design setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "claude\_ai\_design\_enabled"



ArtifactPublishingEnabled object { current\_value, previous\_value, type } 

The Artifact publishing setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "artifact\_publishing\_enabled"



ClaudeAISkillSharingEnabled object { current\_value, previous\_value, type } 

The Claude.ai skill sharing setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "claude\_ai\_skill\_sharing\_enabled"



ClaudeAISkillSharingOrgEnabled object { current\_value, previous\_value, type } 

The Claude.ai organization-wide skill sharing setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "claude\_ai\_skill\_sharing\_org\_enabled"



ClaudeCodeRemoteControlEnabled object { current\_value, previous\_value, type } 

The Claude Code remote control setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "claude\_code\_remote\_control\_enabled"



ClaudeCodeRemoteControlDefaultEnabled object { current\_value, previous\_value, type } 

The Claude Code remote control auto-enable default was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "claude\_code\_remote\_control\_default\_enabled"



ClaudeCodeRoutinesEnabled object { current\_value, previous\_value, type } 

The Claude Code routines setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "claude\_code\_routines\_enabled"



ClaudeCodeWorkflowsEnabled object { current\_value, previous\_value, type } 

The Claude Code Workflows setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "claude\_code\_workflows\_enabled"



FrontierServicesDataUseEnabled object { current\_value, previous\_value, type } 

The frontier services data use setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "frontier\_services\_data\_use\_enabled"



LtiCourseProjectsEnabled object { current\_value, previous\_value, type } 

The LTI course projects setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "lti\_course\_projects\_enabled"



ClaudeAISkillCreationEnabled object { current\_value, previous\_value, type } 

The Claude.ai skill creation setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "claude\_ai\_skill\_creation\_enabled"



ClaudeCodeGitHubAnalyticsEnabled object { current\_value, previous\_value, type } 

The Claude Code GitHub analytics setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "claude\_code\_github\_analytics\_enabled"



ClaudeCodeHideManagedEnvironments object { current\_value, previous\_value, type } 

The Claude Code hide managed environments setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "claude\_code\_hide\_managed\_environments"



ClaudeCodeMetricsLoggingEnabled object { current\_value, previous\_value, type } 

The Claude Code metrics logging setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "claude\_code\_metrics\_logging\_enabled"



ClaudeCodeFastModeEnabled object { current\_value, previous\_value, type } 

The Claude Code fast mode setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "claude\_code\_fast\_mode\_enabled"



ClaudeCodeTrustedDevicesRequired object { current\_value, previous\_value, type } 

The Claude Code trusted devices setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "claude\_code\_trusted\_devices\_required"



InlineVisualizationsEnabled object { current\_value, previous\_value, type } 

The inline visualizations setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "inline\_visualizations\_enabled"



OrganizationBannerSettingsUpdated object { current\_value, previous\_value, type } 

The organization banner setting was changed.

current\_value: map[unknown]

Setting value immediately after this change

previous\_value: map[unknown]

Setting value immediately before this change

type: optional "organization\_banner\_settings"



ClaudeInSlackSettingsUpdated object { current\_value, previous\_value, type } 

The Claude in Slack setting was changed for the organization.

current\_value: map[unknown]

Setting value immediately after this change

previous\_value: map[unknown]

Setting value immediately before this change

type: optional "claude\_in\_slack\_settings"



ClaudeCodeDefaultWorkerEnvironmentID object { current\_value, previous\_value, type } 

The Claude Code default worker environment setting was changed for the organization.

current\_value: string

Setting value immediately after this change

previous\_value: string

Setting value immediately before this change

type: optional "claude\_code\_default\_worker\_environment\_id"



ClaudeCodeDefaultWorkerPoolID object { current\_value, previous\_value, type } 

The Claude Code default worker pool setting was changed for the organization.

current\_value: string

Setting value immediately after this change

previous\_value: string

Setting value immediately before this change

type: optional "claude\_code\_default\_worker\_pool\_id"



ManagedAgentsEnabled object { current\_value, previous\_value, type } 

The managed agents setting was changed for the organization.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "managed\_agents\_enabled"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_organization\_settings\_updated"



OwnedProjectsAccessRestored object { actor, id, created\_at, 4 more } 

Access to owned projects was restored.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "owned\_projects\_access\_restored"

user\_id: optional string



PaymentMethodUpdated object { actor, id, created\_at, 3 more } 

The organization's default payment method was updated.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "payment\_method\_updated"



PendingShareCreated object { actor, invitee\_email, resource\_id, 7 more } 

A pending share of a project or skill was created for an email address that is not yet an organization member.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

invitee\_email: string

Email address the share was created for.

resource\_id: string

Tagged ID of the resource being shared.

resource\_type: string

The type of resource being shared.

role: string

The role that will be granted when the invitee joins the organization.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "pending\_share\_created"



PendingShareRevoked object { actor, invitee\_email, resource\_id, 6 more } 

A pending share of a project or skill was revoked before the invitee joined the organization.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

invitee\_email: string

Email address the share had been created for.

resource\_id: string

Tagged ID of the resource that was shared.

resource\_type: string

The type of resource that was shared.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "pending\_share\_revoked"



PhoneCodeSent object { actor, id, created\_at, 3 more } 

User requested a phone verification code.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "phone\_code\_sent"



PhoneCodeVerified object { actor, id, created\_at, 3 more } 

User successfully verified their phone code.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "phone\_code\_verified"



PlatformAPIKeyCreated object { actor, api\_key\_id, id, 4 more } 

An API key was created.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

api\_key\_id: string

Tagged ID of the created API key

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_api\_key\_created"



PlatformAPIKeyUpdated object { actor, api\_key\_id, updates, 5 more } 

An API key was updated.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

api\_key\_id: string

Tagged ID of the updated API key



updates: array of object { current\_value, previous\_value, type } 

current\_value: string

previous\_value: string



type: "name" or "status" or "workspace"

One of the following:

"name"

"status"

"workspace"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_api\_key\_updated"



PlatformBillingUpgradedToPrepaid object { actor, previous\_billing\_type, id, 4 more } 

The organization's API billing was upgraded to the prepaid plan.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

previous\_billing\_type: string

The organization's billing type before this upgrade, for example "api\_evaluation".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_billing\_upgraded\_to\_prepaid"



PlatformCostReportViewed object { actor, id, created\_at, 3 more } 

The cost report was viewed.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_cost\_report\_viewed"



PlatformFederatedAuthentication object { actor, id, created\_at, 7 more } 

A federated workload identity attempted to exchange an OIDC token for Anthropic API credentials.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.



event\_data: optional object { federation\_rule\_id, issuer\_id, oidc\_token, requested\_service\_account\_id } 

A nested object within a compliance activity payload.

federation\_rule\_id: optional string

The federation rule that matched the request, e.g. "fdrl\_01HXZ4J2N8K5P7R9T3V6W1Y4M0".

issuer\_id: optional string

The registered identity issuer for the request, e.g. "fdis\_01HXZ4H5M3K8P1R7T9V2W6Y4N0".



oidc\_token: optional object { claims, jti } 

A nested object within a compliance activity payload.

claims: optional map[unknown]

The verified claims from the presented OIDC token.

jti: optional string

The presented token's unique identifier (its `jti` claim).

requested\_service\_account\_id: optional string

The service account the caller requested to authenticate as, e.g. "svac\_01HXZ4...".

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

request\_id: optional string

The Anthropic API request identifier for correlation, e.g. "req\_01HXZ4K7M9P2QR5T8V6W3Y1N0B".



resources: optional array of object { id, type } 

The resources involved in the exchange.

id: string

The identifier of the resource involved in the exchange.

type: string

The kind of resource involved in the exchange.



status: optional object { outcome, detail, reason } 

A nested object within a compliance activity payload.

outcome: string

Whether the token exchange succeeded or was denied.

detail: optional string

A human-readable explanation when the exchange did not succeed.

reason: optional string

A short reason code when the exchange did not succeed.

type: optional "platform\_federated\_authentication"



PlatformFederationIssuerArchived object { actor, federation\_issuer\_id, id, 4 more } 

An OIDC federation issuer was archived.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

federation\_issuer\_id: string

Tagged ID of the archived issuer

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_federation\_issuer\_archived"



PlatformFederationIssuerUpdated object { actor, federation\_issuer\_id, updates, 5 more } 

An OIDC federation issuer was updated.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

federation\_issuer\_id: string

Tagged ID of the updated issuer



updates: array of object { current\_value, previous\_value, type } 

current\_value: string

previous\_value: string



type: "ca\_cert\_pem\_sha256" or "check\_jti" or "discovery\_base" or 7 more

One of the following:

"ca\_cert\_pem\_sha256"

"check\_jti"

"discovery\_base"

"issuer\_url"

"jwks\_keys\_sha256"

"jwks\_polling\_disabled\_at"

"jwks\_source"

"jwks\_url"

"max\_jwt\_lifetime\_seconds"

"name"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_federation\_issuer\_updated"



PlatformFederationRuleArchived object { actor, federation\_rule\_id, id, 4 more } 

An OIDC federation rule was archived.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

federation\_rule\_id: string

Tagged ID of the archived rule

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_federation\_rule\_archived"



PlatformFederationRuleUpdated object { actor, federation\_rule\_id, updates, 5 more } 

An OIDC federation rule was updated.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

federation\_rule\_id: string

Tagged ID of the updated rule



updates: array of object { current\_value, previous\_value, type } 

current\_value: string

previous\_value: string



type: "applies\_to\_all\_workspaces" or "attributes" or "description" or 11 more

One of the following:

"applies\_to\_all\_workspaces"

"attributes"

"description"

"match\_audience"

"match\_claims"

"match\_condition"

"match\_subject\_prefix"

"name"

"oauth\_scope"

"target\_id"

"target\_lookup\_attr"

"target\_type"

"token\_lifetime\_seconds"

"workspace\_id"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_federation\_rule\_updated"



PlatformFederationRuleWorkspaceAdded object { actor, federation\_rule\_id, workspace\_id, 5 more } 

A federation rule was enabled for a workspace.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

federation\_rule\_id: string

Tagged ID of the federation rule

workspace\_id: string

Tagged ID of the workspace the rule was enabled for

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_federation\_rule\_workspace\_added"



PlatformFederationRuleWorkspaceRemoved object { actor, federation\_rule\_id, workspace\_id, 5 more } 

A federation rule was disabled for a workspace.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

federation\_rule\_id: string

Tagged ID of the federation rule

workspace\_id: string

Tagged ID of the workspace the rule was disabled for

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_federation\_rule\_workspace\_removed"



PlatformFileContentDownloaded object { actor, file\_id, id, 4 more } 

Activity logged when file content is downloaded via GET /v1/files/{file\_id}/content.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

file\_id: string

The tagged ID of the downloaded file

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_file\_content\_downloaded"



PlatformFileDeleted object { actor, file\_id, id, 4 more } 

Activity logged when a file is deleted via DELETE /v1/files/{file\_id}.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

file\_id: string

The tagged ID of the deleted file

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_file\_deleted"



PlatformFileUploaded object { actor, file\_id, id, 5 more } 

Activity logged when a file is uploaded via POST /v1/files.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

file\_id: string

The tagged ID of the uploaded file

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

session\_id: optional string

The tagged session ID (agent-api only)

type: optional "platform\_file\_uploaded"



PlatformPluginDirectorySubmissionCreated object { actor, plugin\_name, submission\_id, 5 more } 

A plugin directory submission was created on the API platform. A plugin directory submission is a request to list a plugin in the public plugin directory.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

plugin\_name: string

The name of the plugin being submitted.

submission\_id: string

The submission that was created, e.g. "psub\_01HX...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_plugin\_directory\_submission\_created"



PlatformPluginDirectorySubmissionDeleted object { actor, submission\_id, id, 4 more } 

A plugin directory submission was deleted on the API platform.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

submission\_id: string

The submission that was deleted, e.g. "psub\_01HX...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_plugin\_directory\_submission\_deleted"



PlatformPluginDirectorySubmissionUpdated object { actor, status, submission\_id, 5 more } 

A plugin directory submission was updated on the API platform.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

status: string

The submission's status after the update.

submission\_id: string

The submission that was updated, e.g. "psub\_01HX...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_plugin\_directory\_submission\_updated"



PlatformServiceAccountArchived object { actor, service\_account\_id, id, 4 more } 

A service account was archived.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

service\_account\_id: string

Tagged ID of the archived service account

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_service\_account\_archived"



PlatformServiceAccountUpdated object { actor, service\_account\_id, updates, 5 more } 

A service account was updated.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

service\_account\_id: string

Tagged ID of the updated service account



updates: array of object { current\_value, previous\_value, type } 

current\_value: string

previous\_value: string



type: "description" or "organization\_role"

One of the following:

"description"

"organization\_role"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_service\_account\_updated"



PlatformServiceAccountWorkspaceMemberAdded object { actor, service\_account\_id, workspace\_id, 5 more } 

A service account was added as a member of a workspace.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

service\_account\_id: string

Tagged ID of the service account

workspace\_id: string

Tagged ID of the workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_service\_account\_workspace\_member\_added"



PlatformServiceAccountWorkspaceMemberRemoved object { actor, service\_account\_id, workspace\_id, 5 more } 

A service account was removed from a workspace.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

service\_account\_id: string

Tagged ID of the service account

workspace\_id: string

Tagged ID of the workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_service\_account\_workspace\_member\_removed"



PlatformServiceAccountWorkspaceMemberUpdated object { actor, service\_account\_id, updates, 6 more } 

A service account's workspace membership role was updated.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

service\_account\_id: string

Tagged ID of the service account



updates: array of object { current\_value, previous\_value, type } 

current\_value: string

previous\_value: string

type: "workspace\_role"

workspace\_id: string

Tagged ID of the workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_service\_account\_workspace\_member\_updated"



PlatformSigningKeyCreated object { actor, algorithm, key\_backing\_type, 7 more } 

Activity logged when a new request-signing key is registered for the org.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

algorithm: string

The signing algorithm (e.g. ecdsa-p256-sha256)

key\_backing\_type: string

The backing type of the key (IN\_MEMORY or CLOUD\_KMS)

signing\_key\_id: string

The tagged ID of the created signing key

status: string

The initial status of the key (ACTIVE or PENDING)

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_signing\_key\_created"



PlatformSigningKeyDeleted object { actor, algorithm, key\_backing\_type, 7 more } 

Activity logged when a signing key is permanently deleted.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

algorithm: string

The algorithm of the deleted key

key\_backing\_type: string

The backing type of the deleted key (IN\_MEMORY or CLOUD\_KMS)

key\_name: string

The name of the deleted key

signing\_key\_id: string

The tagged ID of the deleted signing key

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_signing\_key\_deleted"



PlatformSigningKeyRotated object { actor, algorithm, key\_group\_identifier, 7 more } 

Activity logged when an in-memory signing key is rotated.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

algorithm: string

The algorithm of the new key

key\_group\_identifier: string

The key group identifier linking old and new keys

new\_signing\_key\_id: string

The tagged ID of the newly created key

old\_signing\_key\_id: string

The tagged ID of the expired old key

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_signing\_key\_rotated"



PlatformSkillVersionCreated object { actor, skill\_id, version, 5 more } 

Activity logged when a skill version is created via POST /v1/skills/{skill\_id}/versions.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

skill\_id: string

The tagged ID of the skill

version: string

The version number of the created version

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_skill\_version\_created"



PlatformSkillVersionDeleted object { actor, skill\_id, version, 5 more } 

Activity logged when a skill version is deleted via DELETE /v1/skills/{skill\_id}/versions/{version}.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

skill\_id: string

The tagged ID of the skill

version: string

The version number of the deleted version

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_skill\_version\_deleted"



PlatformSpendLimitAlertEmailsUpdated object { actor, id, alert\_emails, 5 more } 

Spend limit alert email addresses and role targets were updated for an org.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

alert\_emails: optional array of string

Updated list of alert email addresses.

alerted\_roles: optional array of string

Updated list of alerted roles.

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_spend\_limit\_alert\_emails\_updated"



PlatformSpendLimitCreated object { actor, id, created\_at, 5 more } 

An org-level fixed-dollar spend limit was created.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

limit\_action: optional string

The action taken when the limit is reached (notify\_only or notify\_and\_pause).

limit\_usd: optional number

The spend limit threshold in USD cents.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_spend\_limit\_created"



PlatformSpendLimitDeleted object { actor, id, created\_at, 4 more } 

An org-level spend limit was removed.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

spend\_limit\_id: optional string

UUID of the deleted spend limit.

type: optional "platform\_spend\_limit\_deleted"



PlatformSpendLimitUpdated object { actor, id, created\_at, 5 more } 

An org-level spend limit snooze/ignore state was changed.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

ignore: optional boolean

Whether the limit is being snoozed (ignored).

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

spend\_limit\_id: optional string

UUID of the spend limit.

type: optional "platform\_spend\_limit\_updated"



PlatformUsageReportClaudeCodeViewed object { actor, id, created\_at, 3 more } 

The Claude Code usage report was viewed.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_usage\_report\_claude\_code\_viewed"



PlatformUsageReportMessagesViewed object { actor, id, created\_at, 3 more } 

The messages usage report was viewed.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_usage\_report\_messages\_viewed"



PlatformWorkspaceArchived object { actor, workspace\_id, id, 4 more } 

A workspace was archived.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

workspace\_id: string

Tagged ID of the archived workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_workspace\_archived"



PlatformWorkspaceCreated object { actor, workspace\_id, id, 4 more } 

A workspace was created.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

workspace\_id: string

Tagged ID of the created workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_workspace\_created"



PlatformWorkspaceMemberAdded object { actor, user\_id, workspace\_id, 5 more } 

A member was added to a workspace.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

user\_id: string

Tagged ID of the added member

workspace\_id: string

Tagged ID of the workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_workspace\_member\_added"



PlatformWorkspaceMemberRemoved object { actor, user\_id, workspace\_id, 5 more } 

A member was removed from a workspace.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

user\_id: string

Tagged ID of the removed member

workspace\_id: string

Tagged ID of the workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_workspace\_member\_removed"



PlatformWorkspaceMemberUpdated object { actor, updates, user\_id, 6 more } 

A workspace member was updated.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



updates: array of object { current\_value, previous\_value, type } 

current\_value: string

previous\_value: string

type: "workspace\_role"

user\_id: string

Tagged ID of the updated member

workspace\_id: string

Tagged ID of the workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_workspace\_member\_updated"



PlatformWorkspaceMemberViewed object { actor, user\_id, workspace\_id, 5 more } 

A workspace member was viewed.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

user\_id: string

Tagged ID of the viewed member

workspace\_id: string

Tagged ID of the workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_workspace\_member\_viewed"



PlatformWorkspaceMembersListed object { actor, workspace\_id, id, 4 more } 

Workspace members were listed.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"

workspace\_id: string

Tagged ID of the workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_workspace\_members\_listed"



PlatformWorkspaceRateLimitDeleted object { actor, limiter\_type, model\_group, 6 more } 

A workspace rate limit was deleted.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

limiter\_type: string

Type of rate limiter

model\_group: string

Model group the rate limit applied to

workspace\_id: string

Tagged ID of the workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_workspace\_rate\_limit\_deleted"



PlatformWorkspaceRateLimitUpdated object { actor, limiter\_type, model\_group, 7 more } 

A workspace rate limit was created or updated.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

limiter\_type: string

Type of rate limiter

model\_group: string

Model group the rate limit applies to

value: number

New rate limit value

workspace\_id: string

Tagged ID of the workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_workspace\_rate\_limit\_updated"



PlatformWorkspaceUpdated object { actor, updates, workspace\_id, 5 more } 

A workspace was updated.



actor: object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, service\_account\_id, user\_agent, type } 

One of the following:



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



updates: array of object { current\_value, previous\_value, type } 

current\_value: string

previous\_value: string



type: "allowed\_inference\_geos" or "default\_inference\_geo" or "display\_color" or 3 more

The workspace property that was changed

One of the following:

"allowed\_inference\_geos"

"default\_inference\_geo"

"display\_color"

"external\_key\_config\_id"

"inference\_data\_retention"

"name"

workspace\_id: string

Tagged ID of the updated workspace

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "platform\_workspace\_updated"



ClaudePluginCreated object { actor, id, created\_at, 5 more } 

Plugin was created.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

plugin\_id: optional string

plugin\_name: optional string

type: optional "claude\_plugin\_created"



ClaudePluginDeleted object { actor, id, created\_at, 5 more } 

Plugin was deleted.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

plugin\_id: optional string

plugin\_name: optional string

type: optional "claude\_plugin\_deleted"



PluginInstallationPreferenceUpdated object { actor, marketplace\_id, plugin\_name, 9 more } 

An org admin changed the installation preference for a plugin.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

marketplace\_id: string

Marketplace ID

plugin\_name: string

Plugin name

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

action: optional string

Action taken (e.g. 'deleted' for clearing an override)

created\_at: optional string

When this activity occurred.

group\_id: optional string

Tagged group ID for group-level overrides (null for org-level)

group\_name: optional string

Group name for group-level overrides

installation\_preference: optional string

New installation preference value (set only when action is an update; null for delete actions)

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "plugin\_installation\_preference\_updated"



ClaudePluginReplaced object { actor, id, created\_at, 5 more } 

Plugin was replaced.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

plugin\_id: optional string

plugin\_name: optional string

type: optional "claude\_plugin\_replaced"



ClaudePluginUpdated object { actor, id, created\_at, 5 more } 

Plugin was updated.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

plugin\_id: optional string

plugin\_name: optional string

type: optional "claude\_plugin\_updated"



PrepaidAutoRechargeDisabled object { actor, id, created\_at, 3 more } 

Auto-recharge was disabled for API prepaid org.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "prepaid\_auto\_recharge\_disabled"



PrepaidAutoRechargeUpdated object { actor, id, created\_at, 5 more } 

Auto-recharge settings were updated for API prepaid org.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

target\_amount: optional number

Target recharge amount in minor units.

threshold\_amount: optional number

Threshold amount to trigger recharge in minor units.

type: optional "prepaid\_auto\_recharge\_updated"



PrepaidExtraUsageAutoReloadDisabled object { actor, id, created\_at, 3 more } 

Prepaid usage credit auto-reload was disabled.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "prepaid\_extra\_usage\_auto\_reload\_disabled"



PrepaidExtraUsageAutoReloadEnabled object { actor, id, created\_at, 3 more } 

Prepaid usage credit auto-reload was enabled.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "prepaid\_extra\_usage\_auto\_reload\_enabled"



PrepaidExtraUsageAutoReloadSettingsUpdated object { actor, id, created\_at, 3 more } 

Prepaid usage credit auto-reload settings were updated.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "prepaid\_extra\_usage\_auto\_reload\_settings\_updated"



PrimaryOwnerTransferred object { actor, new\_owner\_id, previous\_owner\_id, 5 more } 

Primary owner role was transferred to another org member.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

new\_owner\_id: string

previous\_owner\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "primary\_owner\_transferred"



ClaudeProjectArchived object { actor, claude\_project\_id, id, 4 more } 

A Claude project was archived.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_project\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_project\_archived"



ClaudeProjectCreated object { actor, claude\_project\_id, id, 4 more } 

A Claude project was created.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_project\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_project\_created"



ClaudeProjectDeleted object { actor, claude\_project\_id, id, 4 more } 

A Claude project was deleted.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_project\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_project\_deleted"



ClaudeProjectDocumentAccessFailed object { actor, claude\_project\_document\_id, claude\_project\_id, 6 more } 

An attempt to access a document in a Claude project failed.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

claude\_project\_document\_id: string

claude\_project\_id: string

filename: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_project\_document\_access\_failed"



ClaudeProjectDocumentBulkDeletionAuditTruncated object { actor, audited\_count, claude\_project\_id, 6 more } 

A bulk request to delete documents from a Claude project failed with more documents requested than were individually recorded in the audit log.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

audited\_count: number

Number of documents that received an individual audit record.

claude\_project\_id: string

requested\_count: number

Total number of documents the request asked to delete.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_project\_document\_bulk\_deletion\_audit\_truncated"



ClaudeProjectDocumentDeleted object { actor, claude\_project\_document\_id, claude\_project\_id, 6 more } 

A document was deleted from a Claude project.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_project\_document\_id: string

claude\_project\_id: string

filename: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_project\_document\_deleted"



ClaudeProjectDocumentDeletionFailed object { actor, claude\_project\_document\_id, claude\_project\_id, 6 more } 

A request to delete a document from a Claude project failed.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

claude\_project\_document\_id: string

claude\_project\_id: string

filename: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_project\_document\_deletion\_failed"



ClaudeProjectDocumentUpdated object { actor, claude\_project\_document\_id, claude\_project\_id, 6 more } 

The content of a document in a Claude project was replaced in place.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_project\_document\_id: string

claude\_project\_id: string

filename: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_project\_document\_updated"



ClaudeProjectDocumentUploaded object { actor, claude\_project\_document\_id, claude\_project\_id, 6 more } 

A document was uploaded to a Claude project.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_project\_document\_id: string

claude\_project\_id: string

filename: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_project\_document\_uploaded"



ClaudeProjectDocumentViewed object { actor, claude\_project\_document\_id, claude\_project\_id, 6 more } 

A document in a Claude project was viewed.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_project\_document\_id: string

claude\_project\_id: string

filename: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_project\_document\_viewed"



ClaudeProjectFileAccessFailed object { actor, claude\_file\_id, claude\_project\_id, 5 more } 

An attempt to access a file in a Claude project failed.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

claude\_file\_id: string

claude\_project\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_project\_file\_access\_failed"



ClaudeProjectFileBulkDeletionAuditTruncated object { actor, audited\_count, claude\_project\_id, 6 more } 

A bulk request to delete files from a Claude project failed with more files requested than were individually recorded in the audit log.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

audited\_count: number

Number of files that received an individual audit record.

claude\_project\_id: string

requested\_count: number

Total number of files the request asked to delete.

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_project\_file\_bulk\_deletion\_audit\_truncated"



ClaudeProjectFileDeleted object { actor, claude\_file\_id, claude\_project\_id, 5 more } 

A file was deleted from a Claude project.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

claude\_file\_id: string

claude\_project\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_project\_file\_deleted"



ClaudeProjectFileDeletionFailed object { actor, claude\_file\_id, claude\_project\_id, 5 more } 

A request to delete a file from a Claude project failed.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

claude\_file\_id: string

claude\_project\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_project\_file\_deletion\_failed"



ClaudeProjectFileUploaded object { actor, claude\_file\_id, claude\_project\_id, 6 more } 

A file was uploaded to a Claude project.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

claude\_file\_id: string

claude\_project\_id: string

filename: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_project\_file\_uploaded"



ClaudeProjectReported object { actor, claude\_project\_id, id, 4 more } 

A Claude project was reported.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_project\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_project\_reported"



ClaudeProjectSharingUpdated object { actor, audience, claude\_project\_id, 5 more } 

A Claude project's sharing settings were updated.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



audience: array of object { type }  or object { type } 

Sharing audience for the project. If empty, this it's only visible to the creating user.

One of the following:



ProjectSharingAudiencePublic object { type } 

type: optional "public"



ProjectSharingAudienceOrganization object { type } 

type: optional "organization"

claude\_project\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_project\_sharing\_updated"



ClaudeProjectViewed object { actor, claude\_project\_id, id, 5 more } 

A Claude project was viewed.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

claude\_project\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

preview\_only: optional boolean

type: optional "claude\_project\_viewed"



ClaudePubsecIdentityConfigured object { actor, idp\_saml\_config\_updated, magic\_link\_toggled, 6 more } 

SAML IdP configuration updated for a public sector organization.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

idp\_saml\_config\_updated: boolean

magic\_link\_toggled: boolean

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

magic\_link\_enabled: optional boolean

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_pubsec\_identity\_configured"



RbacRoleAssigned object { actor, principal\_id, principal\_type, 6 more } 

Admin assigned an RBAC custom role to a principal.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

principal\_id: string

Tagged ID of the principal

principal\_type: string

Type of principal: account or group

role\_id: string

Tagged ID of the role

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "rbac\_role\_assigned"



RbacRoleCreated object { actor, role\_id, role\_name, 5 more } 

Admin created an RBAC custom role.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

role\_id: string

Tagged ID of the created role

role\_name: string

Name of the created role

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "rbac\_role\_created"



RbacRoleDeleted object { actor, role\_id, id, 4 more } 

Admin deleted an RBAC custom role.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

role\_id: string

Tagged ID of the deleted role

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "rbac\_role\_deleted"



RbacRolePermissionAdded object { action, actor, resource\_id, 7 more } 

Admin added a permission to an RBAC custom role.

Emitted once per requested permission, including permissions the role
already had, so a retried request still produces a complete audit record.

action: string

Action permitted on the resource



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

resource\_id: string

ID of the resource

resource\_type: string

Type of resource the permission applies to

role\_id: string

Tagged ID of the role

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "rbac\_role\_permission\_added"



RbacRolePermissionRemoved object { action, actor, resource\_id, 7 more } 

Admin removed a permission from an RBAC custom role.

Emitted once per requested permission, including permissions the role
already lacked, so a retried request still produces a complete audit
record.

action: string

Action that was permitted on the resource



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

resource\_id: string

ID of the resource

resource\_type: string

Type of resource the permission applied to

role\_id: string

Tagged ID of the role

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "rbac\_role\_permission\_removed"



RbacRoleUnassigned object { actor, principal\_id, principal\_type, 6 more } 

Admin unassigned an RBAC custom role from a principal.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

principal\_id: string

Tagged ID of the principal

principal\_type: string

Type of principal: account or group

role\_id: string

Tagged ID of the role

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "rbac\_role\_unassigned"



RbacRoleUpdated object { actor, role\_id, id, 4 more } 

Admin updated an RBAC custom role.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

role\_id: string

Tagged ID of the updated role

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "rbac\_role\_updated"



RoleAssignmentGranted object { actor, id, created\_at, 8 more } 

Role assignment was granted.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

resource\_id: optional string

resource\_type: optional string

role: optional string

target\_id: optional string

target\_type: optional string

type: optional "role\_assignment\_granted"



RoleAssignmentRevoked object { actor, id, created\_at, 8 more } 

Role assignment was revoked.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { email\_address, type } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

resource\_id: optional string

resource\_type: optional string

role: optional string

target\_id: optional string

target\_type: optional string

type: optional "role\_assignment\_revoked"



SSOLoginFailed object { actor, id, created\_at, 3 more } 

An SSO sign-in attempt failed.



actor: object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "sso\_login\_failed"



SSOLoginInitiated object { actor, id, created\_at, 3 more } 

A user started an SSO sign-in flow.



actor: object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "sso\_login\_initiated"



SSOLoginSucceeded object { actor, id, auth\_method, 5 more } 

A user successfully signed in with SSO.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

auth\_method: optional "sso"

The method the user used to authenticate. May be absent on activities recorded before this field was introduced.

created\_at: optional string

When this activity occurred.

mfa\_method: optional "not\_used"

The second authentication factor performed during this login, if any. `null` when the second-factor status is not recorded on this event — for example, when authentication was delegated to an external identity provider and any second factor is not visible to Anthropic, or when this event is one step of a multi-step login whose MFA is reported on another activity. May be absent on activities recorded before this field was introduced.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "sso\_login\_succeeded"



SSOSecondFactorMagicLink object { actor, id, created\_at, 3 more } 

SSO second factor magic link was used.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "sso\_second\_factor\_magic\_link"



ScimUserCreated object { actor, user\_id, id, 4 more } 

A SCIM user was provisioned.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

user\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "scim\_user\_created"



ScimUserDeleted object { actor, user\_id, id, 4 more } 

A SCIM user was deleted.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

user\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "scim\_user\_deleted"



ScimUserUpdated object { actor, user\_id, id, 4 more } 

A SCIM user was updated.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

user\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "scim\_user\_updated"



ScopedAPIKeyDeleted object { actor, api\_key\_id, api\_key\_name, 6 more } 

A scoped API key was deleted.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

api\_key\_id: string

Tagged ID of the deleted scoped API key

api\_key\_name: string

Name of the deleted scoped API key

scopes: array of string

Scopes the deleted key had

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "scoped\_api\_key\_deleted"



ScopedAPIKeyUpdated object { actor, api\_key\_id, updates, 5 more } 

A scoped API key was renamed or its activation state changed.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

api\_key\_id: string

Tagged ID of the updated scoped API key



updates: array of object { current\_value, previous\_value, type } 

current\_value: string

previous\_value: string



type: "activation\_state" or "name"

One of the following:

"activation\_state"

"name"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "scoped\_api\_key\_updated"



SeatTierChangesCancelled object { actor, id, created\_at, 3 more } 

Scheduled seat tier downgrades were cancelled.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "seat\_tier\_changes\_cancelled"



SeatTiersPurchased object { actor, id, created\_at, 4 more } 

Seat tiers were purchased or upgraded on a subscription.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

item\_allocations: optional map[number]

Desired seat tier allocations (item type to quantity).

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "seat\_tiers\_purchased"



ServiceCreated object { actor, service\_name, id, 4 more } 

Activity logged when an org service is explicitly created.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

service\_name: string

The org service name (e.g., 'external

')

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "service\_created"



ServiceDeleted object { actor, service\_name, id, 4 more } 

Activity logged when an org service is deleted.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

service\_name: string

The org service name (e.g., 'external

')

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "service\_deleted"



ServiceKeyCreated object { actor, is\_service\_created, key\_name, 8 more } 

Activity logged when a new org service key is created.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

is\_service\_created: boolean

Whether the org service was implicitly created in this request

key\_name: string

The human-readable name of the key

service\_name: string

The service name this key belongs to

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

scopes: optional array of string

The scopes granted to this service key

service\_key\_id: optional string

The ID of the created service key

type: optional "service\_key\_created"



ServiceKeyRevoked object { actor, service\_key\_id, service\_name, 5 more } 

Activity logged when an org service key is revoked.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

service\_key\_id: string

The tagged ID of the revoked service key

service\_name: string

The service name this key belongs to

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "service\_key\_revoked"



SessionRevoked object { actor, id, created\_at, 3 more } 

User revoked a specific session.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "session\_revoked"



SessionShareAccessed object { actor, id, created\_at, 4 more } 

Session share was accessed.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

share\_id: optional string

type: optional "session\_share\_accessed"



SessionShareCreated object { actor, id, created\_at, 4 more } 

Session share was created.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

share\_id: optional string

type: optional "session\_share\_created"



SessionShareRevoked object { actor, id, created\_at, 4 more } 

Session share was revoked.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

share\_id: optional string

type: optional "session\_share\_revoked"



ClaudeSkillCreated object { actor, id, created\_at, 5 more } 

Skill was created.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

skill\_id: optional string

skill\_name: optional string

type: optional "claude\_skill\_created"



ClaudeSkillDeleted object { actor, id, created\_at, 5 more } 

Skill was deleted.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

skill\_id: optional string

skill\_name: optional string

type: optional "claude\_skill\_deleted"



ClaudeSkillDisabled object { actor, id, created\_at, 5 more } 

User disabled a skill for their account.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

skill\_id: optional string

skill\_name: optional string

type: optional "claude\_skill\_disabled"



ClaudeSkillEnabled object { actor, id, created\_at, 5 more } 

User enabled a skill for their account.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

skill\_id: optional string

skill\_name: optional string

type: optional "claude\_skill\_enabled"



ClaudeSkillReplaced object { actor, id, created\_at, 5 more } 

Skill was replaced.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

skill\_id: optional string

skill\_name: optional string

type: optional "claude\_skill\_replaced"



SocialLoginSucceeded object { actor, provider, id, 6 more } 

A user successfully signed in with a social identity provider (Google, Apple, or Microsoft).



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



provider: "apple" or "google" or "microsoft"

One of the following:

"apple"

"google"

"microsoft"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

auth\_method: optional "social"

The method the user used to authenticate. May be absent on activities recorded before this field was introduced.

created\_at: optional string

When this activity occurred.

mfa\_method: optional "not\_used"

The second authentication factor performed during this login, if any. `null` when the second-factor status is not recorded on this event — for example, when authentication was delegated to an external identity provider and any second factor is not visible to Anthropic, or when this event is one step of a multi-step login whose MFA is reported on another activity. May be absent on activities recorded before this field was introduced.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "social\_login\_succeeded"



StepUpAuthenticationFailed object { actor, method, reason, 6 more } 

An additional identity check failed.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string



method: "device\_key" or "unspecified" or "webauthn"

The verification method the user attempted.

One of the following:

"device\_key"

"unspecified"

"webauthn"



reason: "challenge\_rejected" or "unspecified" or "verification\_failed"

Why the attempt failed.

One of the following:

"challenge\_rejected"

"unspecified"

"verification\_failed"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

trusted\_device\_id: optional string

Identifier of the trusted device the attempt referenced, e.g. "tdev\_...". Present only for the device key method.

type: optional "step\_up\_authentication\_failed"



StepUpAuthenticationSucceeded object { actor, method, id, 5 more } 

The user completed an additional identity check to confirm a sensitive action.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string



method: "device\_key" or "unspecified" or "webauthn"

The verification method the user completed.

One of the following:

"device\_key"

"unspecified"

"webauthn"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

trusted\_device\_id: optional string

Identifier of the trusted device used, e.g. "tdev\_...". Present only for the device key method.

type: optional "step\_up\_authentication\_succeeded"



StepUpCredentialEnrolled object { actor, credential\_id, id, 4 more } 

A user enrolled a passkey for confirming sensitive actions on their account.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

credential\_id: string

Identifier of the enrolled credential, e.g. "sucr\_...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "step\_up\_credential\_enrolled"



SubscriptionCancellationScheduled object { actor, id, created\_at, 3 more } 

Subscription cancellation was scheduled at end of billing period.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "subscription\_cancellation\_scheduled"



SubscriptionQuantityUpdated object { actor, added\_seats, new\_quantity, 6 more } 

Contracted subscription seat quantity was updated.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

added\_seats: number

new\_quantity: number

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

previous\_quantity: optional number

type: optional "subscription\_quantity\_updated"



SubscriptionRenewed object { actor, id, billing\_interval, 5 more } 

A cancelled subscription was renewed.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

billing\_interval: optional string

Billing interval (e.g. monthly, annual).

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

plan\_type: optional string

Plan type being renewed into (e.g. team).

type: optional "subscription\_renewed"



SubscriptionResumed object { actor, id, created\_at, 3 more } 

A scheduled subscription cancellation was reversed.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "subscription\_resumed"



SubscriptionStarted object { actor, id, billing\_interval, 6 more } 

A new subscription was created (Team or Enterprise).



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

billing\_interval: optional string

Billing interval (e.g. monthly, annual).

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

plan\_type: optional string

Type of subscription started (e.g. team, enterprise).

seat\_count: optional number

Number of seats purchased.

type: optional "subscription\_started"



SubscriptionUpgraded object { actor, id, created\_at, 5 more } 

Subscription plan was upgraded (e.g. Team to Enterprise).



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

new\_plan: optional string

New plan type after upgrade.

old\_plan: optional string

Previous plan type.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "subscription\_upgraded"



TrustedDeviceCredentialRotated object { actor, trusted\_device\_id, id, 4 more } 

The identity-verification credential of a trusted device was rotated to a new key.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

trusted\_device\_id: string

Identifier of the device whose credential was rotated, e.g. "tdev\_...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "trusted\_device\_credential\_rotated"



TrustedDeviceEnrolled object { actor, enrollment\_method, platform, 6 more } 

A device was enrolled as a trusted device for the user's account. Trusted devices can be used to confirm the user's identity for sensitive actions.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string



enrollment\_method: "oauth" or "session" or "unspecified"

How the user confirmed their identity when enrolling the device.

One of the following:

"oauth"

"session"

"unspecified"



platform: "android" or "claude\_in\_slack" or "desktop\_app" or 4 more

The kind of client the enrollment request came from.

One of the following:

"android"

"claude\_in\_slack"

"desktop\_app"

"ios"

"unspecified"

"web\_claude\_ai"

"web\_console"

trusted\_device\_id: string

Identifier of the device that was enrolled, e.g. "tdev\_...".

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "trusted\_device\_enrolled"



TrustedDeviceRevoked object { actor, reason, id, 6 more } 

A trusted device was removed from the user's account.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string



reason: "org\_member\_removed" or "superseded" or "unspecified" or "user\_revoked"

Why the device trust was removed.

One of the following:

"org\_member\_removed"

"superseded"

"unspecified"

"user\_revoked"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

revoked\_count: optional number

Number of devices removed. Set when a security action removed all of the user's trusted devices at once; absent when a single device was removed (see trusted\_device\_id).

trusted\_device\_id: optional string

Identifier of the device that was removed, e.g. "tdev\_...". Set when a single device was removed; absent when several devices were removed at once (see revoked\_count).

type: optional "trusted\_device\_revoked"



TunnelArchived object { actor, tunnel\_id, id, 4 more } 

An MCP tunnel was archived.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

tunnel\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "tunnel\_archived"



TunnelCertificateAdded object { actor, certificate\_id, tunnel\_id, 6 more } 

An inner-TLS CA certificate was added to a tunnel.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

certificate\_id: string

tunnel\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

certificate\_fingerprint: optional string

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "tunnel\_certificate\_added"



TunnelCertificateRevoked object { actor, certificate\_id, tunnel\_id, 6 more } 

An inner-TLS CA certificate was revoked from a tunnel.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

certificate\_id: string

tunnel\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

certificate\_fingerprint: optional string

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "tunnel\_certificate\_revoked"



TunnelCreated object { actor, tunnel\_id, id, 4 more } 

An MCP tunnel was created.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

tunnel\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "tunnel\_created"



TunnelTokenMinted object { actor, token\_id, id, 5 more } 

An OAuth bearer token for the tunnel management API was minted.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

token\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

token\_name: optional string

type: optional "tunnel\_token\_minted"



TunnelTokenRevealed object { actor, tunnel\_id, tunnel\_token\_id, 5 more } 

The Cloudflare connector secret for a tunnel was revealed to the caller.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

tunnel\_id: string

tunnel\_token\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "tunnel\_token\_revealed"



TunnelTokenRevoked object { actor, token\_id, id, 4 more } 

An OAuth bearer token for the tunnel management API was revoked.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

token\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "tunnel\_token\_revoked"



TunnelTokenRotated object { actor, tunnel\_id, tunnel\_token\_id, 6 more } 

The Cloudflare connector secret for a tunnel was rotated.

`tunnel_token_id` is the id of the *newly-issued* token. The previous
token is invalidated by the rotation and its id is not recorded here.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

tunnel\_id: string

tunnel\_token\_id: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

reason: optional string

type: optional "tunnel\_token\_rotated"



UserConsentRecorded object { actor, consent\_type, entity\_id, 6 more } 

User granted a consent for a specific entity (e.g. consumer health consent for an MCP server).



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

consent\_type: string

entity\_id: string

entity\_type: string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "user\_consent\_recorded"



UserConsentRevoked object { actor, id, consent\_id, 7 more } 

User revoked a previously granted consent for a specific entity.



actor: object { api\_key\_id, ip\_address, user\_agent, type }  or object { email\_address, ip\_address, user\_agent, 2 more }  or object { ip\_address, user\_agent, type, unauthenticated\_email\_address }  or 6 more

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

One of the following:



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



UnauthenticatedUserActor object { ip\_address, user\_agent, type, unauthenticated\_email\_address } 

ip\_address: string

user\_agent: string

type: optional "unauthenticated\_user\_actor"

unauthenticated\_email\_address: optional string



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"



SystemActor object { service, type } 

Automated background processing performed by Anthropic systems, acting
without a user or customer credential.

service: optional string

Name of the automated process that performed the action, when known.

type: optional "system\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



ScimDirectorySyncActor object { directory\_id, workos\_event\_id, idp\_connection\_type, type } 

directory\_id: string

workos\_event\_id: string

idp\_connection\_type: optional string

type: optional "scim\_directory\_sync\_actor"



FederatedIdentityActor object { issuer, subject, audience, 3 more } 

A federated external workload authenticated via a verified OIDC token.

Carries the verified issuer, subject, and audience claims from the
presented JWT.

issuer: string

subject: string

audience: optional array of string

ip\_address: optional string

type: optional "federated\_identity\_actor"

user\_agent: optional string

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

consent\_id: optional string

consent\_type: optional string

created\_at: optional string

When this activity occurred.

entity\_id: optional string

entity\_type: optional string

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "user\_consent\_revoked"



ClaudeUserRoleUpdated object { actor, current\_role, previous\_role, 7 more } 

A user's role within the organization was changed, or the user was added to or removed from the organization.



actor: object { email\_address, ip\_address, user\_agent, 2 more }  or object { admin\_api\_key\_id, ip\_address, user\_agent, type }  or object { api\_key\_id, ip\_address, user\_agent, type }  or 2 more

One of the following:



UserActor object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



AdminAPIKeyActor object { admin\_api\_key\_id, ip\_address, user\_agent, type } 

admin\_api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "admin\_api\_key\_actor"



APIActor object { api\_key\_id, ip\_address, user\_agent, type } 

api\_key\_id: string

ip\_address: string

user\_agent: string

type: optional "api\_actor"



ServiceAccountActor object { ip\_address, service\_account\_id, user\_agent, type } 

ip\_address: string

service\_account\_id: string

user\_agent: string

type: optional "service\_account\_actor"



AnthropicActor object { email\_address, type } 

email\_address: optional string

type: optional "anthropic\_actor"

current\_role: string

If null, then user was removed from the Organization

previous\_role: string

If null, then user was added to the Organization

user\_email: string

Email of the user whose role was changed

user\_id: string

ID of the user whose role was changed

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_user\_role\_updated"



ClaudeUserSettingsUpdated object { actor, updates, id, 4 more } 

User updated their personal settings.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"



updates: array of object { current\_value, previous\_value, type }  or object { current\_value, previous\_value, type }  or object { current\_value, previous\_value, type }  or 19 more

One of the following:



FullName object { current\_value, previous\_value, type } 

current\_value: string

previous\_value: string

type: optional "full\_name"



DisplayName object { current\_value, previous\_value, type } 

current\_value: string

previous\_value: string

type: optional "display\_name"



ArtifactsEnabled object { current\_value, previous\_value, type } 

current\_value: boolean

previous\_value: boolean

type: optional "artifacts\_enabled"



LatexEnabled object { current\_value, previous\_value, type } 

current\_value: boolean

previous\_value: boolean

type: optional "latex\_enabled"



AnalysisToolEnabled object { current\_value, previous\_value, type } 

current\_value: boolean

previous\_value: boolean

type: optional "analysis\_tool\_enabled"



ChatSuggestionsEnabled object { current\_value, previous\_value, type } 

current\_value: boolean

previous\_value: boolean

type: optional "chat\_suggestions\_enabled"



MultimodalPdfsEnabled object { current\_value, previous\_value, type } 

current\_value: boolean

previous\_value: boolean

type: optional "multimodal\_pdfs\_enabled"



GDriveEnabled object { current\_value, previous\_value, type } 

current\_value: boolean

previous\_value: boolean

type: optional "gdrive\_enabled"



WebSearchEnabled object { current\_value, previous\_value, type } 

The web search setting was changed.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "web\_search\_enabled"



GeolocationEnabled object { current\_value, previous\_value, type } 

The geolocation setting was changed.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "geolocation\_enabled"



UserMemoryEnabledSetting object { current\_value, previous\_value, type } 

current\_value: boolean

previous\_value: boolean

type: optional "enabled\_saffron"



McpToolsEnabled object { current\_value, previous\_value, type } 

current\_value: map[boolean]

previous\_value: map[boolean]

type: optional "mcp\_tools\_enabled"



CliOpPermissionsEnabled object { current\_value, previous\_value, type } 

current\_value: map[string]

previous\_value: map[string]

type: optional "cli\_op\_permissions\_enabled"



GoogleDriveSearchEnabled object { current\_value, previous\_value, type } 

current\_value: boolean

previous\_value: boolean

type: optional "google\_drive\_search\_enabled"



GmailIntegrationEnabled object { current\_value, previous\_value, type } 

current\_value: boolean

previous\_value: boolean

type: optional "gmail\_integration\_enabled"



GoogleCalendarIntegrationEnabled object { current\_value, previous\_value, type } 

current\_value: boolean

previous\_value: boolean

type: optional "google\_calendar\_integration\_enabled"



ThinkingModeEnabled object { current\_value, previous\_value, type } 



current\_value: "adaptive" or "extended" or "off"

One of the following:

"adaptive"

"extended"

"off"



previous\_value: "adaptive" or "extended" or "off"

One of the following:

"adaptive"

"extended"

"off"

type: optional "thinking\_mode\_enabled"



ResearchModeEnabled object { current\_value, previous\_value, type } 

current\_value: boolean

previous\_value: boolean

type: optional "research\_mode\_enabled"



ComputerUseEnabled object { current\_value, previous\_value, type } 

current\_value: boolean

previous\_value: boolean

type: optional "computer\_use\_enabled"



ClaudeAPIInArtifactsEnabled object { current\_value, previous\_value, type } 

The Claude API in Artifacts setting was changed.

current\_value: boolean

Setting value immediately after this change

previous\_value: boolean

Setting value immediately before this change

type: optional "claude\_api\_in\_artifacts\_enabled"



ConversationPreferences object { type } 

The 'conversation\_preferences' for the user were updated. Values omitted.

type: optional "conversation\_preferences"



CoworkGlobalInstructions object { type } 

The Cowork global instructions were updated. Values omitted.

type: optional "cowork\_global\_instructions"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "claude\_user\_settings\_updated"



WorkspaceMemberSpendLimitCreated object { actor, id, account\_id, 7 more } 

A per-member or workspace-default Claude Code spend limit was created.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

account\_id: optional string

Tagged ID of the user (null for workspace-wide default).

created\_at: optional string

When this activity occurred.

limit\_action: optional string

The action taken when the limit is reached.

limit\_usd: optional number

The spend limit threshold in USD cents.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "workspace\_member\_spend\_limit\_created"

workspace\_id: optional string

Tagged ID of the workspace.



WorkspaceMemberSpendLimitDeleted object { actor, id, account\_id, 6 more } 

A per-member or workspace-default Claude Code spend limit was deleted.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

account\_id: optional string

Tagged ID of the user (null for workspace-wide default).

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

spend\_limit\_id: optional string

UUID of the deleted spend limit.

type: optional "workspace\_member\_spend\_limit\_deleted"

workspace\_id: optional string

Tagged ID of the workspace.



WorkspaceMemberSpendLimitUpdated object { actor, id, account\_id, 7 more } 

A per-member Claude Code spend limit amount was updated.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

account\_id: optional string

Tagged ID of the user (null for workspace-wide default).

created\_at: optional string

When this activity occurred.

new\_limit\_usd: optional number

The new spend limit threshold in USD cents.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

spend\_limit\_id: optional string

UUID of the spend limit.

type: optional "workspace\_member\_spend\_limit\_updated"

workspace\_id: optional string

Tagged ID of the workspace.



WorkspaceSpendLimitAlertEmailsUpdated object { actor, id, alert\_emails, 5 more } 

Spend limit alert email recipients were updated for a workspace.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

alert\_emails: optional array of string

Updated list of alert email addresses.

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "workspace\_spend\_limit\_alert\_emails\_updated"

workspace\_id: optional string

Tagged ID of the workspace.



WorkspaceSpendLimitCreated object { actor, id, created\_at, 6 more } 

A workspace-level API spend limit was created.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

limit\_action: optional string

The action taken when the limit is reached (notify\_only or notify\_and\_pause).

limit\_usd: optional number

The spend limit threshold in USD cents.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

type: optional "workspace\_spend\_limit\_created"

workspace\_id: optional string

Tagged ID of the workspace.



WorkspaceSpendLimitDeleted object { actor, id, created\_at, 5 more } 

A workspace-level API spend limit was deleted.



actor: object { email\_address, ip\_address, user\_agent, 2 more } 

email\_address: string

ip\_address: string

user\_agent: string

user\_id: string

type: optional "user\_actor"

id: optional string

Unique identifier for the activity e.g. 'activity\_abcd1234'

created\_at: optional string

When this activity occurred.

organization\_id: optional string

Organization ID this activity is associated with

organization\_uuid: optional string

Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

spend\_limit\_id: optional string

UUID of the deleted spend limit.

type: optional "workspace\_spend\_limit\_deleted"

workspace\_id: optional string

Tagged ID of the workspace.

---

*Copyright © Anthropic. All rights reserved.*
