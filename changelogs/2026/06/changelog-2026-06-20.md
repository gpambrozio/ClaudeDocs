# [Claude docs changes for June 20th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/02bab96af33cc1c7e96a77ae0e179555170c5523) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/02bab96af33cc1c7e96a77ae0e179555170c5523)]

## Executive Summary
- New `disableClaudeAiConnectors` setting lets you disable claude.ai MCP connectors at any settings scope (user, project, org), giving per-project control over cloud connectors
- Auto permission mode expanded to block more destructive operations: `git reset --hard`, `git stash drop/clear`, `git commit --amend` on pre-session commits, and Terraform/Pulumi/CDK destroy commands
- New `SDKRateLimitEvent` fields (`errorCode`, `canUserPurchaseCredits`, `hasChargeableSavedPaymentMethod`) allow SDK callers to detect and handle credits-exhausted subscription scenarios
- `/config` command now accepts named shorthand keys (e.g. `/config theme=dark`, `/config model=sonnet`) and `--help` lists all settable keys
- Two new env vars: `CLAUDE_CODE_CONNECT_TIMEOUT_MS` for API streaming timeouts and `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS` for capping background subagent wait in non-interactive mode

## New Claude Code versions

No new versions today.

-----

## Claude Code changes

### Changed documents

#### [Agent SDK: Claude Code Features](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/agent-sdk/claude-code-features.md) [[Source](https://code.claude.com/docs/en/agent-sdk/claude-code-features)]

