# [Claude docs changes for April 23rd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/01504a39cd024d467ec6a5cc658468c1cf23cab5) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/01504a39cd024d467ec6a5cc658468c1cf23cab5)]

## Executive Summary
- Vim visual mode (`v`/`V`) and custom themes (via `/theme`) added to the Claude Code UI
- Hooks can now invoke MCP tools directly via `type: "mcp_tool"` in shell command hooks
- Linux package manager support added (apt for Debian/Ubuntu, dnf for Fedora/RHEL, apk for Alpine)
- Voice dictation gains tap-to-toggle mode alongside the existing hold-to-talk mode
- Auto mode configuration extracted into a dedicated reference page (`auto-mode-config.md`)

## New Claude Code versions

### [2.1.118](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/versions/2.1.118.md)

#### New features

* Added vim visual mode (`v`) and visual-line mode (`V`) with selection, operators, and visual feedback
* Merged `/cost` and `/stats` into `/usage` — both remain as typing shortcuts that open the relevant tab
* Create and switch between named custom themes from `/theme`, or hand-edit JSON files in `~/.claude/themes/`; plugins can also ship themes via a `themes/` directory
* Hooks can now invoke MCP tools directly via `type: "mcp_tool"`
* Added `DISABLE_UPDATES` env var to completely block all update paths including manual `claude update` — stricter than `DISABLE_AUTOUPDATER`
* WSL on Windows can now inherit Windows-side managed settings via the `wslInheritsWindowsSettings` policy key
* Auto mode: include `"$defaults"` in `autoMode.allow`, `autoMode.soft_deny`, or `autoMode.environment` to add custom rules alongside the built-in list instead of replacing it
* Added a "Don't ask again" option to the auto mode opt-in prompt
* Added `claude plugin tag` to create release git tags for plugins with version validation
* `--continue`/`--resume` now find sessions that added the current directory via `/add-dir`
* `/color` now syncs the session accent color to claude.ai/code when Remote Control is connected
* The `/model` picker now honors `ANTHROPIC_DEFAULT_*_MODEL_NAME`/`_DESCRIPTION` overrides when using a custom `ANTHROPIC_BASE_URL` gateway

#### Existing feature improvements

* When auto-update skips a plugin due to another plugin's version constraint, the skip now appears in `/doctor` and the `/plugin` Errors tab

#### Major bug fixes

* Fixed `/mcp` menu hiding OAuth Authenticate/Re-authenticate actions for servers configured with `headersHelper`, and HTTP/SSE MCP servers with custom headers being stuck in "needs authentication" after a transient 401
* Fixed MCP servers whose OAuth token response omits `expires_in` requiring re-authentication every hour
* Fixed MCP step-up authorization silently refreshing instead of prompting for re-consent
* Fixed multiple MCP OAuth race conditions (cross-process lock contention, macOS keychain concurrent refresh, token refresh when server revokes before local expiry)
* Fixed credential save crash on Linux/Windows corrupting `~/.claude/.credentials.json`
* Fixed `/login` having no effect in a session launched with `CLAUDE_CODE_OAUTH_TOKEN`
* Fixed plan acceptance dialog offering "auto mode" instead of "bypass permissions" when running with `--dangerously-skip-permissions`
* Fixed agent-type hooks failing with "Messages are required for agent hooks" when configured for events other than `Stop` or `SubagentStop`
* Fixed `prompt` hooks re-firing on tool calls made by an agent-hook verifier subagent
* Fixed `/fork` writing the full parent conversation to disk per fork — now writes a pointer and hydrates on read
* Fixed Alt+K / Alt+X / Alt+^ / Alt+_ freezing keyboard input
* Fixed connecting to a remote session overwriting your local `model` setting in `~/.claude/settings.json`
* Fixed typeahead showing "No commands match" error when pasting file paths that start with `/`
* Fixed `plugin install` on an already-installed plugin not re-resolving a dependency installed at the wrong version
* Fixed Remote Control sessions getting archived on transient CCR initialization blips during JWT refresh
* Fixed subagents resumed via `SendMessage` not restoring the explicit `cwd` they were spawned with

