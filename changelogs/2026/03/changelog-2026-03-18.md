# [Claude docs changes for March 18th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/fa2c53b) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/fa2c53b)]

## Executive Summary
- **Voice dictation is now fully documented**: push-to-talk transcription (hold Space) with 20-language support, live waveform, coding-vocabulary tuning — requires Claude.ai account auth
- **New `StopFailure` hook** fires when a turn ends due to API errors (rate limit, auth failure), enabling automated error recovery flows
- **Plugin persistent state via `${CLAUDE_PLUGIN_DATA}`**: survives plugin updates; `/plugin uninstall --keep-data` preserves it; full lifecycle docs added
- **Subagent invocation expanded**: @-mention for one-task delegation and `--agent`/`agent` setting for session-wide subagent mode now documented
- **Sandbox read control**: new `filesystem.allowRead` and `allowManagedReadPathsOnly` let you whitelist specific paths within a broader `denyRead` region

## New Claude Code versions

### [2.1.78](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/versions/2.1.78.md)

#### New features

* Added `StopFailure` hook event — fires when a turn ends due to API error (rate limit, auth failure, etc.)
* Added `${CLAUDE_PLUGIN_DATA}` variable for plugin persistent state that survives plugin updates; `/plugin uninstall` prompts before deleting it
* Added `effort`, `maxTurns`, and `disallowedTools` frontmatter support for plugin-shipped agents
* Added `ANTHROPIC_CUSTOM_MODEL_OPTION` env var for a custom entry in the `/model` picker, with optional `_NAME` and `_DESCRIPTION` suffix vars
* Response text now streams line-by-line as it's generated

#### Existing feature improvements

* Terminal notifications (iTerm2/Kitty/Ghostty popups, progress bar) now reach the outer terminal when running inside tmux with `set -g allow-passthrough on`
* Improved memory usage and startup time when resuming large sessions

#### Major bug fixes

* **Security:** Fixed silent sandbox disable when `sandbox.enabled: true` is set but dependencies are missing — now shows a visible startup warning
* Fixed `.git`, `.claude`, and other protected directories being writable without a prompt in `bypassPermissions` mode
* Fixed infinite loop when API errors triggered stop hooks that re-fed blocking errors to the model
* Fixed `deny: ["mcp__servername"]` permission rules not removing MCP server tools before sending to the model
* Fixed `sandbox.filesystem.allowWrite` not working with absolute paths (previously required `//` prefix)
* Fixed `cc log` and `--resume` silently truncating conversation history on large sessions (>5 MB) that used subagents
* Fixed `git log HEAD` failing with "ambiguous argument" inside sandboxed Bash on Linux
* Fixed voice mode modifier-combo push-to-talk keybindings (e.g. `ctrl+k`) requiring a hold instead of activating immediately
* Fixed voice mode not working on WSL2 with WSLg (Windows 11); WSL1/Win10 users now get a clear error
* Fixed `--worktree` flag not loading skills and hooks from the worktree directory
* Fixed `ANTHROPIC_BETAS` environment variable being silently ignored when using Haiku models
* Fixed Bash tool not finding Homebrew and other PATH-dependent binaries when VS Code is launched from Dock/Spotlight
* [VSCode] Fixed "API Error: Rate limit reached" when selecting Opus — model dropdown no longer offers 1M context variant to subscribers whose plan tier is unknown

-----

## Claude Code changes

### New Documents

#### [voice-dictation](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/voice-dictation.md) [[Source](https://code.claude.com/docs/en/voice-dictation)]

New page documenting push-to-talk voice dictation. Requires Claude Code v2.1.69+ and Claude.ai account authentication (not available with API keys, Bedrock, Vertex, or Foundry). Covers enabling via `/voice` command, default Space push-to-talk keybinding (rebindable to modifier combos), live waveform display, 20-language support, coding-vocabulary transcription tuning, and platform support (macOS, Linux, Windows; not available in remote/SSH). Includes troubleshooting for microphone permissions, Linux audio tools, and WSL.

### Changed documents

#### [amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* `ANTHROPIC_SMALL_FAST_MODEL` renamed to `ANTHROPIC_DEFAULT_HAIKU_MODEL` in the Bedrock configuration example. [[line reference](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/amazon-bedrock.md?plain=1)]

#### [authentication](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/authentication.md) [[Source](https://code.claude.com/docs/en/authentication)]

* Expanded credential storage documentation: Linux/Windows credential storage location clarified (`~/.claude/.credentials.json` or `$CLAUDE_CONFIG_DIR`; Linux file mode `0600`).
* New: `apiKeyHelper` slow-helper warning — if helper takes >10 seconds, a warning appears in the prompt bar.
* New: clarification that `apiKeyHelper`, `ANTHROPIC_API_KEY`, and `ANTHROPIC_AUTH_TOKEN` only apply to terminal CLI sessions; Claude Desktop and remote sessions use OAuth exclusively.
* New section: **Authentication precedence** — documents full 5-step resolution order: cloud provider env vars → `ANTHROPIC_AUTH_TOKEN` → `ANTHROPIC_API_KEY` → `apiKeyHelper` → subscription OAuth.
* Note added: if `ANTHROPIC_API_KEY` is set and approved, it takes precedence over an active subscription and can cause auth failures if the key's org is disabled.

