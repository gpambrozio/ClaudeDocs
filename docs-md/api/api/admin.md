# Admin

Copy page



# Admin

#### Admin[Organizations](api/http/admin/organizations.md)

##### [Get Current Organization](api/http/admin/organizations/me.md)

GET/v1/organizations/me

#### Admin[Invites](api/http/admin/invites.md)

##### [Create Invite](api/http/admin/invites/create.md)

POST/v1/organizations/invites

##### [Get Invite](api/http/admin/invites/retrieve.md)

GET/v1/organizations/invites/{invite\_id}

##### [List Invites](api/http/admin/invites/list.md)

GET/v1/organizations/invites

##### [Delete Invite](api/http/admin/invites/delete.md)

DELETE/v1/organizations/invites/{invite\_id}

#### Admin[Users](api/http/admin/users.md)

##### [Get User](api/http/admin/users/retrieve.md)

GET/v1/organizations/users/{user\_id}

##### [List Users](api/http/admin/users/list.md)

GET/v1/organizations/users

##### [Update User](api/http/admin/users/update.md)

POST/v1/organizations/users/{user\_id}

##### [Remove User](api/http/admin/users/delete.md)

DELETE/v1/organizations/users/{user\_id}

#### Admin[RBAC Groups](api/http/admin/rbac_groups.md)

##### [List RBAC Groups](api/http/admin/rbac_groups/list.md)

GET/v1/organizations/rbac\_groups

##### [Get RBAC Group](api/http/admin/rbac_groups/retrieve.md)

GET/v1/organizations/rbac\_groups/{group\_id}

##### [Create RBAC Group](api/http/admin/rbac_groups/create.md)

POST/v1/organizations/rbac\_groups

##### [Update RBAC Group](api/http/admin/rbac_groups/update.md)

POST/v1/organizations/rbac\_groups/{group\_id}

##### [Delete RBAC Group](api/http/admin/rbac_groups/delete.md)

DELETE/v1/organizations/rbac\_groups/{group\_id}

#### AdminRBAC Groups[Members](api/http/admin/rbac_groups/members.md)

##### [List RBAC Group Members](api/http/admin/rbac_groups/members/list.md)

GET/v1/organizations/rbac\_groups/{group\_id}/members

##### [Add RBAC Group Member](api/http/admin/rbac_groups/members/create.md)

POST/v1/organizations/rbac\_groups/{group\_id}/members

##### [Remove RBAC Group Member](api/http/admin/rbac_groups/members/delete.md)

DELETE/v1/organizations/rbac\_groups/{group\_id}/members/{user\_id}

#### Admin[RBAC Roles](api/http/admin/rbac_roles.md)

##### [List RBAC Roles](api/http/admin/rbac_roles/list.md)

GET/v1/organizations/rbac\_roles

##### [Get RBAC Role](api/http/admin/rbac_roles/retrieve.md)

GET/v1/organizations/rbac\_roles/{role\_id}

#### AdminRBAC Roles[Permissions](api/http/admin/rbac_roles/permissions.md)

##### [List RBAC Role Permissions](api/http/admin/rbac_roles/permissions/list.md)

GET/v1/organizations/rbac\_roles/{role\_id}/permissions

#### Admin[Workspaces](api/http/admin/workspaces.md)

##### [Create Workspace](api/http/admin/workspaces/create.md)

POST/v1/organizations/workspaces

##### [Get Workspace](api/http/admin/workspaces/retrieve.md)

GET/v1/organizations/workspaces/{workspace\_id}

##### [List Workspaces](api/http/admin/workspaces/list.md)

GET/v1/organizations/workspaces

##### [Update Workspace](api/http/admin/workspaces/update.md)

POST/v1/organizations/workspaces/{workspace\_id}

##### [Archive Workspace](api/http/admin/workspaces/archive.md)

POST/v1/organizations/workspaces/{workspace\_id}/archive

#### AdminWorkspaces[Members](api/http/admin/workspaces/members.md)

##### [Create Workspace Member](api/http/admin/workspaces/members/create.md)

POST/v1/organizations/workspaces/{workspace\_id}/members

##### [Get Workspace Member](api/http/admin/workspaces/members/retrieve.md)

GET/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

##### [List Workspace Members](api/http/admin/workspaces/members/list.md)

GET/v1/organizations/workspaces/{workspace\_id}/members

