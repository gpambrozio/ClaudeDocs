# [Claude docs changes for October 6th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/93cce2ce988a39621a5337739712d852a2b7667d) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/93cce2ce988a39621a5337739712d852a2b7667d)]

## Executive Summary
- Claude Code 2.1.290 is a large release: `claude attach`/`claude logs` accept session names, new `/claude-api managed-agents-onboard` commands, a refilling WebSearch budget, many permission and sandbox hardening fixes, and mod/plugin hook additions. 2.1.291 fixes two regressions (lost permission answers in cloud sessions, lost last messages on quit).
- Inference hooks gain a new `tool_call` event ("Validate tool calls"): your AI security server can now return one verdict on Claude's tool calls before any of them run, with `tool_info` describing who provides each tool.
- Agent SDK custom tools docs now cover optional parameters, `Annotated` descriptions and `TypedDict` schemas in Python, and a new `session_state_changed` message enabled with `CLAUDE_CODE_EMIT_SESSION_STATE_EVENTS=1`.
- The RBAC Roles API now returns `display_name` (with `name` deprecated), and the Agents API raises the tool limit from 128 to 256.
- Desktop app docs describe a reworked Browser pane and a `/code-review` card with "Walk through in diff" and "Apply fixes"; the legacy Claude in Slack page is now limited to Pro/Max workspaces not connected to Claude Tag.

## New Claude Code versions

### [2.1.290](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/versions/2.1.290.md)

#### New features

* `claude attach <name>` and `claude logs <name>`: part of a session name works in place of the id
* `/claude-api managed-agents-onboard <url>` sets up the Managed Agents pattern a page describes as `ant apply` files, and `/claude-api managed-agents-onboard <quickstart-name>` builds a Console quickstart template (such as `deep-researcher`) with the `ant` CLI
* Plugin hooks and mods: `serverToolUses` on `turn.step`, `agentId` on `tool.check`, `ceiling` on the `tool.check` question and verdict, `ThemeKey`/`Color` typings, and `claude plugin validate` now lists gating hooks and whether each has a `.catch` (`gatingHooks` under `--json`)
* Warnings when a managed settings file is a link to a file outside the managed settings folder, and in `/status` and doctor when managed settings ignore user-configured sandbox `allowRead` paths or allowed domains
* Claude apps gateway sign-in approval page has a Deny button
* [Claude Tag] Fast mode in Slack with `!fast` / `!fast off`, and an optional Path prefixes field for custom connections in an access bundle
* [VSCode] Manage plugins dialog can review and run a marketplace's install or update command; screen reader announcement when a message is queued

#### Existing feature improvements

* The interactive session's WebSearch budget now refills over time (100 calls/hour, set with `CLAUDE_CODE_WEB_SEARCH_REFILLS_PER_HOUR`) instead of ending after 200 calls
* WebFetch now reports how much text was unread past 100,000 characters and takes an `offset` to read on
* `/code-review` at medium effort also reports cleanup and CLAUDE.md convention findings on models without tuned review settings (including Opus 5.5 and Sonnet 5.5)
* `/model`, `/effort` and `/rename` sent from `claude agents` to a busy background session apply right away
* Background sessions waiting on a scheduled wakeup (`/loop`) are left running through updates and low memory
* Faster responsiveness while resuming large sessions; `/` and `@` suggestion lists show a ❯ pointer on the selected row
* `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` also skips the startup connection warm-up; Claude in Chrome `browser_batch` timeout raised to 90 seconds
* Security-related changes: project settings can no longer turn on Claude in Chrome or set `CLAUDE_CODE_DISABLE_ATTACHMENTS`; `pyright` and more `ps` forms now ask for permission; `!` shell commands with raw control characters are refused
* Claude apps gateway: minimum PostgreSQL version lowered from 14 to 11, certificate-expiry warnings, nicer sign-in pages
* Claude Tag channel instructions limit is now 8,192 characters instead of bytes
* [VSCode] Message timestamps are shown by default

#### Major bug fixes

