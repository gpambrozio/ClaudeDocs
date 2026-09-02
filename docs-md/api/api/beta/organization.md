# Organization

Copy page



cURL

# Organization

##### [Get Current Organization](api/http/beta/organization/retrieve.md)

GET/v1/organizations/me

##### Models



BetaOrganization object{ id, name, type }



id: string

ID of the Organization.

formatuuid

name: string

Name of the Organization.



type: "organization"

Object type.

For Organizations, this is always `"organization"`.

defaultorganization



BetaOrganizationRole = "admin" or "billing" or "claude\_code\_user" or 6 more

One of the following:

"admin"

"billing"

"claude\_code\_user"

"developer"

"managed"

"membership\_admin"

"owner"

"primary\_owner"

"user"

#### Organization[API Keys](api/http/beta/organization/api_keys.md)

##### [List API Keys](api/http/beta/organization/api_keys/list.md)

GET/v1/organizations/api\_keys

##### [Get API Key](api/http/beta/organization/api_keys/retrieve.md)

GET/v1/organizations/api\_keys/{api\_key\_id}

##### [Update API Key](api/http/beta/organization/api_keys/update.md)

POST/v1/organizations/api\_keys/{api\_key\_id}

#### Organization[External Keys](api/http/beta/organization/external_keys.md)

##### [Create External Key](api/http/beta/organization/external_keys/create.md)

POST/v1/organizations/external\_keys

##### [List External Keys](api/http/beta/organization/external_keys/list.md)

GET/v1/organizations/external\_keys

##### [Get External Key](api/http/beta/organization/external_keys/retrieve.md)

GET/v1/organizations/external\_keys/{external\_key\_id}

##### [Update External Key](api/http/beta/organization/external_keys/update.md)

POST/v1/organizations/external\_keys/{external\_key\_id}

##### [Delete External Key](api/http/beta/organization/external_keys/delete.md)

DELETE/v1/organizations/external\_keys/{external\_key\_id}

##### [Validate External Key](api/http/beta/organization/external_keys/validate.md)

POST/v1/organizations/external\_keys/{external\_key\_id}/validate

#### OrganizationFederation[Issuers](api/http/beta/organization/federation/issuers.md)

##### [Create Federation Issuer](api/http/beta/organization/federation/issuers/create.md)

POST/v1/organizations/federation\_issuers

##### [List Federation Issuers](api/http/beta/organization/federation/issuers/list.md)

GET/v1/organizations/federation\_issuers

##### [Get Federation Issuer](api/http/beta/organization/federation/issuers/retrieve.md)

GET/v1/organizations/federation\_issuers/{federation\_issuer\_id}

##### [Update Federation Issuer](api/http/beta/organization/federation/issuers/update.md)

POST/v1/organizations/federation\_issuers/{federation\_issuer\_id}

##### [Archive Federation Issuer](api/http/beta/organization/federation/issuers/archive.md)

POST/v1/organizations/federation\_issuers/{federation\_issuer\_id}/archive

#### OrganizationFederation[Rules](api/http/beta/organization/federation/rules.md)

##### [Create Federation Rule](api/http/beta/organization/federation/rules/create.md)

POST/v1/organizations/federation\_rules

##### [List Federation Rules](api/http/beta/organization/federation/rules/list.md)

GET/v1/organizations/federation\_rules

##### [Get Federation Rule](api/http/beta/organization/federation/rules/retrieve.md)

GET/v1/organizations/federation\_rules/{federation\_rule\_id}

##### [Update Federation Rule](api/http/beta/organization/federation/rules/update.md)

POST/v1/organizations/federation\_rules/{federation\_rule\_id}

##### [Archive Federation Rule](api/http/beta/organization/federation/rules/archive.md)

POST/v1/organizations/federation\_rules/{federation\_rule\_id}/archive

#### OrganizationFederationRules[Workspaces](api/http/beta/organization/federation/rules/workspaces.md)

##### [Add Federation Rule Workspace](api/http/beta/organization/federation/rules/workspaces/add.md)

POST/v1/organizations/federation\_rules/{federation\_rule\_id}/workspaces

##### [List Federation Rule Workspaces](api/http/beta/organization/federation/rules/workspaces/list.md)

GET/v1/organizations/federation\_rules/{federation\_rule\_id}/workspaces

##### [Remove Federation Rule Workspace](api/http/beta/organization/federation/rules/workspaces/remove.md)

DELETE/v1/organizations/federation\_rules/{federation\_rule\_id}/workspaces/{workspace\_id}

#### Organization[Invites](api/http/beta/organization/invites.md)

##### [Create Invite](api/http/beta/organization/invites/create.md)

POST/v1/organizations/invites

##### [List Invites](api/http/beta/organization/invites/list.md)

GET/v1/organizations/invites

##### [Get Invite](api/http/beta/organization/invites/retrieve.md)

GET/v1/organizations/invites/{invite\_id}

##### [Delete Invite](api/http/beta/organization/invites/delete.md)

DELETE/v1/organizations/invites/{invite\_id}

#### Organization[Service Accounts](api/http/beta/organization/service_accounts.md)

##### [Create Service Account](api/http/beta/organization/service_accounts/create.md)

POST/v1/organizations/service\_accounts

