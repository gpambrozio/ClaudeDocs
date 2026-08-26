# [Claude docs changes for August 26th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/8e83fab01bcdbabfc6b6359d1544ef834d097c88) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/8e83fab01bcdbabfc6b6359d1544ef834d097c88)]

## Executive Summary
- Claude Code 2.1.246 adds a startup warning for Bash allow rules whose wildcard sits before the subcommand (e.g. `Bash(git * main)`), since such rules can approve options like git's `-c` that run arbitrary commands, plus a new **Auto mode** tab in `/permissions` for editing classifier rules without hand-editing settings files.
- `/goal` idle check-ins are now capped at three per goal between prompts instead of running indefinitely, and `/code-review` can now start itself automatically on more platforms (Bedrock, Vertex AI, Foundry, the Claude apps gateway) since it now follows feature-flag availability instead of a hardcoded exception list.
- The permissions docs got a rewrite of Bash wildcard matching with a full table of examples, clarifying exactly where `*` can go and what it does and doesn't match.
- Anthropic split its single sprawling model migration guide into one page per model (Opus 5, Sonnet 5, Haiku 4.5, Fable 5/Mythos 5); the old combined page is now just an index linking to them.
- The Linux desktop app documents Cowork's virtualization requirements (KVM, QEMU, `/dev/kvm` access) and new troubleshooting for unmet dependencies and Cowork startup failures, and admins gained a `disableDesktopLocalSessions` managed setting to force developers onto SSH or cloud sessions.

## New Claude Code versions

### [2.1.246](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/versions/2.1.246.md)

#### New features

* Added a startup warning for Bash allow rules with a wildcard before the subcommand (e.g. `Bash(git * main)`), since they also match options inserted before the subcommand
* Added an Auto mode tab to `/permissions` for viewing and editing auto mode classifier rules
* Added the turn's completion time to the end-of-turn duration line, e.g. `✻ Sautéed for 23s · done 6:05 PM`

#### Existing feature improvements

* Improved `/cd`: the new directory's project settings, hooks, `.mcp.json` servers, skills, and agents now take effect right after the move instead of on `--resume`
* Improved Bash tool latency on bash shells by replaying snapshot functions without a base64 subshell per function
* Improved subagent results: a subagent that stops at its `maxTurns` limit now returns its output marked as partial, with a hint to continue it via `SendMessage`, instead of appearing finished
* Improved non-interactive sessions (`-p`, SDK, cloud sessions) to automatically continue a response cut off mid-stream by a server error, connection loss, or stall instead of ending with an error
* Improved attribution of usage telemetry to your organization for workload identity federation sessions and other edge cases
* Changed `/code-review` so Claude can also start it on its own on Bedrock, Vertex AI, and Foundry, through the Claude apps gateway, and when telemetry or non-essential traffic is disabled
* `/goal`: Changed idle sessions to start at most three check-ins on long-running background work per goal; your next message allows three more
* Changed `claude install` and `claude update` to defer a pending managed-settings consent prompt to the next interactive session instead of prompting mid-command
* Changed OpenTelemetry plugin events for plugins synced from claude.ai: `plugin_id_hash` now reflects the plugin's real marketplace, and `enabled_via` is `admin-install` for admin-installed plugins

#### Major bug fixes