* Fixed requests failing behind proxies/gateways that reject a Claude Code beta header with a status other than 400
* Fixed long sessions with hundreds of images getting stuck on "Request rejected as unprocessable by the model"
* Fixed scheduled tasks (`/loop`, reminders) not returning on resume after compaction, never firing after a hand-off to the background, and firing extra runs on resume/respawn/fork
* Fixed several permission bypasses: auto-approved read-only commands whose wildcards the shell would expand, zsh variable-name differences, deny/ask rules missed after `declare`/`export` prefixes or a PreToolUse hook input rewrite, Read deny rules not applying to pasted image paths, and symlink swaps during image/@-mention reads
* Fixed plan mode letting the auto mode classifier approve non-read-only connector tools with a server-pushed ask policy, and plan mode not being restored on `--continue`/`--resume`
* Fixed `/ultrareview` dropping or unfiltered-uploading uncommitted changes in several git configurations
* Fixed `claude --teleport` and `/teleport` deleting files when choosing to stash
* Fixed many agent view and `claude agents` issues (Esc confirming restarts, Ctrl+X deleting whole sections, undeliverable commands replayed on restart, replies refused after a crash)
* Fixed freezes and slowdowns: very long messages, secret scan/masking on long text, rewind menu with large pastes, transcript expansion with non-ASCII output
* Fixed unbounded memory use when an HTTP MCP server sends a very large response
* Fixed headless `--json-schema` runs exiting non-zero after the structured output was delivered

### [2.1.291](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/versions/2.1.291.md)

#### Major bug fixes

* Fixed a regression in 2.1.290 where cloud sessions could drop answers to permission prompts
* Fixed a regression in 2.1.288 where the last messages of a session could be lost when quitting

-----

## Claude Code changes

### New Documents

None.

### Changed documents

#### [agent-sdk/cost-tracking](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/agent-sdk/cost-tracking.md) [[Source](https://code.claude.com/docs/en/agent-sdk/cost-tracking)]

* Added an "estimates, not billing" anchor and a note that combined `total_cost_usd` figures are client-side estimates. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/agent-sdk/cost-tracking.md?plain=1#L9)] [[Source](https://code.claude.com/docs/en/agent-sdk/cost-tracking#track-cost-and-usage)]

#### [agent-sdk/custom-tools](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/agent-sdk/custom-tools.md) [[Source](https://code.claude.com/docs/en/agent-sdk/custom-tools)]

