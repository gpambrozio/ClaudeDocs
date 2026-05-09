# [Claude docs changes for May 9th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/eafe057) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/eafe057)]

## Executive Summary
- A new **Compliance API** is now documented for Claude Enterprise customers, providing programmatic access to the Activity Feed, user directory, chats, files, and projects for audit and eDiscovery use cases (8 new documentation pages)
- A new dedicated **Admin API** guide (`manage-claude/admin-api.md`) replaces scattered references to the old `overview.md` page, consolidating all Admin API documentation in one place
- Claude Code 2.1.136 ships with a large bug fix release, including critical fixes for MCP servers disappearing after `/clear`, OAuth refresh token loss on concurrent refreshes, and plan mode not blocking file writes
- API rate limit examples were updated to reflect significantly higher token limits (input tokens per minute raised from 2M to 10M, output tokens from 400K to 800K)
- **Structured Outputs** is now marked as GA on Google Cloud's Vertex AI (previously Beta)

## New Claude Code versions

### [2.1.136](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/versions/2.1.136.md)

#### New features

* Added `CLAUDE_CODE_ENABLE_FEEDBACK_SURVEY_FOR_OTEL` environment variable to re-enable the session quality survey for enterprises capturing responses via OpenTelemetry
* Added `settings.autoMode.hard_deny` for auto mode classifier rules that block unconditionally, regardless of user intent or allow exceptions
* WSL2: image paste from Windows clipboard now works via a PowerShell fallback when xclip/wl-paste cannot read image data

#### Existing feature improvements

* Improved visual consistency across slash command dialogs: standardized footer hints, dialog spacing, and arrow-key styling; dialog frame now appears immediately during loading instead of popping in afterward

#### Major bug fixes

* Fixed MCP servers configured in `.mcp.json`, plugins, and claude.ai connectors silently disappearing after `/clear` in the VS Code extension, JetBrains plugin, and Agent SDK
* Fixed a rare login loop where a concurrent credential write could overwrite a freshly-rotated OAuth token and force re-login
* Fixed MCP OAuth refresh tokens being lost when multiple servers refresh concurrently — users with several remote MCP servers should no longer need daily re-authentication
* Fixed an API error (400) when extended thinking emitted a redacted thinking block after a tool call
* Fixed `--resume` / `--continue` not finding sessions when the project path contains underscores
* Fixed plan mode not blocking file writes when a matching `Edit(...)` allow rule exists
* Fixed env vars from `CLAUDE_ENV_FILE` SessionStart hooks going stale after `/resume` or `/clear`
* Fixed plugin `Stop`/`UserPromptSubmit` hooks failing when cache cleanup deletes a version still in use by a running session
* Fixed `AskUserQuestion` discarding multi-select answers when supplied as an array

### [2.1.137](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/versions/2.1.137.md)

#### Major bug fixes

* Fixed VS Code extension failing to activate on Windows

-----

## Claude Code changes

### Changed documents

#### [GitHub Actions](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/claude-code/github-actions.md) [[Source](https://code.claude.com/docs/en/github-actions)]

* The page now returns a crawler error (HTTP 500) — all previous documentation content has been replaced with an "Error loading page" message. The GitHub Actions documentation is currently unavailable.

-----

## API changes

### New Documents

#### [Admin API](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/manage-claude/admin-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api)]

New dedicated Admin API overview page that consolidates documentation on programmatically managing organization members, workspaces, API keys, and organization info. Replaces scattered references to a previous `overview.md` file. Includes code examples for all major Admin API operations and references to the new Compliance API.

#### [Compliance API](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/manage-claude/compliance-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-api)]

New top-level overview for the Compliance API (Claude Enterprise plan only). Explains the two key types (Compliance Access Keys vs Admin API keys), how the API is organized, how it differs from audit log exports and the Analytics API, and links to all sub-sections.

#### [Get access to the Compliance API](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/manage-claude/compliance-api-access.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-api-access)]

New guide for provisioning Compliance API access. Covers which key type to create depending on product (claude.ai vs Claude Console), how to enable the API, scope selection (`read:compliance_activities`, `read:compliance_user_data`, `delete:compliance_user_data`, `read:compliance_org_data`), key rotation, and checking key scopes.

#### [Query the Activity Feed](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/manage-claude/compliance-activity-feed.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed)]

New guide for querying the Compliance API Activity Feed. Documents filtering by type, actor, and time window; pagination using cursor-based and page-token schemes; and the full Activity object structure including all actor types (`user_actor`, `api_actor`, `admin_api_key_actor`, `scim_directory_sync_actor`, etc.). Activities are queryable within 1 minute of occurring and retained for 6 years.

#### [Retrieve and delete chats, files, and projects](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/manage-claude/compliance-content-data.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-content-data)]

New guide for accessing claude.ai content via the Compliance API. Covers listing chats by user ID, fetching message content (including files, generated files, and artifacts), downloading file/artifact binary content, listing projects and attachments, and hard-deleting chats, files, project documents, and projects. Notes that deletes are permanent and immediate.

#### [Handle Compliance API errors](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/manage-claude/compliance-errors.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-errors)]

New error reference page listing all 400, 401, 403, 404, 409, 429, and 500-series errors the Compliance API returns, with verbatim error bodies and specific fixes for each. Includes retry guidance for each status code.

#### [Compliance API FAQ](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/manage-claude/compliance-faq.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-faq)]

New FAQ page covering access and scopes, data coverage and retention, integration and pagination patterns, and sandbox testing for the Compliance API.

#### [Design your compliance integration](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/manage-claude/compliance-integration-patterns.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-integration-patterns)]

