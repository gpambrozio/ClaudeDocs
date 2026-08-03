# [Claude docs changes for August 3rd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/cc28a332b14c1dc82478bb1be009853c70551813) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/cc28a332b14c1dc82478bb1be009853c70551813)]

## Executive Summary
- New `DirectoryAdded` hook event fires when a working directory is added mid-session via `/add-dir` or the SDK's `register_repo_root` control request, letting hooks prepare newly added repositories.
- Fullscreen rendering is no longer purely opt-in: anyone who first used Claude Code on or after May 6, 2026 now gets it by default, with `/tui default` to switch back to the classic renderer.
- A new built-in `claude` subagent handles background sessions dispatched via `claude agents` or `claude --bg` when no agent is named.
- Bare mode (`claude --bare`) documentation now spells out that it skips OAuth and the system keychain entirely, so scripts must set `ANTHROPIC_API_KEY` (or `apiKeyHelper`) explicitly.
- Official plugin marketplace auto-registration behavior is clarified: it doesn't cover non-interactive environments or machines where an earlier policy blocked the marketplace, and the block isn't retried after the policy changes.

-----

## Claude Code changes

### Changed documents

#### [agent-loop](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/agent-sdk/agent-loop.md) [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop)]

* `permission_mode` docs now point to a new "How permissions are evaluated" section describing the fixed order modes and allow/deny rules are checked in. [[line 146](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/agent-sdk/agent-loop.md?plain=1#L146)] [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop#tool-permissions)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Clarifies that the desktop app doesn't save side chats to disk, so you can't reopen one after closing the app. [[line 300](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/desktop.md?plain=1#L300)] [[Source](https://code.claude.com/docs/en/desktop#ask-a-side-question-without-derailing-the-session)]

#### [discover-plugins](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* Auto-registration of the official marketplace now happens on first *interactive* start, and a blocked prior attempt due to marketplace policy is called out as another reason to add it manually. [[line 26](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/discover-plugins.md?plain=1#L26)] [[Source](https://code.claude.com/docs/en/discover-plugins#official-anthropic-marketplace)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL` is now documented as a one-time, permanent skip: Claude Code only checks it during first interactive launch, and unsetting it later doesn't undo the skip. [[line 218](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/env-vars.md?plain=1#L218)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [fullscreen](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/fullscreen.md) [[Source](https://code.claude.com/docs/en/fullscreen)]

* Fullscreen rendering is now the default renderer for anyone whose first Claude Code use was on or after May 6, 2026; earlier users keep the classic renderer unless they opt in with `/tui fullscreen`. [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/fullscreen.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/fullscreen)]

#### [headless](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* Documents `claude -p` exit codes: 0 on success, non-zero on failure, so scripts can branch on exit status. [[line 26](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/headless.md?plain=1#L26)] [[Source](https://code.claude.com/docs/en/headless#basic-usage)]
* Bare mode now explicitly requires setting `ANTHROPIC_API_KEY` since it doesn't use your subscription login, and it skips OAuth and the system keychain entirely. [[lines 32-38](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/headless.md?plain=1#L32-L38)] [[Source](https://code.claude.com/docs/en/headless#start-faster-with-bare-mode)]
* Added a `package.json` lint example run command and a `"$1"` argument-substitution explanation for the security-review script example. [[lines 89](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/headless.md?plain=1#L89), [242-250](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/headless.md?plain=1#L242-L250)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* New `DirectoryAdded` hook event: fires after a directory is added mid-session via `/add-dir` or the SDK's `register_repo_root` request, with `directory` and `source` input fields and no decision control. [[lines 2296-2327](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/hooks.md?plain=1#L2296-L2327)] [[Source](https://code.claude.com/docs/en/hooks#directoryadded)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Adds the new `DirectoryAdded` event to the lifecycle event table and spells out the `PreToolUse` input fields explicitly. [[line 448](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/hooks-guide.md?plain=1#L448)] [[Source](https://code.claude.com/docs/en/hooks-guide#how-hooks-work)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Renames the "default renderer" to the "classic renderer" throughout, reflecting fullscreen becoming the default for newer users.

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* Same "default renderer" → "classic renderer" terminology update for transcript and history-search keybindings.

#### [migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/agent-sdk/migration-guide.md) [[Source](https://code.claude.com/docs/en/agent-sdk/migration-guide)]

* Corrects the documentation-location note: Agent SDK docs live in the Claude Code docs under a dedicated section, not in the API Guide as previously stated. [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/agent-sdk/migration-guide.md?plain=1#L11)] [[Source](https://code.claude.com/docs/en/agent-sdk/migration-guide#what’s-changed)]

#### [plugin-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Expands on when official-marketplace auto-registration doesn't apply: non-interactive environments, and machines where an earlier blocked attempt (e.g. empty-array lockdown) isn't retried after the policy changes. Recommends pairing with `extraKnownMarketplaces` to cover those machines. [[lines 682-687](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/plugin-marketplaces.md?plain=1#L682-L687)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#common-configurations)]

#### [plugins](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/plugins.md) [[Source](https://code.claude.com/docs/en/plugins)]

* Notes that a marketplace-policy block, not just non-interactive timing, can prevent official marketplace auto-registration.

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* Adds `DirectoryAdded` to the plugin hooks lifecycle event table.

#### [quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/agent-sdk/quickstart.md) [[Source](https://code.claude.com/docs/en/agent-sdk/quickstart)]

* Permission modes description now links to the new "How permissions are evaluated" section covering the fixed evaluation order. [[line 326](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/agent-sdk/quickstart.md?plain=1#L326)] [[Source](https://code.claude.com/docs/en/agent-sdk/quickstart#key-concepts)]

#### [routines](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)]

* Clarifies the `/schedule` "Unknown command" troubleshooting: a Console API key now shows a dedicated "available with Claude for Enterprise" message instead of the generic unknown-command error. [[line 354](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/routines.md?plain=1#L354)] [[Source](https://code.claude.com/docs/en/routines#/schedule-returns-“unknown-command”)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Same official-marketplace auto-registration caveats (non-interactive environments, blocked-policy machines) added to the `strictKnownMarketplaces`/`extraKnownMarketplaces` reference. [[lines 996-1001](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/settings.md?plain=1#L996-L1001)] [[Source](https://code.claude.com/docs/en/settings#strictknownmarketplaces)]

#### [streaming-vs-single-mode](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/agent-sdk/streaming-vs-single-mode.md) [[Source](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode)]

* Drops the "(Default & Recommended)" label from the Streaming Input Mode summary bullet (the dedicated section heading still calls it recommended). [[lines 5-6](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/agent-sdk/streaming-vs-single-mode.md?plain=1#L5-L6)] [[Source](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode#overview)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Documents a new built-in `claude` subagent, used for background sessions dispatched via `claude agents` or `claude --bg` when no agent is named, and which Claude can also delegate to directly. [[line 59](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/sub-agents.md?plain=1#L59)] [[Source](https://code.claude.com/docs/en/sub-agents#built-in-subagents)]

#### [troubleshoot-install](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/troubleshoot-install.md) [[Source](https://code.claude.com/docs/en/troubleshoot-install)]

* Splits the connectivity-check command into separate macOS/Linux and Windows PowerShell tabs, and clarifies the expected success status line differs by platform (`HTTP/2 200` vs. `HTTP/1.1 200 OK`). [[lines 51-62](https://github.com/gpambrozio/ClaudeDocs/blob/cc28a332b14c1dc82478bb1be009853c70551813/docs-md/claude-code/troubleshoot-install.md?plain=1#L51-L62)] [[Source](https://code.claude.com/docs/en/troubleshoot-install#check-network-connectivity)]

-----

## API changes

No significant changes today — the only diffs were Cloudflare email-obfuscation hash refreshes in `files` and `thinking`.