##### [Update Workspace Member](api/http/admin/workspaces/members/update.md)

POST/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

##### [Delete Workspace Member](api/http/admin/workspaces/members/delete.md)

DELETE/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

#### AdminWorkspaces[Rate Limits](api/http/admin/workspaces/rate_limits.md)

##### [List Workspace Rate Limits](api/http/admin/workspaces/rate_limits/list.md)

GET/v1/organizations/workspaces/{workspace\_id}/rate\_limits

#### AdminWorkspaces[Service Accounts](api/http/admin/workspaces/service_accounts.md)

##### [Create Service Account Workspace Member](api/http/admin/workspaces/service_accounts/create.md)

POST/v1/organizations/workspaces/{workspace\_id}/service\_accounts

##### [Get Service Account Workspace Member](api/http/admin/workspaces/service_accounts/retrieve.md)

GET/v1/organizations/workspaces/{workspace\_id}/service\_accounts/{service\_account\_id}

##### [List Service Account Workspace Members](api/http/admin/workspaces/service_accounts/list.md)

GET/v1/organizations/workspaces/{workspace\_id}/service\_accounts

##### [Update Service Account Workspace Member](api/http/admin/workspaces/service_accounts/update.md)

POST/v1/organizations/workspaces/{workspace\_id}/service\_accounts/{service\_account\_id}

##### [Delete Service Account Workspace Member](api/http/admin/workspaces/service_accounts/delete.md)

DELETE/v1/organizations/workspaces/{workspace\_id}/service\_accounts/{service\_account\_id}

#### Admin[API Keys](api/http/admin/api_keys.md)

##### [Retrieve API Key (Admin API)](api/http/admin/api_keys/retrieve.md)

GET/v1/organizations/api\_keys/{api\_key\_id}

##### [List API Keys](api/http/admin/api_keys/list.md)

GET/v1/organizations/api\_keys

##### [Update API Key](api/http/admin/api_keys/update.md)

POST/v1/organizations/api\_keys/{api\_key\_id}

#### Admin[External Keys](api/http/admin/external_keys.md)

##### [Create External Key](api/http/admin/external_keys/create.md)

POST/v1/organizations/external\_keys

##### [List External Keys](api/http/admin/external_keys/list.md)

GET/v1/organizations/external\_keys

##### [Get External Key](api/http/admin/external_keys/retrieve.md)

GET/v1/organizations/external\_keys/{external\_key\_id}

##### [Update External Key](api/http/admin/external_keys/update.md)

POST/v1/organizations/external\_keys/{external\_key\_id}

##### [Delete External Key](api/http/admin/external_keys/delete.md)

DELETE/v1/organizations/external\_keys/{external\_key\_id}

##### [Validate External Key](api/http/admin/external_keys/validate.md)

POST/v1/organizations/external\_keys/{external\_key\_id}/validate

#### Admin[Usage Report](api/http/admin/usage_report.md)

##### [Get Messages Usage Report](api/http/admin/usage_report/retrieve_messages.md)

GET/v1/organizations/usage\_report/messages

##### [Get Claude Code Usage Report](api/http/admin/usage_report/retrieve_claude_code.md)

GET/v1/organizations/usage\_report/claude\_code

#### Admin[Cost Report](api/http/admin/cost_report.md)

##### [Get Cost Report](api/http/admin/cost_report/retrieve.md)

GET/v1/organizations/cost\_report

#### Admin[Analytics](api/http/admin/analytics.md)

##### [Get Activity Summaries](api/http/admin/analytics/retrieve_summaries.md)

GET/v1/organizations/analytics/summaries

#### AdminAnalytics[Usage](api/http/admin/analytics/usage.md)

##### [Get Token Usage Over Time](api/http/admin/analytics/usage/list.md)

GET/v1/organizations/analytics/usage\_report

##### [Get Per-User Token Usage](api/http/admin/analytics/usage/list_by_user.md)

GET/v1/organizations/analytics/user\_usage\_report

#### AdminAnalytics[Cost](api/http/admin/analytics/cost.md)

##### [Get Cost Over Time](api/http/admin/analytics/cost/list.md)

GET/v1/organizations/analytics/cost\_report

##### [Get Per-User Cost](api/http/admin/analytics/cost/list_by_user.md)

GET/v1/organizations/analytics/user\_cost\_report

#### AdminAnalytics[Users](api/http/admin/analytics/users.md)