* Added `disableClaudeAiConnectors: true` as an alternative to `strictMcpConfig: true` or the `ENABLE_CLAUDEAI_MCP_SERVERS=false` env var for suppressing claude.ai MCP connectors. [[line 57](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/agent-sdk/claude-code-features.md?plain=1#L57)] [[Source](https://code.claude.com/docs/en/agent-sdk/claude-code-features#what-settingsources-does-not-control)]

#### [Agent SDK: TypeScript Reference](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Added three new optional fields to `SDKRateLimitEvent`: `errorCode` (set to `"credits_required"` when a claude.ai subscription's included usage is exhausted), `canUserPurchaseCredits`, and `hasChargeableSavedPaymentMethod`. Requires Claude Code v2.1.181 or later. [[lines 3234-3248](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L3234-L3248)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkratelimitevent)]

#### [Claude Code on the Web](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* From v2.1.182, the new `attribution.sessionUrl` setting can be set to `false` to omit the `Claude-Session` git trailer and PR-body session link that web sessions add by default. [[line 104](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L104)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#link-output-back-to-the-session)]

#### [Commands](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/config` now accepts named shorthand keys as of v2.1.182, such as `/config theme=dark` or `/config model=sonnet`. The help flag changed from `help` to `--help`, and the description now says it lists every settable key with its options. [[line 46](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/commands.md?plain=1#L46)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]

#### [Environment Variables](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_CONNECT_TIMEOUT_MS` env var sets the timeout (default 60s) for the connect, TLS, and response-header phase of a streaming API request. Set to `0` to rely on `API_TIMEOUT_MS` alone. [[line 149](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/env-vars.md?plain=1#L149)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS` env var controls how long non-interactive mode (`-p`) waits for background subagents and workflows. Default is 10 minutes; set to `0` to wait indefinitely. [[line 230](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/env-vars.md?plain=1#L230)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `ENABLE_CLAUDEAI_MCP_SERVERS` documentation now notes that `disableClaudeAiConnectors` in settings is the preferred way to disable connectors per-project or per-org. [[line 303](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/env-vars.md?plain=1#L303)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [Headless Mode](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* Background subagents and workflows are now exempt from the 5-second grace period and instead wait until complete. From v2.1.182, that wait is capped at 10 minutes by default to prevent a stuck agent from holding the process open indefinitely. Configurable via `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS`. [[lines 52-53](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/headless.md?plain=1#L52-L53)] [[Source](https://code.claude.com/docs/en/headless#background-tasks-at-exit)]

#### [Keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* Settings context actions updated: `settings:close` replaced by `select:accept` (Enter/Space) and `confirm:no` (Escape). Clarification added that settings apply immediately as you change them, so Escape closes with changes saved. [[lines 296-302](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/keybindings.md?plain=1#L296-L302)] [[Source](https://code.claude.com/docs/en/keybindings#settings-actions)]

#### [Managed MCP](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/managed-mcp.md) [[Source](https://code.claude.com/docs/en/managed-mcp)]

* Expanded explanation of `serverName` validation differences between `allowedMcpServers` and `deniedMcpServers`: in deny lists, any non-empty string is accepted (including claude.ai connector display names like `"claude.ai Slack"`); in allow lists, only letters, numbers, hyphens, and underscores are accepted. [[lines 129-137](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/managed-mcp.md?plain=1#L129-L137)] [[Source](https://code.claude.com/docs/en/managed-mcp#match-servers-by-url-command-or-name)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* New "Disable claude.ai connectors" section documents the `disableClaudeAiConnectors` settings key (any-source-true semantics), the existing `ENABLE_CLAUDEAI_MCP_SERVERS=false` env var alternative, and guidance on blocking individual connectors via `deniedMcpServers`. Also clarifies that `disableClaudeAiConnectors` does not apply to Claude Code on the web sessions. [[lines 742-769](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/mcp.md?plain=1#L742-L769)] [[Source](https://code.claude.com/docs/en/mcp#use-mcp-servers-from-claude-ai)]

#### [Model Configuration](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* From v2.1.182, model retirement and remapping warnings are now written to stderr in non-interactive mode when using the default text output format. The warning is suppressed for `--output-format json` and `stream-json`; use the `modelUsage` field of the result message instead. [[line 69](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/model-config.md?plain=1#L69)] [[Source](https://code.claude.com/docs/en/model-config#setting-your-model)]

#### [Permission Modes](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Auto permission mode now blocks additional destructive operations: `git reset --hard`, `git checkout -- .`, `git restore .`, `git clean -fd`, `git stash drop`, `git stash clear` (presumed to discard uncommitted changes); `git commit --amend` when the HEAD commit was not created in this session; and `terraform destroy`, `pulumi destroy`, `cdk destroy`, `terragrunt destroy` (plus any plan that destroys resources). [[lines 180-182](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/permission-modes.md?plain=1#L180-L182)] [[Source](https://code.claude.com/docs/en/permission-modes#what-the-classifier-blocks-by-default)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New `disableClaudeAiConnectors` setting documented: disables claude.ai MCP connectors globally. Uses any-source-true semantics — a project-level `false` cannot override a user- or policy-level `true`. Requires v2.1.182+. [[line 214](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/settings.md?plain=1#L214)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* New `remoteControlAtStartup` setting: connects Remote Control automatically at every interactive session start. Appears in `/config` as "Enable Remote Control for all sessions". [[line 257](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/settings.md?plain=1#L257)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* New `attribution.sessionUrl` sub-setting: controls whether the claude.ai session link is appended as a `Claude-Session` trailer on commits and a link in PR descriptions. Defaults to `true`. [[line 423](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/claude-code/settings.md?plain=1#L423)] [[Source](https://code.claude.com/docs/en/settings#attribution-settings)]

-----

## API changes

### Changed documents

#### [Multilingual Support](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/api/build-with-claude/multilingual-support.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/multilingual-support)]

* New "Set the response language" section added with code examples and guidance on explicitly setting the response language in the system prompt for production applications. [[lines 43-57](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/api/build-with-claude/multilingual-support.md?plain=1#L43-L57)] [[Source](https://platform.claude.com/docs/en/build-with-claude/multilingual-support)]
* Expanded "Next steps" section with links to customer support agent guide, models overview, and evaluation guidance. [[lines 82-93](https://github.com/gpambrozio/ClaudeDocs/blob/02bab96af33cc1c7e96a77ae0e179555170c5523/docs-md/api/build-with-claude/multilingual-support.md?plain=1#L82-L93)] [[Source](https://platform.claude.com/docs/en/build-with-claude/multilingual-support)]
