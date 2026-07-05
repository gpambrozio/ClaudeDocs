# Admin

Copy page



# Admin

#### AdminOrganizations

##### [Get Current Organization](api/admin/organizations/me.md)

GET/v1/organizations/me

#### AdminInvites

##### [Create Invite](api/admin/invites/create.md)

POST/v1/organizations/invites

##### [Get Invite](api/admin/invites/retrieve.md)

GET/v1/organizations/invites/{invite\_id}

##### [List Invites](api/admin/invites/list.md)

GET/v1/organizations/invites

##### [Delete Invite](api/admin/invites/delete.md)

DELETE/v1/organizations/invites/{invite\_id}

#### AdminUsers

##### [Get User](api/admin/users/retrieve.md)

GET/v1/organizations/users/{user\_id}

##### [List Users](api/admin/users/list.md)

GET/v1/organizations/users

##### [Update User](api/admin/users/update.md)

POST/v1/organizations/users/{user\_id}

##### [Remove User](api/admin/users/delete.md)

DELETE/v1/organizations/users/{user\_id}

#### AdminWorkspaces

##### [Create Workspace](api/admin/workspaces/create.md)

POST/v1/organizations/workspaces

##### [Get Workspace](api/admin/workspaces/retrieve.md)

GET/v1/organizations/workspaces/{workspace\_id}

##### [List Workspaces](api/admin/workspaces/list.md)

GET/v1/organizations/workspaces

##### [Update Workspace](api/admin/workspaces/update.md)

POST/v1/organizations/workspaces/{workspace\_id}

##### [Archive Workspace](api/admin/workspaces/archive.md)

POST/v1/organizations/workspaces/{workspace\_id}/archive

#### AdminWorkspacesMembers

##### [Create Workspace Member](api/admin/workspaces/members/create.md)

POST/v1/organizations/workspaces/{workspace\_id}/members

##### [Get Workspace Member](api/admin/workspaces/members/retrieve.md)

GET/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

##### [List Workspace Members](api/admin/workspaces/members/list.md)

GET/v1/organizations/workspaces/{workspace\_id}/members

##### [Update Workspace Member](api/admin/workspaces/members/update.md)

POST/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

##### [Delete Workspace Member](api/admin/workspaces/members/delete.md)

DELETE/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

#### AdminWorkspacesRate Limits

##### [List Workspace Rate Limits](api/admin/workspaces/rate_limits/list.md)

GET/v1/organizations/workspaces/{workspace\_id}/rate\_limits

#### AdminWorkspacesService Accounts

##### [Create Service Account Workspace Member](api/admin/workspaces/service_accounts/create.md)

POST/v1/organizations/workspaces/{workspace\_id}/service\_accounts

##### [Get Service Account Workspace Member](api/admin/workspaces/service_accounts/retrieve.md)

GET/v1/organizations/workspaces/{workspace\_id}/service\_accounts/{service\_account\_id}

##### [List Service Account Workspace Members](api/admin/workspaces/service_accounts/list.md)

GET/v1/organizations/workspaces/{workspace\_id}/service\_accounts

##### [Update Service Account Workspace Member](api/admin/workspaces/service_accounts/update.md)

POST/v1/organizations/workspaces/{workspace\_id}/service\_accounts/{service\_account\_id}

##### [Delete Service Account Workspace Member](api/admin/workspaces/service_accounts/delete.md)

DELETE/v1/organizations/workspaces/{workspace\_id}/service\_accounts/{service\_account\_id}

#### AdminAPI Keys

##### [Get API Key](api/admin/api_keys/retrieve.md)

GET/v1/organizations/api\_keys/{api\_key\_id}

##### [List API Keys](api/admin/api_keys/list.md)

GET/v1/organizations/api\_keys

##### [Update API Key](api/admin/api_keys/update.md)

POST/v1/organizations/api\_keys/{api\_key\_id}

#### AdminExternal Keys

##### [Create External Key](api/admin/external_keys/create.md)

POST/v1/organizations/external\_keys

##### [List External Keys](api/admin/external_keys/list.md)

GET/v1/organizations/external\_keys

##### [Get External Key](api/admin/external_keys/retrieve.md)

GET/v1/organizations/external\_keys/{external\_key\_id}

##### [Update External Key](api/admin/external_keys/update.md)

POST/v1/organizations/external\_keys/{external\_key\_id}

##### [Delete External Key](api/admin/external_keys/delete.md)

DELETE/v1/organizations/external\_keys/{external\_key\_id}

##### [Validate External Key](api/admin/external_keys/validate.md)

