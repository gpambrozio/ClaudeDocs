# Admin Api Keys

---
title: Create an Admin API key
url: https://platform.claude.com/docs/en/manage-claude/admin-api-keys
description: Create an Admin API key for your Claude Console or Claude Enterprise organization.
---

An Admin API key authenticates every API in the **Admin** section of this guide: the [Admin API](admin-api.md), [Analytics APIs](analytics-api.md), [Compliance API](compliance-api.md), [Spend Limits API](spend-limits-api.md), [Usage and Cost API](usage-cost-api.md), and [Rate Limits API](rate-limits-api.md). You do not need a separate key for each API. The one exception is the Admin API's service-account, federation-issuer, and federation-rule endpoints, which accept only an OAuth bearer token with the `org:admin` scope. See [Obtain an OAuth bearer token](admin-api.md#oauth-bearer-token).

Where you create the key depends on which Claude product your organization uses.

## Which key do you need?

| Your organization                                           | Create the key in                                                                         | Key prefix           | Who can create it                                                                                                                                                                          | Works with                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------- | ----------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Claude Console** (Claude Platform, `platform.claude.com`) | [Claude Console > Settings > Admin keys](https://platform.claude.com/settings/admin-keys) | `sk-ant-admin01-...` | Organization members with the **admin** role                                                                                                                                               | [Admin API](admin-api.md), [Usage and Cost API](usage-cost-api.md), [Rate Limits API](rate-limits-api.md), [Claude Code Analytics API](claude-code-analytics-api.md), and the Compliance API [Activity Feed](compliance-activity-feed.md)                                                                                             |
| **Claude Enterprise** (`claude.ai`)                         | [claude.ai > Organization settings > API](https://claude.ai/admin-settings/api-access)    | `sk-ant-api01-...`   | The parent organization's **primary owner** (all linked organizations). An **organization owner** can create one carrying Compliance API scopes only, restricted to their own organization | [User management](user-management.md) (the Admin API's member, invite, and group endpoints), [Compliance API](compliance-api.md), [Claude Enterprise Analytics API](analytics-api.md), and [Spend Limits API](spend-limits-api.md), according to the [scopes](admin-api-keys.md#choose-scopes-for-a-claude-enterprise-key) you select |

A key created in one organization cannot be used to manage a different organization. If your company uses both Claude Console and Claude Enterprise, create one key in each.

## Create a key for a Claude Console organization

**Sign in as an organization admin**

Only organization members with the **admin** role can create Admin API keys. See [Organization roles and permissions](admin-api.md#organization-roles-and-permissions).

**Open Admin keys settings**

Go to [Claude Console > Settings > Admin keys](https://platform.claude.com/settings/admin-keys).

**Create the key**

Click **Create key**, give it a name, choose a [key expiration](authentication.md#key-expiration), and click **Create**. Claude Console keys do not have selectable scopes; every key carries full access to all endpoints that accept Admin API keys (the service-account and federation endpoints noted at the top of this page do not accept Admin API keys).

**Copy and store the secret**

Copy the displayed secret (starting with `sk-ant-admin01-`) and store it in your secrets manager. The full secret is shown only once.

## Create a key for a Claude Enterprise organization

**Sign in as the primary owner or an organization owner**

The **primary owner** of the Claude Enterprise parent organization can create a key that can access every linked organization, or one restricted to a single organization. An **organization owner** can create a key with Compliance API scopes only, restricted to their own organization.

**Open API settings**

Go to [claude.ai > Organization settings > API](https://claude.ai/admin-settings/api-access) and find the **Keys** section.

**Click + Create key**

Name the key and select the scopes you need from the [scopes table](admin-api-keys.md#choose-scopes-for-a-claude-enterprise-key). The primary owner can combine scopes from different APIs (for example, `read:analytics` and `read:spend_limits`) on a single key.

**Copy and store the secret**

Copy the displayed secret (starting with `sk-ant-api01-`) and store it in your secrets manager. The full secret is shown only once.

## Choose scopes for a Claude Enterprise key

When you create a Claude Enterprise key, select every scope that the APIs you plan to call require. Scopes are fixed at creation; to add a scope later, create a new key.

| To call...                                                                                                                                                                                                                                                                                                                                                                                                             | Select these scopes           |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| Admin API [user management](user-management.md): list and look up members and invites; read custom roles and their permissions                                                                                                                                                                                                                                          | `read:members`                |
| Admin API [user management](user-management.md): change member roles, remove members, create and withdraw invites                                                                                                                                                                                                                                                       | `write:members`               |
| Admin API [user management](user-management.md): read groups and their members                                                                                                                                                                                                                                                                                          | `read:rbac_groups`            |
| Admin API [user management](user-management.md): create, rename, and delete groups; add and remove group members; assign groups on invite creation                                                                                                                                                                                                                      | `write:rbac_groups`           |
| [Spend Limits API](spend-limits-api.md): read members' effective spend limits and increase requests                                                                                                                                                                                                                                                                     | `read:spend_limits`           |
| [Spend Limits API](spend-limits-api.md): set or clear per-user spend limits; approve or deny increase requests                                                                                                                                                                                                                                                          | `write:spend_limits`          |
| [Claude Enterprise Analytics API](analytics-api.md): engagement, adoption, cost, and usage reports                                                                                                                                                                                                                                                                      | `read:analytics`              |
| [Compliance API Activity Feed](compliance-activity-feed.md): organization-wide activity events                                                                                                                                                                                                                                                                          | `read:compliance_activities`  |
| [Compliance API chat, file, and project endpoints](compliance-content-data.md) and [Compliance API session endpoints](compliance-sessions.md): read chats, files, projects, session transcripts, and [organization users](compliance-org-data.md#list-organization-users) | `read:compliance_user_data`   |
| [Compliance API chat, file, and project endpoints](compliance-content-data.md): delete chats, files, and projects                                                                                                                                                                                                                                                       | `delete:compliance_user_data` |
| [Compliance API organization endpoints](compliance-org-data.md): read organization metadata and effective settings                                                                                                                                                                                                                                                      | `read:compliance_org_data`    |
| Admin API [user management](user-management.md) read endpoints and every Compliance API read endpoint, with a single read-only scope (for security-audit integrations; does not include the Spend Limits or Analytics APIs)                                                                                                                                             | `read:org_audit`              |

The Compliance and Analytics APIs must be enabled for your organization before keys with those scopes can be used. See [Set up the Compliance API](compliance-api-access.md#set-up-the-compliance-api) and [Get access to the Claude Enterprise Analytics API](analytics-api.md#get-access-to-the-claude-enterprise-analytics-api).

## Use the key

Pass the key in the `x-api-key` header on every request. See each API's documentation for complete request examples.

A call that exceeds the key's scopes returns `403 Forbidden` with a message listing the scopes the key has and the scopes the endpoint needs.

## Next steps

**Admin API**

Manage organization members, workspaces, and API keys.

**Spend Limits API**

Set per-member spend limits and review increase requests for your Claude Enterprise organization.

**Analytics APIs**

Report on Claude Code productivity or Claude Enterprise engagement and adoption.

**Compliance API**

Audit activity and retrieve or delete user content across your organization.

---

*Copyright © Anthropic. All rights reserved.*
