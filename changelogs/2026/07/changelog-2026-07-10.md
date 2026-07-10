# [Claude docs changes for July 10th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/f87a418157a1ef4630c5b8d24d1b1e94a932aaef) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/f87a418157a1ef4630c5b8d24d1b1e94a932aaef)]

## Executive Summary
- Managed Agents: self-hosted sandbox workers can now [serve custom tools directly](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/self-hosted-sandboxes.md) — including wrapping an internal-only MCP server as custom tools — without an MCP tunnel or exposing your Claude API key to the worker host.
- Memory store endpoints (list/create/update/delete memories) move to their own [`agent-memory-2026-07-22` beta header](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/memory.md), replacing `managed-agents-2026-04-01` for those calls, with clearer `depth`/`limit`/`path_prefix` semantics — don't send both beta headers on the same request.
- New [API key expiration](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/manage-claude/authentication.md) feature: Console and Admin API keys can now be created with a preset or custom expiration (or Never), with warning emails before expiry and automatic `401`s once a key expires.
- Claude Code 2.1.206 adds directory suggestions to `/cd`, a `/doctor` check that trims bloated checked-in `CLAUDE.md` files, gateway `/login` support for Anthropic-operated public endpoints, and a confirmation prompt before entering worktrees outside the project.
- Custom tool descriptions across the Claude API can now be up to 4096 characters (up from 1024), and self-hosted work items no longer expose a `secret` credential field in their schema.

-----

## New Claude Code versions

### [2.1.206](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/versions/2.1.206.md)

#### New features

* Added directory path suggestions to `/cd`, matching `/add-dir` behavior
* Added a `/doctor` check that proposes trimming checked-in `CLAUDE.md` files by cutting content Claude could derive from the codebase
* `/commit-push-pr` now auto-allows `git push` to the repo's configured push remote (`remote.pushDefault`, or the sole remote when only one is configured) in addition to `origin`
* Gateway: `/login` now supports Anthropic-operated public gateway endpoints
* `EnterWorktree` now asks for confirmation before entering a git worktree outside the project's `.claude/worktrees/` directory

#### Existing feature improvements

* Background agents now upgrade to a new version in the background right after a Claude Code update, instead of paying a slow stale-session upgrade when you attach
* Improved `/code-review` findings quality on claude-opus-4-8 across all effort levels
* Improved agents view: status column now uses full terminal width instead of truncating at 64 characters
* Changed agents view: Ctrl+X now permanently removes a completed session, and sessions no longer render twice; deleted background jobs stay deleted

#### Major bug fixes

* Fixed an expired login failing every model with a misleading "There's an issue with the selected model" error instead of prompting to run `/login`
* Fixed `claude --resume` and `--continue` not responding to keyboard input on startup
* Fixed MCP servers configured via `--mcp-config` or `.mcp.json` ignoring a per-server `request_timeout_ms`, which caused long-running MCP tool calls to time out at the 60s default in fresh sessions
* Fixed `CLAUDE_CODE_EXTRA_BODY` being silently ignored by `claude agents` / `--bg` background workers; the shell-exported override now follows the dispatching session
* Fixed OAuth MCP servers requiring manual re-authentication after a single failed token refresh
* Fixed `--permission-prompt-tool` pointing at an MCP server crashing with "MCP tool not found" on cold start before the server finishes connecting
* Fixed desktop sessions getting stuck showing "running" after a slash command was sent mid-turn
* Bedrock: fixed a multi-minute startup hang when using an `awsCredentialExport` helper on networks with restricted egress

-----

## Claude Code changes

### Changed documents

#### [How the agent loop works](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/agent-sdk/agent-loop.md) [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop)]

