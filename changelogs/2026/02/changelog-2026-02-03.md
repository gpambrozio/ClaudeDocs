# [Claude docs changes for February 3rd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/04448f07318631d89b108215bf121d1ae35c5d48) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/04448f07318631d89b108215bf121d1ae35c5d48)]

## Claude Code changes

### New Documents

#### [Authentication](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/authentication.md) [[Source](https://code.claude.com/docs/en/authentication)]

New comprehensive guide covering authentication methods for Claude Code. Documents three primary authentication approaches: Claude for Teams/Enterprise (recommended for organizations), Claude Console authentication (for API-based billing), and cloud provider authentication (Bedrock, Vertex AI, Microsoft Foundry). Includes detailed setup steps for each method, credential management details (macOS Keychain storage, supported auth types, custom credential scripts via `apiKeyHelper`), and refresh interval configuration via `CLAUDE_CODE_API_KEY_HELPER_TTL_MS`.

#### [Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

New detailed documentation for Claude Code's permission system. Covers the tiered permission system (read-only, Bash commands, file modifications), permission modes (default, acceptEdits, plan, dontAsk, bypassPermissions), and comprehensive permission rule syntax including wildcard patterns. Documents tool-specific rules for Bash, Read/Edit (using gitignore patterns), WebFetch (domain-based), MCP tools, and Task subagents. Includes guidance on working directories, how permissions interact with sandboxing, managed settings for enterprise deployments, settings precedence, and example configurations.

### Changed documents

#### [Analytics](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/analytics.md) [[Source](https://code.claude.com/docs/en/analytics)]

