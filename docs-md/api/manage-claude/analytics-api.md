# Analytics APIs

Copy page

Anthropic provides two analytics APIs, and which one you use depends on which Claude product your organization manages:

- The **Claude Code Analytics API** reports daily Claude Code productivity metrics for organizations that use the Claude Platform. It is part of the [Admin API](manage-claude/admin-api.md) and uses an Admin API key.
- The **Claude Enterprise Analytics API** reports organization-wide engagement, adoption, and cost data across Claude products (chat, projects, Claude Code, and more) for Claude Enterprise organizations. It uses an Analytics API key created in claude.ai.

The two APIs use different key types, created in different places by different roles. This page describes which API fits your organization and how to create the right key.

##  Which API do you need?

| API | Key type | Created in | Who can create it | What it covers |
| --- | --- | --- | --- | --- |
| **Claude Code Analytics API** | Admin API key (`sk-ant-admin01-...`) | [Claude Console > Settings > Admin keys](https://platform.claude.com/settings/admin-keys) | Organization admin | Daily Claude Code metrics per user: sessions, lines of code, commits, pull requests, tool acceptance, and estimated cost by model |
| **Claude Enterprise Analytics API** | Analytics API key | [claude.ai > Analytics > API keys](https://claude.ai/analytics/api-keys) | Primary owner | Organization-wide engagement and adoption (user activity, active-user summaries, project, skill, and connector usage), plus cost and usage reports |

The key types are not interchangeable: an Admin API key cannot call the Claude Enterprise Analytics API, and an Analytics API key cannot call the Admin API. If your organization uses both the Claude Platform and Claude Enterprise, you can provision both keys and use each API for its own data.



Looking for API usage and cost data rather than product analytics? See the [Usage and Cost API](manage-claude/usage-cost-api.md), which explains the right path for both Claude Console and Claude Enterprise organizations.

##  Get access to the Claude Code Analytics API

The Claude Code Analytics API is available to every organization with access to the [Admin API](manage-claude/admin-api.md), and is free to use.

1. 1

   Sign in as an organization admin

   Only organization members with the **admin** role can create Admin API keys. See [Organization roles and permissions](manage-claude/admin-api.md) for the full role list.
2. 2

   Create an Admin API key

   Go to [Claude Console > Settings > Admin keys](https://platform.claude.com/settings/admin-keys), click **Create key**, name the key, and click **Create**. Copy the displayed secret key (starting with `sk-ant-admin01-`) and store it in your secrets manager. The full secret is displayed only once.
3. 3

   Call the API

   Pass the key in the `x-api-key` header:

   ```shiki
   curl "https://api.anthropic.com/v1/organizations/usage_report/claude_code?starting_at=2025-09-08" \
     --header "anthropic-version: 2023-06-01" \
     --header "x-api-key: $ADMIN_API_KEY"
   ```

   

For the available metrics, request parameters, and response schema, see the [Claude Code Analytics API guide](manage-claude/claude-code-analytics-api.md) and the [API reference](api/admin-api/claude-code/get-claude-code-usage-report.md).

##  Get access to the Claude Enterprise Analytics API

The Claude Enterprise Analytics API is available to Claude Enterprise organizations. Engagement and adoption data is available on all Enterprise plans. The cost and usage endpoints apply to usage-based Enterprise plans; for seat-based Enterprise plans, they reflect usage credits only.

1. 1

   Sign in as the primary owner

   Only the primary owner of the organization can enable API access and create Analytics API keys.
2. 2

   Enable API access and create a key

   Go to [claude.ai > Analytics > API keys](https://claude.ai/analytics/api-keys) and enable public API access, then create an Analytics API key. Keys carry the `read:analytics` scope. Copy the displayed secret and store it in your secrets manager.
3. 3

   Call the API

   Pass the key in the `x-api-key` header. Endpoints live under `https://api.anthropic.com/v1/organizations/analytics/`. For request examples, parameters, and response schemas, see the [Claude Enterprise Analytics API reference guide](https://support.claude.com/en/articles/13703965-claude-enterprise-analytics-api-reference-guide).

The Claude Enterprise Analytics API provides:

- **User activity:** per-user daily metrics across chat (conversations, messages, projects, files, artifacts), Claude Code (sessions, commits, pull requests, lines of code, tool actions), and other Claude products
- **Activity summaries:** organization-level daily, weekly, and monthly active users, seat counts, and pending invites
- **Project, skill, and connector usage:** adoption breakdowns for chat projects, skills, and connectors
- **Cost and usage reports:** per-user and organization-level token usage and cost over time (usage-based Enterprise plans)

For an overview of the engagement and adoption data, see [Claude Enterprise Analytics API: access, engagement, and adoption data](https://support.claude.com/en/articles/13694757-claude-enterprise-analytics-api-access-engagement-and-adoption-data). For endpoint details, parameters, and response schemas, see the [Claude Enterprise Analytics API reference guide](https://support.claude.com/en/articles/13703965-claude-enterprise-analytics-api-reference-guide).

##  Next steps

[Claude Code Analytics API

Track Claude Code sessions, code changes, and tool usage with an Admin API key.](manage-claude/claude-code-analytics-api.md)[Usage and Cost API

Track API token usage and costs for your organization.](manage-claude/usage-cost-api.md)[Claude Enterprise Analytics API reference



Endpoint reference for engagement, adoption, and cost data.](https://support.claude.com/en/articles/13703965-claude-enterprise-analytics-api-reference-guide)[Get access to the Compliance API

Audit and compliance data uses its own key types.](manage-claude/compliance-api-access.md)

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
