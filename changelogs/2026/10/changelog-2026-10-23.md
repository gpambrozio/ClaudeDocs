# [Claude docs changes for October 23rd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/06365c612f38c93c5f2accc14afb39bed5a4099d) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/06365c612f38c93c5f2accc14afb39bed5a4099d)]

## Executive Summary
- Claude Code 2.1.309 ships a batch of sandbox and permission-check hardening fixes, and `claude ultrareview` now requires workspace trust (`--trust-workspace` for scripts and CI).
- `/rewind` now also undoes Bash-command changes to files Claude has already edited with its file tools. Checkpointing, glossary and Agent SDK docs were updated to match.
- New API docs split "Claude Models on Google Cloud" into Anthropic-managed and Google-managed offerings, with an IAM permissions reference.
- A new set of customer-managed encryption key (CMEK) docs covers how it works, coverage, key lifecycle, the Admin API and troubleshooting.
- Claude Code docs add OpenTelemetry `safety_event` telemetry, MCP idempotency hints and stdio reconnect behavior, and new VS Code and Desktop troubleshooting sections.
- Note: most files changed only because in-site links were rewritten (relative `.md` paths vs. `/docs/en/...`), and API reference pages were re-indented. These are not listed below.

## New Claude Code versions

### [2.1.309](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/versions/2.1.309.md)

#### New features

* `claude ultrareview` requires workspace trust: it asks on a terminal and otherwise refuses. Scripts pass `--trust-workspace`, or set `CLAUDE_CODE_DISABLE_ULTRAREVIEW_TRUST_CHECK=1`
* Skills from an `--add-dir` folder that share a name with an existing skill are now offered as `<folder>:<name>`
* Failed shell/hook environments now give clearer errors: full-disk and quota messages name the folder to free up, and hooks-module nesting errors name the file
* Bundled `dataviz` skill accepts APCA as a text-contrast measure and adds an `apca()` function to its validator scripts
* `/claude-api` skill builds Managed Agents subagent teams on `multiagent_20261001` with dynamic workflows on by default, and offers API tracing alongside SDK tracing for OpenTelemetry
* [VSCode] Warning in the log that explains what to do when dictation or extension requests fail certificate verification (for example behind a TLS-inspecting proxy)
* [VSCode] Ctrl+J in the chat input can be left to VS Code and the OS by setting `"ctrl+j": null` in the Chat context of `~/.claude/keybindings.json`

#### Existing feature improvements

* Faster git commands on Windows, and git errors show in English on every platform
* `sed -i` now gets the standard Bash prompt and runs as written, so it is no longer restored by `/rewind`
* Bypass-permissions mode in the Desktop app and VS Code denies dangerous `rm`/`rmdir` immediately with a rewrite hint instead of prompting
* Commands excluded from the sandbox ask before writing to write-list paths when the sandbox is enabled but cannot run
* Worktree creation no longer lets git fetch objects on demand (partial clones fetch first)
* Nested CLAUDE.md files over the size limit now load only their start
* [VSCode] Faster Edit and Write in the chat panel (0.75 s wait for new problems, down from 1 to 1.5 s)
* [VSCode] Long slash-command messages such as `/goal` fold behind Show more
* [Cloud sessions] The Changes pane says whether it lists only pushed commits or only Claude's edits
* Self-hosted runner: sessions that move to a new runner show the interrupted tool call as outcome unknown

#### Major bug fixes

* Sandbox: shell startup files no longer run outside the sandbox, macOS `denyWrite` globs apply through symlinks, and sandboxed commands can't modify the `--mcp-config` file
* Permission checks: fixed several Bash and PowerShell bypasses (variables set by commands with failing redirects, wrapped `cd` before git, `Edit(path)` deny rules with subshell redirects, `Set-Location`/`cd` with extra arguments)
* Worktree-isolated sessions no longer accept locale-prefixed or zsh arithmetic commands that the guard should refuse
* PowerShell hooks now block on exit code 2, and `PreToolUse`/`PermissionRequest` PowerShell hooks no longer fail open without Git for Windows
* Fixed repeated compaction caused by large nested CLAUDE.md files
* Fixed `/rewind` showing "No code changes" for turns changed via `/code-review --fix`, subagents or shell commands
* Split-pane agent teammates now inherit the leader's `--tools` and deny rules
* Fixed Claude notifying unrelated GitHub users by writing role names or placeholders as mentions
* Fixed macOS repeatedly opening the "Install Command Line Developer Tools" dialog
* [Claude Tag] Fixed Slack drafts posting to a DM instead of the approved channel, Allow/Deny cards doing nothing after the session stopped, and untagged messages being ignored after a workspace moved organizations
* [Code Review] Fixed reviews showing no check on the PR after failed creation, and pushes queued behind a review restarting it after `@claude review stop`