##### [List User Activity](api/http/admin/analytics/users/list.md)

GET/v1/organizations/analytics/users

#### AdminAnalytics[Skills](api/http/admin/analytics/skills.md)

##### [Get Skill Usage](api/http/admin/analytics/skills/list.md)

GET/v1/organizations/analytics/skills

#### AdminAnalytics[Connectors](api/http/admin/analytics/connectors.md)

##### [Get Connector Usage](api/http/admin/analytics/connectors/list.md)

GET/v1/organizations/analytics/connectors

#### AdminAnalytics[Chat Projects](api/http/admin/analytics/chat_projects.md)

##### [Get Chat Project Usage](api/http/admin/analytics/chat_projects/list.md)

GET/v1/organizations/analytics/apps/chat/projects

#### AdminAnalytics[Plugins](api/http/admin/analytics/plugins.md)

##### [Get Plugin Usage](api/http/admin/analytics/plugins/list.md)

GET/v1/organizations/analytics/plugins

#### AdminAnalytics[Artifacts](api/http/admin/analytics/artifacts.md)

##### [Get Artifact Activity](api/http/admin/analytics/artifacts/list.md)

GET/v1/organizations/analytics/artifacts

#### Admin[Spend Limits](api/http/admin/spend_limits.md)

##### [Set Spend Limit](api/http/admin/spend_limits/create.md)

POST/v1/organizations/spend\_limits

##### [Get Spend Limit](api/http/admin/spend_limits/retrieve.md)

GET/v1/organizations/spend\_limits/{spend\_limit\_id}

##### [Delete Spend Limit](api/http/admin/spend_limits/delete.md)

DELETE/v1/organizations/spend\_limits/{spend\_limit\_id}

##### [List Effective Spend Limits](api/http/admin/spend_limits/list_effective.md)

GET/v1/organizations/spend\_limits/effective

#### AdminSpend Limits[Increase Requests](api/http/admin/spend_limits/increase_requests.md)

##### [List Spend Limit Increase Requests](api/http/admin/spend_limits/increase_requests/list.md)

GET/v1/organizations/spend\_limit\_increase\_requests

##### [Get Spend Limit Increase Request](api/http/admin/spend_limits/increase_requests/retrieve.md)

GET/v1/organizations/spend\_limit\_increase\_requests/{spend\_limit\_increase\_request\_id}

##### [Approve Spend Limit Increase Request](api/http/admin/spend_limits/increase_requests/approve.md)

POST/v1/organizations/spend\_limit\_increase\_requests/{spend\_limit\_increase\_request\_id}/approve

##### [Deny Spend Limit Increase Request](api/http/admin/spend_limits/increase_requests/deny.md)

POST/v1/organizations/spend\_limit\_increase\_requests/{spend\_limit\_increase\_request\_id}/deny

#### Admin[Rate Limits](api/http/admin/rate_limits.md)

##### [List Organization Rate Limits](api/http/admin/rate_limits/list.md)

GET/v1/organizations/rate\_limits

#### Admin[Service Accounts](api/http/admin/service_accounts.md)

##### [Create Service Account](api/http/admin/service_accounts/create.md)

POST/v1/organizations/service\_accounts

##### [Get Service Account](api/http/admin/service_accounts/retrieve.md)

GET/v1/organizations/service\_accounts/{service\_account\_id}

##### [List Service Accounts](api/http/admin/service_accounts/list.md)

GET/v1/organizations/service\_accounts

##### [Update Service Account](api/http/admin/service_accounts/update.md)

POST/v1/organizations/service\_accounts/{service\_account\_id}

##### [Archive Service Account](api/http/admin/service_accounts/archive.md)

POST/v1/organizations/service\_accounts/{service\_account\_id}/archive

#### AdminService Accounts[Workspaces](api/http/admin/service_accounts/workspaces.md)

##### [Add Workspace To Service Account](api/http/admin/service_accounts/workspaces/create.md)

POST/v1/organizations/service\_accounts/{service\_account\_id}/workspaces

##### [List Workspaces For Service Account](api/http/admin/service_accounts/workspaces/list.md)

GET/v1/organizations/service\_accounts/{service\_account\_id}/workspaces

##### [Remove Workspace From Service Account](api/http/admin/service_accounts/workspaces/delete.md)

