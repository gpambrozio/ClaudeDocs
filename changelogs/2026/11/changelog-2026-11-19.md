# [Claude docs changes for November 19th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/7c74336ce0c5b44f7b481f7562b127a895245ee8) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/7c74336ce0c5b44f7b481f7562b127a895245ee8)]

## Executive Summary
- Claude Code 2.1.328 adds auto mode for Opus 4.6 and Sonnet 4.6 on Bedrock, Google Cloud's Agent Platform, Microsoft Foundry and the Claude apps gateway, and `mcp_tool` hooks now support `"onFailure": "block"`.
- Code Mode gets a large round of fixes and speedups. Its output is now checked with `PostToolUse` hooks (using `updatedToolOutput`) instead of `UserPromptSubmit` hooks, and the Code Mode docs have a new section on this.
- The `/install-github-app` setup guide was rewritten as a seven-step walkthrough, and new environment variables cover OpenTelemetry host attributes, stricter inline `rm` checks and proxy-scheme repair.
- API docs: the Claude Models on Google Cloud (Anthropic managed) page now lists model IDs and features, and the API reference pages now have structured `Errors` sections (Files, Claude Tag and others).
- The Claude Opus 5.5 system prompt page gained a November 9, 2026 entry.

## New Claude Code versions

### [2.1.328](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/versions/2.1.328.md)

#### New features

* Auto mode for Claude Opus 4.6 and Sonnet 4.6 on Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry and Claude apps gateway. Interactive sessions with no permission mode start in it.
* `"onFailure": "block"` for `mcp_tool` hooks, so a hook whose call fails blocks the action.
* `CLAUDE_CODE_DISABLE_DEFERRED_TOOL_RESUME` lets a host stop `claude -p --resume` and `--continue` from running a tool call that a hook deferred.
* A notice in `/status` and `claude doctor` when an OpenTelemetry exporter has no endpoint.
* A warning when a message from a session that skips permission prompts may be held and dropped by a cloud session.
* Embedding apps can switch on the policy plugin's `allowManagedModsOnly` option.
* Self-hosted runner: `--repository-folder`, `--hook-label`, `--metadata key=value` for `claude --environment`, and new orchestrator metrics for queue wait by reason and sessions given up.

#### Existing feature improvements

* Code Mode is faster in auto and bypass-permissions modes (a 0.75 second pause is removed). It shows the running command and its output, has better edit failure messages and uses fewer tokens for tool descriptions.
* Code Mode runs dev servers as background tasks that show in `/tasks`.
* Prompt caching is better for new Code Mode sessions that have MCP servers.
* Resuming large sessions is faster and uses less memory, including sessions with many images.
* Managed-settings plugins from a git marketplace load sooner on fresh machines in `claude -p`, SDK and Desktop sessions.
* Starting several in-process teammates at once fails far less often with "Lock file is already being held".
* The computer use approval dialog shows each app's level of access and plainer warnings.
* `/code-review` reports only bugs and CLAUDE.md violations on most models, marks findings Important, Pre-existing or Nit, and ends with a suggested fix. Use `/simplify` for cleanups.
* Code Mode no longer runs `UserPromptSubmit` hooks on script output. Use a `PostToolUse` hook with `updatedToolOutput` instead.
* Managed `PostToolUse` hooks no longer fire for calls refused before they ran.
* `/bug` asks Yes or No before sending.
* `deniedMcpServers` entries of the form `claude.ai <name>` now apply in cloud and self-hosted runner sessions.

#### Major bug fixes