* New "Make a parameter optional" guidance: `.optional()` in Zod for TypeScript; JSON Schema form (omit from `required`, read with `args.get()`) for Python. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/agent-sdk/custom-tools.md?plain=1#L12)] [[Source](https://code.claude.com/docs/en/agent-sdk/custom-tools#quick-reference)]
* Input schema section is now per-language, with `.describe()` for Zod and `Annotated[type, "description"]` for Python field descriptions. [[lines 28-31](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/agent-sdk/custom-tools.md?plain=1#L28-L31)] [[Source](https://code.claude.com/docs/en/agent-sdk/custom-tools#create-a-custom-tool)]
* Added httpx install instructions (uv and pip) for Python examples that make HTTP requests. [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/agent-sdk/custom-tools.md?plain=1#L38)] [[Source](https://code.claude.com/docs/en/agent-sdk/custom-tools#create-a-custom-tool)]
* Run instructions now separate TypeScript, Python (uv) and Python (pip) commands. [[line 190](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/agent-sdk/custom-tools.md?plain=1#L190)] [[Source](https://code.claude.com/docs/en/agent-sdk/custom-tools#call-a-custom-tool)]
* The `get_precipitation_chance` example now uses a JSON Schema with `hours` left out of `required`. [[line 224](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/agent-sdk/custom-tools.md?plain=1#L224)] [[Source](https://code.claude.com/docs/en/agent-sdk/custom-tools#add-more-tools)]

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* Documented a third `tool()` schema form, a `TypedDict` class with `NotRequired` keys (with Python 3.10 `typing_extensions` note), and `Annotated` descriptions. [[lines 124-144](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/agent-sdk/python.md?plain=1#L124-L144)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#input-schema-options)]
* `SystemMessage` subtypes without their own dataclass: set `CLAUDE_CODE_EMIT_SESSION_STATE_EVENTS=1` and read `message.data["state"]`. [[line 1589](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/agent-sdk/python.md?plain=1#L1589)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#systemmessage)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* New `SDKSessionStateChangedMessage` (`session_state_changed`) with `running`, `idle` and `requires_action` states, enabled by `CLAUDE_CODE_EMIT_SESSION_STATE_EVENTS=1`. [[line 5344](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L5344)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdksessionstatechangedmessage)]

#### [agent-view](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* `claude attach` and `claude logs` accept part of a session name (v2.1.290+). [[lines 739-751](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/agent-view.md?plain=1#L739-L751)] [[Source](https://code.claude.com/docs/en/agent-view#manage-sessions-from-the-shell)]
* Session row example and icon-shape description updated (`✻` means running or needs your input); voice dictation reply works in hold mode. [[lines 111-136](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/agent-view.md?plain=1#L111-L136)] [[Source](https://code.claude.com/docs/en/agent-view#monitor-sessions-with-agent-view)]
* Added v2.1.290 entry to the version history table. [[line 972](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/agent-view.md?plain=1#L972)] [[Source](https://code.claude.com/docs/en/agent-view#version-history)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* `claude attach <id|name>` and `claude logs <id|name>` document name support. [[lines 25-32](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/cli-reference.md?plain=1#L25-L32)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-commands)]
* `--max-budget-usd` is checked against a client-side cost estimate that can differ from billing. [[line 99](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/cli-reference.md?plain=1#L99)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Browser pane controls reworked: Dev servers menu, Keep cookies, Clear browsing data, Browser tools toggle, and a first-click prompt for opening links in the built-in browser. [[lines 107-118](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/desktop.md?plain=1#L107-L118)] [[Source](https://code.claude.com/docs/en/desktop#preview-your-app)]
* Code review is now `/code-review` in the prompt box, with a Code review card offering "Walk through in diff", "Fix this one" and "Apply fixes". [[lines 156-163](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/desktop.md?plain=1#L156-L163)] [[Source](https://code.claude.com/docs/en/desktop#review-your-code)]
* CI options renamed "Auto-fix CI & address comments" and "Auto-merge when ready", opened via **CI** in the status bar. [[lines 169-172](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/desktop.md?plain=1#L169-L172)] [[Source](https://code.claude.com/docs/en/desktop#monitor-pull-request-status)]
* SSH connection dialog fields and menu path updated; the "Disable Bypass permissions mode" admin setting entry was removed. [[lines 657-664](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/desktop.md?plain=1#L657-L664)] [[Source](https://code.claude.com/docs/en/desktop#ssh-sessions)]

#### [desktop-changelog](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/desktop-changelog.md) [[Source](https://code.claude.com/docs/en/desktop-changelog)]

* Contains the same desktop updates as above (Browser pane, `/code-review` card, CI options, SSH dialog). [[lines 107-118](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/desktop-changelog.md?plain=1#L107-L118)] [[Source](https://code.claude.com/docs/en/desktop-changelog#preview-your-app)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_EMIT_SESSION_STATE_EVENTS` adds `session_state_changed` messages to the stream. [[line 270](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/env-vars.md?plain=1#L270)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `CLAUDE_CODE_GZIP_REQUEST_BODIES` (set `0` to disable gzip of API, telemetry and artifact publish bodies). [[line 298](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/env-vars.md?plain=1#L298)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* Beta tracing endpoint is now specified as an OTLP/HTTP endpoint. [[line 178](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/env-vars.md?plain=1#L178)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [feature-availability](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/feature-availability.md) [[Source](https://code.claude.com/docs/en/feature-availability)]

* Claude Code in Slack is listed as Pro and Max only. [[line 44](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/feature-availability.md?plain=1#L44)] [[Source](https://code.claude.com/docs/en/feature-availability#features-that-require-a-claude-subscription)]

#### [fullscreen](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/fullscreen.md) [[Source](https://code.claude.com/docs/en/fullscreen)]

* Clicking a file path on Linux/WSL needs a file manager providing `org.freedesktop.FileManager1`. [[line 98](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/fullscreen.md?plain=1#L98)] [[Source](https://code.claude.com/docs/en/fullscreen#use-the-mouse)]

#### [hipaa-setup](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/hipaa-setup.md) [[Source](https://code.claude.com/docs/en/hipaa-setup)]

* Versions older than v2.1.285 ignore `allowedProviders`; suggested `requiredMinimumVersion` as a workaround. [[line 149](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/hipaa-setup.md?plain=1#L149)] [[Source](https://code.claude.com/docs/en/hipaa-setup#sessions-the-managed-settings-keys-dont-block)]
* Session data removal: `claude purge` on v2.1.288+, `claude project purge` on v2.1.126-2.1.287. [[lines 233-247](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/hipaa-setup.md?plain=1#L233-L247)] [[Source](https://code.claude.com/docs/en/hipaa-setup#delete-session-data-right-away)]

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* `confirm:nextField` now documented as toggling fast mode in the `/fast` dialog; `confirm:previousField` and `permission:toggleDebug` are no-op actions that stay valid in `keybindings.json`. [[lines 142-181](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/keybindings.md?plain=1#L142-L181)] [[Source](https://code.claude.com/docs/en/keybindings#confirmation-actions)]

#### [memory](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Subdirectory CLAUDE.md files load on demand when Claude uses Read, Write and other file tools; a `Loaded` line appears and they don't show under **Memory files** in `/context`. [[lines 138-140](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/memory.md?plain=1#L138-L140)] [[Source](https://code.claude.com/docs/en/memory#how-claudemd-files-load)]
* The built-in AGENTS.md plugin ID is `cc-plugin-agents-md@builtin` (was `agents-md@builtin` before v2.1.285). [[lines 376-390](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/memory.md?plain=1#L376-L390)] [[Source](https://code.claude.com/docs/en/memory#choose-which-instruction-files-load)]
* Debugging tips for on-demand CLAUDE.md loading. [[line 564](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/memory.md?plain=1#L564)] [[Source](https://code.claude.com/docs/en/memory#claude-isnt-following-my-claudemd)]

#### [claude-md](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/claude-md.md) [[Source](https://code.claude.com/docs/en/claude-md)]

* Same on-demand loading and `cc-plugin-agents-md@builtin` plugin ID updates as in memory. [[lines 138-140](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/claude-md.md?plain=1#L138-L140)] [[Source](https://code.claude.com/docs/en/claude-md#how-claudemd-files-load)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Auto mode default-block list is merged into one list (no longer split at v2.1.200). [[lines 367-376](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/permission-modes.md?plain=1#L367-L376)] [[Source](https://code.claude.com/docs/en/permission-modes#what-the-classifier-blocks-by-default)]
* Protected directories: `.claude` exceptions now list worktrees, the session's plan files, background session scratch directories, and project/subagent memory markdown files. [[lines 626-632](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/permission-modes.md?plain=1#L626-L632)] [[Source](https://code.claude.com/docs/en/permission-modes#protected-paths)]

#### [plugins/mods/overview](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/plugins/mods/overview.md) [[Source](https://code.claude.com/docs/en/plugins/mods/overview)]

* Mods work in the Desktop app from v2.1.286 (terminal needs v2.1.287); added how to check the version in each. [[line 89](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/plugins/mods/overview.md?plain=1#L89)] [[Source](https://code.claude.com/docs/en/plugins/mods/overview#turn-mods-on-or-off)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* In cloud sessions Claude Code honors only a subset of `defaultMode` values; `@builtin` plugin config example updated to the new AGENTS.md plugin ID. [[lines 1631-1643](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/settings-reference.md?plain=1#L1631-L1643)] [[Source](https://code.claude.com/docs/en/settings-reference#permissionsdefaultmode)]

#### [slack](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/slack.md) [[Source](https://code.claude.com/docs/en/slack)]

* The earlier Claude in Slack now only answers Pro and Max accounts in workspaces not connected to Claude Tag; Team/Enterprise should use Claude Tag. [[lines 3-9](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/slack.md?plain=1#L3-L9)] [[Source](https://code.claude.com/docs/en/slack#claude-code-in-slack)]
* New troubleshooting entries for the "This workspace isn't set up for Claude Tag yet" and "legacy Claude in Slack bot is retired" notices. [[lines 166-190](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/claude-code/slack.md?plain=1#L166-L190)] [[Source](https://code.claude.com/docs/en/slack#troubleshooting)]

-----

## API changes

### New Documents

None.

### Changed documents

#### [api/beta/agents](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/api/api/beta/agents.md) [[Source](https://platform.claude.com/docs/en/api/beta/agents)]

* Maximum tools across all toolsets raised from 128 to 256 for Create and Update Agent (also mirrored in the per-language SDK reference pages and `beta.md`). [[line 418](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/api/api/beta/agents.md?plain=1#L418)] [[Source](https://platform.claude.com/docs/en/api/beta/agents#body-parameters)]

#### [api/beta/organization/rbac_roles](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/api/api/beta/organization/rbac_roles.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/rbac_roles)]

* RBAC roles now expose `display_name`; `name` is deprecated and always equals it. Anthropic-created role names may differ from claude.ai labels and can change, so store the role `id`. List and retrieve responses show `display_name`. (Mirrored in `beta/organization.md`, `rbac_roles/list.md`, `rbac_roles/retrieve.md` and the SDK reference pages.)

#### [manage-claude/inference-hooks](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/api/manage-claude/inference-hooks.md) [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks)]

* Two hook events now exist: `prompt` and `tool_call` (with **Validate tool calls** on). [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/api/manage-claude/inference-hooks.md?plain=1#L15)] [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks#inference-hooks)]
* `tool_call` events may omit some claude.ai-internal tools; Claude Tag measurement requests are not sent to your endpoint. [[lines 82-84](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/api/manage-claude/inference-hooks.md?plain=1#L82-L84)] [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks#availability)]

#### [manage-claude/inference-hooks-configuration](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/api/manage-claude/inference-hooks-configuration.md) [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-configuration)]

* New **Validate tool calls** setting (off by default, requires **Enforce verdicts**, takes about a minute to propagate). [[line 92](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/api/manage-claude/inference-hooks-configuration.md?plain=1#L92)] [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-configuration#set-up-inference-hooks)]

#### [manage-claude/inference-hooks-endpoint](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/api/manage-claude/inference-hooks-endpoint.md) [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-endpoint)]

* New "The tool call frame" section: `type` is `"tool_call"`, `messages` holds only the latest assistant message, one verdict covers all calls, and each `tool_use` block carries `tool_info`. [[line 241](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/api/manage-claude/inference-hooks-endpoint.md?plain=1#L241)] [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-endpoint#the-tool-call-frame)]
* `tool_info` kinds documented with fields and examples: `platform`, `application`, `third_party` (with `origin`/`verified_origin`) and `client`. [[lines 255-330](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/api/manage-claude/inference-hooks-endpoint.md?plain=1#L255-L330)] [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-endpoint#the-tool-call-frame)]
* Request field table: `type` is `"prompt"` or `"tool_call"`, and `request_id` is a per-frame identifier. [[lines 161-170](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/api/manage-claude/inference-hooks-endpoint.md?plain=1#L161-L170)] [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-endpoint#the-prompt-frame)]

#### [models/fable-5/introducing-claude-fable-5-and-claude-mythos-5](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/api/models/fable-5/introducing-claude-fable-5-and-claude-mythos-5.md) [[Source](https://platform.claude.com/docs/en/models/fable-5/introducing-claude-fable-5-and-claude-mythos-5)]

* Removed statements that Claude Mythos 5 lacks the safety classifiers Claude Fable 5 has (also in fable-5 `overview` and `migration-guide`). [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/api/models/fable-5/introducing-claude-fable-5-and-claude-mythos-5.md?plain=1#L15)] [[Source](https://platform.claude.com/docs/en/models/fable-5/introducing-claude-fable-5-and-claude-mythos-5#introducing-claude-fable-5-and-claude-mythos-5)]

#### [models/fable-5-1/overview](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/api/models/fable-5-1/overview.md) [[Source](https://platform.claude.com/docs/en/models/fable-5-1/overview)]

* Recommended starting model changed from Claude Opus 5 to Claude Opus 5.5 (also in `whats-new-fable-5-1`); the safety classifiers divergence bullet was dropped from the Fable 5.1 migration guide. [[line 21](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/api/models/fable-5-1/overview.md?plain=1#L21)] [[Source](https://platform.claude.com/docs/en/models/fable-5-1/overview#overview)]

#### [models/opus-5-5/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/api/models/opus-5-5/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide)]

* On Amazon Bedrock, structured outputs aren't available for Claude Opus 5.5: use system prompt instructions for prefill replacement, and `auto` alone instead of `any`/`tool` tool choice. [[lines 32-281](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/api/models/opus-5-5/migration-guide.md?plain=1#L32)] [[Source](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide#what-every-request-to-claude-opus-55-must-satisfy)]

#### [models/sonnet-5-5/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/api/models/sonnet-5-5/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide)]

* On Amazon Bedrock, structured outputs aren't available for Claude Sonnet 5.5; describe the format in the prompt or use a non-`strict` tool and validate in code. [[line 1200](https://github.com/gpambrozio/ClaudeDocs/blob/93cce2ce988a39621a5337739712d852a2b7667d/docs-md/api/models/sonnet-5-5/migration-guide.md?plain=1#L1200)] [[Source](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide#migrating-from-claude-sonnet-45-or-earlier)]