#### [best-practices](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

* `--dangerously-skip-permissions` description clarified: bypasses "permission prompts" not "all permission checks"; added cross-reference to `permissions.md` for what is/isn't skipped.

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* `--dangerously-skip-permissions` flag description updated with cross-reference to `permissions.md`.

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/copy` now accepts an `[N]` argument to copy the Nth-latest response (e.g., `/copy 2` for the second-to-last).
* `/fork` renamed to `/branch` (with `/fork` kept as an alias).
* `/init` updated: mentions `CLAUDE_CODE_NEW_INIT=true` env var for interactive setup flow that also sets up skills, hooks, and personal memory files.
* New `/voice` command: toggle push-to-talk voice dictation; requires a Claude.ai account.

#### [common-workflows](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Plan mode: accepting a plan now automatically names the session from the plan content (won't overwrite an existing `--name`/`/rename`).
* Extended thinking section rewritten: adaptive reasoning controls depth on newer models; `MAX_THINKING_TOKENS` only applies when set to `0` or `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1` on Opus 4.6/Sonnet 4.6.
* Session picker: forked sessions now reference `/branch` command as well as `/rewind`.

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* Extended thinking default budget description updated: removed specific "31,999 tokens" number; now says "can be tens of thousands of tokens per request depending on the model".

#### [data-usage](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/data-usage.md) [[Source](https://code.claude.com/docs/en/data-usage)]

* `/bug` command renamed to `/feedback` throughout.
* `DISABLE_BUG_COMMAND` env var renamed to `DISABLE_FEEDBACK_COMMAND`.

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* `bypassPermissions` mode description updated: clarifies protected directories still prompt even in bypass mode; cross-reference to `permissions.md` added.

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `ANTHROPIC_API_KEY` description significantly expanded: explains precedence over subscriptions and interactive approval behavior.
* New env var: `ANTHROPIC_BASE_URL` — override API endpoint for proxy/gateway; when set to a non-Anthropic host, MCP tool search is disabled by default (`ENABLE_TOOL_SEARCH=true` to override).
* `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` description expanded: also strips beta tool-schema fields like `defer_loading` and `eager_input_streaming`.
* `CLAUDE_CODE_MAX_OUTPUT_TOKENS` updated: defaults and caps are now model-specific.
* New env var: `CLAUDE_CODE_NEW_INIT` — set to `true` for interactive `/init` flow that includes skills, hooks, and personal memory setup.
* New env var: `CLAUDE_CODE_PLUGIN_SEED_DIR` — path to read-only plugin seed directory for containers; pre-populates plugins without runtime cloning.
* `DISABLE_BUG_COMMAND` replaced by `DISABLE_FEEDBACK_COMMAND` (old name still accepted).

#### [google-vertex-ai](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/google-vertex-ai.md) [[Source](https://code.claude.com/docs/en/google-vertex-ai)]

* `ANTHROPIC_SMALL_FAST_MODEL` renamed to `ANTHROPIC_DEFAULT_HAIKU_MODEL` in Vertex AI configuration examples.

#### [headless](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* New section: **`system/api_retry` stream event** — emitted before each retry when an API request fails with a retryable error. Documents all fields: `type`, `subtype`, `attempt`, `max_retries`, `retry_delay_ms`, `error_status`, `error` (values: `authentication_failed`, `billing_error`, `rate_limit`, `invalid_request`, `server_error`, `max_output_tokens`, `unknown`), `uuid`, `session_id`.

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* `PostCompact` added to the matcher table alongside `PreCompact`.
* `${CLAUDE_PLUGIN_DATA}` variable added to plugin hook environment variables.
* `InstructionsLoaded` hook: new `"compact"` load reason added — fires when instruction files are re-loaded after a compaction event.
* `PreToolUse` `permissionDecision` clarification: `"allow"` skips the interactive prompt but deny/ask rules still apply.

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* `PreToolUse` hook `"allow"` decision clarified: skips interactive prompt only; deny and ask rules (including managed deny lists) still apply; deny rules always take precedence over hook approvals.
* `PostCompact` matcher support added to the hooks matcher table.

#### [index](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/index.md) [[Source](https://code.claude.com/docs/en/index)]

* Example code snippet updated: `tail -f app.log` (follow mode) replaced with `tail -200 app.log` (last 200 lines).

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* New **Voice input** keyboard shortcut: "Hold Space: Push-to-talk dictation".
* Background tasks: new note that tasks are automatically terminated if output exceeds 5 GB.

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* New section: **Voice actions** — documents the `voice:pushToTalk` action (default: Space) in the `Chat` context.

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Plugin MCP environment variables updated: `${CLAUDE_PLUGIN_DATA}` documented alongside `${CLAUDE_PLUGIN_ROOT}`.

#### [memory](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* `/init` description updated: mentions `CLAUDE_CODE_NEW_INIT=true` for interactive multi-phase flow.
* New table: **Managed CLAUDE.md vs. managed settings** — clarifies which concerns go in settings (tool blocks, sandbox, env vars, auth) vs. CLAUDE.md (code style, compliance, behavioral guidance); explains settings rules are enforced while CLAUDE.md shapes but does not enforce.

#### [network-config](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/network-config.md) [[Source](https://code.claude.com/docs/en/network-config)]

* New: native installer and update checks require `downloads.claude.ai` and `storage.googleapis.com` (legacy, deprecation in progress).

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* `bypassPermissions` mode clarified: writes to `.git`, `.claude`, `.vscode`, `.idea` directories still prompt; `.claude/commands`, `.claude/agents`, `.claude/skills` are exempt.
* New: compound command approval saves separate rules per subcommand (up to 5 rules); explains how `cd` generates Read rules.
* New: clarification that `Read`/`Edit` deny rules block Claude's built-in file tools but not Bash subprocesses (e.g., `cat .env`); sandbox needed for OS-level enforcement.
* New: Windows path normalization in permissions matching (`C:\Users\alice` becomes `/c/Users/alice`).
* New managed setting: `sandbox.filesystem.allowManagedReadPathsOnly`.

#### [plugin-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* `${CLAUDE_PLUGIN_DATA}` documented alongside `${CLAUDE_PLUGIN_ROOT}`.
* New section: **Pre-populate plugins for containers** — `CLAUDE_CODE_PLUGIN_SEED_DIR` env var; details on seed directory structure, build-time population, read-only behavior, precedence, and path resolution.
* Validator expanded: now checks skill/agent/command frontmatter and `hooks/hooks.json` in addition to `plugin.json`.
* New validation errors documented: YAML frontmatter parse failure, `hooks/hooks.json` JSON syntax error.
* New warning: non-kebab-case plugin names.

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* `PostCompact` added to hook event list.
* New section: **Persistent data directory** — full documentation of `${CLAUDE_PLUGIN_DATA}`, location formula, recommended pattern for managing `node_modules`, example `SessionStart` hook for dependency management, example MCP server config using `NODE_PATH`, automatic deletion on uninstall, and `/plugin` UI showing data directory size.
* `claude plugin uninstall` updated: new `--keep-data` flag to preserve the persistent data directory.

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* New section: **Troubleshooting** — covers `Remote credentials fetch failed` error (use `--verbose` to see details); common causes: not signed in, network/proxy blocking port 443, session creation failure.

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* New: `sandbox.filesystem.allowRead` to re-allow reading specific paths within a `denyRead` region; takes precedence over `denyRead`.
* New: `allowManagedReadPathsOnly` flag support.
* New code example: blocking entire home directory reads while allowing reads from current project using `denyRead` + `allowRead`.

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New setting: `agent` — run the main thread as a named subagent (applies subagent's system prompt, tool restrictions, and model).
* `language` setting updated: also controls voice dictation language.
* New setting: `voiceEnabled` — enable push-to-talk voice dictation; written automatically by the `/voice` command.
* Settings clarification: `showTurnDuration` and `terminalProgressBarEnabled` moved to new **Global config settings** section — stored in `~/.claude.json`, NOT `settings.json`; adding them to `settings.json` triggers a schema validation error.
* New sandbox settings: `filesystem.allowRead` and `filesystem.allowManagedReadPathsOnly` documented.

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Quickstart walkthrough updated: new step 7 for **Configure memory** (persistent memory directory); save step updated (`s` or `Enter` to save, `e` to save and edit).
* `bypassPermissions` description updated: "skips permission prompts" not "all permission checks"; protected directory exceptions documented.
* New section: **Invoke subagents explicitly** — three patterns documented:
  * Natural language (Claude decides)
  * **@-mention**: guaranteed delegation for one task; typeahead syntax; plugin subagents as `<plugin-name>:<agent-name>`
  * **Session-wide**: `--agent <name>` flag or `agent` setting replaces main system prompt entirely; works for built-in and custom subagents; persists on resume
* Clarified that a stopped subagent receiving `SendMessage` auto-resumes in background without a new `Agent` invocation.

#### [terminal-config](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* VS Code Option key setup separated from iTerm2 instructions: now documents `"terminal.integrated.macOptionIsMeta": true` in VS Code settings.

#### [troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/claude-code/troubleshooting.md) [[Source](https://code.claude.com/docs/en/troubleshooting)]

* New troubleshooting entry: **"This organization has been disabled" with an active subscription** — caused by `ANTHROPIC_API_KEY` overriding subscription auth; fix is `unset ANTHROPIC_API_KEY`.

-----

## API changes

### Changed documents

#### [remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/fa2c53b/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Added two new remote MCP servers to the directory:
  * **Intuit TurboTax** (`https://ai-inc.turbotax.intuit.com/.../mcp`): estimate tax refunds and connect with live tax experts.
  * **DocuSeal** (`https://docuseal.com/mcp`): sign, send & manage documents.
