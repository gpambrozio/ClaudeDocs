# [Claude docs changes for Oct, 4th 2026](https://github.com/gpambrozio/ClaudeDocs/tree/0123f2c2df278c9701b11fb801c7118a18b466ef) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/0123f2c2df278c9701b11fb801c7118a18b466ef)]

## Executive Summary
- Claude Code 2.1.289 fixes several permission-rule bypasses: Bash deny/ask rules under sandbox auto-allow, `Read` deny rules through symlinks in the IDE, and managed-machine deny rules on nested commands. It also hardens plugins and mods.
- The Claude Apps gateway adds a `mantle` upstream for Amazon Bedrock's Mantle endpoint. It also adds `enforceAvailableModels` so the Default model resolves inside a policy's `availableModels`.
- New `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` documentation explains how credentials are stripped from Bash, hook and MCP subprocess environments.
- Cloud sessions docs are reorganized. They add Quick web setup for Team and Enterprise, sending follow-ups from the CLI, a diff review view, and a table of send errors.
- Hooks docs now explain how a `PreToolUse` hook can answer `AskUserQuestion` through `updatedInput`, and how `if` patterns match Bash commands.

## New Claude Code versions

### [2.1.289](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/versions/2.1.289.md)

#### New features

* Added `agent.spawn` for teammates, one agent id across plugin hook events, and idle and waiting states in `$.agent.list()`

#### Existing feature improvements

* Large files open faster in a plugin code pane
* Clearer error message when a mod's band or pane fails to draw, naming the mod
* A mod's `Client` that fails while drawn now fails alone and raises `ui.fault` instead of taking down everything around it

#### Major bug fixes

* Fixed deny or ask rules on a nested part of a compound shell command not holding over a user-installed mod's approval on managed machines
* Fixed Bash deny and ask rules missing a command behind an environment variable prefix, or after a bare variable assignment, when the sandbox auto-allows commands
* Fixed `Read` deny rules not applying to files @-mentioned, changed, or selected in the IDE through a symlink
* Fixed a user-installed plugin being able to rewrite descriptions of an organization-managed MCP server's sign-in tools
* Fixed the terminal freezing on short code blocks with many unclosed `<script>` tags, including in published artifact pages
* Fixed installed mods not loading in the first session after an upgrade
* Fixed `plugin list`, `plugin eval` and `plugin update` showing a stale copy of a plugin installed from a local folder marketplace
* Fixed sessions ending with an interface error or "unrecoverable interface error" caused by plugin or mod rendering failures
* Fixed `claude plugin validate` skipping a plugin when the folder also holds a marketplace manifest
* [VSCode] Reverted a 2.1.288 change to `claude auth status` that may have made sign-outs more frequent

-----

## Claude Code changes

### New Documents

None.

### Changed documents

#### [agent-sdk/mcp](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/agent-sdk/mcp.md) [[Source](https://code.claude.com/docs/en/agent-sdk/mcp)]