POST/v1/organizations/external\_keys/{external\_key\_id}/validate

#### AdminUsage Report

##### [Get Messages Usage Report](api/admin/usage_report/retrieve_messages.md)

GET/v1/organizations/usage\_report/messages

##### [Get Claude Code Usage Report](api/admin/usage_report/retrieve_claude_code.md)

GET/v1/organizations/usage\_report/claude\_code

#### AdminCost Report

##### [Get Cost Report](api/admin/cost_report/retrieve.md)

GET/v1/organizations/cost\_report

#### AdminAnalytics

##### [Get Activity Summaries](api/admin/analytics/retrieve_summaries.md)

GET/v1/organizations/analytics/summaries

#### AdminAnalyticsUsage

##### [Get Token Usage Over Time](api/admin/analytics/usage/list.md)

GET/v1/organizations/analytics/usage\_report

##### [Get Per-User Token Usage](api/admin/analytics/usage/list_by_user.md)

GET/v1/organizations/analytics/user\_usage\_report

#### AdminAnalyticsCost

##### [Get Cost Over Time](api/admin/analytics/cost/list.md)

GET/v1/organizations/analytics/cost\_report

##### [Get Per-User Cost](api/admin/analytics/cost/list_by_user.md)

GET/v1/organizations/analytics/user\_cost\_report

#### AdminAnalyticsUsers

##### [List User Activity](api/admin/analytics/users/list.md)

GET/v1/organizations/analytics/users

#### AdminAnalyticsSkills

##### [Get Skill Usage](api/admin/analytics/skills/list.md)

GET/v1/organizations/analytics/skills

#### AdminAnalyticsConnectors

##### [Get Connector Usage](api/admin/analytics/connectors/list.md)

GET/v1/organizations/analytics/connectors

#### AdminAnalyticsChat Projects

##### [Get Chat Project Usage](api/admin/analytics/chat_projects/list.md)

GET/v1/organizations/analytics/apps/chat/projects

#### AdminAnalyticsPlugins

##### [Get Plugin Usage](api/admin/analytics/plugins/list.md)

GET/v1/organizations/analytics/plugins

#### AdminAnalyticsArtifacts

##### [Get Artifact Activity](api/admin/analytics/artifacts/list.md)

GET/v1/organizations/analytics/artifacts

#### AdminSpend Limits

##### [Set Spend Limit](api/admin/spend_limits/create.md)

POST/v1/organizations/spend\_limits

##### [Get Spend Limit](api/admin/spend_limits/retrieve.md)

GET/v1/organizations/spend\_limits/{spend\_limit\_id}

##### [Delete Spend Limit](api/admin/spend_limits/delete.md)

DELETE/v1/organizations/spend\_limits/{spend\_limit\_id}

##### [List Effective Spend Limits](api/admin/spend_limits/list_effective.md)

GET/v1/organizations/spend\_limits/effective

#### AdminSpend LimitsIncrease Requests

##### [List Spend Limit Increase Requests](api/admin/spend_limits/increase_requests/list.md)

GET/v1/organizations/spend\_limit\_increase\_requests

##### [Get Spend Limit Increase Request](api/admin/spend_limits/increase_requests/retrieve.md)

GET/v1/organizations/spend\_limit\_increase\_requests/{spend\_limit\_increase\_request\_id}

##### [Approve Spend Limit Increase Request](api/admin/spend_limits/increase_requests/approve.md)

POST/v1/organizations/spend\_limit\_increase\_requests/{spend\_limit\_increase\_request\_id}/approve

##### [Deny Spend Limit Increase Request](api/admin/spend_limits/increase_requests/deny.md)

POST/v1/organizations/spend\_limit\_increase\_requests/{spend\_limit\_increase\_request\_id}/deny

#### AdminRate Limits

##### [List Organization Rate Limits](api/admin/rate_limits/list.md)

GET/v1/organizations/rate\_limits

#### AdminService Accounts

##### [Create Service Account](api/admin/service_accounts/create.md)

POST/v1/organizations/service\_accounts

##### [Get Service Account](api/admin/service_accounts/retrieve.md)

GET/v1/organizations/service\_accounts/{service\_account\_id}

##### [List Service Accounts](api/admin/service_accounts/list.md)

GET/v1/organizations/service\_accounts

##### [Update Service Account](api/admin/service_accounts/update.md)

POST/v1/organizations/service\_accounts/{service\_account\_id}

##### [Archive Service Account](api/admin/service_accounts/archive.md)

