# [Claude docs changes for November 21st, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/0e63f67d8201a8007cce96c41fba15e588895a4d) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/0e63f67d8201a8007cce96c41fba15e588895a4d)]

## Executive Summary
- Claude Code 2.1.330 adds sign-in to organizations managed in Anthropic's Enterprise Admin Console, with a new managed-only `enforceAnthropicSignIn` setting to require it.
- A new built-in "easel" mod (`cc-plugin-easel`) draws charts on request and under MCP time-series results.
- WebFetch now works through a built-in `web-fetch` subagent. Its docs cover domain allow/deny rules, which model it runs on, and how managed-settings hooks apply to it.
- A new Claude Code Managed Settings Admin API (beta, Enterprise only) manages settings configuration and RBAC groups.
- The Compliance API gained about 13 new activity types, and the API reference renamed several error types (for example `WebSearchToolResultErrorObject`).

## New Claude Code versions

### [2.1.330](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/versions/2.1.330.md)

#### New features

* Sign-in to organizations managed in Anthropic's Enterprise Admin Console via `claude auth login`. The organization's settings and its cloud provider or gateway then apply.
* Built-in "easel" mod that draws charts on request and under MCP metrics results (Pro, Max, and where available Team and Enterprise, on macOS and Linux). Automatic charts can be turned off in `/config`.
* `CLAUDE_CODE_FULL_SIGN_IN_LINK=1` prints the full sign-in link.
* Self-hosted runner: `--start-dir` / `SELF_HOSTED_RUNNER_START_DIR`, new notices for plugin marketplace and git problems, and two new `/metrics` timing metrics.
* `claude plugin install --json` results now include `commandPrinted` and `commandFailed`.
* VS Code: `/fork`, `/workflows`, and the `claudeCode.escapeStopsClaude`, `claudeCode.pinPrompt` and `claudeCode.contextUsageThreshold` settings. The "Open in Side Bar" command takes a `prompt` argument, and session groups can be moved up and down.

#### Existing feature improvements

* Recurring scheduled tasks and `/loop` now run up to 30 days instead of 7.
* More `rm` commands aimed at the root, home or a top-level folder now ask for approval (refused where nobody can answer).
* `deniedMcpServers` name entries now hide only the named claude.ai connector, not others at the same URL.
* Prompt hooks accept model aliases such as `haiku` or `sonnet` in `model`.
* The claude.ai sign-in link is much shorter.
* Faster Grep and Glob on Windows, and faster file diffs.
* `/config` search ranks name-prefix matches first, and `/resume` no longer lists sessions where you only opened a screen.
* Reconnect in `/mcp` and `/plugin` keeps the server page open with the cause visible.
* `/ultrareview` cost confirmation shows the remaining monthly spend limit on Team and Enterprise.
* Code Mode: Claude is told how to view images and PDFs, "Interrupted" replaces the red error after Esc, and the terminal freezes for far less time after a subagent script makes thousands of tool calls.
* Self-hosted runner: `spawn-runner` hooks run concurrently (`--hook-concurrency`, default 4), and Bash skips the file diff unless `bashEditDiffEnabled` is true.
* Subagent progress summaries on a Claude apps gateway use far fewer tokens.

#### Major bug fixes

* Fixed freezes of up to several minutes after compacting a very long conversation, and WebFetch freezing or returning empty results.
* Fixed `ExitWorktree` and the worktree exit dialog deleting a worktree another session was using.
* Fixed lost user-settings changes, plugin lists, task metadata and `~/.claude.json` backups when several processes wrote at once.
* Fixed `--continue` and `--resume` failing on an invalid timestamp.
* Fixed "JSON schema is invalid" turn failures and huge session files when many MCP tools have schemas the API refuses.
* Fixed `/rewind` restoring older file versions with queued prompts or stacked skills.
* Fixed a shared MCP server declared by subagents being shut down when one subagent finished.
* Fixed `claude -p` exiting 0 on a full disk, and SessionStart hook environment variables being lost with `--continue`.
* Fixed several Code Mode problems: a long pause with many reads, chart tool failures, and MCP end-turn requests being ignored.
* Reverted 2.1.329's removal of the automatic retry when `max_tokens` exceeds a limit.
* Fixed many self-hosted runner and VS Code extension issues.