* Fixed a severe transcript slowdown when a diff contained a very long single line (e.g. a base64 string); such lines now render truncated with a marker
* Fixed fullscreen mode showing a blank transcript after resizing the terminal, and erratic fullscreen scrolling including jump-to-bottom getting stuck mid-transcript
* Fixed background sessions failing to open after 45 seconds when the starting directory had been deleted, the machine had slept, or the host is slow to start processes
* Fixed background sessions failing to open with an `EACCES` error when another Claude Code process was re-installing the npm package at that moment
* Fixed markdown rendering being disabled for a whole message when its first 500 characters contained no markdown
* Fixed MCP tool calls interrupted by an incoming message in headless/remote sessions being reported as "completed with no output" instead of an explicit interrupted error
* Fixed MCP tool arguments being sent as JSON strings when the parameter's schema is empty (`{}`), instead of their real type
* Fixed the background retention sweep removing git worktrees under `.claude/worktrees/` that you created yourself when an old background-session record pointed at them
* Fixed auto mode tool calls being denied as "temporarily unavailable" on very large sessions by scaling the safety-check deadline with prompt size
* Fixed the Write tool reporting "Out of memory" or freezing for a long time after overwriting a very large existing file, even though the file had been written
* Fixed resumed sessions failing every turn with a 400 when the saved history contains tool blocks the Anthropic API does not accept (typically written by a third-party API proxy)
* Fixed telemetry and metrics requests to Anthropic carrying the API key configured for a third-party gateway (`ANTHROPIC_BASE_URL`); a credential is now only sent to its own host
* Fixed sessions that ended in plan mode resuming outside plan mode in the VS Code extension, and in `claude -p --continue`/`--resume` with a permission prompt tool, when no permission mode was set
* Fixed Bash permission checks to always require approval for malformed commands with a dangling `&&` or `||` operator
* Fixed `--strict-mcp-config` sessions prompting to approve `.mcp.json` servers they would never load, which left background sessions waiting at startup
* Fixed memory growing with session length in the fullscreen and Ctrl+O transcript views
* Fixed the UI stopping with a render error on the first tool call when a third-party Anthropic-compatible endpoint (`ANTHROPIC_BASE_URL`) streams a `tool_use` block without an `id`
* Fixed `curl -fsSL https://claude.ai/install.sh | bash` failing with "Raw mode is not supported" for some Team/Enterprise users with server-managed settings
* Fixed the command sandbox's filesystem configuration not respecting `--setting-sources`

-----

## Claude Code changes

### Changed documents

