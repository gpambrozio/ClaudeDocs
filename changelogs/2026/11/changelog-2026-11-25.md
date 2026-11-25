# [Claude docs changes for November 25th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/a715226234ce74a0b4805efd4353c10db31baa74) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/a715226234ce74a0b4805efd4353c10db31baa74)]

## Executive Summary
- Claude Code 2.1.332 adds a `PreSkillShellCommand` hook that can block the shell commands a skill injects while it loads, plus beta support for skills served from MCP servers.
- Claude Code 2.1.332 changes the Sonnet and Opus aliases and defaults on Foundry, Google Cloud's Agent Platform and Bedrock Mantle (Sonnet 5.5 is now the Foundry default), and makes model fallback more robust.
- A new "Linked billing" documentation set (beta) explains how OAuth apps can bill customers through the customers' own Claude organizations.
- New "Handle errors" API guide, with a much expanded errors reference, shows how to catch API errors by error code, HTTP status or connection failure in each SDK.
- The earlier Claude Code in Slack is retired in favor of Claude Tag, and the Claude Security plugin docs were substantially reworked.

## New Claude Code versions

### [2.1.332](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/versions/2.1.332.md)

#### New features

* Skills from MCP servers (beta), shown as `server:skill` in the `/` menu
* New `PreSkillShellCommand` hook event that can refuse a skill or command's inline shell commands as it loads (2.1.331 and older show a dialog at start if a settings file names it)
* "Always deliver" option in the prompt for held messages from other sessions
* Footer line shown while a flagged message has your session on a different model, until you pick one with `/model`
* New OpenTelemetry `assistant_response` event for text sent through SendUserMessage or Cowork's message tool, when response logging is on
* VS Code and Desktop Code tab warn when part of a session couldn't be saved (and how to save it with `/compact`), and notify when a resumed session's earlier messages weren't loaded
* Cyber Verification Program access tier shown in the startup header
* [VSCode] Warning when `/rewind` stops a self-paced `/loop`, and installed version shown in Manage plugins

#### Existing feature improvements

* Computer use: Screen Recording permission prompt can restart Claude Code and resume the chat; uses less context until needed; macOS safety rules updated (some actions refused, typing can be slower)
* Model fallback: `--model default` moves to an older model when unavailable; enforced older-model lists step down on Agent Platform and Foundry; `opus` steps down behind gateways that refuse a model; Bedrock sub-agents use the model's own profile
* Provider defaults: `sonnet` alias is Sonnet 5.5 on Agent Platform and Foundry; Foundry `opus` is Opus 5.5 and its default model is Sonnet 5.5 (`claude-sonnet-5-5`); Agent Platform reads `VERTEX_REGION_CLAUDE_5_5_SONNET`; Foundry treats Sonnet 4, Opus 4 and Opus 4.1 as retired
* Sessions moved to Sonnet 5 or 5.5 on Bedrock Mantle, Agent Platform and Foundry start in auto mode if no mode is set (`disableAutoMode: "disable"` stops it)
* `/permissions` refuses rules that would be skipped at next start and shows the reason
* Code Mode: confirms before discarding worktree changes, updates existing artifacts, shows long MCP tool descriptions whole, and tells Claude script variables are gone on resume
* Tap-mode voice dictation stays on for 60 seconds of silence or 10 minutes (up from 15 seconds and 2 minutes), and stops when you send the prompt
* `/schedule`, permission prompts and `/loop` now say "cloud scheduled task" instead of "routine"
* Better recovery from 413 errors behind size-limited proxies; faster Glob on Windows; lower memory use at startup, on resume and in `claude -p`
* `awsCredentialExport` now times out after 10 minutes
* Changed default OpenTelemetry `service.name` for desktop Code tab sessions to `claude-code-desktop`
* `computer-use` is now a reserved skill name on Macs with computer use on
* Self-hosted runner: `CLAUDE_CODE_OAUTH_TOKEN` prefix may end in `oat02-`; `setup` asks for the environment key in the terminal and hides it

#### Major bug fixes

* Fixed several freezes: long wildcard permission rules, endless hook output, huge hook logs, local MCP servers flooding stdout, long `@` strings, rewind after large file rewrites
* Fixed compaction failures and "Prompt is too long" after repeated auto-compaction failures
* Fixed `claude auth login` reporting success when the login could not be saved
* Fixed Read, @-mentions and compaction hanging on a named pipe (now fails after 20 seconds)
* Fixed SSE MCP servers hanging after their stream was cut, and MCP task IDs over 128 characters failing
* Fixed CLAUDE.md and rules being sent twice after moving into a worktree
* Fixed the `sonnet` alias on Bedrock Mantle resolving to Haiku 4.5
* Fixed PreToolUse hook "ask" reasons not showing on Read, Grep, Glob, Edit and Write prompts
* Fixed web searches failing when allowed or blocked domain lists were empty or had duplicates
* Fixed NotebookEdit saving an invalid notebook when a cell's type changes
* Fixed `~/.claude.json` being reported as corrupted during a concurrent save
* Fixed dictated text past 10,000 characters being lost
* Many Code Mode and VS Code fixes (stalled subagents, diff copy actions, links, rewind, model picker, sign-in)

