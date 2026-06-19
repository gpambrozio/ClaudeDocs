# Create an Admin API key

Copy page



Every API in the **Admin** section of this guide (the [Admin API](manage-claude/admin-api.md), [Analytics APIs](manage-claude/analytics-api.md), [Compliance API](manage-claude/compliance-api.md), [Spend Limits API](manage-claude/spend-limits-api.md), [Usage and Cost API](manage-claude/usage-cost-api.md), and [Rate Limits API](manage-claude/rate-limits-api.md)) is authenticated with an Admin API key. You do not need a separate key for each API.

Where you create the key depends on which Claude product your organization uses.

##  Which key do you need?

| Your organization | Create the key in | Key prefix | Who can create it | Works with |
| --- | --- | --- | --- | --- |
| **Claude Console** (Claude Platform, `platform.claude.com`) | [Claude Console > Settings > Admin keys](https://platform.claude.com/settings/admin-keys) | `sk-ant-admin01-...` | Organization members with the **admin** role | [Admin API](manage-claude/admin-api.md), [Usage and Cost API](manage-claude/usage-cost-api.md), [Rate Limits API](manage-claude/rate-limits-api.md), [Claude Code Analytics API](manage-claude/claude-code-analytics-api.md), and the Compliance API [Activity Feed](manage-claude/compliance-activity-feed.md) |
| **Claude Enterprise** (`claude.ai`) | [claude.ai > Organization settings > API](https://claude.ai/admin-settings/api-access) | `sk-ant-api01-...` | The organization's **primary owner** | [Compliance API](manage-claude/compliance-api.md), [Claude Enterprise Analytics API](manage-claude/analytics-api.md), and [Spend Limits API](manage-claude/spend-limits-api.md), according to the [scopes](#choose-scopes-for-a-claude-enterprise-key) you select |

A key created in one organization cannot be used to manage a different organization. If your company uses both Claude Console and Claude Enterprise, create one key in each.

##  Create a key for a Claude Console organization

1. 1

   Sign in as an organization admin

   Only organization members with the **admin** role can create Admin API keys. See [Organization roles and permissions](manage-claude/admin-api.md).
2. 2

   Open Admin keys settings

   Go to [Claude Console > Settings > Admin keys](https://platform.claude.com/settings/admin-keys).
3. 3

   Create the key

   Click **Create key**, give it a name, and click **Create**. Claude Console keys do not have selectable scopes; every key carries full Admin API access.
4. 4

   Copy and store the secret

   Copy the displayed secret (starting with `sk-ant-admin01-`) and store it in your secrets manager. The full secret is shown only once.

##  Create a key for a Claude Enterprise organization

1. 1

   Sign in as the primary owner

   Only the **primary owner** of the Claude Enterprise parent organization can create these keys.
2. 2

   Open API settings

   Go to [claude.ai > Organization settings > API](https://claude.ai/admin-settings/api-access) and find the **Keys** section.
3. 3

   Click + Create key

   Name the key and select the scopes you need from the [scopes table](#choose-scopes-for-a-claude-enterprise-key). You can combine scopes from different APIs (for example, `read:analytics` and `read:spend_limits`) on a single key.
4. 4

   Copy and store the secret

   Copy the displayed secret (starting with `sk-ant-api01-`) and store it in your secrets manager. The full secret is shown only once.

##  Choose scopes for a Claude Enterprise key

When you create a Claude Enterprise key, select every scope that the APIs you plan to call require. Scopes are fixed at creation; to add a scope later, create a new key.

| To call... | Select these scopes |
| --- | --- |
| [Spend Limits API](manage-claude/spend-limits-api.md): read members' effective spend limits and increase requests | `read:spend_limits` |
| [Spend Limits API](manage-claude/spend-limits-api.md): set or clear per-user spend limits; approve or deny increase requests | `write:spend_limits` |
| [Claude Enterprise Analytics API](manage-claude/analytics-api.md): engagement, adoption, cost, and usage reports | `read:analytics` |
| [Compliance API Activity Feed](manage-claude/compliance-activity-feed.md): organization-wide activity events | `read:compliance_activities` |
| [Compliance API content endpoints](manage-claude/compliance-content-data.md): read chats, files, projects, and users | `read:compliance_user_data` |
| [Compliance API content endpoints](manage-claude/compliance-content-data.md): delete chats, files, and projects | `delete:compliance_user_data` |
| [Compliance API organization endpoints](manage-claude/compliance-org-data.md): read organization metadata and settings | `read:compliance_org_data`, `read:compliance_org_settings` |

The Compliance and Analytics APIs must be enabled for your organization before keys with those scopes can be used. See [Get access to the Compliance API](manage-claude/compliance-api-access.md) and [Analytics APIs](manage-claude/analytics-api.md).

##  Use the key

Pass the key in the `x-api-key` header on every request. See each API's documentation for complete request examples.

A call that exceeds the key's scopes returns `403 Forbidden` with a message listing the scopes the key has and the scopes the endpoint needs.

##  Next steps

[Admin API

Manage organization members, workspaces, and API keys.](manage-claude/admin-api.md)[Spend Limits API

Set per-member spend limits and review increase requests for your Claude Enterprise organization.](manage-claude/spend-limits-api.md)[Analytics APIs

Report on Claude Code productivity or Claude Enterprise engagement and adoption.](manage-claude/analytics-api.md)[Compliance API

Audit activity and retrieve or delete user content across your organization.](manage-claude/compliance-api.md)

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