-----

## Claude Code changes

### Changed documents

#### [accessibility](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/accessibility.md) [[Source](https://code.claude.com/docs/en/accessibility)]

* New troubleshooting entry: project settings can't turn on screen reader mode. Claude Code ignores `axScreenReader` and `CLAUDE_AX_SCREEN_READER` in project `.claude/settings*.json` files; set `"axScreenReader": false` in user settings to silence the startup line.

#### [agent-sdk/file-checkpointing](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/agent-sdk/file-checkpointing.md) [[Source](https://code.claude.com/docs/en/agent-sdk/file-checkpointing)]

* Rewinding now undoes Bash-command changes to files the main conversation already edited with Write or Edit.

#### [agent-sdk/observability](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/agent-sdk/observability.md) [[Source](https://code.claude.com/docs/en/agent-sdk/observability)]

* Events that become a per-user audit trail for SIEM forwarding (`tool_decision`, `tool_result`, `mcp_server_connection`, `permission_mode_changed`).

#### [agent-sdk/skills](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/agent-sdk/skills.md) [[Source](https://code.claude.com/docs/en/agent-sdk/skills)]

* Clarified the `skills` list: own skills use the directory name, plugin skills use `plugin:skill`. The same change is in `agent-sdk/slash-commands`.

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Added the `allowNestedUserNamespaces` sandbox option.

#### [agent-teams](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

* Teammates inherit the lead's `--disallowedTools` and `--tools` (v2.1.309+).
* Added a subagents vs. agent teams comparison sentence.

#### [checkpointing](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/checkpointing.md) [[Source](https://code.claude.com/docs/en/checkpointing)]

* Replaced "Bash changes are not tracked" with new behavior: `/rewind` undoes Bash changes to files Claude already edited with its file tools. Files changed only by Bash are still untracked; use Git.
* The rewind menu counts changes to already-edited files regardless of what made them.

#### [claude-apps-gateway](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/claude-apps-gateway.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway)]

* New section on how hook and skill keys in parent settings take effect (`allowedHttpHookUrls`, `httpHookAllowedEnvVars`), requiring v2.1.309+.

#### [claude-apps-gateway-deploy](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/claude-apps-gateway-deploy.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy)]

* New section on retrying unanswered requests sooner with `CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS`.

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* `/clear` is now supported in cloud sessions and starts a fresh conversation in the same session.

#### [claude-md](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/claude-md.md) [[Source](https://code.claude.com/docs/en/claude-md)]

* Per-file size limits now apply to on-demand files (subdirectory CLAUDE.md and rules): 40,000 characters (200K window) or 150,000 to 200,000 (1M window). Larger files load only their start.
* New troubleshooting entry "Claude ignores the end of my subdirectory CLAUDE.md". The same content was added to `memory`.

#### [claude-projects](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/claude-projects.md) [[Source](https://code.claude.com/docs/en/claude-projects)]

* Reworked moving a cloud session into a project: **Move to project** now has a submenu with **Continue as new project** or an existing project.

#### [cloud-environments](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/cloud-environments.md) [[Source](https://code.claude.com/docs/en/cloud-environments)]

* "Add a setup script" is now its own section.

#### [code-review-pull-requests](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/code-review-pull-requests.md) [[Source](https://code.claude.com/docs/en/code-review-pull-requests)]