-----

## Claude Code changes

### Changed documents

#### [advisor](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/advisor.md) [[Source](https://code.claude.com/docs/en/advisor)]

* Minor wording updates.

#### [approvals-policy](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/approvals-policy.md) [[Source](https://code.claude.com/docs/en/approvals-policy)]

* Policy documentation revised along with the other Approvals pages (`approvals-pull-requests`, `approvals-setup`, `approvals-troubleshooting`).

#### [artifacts](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/artifacts.md) [[Source](https://code.claude.com/docs/en/artifacts)]

* Artifact publishing and updating guidance revised.

#### [claude-security](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/claude-security.md) [[Source](https://code.claude.com/docs/en/claude-security)]

* Description updated: scans no longer build a separate threat model step, and a reminder to scan only code you own or have permission to test was added. [[lines 5-11](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/claude-security.md?plain=1#L5-L11)] [[Source](https://code.claude.com/docs/en/claude-security#scan-your-codebase-for-vulnerabilities)]
* New guidance for scanning large repositories at higher effort levels. [[line 150](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/claude-security.md?plain=1#L150)] [[Source](https://code.claude.com/docs/en/claude-security#choose-a-scan-effort)]
* Large new section expanding the patch-suggestion and `git apply` workflow. [[lines 211-310](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/claude-security.md?plain=1#L211-L310)] [[Source](https://code.claude.com/docs/en/claude-security#patches-are-never-applied-automatically)]

#### [code-mode](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/code-mode.md) [[Source](https://code.claude.com/docs/en/code-mode)]

* Eight lines added covering new Code Mode behavior.

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* Command descriptions updated (e.g. cloud scheduled tasks wording).

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Desktop app Code tab documentation revised.

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Environment variable entries added or updated, including provider region and model variables.

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New error messages and troubleshooting sections added, such as connection-ended and restore-skipped messages. [[line 5996](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/errors.md?plain=1#L5996)] [[Source](https://code.claude.com/docs/en/errors#claude-code-needs-a-recent-sign-in)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* New `PreSkillShellCommand` event added to the event table, matcher table and blocking table. [[line 33](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/hooks.md?plain=1#L33)] [[Source](https://code.claude.com/docs/en/hooks#hook-lifecycle)]
* New section documenting `PreSkillShellCommand`: requires v2.1.332, matcher `Bash|PowerShell`, input fields (`command_name`, `command_source`, `invoked_by`), block-only decision control and failure behavior. [[lines 1655-1727](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/hooks.md?plain=1#L1655-L1727)] [[Source](https://code.claude.com/docs/en/hooks#preskillshellcommand)]
* Clarified that PreToolUse does not fire for skill-injected shell commands. [[lines 1865-1867](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/hooks.md?plain=1#L1865-L1867)] [[Source](https://code.claude.com/docs/en/hooks#pretooluse)]
* Windows-without-Git-Bash failure behavior now also covers `PreSkillShellCommand`. [[line 944](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/hooks.md?plain=1#L944)] [[Source](https://code.claude.com/docs/en/hooks#block-the-action-when-a-hook-fails)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Documented the new `assistant_response` event and the `tool_input` length-only change.

#### [plugins/mods/interface](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/plugins/mods/interface.md) [[Source](https://code.claude.com/docs/en/plugins/mods/interface)]

* Substantially expanded (about 300 lines changed) with more interface reference detail for mods. Related edits in `plugins/mods/events`, `reference`, `create`, `test` and `troubleshoot`.

#### [ship-command](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/ship-command.md) [[Source](https://code.claude.com/docs/en/ship-command)]

* New section on what Claude does while watching a pull request and when merging is left to you. [[lines 121-160](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/ship-command.md?plain=1#L121-L160)] [[Source](https://code.claude.com/docs/en/ship-command#watch-a-branch-on-another-host)]
* Setup and prerequisite steps reworded. [[lines 46-85](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/ship-command.md?plain=1#L46-L85)] [[Source](https://code.claude.com/docs/en/ship-command#prerequisites-for-ship-and-steward)]

#### [ship-command-troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/ship-command-troubleshooting.md) [[Source](https://code.claude.com/docs/en/ship-command-troubleshooting)]

* Troubleshooting entries reorganized (about 100 lines changed).

#### [slack](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/slack.md) [[Source](https://code.claude.com/docs/en/slack)]

* The earlier Claude Code in Slack is now documented as retired. In a workspace that isn't connected to Claude Tag, `@Claude` replies that the workspace isn't set up for Claude Tag. Use cases, prerequisites and setup steps were removed. [[lines 1-10](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/slack.md?plain=1#L1-L10)] [[Source](https://code.claude.com/docs/en/slack#claude-code-in-slack)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* Tool reference updated (about 66 lines changed).

#### [voice-dictation](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/voice-dictation.md) [[Source](https://code.claude.com/docs/en/voice-dictation)]

* Tap-mode timeouts and stop conditions updated to match 2.1.332.

#### [amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)], [google-vertex-ai](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/google-vertex-ai.md), [microsoft-foundry](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/claude-code/microsoft-foundry.md)

* New default model, alias and fallback behavior notes for each provider.

-----

## API changes

### New Documents

#### [$shared](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/api/api/$shared.md) [[Source](https://platform.claude.com/docs/en/api/$shared)]

Large shared API reference page of common types (about 1,770 lines).

#### [handle-errors](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/api/api/handle-errors.md) [[Source](https://platform.claude.com/docs/en/api/handle-errors)]

Shows how to use the SDK to catch API errors by error code, HTTP status or connection failure, and how to handle an error that arrives mid-stream. It has examples in several languages, including the `enforced_spend_limit_reached` error.

#### [oauth-apps/linked-billing](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/api/manage-claude/oauth-apps/linked-billing.md) [[Source](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing)]

Beta overview (`user-profiles-billing-2026-10-01` header) of Linked billing. It explains who pays, which customers are eligible and whose terms apply. A set of sub-pages covers the rest:

* [set-up-your-app](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/api/manage-claude/oauth-apps/linked-billing/set-up-your-app.md)
* [link-button](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/api/manage-claude/oauth-apps/linked-billing/link-button.md)
* [link-and-bill-a-customer](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/api/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer.md)
* [credential-for-each-customer](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/api/manage-claude/oauth-apps/linked-billing/credential-for-each-customer.md)
* [manage-customers](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/api/manage-claude/oauth-apps/linked-billing/manage-customers.md)
* [what-your-customers-see](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/api/manage-claude/oauth-apps/linked-billing/what-your-customers-see.md)
* [test-and-publish](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/api/manage-claude/oauth-apps/linked-billing/test-and-publish.md)
* [errors](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/api/manage-claude/oauth-apps/linked-billing/errors.md)

#### [oauth-apps/endpoints-and-parameters](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/api/manage-claude/oauth-apps/endpoints-and-parameters.md) [[Source](https://platform.claude.com/docs/en/manage-claude/oauth-apps/endpoints-and-parameters)]

Reference for the OAuth endpoints and parameters used by apps.

### Changed documents

#### [api/errors](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/api/api/errors.md) [[Source](https://platform.claude.com/docs/en/api/errors)]

* Expanded by about 250 lines with error codes and details, linking to the new handle-errors guide.

#### [cli-sdks-libraries/sdks (csharp, go, java, php, python, ruby, typescript)](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/api/cli-sdks-libraries/overview.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/overview)]

* Each SDK page was updated, with changes to the error handling documentation and the latest-version references.

#### [manage-claude/api-and-data-retention](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/api/manage-claude/api-and-data-retention.md) [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

* Data retention content revised (about 44 lines changed).

#### [manage-claude/oauth-apps/overview](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/api/manage-claude/oauth-apps/overview.md) [[Source](https://platform.claude.com/docs/en/manage-claude/oauth-apps/overview)]

* Reworked to link into the new Linked billing and endpoints pages.

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* Fixes for undercounts in the Enterprise Analytics API: web searches in List User Activity (from Nov 17), connector usage (from Nov 19), and project activity (from Nov 20). [[lines 17-23](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/api/release-notes/overview.md?plain=1#L17-L23)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#november-23-2026)]
* New Nov 20 entry: a new rule for when a Chat and Cowork chat counts as a session, with the impact on user, skill, plugin and connector metrics. [[lines 28-55](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/api/release-notes/overview.md?plain=1#L28-L55)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#november-20-2026)]
* New Nov 4 entry: SDK error codes, with a dedicated exception class per error code. [[line 88](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/api/release-notes/overview.md?plain=1#L88)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#november-4-2026)]
* Linked billing link now points to the new page. [[line 58](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/api/release-notes/overview.md?plain=1#L58)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#november-17-2026)]

#### [build-with-claude/claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/api/build-with-claude/claude-platform-on-aws.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)]

* Updated platform content (about 24 lines); related small edits to the Foundry, Google Cloud, context-windows, thinking and extended-thinking pages.

#### [manage-claude/enterprise-frontier-safeguards/faq](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/api/manage-claude/enterprise-frontier-safeguards/faq.md) [[Source](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/faq)]

* New FAQ entries added.

#### [managed-agents/migration](https://github.com/gpambrozio/ClaudeDocs/blob/a715226234ce74a0b4805efd4353c10db31baa74/docs-md/api/managed-agents/migration.md) [[Source](https://platform.claude.com/docs/en/managed-agents/migration)]

* 13 lines of new migration guidance added.