* Fixed Bash commands in zsh failing with "not found" at words starting with `=`, such as `echo ====`.
* Fixed automatic compaction reusing the earlier system prompt.
* Fixed rare screen freezes and markdown rendering freezes.
* Fixed scheduled tasks being erased or deleted when the tasks file couldn't be read or had a typo.
* Fixed auto mode failing every turn on third-party providers with `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` set.
* Fixed MCP tools with `anyOf`, `oneOf` or `allOf` input schemas going missing, and invalid MCP schemas failing requests, on third-party providers.
* Fixed many Code Mode problems: a script stopping when a permission prompt stayed open, MCP servers that connected mid-script, background running after `--resume`, valid scripts being refused, and more.
* Fixed Remote Control and cloud session problems: lost permission prompts, lost tool calls and results, cleared conversations resuming, and `/diff` leaving out committed work.
* Fixed `/plugin` closing, uninstalling or disabling the wrong plugin from stale saves, Esc and held Enter.
* Fixed a crash at startup with a negative `FORCE_COLOR`, and a crash in secret masking when memory was almost exhausted.
* Fixed one malformed `OTEL_RESOURCE_ATTRIBUTES` entry dropping all the variable's other labels.
* Fixed several self-hosted runner issues, including all sessions stopping after an HTTP 200 proxy response and data loss in a kept clone after a disk error.

-----

## Claude Code changes

### Changed documents

#### [auto-mode-config](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/auto-mode-config.md) [[Source](https://code.claude.com/docs/en/auto-mode-config)]

* Minor update to auto mode configuration guidance.

#### [code-mode](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/code-mode.md) [[Source](https://code.claude.com/docs/en/code-mode)]