POST/v1/organizations/service\_accounts/{service\_account\_id}/archive

#### AdminService AccountsWorkspaces

##### [Add Workspace To Service Account](api/admin/service_accounts/workspaces/create.md)

POST/v1/organizations/service\_accounts/{service\_account\_id}/workspaces

##### [List Workspaces For Service Account](api/admin/service_accounts/workspaces/list.md)

GET/v1/organizations/service\_accounts/{service\_account\_id}/workspaces

##### [Remove Workspace From Service Account](api/admin/service_accounts/workspaces/delete.md)

DELETE/v1/organizations/service\_accounts/{service\_account\_id}/workspaces/{workspace\_id}

#### AdminFederation Issuers

##### [Create Federation Issuer](api/admin/federation_issuers/create.md)

POST/v1/organizations/federation\_issuers

##### [Get Federation Issuer](api/admin/federation_issuers/retrieve.md)

GET/v1/organizations/federation\_issuers/{federation\_issuer\_id}

##### [List Federation Issuers](api/admin/federation_issuers/list.md)

GET/v1/organizations/federation\_issuers

##### [Update Federation Issuer](api/admin/federation_issuers/update.md)

POST/v1/organizations/federation\_issuers/{federation\_issuer\_id}

##### [Archive Federation Issuer](api/admin/federation_issuers/archive.md)

POST/v1/organizations/federation\_issuers/{federation\_issuer\_id}/archive

#### AdminFederation Rules

##### [Create Federation Rule](api/admin/federation_rules/create.md)

POST/v1/organizations/federation\_rules

##### [Get Federation Rule](api/admin/federation_rules/retrieve.md)

GET/v1/organizations/federation\_rules/{federation\_rule\_id}

##### [List Federation Rules](api/admin/federation_rules/list.md)

GET/v1/organizations/federation\_rules

##### [Update Federation Rule](api/admin/federation_rules/update.md)

POST/v1/organizations/federation\_rules/{federation\_rule\_id}

##### [Archive Federation Rule](api/admin/federation_rules/archive.md)

POST/v1/organizations/federation\_rules/{federation\_rule\_id}/archive

#### AdminFederation RulesWorkspaces

##### [List Federation Rule Workspaces](api/admin/federation_rules/workspaces/list.md)

GET/v1/organizations/federation\_rules/{federation\_rule\_id}/workspaces

##### [Add Federation Rule Workspace](api/admin/federation_rules/workspaces/create.md)

POST/v1/organizations/federation\_rules/{federation\_rule\_id}/workspaces

##### [Remove Federation Rule Workspace](api/admin/federation_rules/workspaces/delete.md)

DELETE/v1/organizations/federation\_rules/{federation\_rule\_id}/workspaces/{workspace\_id}

#### AdminMCP Tunnels

##### [Get Tunnel](api/admin/mcp_tunnels/retrieve.md)

Deprecated

GET/v1/organizations/tunnels/{tunnel\_id}

##### [List Tunnels](api/admin/mcp_tunnels/list.md)

Deprecated

GET/v1/organizations/tunnels

##### [Reveal Tunnel Token](api/admin/mcp_tunnels/reveal_token.md)

Deprecated

POST/v1/organizations/tunnels/{tunnel\_id}/reveal\_token

##### [Rotate Tunnel Token](api/admin/mcp_tunnels/rotate_token.md)

Deprecated

POST/v1/organizations/tunnels/{tunnel\_id}/rotate\_token

##### [Archive Tunnel](api/admin/mcp_tunnels/archive.md)

Deprecated

POST/v1/organizations/tunnels/{tunnel\_id}/archive

#### AdminMCP TunnelsTunnel Certificates

##### [Create Tunnel Certificate](api/admin/mcp_tunnels/tunnel_certificates/create.md)

Deprecated

POST/v1/organizations/tunnels/{tunnel\_id}/certificates

##### [Get Tunnel Certificate](api/admin/mcp_tunnels/tunnel_certificates/retrieve.md)

Deprecated

GET/v1/organizations/tunnels/{tunnel\_id}/certificates/{certificate\_id}

##### [List Tunnel Certificates](api/admin/mcp_tunnels/tunnel_certificates/list.md)

Deprecated

GET/v1/organizations/tunnels/{tunnel\_id}/certificates

##### [Archive Tunnel Certificate](api/admin/mcp_tunnels/tunnel_certificates/archive.md)

Deprecated

POST/v1/organizations/tunnels/{tunnel\_id}/certificates/{certificate\_id}/archive

---

*Copyright © Anthropic. All rights reserved.*