##### [List Service Accounts](api/http/beta/organization/service_accounts/list.md)

GET/v1/organizations/service\_accounts

##### [Get Service Account](api/http/beta/organization/service_accounts/retrieve.md)

GET/v1/organizations/service\_accounts/{service\_account\_id}

##### [Update Service Account](api/http/beta/organization/service_accounts/update.md)

POST/v1/organizations/service\_accounts/{service\_account\_id}

##### [Archive Service Account](api/http/beta/organization/service_accounts/archive.md)

POST/v1/organizations/service\_accounts/{service\_account\_id}/archive

#### OrganizationService Accounts[Workspaces](api/http/beta/organization/service_accounts/workspaces.md)

##### [Add Workspace To Service Account](api/http/beta/organization/service_accounts/workspaces/add.md)

POST/v1/organizations/service\_accounts/{service\_account\_id}/workspaces

##### [List Workspaces For Service Account](api/http/beta/organization/service_accounts/workspaces/list.md)

GET/v1/organizations/service\_accounts/{service\_account\_id}/workspaces

##### [Remove Workspace From Service Account](api/http/beta/organization/service_accounts/workspaces/remove.md)

DELETE/v1/organizations/service\_accounts/{service\_account\_id}/workspaces/{workspace\_id}

#### Organization[Users](api/http/beta/organization/users.md)

##### [List Users](api/http/beta/organization/users/list.md)

GET/v1/organizations/users

##### [Get User](api/http/beta/organization/users/retrieve.md)

GET/v1/organizations/users/{user\_id}

##### [Update User](api/http/beta/organization/users/update.md)

POST/v1/organizations/users/{user\_id}

##### [Remove User](api/http/beta/organization/users/remove.md)

DELETE/v1/organizations/users/{user\_id}

#### Organization[Workspaces](api/http/beta/organization/workspaces.md)

##### [List Workspaces](api/http/beta/organization/workspaces/list.md)

GET/v1/organizations/workspaces

##### [Create Workspace](api/http/beta/organization/workspaces/create.md)

POST/v1/organizations/workspaces

##### [Get Workspace](api/http/beta/organization/workspaces/retrieve.md)

GET/v1/organizations/workspaces/{workspace\_id}

##### [Update Workspace](api/http/beta/organization/workspaces/update.md)

POST/v1/organizations/workspaces/{workspace\_id}

##### [Archive Workspace](api/http/beta/organization/workspaces/archive.md)

POST/v1/organizations/workspaces/{workspace\_id}/archive

#### OrganizationWorkspaces[Rate Limits](api/http/beta/organization/workspaces/rate_limits.md)

##### [List Workspace Rate Limits](api/http/beta/organization/workspaces/rate_limits/list.md)

GET/v1/organizations/workspaces/{workspace\_id}/rate\_limits

#### OrganizationWorkspaces[Members](api/http/beta/organization/workspaces/members.md)

##### [List Workspace Members](api/http/beta/organization/workspaces/members/list.md)

GET/v1/organizations/workspaces/{workspace\_id}/members

##### [Create Workspace Member](api/http/beta/organization/workspaces/members/add.md)

POST/v1/organizations/workspaces/{workspace\_id}/members

##### [Get Workspace Member](api/http/beta/organization/workspaces/members/retrieve.md)

GET/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

##### [Update Workspace Member](api/http/beta/organization/workspaces/members/update.md)

POST/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

##### [Delete Workspace Member](api/http/beta/organization/workspaces/members/remove.md)

DELETE/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

#### OrganizationWorkspaces[Service Accounts](api/http/beta/organization/workspaces/service_accounts.md)

##### [List Service Account Workspace Members](api/http/beta/organization/workspaces/service_accounts/list.md)

GET/v1/organizations/workspaces/{workspace\_id}/service\_accounts

##### [Create Service Account Workspace Member](api/http/beta/organization/workspaces/service_accounts/add.md)

POST/v1/organizations/workspaces/{workspace\_id}/service\_accounts

##### [Get Service Account Workspace Member](api/http/beta/organization/workspaces/service_accounts/retrieve.md)

GET/v1/organizations/workspaces/{workspace\_id}/service\_accounts/{service\_account\_id}

##### [Update Service Account Workspace Member](api/http/beta/organization/workspaces/service_accounts/update.md)

POST/v1/organizations/workspaces/{workspace\_id}/service\_accounts/{service\_account\_id}

##### [Delete Service Account Workspace Member](api/http/beta/organization/workspaces/service_accounts/remove.md)

DELETE/v1/organizations/workspaces/{workspace\_id}/service\_accounts/{service\_account\_id}

#### Organization[Rate Limits](api/http/beta/organization/rate_limits.md)

##### [List Organization Rate Limits](api/http/beta/organization/rate_limits/list.md)

GET/v1/organizations/rate\_limits

#### Organization[Compliance Settings](api/http/beta/organization/compliance_settings.md)

##### [Get Compliance Settings](api/http/beta/organization/compliance_settings/retrieve.md)

GET/v1/organizations/compliance\_settings

##### [Update Compliance Settings](api/http/beta/organization/compliance_settings/update.md)

POST/v1/organizations/compliance\_settings

---

*Copyright © Anthropic. All rights reserved.*