* Updated "See also" reference from `iam.md` to `permissions.md`. [[line 209](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/analytics.md?plain=1#L209)] [[Source](https://code.claude.com/docs/en/analytics#related-resources)]

#### [CLI Reference](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Updated `--permission-mode` flag documentation link from `iam.md` to `permissions.md`. [[line 52](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/cli-reference.md?plain=1#L52)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [Desktop](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Updated permission modes documentation reference from `iam.md` to `permissions.md`. [[line 105](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/desktop.md?plain=1#L105)] [[Source](https://code.claude.com/docs/en/desktop#choose-a-permission-mode)]

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Updated `permission_mode` field description link from `iam.md` to `permissions.md`. [[line 406](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/hooks.md?plain=1#L406)] [[Source](https://code.claude.com/docs/en/hooks#common-input-fields)]

#### [How Claude Code Works](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/how-claude-code-works.md) [[Source](https://code.claude.com/docs/en/how-claude-code-works)]

* Updated permissions documentation reference from `iam.md` to `permissions.md`. [[line 121](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/how-claude-code-works.md?plain=1#L121)] [[Source](https://code.claude.com/docs/en/how-claude-code-works#control-what-claude-can-do)]

#### [Interactive Mode](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Updated `/permissions` command documentation link from `iam.md` to `permissions.md`. [[line 89](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/interactive-mode.md?plain=1#L89)] [[Source](https://code.claude.com/docs/en/interactive-mode#built-in-commands)]

#### [Monitoring Usage](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Added new `OTEL_LOG_TOOL_DETAILS` environment variable to enable logging of MCP server/tool names and skill names in tool events (disabled by default for privacy). [[line 86](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/monitoring-usage.md?plain=1#L86)] [[Source](https://code.claude.com/docs/en/monitoring-usage#common-configuration-variables)]
* Added `event.sequence` attribute to user_prompt event for ordering events within a session. [[line 340](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/monitoring-usage.md?plain=1#L340)] [[Source](https://code.claude.com/docs/en/monitoring-usage#user-prompt-event)]
* Added `event.sequence` attribute to tool_result event for ordering events within a session. [[line 353](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/monitoring-usage.md?plain=1#L353)] [[Source](https://code.claude.com/docs/en/monitoring-usage#tool-result-event)]
* Enhanced tool_parameters for MCP tools to include `mcp_server_name` and `mcp_tool_name` when `OTEL_LOG_TOOL_DETAILS=1`. [[lines 362-363](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/monitoring-usage.md?plain=1#L362-L363)] [[Source](https://code.claude.com/docs/en/monitoring-usage#tool-result-event)]
* Added `event.sequence` attribute to api_request event for ordering events within a session. [[line 374](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/monitoring-usage.md?plain=1#L374)] [[Source](https://code.claude.com/docs/en/monitoring-usage#api-request-event)]
* Added `event.sequence` attribute to api_error event for ordering events within a session. [[line 392](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/monitoring-usage.md?plain=1#L392)] [[Source](https://code.claude.com/docs/en/monitoring-usage#api-error-event)]
* Added `event.sequence` attribute to tool_decision event for ordering events within a session. [[line 408](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/monitoring-usage.md?plain=1#L408)] [[Source](https://code.claude.com/docs/en/monitoring-usage#tool-decision-event)]
* Added privacy note about MCP server/tool names and skill names not being logged by default. [[line 496](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/monitoring-usage.md?plain=1#L496)] [[Source](https://code.claude.com/docs/en/monitoring-usage#security/privacy-considerations)]

#### [Quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/quickstart.md) [[Source](https://code.claude.com/docs/en/quickstart)]

* Updated credential management documentation link from `iam.md` to `authentication.md`. [[line 120](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/quickstart.md?plain=1#L120)] [[Source](https://code.claude.com/docs/en/quickstart#step-3:-start-your-first-session)]

#### [Sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Updated Claude permission settings reference from `iam.md` to `permissions.md`. [[line 124](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/sandboxing.md?plain=1#L124)] [[Source](https://code.claude.com/docs/en/sandboxing#protection-against-prompt-injection)]
* Added new section explaining how sandboxing relates to permissions, clarifying that they are complementary security layers. [[lines 169-182](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/sandboxing.md?plain=1#L169-L182)] [[Source](https://code.claude.com/docs/en/sandboxing#how-sandboxing-relates-to-permissions)]
* Updated IAM policies reference to "Permission rules" with link to `permissions.md`. [[line 214](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/sandboxing.md?plain=1#L214)] [[Source](https://code.claude.com/docs/en/sandboxing#integration-with-existing-security-tools)]
* Updated "See also" reference from `iam.md` to `permissions.md`. [[line 249](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/sandboxing.md?plain=1#L249)] [[Source](https://code.claude.com/docs/en/sandboxing#see-also)]

#### [Security](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/security.md) [[Source](https://code.claude.com/docs/en/security)]

* Updated permission configuration documentation link from `iam.md` to `permissions.md`. [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/security.md?plain=1#L11)] [[Source](https://code.claude.com/docs/en/security#permission-based-architecture)]
* Updated permission pattern limitations reference from `iam.md` to `permissions.md`. [[line 35](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/security.md?plain=1#L35)] [[Source](https://code.claude.com/docs/en/security#core-protections)]
* Updated credential storage documentation link from `iam.md` to `authentication.md`. [[line 56](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/security.md?plain=1#L56)] [[Source](https://code.claude.com/docs/en/security#additional-safeguards)]
* Updated managed settings reference from `iam.md` to `permissions.md`. [[line 105](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/security.md?plain=1#L105)] [[Source](https://code.claude.com/docs/en/security#team-security)]
* Updated "Related resources" reference from `iam.md` to `permissions.md`. [[line 122](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/security.md?plain=1#L122)] [[Source](https://code.claude.com/docs/en/security#related-resources)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Updated managed settings documentation reference from `iam.md` to `permissions.md`. [[line 87](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/settings.md?plain=1#L87)] [[Source](https://code.claude.com/docs/en/settings#settings-files)]
* Added new `allowManagedPermissionRulesOnly` setting for managed settings to prevent user/project permission rules. [[line 147](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/settings.md?plain=1#L147)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* Simplified permission rule syntax documentation with condensed examples and reference to full permissions page. [[lines 186-195](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/settings.md?plain=1#L186-L195)] [[Source](https://code.claude.com/docs/en/settings#permission-rule-syntax)]
* Updated various permission-related setting documentation links from `iam.md` to `permissions.md`. [[lines 179-182](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/settings.md?plain=1#L179-L182)] [[Source](https://code.claude.com/docs/en/settings#permission-settings)]

#### [Setup](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* Updated managed settings reference from `iam.md` to `permissions.md`. [[line 272](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/setup.md?plain=1#L272)] [[Source](https://code.claude.com/docs/en/setup#configure-release-channel)]

#### [Skills](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Updated enterprise skills location reference from `iam.md` to `permissions.md`. [[line 87](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/skills.md?plain=1#L87)] [[Source](https://code.claude.com/docs/en/skills#where-skills-live)]
* Updated permission settings reference from `iam.md` to `permissions.md`. [[line 459](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/skills.md?plain=1#L459)] [[Source](https://code.claude.com/docs/en/skills#restrict-claude’s-skill-access)]
* Updated permission rules documentation link from `iam.md` to `permissions.md`. [[line 472](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/skills.md?plain=1#L472)] [[Source](https://code.claude.com/docs/en/skills#restrict-claude’s-skill-access)]
* Updated managed settings reference from `iam.md` to `permissions.md`. [[line 498](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/skills.md?plain=1#L498)] [[Source](https://code.claude.com/docs/en/skills#share-skills)]
* Updated "See also" reference from `iam.md` to `permissions.md`. [[line 730](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/skills.md?plain=1#L730)] [[Source](https://code.claude.com/docs/en/skills#related-resources)]

#### [Sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Updated permission rules documentation reference from `iam.md` to `permissions.md`. [[line 367](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/sub-agents.md?plain=1#L367)] [[Source](https://code.claude.com/docs/en/sub-agents#disable-specific-subagents)]

#### [Third-party Integrations](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/third-party-integrations.md) [[Source](https://code.claude.com/docs/en/third-party-integrations)]

* Updated Claude for Teams/Enterprise and Anthropic Console links from `iam.md` to `authentication.md`. [[lines 26-27](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/third-party-integrations.md?plain=1#L26-L27)] [[Source](https://code.claude.com/docs/en/third-party-integrations#compare-deployment-options)]

#### [Troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/troubleshooting.md) [[Source](https://code.claude.com/docs/en/troubleshooting)]

* Updated permissions documentation reference from `iam.md` to `permissions.md`. [[line 190](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/claude-code/troubleshooting.md?plain=1#L190)] [[Source](https://code.claude.com/docs/en/troubleshooting#repeated-permission-prompts)]

-----

## API changes

### Changed documents

#### [Extended Thinking](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Updated contact sales email protection string. [[line 98](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L98)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

#### [Files](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Updated contact email protection string for API limits. [[line 284](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/api/build-with-claude/files.md?plain=1#L284)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

#### [System Prompts](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/api/release-notes/system-prompts.md) [[Source](https://platform.claude.com/docs/en/release-notes/system-prompts)]

* Added January 18, 2026 system prompt update entries for Claude Opus 4.5, Haiku 4.5, and Sonnet 4.5. [[lines 9, 13, 23](https://github.com/gpambrozio/ClaudeDocs/blob/04448f07318631d89b108215bf121d1ae35c5d48/docs-md/api/release-notes/system-prompts.md?plain=1#L9-L23)]