#### [amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Before running the `awsAuthRefresh` command, Claude Code now first makes an STS `GetCallerIdentity` call to confirm credentials are actually expired, sent through your proxy configuration; before v2.1.239 it hung at startup on proxy-only networks. [[line 113](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/amazon-bedrock.md?plain=1#L113)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#configure-credential-refresh)]
* New `CLAUDE_CODE_DISABLE_BEDROCK_CONTENT_TYPE_DEFAULT` guidance for a streaming response with a missing/empty `Content-Type` header: Claude Code now defaults to decoding it as the binary event-stream format instead of erroring. [[line 463](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/amazon-bedrock.md?plain=1#L463)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#streaming-errors-behind-a-gateway-or-proxy)]

#### [artifacts](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/artifacts.md) [[Source](https://code.claude.com/docs/en/artifacts)]

* Softened wording on comment reading in the first session after install/upgrade: Claude "might not be able to" read comments yet, rather than definitely can't. [[line 94](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/artifacts.md?plain=1#L94)] [[Source](https://code.claude.com/docs/en/artifacts#claude-cant-read-comments)]

#### [auto-mode-config](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/auto-mode-config.md) [[Source](https://code.claude.com/docs/en/auto-mode-config)]

* New "Edit rules from `/permissions`" section: the **Auto mode** tab (v2.1.246+) lists `allow`/`soft_deny`/`hard_deny`/`environment` entries per scope, lets you add/edit/delete rules and toggle built-in defaults, and edit `environment` as a document in your editor. [[lines 16, 242-250](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/auto-mode-config.md?plain=1#L242-L250)] [[Source](https://code.claude.com/docs/en/auto-mode-config#edit-rules-from-permissions)]

#### [claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/claude-platform-on-aws.md) [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

* New sales/pricing banner added at the top of the page ("Deploying Claude Code across your organization?"). [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/claude-platform-on-aws.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

#### [code-review](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/code-review.md) [[Source](https://code.claude.com/docs/en/code-review)]

* Removed the hardcoded list of sessions where Claude could never auto-start `/code-review` (cloud providers, Claude apps gateway, privacy env vars). As of v2.1.246, Claude auto-starts it wherever feature-flag fetching reaches it; before that, it depended on an Anthropic-side flag and sessions without flag fetching only ran it when typed. [[line 323](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/code-review.md?plain=1#L323)] [[Source](https://code.claude.com/docs/en/code-review#let-claude-start-the-review)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/cd`'s directory-suggestion autocomplete now requires Claude Code v2.1.206 or later. [[line 46](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/commands.md?plain=1#L46)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]
* `/permissions` description now mentions the new **Auto mode** tab. [[line 93](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/commands.md?plain=1#L93)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]
* `/skills`: removed the "then Enter to save" step for cycling a skill's visibility. [[line 120](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/commands.md?plain=1#L120)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]
* `/` menu highlighting rules (matching from the start of a command name/alias or a word within it) now require Claude Code v2.1.236 or later; before that, pressing Enter after a typo ran the closest match instead of submitting as typed. [[lines 148-149](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/commands.md?plain=1#L148-L149)] [[Source](https://code.claude.com/docs/en/commands#how-claude-code-filters-the-menu)]

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* Goal check-ins are now capped at three idle check-ins per goal between prompts (previously uncapped), reducing token spend from indefinite idle check-ins. [[line 270](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/costs.md?plain=1#L270)] [[Source](https://code.claude.com/docs/en/costs#session-level-cost-drivers)]

#### [desktop-linux](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/desktop-linux.md) [[Source](https://code.claude.com/docs/en/desktop-linux)]

* New "Cowork requirements" section: documents hardware virtualization (KVM), QEMU/UEFI firmware packages, and `/dev/kvm`/`/dev/vhost-vsock` access needed to run Cowork's VM on Linux. [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/desktop-linux.md?plain=1#L14)] [[Source](https://code.claude.com/docs/en/desktop-linux#cowork-requirements)]
* New "Unmet dependencies" troubleshooting section for `libc6` version mismatches and downloading the wrong-architecture `.deb`. [[line 124](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/desktop-linux.md?plain=1#L124)] [[Source](https://code.claude.com/docs/en/desktop-linux#unmet-dependencies)]
* New "Cowork isn't available" troubleshooting section mapping each Cowork error message to its fix. [[line 135](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/desktop-linux.md?plain=1#L135)] [[Source](https://code.claude.com/docs/en/desktop-linux#cowork-isnt-available)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* New "Local sessions on managed devices" section documenting the `disableDesktopLocalSessions` managed setting, which grays out the **Local** (and Windows WSL) environment option and defaults new sessions to SSH. [[line 562](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/desktop.md?plain=1#L562)] [[Source](https://code.claude.com/docs/en/desktop#local-sessions-on-managed-devices)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_DISABLE_BEDROCK_CONTENT_TYPE_DEFAULT` variable to opt out of the new default binary-decode behavior for Bedrock streams missing a `Content-Type` header. [[line 213](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/env-vars.md?plain=1#L213)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* Clarifies that flag fetching is also off through the Claude apps gateway and on Bedrock/Claude Platform on AWS/Google Cloud/Foundry (unless a host sets `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST`); removed the note that flag-off sessions can never auto-start `/code-review` (see `code-review.md` change above). [[line 462](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/env-vars.md?plain=1#L462)] [[Source](https://code.claude.com/docs/en/env-vars#features-that-need-feature-flag-fetching)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New "Streaming response ended before any complete data was received" entry: a warning (shown once per session) now surfaces this proxy/gateway condition instead of Claude Code silently retrying without streaming. [[line 1042](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/errors.md?plain=1#L1042)] [[Source](https://code.claude.com/docs/en/errors#streaming-response-ended-before-any-complete-data-was-received)]
* New "Has a wildcard before the rest of the command" configuration warning for Bash allow rules like `Bash(git * main)`, explaining the `-c`/`--exec-path`-style risk and how to narrow the rule. [[line 2367](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/errors.md?plain=1#L2367)] [[Source](https://code.claude.com/docs/en/errors#has-a-wildcard-before-the-rest-of-the-command)]

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* The VS Code extension now supports fast mode, following the `fastMode` setting and offering a "Toggle fast mode" command, reversing the prior "not supported in VS Code" note. [[line 10](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/fast-mode.md?plain=1#L10)] [[Source](https://code.claude.com/docs/en/fast-mode#toggle-fast-mode)]

#### [feature-availability](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/feature-availability.md) [[Source](https://code.claude.com/docs/en/feature-availability)]

* Removed the "`/code-review` runs when you type it; Claude doesn't start it on its own" partial-support bullet from the Bedrock, Claude Platform on AWS, Google Cloud, and Microsoft Foundry tabs, matching the `code-review.md` behavior change above. [[Source](https://code.claude.com/docs/en/feature-availability)]

#### [goal](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/goal.md) [[Source](https://code.claude.com/docs/en/goal)]

* Idle check-ins are now capped at three per goal between your prompts (the third one says check-ins are paused until you prompt again); before v2.1.246 they were uncapped. [[lines 17, 127](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/goal.md?plain=1#L127)] [[Source](https://code.claude.com/docs/en/goal#background-work-defers-evaluation)]

#### [index](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/index.md) [[Source](https://code.claude.com/docs/en/)], [overview](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/overview.md) [[Source](https://code.claude.com/docs/en/overview)]

* Clarifies that the desktop app bundles Claude Code, so installing it means you don't need the CLI separately. [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/index.md?plain=1#L82)] [[Source](https://code.claude.com/docs/en/#claude-code-desktop-app)]

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* `scroll:lineUp`/`scroll:lineDown` now default to `wheelup`/`wheeldown` instead of being unbound, and those two key names are now documented as available bindings. [[lines 325-326, 385](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/keybindings.md?plain=1#L325-L326)] [[Source](https://code.claude.com/docs/en/keybindings#scroll)]
* Key parsing is now fully case-insensitive: `K` and `ctrl+K` both behave the same as their lowercase forms; write `shift+k` to require Shift explicitly. This replaces the old rule where a bare uppercase letter implied Shift. [[line 367](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/keybindings.md?plain=1#L367)] [[Source](https://code.claude.com/docs/en/keybindings#uppercase-letters)]
* Validation now also warns about invalid action values (not a string or `null`); removed the "terminal multiplexer conflicts" warning category. [[line 469](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/keybindings.md?plain=1#L469)] [[Source](https://code.claude.com/docs/en/keybindings#validation-and-troubleshooting)]

#### [managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/managed-settings.md) [[Source](https://code.claude.com/docs/en/managed-settings)]

* Clarifies that some server-managed changes now wait for the next launch rather than applying to the running session or on next poll (see `server-managed-settings.md` change below). [[line 78](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/managed-settings.md?plain=1#L78)] [[Source](https://code.claude.com/docs/en/managed-settings#how-a-policy-reaches-a-session)]
* Adds "Desktop local-session" to the list of managed-only keys not covered by the permission/plugin/delivery table, referencing the new `disableDesktopLocalSessions` key. [[line 222](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/managed-settings.md?plain=1#L222)] [[Source](https://code.claude.com/docs/en/managed-settings#keys-read-from-every-admin-source)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* `plugin.scope` gains a new `"community"` value, and `enabled_via` gains a new `"admin-install"` value for plugins set to required/auto-install in Organization settings; before v2.1.246 these reported as `"user-install"` or `"seed-mount"`. `plugin_id_hash` for claude.ai-synced plugins now incorporates the marketplace name claude.ai reports (or `synced` otherwise). [[lines 843-844](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/monitoring-usage.md?plain=1#L843-L844)] [[Source](https://code.claude.com/docs/en/monitoring-usage#plugin-loaded-event)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Splits out the "first session after install/upgrade" case: a non-interactive session can now pick up feature flags in time to start in `auto` normally, whereas an interactive terminal session still defaults to `default` until flags arrive. [[line 64](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/permission-modes.md?plain=1#L64)] [[Source](https://code.claude.com/docs/en/permission-modes#which-mode-a-session-starts-in)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Notes that the `/permissions` dialog now also shows auto mode classifier rules under a new **Auto mode** tab when auto mode is available. [[line 58](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/permissions.md?plain=1#L58)] [[Source](https://code.claude.com/docs/en/permissions#permissions)]
* Rewrote the "Wildcard patterns" section: explains that Claude Code now warns at startup about a rule whose `*` sits before the subcommand, and adds a full table of example rules with what they match/don't match (e.g. `Bash(ls *)` vs `Bash(ls*)`, trailing-`*` word-boundary behavior). Removed the duplicate, less-detailed wildcard explanation from the Bash-specific subsection below it. [[lines 128, 148-159, 190](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/permissions.md?plain=1#L148-L159)] [[Source](https://code.claude.com/docs/en/permissions#wildcard-patterns)]

#### [quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/quickstart.md) [[Source](https://code.claude.com/docs/en/quickstart)]

* Narrows the auto-mode-by-default claim to interactive terminal sessions specifically, dropping the earlier mention that it also applied to VS Code sessions. [[line 151](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/quickstart.md?plain=1#L151)] [[Source](https://code.claude.com/docs/en/quickstart#your-first-code-change)]

#### [server-managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* New behavior for Claude apps gateway clients: they fetch settings from the gateway and wait for that fetch before the session starts, and exit at startup if it fails (with a `claude auth` exemption), rather than fetching asynchronously like other sessions. [[line 126](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/server-managed-settings.md?plain=1#L126)] [[Source](https://code.claude.com/docs/en/server-managed-settings#fetch-and-caching-behavior)]
* Clarifies that some settings updates (OpenTelemetry exporter config, the `model` key, and removing an `env` variable) now only apply at the next launch, not to the running session; a tampered cached-settings file for one of these keys also survives a fresh server fetch until relaunch. [[lines 112, 150, 248](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/server-managed-settings.md?plain=1#L150)] [[Source](https://code.claude.com/docs/en/server-managed-settings#fetch-and-caching-behavior)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* New `disableDesktopLocalSessions` managed setting: grays out on-device Code sessions (and Windows WSL) in the desktop app, defaulting new sessions to a configured SSH connection; the terminal CLI ignores it. [[lines 65, 4403-4417](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/settings-reference.md?plain=1#L4403-L4417)] [[Source](https://code.claude.com/docs/en/settings-reference#disabledesktoplocalsessions)]

#### [statusline](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/statusline.md) [[Source](https://code.claude.com/docs/en/statusline)]

* Status line scripts now run immediately when you save a config change to the `command` itself, skipping the usual 300ms debounce used for other update triggers. [[lines 121, 136](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/statusline.md?plain=1#L136)] [[Source](https://code.claude.com/docs/en/statusline#how-status-lines-work)]
* Documents that `cost.total_cost_usd` correctly resets to $0 on `/clear`, noting it used to carry over before v2.1.211. [[line 161](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/statusline.md?plain=1#L161)] [[Source](https://code.claude.com/docs/en/statusline#json-fields)]

#### [terminal-config](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* Notes `/terminal-setup`'s GPU acceleration change has applied since v2.1.157. [[line 27](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/terminal-config.md?plain=1#L27)] [[Source](https://code.claude.com/docs/en/terminal-config#set-up-shiftenter-for-multiline-input)]
* Clarifies that `userMessageBackground`, `bashMessageBackgroundColor`, and `memoryBackgroundColor` theme tokens apply in both the default and fullscreen renderers, not fullscreen only. [[line 224](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/terminal-config.md?plain=1#L224)] [[Source](https://code.claude.com/docs/en/terminal-config#fullscreen-mode)]

#### [voice-dictation](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/voice-dictation.md) [[Source](https://code.claude.com/docs/en/voice-dictation)]

* The `hold space to speak` footer hint now only shows for your first three sessions with voice dictation enabled, instead of persisting forever. [[line 47](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/voice-dictation.md?plain=1#L47)] [[Source](https://code.claude.com/docs/en/voice-dictation#voice-dictation)]
* Hold mode's footer now shows `listening…` (was a live waveform) once recording starts, plus a new mic-level-reactive cursor bar; tap mode's footer now shows `● REC · tap to send` instead of a waveform. [[lines 53, 71](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/voice-dictation.md?plain=1#L53-L71)] [[Source](https://code.claude.com/docs/en/voice-dictation#hold-to-record)]
* The repeated-failure pause now triggers on three capture failures within a 10-second window (was an unspecified threshold), and the missing-audio-tool error message changed to `Voice mode requires SoX for audio recording`. [[lines 144, 147](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/claude-code/voice-dictation.md?plain=1#L144-L147)] [[Source](https://code.claude.com/docs/en/voice-dictation#troubleshooting)]

-----

## API changes

### New Documents

#### [models/opus-5/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/api/models/opus-5/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/opus-5/migration-guide)]

New standalone page covering migration to Claude Opus 5 from Opus 4.8, 4.7, and 4.6/earlier: thinking-on-by-default, the effort cap on disabling thinking, pricing (unchanged from 4.8), Priority Tier unavailability, the 1M context window, mid-conversation system messages/tool changes, refusal handling, and per-source checklists. This content was previously part of the single combined `about-claude/models/migration-guide.md` page.

#### [models/sonnet-5/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/api/models/sonnet-5/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/sonnet-5/migration-guide)]

New standalone page covering migration to Claude Sonnet 5 from Sonnet 4.6, 4.5/earlier, and Haiku 4.5: the new tokenizer (~30% more tokens), adaptive thinking on by default, removed sampling parameters, and new real-time cybersecurity safeguards. Split out from the old combined migration guide.

#### [models/haiku-4-5/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/api/models/haiku-4-5/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/haiku-4-5/migration-guide)]

New standalone page covering migration to Claude Haiku 4.5 from Haiku 3.5/earlier: sampling parameter restrictions, updated tool versions, the `refusal` stop reason, and new rate limits. Split out from the old combined migration guide.

#### [models/fable-5/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/api/models/fable-5/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/fable-5/migration-guide)]

New standalone page covering migration to Claude Fable 5 and Claude Mythos 5 from Mythos Preview and Opus 4.8: always-on adaptive thinking, no prefill, $10/$50 per-MTok pricing, 30-day-minimum data retention, and safety classifier refusals (Fable 5 only). Split out from the old combined migration guide.

### Changed documents

#### [about-claude/models/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/api/about-claude/models/migration-guide.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]

* This page shrank from ~980 lines to a short index: it's now just a bulleted list of links to the four new per-model migration guides above, plus a "Get help" section. All the detailed migration content moved to those pages. [[lines 1-13](https://github.com/gpambrozio/ClaudeDocs/blob/8e83fab01bcdbabfc6b6359d1544ef834d097c88/docs-md/api/about-claude/models/migration-guide.md?plain=1#L1-L13)] [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]

*Note: several other API pages (`agent-skills/claude-api-skill`, `claude-prompting-best-practices`, `prompting-claude-opus-4-8`, `prompting-claude-opus-5`, `refusals-and-fallback`, the `opus-4-5`/`opus-4-6`/`opus-4-7`/`opus-4-8`/`sonnet-4-5`/`sonnet-4-6` model overviews, `opus-5/whats-new-opus-5`, `sonnet-5/whats-new-sonnet-5`, `models/overview`, and `release-notes/overview`) changed today only to repoint existing links from the old combined migration guide to the new per-model pages above; no wording or content changed, so they're omitted here.*
