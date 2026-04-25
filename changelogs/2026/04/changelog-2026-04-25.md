# [Claude docs changes for April 25th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/0418eeb9af77a400553825f4711ccecb9ffe9c81) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/0418eeb9af77a400553825f4711ccecb9ffe9c81)]

## Executive Summary
- New **Rate Limits API** allows admins to programmatically read rate limits for their organization and workspaces, enabling gateways and alerting systems to stay in sync without hardcoded values
- **PostToolUse and PostToolUseFailure hooks** now include a `duration_ms` field exposing tool execution time in milliseconds
- Several Claude Code settings (`autoScrollEnabled`, `editorMode`, `showTurnDuration`, `teammateMode`, `terminalProgressBarEnabled`) moved from `~/.claude.json` to `~/.claude/settings.json`, with three new settings added (`prUrlTemplate`, `autoScrollEnabled` documented in settings)
- **Microsoft 365 MCP server** added as a built-in remote MCP connector for SharePoint, OneDrive, Outlook, and Teams access
- **Legacy Amazon Bedrock** integration now has its own dedicated documentation page, separated from the modern Messages API Bedrock page

## New Claude Code versions

### [2.1.116](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/versions/2.1.116.md)

*Note: This version was previously documented; the following entry was added:*

* Claude Code and installer now use `https://downloads.claude.ai/claude-code-releases` as the download URL (changed from the previous Google Storage bucket URL)

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Added optional `duration_ms` field to `PostToolUseHookInput` and `PostToolUseFailureHookInput` types, exposing tool execution time in milliseconds [[line 1116](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1116)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#posttoolusehookinput)]
* Added optional `aliases` field to the `SlashCommand` type [[line 2260](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L2260)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#slashcommand)]

#### [agent-teams](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

* Updated reference for `teammateMode` setting: configuration is now stored in `~/.claude/settings.json` rather than `~/.claude.json`

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* `--from-pr` flag now accepts GitHub Enterprise PR URLs, GitLab merge request URLs, and Bitbucket pull request URLs in addition to GitHub PR numbers and URLs [[line 57](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/cli-reference.md?plain=1#L57)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_HIDE_CWD` environment variable: set to `1` to hide the working directory from the startup logo, useful during screenshares [[line 96](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/env-vars.md?plain=1#L96)] [[Source](https://code.claude.com/docs/en/env-vars)]
* Updated `ENABLE_TOOL_SEARCH` documentation to note it is now also disabled by default on Vertex AI (not just non-first-party base URLs)

#### [google-vertex-ai](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/google-vertex-ai.md) [[Source](https://code.claude.com/docs/en/google-vertex-ai)]

* Added explicit note that MCP tool search is disabled by default on Vertex AI because the endpoint does not accept the required beta header; all MCP tool definitions load upfront instead. Set `ENABLE_TOOL_SEARCH=true` to opt in

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* `PostToolUse` hook payload now includes `duration_ms`: tool execution time in milliseconds, excluding time spent in permission prompts and PreToolUse hooks [[line 1200](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/hooks.md?plain=1#L1200)] [[Source](https://code.claude.com/docs/en/hooks#posttooluse-input)]
* `PostToolUseFailure` hook payload also gains `duration_ms` [[line 1256](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/hooks.md?plain=1#L1256)] [[Source](https://code.claude.com/docs/en/hooks#posttoolusefailure-input)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Added **Microsoft 365** as a built-in remote MCP server, giving access to SharePoint, OneDrive, Outlook, and Teams [[line 451](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/mcp.md?plain=1#L451)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* Updated tool search documentation: MCP tool search is now also disabled by default on Vertex AI, and `ENABLE_TOOL_SEARCH=true` explicitly opts in for both Vertex AI and non-first-party base URLs
* Removed outdated Windows-specific note about requiring `cmd /c` wrapper for `npx`-based MCP servers

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* OTel tool completion events now include `tool_use_id`, allowing correlation between OpenTelemetry events and hook-captured data [[line 481](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/monitoring-usage.md?plain=1#L481)] [[Source](https://code.claude.com/docs/en/monitoring-usage#tool-result-event)]
* OTel tool completion events now also include `tool_input_size_bytes`: size of the JSON-serialized tool input [[line 488](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/monitoring-usage.md?plain=1#L488)] [[Source](https://code.claude.com/docs/en/monitoring-usage#tool-result-event)]
* `tool_use_id` also added to OTel tool permission decision events [[line 586](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/monitoring-usage.md?plain=1#L586)] [[Source](https://code.claude.com/docs/en/monitoring-usage#tool-decision-event)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Auto mode now also drops blanket `PowerShell(*)` allow rules on entry, the same way it drops `Bash(*)` [[line 176](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/permission-modes.md?plain=1#L176)] [[Source](https://code.claude.com/docs/en/permission-modes#when-auto-mode-falls-back)]

#### [plugin-dependencies](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/plugin-dependencies.md) [[Source](https://code.claude.com/docs/en/plugin-dependencies)]

* Clarified auto-update behavior for constrained dependencies: auto-update now fetches at the highest git tag satisfying all installed plugins' ranges rather than skipping the update entirely when the marketplace latest doesn't satisfy constraints [[line 96](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/plugin-dependencies.md?plain=1#L96)] [[Source](https://code.claude.com/docs/en/plugin-dependencies#how-constraints-interact)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* `autoScrollEnabled`, `editorMode`, `showTurnDuration`, `teammateMode`, and `terminalProgressBarEnabled` moved from `~/.claude.json` (non-settings config) to `settings.json` starting with v2.1.119 [[line 222](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/settings.md?plain=1#L222)] [[Source](https://code.claude.com/docs/en/settings#global-config-settings)]
* New `prUrlTemplate` setting: URL template for the PR badge in the footer and tool-result summaries, allowing links to point at an internal code-review tool instead of `github.com` [[line 197](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/settings.md?plain=1#L197)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

#### [statusline](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/statusline.md) [[Source](https://code.claude.com/docs/en/statusline)]

* New `effort.level` field in status line JSON: current reasoning effort level (`low`, `medium`, `high`, `xhigh`, `max`), reflecting live mid-session `/effort` changes [[line 154](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/statusline.md?plain=1#L154)] [[Source](https://code.claude.com/docs/en/statusline#available-data)]
* New `thinking.enabled` field: whether extended thinking is enabled for the session [[line 155](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/statusline.md?plain=1#L155)] [[Source](https://code.claude.com/docs/en/statusline#available-data)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* Removed the limitation note that auto mode does not work with the PowerShell tool (now supported)

-----

## API changes

### New Documents

#### [api/admin/rate_limits](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/api/admin/rate_limits.md) [[Source](https://platform.claude.com/docs/en/api/admin/rate_limits)]

API reference index for the Admin Rate Limits resource, providing an overview of the `RateLimitListResponse` model for organization-level rate limit queries.

#### [api/admin/rate_limits/list](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/api/admin/rate_limits/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/rate_limits/list)]

Full API reference for `GET /v1/organizations/rate_limits`. Lists all rate limit groups (model groups, batch, files, token count, skills, web search) with their configured limiter values. Supports filtering by `group_type` or by `model` string.

#### [api/admin/workspaces/rate_limits](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/api/admin/workspaces/rate_limits.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits)]

API reference index for the Workspace Rate Limits resource, describing the `workspace_rate_limit` response model which includes `org_limit` for reference comparison.

#### [api/admin/workspaces/rate_limits/list](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/api/admin/workspaces/rate_limits/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list)]

Full API reference for `GET /v1/organizations/workspaces/{workspace_id}/rate_limits`. Returns only rate limit groups that have workspace-level overrides; groups without overrides inherit organization limits and are omitted.

#### [build-with-claude/claude-on-amazon-bedrock-legacy](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/build-with-claude/claude-on-amazon-bedrock-legacy.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)]

New dedicated page for the legacy Amazon Bedrock integration using the `InvokeModel` and `Converse` APIs with ARN-versioned model identifiers. Covers authentication, bearer tokens, available model IDs with regional availability, global vs. regional endpoints, and PDF support. Claude Opus 4.7 is noted as available only through the modern Messages API endpoint.

#### [build-with-claude/rate-limits-api](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/build-with-claude/rate-limits-api.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/rate-limits-api)]

New guide for the Rate Limits API, providing programmatic access to rate limits for organizations and workspaces. Documents use cases (gateway sync, internal alerting, workspace audit), organization and workspace endpoints, filtering by group type, pagination, and an FAQ. Requires Admin API key.

### Changed documents

#### [agents-and-tools/remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Added **Microsoft 365** as a built-in remote MCP server for SharePoint, OneDrive, Outlook, and Teams access

#### [agents-and-tools/tool-use/build-a-tool-using-agent](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/agents-and-tools/tool-use/build-a-tool-using-agent.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent)]

* Added cURL, CLI, and TypeScript code examples for the single-turn and multi-turn tool-use examples (previously Python only)

#### [agents-and-tools/tool-use/define-tools](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/agents-and-tools/tool-use/define-tools.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)]

* Updated recommended model to Claude Opus 4.7 (previously 4.6) and added multi-language code examples

#### [agents-and-tools/tool-use/parallel-tool-use](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/agents-and-tools/tool-use/parallel-tool-use.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use)]

* Updated model references to Claude Opus 4.7 and added multi-language code examples

#### [agents-and-tools/tool-use/server-tools](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/agents-and-tools/tool-use/server-tools.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools)]

* Updated model references to Claude Opus 4.7 and added multi-language code examples

#### [agents-and-tools/tool-use/strict-tool-use](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/agents-and-tools/tool-use/strict-tool-use.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use)]

* Quick start example now uses Python code and multi-language tabs instead of a shell curl command; model updated to Claude Opus 4.7

#### [agents-and-tools/tool-use/tool-runner](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/agents-and-tools/tool-use/tool-runner.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner)]

* Updated model references throughout from Claude Opus 4.6 to Claude Opus 4.7

#### [api/admin](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/api/admin.md) [[Source](https://platform.claude.com/docs/en/api/admin)]

* Added Workspace Rate Limits section documenting the new `GET /v1/organizations/workspaces/{workspace_id}/rate_limits` endpoint
* Added Organization Rate Limits section documenting the new `GET /v1/organizations/rate_limits` endpoint
* `"managed"` role removed from user and invite role enums
* Usage report results now include `account_id` (user account that made the request) and `service_account_id` (OIDC-federation service account)
* Cost report: added `"session_usage"` as a new `cost_type` value; removed the `speed` field (fast mode research preview)

#### [api/admin/cost_report/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/api/admin/cost_report/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve)]

* Added `"session_usage"` as a valid `cost_type` value in cost reports
* Removed `speed` field (was a fast-mode research preview field) from cost report results

#### [api/admin/invites/create](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/api/admin/invites/create.md) [[Source](https://platform.claude.com/docs/en/api/admin/invites/create)]

* `"managed"` role removed from the list of valid invite roles

#### [api/admin/usage_report/retrieve_messages](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/api/admin/usage_report/retrieve_messages.md) [[Source](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages)]

* New `account_ids` filter parameter to restrict usage to specific user accounts [[line 18](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/api/admin/usage_report/retrieve_messages.md?plain=1#L18)] [[Source](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages)]
* New `service_account_ids` filter parameter to restrict usage to specific OIDC-federation service accounts [[line 105](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/api/admin/usage_report/retrieve_messages.md?plain=1#L105)] [[Source](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages)]
* New `account_id` and `service_account_id` options added to the `group_by` parameter [[lines 72-74](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/api/admin/usage_report/retrieve_messages.md?plain=1#L72-L74)] [[Source](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages)]

#### [api/admin/workspaces](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/api/admin/workspaces.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces)]

* Added Workspace Rate Limits section with the new endpoint reference

#### [api/rate-limits](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/api/rate-limits.md) [[Source](https://platform.claude.com/docs/en/api/rate-limits)]

* Added reference to the new Rate Limits API for programmatically reading current rate limit configuration
* Workspace rate limits section updated: removed the "Support for input and output token limits coming in future" note (now available); added note that workspace limits are set per limiter type; added `Workspace limits are set per limiter type` clarification

#### [build-with-claude/administration-api](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/build-with-claude/administration-api.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/administration-api)]

* Added new "Rate limits" section linking to the Rate Limits API guide

#### [build-with-claude/claude-in-amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/build-with-claude/claude-in-amazon-bedrock.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)]

* Updated link to legacy Bedrock integration to point to the new dedicated `claude-on-amazon-bedrock-legacy.md` page

#### [managed-agents/memory](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/managed-agents/memory.md) [[Source](https://platform.claude.com/docs/en/managed-agents/memory)]

* Fixed memory version listing code example: the paginated list result is now stored in a variable before iterating, and a `version_id` extraction example is shown

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* Added April 24, 2026 entry announcing the Rate Limits API

#### [build-with-claude/workspaces](https://github.com/gpambrozio/ClaudeDocs/blob/0418eeb9af77a400553825f4711ccecb9ffe9c81/docs-md/api/build-with-claude/workspaces.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/workspaces)]

* Added reference to the Rate Limits API for programmatic rate limit reads alongside the existing link to the rate limits documentation