New guide for production integration design. Covers two feed-consumption patterns (window polling vs cursor-driven incremental reads), SIEM correlation using `actor.user_id` as the stable join key, and content retention planning including export-and-archive vs on-demand retrieval tradeoffs.

#### [List organizations, users, roles, and groups](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/manage-claude/compliance-org-data.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-org-data)]

New guide for the Compliance API directory endpoints. Covers listing all linked organizations, paginating users per organization, listing RBAC roles and their permissions, and listing SCIM/RBAC groups and their members. Explains how organization UUIDs map to identifiers used in the Activity Feed and content endpoints.

### Changed documents

#### [API and data retention](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/manage-claude/api-and-data-retention.md) [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

* Added a paragraph documenting the Compliance API's data retention model: the Activity Feed retains data for 6 years, while chat/file/project content follows the organization's retention policy set in claude.ai settings. [[line 20](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/manage-claude/api-and-data-retention.md?plain=1#L20)] [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

#### [Adaptive thinking](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/build-with-claude/adaptive-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

* Email obfuscation hash updated in the "contact our sales team" link (no content change).

#### [Build with Claude overview](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/build-with-claude/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

* Structured Outputs is now listed as GA on Google Cloud's Vertex AI (previously Beta). [[line 47](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/build-with-claude/overview.md?plain=1#L47)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]
* Added a sentence linking to the Admin API, Usage and Cost API, and Compliance API for administration and governance. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/build-with-claude/overview.md?plain=1#L15)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

#### [Context editing](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/build-with-claude/context-editing.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/context-editing)]

* The `clear_thinking_20251015` strategy default behavior was reformatted from a dense paragraph into a table showing which model generations keep all prior thinking blocks vs only the last turn. [[lines 38-44](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/build-with-claude/context-editing.md?plain=1#L38-L44)] [[Source](https://platform.claude.com/docs/en/build-with-claude/context-editing)]

#### [Context windows](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/build-with-claude/context-windows.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]

* Server-side compaction is now noted as available in beta for Claude Mythos Preview (in addition to Opus 4.7, Opus 4.6, and Sonnet 4.6). [[line 134](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/build-with-claude/context-windows.md?plain=1#L134)] [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]

#### [Extended thinking](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Removed "and later models" qualifier from the Claude Opus 4.7 manual extended thinking restriction — the prohibition is now scoped specifically to Claude Opus 4.7 rather than implying all future models. [[lines 9-13](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L9-L13)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

#### [Fast mode](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/build-with-claude/fast-mode.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]

* Updated the error handling fallback code example: replaced catching `InternalServerError` and `OverloadedError` separately with catching the broader `APIStatusError` and checking `status_code < 500` to distinguish retryable from non-retryable errors. [[lines 141-149](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/build-with-claude/fast-mode.md?plain=1#L141-L149)] [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]

#### [Claude Code Analytics API](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/manage-claude/claude-code-analytics-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/claude-code-analytics-api)]

* Added a link to the Compliance API in the "See also" section. [[line 263](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/manage-claude/claude-code-analytics-api.md?plain=1#L263)] [[Source](https://platform.claude.com/docs/en/manage-claude/claude-code-analytics-api)]

#### [Rate Limits API](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/manage-claude/rate-limits-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/rate-limits-api)]

* Updated rate limit example values: `input_tokens_per_minute` raised from 2,000,000 to 10,000,000; `output_tokens_per_minute` raised from 400,000 to 800,000. [[lines 68-69](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/manage-claude/rate-limits-api.md?plain=1#L68-L69)] [[Source](https://platform.claude.com/docs/en/manage-claude/rate-limits-api)]

#### [Usage and Cost API](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/manage-claude/usage-cost-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/usage-cost-api)]

* All cURL code examples updated to use `$ANTHROPIC_ADMIN_KEY` instead of `$ADMIN_API_KEY` as the environment variable name, aligning with the naming convention used elsewhere. [[multiple lines](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/manage-claude/usage-cost-api.md?plain=1#L49)]

#### [Handle streaming refusals](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals.md) [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)]

* Updated guidance on resetting context after a `stop_reason: refusal` response: users can now remove, rephrase, or clear the entire conversation history (previously only "remove or update the turn" was mentioned). [[line 30](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals.md?plain=1#L30)] [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)]

#### [Tool runner](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/agents-and-tools/tool-use/tool-runner.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner)]

* Code example for accessing the final message result updated to iterate over content blocks and check `block.type == "text"` instead of directly accessing `content[0].text`, making it more robust when multiple content blocks are present. [[lines 143-145](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/agents-and-tools/tool-use/tool-runner.md?plain=1#L143-L145)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner)]

#### [Tool search tool](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/agents-and-tools/tool-use/tool-search-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)]

* Fixed a bug in the error response example: the `type` field was incorrectly shown as `tool_result` but should be `tool_search_tool_result`. [[line 283](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/agents-and-tools/tool-use/tool-search-tool.md?plain=1#L283)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)]

#### [Messages API reference (create)](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/api/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/messages/create)]

* The cURL request example was expanded to include additional fields: `system`, `temperature`, `thinking` (with `type: "adaptive"`), `tools`, `top_k`, and `top_p`. [[lines 6572-6610](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/api/messages/create.md?plain=1#L6572-L6610)] [[Source](https://platform.claude.com/docs/en/api/messages/create)]

#### [Beta Messages API reference (create)](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/api/beta/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]

* Same cURL example expansion as the non-beta messages/create.md, adding system, temperature, thinking, tools, top_k, and top_p fields. [[lines 9194-9232](https://github.com/gpambrozio/ClaudeDocs/blob/eafe057/docs-md/api/api/beta/messages/create.md?plain=1#L9194-L9232)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]