* New section "Check code output with a hook". It explains how to check or redact code output with a `PostToolUse` hook that matches `REPL`, using `tool_response` and `updatedToolOutput`. It also covers background and failed code, blocking, hook failures and refused calls. [[lines 174-220](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/code-mode.md?plain=1#L174-L220)] [[Source](https://code.claude.com/docs/en/code-mode#check-code-output-with-a-hook)]
* On v2.1.328 and later, `UserPromptSubmit` hooks no longer receive code output. The troubleshooting section describes how to handle this on earlier versions. [[line 266](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/code-mode.md?plain=1#L266)] [[Source](https://code.claude.com/docs/en/code-mode#code-output-withheld-by-a-hook)]
* In Manual and `acceptEdits` modes, time spent at a permission prompt no longer counts toward the ten-minute code limit. Sessions picked from the `claude --resume` list now work with background code from v2.1.328. [[line 164](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/code-mode.md?plain=1#L164)] [[Source](https://code.claude.com/docs/en/code-mode#long-running-code)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Added `CLAUDE_CODE_DISABLE_PROXY_SCHEME_REPAIR`. [[line 272](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/env-vars.md?plain=1#L272)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* Added `CLAUDE_CODE_STRICT_INLINE_SHELL_RM_PROMPT`, which flags more `-c` scripts that can't be checked. [[line 408](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/env-vars.md?plain=1#L408)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* Added `OTEL_RESOURCE_INCLUDE_HOST`, which adds `host.name` and `host.id` to OpenTelemetry resource attributes. [[line 520](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/env-vars.md?plain=1#L520)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CLAUDE_CODE_AUTO_COMPACT_WINDOW` no longer has a 1,000,000 token upper bound in its description. [[line 210](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/env-vars.md?plain=1#L210)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [github-actions](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/github-actions.md) [[Source](https://code.claude.com/docs/en/github-actions)]

* The `/install-github-app` quick setup is now a seven-step walkthrough: GitHub CLI sign-in, starting setup, installing the app, selecting workflows, choosing a credential, confirming changes, and creating and merging the pull request. It includes how to keep an existing `claude.yml`. [[lines 18-70](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/github-actions.md?plain=1#L18-L70)] [[Source](https://code.claude.com/docs/en/github-actions#setup)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* `UserPromptSubmit` receiving Code Mode output is now documented as behavior before v2.1.328. [[line 1524](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/hooks.md?plain=1#L1524)] [[Source](https://code.claude.com/docs/en/hooks#userpromptsubmit)]
* A `PermissionRequest` hook can't approve what a deny rule refuses unless a mod overrides the rule. [[line 2202](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/hooks.md?plain=1#L2202)] [[Source](https://code.claude.com/docs/en/hooks#permissionrequest-decision-control)]
* Clarified that only `claude remote-control` cleanup runs a worktree hook without prompting. [[line 3334](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/hooks.md?plain=1#L3334)] [[Source](https://code.claude.com/docs/en/hooks#worktreeremove)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* The auto-compact window now accepts 100K tokens or more, with no 1M ceiling. [[line 893](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/model-config.md?plain=1#L893)] [[Source](https://code.claude.com/docs/en/model-config#set-the-auto-compact-window)]
* Use `opusplan[1m]` to request the 1M context window for `opusplan`. [[line 516](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/model-config.md?plain=1#L516)] [[Source](https://code.claude.com/docs/en/model-config#opusplan-model-setting)]
* Simplified the `availableModels` filtering notes for third-party providers. [[line 1058](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/model-config.md?plain=1#L1058)] [[Source](https://code.claude.com/docs/en/model-config#pin-models-for-third-party-deployments)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* The first-read-outside-working-directory prompt doesn't appear in `-p`, Agent SDK, background, VS Code chat or desktop sessions. [[line 531](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/permission-modes.md?plain=1#L531)] [[Source](https://code.claude.com/docs/en/permission-modes#the-first-read-outside-the-working-directories)]
* Server-side classifier review can block `git reset --hard` on a clean working tree. [[line 615](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/permission-modes.md?plain=1#L615)] [[Source](https://code.claude.com/docs/en/permission-modes#how-auto-mode-evaluates-actions)]
* New troubleshooting entry "Restricted mode refuses bypassPermissions". [[line 724](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/permission-modes.md?plain=1#L724)] [[Source](https://code.claude.com/docs/en/permission-modes#restricted-mode-refuses-bypasspermissions)]
* Added an explanation of the "This shell -c script runs rm and could not be checked" message. [[line 859](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/permission-modes.md?plain=1#L859)] [[Source](https://code.claude.com/docs/en/permission-modes#removals-inside-nested-commands-and-inline-scripts)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* `permissions.ask` entries can still run without approval if a `PermissionRequest` hook or a mod allows them. [[line 979](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/settings-reference.md?plain=1#L979)] [[Source](https://code.claude.com/docs/en/settings-reference#permissionsask)]
* `autoCompactWindow` now accepts any value of 100000 or more. [[line 2339](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/settings-reference.md?plain=1#L2339)] [[Source](https://code.claude.com/docs/en/settings-reference#autocompactwindow)]
* Added `OTEL_RESOURCE_INCLUDE_HOST` and `CLAUDE_CODE_STRICT_INLINE_SHELL_RM_PROMPT` to the lists of launch-environment variables. [[lines 2482-2503](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/settings-reference.md?plain=1#L2482-L2503)] [[Source](https://code.claude.com/docs/en/settings-reference#variables-claude-code-ignores-in-env)]
* The `github` marketplace source example's `path` now points to the marketplace file (`.claude-plugin/marketplace.json`) rather than a subdirectory. [[line 4045](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/settings-reference.md?plain=1#L4045)] [[Source](https://code.claude.com/docs/en/settings-reference#allowed-source-types)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Updated for the new `OTEL_RESOURCE_INCLUDE_HOST` option, with a section on identifying the machine a session ran on.

#### Other changed documents

* Smaller edits were made to the desktop, desktop-changelog (Browser pane auto-mode classifier wording), chrome, errors, plugins (install, loading, troubleshooting and others), remote-control, sandboxing, sub-agents, vs-code, ide-integrations and managed-settings pages.

-----

## API changes

### Changed documents

#### [api/beta/organization/claude_tag](https://github.com/gpambrozo/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/api/api/beta/organization/claude_tag.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/claude_tag)]

* Error descriptions (`bundle_attachment_not_supported`, `api_key_scope_missing`, `slack_channel_set_up_settings_conflict` and others) moved into a dedicated `Errors` section grouped by HTTP status. [[lines 708-833](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/api/api/beta/organization/claude_tag.md?plain=1#L708-L833)] [[Source](https://platform.claude.com/docs/en/api/beta/organization/claude_tag#errors)]

#### [api/files](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/api/api/files.md) [[Source](https://platform.claude.com/docs/en/api/files)]

* Each method now has an `Errors` section listing the `error.details.error_code` values it can return. These include customer-managed encryption key errors, trust-and-safety disablement, `file_not_downloadable`, `file_expired` and `storage_quota_exceeded`. [[line 96](https://github.com/gpambrozo/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/api/api/files.md?plain=1#L96)] [[Source](https://platform.claude.com/docs/en/api/files#errors)]
* The same error documentation was added across the beta, CLI, skills, messages, batches, environments, organization, workspaces, federation and related API reference pages.

#### [about-claude/pricing](https://github.com/gpambrozo/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* The 1.1x US-only inference multiplier is now broken down by platform. It applies on the Claude API, Claude Platform on AWS, Google Cloud (Anthropic managed) and Foundry US Data Zone. It doesn't apply on Google managed or Bedrock. Models before Claude 4.6 return a 400 if `inference_geo` is sent. [[line 176](https://github.com/gpambrozo/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/api/about-claude/pricing.md?plain=1#L176)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing#data-residency-pricing)]
* Managed Agents pricing now lists the rules that apply: prompt caching multipliers, web search at $10 per 1,000 searches, and the fast mode premium when `model.speed` is `"fast"`. [[line 453](https://github.com/gpambrozo/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/api/about-claude/pricing.md?plain=1#L453)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing#tokens)]

#### [build-with-claude/claude-models-on-google-cloud/anthropic-managed](https://github.com/gpambrozo/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/api/build-with-claude/claude-models-on-google-cloud/anthropic-managed.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed)]

* Added a table of available models and model IDs (Fable 5.x, Mythos 5.x, Opus, Sonnet, Haiku). [[line 401](https://github.com/gpambrozo/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/api/build-with-claude/claude-models-on-google-cloud/anthropic-managed.md?plain=1#L401)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#api-model-ids)]
* The feature list was reorganized into Messages API features, Claude Managed Agents and Administration/compliance. Many more features are listed as available, such as the bash, computer use, browser use and text editor tools, citations, context editing, compaction, task budgets and tool search. [[line 524](https://github.com/gpambrozo/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/api/build-with-claude/claude-models-on-google-cloud/anthropic-managed.md?plain=1#L524)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#feature-support)]
* Messages and Token Counting requests have a lower request-size limit on this platform. [[line 243](https://github.com/gpambrozo/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/api/build-with-claude/claude-models-on-google-cloud/anthropic-managed.md?plain=1#L243)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#making-requests)]

#### [manage-claude/opentelemetry](https://github.com/gpambrozo/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/api/manage-claude/opentelemetry.md) [[Source](https://platform.claude.com/docs/en/manage-claude/opentelemetry)]

* Beta availability is now stated per platform: SDK tracing on the Claude API, Bedrock and Claude Platform on AWS, and API tracing on the Claude API and Claude Platform on AWS. Google Cloud (Anthropic managed) is no longer listed as beta. [[line 270](https://github.com/gpambrozo/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/api/manage-claude/opentelemetry.md?plain=1#L270)] [[Source](https://platform.claude.com/docs/en/manage-claude/opentelemetry#messages-api)]

#### [release-notes/system-prompts/claude-opus-5-5](https://github.com/gpambrozo/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/api/release-notes/system-prompts/claude-opus-5-5.md) [[Source](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-opus-5-5)]

* Added a November 9, 2026 system prompt entry. It covers product information, refusal handling (including character and artwork reproduction), medical guidance for children's medicines, and tone and formatting. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/7c74336ce0c5b44f7b481f7562b127a895245ee8/docs-md/api/release-notes/system-prompts/claude-opus-5-5.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-opus-5-5#november-9-2026)]
* Similar system prompt entries were added for the other Claude 4.x and 5.x model pages (Fable, Opus, Sonnet and Haiku).

#### Other changed documents

* Many pages were lightly updated for Google Cloud (Anthropic managed) availability. These include the tool use, prompt caching, compaction, effort, thinking, vision, compliance and data residency pages.