* New section "When a push keeps the earlier result": Code Review may keep an earlier result when the PR's diff is unchanged and no Important thread was resolved. The check title is `Code review skipped — no new changes`.
* Scripts parsing severity counts should handle the `no new changes` title first.

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* Explained the recommendation share: it shows how much usage a row applies to, not the savings, and shares can exceed 100%.

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* New "Allow jump hosts" section for `sshHostAllowlist`. Jump hosts from `ProxyJump` or `ssh -W` `ProxyCommand` must be listed (Desktop v3.1623.0+), with a step-by-step way to find the names. The same content was added to `desktop-changelog`.
* `/config` opens **Settings > Claude Code**, and a disk-space error message was renamed.

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Added `CLAUDE_CODE_WARN_DISK_FREE_GIB` and `CLAUDE_CODE_WARN_MEMORY_FREE_GIB` (v2.1.304+).

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New entries: MCP stored credentials unreadable (locked macOS keychain), MCP connection timed out during sleep or clock change, MCP connection closed before the tool call was answered, cached plugin MCP connection failure, and `claude ultrareview` workspace-not-trusted errors.
* Rewrote disk-full and quota messages and fixes, now naming the volume and `CLAUDE_CODE_TMPDIR`.
* Renamed the sandbox mask file warning ("left behind at write-deny paths") with updated cleanup steps.
* Reworked feedback error handling and noted that `CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS` applies to gateway sessions from v2.1.307.

#### [features-overview](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/features-overview.md) [[Source](https://code.claude.com/docs/en/features-overview)]

* Clarified that only CLAUDE.md files loaded at session start load in full.

#### [glossary](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/glossary.md) [[Source](https://code.claude.com/docs/en/glossary)]

* Checkpoint entry updated for the new Bash-change rewind behavior.

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Reworked guidance for hooks that fail without Git Bash: exec-form hooks for `.exe` programs, and `"onFailure": "block"` plus `"shell": "powershell"` for PowerShell guard hooks. The message text changed in v2.1.309.

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* The same VS Code additions as `vs-code` (below).

#### [managed-mcp](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/managed-mcp.md) [[Source](https://code.claude.com/docs/en/managed-mcp)]

* Reworded the upgrade warning for `allowedMcpServers` users: add `deniedMcpServers` entries before upgrading. `${VAR}` expansion in `env` no longer counts toward the check.

#### [managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/managed-settings.md) [[Source](https://code.claude.com/docs/en/managed-settings)]

* Managed settings files may be symlinks. Claude Code follows them and warns in `/status` and `claude doctor` when the target is outside the system directory.

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* New "Stdio servers that exit or fail to start" table covering reconnect behavior by run mode.
* New section "Mark tools that are safe to call twice" for `idempotentHint` and `readOnlyHint` annotations.
* Revised the retry description for dropped remote servers and 401 refresh.

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* New `claude_code.safety_event` with attributes, categories and an example, plus which calls don't emit one.
* `ccr.session.id` identifies cloud sessions, and `session.id` is replaced by `/clear`.

#### [network-config](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/network-config.md) [[Source](https://code.claude.com/docs/en/network-config)]

* Removed the note about the 5 to 6 minute body idle timeout on other connections.

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* `Write(path)`, `NotebookEdit(path)` and `Glob(path)` rules never match. Use `Edit(path)` and `Read(path)` instead.
* Reorganized path-pattern docs: anchoring, depth, special characters and `!` negation.

#### [plugins/mods/interface](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/plugins/mods/interface.md) [[Source](https://code.claude.com/docs/en/plugins/mods/interface)]

* Users can collapse the mod band to one row. Mods can't expand it or detect it, so don't make the band the only place to ask something.

#### [plugins/mods/reference](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/plugins/mods/reference.md) [[Source](https://code.claude.com/docs/en/plugins/mods/reference)]

* `Svg` props listed (`source`, `alt`, `width`, `height`, `isInteractive`); new `Button` rules for hotkeys; more band-supported props (`position` offsets, `alignSelf`, `borderDimColor`, `hover`).

#### [plugins/mods/troubleshoot](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/plugins/mods/troubleshoot.md) [[Source](https://code.claude.com/docs/en/plugins/mods/troubleshoot)]

* New entries for "engine ran out of stack" hooks-module errors and "plugin panel hidden", and an expanded hotkey-not-working checklist.

#### [routines](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)]

* New "Permission prompts during a run" section and an "Artifacts in Accept edits mode" subsection. The same content is in `web-scheduled-tasks`.

#### [security-guidance](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/security-guidance.md) [[Source](https://code.claude.com/docs/en/security-guidance)]

* Reviews now default to "a Claude Opus model" instead of a pinned version.

#### [self-hosted-environments-configuration](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/self-hosted-environments-configuration.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration)]

* Wrapper stdin guidance changed to file descriptor 9. Runners on v2.1.309+ reserve fds 4 and 5.
* New "Exit the hook without waiting for the runner" section (`--hook-timeout` kills the process tree).
* The Stop hook script is hardened (`core.fsmonitor` and hooks path disabled, `--ignore-submodules=dirty`), with new submodule behavior notes and replacement instructions for older copies.

