# [Claude docs changes for October 22nd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/e2830f8253934d14af63759b61abd94343dca74b) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/e2830f8253934d14af63759b61abd94343dca74b)]

## Executive Summary
- New Claude API version `2026-10-21` with a full migration guide. It removes `temperature`, `top_p` and `top_k` on every model, rejects `document` blocks in assistant messages and `citations` in user messages, and renames several Admin and Analytics API fields. It ships with new major SDK versions (Python 2.0.0, TypeScript 1.0.0, Go v2, Java 3.0.0, and others) and `ant` CLI 2.0.0.
- Claude Code 2.1.307 adds `/claude-api api-version` to move API code to the new version. It also adds the `claude_code.safety_event` OpenTelemetry event and retries unparseable tool calls up to twice.
- New sandbox setting `sandbox.allowNestedUserNamespaces` lets Chromium, Electron and rootless Podman run inside the Linux/WSL2 sandbox. The docs warn that it turns off a security boundary.
- The docs say more about managed-settings controls. `strictPluginOnlyCustomization` and `strictKnownMarketplaces` now block skills-directory plugins, and `rm`/`rmdir` critical-path protection is described as covering only commands Claude Code recognizes.
- Scheduled tasks gain custom cron intervals, loop-stop behavior and resume semantics. A new keybinding (`select:cancel`) cancels a question with one key press.

## New Claude Code versions

### [2.1.307](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/versions/2.1.307.md)

#### New features

* Added `/claude-api api-version` to move Claude API code to API version `2026-10-21`
* Added the `claude_code.safety_event` OpenTelemetry event for each tool call that a permission rule, auto mode, a safety check, a hook or the sandbox stopped, prompted or sent back
* [Code Review] Added `@claude review stop` (also `off` and `pause`), which ends an `@claude review always` subscription on a pull request
* [VSCode] Added a notice on the microphone button when voice dictation stops by itself, saying why and that the text so far is kept

#### Existing feature improvements

* Claude Code now retries unparseable tool calls up to twice before ending the turn with an error
* Fork subagents launched together are now told which launch is their own, so they are much less likely to start each other's work
* Browser sign-in shows the success page as soon as sign-in completes
* Web search errors in cloud and self-hosted runner sessions now show the reason when a 403 gives one
* Faster first reply in cloud sessions when one of the desktop app's MCP servers can't connect
* Faster Remote Control connection for sessions with large pasted images or PDF reads
* The `axScreenReader` setting and `CLAUDE_AX_SCREEN_READER` in a settings `env` block now apply only from user, managed or `--settings` settings
* Self-hosted runner: checkout hooks are stopped after 30 minutes by default (`--checkout-hook-timeout-min`, `0` to disable)
* Self-hosted runner: the certificate file built for Anthropic-managed git filters its trusted certificates as the CLI does
* [VSCode] Dictation and the extension's own requests filter trusted certificates as the CLI does, and trust the `NODE_EXTRA_CA_CERTS` file from the environment or user settings

#### Major bug fixes

* Fixed model-not-found errors when `CLAUDE_CODE_DISABLE_1M_CONTEXT` is set and the model is an alias with the `[1m]` suffix
* Fixed MCP problems: "needs authentication" in `claude -p` on macOS with a locked keychain, false timeouts after sleep, and HTTP MCP tool calls sent twice when the connection closed mid-call (only read-only or idempotent tools are now retried)
* Fixed some "Autocompact is thrashing" errors in turns that read many PDF pages, images or other large tool results
* Fixed `/autocompact` and `/clear` state being lost when cloud or self-hosted runner sessions restarted
* Fixed `/permissions` > Recently denied not showing the denied shell command
* Fixed model switches through the Agent SDK's `setModel()` being refused when the API took more than 5 seconds to confirm; the wait is now up to 15 seconds
* Self-hosted runner: fixed checkout hooks leaving processes running and the runner's slot held when a session was archived, requeued or stopped

### [2.1.308](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/versions/2.1.308.md)

#### Major bug fixes

* Bug fixes and reliability improvements

-----

## Claude Code changes