-----

## Claude Code changes

### New Documents

#### [auto-mode-config](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/auto-mode-config.md) [[Source](https://code.claude.com/docs/en/auto-mode-config)]

New dedicated configuration reference for the auto mode classifier (previously embedded in `permissions.md`). Covers how to define trusted infrastructure via `autoMode.environment`, override block/allow rules with `autoMode.soft_deny` and `autoMode.allow`, inspect the effective config with `claude auto-mode` subcommands, and review denials via the `/permissions` Recently denied tab.

### Changed documents

#### [agent-sdk/hooks](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/agent-sdk/hooks.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

* Added `"defer"` as a new `permissionDecision` value in the TypeScript SDK `PreToolUse` hook — allows pausing execution and resuming later from a persisted session. Not available in the Python SDK. [[line 179](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L179)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#outputs)]
* Updated hook priority order to: deny > defer > ask > allow [[line 183](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L183)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#outputs)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Added `deferred_tool_use` field to `SDKResultMessage` type carrying the pending tool's `id`, `name`, and `input` when a `PreToolUse` hook returns `"defer"` [[line 885](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L885)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkresultmessage)]
* Added `"defer"` as valid value for `permissionDecision` in `SyncHookJSONOutput` type definition [[line 1316](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1316)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#synchookjsonoutput)]

#### [agent-sdk/user-input](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/agent-sdk/user-input.md) [[Source](https://code.claude.com/docs/en/agent-sdk/user-input)]

* Added note that the `canUseTool` callback can stay pending indefinitely, and that the TypeScript SDK supports `defer` to let the process exit and resume later from a persisted session [[line 6](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/agent-sdk/user-input.md?plain=1#L6)] [[Source](https://code.claude.com/docs/en/agent-sdk/user-input)]

#### [claude-directory](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* Added `tasks/`, `shell-snapshots/`, and `backups/` to the auto-cleanup section (previously `backups/` and `shell-snapshots/` were listed under "kept until you delete them") [[line 189](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/claude-directory.md?plain=1#L189)] [[Source](https://code.claude.com/docs/en/claude-directory#cleaned-up-automatically)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/voice` command now accepts optional `[hold|tap|off]` modes [[line 92](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/commands.md?plain=1#L92)] [[Source](https://code.claude.com/docs/en/commands)]

#### [common-workflows](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Added note that `--resume`, `--continue`, and `/resume` offer to resume old large sessions from a summary instead of loading the full transcript (not available on Bedrock, Vertex AI, or Foundry) [[line 578](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/common-workflows.md?plain=1#L578)] [[Source](https://code.claude.com/docs/en/common-workflows#resume-previous-conversations)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* Changed recommendation for large `CLAUDE.md` to use path-scoped rules (load only when relevant) rather than imports (which still load at launch and consume context) [[line 330](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/errors.md?plain=1#L330)] [[Source](https://code.claude.com/docs/en/errors#prompt-is-too-long)]

#### [google-vertex-ai](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/google-vertex-ai.md) [[Source](https://code.claude.com/docs/en/google-vertex-ai)]

* Added multi-region endpoint support: `CLOUD_ML_REGION` can now be set to `global`, a multi-region location (`eu`, `us`), or a specific region; Claude Code selects the correct hostname automatically [[line 41](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/google-vertex-ai.md?plain=1#L41)] [[Source](https://code.claude.com/docs/en/google-vertex-ai#region-configuration)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Deferred sessions are now subject to the `cleanupPeriodDays` retention sweep (30 days by default) [[line 1040](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/hooks.md?plain=1#L1040)] [[Source](https://code.claude.com/docs/en/hooks#defer-a-tool-call-for-later)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Updated voice dictation shortcut description to reflect both hold and tap modes [[line 88](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/interactive-mode.md?plain=1#L88)] [[Source](https://code.claude.com/docs/en/interactive-mode#voice-input)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* GitHub MCP server connection example updated: now requires a personal access token (PAT) passed as an `Authorization` header instead of the previous OAuth flow [[line 1257](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/mcp.md?plain=1#L1257)] [[Source](https://code.claude.com/docs/en/mcp#example-connect-to-github-for-code-reviews)]

#### [memory](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Clarified that `@path` imports do not reduce context (imported files still load at launch); path-scoped rules are now the recommended approach for large `CLAUDE.md` files [[line 68](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/memory.md?plain=1#L68)] [[Source](https://code.claude.com/docs/en/memory#write-effective-instructions)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Added note that `/model` selection persists across restarts; if project settings pin a different model, the choice is written to `.claude/settings.local.json` so it continues to apply [[line 43](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/model-config.md?plain=1#L43)] [[Source](https://code.claude.com/docs/en/model-config#setting-your-model)]
* Simplified effort level defaults: `xhigh` on Opus 4.7, `high` on Opus 4.6 and Sonnet 4.6 (removed per-plan differentiation) [[line 151](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/model-config.md?plain=1#L151)] [[Source](https://code.claude.com/docs/en/model-config#adjust-effort-level)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Added `effort` attribute to cost counter, token counter, API event, and API error event telemetry [[lines 406-536](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/monitoring-usage.md?plain=1#L406-L536)] [[Source](https://code.claude.com/docs/en/monitoring-usage#cost-counter)]
* Added `command_name` and `command_source` attributes to user_prompt event [[line 466](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/monitoring-usage.md?plain=1#L466)] [[Source](https://code.claude.com/docs/en/monitoring-usage#user-prompt-event)]
* `OTEL_LOG_TOOL_DETAILS=1` now also exposes verbatim custom, plugin, and MCP command names on `user_prompt` events [[line 77](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/monitoring-usage.md?plain=1#L77)] [[Source](https://code.claude.com/docs/en/monitoring-usage#common-configuration-variables)]

#### [network-config](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/network-config.md) [[Source](https://code.claude.com/docs/en/network-config)]

* Network access requirements reformatted as a table listing each URL with its purpose, and clarified when Bedrock/Vertex/Foundry providers replace `api.anthropic.com` [[line 88](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/network-config.md?plain=1#L88)] [[Source](https://code.claude.com/docs/en/network-config#network-access-requirements)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Links to auto mode classifier configuration now point to the new `auto-mode-config.md` page instead of `permissions.md` [[lines 131-28](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/permission-modes.md?plain=1#L131)] [[Source](https://code.claude.com/docs/en/permission-modes#what-the-classifier-blocks-by-default)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Large "Configure the auto mode classifier" and "Review auto mode denials" sections removed — content moved to the new `auto-mode-config.md` page

#### [plugin-dependencies](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/plugin-dependencies.md) [[Source](https://code.claude.com/docs/en/plugin-dependencies)]

* Added `dependency-unsatisfied` error to the error table with resolution steps [[line 192](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/plugin-dependencies.md?plain=1#L192)] [[Source](https://code.claude.com/docs/en/plugin-dependencies#see-also)]
* Clarified that re-running `claude plugin install` or adding a new marketplace also resolves outstanding missing dependencies

#### [plugin-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Marketplace restrictions (`strictKnownMarketplaces`, `blockedMarketplaces`) are now enforced on plugin install, update, refresh, and auto-update — not just on marketplace add. A marketplace added before the policy was set cannot be used to fetch plugins once its source no longer matches the allowlist [[line 204](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/plugin-marketplaces.md?plain=1#L204)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#optional-plugin-fields)]

#### [quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/quickstart.md) [[Source](https://code.claude.com/docs/en/quickstart)]

* Added mention of Linux package manager installation (apt, dnf, apk)

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Remote Control is now described as "research preview" [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/remote-control.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/remote-control)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added new `voice` settings object (`enabled`, `mode`, `autoSubmit`) to replace the legacy `voiceEnabled` key (which remains as an alias) [[line 277](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/settings.md?plain=1#L277)] [[Source](https://code.claude.com/docs/en/settings#sandbox-settings)]
* `blockedMarketplaces` and `strictKnownMarketplaces` descriptions updated to reflect enforcement on install/update/refresh/auto-update cycles [[lines 263-272](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/settings.md?plain=1#L263-L272)] [[Source](https://code.claude.com/docs/en/settings#sandbox-settings)]

#### [setup](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* Added full Linux package manager installation instructions for apt (Debian/Ubuntu), dnf (Fedora/RHEL), and apk (Alpine) with signed repository setup and GPG key verification [[line 265](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/setup.md?plain=1#L265)] [[Source](https://code.claude.com/docs/en/setup#install-a-specific-version)]
* Added uninstall instructions for apt/dnf/apk [[line 458](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/setup.md?plain=1#L458)] [[Source](https://code.claude.com/docs/en/setup#winget-installation)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Clarified that `mcpServers` field applies both when the agent runs as a subagent and when launched as the main session via `--agent` [[line 311](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/sub-agents.md?plain=1#L311)] [[Source](https://code.claude.com/docs/en/sub-agents#scope-mcp-servers-to-a-subagent)]

#### [terminal-guide](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/terminal-guide.md) [[Source](https://code.claude.com/docs/en/terminal-guide)]

* Added system requirements callouts: macOS 13.0+ for macOS, Windows 10 version 1809+ for Windows [[lines 12-59](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/terminal-guide.md?plain=1#L12-L59)] [[Source](https://code.claude.com/docs/en/terminal-guide#macos-and-linux)]
* Added dyld error troubleshooting section for users on unsupported macOS versions [[line 209](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/terminal-guide.md?plain=1#L209)] [[Source](https://code.claude.com/docs/en/terminal-guide#macos-and-linux-troubleshooting)]

#### [voice-dictation](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/voice-dictation.md) [[Source](https://code.claude.com/docs/en/voice-dictation)]

* Added tap mode: tap once to start recording, tap again to send — no hold required. Enable with `/voice tap` [[line 67](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/voice-dictation.md?plain=1#L67)] [[Source](https://code.claude.com/docs/en/voice-dictation#tap-to-record-and-send)]
* Added `autoSubmit` option for hold mode: sends the prompt automatically on key release when transcript is at least three words [[line 62](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/voice-dictation.md?plain=1#L62)] [[Source](https://code.claude.com/docs/en/voice-dictation#hold-to-record)]
* Added VS Code extension voice dictation support note (not available in VS Code Remote sessions) [[line 27](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/voice-dictation.md?plain=1#L27)] [[Source](https://code.claude.com/docs/en/voice-dictation#enable-voice-dictation)]
* Transcription does not consume Claude messages or tokens and does not count toward `/usage` limits [[line 17](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/voice-dictation.md?plain=1#L17)] [[Source](https://code.claude.com/docs/en/voice-dictation#enable-voice-dictation)]
* Added new troubleshooting entries: "No audio detected", "No speech detected", and tap mode space key behavior [[lines 137-141](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/voice-dictation.md?plain=1#L137-L141)] [[Source](https://code.claude.com/docs/en/voice-dictation#troubleshooting)]

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* GitHub MCP server example updated to use a personal access token passed as a header [[line 303](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/claude-code/vs-code.md?plain=1#L303)] [[Source](https://code.claude.com/docs/en/vs-code#connect-to-external-tools-with-mcp)]

-----

## API changes

### Changed documents

#### [build-with-claude/vision](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/api/build-with-claude/vision.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/vision)]

* Added guidance on image compression: using lossy formats (JPEG/WebP) can reduce latency but may introduce artifacts that harm model performance, especially text legibility [[line 95](https://github.com/gpambrozio/ClaudeDocs/blob/01504a39cd024d467ec6a5cc658468c1cf23cab5/docs-md/api/build-with-claude/vision.md?plain=1#L95)] [[Source](https://platform.claude.com/docs/en/build-with-claude/vision)]