#### [self-hosted-environments-deploy](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/self-hosted-environments-deploy.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy)]

* `--base-dir /workspace` added to deployment examples.
* New "Let running turns finish before a restart" section (`--drain-wait-sec`).
* New troubleshooting for malformed poll responses from intercepting proxies and for an unwritable base directory.

#### [self-hosted-environments-reference](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/self-hosted-environments-reference.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-reference)]

* New section on joining a session's metrics to the runner's by `session_id`.

#### [sessions](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/sessions.md) [[Source](https://code.claude.com/docs/en/sessions)]

* Documented the "Resume this conversation?" dialog and its usage estimate.

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* Unix socket sandbox setting now also allows `AF_VSOCK` VM sockets on Linux and WSL2.

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* New section on running a same-named skill from an added directory (`/cli:verify`) and on managed settings that lock hooks to plugins. The same content is in `slash-commands`.

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Subagent permission mode inheritance now lists only `default` and `dontAsk` (plan removed).

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* New "Task-tracking tools in subagents and agent teams" section.

#### [ultrareview](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/ultrareview.md) [[Source](https://code.claude.com/docs/en/ultrareview)]

* New "Trust the folder before the review runs" section (`claude ultrareview 1234 --trust-workspace`) and a revised exit-code list (130 for Ctrl-C).

#### [voice-dictation](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/voice-dictation.md) [[Source](https://code.claude.com/docs/en/voice-dictation)]

* VS Code dictation stops after 15 seconds without recognized speech or at a 2-minute limit.

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* New sections: "The conversation is still open somewhere else" (**Open here anyway**), "Ctrl+J adds a new line in the prompt box" (unbind with `keybindings.json`), "The Claude Code panel is blank or couldn't load", and "Dictation or the Web tab fails behind a TLS-inspecting proxy" (`NODE_EXTRA_CA_CERTS`).

#### [whats-new](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/whats-new.md) [[Source](https://code.claude.com/docs/en/whats-new)]

* Weekly entries gained date ranges (September 7–11 back to March 23–27, 2026).

#### [worktrees](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/claude-code/worktrees.md) [[Source](https://code.claude.com/docs/en/worktrees)]

* New troubleshooting entry for worktree creation failing in a partial clone.

-----

## API changes

### New Documents

#### [api/claude-models-on-google-cloud-anthropic-managed-iam-permissions](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/api/api/claude-models-on-google-cloud-anthropic-managed-iam-permissions.md) [[Source](https://platform.claude.com/docs/en/api/claude-models-on-google-cloud-anthropic-managed-iam-permissions)]

Reference of Google Cloud IAM permissions (`claude.googleapis.com`), the three predefined roles and audit log types for Claude Models on Google Cloud (Anthropic managed).

#### [build-with-claude/claude-models-on-google-cloud/anthropic-managed](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/api/build-with-claude/claude-models-on-google-cloud/anthropic-managed.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed)]

Setup guide for the Claude API run by Anthropic and reached through a Google Cloud project, with Google Cloud handling access and billing.

#### [build-with-claude/claude-models-on-google-cloud/google-managed](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/api/build-with-claude/claude-models-on-google-cloud/google-managed.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed)]

Guide for Claude operated by Google as part of Google Cloud's Agent Platform, called with Anthropic's client SDKs (prerequisites, gcloud, SDK usage).

#### [build-with-claude/claude-models-on-google-cloud/overview](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/api/build-with-claude/claude-models-on-google-cloud/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/overview)]

Compares the two Google Cloud offerings and explains how to tell which one you use.

#### [manage-claude/cmek-admin-api](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/api/manage-claude/cmek-admin-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-admin-api)]

Create, validate and attach a customer-managed encryption key using three Admin API calls.

#### [manage-claude/cmek-aws-kms-workspaces](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/api/manage-claude/cmek-aws-kms-workspaces.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms-workspaces)]

How to limit an AWS KMS key to specific workspaces with a key policy condition.

#### [manage-claude/cmek-coverage-claude-enterprise](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/api/manage-claude/cmek-coverage-claude-enterprise.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-enterprise)]

Lists which Claude Enterprise data a CMEK key encrypts, what turns off or changes, and what stays under Anthropic's key.