### Changed documents

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New error entries for `API Error: Stream idle timeout - no chunks received` and `The model's tool call could not be parsed (retry also failed).` [[lines 24-33](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/errors.md?plain=1#L24-L33)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]
* Automatic retries now cover a response that announces a tool call but contains none; Claude Code retries up to two times. [[line 445](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/errors.md?plain=1#L445)] [[Source](https://code.claude.com/docs/en/errors#automatic-retries)]
* A "Prompt is too long" error behind a custom `ANTHROPIC_BASE_URL` is fixed by setting the model's context window or updating to v2.1.299+. On v2.1.305 with many MCP tools, the error can hide an unrelated 400/422, which v2.1.306+ fixes. [[lines 2216-2218](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/errors.md?plain=1#L2216-L2218)] [[Source](https://code.claude.com/docs/en/errors#prompt-is-too-long)]
* New section "Managed settings need your approval" for `claude plugin` commands that can't show the approval dialog. [[lines 5469-5480](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/errors.md?plain=1#L5469-L5480)] [[Source](https://code.claude.com/docs/en/errors#managed-settings-need-your-approval)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* New "Limits on skill hooks" section. Skill frontmatter hooks may not fire because of a plugin-only lock (`strictPluginOnlyCustomization`) or the v2.1.304+ per-source limits (1,024 hooks, 16,384 matcher characters). It explains how to diagnose with `claude --debug` and fix. [[lines 680-695](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/hooks.md?plain=1#L680-L695)] [[Source](https://code.claude.com/docs/en/hooks#limits-on-skill-hooks)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* New "Cancel a question in vim mode" section: press `Esc` twice in the `Other` row, or bind a single key. [[lines 261-266](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/interactive-mode.md?plain=1#L261-L266)] [[Source](https://code.claude.com/docs/en/interactive-mode#cancel-a-question-in-vim-mode)]
* New "Background a session with messages queued" section: queued messages move with the session, but commands, `!` shell commands and messages with an IDE selection can't. [[lines 398-406](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/interactive-mode.md?plain=1#L398-L406)] [[Source](https://code.claude.com/docs/en/interactive-mode#background-a-session-with-messages-queued)]

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* New "Cancel a question with one key press" section showing how to bind a Ctrl/Alt key to `select:cancel` in the `Select` context. [[lines 688-708](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/keybindings.md?plain=1#L688-L708)] [[Source](https://code.claude.com/docs/en/keybindings#cancel-a-question-with-one-key-press)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Reconnect behavior in `claude -p` and Agent SDK sessions is split: transient errors keep retrying for about half an hour, while a server that needs sign-in again stops retrying and reports `needs-auth`. [[lines 372-374](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/mcp.md?plain=1#L372-L374)] [[Source](https://code.claude.com/docs/en/mcp#mid-session-drops-of-a-remote-server)]
* New section on signing in to an MCP server behind a gateway that requires a header (v2.1.299+): configured `headers` or `headersHelper` are sent on sign-in, refresh and revocation requests, except `Authorization`. [[lines 1046-1057](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/mcp.md?plain=1#L1046-L1057)] [[Source](https://code.claude.com/docs/en/mcp#sign-in-to-an-mcp-server-behind-a-gateway-that-requires-a-header)]
* New "Read a background command's output as an MCP client" section covering `backgroundOutputPath` from `claude mcp serve`, including how to detect completion and read the tail of the file (v2.1.295+). [[lines 1281-1294](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/mcp.md?plain=1#L1281-L1294)] [[Source](https://code.claude.com/docs/en/mcp#read-a-background-commands-output-as-an-mcp-client)]

#### [memory](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Path-scoped rule patterns are relative to the rule's base directory (the project's `.claude` parent, or the primary working directory for user-level rules). For rules in a sibling worktree, start in that worktree or use `/cd`. [[lines 207-213](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/memory.md?plain=1#L207-L213)] [[Source](https://code.claude.com/docs/en/memory#path-specific-rules)]
* A managed CLAUDE.md can't be excluded with `claudeMdExcludes`. [[lines 285-345](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/memory.md?plain=1#L285-L345)] [[Source](https://code.claude.com/docs/en/memory#deploy-organization-wide-claudemd)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* The critical-path `rm`/`rmdir` protection is reworded to cover only removals Claude Code recognizes. A warning says a missed command gets no special handling and can be approved by allow rules, `bypassPermissions` or sandbox auto-allow. It lists mitigations: deny rules, sandboxing and strict sandbox mode. [[lines 772-786](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/permission-modes.md?plain=1#L772-L786)] [[Source](https://code.claude.com/docs/en/permission-modes#critical-paths)]
* New troubleshooting entry: `claude agents` shows the bypass permissions warning when `skipDangerousModePermissionPrompt` is set in local settings or a `--settings` file. [[lines 712-715](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/permission-modes.md?plain=1#L712-L715)] [[Source](https://code.claude.com/docs/en/permission-modes#claude-agents-shows-the-bypass-permissions-warning-that-interactive-sessions-skip)]

#### [plugins/loading](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/plugins/loading.md) [[Source](https://code.claude.com/docs/en/plugins/loading)]

* New section "Skills-directory plugins blocked by managed settings": `strictPluginOnlyCustomization` (any locked kind) or a `strictKnownMarketplaces`/`blockedMarketplaces` list without or with `skills-dir` silently skips plugin folders in `~/.claude/skills/` and `.claude/skills/`. [[lines 82-105](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/plugins/loading.md?plain=1#L82-L105)] [[Source](https://code.claude.com/docs/en/plugins/loading#check-why-a-repository-plugin-didnt-load)]
* Repository-plugin checks are reorganized into a "Check why a repository plugin didn't load" section. [[lines 70-82](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/plugins/loading.md?plain=1#L70-L82)] [[Source](https://code.claude.com/docs/en/plugins/loading#trust-check-and-component-limits-for-repository-plugins)]
* Clarified sync timing in cloud Cowork sessions and for plugins toggled on claude.ai during a terminal session. [[lines 118-126](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/plugins/loading.md?plain=1#L118-L126)] [[Source](https://code.claude.com/docs/en/plugins/loading#sync-timing-in-cloud-cowork-sessions)]

#### [plugins/mods/troubleshoot](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/plugins/mods/troubleshoot.md) [[Source](https://code.claude.com/docs/en/plugins/mods/troubleshoot)]

* After a load error ending in "the version loaded before is unloaded", run `/reload-plugins` once fixed. [[line 87](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/plugins/mods/troubleshoot.md?plain=1#L87)] [[Source](https://code.claude.com/docs/en/plugins/mods/troubleshoot#hooks-module-did-not-load)]
* New entry for "the parser stopped" / "the engine ran out of stack loading the file" errors caused by deeply nested hooks-module code. [[lines 101-109](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/plugins/mods/troubleshoot.md?plain=1#L101-L109)] [[Source](https://code.claude.com/docs/en/plugins/mods/troubleshoot#the-parser-stopped-or-the-engine-ran-out-of-stack-loading-the-file)]

#### [prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/prompt-caching.md) [[Source](https://code.claude.com/docs/en/prompt-caching)]

* Compaction caching is detailed layer by layer: the system prompt layer is read from cache (rebuilt once for old resumed conversations), and the project context layer is read from cache only if CLAUDE.md and memory are unchanged. [[lines 170-177](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/prompt-caching.md?plain=1#L170-L177)] [[Source](https://code.claude.com/docs/en/prompt-caching#compacting-the-conversation)]

#### [routines](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)]

* Enterprise organizations with custom roles need a role that includes the scheduled tasks permission. [[lines 32-33](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/routines.md?plain=1#L32-L33)] [[Source](https://code.claude.com/docs/en/routines#automate-work-with-scheduled-tasks)]
* Scheduled tasks run autonomously without a permission mode. [[line 49](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/routines.md?plain=1#L49)] [[Source](https://code.claude.com/docs/en/routines#create-a-scheduled-task)]
* Custom cron intervals can be set from the edit dialog. One-off tasks turn themselves off and show **Completed** after running. [[lines 149-160](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/routines.md?plain=1#L149-L160)] [[Source](https://code.claude.com/docs/en/routines#add-a-schedule-trigger)]
* A scheduled task with one repository can declare MCP servers in a committed `.mcp.json`. [[line 355](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/routines.md?plain=1#L355)] [[Source](https://code.claude.com/docs/en/routines#connectors)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* New troubleshooting section "Chromium or rootless Podman fails inside the sandbox on Linux". It covers `--no-sandbox`, `excludedCommands`, and the new `sandbox.allowNestedUserNamespaces` setting, with a warning that it removes a security boundary. [[lines 840-861](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/sandboxing.md?plain=1#L840-L861)] [[Source](https://code.claude.com/docs/en/sandboxing#chromium-or-rootless-podman-fails-inside-the-sandbox-on-linux)]
* When managed settings configure `sandbox.filesystem` or deny-mode `credentials.files`, only managed settings can set `filesystem.disabled`. [[lines 362-362](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/sandboxing.md?plain=1#L362)] [[Source](https://code.claude.com/docs/en/sandboxing#which-settings-can-disable-it)]
* Protected paths stay protected despite `allowWrite` or `Edit` allow rules. Only `filesystem.disabled` turns them off. [[lines 541-548](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/sandboxing.md?plain=1#L541-L548)] [[Source](https://code.claude.com/docs/en/sandboxing#protected-paths)]

#### [scheduled-tasks](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/scheduled-tasks)]

* Comparison table gains customizable schedule and minimum interval rows. [[lines 29-30](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/scheduled-tasks.md?plain=1#L29-L30)] [[Source](https://code.claude.com/docs/en/scheduled-tasks#compare-scheduling-options)]
* How to stop loops: `Esc` or `Ctrl+C` for self-paced loops, but ask Claude to cancel fixed-interval loops. Pressing `Ctrl+C` twice detaches from a background session without stopping a self-paced loop. [[lines 123-131](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/scheduled-tasks.md?plain=1#L123-L131)] [[Source](https://code.claude.com/docs/en/scheduled-tasks#stop-a-loop)]
* Resume semantics: `--resume`/`--continue` restore `CronCreate` tasks without replaying missed runs, and background Bash commands and monitors aren't restarted. [[lines 234-238](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/scheduled-tasks.md?plain=1#L234-L238)] [[Source](https://code.claude.com/docs/en/scheduled-tasks#limitations)]

#### [self-hosted-environments-deploy](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/self-hosted-environments-deploy.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy)]

* New troubleshooting entry for `no longer exists on the remote` / `couldn't find remote ref`, with causes (deleted branch, checkout hook, git host rewrite, runner older than v2.1.301). [[lines 670-680](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L670-L680)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#troubleshooting)]
* The runner's clone and fetches check Anthropic-managed git against a per-session certificate file. [[line 300](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L300)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#trust-a-private-certificate-authority-with-anthropic-managed-git)]

#### [server-managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* Sandbox network and isolation settings are added to the settings that need security approval. [[line 250](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/server-managed-settings.md?plain=1#L250)] [[Source](https://code.claude.com/docs/en/server-managed-settings#security-approval-dialogs)]
* `claude plugin` commands that can't read the keyboard don't apply delivered settings without cached settings. [[lines 281-283](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/server-managed-settings.md?plain=1#L281-L283)] [[Source](https://code.claude.com/docs/en/server-managed-settings#approval-memory)]
* Delivered `env` variables for context window and compaction apply without approval, except `CLAUDE_CODE_DISABLE_1M_CONTEXT`. Proxy/base-URL variables, `OTEL_EXPORTER_OTLP_ENDPOINT` and `CLAUDE_CODE_DISABLE_1M_CONTEXT` always need approval in interactive sessions. [[lines 293-304](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/server-managed-settings.md?plain=1#L293-L304)] [[Source](https://code.claude.com/docs/en/server-managed-settings#environment-variables-and-the-approval-dialog)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* New `sandbox.allowNestedUserNamespaces` setting (Boolean, default `false`, user or managed scope only). [[lines 1594-1616](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/settings-reference.md?plain=1#L1594-L1616)] [[Source](https://code.claude.com/docs/en/settings-reference#sandboxallownestedusernamespaces)]
* New `{ "source": "skills-dir" }` marketplace source. Any `strictKnownMarketplaces` allowlist, even an empty one, stops `@skills-dir` plugins loading unless it is included. [[lines 3904-3918](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/settings-reference.md?plain=1#L3904-L3918)] [[Source](https://code.claude.com/docs/en/settings-reference#allowed-source-types)]
* Locking any `strictPluginOnlyCustomization` surface also stops skills-directory plugins from loading. [[lines 4024-4026](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/settings-reference.md?plain=1#L4024-L4026)] [[Source](https://code.claude.com/docs/en/settings-reference#strictpluginonlycustomization)]

#### [fullscreen](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/fullscreen.md) [[Source](https://code.claude.com/docs/en/fullscreen)]

* A `--chrome` or `--no-chrome` launch flag is carried into the relaunched fullscreen session. [[line 31](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/claude-code/fullscreen.md?plain=1#L31)] [[Source](https://code.claude.com/docs/en/fullscreen#enable-fullscreen-rendering)]

-----

## API changes

### New Documents

#### [api/migration-2026-10-21](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/api/api/migration-2026-10-21.md) [[Source](https://platform.claude.com/docs/en/api/migration-2026-10-21)]

Guide for moving from API version `2023-06-01` to `2026-10-21`. It lists the minimum SDK versions (Python 2.0.0, TypeScript 1.0.0, C# 13.0.0, Go v2 with a new `/v2` module path, Java 3.0.0, PHP 1.0.0, Ruby 2.0.0, `ant` CLI 2.0.0) and how to send the `anthropic-version` header with cURL. It notes that on Amazon Bedrock the new version is only available for Claude 4.7 and later models. Breaking changes covered:

* Messages API: `document` blocks in assistant messages and non-empty `citations` on user `text` blocks now return 400. `temperature`, `top_p` and `top_k` are removed on every model.
* Admin API and Claude Enterprise Analytics API: renamed response fields (see the versioning entry below).
* SDK-specific code changes.

### Changed documents

#### [about-claude/model-deprecations](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/api/about-claude/model-deprecations.md) [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]

* The deprecated-parameters table now lists `temperature`, `top_p` and `top_k` as removed in API version `2026-10-21` (400 on every model). Earlier versions reject them only on Claude 4.7+ and Claude Mythos Preview. [[lines 209-213](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/api/about-claude/model-deprecations.md?plain=1#L209-L213)] [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations#api-parameter-deprecations)]

#### [api/versioning](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/api/api/versioning.md) [[Source](https://platform.claude.com/docs/en/api/versioning)]

* Added `2026-10-21` to the version history, with platform availability and its breaking changes: the Messages API changes above and renamed Admin API fields (RBAC groups `roles` → `role_ids`, members `group_id` → `rbac_group_id`, roles `name` → `display_name`, rate-limit `group_type` → `group.type`, API keys `workspace_id` → `scope.workspace_id`). In the Analytics API, `actor.email` → `actor.email_address` and `summaries` → `data`. [[lines 25-52](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/api/api/versioning.md?plain=1#L25-L52)] [[Source](https://platform.claude.com/docs/en/api/versioning#version-history)]
* The older versions are no longer described as deprecated. [[line 25](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/api/api/versioning.md?plain=1#L25)] [[Source](https://platform.claude.com/docs/en/api/versioning#version-history)]

#### [get-started](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/api/get-started.md) [[Source](https://platform.claude.com/docs/en/get-started)]

* The Java SDK dependency version is bumped from 2.75.0 to 3.1.0. [[lines 429-454](https://github.com/gpambrozio/ClaudeDocs/blob/e2830f8253934d14af63759b61abd94343dca74b/docs-md/api/get-started.md?plain=1#L429-L454)] [[Source](https://platform.claude.com/docs/en/get-started#call-the-api)]

#### Many other API pages (SDK samples and wording only)

* Across most API guides, and the SDK pages for C#, Go, Java, PHP, Python, Ruby and TypeScript, code samples were updated for the new SDK major versions. For example, C# uses `new UserMessageParam { Content = ... }` and Ruby uses `Anthropic::Model::CLAUDE_*` constants. Example JSON output fences were relabeled, and the prose was lightly reworded. These are not listed individually.
