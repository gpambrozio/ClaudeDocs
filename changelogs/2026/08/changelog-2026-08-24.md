# [Claude docs changes for August 24th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/765706b4ca5be949aea8f95e498116cc9cbdfd36) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/765706b4ca5be949aea8f95e498116cc9cbdfd36)]

## Executive Summary
- Quiet day: no new Claude Code version notes and no substantive documentation content changes from Anthropic.
- The archive's crawler recovered full content for 9 previously blank "Loading"-placeholder Compliance/Apps API pages (Groups, Apps/Chats, Role Permissions, Effective Organization Settings), documented below as if new.
- 6 pages that had full content before this sync regressed back to blank "Loading" placeholders this time, including the Messages API's `create` and `count_tokens` endpoints and the Compliance `activities`/`roles` list pages — their prior content is not reflected in this changelog.
- Two Claude Code pages (`claude-platform-on-aws`, `settings-reference`) only lost cosmetic UI chrome (marketing banner, filter/sort widgets) in this crawl, not real content, so they're excluded below.

-----

## Claude Code changes

No substantive content changes today — the only diffs were cosmetic UI elements (a marketing CTA banner on `claude-platform-on-aws` and page filter/sort widgets on `settings-reference`) stripped by the crawler, not documentation changes from Anthropic.

-----

## API changes

### A note on this section

Of the 15 changed API pages today, none reflect real documentation edits from Anthropic — they're all archive crawler artifacts. 9 pages that had been captured mid-render (holding only "Loading" placeholder text) finally got their full rendered content this sync, so they're summarized below as if new. The other 6 pages went the opposite way: they had full content captured previously, but this sync's crawl regressed them to blank "Loading" placeholders, so no content is available to summarize.

### Recovered documents (previously blank "Loading" placeholders)

#### [api/compliance/apps](https://github.com/gpambrozio/ClaudeDocs/blob/765706b4ca5be949aea8f95e498116cc9cbdfd36/docs-md/api/api/compliance/apps.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps)]

Index page listing the Compliance API's "Apps" endpoint group: chats, chat messages, chat files, Claude-generated files, projects (with attachments, collaborators, documents), artifacts, and local/remote sessions.

#### [api/compliance/apps/chats/delete](https://github.com/gpambrozio/ClaudeDocs/blob/765706b4ca5be949aea8f95e498116cc9cbdfd36/docs-md/api/api/compliance/apps/chats/delete.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/chats/delete)]

Documents `DELETE /v1/compliance/apps/chats/{claude_chat_id}`, which permanently and irreversibly deletes a chat along with its messages and files.

#### [api/compliance/apps/chats/messages](https://github.com/gpambrozio/ClaudeDocs/blob/765706b4ca5be949aea8f95e498116cc9cbdfd36/docs-md/api/api/compliance/apps/chats/messages.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages)]

Documents the `MessageListResponse` model returned by `GET /v1/compliance/apps/chats/{claude_chat_id}/messages`, covering message content blocks (text, tool use, tool result), attached/generated files, and truncation flags for exported content.

#### [api/compliance/groups](https://github.com/gpambrozio/ClaudeDocs/blob/765706b4ca5be949aea8f95e498116cc9cbdfd36/docs-md/api/api/compliance/groups.md) [[Source](https://platform.claude.com/docs/en/api/compliance/groups)]

Index page for the Compliance Groups endpoints (list groups, get a group, list group members) and the shared `Group` response model (id, description, name, roles, `source_type` of `direct` or `scim`).

#### [api/compliance/groups/list](https://github.com/gpambrozio/ClaudeDocs/blob/765706b4ca5be949aea8f95e498116cc9cbdfd36/docs-md/api/api/compliance/groups/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/groups/list)]

Documents `GET /v1/compliance/groups`, listing RBAC groups with `name_prefix` filtering and cursor-based pagination (`limit`, `page`, `has_more`, `next_page`).

#### [api/compliance/groups/members](https://github.com/gpambrozio/ClaudeDocs/blob/765706b4ca5be949aea8f95e498116cc9cbdfd36/docs-md/api/api/compliance/groups/members.md) [[Source](https://platform.claude.com/docs/en/api/compliance/groups/members)]

Documents the `MemberListResponse` model (email, `user_id`, created/updated timestamps) used by the group-members listing endpoint.

#### [api/compliance/groups/members/list](https://github.com/gpambrozio/ClaudeDocs/blob/765706b4ca5be949aea8f95e498116cc9cbdfd36/docs-md/api/api/compliance/groups/members/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/groups/members/list)]

Documents `GET /v1/compliance/groups/{group_id}/members`, listing a group's members with pagination.

#### [api/compliance/organizations/roles/permissions/list](https://github.com/gpambrozio/ClaudeDocs/blob/765706b4ca5be949aea8f95e498116cc9cbdfd36/docs-md/api/api/compliance/organizations/roles/permissions/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/organizations/roles/permissions/list)]

Documents `GET /v1/compliance/organizations/{org_uuid}/roles/{role_id}/permissions`, listing the `action`/`resource_type`/`resource_id` permission grants for an RBAC role.

#### [api/compliance/organizations/settings/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/765706b4ca5be949aea8f95e498116cc9cbdfd36/docs-md/api/api/compliance/organizations/settings/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve)]

Documents `GET /v1/compliance/organizations/{organization_id}/settings`, returning the effective (post-policy) settings in force for an organization: configured compliance API keys, ~45 boolean feature flags (e.g. `hipaa_compliance_enabled`, `sso_enabled`, `claude_code_web_enabled`), integer/string/string-list settings, SSO provisioning mode, and per-data-type retention periods.

### Regressed documents (now blank "Loading" placeholders; no content to summarize)

* [api/beta/messages/batches/create](https://github.com/gpambrozio/ClaudeDocs/blob/765706b4ca5be949aea8f95e498116cc9cbdfd36/docs-md/api/api/beta/messages/batches/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/batches/create)] — previously documented creating a Message Batch.
* [api/beta/messages/batches/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/765706b4ca5be949aea8f95e498116cc9cbdfd36/docs-md/api/api/beta/messages/batches/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve)] — previously documented retrieving a Message Batch.
* [api/beta/messages/count_tokens](https://github.com/gpambrozio/ClaudeDocs/blob/765706b4ca5be949aea8f95e498116cc9cbdfd36/docs-md/api/api/beta/messages/count_tokens.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/count_tokens)] — previously documented the token-counting endpoint.
* [api/beta/messages/create](https://github.com/gpambrozio/ClaudeDocs/blob/765706b4ca5be949aea8f95e498116cc9cbdfd36/docs-md/api/api/beta/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)] — previously documented the core Messages `create` endpoint.
* [api/compliance/activities/list](https://github.com/gpambrozio/ClaudeDocs/blob/765706b4ca5be949aea8f95e498116cc9cbdfd36/docs-md/api/api/compliance/activities/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/activities/list)] — previously documented querying compliance activities, including the full `activity_types` enum.
* [api/compliance/organizations/roles/list](https://github.com/gpambrozio/ClaudeDocs/blob/765706b4ca5be949aea8f95e498116cc9cbdfd36/docs-md/api/api/compliance/organizations/roles/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/organizations/roles/list)] — previously documented listing an organization's compliance roles.