#### [manage-claude/cmek-coverage-claude-platform](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/api/manage-claude/cmek-coverage-claude-platform.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-platform)]

The same coverage reference for Claude Platform data.

#### [manage-claude/cmek-data-retention](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/api/manage-claude/cmek-data-retention.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-data-retention)]

Explains why a workspace with a key retains data, what that means for zero data retention (ZDR), and what Anthropic can preserve outside your key.

#### [manage-claude/cmek-how-it-works](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/api/manage-claude/cmek-how-it-works.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-how-it-works)]

Explains envelope encryption: your KMS key wraps Anthropic's data keys, the key never leaves your KMS, and you can log each call. Also covers when it takes effect.

#### [manage-claude/cmek-key-lifecycle](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/api/manage-claude/cmek-key-lifecycle.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-key-lifecycle)]

What rotating, disabling or deleting your key does to your data, how soon, and whether it can be undone.

#### [manage-claude/cmek-troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/api/manage-claude/cmek-troubleshooting.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting)]

Causes and fixes for CMEK errors, failed verification and unexpected log entries.

### Changed documents

#### [about-claude/models/model-ids-and-versions](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/api/about-claude/models/model-ids-and-versions.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)]

* "Google Cloud" renamed to "Claude Models on Google Cloud (Google managed)" in model ID format notes. The rename also appears in `pricing` and `api/errors`.

#### [about-claude/models/optimizing-for-cost-and-intelligence](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/api/about-claude/models/optimizing-for-cost-and-intelligence.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence)]

* New measurements (October 20, 2026): a `max_tokens: 0` request refreshes an existing cache entry on Claude Fable 5.1, Opus 5.5, Sonnet 5.5 and Haiku 5.5. The Haiku 5.5 keep-alive guidance was rewritten.
* Removed the cost-of-one-broken-turn table, and added October 2026 cache-break test results (tokens read and written).

#### [about-claude/use-case-guides/commerce-agents](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/api/about-claude/use-case-guides/commerce-agents.md) [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/commerce-agents)]

* Guide intro now covers building a shopping agent and a merchant agent, with runnable examples for retail, travel, telecom and entertainment, plus a Claude Code plugin that scaffolds the design.

#### [about-claude/use-case-guides/customer-support-chat](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/api/about-claude/use-case-guides/customer-support-chat.md) [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/customer-support-chat)]

* Go example now imports `anthropic-sdk-go/v2`.

#### [agents-and-tools/agent-skills/claude-api-skill](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/api/agents-and-tools/agent-skills/claude-api-skill.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill)]

* Platform availability for Managed Agents is no longer listed in the page. It now points to which platforms are supported.

#### [api/errors](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/api/api/errors.md) [[Source](https://platform.claude.com/docs/en/api/errors)]

* Clarified how to pass thinking and `redacted_thinking` blocks back with tool use, and updated the per-SDK `maxRetries` option names.

#### [api/migration-2026-10-21](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/api/api/migration-2026-10-21.md) [[Source](https://platform.claude.com/docs/en/api/migration-2026-10-21)]

* Removed the Text Completions API removal section (CLI and per-SDK before/after examples) from the migration guide.

#### [api/compliance/activities/list](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/api/api/compliance/activities/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/activities/list)]

* New activity types: `account_migration_started`, `account_migration_completed`, `account_migration_failed`, `claude_code_review_promo_enrolled`, `claude_skill_auto_enabled` and `claude_skill_auto_disabled`. The Claude Code Security scan project description now includes pausing and unpausing scheduled scanning.

#### [api/messages](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/api/api/messages.md) [[Source](https://platform.claude.com/docs/en/api/messages)]

* The reference was restructured so message params nest under `UserMessageParam` and `MessageContentParam`. The same restructuring applies to the beta, CLI and per-language SDK reference pages (`api/beta/*`, `api/python/*`, `api/typescript/*`, and so on).
* Removed the note about a `"system"` role from the messages `system` prompt guidance.

#### [api/claude-code/routines-fire](https://github.com/gpambrozio/ClaudeDocs/blob/06365c612f38c93c5f2accc14afb39bed5a4099d/docs-md/api/api/claude-code/routines-fire.md) [[Source](https://platform.claude.com/docs/en/api/claude-code/routines-fire)]

* Response examples are now marked as `json` code blocks.