-----

## Claude Code changes

### Changed documents

#### [best-practices](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

* Removed the paragraph saying auto mode runs after deny/ask rules and `PreToolUse` hooks. [[line 398](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/best-practices.md?plain=1#L398)] [[Source](https://code.claude.com/docs/en/best-practices#change-the-permission-mode)]

#### [code-mode](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/code-mode.md) [[Source](https://code.claude.com/docs/en/code-mode)]

* New limits listed: refused tool calls when a `PreToolUse` hook doesn't finish, and Code Mode works only in an interactive terminal session (not the VS Code panel, Desktop or cloud). [[lines 41-51](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/code-mode.md?plain=1#L41-L51)] [[Source](https://code.claude.com/docs/en/code-mode#code-mode-limitations)]
* Rewrote the troubleshooting for "the hook did not finish" and "the hook failed". Documents the `onFailure` (`block` or `continue`) hook option on v2.1.329+. [[lines 323-332](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/code-mode.md?plain=1#L323-L332)] [[Source](https://code.claude.com/docs/en/code-mode#tool-call-refused-by-a-hook)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* Added error messages for Enterprise Admin Console organization sign-in, `enforceAnthropicSignIn`, and managed-settings sign-in conflicts. [[lines 107-113](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/errors.md?plain=1#L107-L113)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]
* Added errors for accounts on hold in Claude Design, `--fork-session` on cloud sessions, a branch not checked out on teleport, and claude.ai connectors that can't be removed. [[lines 125-300](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/errors.md?plain=1#L125-L300)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]
* Added errors for `/ultrareview` when the shell moved to another repository, macOS sandbox rule lists that are too long, tools blocked in the working folder, worktrees kept because another session uses them, a VS Code build mismatch, and invalid `--settings` JSON. [[lines 315-524](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/errors.md?plain=1#L315-L524)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Skill-frontmatter hooks are now described as removed when you exit or use `/clear` or `/resume`, with `once` to remove one sooner. [[line 680](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/hooks.md?plain=1#L680)] [[Source](https://code.claude.com/docs/en/hooks#hooks-in-skills-and-agents)]
* `PostToolUse` hooks from managed settings also run after some failed calls in the main conversation. For a failed call, `tool_response` is the error text. [[lines 2270-2293](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/hooks.md?plain=1#L2270-L2293)] [[Source](https://code.claude.com/docs/en/hooks#posttooluse)]
* For the built-in `web-fetch` subagent, `SubagentStart` and `SubagentStop` hooks run from managed settings only. Elsewhere, match `WebFetch` in `PreToolUse` or `PostToolUse`. [[lines 2659-2705](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/hooks.md?plain=1#L2659-L2705)] [[Source](https://code.claude.com/docs/en/hooks#subagentstart)]
* Clarified how `SubagentStart` context is re-injected after auto-compaction, and what `transcript_path` is for `SubagentStop`. [[lines 2693-2707](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/hooks.md?plain=1#L2693-L2707)] [[Source](https://code.claude.com/docs/en/hooks#subagentstart-input)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Updated for claude.ai connector handling (connectors can't be removed with `claude mcp remove`) and the `deniedMcpServers` name behavior.

#### [managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/managed-settings.md) [[Source](https://code.claude.com/docs/en/managed-settings)]

* Added `enforceAnthropicSignIn` as a sign-in requirement option, a pointer to the Enterprise Admin Console guide, and a note that the `policyHelper` `managedSettings` object is the only managed settings for the session. [[lines 50-229](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/managed-settings.md?plain=1#L50-L229)] [[Source](https://code.claude.com/docs/en/managed-settings#choose-a-delivery-mechanism)]

#### [plugins/mods/overview](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/plugins/mods/overview.md) [[Source](https://code.claude.com/docs/en/plugins/mods/overview)]

* Added the `cc-plugin-easel` charts mod, with a "Check the charts mod requirements" section: claude.ai subscription, v2.1.321+ (Team and Enterprise v2.1.326+), and macOS or Linux outside WSL. [[lines 230-244](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/plugins/mods/overview.md?plain=1#L230-L244)] [[Source](https://code.claude.com/docs/en/plugins/mods/overview#mods-built-into-claude-code)]
* Mod hooks run whichever provider serves the model. The table of where mods run now covers the Desktop Code tab, SSH sessions and cloud sessions. [[lines 183-194](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/plugins/mods/overview.md?plain=1#L183-L194)] [[Source](https://code.claude.com/docs/en/plugins/mods/overview#where-mods-run)]

#### [server-managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* Pointer to the Enterprise Admin Console guide for Desktop 3P setups. New "When endpoint-managed settings take over" section, and `enforceAnthropicSignIn` added to the no-merge exceptions. [[lines 10-199](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/server-managed-settings.md?plain=1#L10-L199)] [[Source](https://code.claude.com/docs/en/server-managed-settings#configure-server-managed-settings)]
* `apiKeyHelper` keys and Workload Identity Federation credentials don't trigger the settings fetch. [[line 400](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/server-managed-settings.md?plain=1#L400)] [[Source](https://code.claude.com/docs/en/server-managed-settings#platform-availability)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* New `enforceAnthropicSignIn` managed-only boolean setting to require a claude.ai login or an Enterprise Admin Console sign-in. It works with `forceLoginOrgUUID`. [[line 5286](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/settings-reference.md?plain=1#L5286)] [[Source](https://code.claude.com/docs/en/settings-reference#enforceanthropicsignin)]
* `forceLoginOrgUUID` can now be a single UUID or an array of organizations, and it stops the keyless Console sign-in. [[lines 5322-5348](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/settings-reference.md?plain=1#L5322-L5348)] [[Source](https://code.claude.com/docs/en/settings-reference#forceloginmethod)]
* `policyHelper` output replaces the managed settings source. Which cross-source keys still apply is documented, and a helper envelope without `managedSettings` contributes nothing. [[lines 5802-5807](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/settings-reference.md?plain=1#L5802-L5807)] [[Source](https://code.claude.com/docs/en/settings-reference#write-the-helper-output)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Added the built-in `web-fetch` subagent (Haiku, or the conversation's model when Haiku can't be used) to the helper-agent table. Where it is used, the main conversation and forks have no `WebFetch` tool of their own. [[lines 76-467](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/sub-agents.md?plain=1#L76-L467)] [[Source](https://code.claude.com/docs/en/sub-agents#built-in-subagents)]
* Under auto mode, the classifier evaluates subagent tool calls with the main conversation's rules and reviews a subagent's work when it finishes. [[line 617](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/sub-agents.md?plain=1#L617)] [[Source](https://code.claude.com/docs/en/sub-agents#permission-modes)]
* Duplicate subagent names across subfolders: only one is loaded, and `/doctor` reports it. A `tools` allowlist of Bash can still change files. [[lines 171-475](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/sub-agents.md?plain=1#L171-L475)] [[Source](https://code.claude.com/docs/en/sub-agents#choose-the-subagent-scope)]
* Removed the note that plan mode runs subagents on Opus or Sonnet for `opusplan` and `haiku`. [[line 371](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/sub-agents.md?plain=1#L371)] [[Source](https://code.claude.com/docs/en/sub-agents#which-model-a-nested-subagent-runs-on)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* Rewrote the WebFetch section. Claude asks a question about the page and usually doesn't see the full text. New subsections: "Allow a domain" (`WebFetch(domain:...)` rules and the auto-mode prompt behavior), "Block a site or turn WebFetch off" (`deny`, `ask`, `CLAUDE_CODE_DISABLE_WEB_FETCH`), and "When a fetch prompts, fails, or WebFetch is missing". It also covers the `web-fetch` subagent and its model. [[lines 656-720](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/claude-code/tools-reference.md?plain=1#L656-L720)] [[Source](https://code.claude.com/docs/en/tools-reference#allow-a-domain)]

#### Other Claude Code pages

* Many other pages (such as `claude-md`, `memory`, `skills`, `vs-code`, `ide-integrations`, `desktop`, `worktrees`, `cloud-environments`, `claude-code-on-the-web`, `plugins/cli-reference`, `plugins/mods/*`) were updated to match 2.1.330: VS Code settings, worktree cleanup, easel, Code Mode, and the Enterprise Admin Console sign-in.

-----

## API changes

### New Documents

#### [api/beta/organization/claude_code](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/api/api/beta/organization/claude_code.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/claude_code)]

New beta Claude Code Managed Settings Admin API (Claude Enterprise only), under `/v1/organizations/claude_code/managed_settings`. It needs an Admin API key with the `read:claude_code_managed_settings` scope and the beta header `anthropic-beta: ce-claude-code-managed-settings-2026-10-06`. It consists of 13 new pages:

* [managed_settings](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/api/api/beta/organization/claude_code/managed_settings.md): domain types and error codes (`cmek_feature_unsupported`, `rbac_group_order_limit_exceeded`, `settings_document_limit_exceeded`, `settings_history_limit_exceeded`, ...).
* [configuration](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/api/api/beta/organization/claude_code/managed_settings/configuration.md), with `retrieve` and `update`: read or change the settings mode and RBAC group order.
* [rbac_group_default](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/api/api/beta/organization/claude_code/managed_settings/rbac_group_default.md), with `retrieve` and `update`: the default settings applied to members.
* [rbac_groups](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/api/api/beta/organization/claude_code/managed_settings/rbac_groups.md), with `list`, `retrieve`, `set` and `delete`: per-RBAC-group managed settings.

### Changed documents

#### [api/compliance](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/api/api/compliance.md) [[Source](https://platform.claude.com/docs/en/api/compliance)]

* About 13 new activity types (630 total), including `ccr_session_feedback_submitted`, `ccr_session_file_added`, `claude_artifact_connector_share_created`/`_revoked` and `claude_directory_domain_added`/`_checked`/`_removed`. The same changes appear in `compliance/activities` and `compliance/activities/list`. [[lines 24-560](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/api/api/compliance.md?plain=1#L24-L560)] [[Source](https://platform.claude.com/docs/en/api/compliance#query-parameters)]
* The Inference hooks circuit breaker now re-enables itself after at least 3 minutes instead of 10. [[line 1193](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/api/api/compliance.md?plain=1#L1193)] [[Source](https://platform.claude.com/docs/en/api/compliance#query-parameters)]

#### [api/messages](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/api/api/messages.md) [[Source](https://platform.claude.com/docs/en/api/messages)]

* Several tool-result error types were renamed with an `Object` suffix: `WebSearchToolResultErrorObject`, `CodeExecutionToolResultErrorObject`, `BashCodeExecutionToolResultErrorObject`, `TextEditorCodeExecutionToolResultErrorObject`. The change is mirrored across the beta Messages pages and the language SDK references (Go, Python, Ruby, Java, C#, CLI, TypeScript, PHP). [[line 731](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/api/api/messages.md?plain=1#L731)] [[Source](https://platform.claude.com/docs/en/api/messages#body-parameters)]

#### [api/beta and SDK beta references](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* The beta reference and every per-language SDK `beta` page were regenerated to include the new organization Claude Code managed settings resources.

#### [about-claude/pricing](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* Pricing table updates: Fable 5.2 listed at $8 / $40 per MTok input/output, Opus 5.5 at $4 / $20, with cache-hit footnotes. [[lines 17-40](https://github.com/gpambrozio/ClaudeDocs/blob/0e63f67d8201a8007cce96c41fba15e588895a4d/docs-md/api/about-claude/pricing.md?plain=1#L17-L40)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing#model-pricing)]

#### Other API pages

* Many pages were reformatted (table syntax) without content changes, such as `rate-limits`, `model-deprecations`, `claude-platform-on-aws-iam-actions`, `manage-claude/plugins-api`, `manage-claude/claude-tag-api`, `managed-agents/secure-deployment` and `mcp-tunnels/overview`.
