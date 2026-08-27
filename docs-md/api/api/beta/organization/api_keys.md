# API Keys

Copy page



cURL

# API Keys

##### [List API Keys](api/http/beta/organization/api_keys/list.md)

GET/v1/organizations/api\_keys

##### [Get API Key](api/http/beta/organization/api_keys/retrieve.md)

GET/v1/organizations/api\_keys/{api\_key\_id}

##### [Update API Key](api/http/beta/organization/api_keys/update.md)

POST/v1/organizations/api\_keys/{api\_key\_id}

##### Models



BetaAPIKey object{ id, created\_at, created\_by, 8 more }



BetaAPIKeyCreatedBy object{ id, type }

id: string

ID of the actor that created the object.



type: "service\_account" or "user"

Type of the actor that created the object.

One of the following:

"service\_account"

"user"



BetaAPIKeyOrganizationScope object{ type }



type: "organization"

Scope type. Always `"organization"`: the API key has no Workspace. Only a principal-bound API key can have this scope.

defaultorganization



BetaAPIKeyServiceAccountActor object{ service\_account\_id, type }

service\_account\_id: string

ID of the Service Account the API key acts as.



type: "service\_account\_actor"

Principal type. Always `"service_account_actor"` for a Service Account.

defaultservice\_account\_actor



BetaAPIKeyUserActor object{ type, user\_id }



type: "user\_actor"

Principal type. Always `"user_actor"` for a User.

defaultuser\_actor

user\_id: string

ID of the User the API key acts as.



BetaAPIKeyWorkspaceScope object{ type, workspace\_id }



type: "workspace"

Scope type. Always `"workspace"`: the API key belongs to one Workspace.

defaultworkspace

workspace\_id: string

ID of the Workspace the API key belongs to. Unlike the deprecated top-level `workspace_id`, this is the Workspace's real ID even for the organization's default Workspace.

---

*Copyright © Anthropic. All rights reserved.*