* New troubleshooting section: a tool is left out of an SDK MCP server's list, with a warning, when its input schema can't be converted to JSON Schema. Before TypeScript SDK v0.3.286 the whole listing failed. [[lines 820-831](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/agent-sdk/mcp.md?plain=1#L820-L831)] [[Source](https://code.claude.com/docs/en/agent-sdk/mcp#a-tool-is-missing-from-an-sdk-mcp-server)]

#### [agent-teams](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

* Teammates inherit the lead's effort level by default, and a teammate's model and fast mode are fixed at spawn. [[line 149](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/agent-teams.md?plain=1#L149)] [[Source](https://code.claude.com/docs/en/agent-teams#specify-teammates-and-models)]
* Teammates can reference subagent types from any scope. In-process teammates honor the definition's `disallowedTools` and `effort`. [[lines 252-265](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/agent-teams.md?plain=1#L252-L265)] [[Source](https://code.claude.com/docs/en/agent-teams#use-subagent-definitions-for-teammates)]

#### [amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* New section on how startup model checks behave when `enforceAvailableModels` is set. Entries must use inference profile IDs with region prefixes. [[lines 345-359](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/amazon-bedrock.md?plain=1#L345-L359)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#when-your-organization-enforces-a-model-allowlist)]

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* New `mantle` upstream provider for Amazon Bedrock's Mantle endpoint (needs v2.1.283+). It documents fields, model-scoped routing, and that guardrail and `assume_role` don't apply to it. [[lines 445-481](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L445-L481)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#amazon-bedrock-mantle-endpoint)]
* Guardrails cover Bedrock upstreams only. A Bedrock role's upstream is usable by every admitted developer. [[line 360](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L360)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#apply-an-amazon-bedrock-guardrail)]
* `availableModels` is enforced server-side at `/v1/messages`. A new section explains how to start sessions on an allowed model with `enforceAvailableModels: true`. [[lines 825-870](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L825-L870)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#managed)]

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* Reorganized intro, with pointers to projects, Remote Control and environment setup. [[lines 9-35](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L9-L35)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#use-claude-code-in-the-cloud)]
* New "Quick web setup for Team and Enterprise" org setting: enables `/web-setup`, skips the GitHub App prompt, and creates the Default environment. [[lines 56-67](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L56-L67)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#quick-web-setup-for-team-and-enterprise)]
* Projects need the Claude GitHub App on each repository they clone. [[line 47](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L47)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#github-authentication-options)]
* Follow-ups can be sent to a running cloud session from the CLI. Teleport needs a checkout of the same repository (not a fork) and claude.ai authentication. [[lines 156-218](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L156-L218)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#send-follow-ups-from-the-cli)]
* New sections: permission modes in cloud sessions, reviewing changes (diff view with **Compare against**), and taking back a queued message. [[lines 223-281](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L223-L281)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#permission-modes-in-cloud-sessions)]
* Sharing rules are restated as lists per account type. [[lines 283-292](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L283-L292)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#share-from-an-enterprise-or-team-account)]
* New troubleshooting for claude.ai sign-in errors and a table of errors when sending to a cloud session. An expired environment restores history but not background work. [[lines 366-403](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L366-L403)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#unable-to-get-organization-uuid)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New variables: `CLAUDE_CODE_DISABLE_INLINE_SHELL_RM_PROMPT`, `CLAUDE_CODE_DISABLE_REFUSAL_FALLBACK`, `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB`, `CLAUDE_CODE_TRANSCRIPT_LOCAL_GC` and `CLAUDE_CODE_WORKER_CHECKIN_SCHEDULE`. The last replaces the removed `CLAUDE_CODE_AUTO_BACKGROUND_WORKER_CHECKIN_SECONDS`. [[lines 203-403](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/env-vars.md?plain=1#L203-L403)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New section "What the subprocess environment scrub removes". It covers which variables are removed or kept, such as `GITHUB_TOKEN` and proxies, and the Linux PID namespace isolation. [[lines 513-538](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/env-vars.md?plain=1#L513-L538)] [[Source](https://code.claude.com/docs/en/env-vars#what-the-subprocess-environment-scrub-removes)]
* The first session after an install or upgrade can miss flag-gated features and start in a different permission mode. This also describes the setups where later sessions are affected. [[lines 566-575](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/env-vars.md?plain=1#L566-L575)] [[Source](https://code.claude.com/docs/en/env-vars#first-session-after-an-install-or-upgrade)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New configuration warning: denying Bash also turns off the PowerShell tool, with fixes. [[lines 5336-5350](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/errors.md?plain=1#L5336-L5350)] [[Source](https://code.claude.com/docs/en/errors#denying-bash-also-turns-off-the-powershell-tool)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* New "How `if` patterns match Bash commands" section. Leading `VAR=value` assignments are stripped before matching. [[lines 407-421](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/hooks.md?plain=1#L407-L421)] [[Source](https://code.claude.com/docs/en/hooks#common-fields)]
* New section "Tools that require user interaction". A `PreToolUse` hook can answer `AskUserQuestion` or `ExitPlanMode` by returning `allow` with `updatedInput`, with an example. MCP tools marked `requiresUserInteraction` can't be bypassed. [[lines 1800-1832](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/hooks.md?plain=1#L1800-L1832)] [[Source](https://code.claude.com/docs/en/hooks#pretooluse-decision-control)]
* Top-level `decision` and `reason` on PreToolUse are deprecated. Use `hookSpecificOutput.permissionDecision`. [[line 1794](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/hooks.md?plain=1#L1794)] [[Source](https://code.claude.com/docs/en/hooks#pretooluse-decision-control)]

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* New agent view actions (v2.1.288+): `agents:find`, `agents:rename`, `agents:previousGroup`, `agents:nextGroup`. [[lines 411-414](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/keybindings.md?plain=1#L411-L414)] [[Source](https://code.claude.com/docs/en/keybindings#agents-actions)]

#### [managed-mcp](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/managed-mcp.md) [[Source](https://code.claude.com/docs/en/managed-mcp)]

* Restructured allowlist matching into per-type sections (`serverName`, `serverCommand`, `serverUrl`). It adds that commands must match exactly, `env` isn't compared, and hostnames are case-insensitive. [[lines 265-310](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/managed-mcp.md?plain=1#L265-L310)] [[Source](https://code.claude.com/docs/en/managed-mcp#match-servers-by-url-command-or-name)]
* Policy entries expand `${VAR}` from a pinned environment (v2.1.219+). Servers from `managedMcpServers` skip the allowlist. [[lines 243-335](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/managed-mcp.md?plain=1#L243-L335)] [[Source](https://code.claude.com/docs/en/managed-mcp#policy-based-control-with-allowlists-and-denylists)]
* New "How a server is evaluated" section: merge lists, check denylist, check allowlist. [[lines 332-356](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/managed-mcp.md?plain=1#L332-L356)] [[Source](https://code.claude.com/docs/en/managed-mcp#how-serverurl-entries-match)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Availability fallback on Bedrock and Google's Agent Platform respects the allowlist. `MAX_THINKING_TOKENS=0` behavior clarified for newer models. [[lines 262-690](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/model-config.md?plain=1#L262-L690)] [[Source](https://code.claude.com/docs/en/model-config#restrict-model-selection)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* New table of content attributes under detailed beta tracing (`new_context`, `system_reminders`, `tool_input`, and others) and the variable each needs. [[lines 337-356](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/monitoring-usage.md?plain=1#L337-L356)] [[Source](https://code.claude.com/docs/en/monitoring-usage#span-attributes)]
* The `user_prompt` event gains a `prompt_text` attribute. The security notes explain how to drop both with a Collector processor. [[lines 737-1567](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/monitoring-usage.md?plain=1#L737-L1567)] [[Source](https://code.claude.com/docs/en/monitoring-usage#user-prompt-event)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Protected directory exceptions: `.claude/worktrees` and auto memory markdown files. Critical-path removal checks now look inside inline `-c` scripts. [[lines 629-684](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/permission-modes.md?plain=1#L629-L684)] [[Source](https://code.claude.com/docs/en/permission-modes#protected-paths)]

#### [google-vertex-ai](https://github.com/gpambrozio/ClaudeDocs/blob/0123f2c2df278c9701b11fb801c7118a18b466ef/docs-md/claude-code/google-vertex-ai.md) [[Source](https://code.claude.com/docs/en/google-vertex-ai)]

* Adds a section on startup model checks under `enforceAvailableModels`, parallel to the Bedrock page.

#### Other changed documents

Smaller edits, not itemized, touched these pages: agent-view, claude-apps-gateway, claude-apps-gateway-deploy, code-review, desktop, desktop-changelog, ide-integrations, interactive-mode, managed-settings, plugins/cli-reference, plugins/loading, plugins/mods/reference, self-hosted-environments-deploy, skills, slash-commands, tools-reference, vs-code and web-quickstart.

-----

## API changes

No API documentation changes today.