DELETE/v1/organizations/service\_accounts/{service\_account\_id}/workspaces/{workspace\_id}

#### Admin[Federation Issuers](api/http/admin/federation_issuers.md)

##### [Create Federation Issuer](api/http/admin/federation_issuers/create.md)

POST/v1/organizations/federation\_issuers

##### [Get Federation Issuer](api/http/admin/federation_issuers/retrieve.md)

GET/v1/organizations/federation\_issuers/{federation\_issuer\_id}

##### [List Federation Issuers](api/http/admin/federation_issuers/list.md)

GET/v1/organizations/federation\_issuers

##### [Update Federation Issuer](api/http/admin/federation_issuers/update.md)

POST/v1/organizations/federation\_issuers/{federation\_issuer\_id}

##### [Archive Federation Issuer](api/http/admin/federation_issuers/archive.md)

POST/v1/organizations/federation\_issuers/{federation\_issuer\_id}/archive

#### Admin[Federation Rules](api/http/admin/federation_rules.md)

##### [Create Federation Rule](api/http/admin/federation_rules/create.md)

POST/v1/organizations/federation\_rules

##### [Get Federation Rule](api/http/admin/federation_rules/retrieve.md)

GET/v1/organizations/federation\_rules/{federation\_rule\_id}

##### [List Federation Rules](api/http/admin/federation_rules/list.md)

GET/v1/organizations/federation\_rules

##### [Update Federation Rule](api/http/admin/federation_rules/update.md)

POST/v1/organizations/federation\_rules/{federation\_rule\_id}

##### [Archive Federation Rule](api/http/admin/federation_rules/archive.md)

POST/v1/organizations/federation\_rules/{federation\_rule\_id}/archive

#### AdminFederation Rules[Workspaces](api/http/admin/federation_rules/workspaces.md)

##### [List Federation Rule Workspaces](api/http/admin/federation_rules/workspaces/list.md)

GET/v1/organizations/federation\_rules/{federation\_rule\_id}/workspaces

##### [Add Federation Rule Workspace](api/http/admin/federation_rules/workspaces/create.md)

POST/v1/organizations/federation\_rules/{federation\_rule\_id}/workspaces

##### [Remove Federation Rule Workspace](api/http/admin/federation_rules/workspaces/delete.md)

DELETE/v1/organizations/federation\_rules/{federation\_rule\_id}/workspaces/{workspace\_id}

#### Admin[MCP Tunnels](api/http/admin/mcp_tunnels.md)

##### [Get Tunnel](api/http/admin/mcp_tunnels/retrieve.md)

Deprecated

GET/v1/organizations/tunnels/{tunnel\_id}

##### [List Tunnels](api/http/admin/mcp_tunnels/list.md)

Deprecated

GET/v1/organizations/tunnels

##### [Reveal Tunnel Token](api/http/admin/mcp_tunnels/reveal_token.md)

Deprecated

POST/v1/organizations/tunnels/{tunnel\_id}/reveal\_token

##### [Rotate Tunnel Token](api/http/admin/mcp_tunnels/rotate_token.md)

Deprecated

POST/v1/organizations/tunnels/{tunnel\_id}/rotate\_token

##### [Archive Tunnel](api/http/admin/mcp_tunnels/archive.md)

Deprecated

POST/v1/organizations/tunnels/{tunnel\_id}/archive

#### AdminMCP Tunnels[Tunnel Certificates](api/http/admin/mcp_tunnels/tunnel_certificates.md)

##### [Create Tunnel Certificate](api/http/admin/mcp_tunnels/tunnel_certificates/create.md)

Deprecated

POST/v1/organizations/tunnels/{tunnel\_id}/certificates

##### [Get Tunnel Certificate](api/http/admin/mcp_tunnels/tunnel_certificates/retrieve.md)

Deprecated

GET/v1/organizations/tunnels/{tunnel\_id}/certificates/{certificate\_id}

##### [List Tunnel Certificates](api/http/admin/mcp_tunnels/tunnel_certificates/list.md)

Deprecated

GET/v1/organizations/tunnels/{tunnel\_id}/certificates

##### [Archive Tunnel Certificate](api/http/admin/mcp_tunnels/tunnel_certificates/archive.md)

Deprecated

POST/v1/organizations/tunnels/{tunnel\_id}/certificates/{certificate\_id}/archive

---

*Copyright © Anthropic. All rights reserved.*