* With streaming input, a message sent while a turn is still running now stays queued and starts its own turn when the max-turns limit ends the current one; before v2.1.205 such a message could be silently consumed and lost. [[line 167](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/agent-sdk/agent-loop.md?plain=1#L167)] [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop)]

#### [Get structured output from agents](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/agent-sdk/structured-outputs.md) [[Source](https://code.claude.com/docs/en/agent-sdk/structured-outputs)]

* An invalid JSON Schema now fails the run at startup with an error naming the problem, instead of being silently ignored and returning unstructured text. [[line 227](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/agent-sdk/structured-outputs.md?plain=1#L227)] [[Source](https://code.claude.com/docs/en/agent-sdk/structured-outputs)]
* The `format` keyword (e.g. `"format": "email"`) is now accepted as an unenforced annotation instead of making the whole schema invalid. [[line 228](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/agent-sdk/structured-outputs.md?plain=1#L228)] [[Source](https://code.claude.com/docs/en/agent-sdk/structured-outputs)]

#### [TypeScript SDK reference](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* `interrupt()` now resolves with a new `SDKControlInterruptResponse` (when the CLI advertises the `interrupt_receipt_v1` capability) listing queued messages that survived the interrupt. [[lines 476-590](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L476-L590)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]
* New `capabilities` field on `SDKSystemMessage` for feature-detecting protocol behaviors, including `interrupt_receipt_v1`. [[lines 1139-1147](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1139-L1147)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]
* `SDKMessageOrigin`'s `peer` kind gains a `body` field alongside `name` (both require v2.1.205+). [[lines 1282-1293](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1282-L1293)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]
* `ExitPlanModeInput.allowedPrompts` is now deprecated and ignored; it previously requested prompt-based Bash permissions. [[lines 2112-2120](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L2112-L2120)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

#### [Manage multiple agents with agent view](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* Row summaries now refresh from the session's own output every 15s without a model request, with full model rewrites at turn end and periodic mid-turn rewrites, truncated at 64 columns. [[lines 125-129](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/agent-view.md?plain=1#L125-L129)] [[Source](https://code.claude.com/docs/en/agent-view)]
* Pull-request linking expanded: sessions that edit/comment/close/ready an existing PR via `gh` are now linked to it, a push links a PR regardless of branch-name match, and PRs found in truncated command output are now linked too. [[lines 134-136](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/agent-view.md?plain=1#L134-L136)] [[Source](https://code.claude.com/docs/en/agent-view)]
* `claude attach` now waits up to ~60 seconds for a session that's mid-restart instead of failing immediately. [[line 209](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/agent-view.md?plain=1#L209)] [[Source](https://code.claude.com/docs/en/agent-view)]

#### [Configure auto mode](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/auto-mode-config.md) [[Source](https://code.claude.com/docs/en/auto-mode-config)]

* Auto mode now also blocks by default: writes to Claude Code's own session transcript files, and recursive forced deletes targeting an unassigned shell variable or glob. [[lines 225-228](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/auto-mode-config.md?plain=1#L225-L228)] [[Source](https://code.claude.com/docs/en/auto-mode-config)]
* The "Repository visibility" classifier now reads only your messages and Claude's commands, not command output — a `gh repo view` result alone no longer counts as evidence a repo is public. [[lines 238-239](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/auto-mode-config.md?plain=1#L238-L239)] [[Source](https://code.claude.com/docs/en/auto-mode-config)]

#### [Use Claude Code on the web](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* Cloud sessions now support `/model`, `/effort`, `/fast`, `/color`, and `/rename` with a value argument (e.g. `/model sonnet`), and `/config key=value`, instead of requiring the terminal picker. [[line 645](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L645)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

#### [CLI reference](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* New `claude doctor` command for read-only installation/settings diagnostics from the terminal without starting a session. [[line 25](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/cli-reference.md?plain=1#L25)] [[Source](https://code.claude.com/docs/en/cli-reference)]
* New `--append-subagent-system-prompt` flag to append text to every subagent's system prompt in non-interactive mode. [[line 54](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/cli-reference.md?plain=1#L54)] [[Source](https://code.claude.com/docs/en/cli-reference)]
* `--json-schema` and `--max-turns` now document the invalid-schema error and the queued-message-on-limit behavior described in the SDK docs above. [[lines 84-87](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/cli-reference.md?plain=1#L84-L87)] [[Source](https://code.claude.com/docs/en/cli-reference)]

#### [Commands](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/doctor` is rewritten as a "setup checkup" skill: it finds unused skills/MCP servers/plugins, deduplicates `CLAUDE.md` files, migrates guidance into skills, flags slow hooks, and asks for confirmation before changing anything — replacing the old read-only diagnostics screen. [[line 57](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/commands.md?plain=1#L57)] [[Source](https://code.claude.com/docs/en/commands)]
* `/effort`, `/fast`, `/color`, `/mcp`, `/model`, and `/rename` now document non-interactive (`-p`) support with value arguments; `/usage-credits` now opens/prints the billing URL. [[lines 44-126](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/commands.md?plain=1#L44-L126)] [[Source](https://code.claude.com/docs/en/commands)]

#### [Debug your configuration](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/debug-your-config.md) [[Source](https://code.claude.com/docs/en/debug-your-config)]

* `/doctor` reference rewritten to "Setup checkup": installation health, invalid settings, unused extensions, and duplicate subagent names, with proposed fixes applied only after confirmation; also documents the new `claude doctor` terminal command. [[lines 18-32](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/debug-your-config.md?plain=1#L18-L32)] [[Source](https://code.claude.com/docs/en/debug-your-config)]
* An array-value schema error in `settings.json` now rejects the whole file in user/project/local scope, but only strips the invalid entry in managed settings. [[lines 48-52](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/debug-your-config.md?plain=1#L48-L52)] [[Source](https://code.claude.com/docs/en/debug-your-config)]

#### [Desktop application](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Permission modes renamed: "Ask permissions" → "Manual", "Auto accept edits" → "Accept edits", "Plan mode" → "Plan"; bypass-permissions now also covers safety-classifier prompts when Claude acts on external sites. [[lines 58-73](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/desktop.md?plain=1#L58-L73)] [[Source](https://code.claude.com/docs/en/desktop)]
* "Preview pane" renamed to "Browser pane", with a new "Browse external sites" feature: tabbed browsing, per-site approval (Allow once/Always allow/Deny), safety classifiers on write actions, and org-level allowlist/blocklist controls via a new `browserExternalPageTools` managed setting. [[lines 80-115](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/desktop.md?plain=1#L80-L115)] [[Source](https://code.claude.com/docs/en/desktop)]

#### [Get started with the desktop app](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/desktop-quickstart.md) [[Source](https://code.claude.com/docs/en/desktop-quickstart)]

* Permission mode list restructured to Manual/Accept edits/Plan, and the "Preview" pane is now the "Browser" pane, which can also open external sites. [[lines 85-108](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/desktop-quickstart.md?plain=1#L85-L108)] [[Source](https://code.claude.com/docs/en/desktop-quickstart)]

#### [Environment variables](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_ENABLE_APPEND_SUBAGENT_PROMPT` variable, auto-set by `--append-subagent-system-prompt`. [[line 189](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/env-vars.md?plain=1#L189)] [[Source](https://code.claude.com/docs/en/env-vars)]
* `DISABLE_DOCTOR_COMMAND` now hides the `/doctor` setup-checkup skill and its `/checkup` alias instead of the old diagnostics screen; it doesn't affect `claude doctor`. [[line 197](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/env-vars.md?plain=1#L197)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [Error reference](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New "The `--json-schema` value is not a valid JSON Schema" section: an invalid schema now exits with code 1 and a diagnostic instead of silently producing unstructured output. [[lines 909-931](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/errors.md?plain=1#L909-L931)] [[Source](https://code.claude.com/docs/en/errors)]
* New "Could not import a server from Claude Desktop" section: `claude mcp add-from-claude-desktop` now imports the other selected servers and reports each one it couldn't add, instead of aborting the whole import on the first failure. [[lines 933-944](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/errors.md?plain=1#L933-L944)] [[Source](https://code.claude.com/docs/en/errors)]
* New "Plugin errors" section covering a marketplace registered under a name reserved for official Anthropic marketplaces — Claude Code now re-checks reserved names on every load, not just when the marketplace is added. [[lines 946-963](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/errors.md?plain=1#L946-L963)] [[Source](https://code.claude.com/docs/en/errors)]
* A download that stays connected but doesn't finish within 10 minutes now fails with `Download timed out: exceeded the total deadline` and isn't retried automatically. [[line 886](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/errors.md?plain=1#L886)] [[Source](https://code.claude.com/docs/en/errors)]
* Documents that a restricted model-family alias (`opus`/`sonnet`/`haiku`/`fable`) now resolves to the newest permitted version under an org's allowlist instead of being substituted/rejected based on the family's newest release alone. [[line 769](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/errors.md?plain=1#L769)] [[Source](https://code.claude.com/docs/en/errors)]

#### [Speed up responses with fast mode](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* `/fast` now works in non-interactive (`-p`) mode only when the session was launched with fast mode enabled via `--settings`, applying to that session only. [[line 26](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/fast-mode.md?plain=1#L26)] [[Source](https://code.claude.com/docs/en/fast-mode)]

#### [Run Claude Code programmatically](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* Documents the new `--json-schema` validation error and that `format` is accepted but unenforced. [[line 108](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/headless.md?plain=1#L108)] [[Source](https://code.claude.com/docs/en/headless)]
* The `system/init` event now carries an optional `capabilities` array for feature-detecting protocol behaviors such as `interrupt_receipt_v1`. [[line 153](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/headless.md?plain=1#L153)] [[Source](https://code.claude.com/docs/en/headless)]

#### [Hooks reference](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* `ExitPlanMode`'s `tool_input.allowedPrompts` field is now deprecated and ignored by Claude Code. [[lines 1378-1384](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/hooks.md?plain=1#L1378-L1384)] [[Source](https://code.claude.com/docs/en/hooks)]
* `WorktreeCreate` command hooks must now print the path as the last non-empty line of stdout; a bad or relative path fails cleanly with an error instead of crashing the session or stalling ~30s in `-p` mode. [[lines 2344-2348](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/hooks.md?plain=1#L2344-L2348)] [[Source](https://code.claude.com/docs/en/hooks)]

#### [How Claude Code works](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/how-claude-code-works.md) [[Source](https://code.claude.com/docs/en/how-claude-code-works)]

* Permission mode names updated (Default → Manual, Auto-accept edits → Accept edits, Plan mode → Plan, Auto mode → Auto), and `/doctor` is now described as running a setup checkup that can fix problems it finds. [[lines 127-146](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/how-claude-code-works.md?plain=1#L127-L146)] [[Source](https://code.claude.com/docs/en/how-claude-code-works)]

#### [Customize keyboard shortcuts](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* The dedicated `Doctor` keybinding context and `doctor:fix` action are removed along with the old diagnostics screen; keybinding validation warnings now go to the debug log instead of `/doctor`. [[lines 63-467](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/keybindings.md?plain=1#L63-L467)] [[Source](https://code.claude.com/docs/en/keybindings)]

#### [Connect Claude Code to an LLM gateway](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/llm-gateway-connect.md) [[Source](https://code.claude.com/docs/en/llm-gateway-connect)]

* Points to the Remote Control section of `claude doctor` (instead of `/doctor`) to find which credential variable to unset. [[line 238](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/llm-gateway-connect.md?plain=1#L238)] [[Source](https://code.claude.com/docs/en/llm-gateway-connect)]

#### [Connect Claude Code to tools via MCP](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Reserves more MCP server names (`claude-in-chrome`, `computer-use`, `Claude Preview`, `Claude Browser`); `claude mcp add` now rejects reserved names with an error. [[lines 153-154](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/mcp.md?plain=1#L153-L154)] [[Source](https://code.claude.com/docs/en/mcp)]
* Claude Code now surfaces MCP connection failures to the model (including in `ToolSearch` results) instead of silently treating the server as never configured. [[line 164](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/mcp.md?plain=1#L164)] [[Source](https://code.claude.com/docs/en/mcp)]
* `claude mcp add-from-claude-desktop` now reports and skips servers with invalid names instead of aborting the whole import. [[line 748](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/mcp.md?plain=1#L748)] [[Source](https://code.claude.com/docs/en/mcp)]

#### [Start with Opus](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Model family aliases (`opus`/`sonnet`/`haiku`/`fable`) restricted by an `availableModels` allowlist now resolve to the newest permitted version instead of being rejected outright; Claude Code only rejects `/model <alias>` when every version of the family is restricted. [[lines 113-276](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/model-config.md?plain=1#L113-L276)] [[Source](https://code.claude.com/docs/en/model-config)]
* `opusplan` (and the Haiku→Sonnet plan-mode upgrade) now uses the newest permitted version of the upgrade family instead of falling back to the session's model whenever the newest version is excluded. [[line 276](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/model-config.md?plain=1#L276)] [[Source](https://code.claude.com/docs/en/model-config)]
* Clarifies `/effort` set non-interactively (`-p`) applies to that session only, and reports `Not applied` when it can't override a model-default effort hold on Fable 5/Opus 4.8/4.7. [[lines 353-354](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/model-config.md?plain=1#L353-L354)] [[Source](https://code.claude.com/docs/en/model-config)]

#### [Monitoring](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Credential-helper failure errors are now reported via `/status` output instead of `/doctor`. [[line 270](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/monitoring-usage.md?plain=1#L270)] [[Source](https://code.claude.com/docs/en/monitoring-usage)]

#### [Choose a permission mode](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Auto mode now also blocks writes to Claude Code's own session transcript files, and recursive forced deletes targeting an unassigned shell variable or glob, by default. [[lines 225-228](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/permission-modes.md?plain=1#L225-L228)] [[Source](https://code.claude.com/docs/en/permission-modes)]

#### [Create and distribute a plugin marketplace](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Two more marketplace names are reserved (`first-party-plugins`, `healthcare`), and Claude Code now re-checks reserved names on every marketplace load, not just when it's added. [[line 164](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/plugin-marketplaces.md?plain=1#L164)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

#### [Plugins reference](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* New LSP config fields `shutdownTimeout` and `restartOnCrash`, which previously caused the server to be silently skipped if set. [[lines 231-236](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/plugins-reference.md?plain=1#L231-L236)] [[Source](https://code.claude.com/docs/en/plugins-reference)]
* Documents that when multiple LSP servers claim the same file extension, the first registered wins, and a server that fails to initialize is skipped without blocking other valid servers on the same extension. [[lines 237-239](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/plugins-reference.md?plain=1#L237-L239)] [[Source](https://code.claude.com/docs/en/plugins-reference)]

#### [Continue local sessions from any device with Remote Control](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* `/model`, `/effort`, `/fast`, `/color`, and `/rename` now work from mobile/web with a value argument instead of being local-only. [[lines 230-232](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/remote-control.md?plain=1#L230-L232)] [[Source](https://code.claude.com/docs/en/remote-control)]

#### [Claude Code settings](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New managed-only setting `browserExternalPageTools` to disable Claude's tools on external pages in the Desktop Browser pane. [[line 207](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/settings.md?plain=1#L207)] [[Source](https://code.claude.com/docs/en/settings)]
* `disableBundledSkills` now documents that `/doctor` is exempt and stays typable, hidden only via `DISABLE_DOCTOR_COMMAND`. [[line 219](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/settings.md?plain=1#L219)] [[Source](https://code.claude.com/docs/en/settings)]

#### [Extend Claude with skills](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* `/doctor` is now listed as a bundled skill that stays typable even when `disableBundledSkills` is on. [[lines 12-13](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/skills.md?plain=1#L12-L13)] [[Source](https://code.claude.com/docs/en/skills)]
* Skill-description-overflow guidance updated: `/doctor` now gives an estimate/biggest-contributors view, and overflow warnings are also written to the debug log. [[lines 227-228](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/skills.md?plain=1#L227-L228)] [[Source](https://code.claude.com/docs/en/skills)]

#### [Customize your status line](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/statusline.md) [[Source](https://code.claude.com/docs/en/statusline)]

* `subagentStatusLine` task objects gain new `model` and `contextWindowSize` fields for rendering a per-row context-usage percentage. [[lines 1007-1008](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/statusline.md?plain=1#L1007-L1008)] [[Source](https://code.claude.com/docs/en/statusline)]

#### [Create custom subagents](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Clarifies duplicate subagent-name resolution: within one `.claude/agents/` directory the winner is filesystem read order; across nested project directories the closest-to-cwd definition wins; `/doctor` now proposes renaming or removing duplicates. [[line 148](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/sub-agents.md?plain=1#L148)] [[Source](https://code.claude.com/docs/en/sub-agents)]
* Resuming a stopped subagent via `SendMessage` now correctly shows it as "running" again instead of keeping a stale failed/completed status. [[line 773](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/sub-agents.md?plain=1#L773)] [[Source](https://code.claude.com/docs/en/sub-agents)]

#### [Troubleshoot installation and login](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/troubleshoot-install.md) [[Source](https://code.claude.com/docs/en/troubleshoot-install)]

* Notes that on FreeBSD the installer now correctly reports the platform as unsupported, instead of misdetecting it as Linux and downloading a binary that couldn't run. [[line 661](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/troubleshoot-install.md?plain=1#L661)] [[Source](https://code.claude.com/docs/en/troubleshoot-install)]

#### [Troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/troubleshooting.md) [[Source](https://code.claude.com/docs/en/troubleshooting)]

* `/doctor` guidance updated to reflect that it now proposes fixes you apply after confirmation, with MCP server status checks split out to `/mcp`. [[lines 17-106](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/troubleshooting.md?plain=1#L17-L106)] [[Source](https://code.claude.com/docs/en/troubleshooting)]

#### [Run parallel sessions with worktrees](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/worktrees.md) [[Source](https://code.claude.com/docs/en/worktrees)]

* If Claude Code can't enter a worktree directory at startup, it now prints an error and exits cleanly instead of crashing or stalling ~30s under `-p`. [[line 30](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/worktrees.md?plain=1#L30)] [[Source](https://code.claude.com/docs/en/worktrees)]
* On Windows, worktree removal now strips NTFS junctions/symlinks at any depth as link entries before deleting, fixing a bug where a nested junction could delete files outside the worktree. [[line 86](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/claude-code/worktrees.md?plain=1#L86)] [[Source](https://code.claude.com/docs/en/worktrees)]

### Minor edits (not itemized individually)

* `feature-availability.md`, `plugin-dependencies.md`, and `web-quickstart.md` picked up small consequences of the permission-mode rename and a "Cowork on 3P" → "Claude Desktop on 3P" product rename, with no new information beyond what's covered above.
* `permissions.md`, `platforms.md`, `vs-code.md`, `llm-gateway-rollout.md`, and `sandboxing.md` had only cosmetic tweaks (wording/link touch-ups).

-----

## API changes

### Changed documents

#### [Tool Runner (SDK)](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/agents-and-tools/tool-use/tool-runner.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner)]

* Clarified the runner only appends the assistant message and tool results, and continues, when the response actually contains tool calls; with no tool calls, the loop just exits. [[line 173](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/agents-and-tools/tool-use/tool-runner.md?plain=1#L173)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner)]
* The linked "Parallel tool use" guide now also covers disabling parallel tool calls, not just enabling/formatting them. [[line 474](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/agents-and-tools/tool-use/tool-runner.md?plain=1#L474)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner)]

#### [Agents](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/api/cli/beta/agents.md), [Sessions](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/api/cli/beta/sessions.md) [[Source](https://platform.claude.com/docs/en/api/cli/beta/agents)]

* Custom tool `description` limit raised from 1024 to 4096 characters (also reflected across the C#, Ruby, PHP, Go, and TypeScript reference pages). [[line 1153](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/api/cli/beta/agents.md?plain=1#L1153)] [[line 483](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/api/cli/beta/sessions.md?plain=1#L483)] [[Source](https://platform.claude.com/docs/en/api/cli/beta/agents)]

#### [Beta](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/api/cli/beta.md), [Webhooks](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/api/cli/beta/webhooks.md) [[Source](https://platform.claude.com/docs/en/api/cli/beta/webhooks)]

* Removed the `environment.*` and `memory_store.*` webhook event types and their event-data schemas entirely, dropping the documented event-data union from 40 variants to 33 (also removed from the language-specific webhook reference pages). [[line 944](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/api/cli/beta.md?plain=1#L944)] [[line 250](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/api/cli/beta/webhooks.md?plain=1#L250)] [[Source](https://platform.claude.com/docs/en/api/cli/beta)]

#### [Work](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/api/cli/beta/environments/work.md), [Acknowledge Work](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/api/cli/beta/environments/work/ack.md), [List Work Items](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/api/cli/beta/environments/work/list.md), [Poll for Work](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/api/cli/beta/environments/work/poll.md), [Get Work Item](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/api/cli/beta/environments/work/retrieve.md), [Stop Work](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/api/cli/beta/environments/work/stop.md), [Update Work Item](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/api/cli/beta/environments/work/update.md) [[Source](https://platform.claude.com/docs/en/api/cli/beta/environments/work)]

* Removed the `secret` field (the credential payload for self-hosted workers) from the `BetaSelfHostedWork` schema across every work endpoint, including polling (also removed from the C#, Ruby, and PHP reference pages). [[line 63](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/api/cli/beta/environments/work.md?plain=1#L63)] [[Source](https://platform.claude.com/docs/en/api/cli/beta/environments/work)]

#### [Create Skill](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/api/cli/beta/skills/create.md), [Create Skill Version](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/api/cli/beta/skills/versions/create.md) [[Source](https://platform.claude.com/docs/en/api/cli/beta/skills/create)]

* `--file` / `file` is now a required parameter instead of optional when creating a skill or a skill version (also reflected across the C#, Ruby, PHP, and TypeScript reference pages). [[line 21](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/api/cli/beta/skills/create.md?plain=1#L21)] [[line 29](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/api/cli/beta/skills/versions/create.md?plain=1#L29)] [[Source](https://platform.claude.com/docs/en/api/cli/beta/skills/create)]

#### [List memories](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/api/cli/beta/memory_stores/memories/list.md) [[Source](https://platform.claude.com/docs/en/api/cli/beta/memory_stores/memories/list)]

* Documented real semantics for `depth` (0/omitted = whole subtree, 1 = immediate children only), `limit` (1-100, default 20, capped at 20 for `view=full`), `page` (opaque cursor), and `path_prefix` (must end with `/`, segment-aligned) — previously placeholder text. [[lines 23-39](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/api/cli/beta/memory_stores/memories/list.md?plain=1#L23-L39)] [[Source](https://platform.claude.com/docs/en/api/cli/beta/memory_stores/memories/list)]
* Removed the `order` and `order_by` query parameters entirely — results are now returned in a stable, server-defined order instead. [[lines 22-39](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/api/cli/beta/memory_stores/memories/list.md?plain=1#L22-L39)] [[Source](https://platform.claude.com/docs/en/api/cli/beta/memory_stores/memories/list)]

#### [Memory](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/memory.md) [[Source](https://platform.claude.com/docs/en/managed-agents/memory)]

* Memory store endpoints now require a dedicated `agent-memory-2026-07-22` beta header instead of `managed-agents-2026-04-01` — sending both on the same request returns a `400` error; session endpoints (including attaching a memory store to a session) keep using `managed-agents-2026-04-01`. [[lines 11-15](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/memory.md?plain=1#L11-L15)] [[Source](https://platform.claude.com/docs/en/managed-agents/memory)]
* On July 22, 2026, `managed-agents-2026-04-01` adopts the same list behavior on `GET /v1/memory_stores/{id}/memories`; page cursors from requests made without a header aren't valid once that behavior is opted into. [[line 17](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/memory.md?plain=1#L17)] [[Source](https://platform.claude.com/docs/en/managed-agents/memory)]
* `path_prefix` must end with `/` and match whole path segments; `depth` accepts only `0` (whole subtree) or `1` (immediate children), returning `400` otherwise; results come back in a stable, server-defined order. [[lines 112-114](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/memory.md?plain=1#L112-L114)] [[Source](https://platform.claude.com/docs/en/managed-agents/memory)]

#### [Define outcomes](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/define-outcomes.md) [[Source](https://platform.claude.com/docs/en/managed-agents/define-outcomes)]

* Same memory-store beta-header split documented here. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/define-outcomes.md?plain=1#L15)] [[Source](https://platform.claude.com/docs/en/managed-agents/define-outcomes)]
* `span.outcome_evaluation_ongoing` events now include an `iteration` field. [[line 155](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/define-outcomes.md?plain=1#L155)] [[Source](https://platform.claude.com/docs/en/managed-agents/define-outcomes)]
* `max_iterations_reached` now triggers one final acknowledgment turn before the session goes idle, instead of ending evaluation immediately. [[line 186](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/define-outcomes.md?plain=1#L186)] [[Source](https://platform.claude.com/docs/en/managed-agents/define-outcomes)]
* New "Next steps" section linking to Vaults, Events and streaming, and Adding files. [[line 252](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/define-outcomes.md?plain=1#L252)] [[Source](https://platform.claude.com/docs/en/managed-agents/define-outcomes)]

#### [Self-hosted sandboxes](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/self-hosted-sandboxes.md), [Tools](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/tools.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

* New "Serve custom tools from your sandbox" section: the SDK worker can implement a custom tool itself, so the tool call reaches only the credentials and network the sandbox is configured with, and the Claude API key never touches the worker host. [[line 318](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L318)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]
* New "Wrap an MCP server as custom tools" guide: expose an internal-network-only MCP server to the agent, with no inbound connectivity or tunnel required, by having the worker act as the MCP client and forward calls. [[line 388](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L388)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

#### [Agent setup](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/agent-setup.md), [Cloud sandboxes reference](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/cloud-sandboxes-reference.md), [Environments](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/environments.md), [Events and streaming](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/events-and-streaming.md), [Files](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/files.md), [GitHub](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/github.md), [MCP connector](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/mcp-connector.md), [Multi-agent systems](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/multi-agent.md), [Onboarding](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/onboarding.md), [Permission policies](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/permission-policies.md), [Quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/quickstart.md), [Reference](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/reference.md), [Session operations](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/session-operations.md), [Sessions](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/sessions.md), [Skills](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/skills.md), [Vaults](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/vaults.md) [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup)]

* All now note that memory store endpoints require the new `agent-memory-2026-07-22` beta header instead of `managed-agents-2026-04-01`, linking to the Beta headers page. [[line 13](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/managed-agents/agent-setup.md?plain=1#L13)] [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup)]

#### [Admin API](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/manage-claude/admin-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api)]

* Documents the new `expires_at` field on Admin API key list/retrieve responses, and recommends auditing it alongside key rotation. [[line 189](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/manage-claude/admin-api.md?plain=1#L189)] [[line 278](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/manage-claude/admin-api.md?plain=1#L278)] [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api)]

#### [Admin API keys](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/manage-claude/admin-api-keys.md) [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api-keys)]

* Key-creation walkthrough now includes choosing an expiration for Console-issued Admin API keys. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/manage-claude/admin-api-keys.md?plain=1#L36)] [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api-keys)]

#### [API and data retention](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/manage-claude/api-and-data-retention.md) [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

* Clarifies this page covers the Claude API and Claude Platform on AWS (Anthropic as data processor); Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry are covered by their own cloud provider as data processor instead. [[line 7](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/manage-claude/api-and-data-retention.md?plain=1#L7)] [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]
* New ZDR detail: Claude Code's metrics-logging productivity data is exempt from Zero Data Retention and may still be retained even when ZDR is enabled; Claude Platform on AWS follows the same retention policy as the first-party API but ZDR there must be requested through an Anthropic account rep. [[lines 28-29](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/manage-claude/api-and-data-retention.md?plain=1#L28-L29)] [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]
* Notes Claude for Excel isn't ZDR-eligible yet, and that ZDR organizations can't use CORS — browser-based apps need a backend proxy instead. [[lines 37-40](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/manage-claude/api-and-data-retention.md?plain=1#L37-L40)] [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

#### [Authentication](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/manage-claude/authentication.md) [[Source](https://platform.claude.com/docs/en/manage-claude/authentication)]

* New "Key expiration" feature: keys can be created with a preset (3 hours/1 day/7 days/30 days), a custom duration, or Never, subject to org-level maximum-expiration policies. [[lines 44-46](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/manage-claude/authentication.md?plain=1#L44-L46)] [[Source](https://platform.claude.com/docs/en/manage-claude/authentication)]
* Expiring keys trigger warning emails to the creator: 7 days before expiry for keys with a lifetime of 14+ days, 1 day before for 7+ day keys; shorter-lived keys get no warning. [[line 48](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/manage-claude/authentication.md?plain=1#L48)] [[Source](https://platform.claude.com/docs/en/manage-claude/authentication)]
* After expiration, requests return `401 authentication_error` and the key can't be reactivated — a new key must be created; the Console keys table and Admin API now expose each key's `expires_at`. [[lines 50-52](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/manage-claude/authentication.md?plain=1#L50-L52)] [[Source](https://platform.claude.com/docs/en/manage-claude/authentication)]

#### [CMEK](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/manage-claude/cmek.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

* CMEK can now be combined with Zero Data Retention on both Claude Platform and Claude Enterprise, replacing the previous requirement to disable ZDR (or enable 30-day per-workspace retention) before attaching a customer-managed key. [[line 33](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/manage-claude/cmek.md?plain=1#L33)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

#### [Claude on Amazon Bedrock (legacy)](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/build-with-claude/claude-on-amazon-bedrock-legacy.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)]

* AWS now requires newer Claude models to be called through cross-region inference profiles; requests using the base model ID get an HTTP 400, and the doc now explains how to construct the inference-profile ID/ARN instead. [[lines 92-100](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/build-with-claude/claude-on-amazon-bedrock-legacy.md?plain=1#L92-L100)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)]

#### [Claude Platform on AWS](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/build-with-claude/claude-platform-on-aws.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)]

* The model ID comparison table now describes Bedrock's `us.`/`global.` prefix as a required "inference profile prefix" rather than optional, matching the new cross-region inference requirement. [[line 555](https://github.com/gpambrozio/ClaudeDocs/blob/f87a418157a1ef4630c5b8d24d1b1e94a932aaef/docs-md/api/build-with-claude/claude-platform-on-aws.md?plain=1#L555)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)]

### Minor edits (not itemized individually)

* Roughly 230 per-language SDK reference pages under `api/api/csharp/beta/**`, `api/api/ruby/beta/**`, `api/api/php/beta/**`, `api/api/go/beta/**`, and `api/api/typescript/beta/**` mirror the tool-description-length increase, the `secret`-field removal from self-hosted work items, the new `agent-memory-2026-07-22` beta header, and/or the removed webhook event types described above for the equivalent `cli/beta` pages.
* `adaptive-thinking.md`, `extended-thinking.md`, and `build-with-claude/files.md` only had their obfuscated email-protection hashes regenerated (same visible mailto links).
