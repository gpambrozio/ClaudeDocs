# [Claude docs changes for July 22nd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/af1833751147994c98e1205fe9f619655afbf89a) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/af1833751147994c98e1205fe9f619655afbf89a)]

## Executive Summary
- Claude Code Desktop adds an **iOS Simulator pane** (public beta, macOS): Claude can build, install, launch, and tap through iOS apps while you watch or take over yourself.
- `/verify` and `/code-review` no longer run automatically — Claude now only invokes them when you explicitly ask, keeping longer-running checks under your control.
- A new `sandbox.filesystem.disabled` setting lets you keep network isolation while turning off filesystem isolation entirely, for workloads that need broad file access but confined egress.
- 2.1.217 adds emoji shortcode autocomplete, a cap on concurrently-running subagents (default 20), and stops subagents from spawning nested subagents by default.
- The Claude API's search-results feature (RAG citations) now works on all active models with no beta header required, and the docs clarify several validation rules (text-only content, user-message-only, tool-result homogeneity).

## New Claude Code versions

### [2.1.208](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/versions/2.1.208.md)

#### Existing feature improvements

* Changed the Fable 5 usage-credits consent prompt to start with the decline option focused

### [2.1.217](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/versions/2.1.217.md)

#### New features

* Added emoji shortcode autocomplete in the prompt input: type `:heart:` to insert ❤️, or `:hea` for suggestions — disable with the `emojiCompletionEnabled` setting
* Added warnings when transcript writes are failing (e.g. disk full) or when session saving is off due to an inherited environment variable, instead of losing transcripts silently
* Added a cap on concurrently-running subagents (default 20, override with `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`) so one message can't fan out unbounded background agents
* Changed subagents to no longer spawn nested subagents by default; set `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` to allow deeper nesting

#### Existing feature improvements

* Improved footer PR badge links to be clickable hyperlinks even when terminal support can't be detected (e.g. over ssh/tmux); set `FORCE_HYPERLINK=0` to opt out
* Changed the login-expiry warning to appear 3 days before expiry instead of 5
* Capped the frontend-design plugin suggestion tip at 3 lifetime impressions instead of repeating indefinitely

#### Major bug fixes

* Fixed a memory leak where truncated MCP tool outputs kept the full untruncated result in memory for the rest of the session
* Fixed Windows auto-update failures that could leave `claude.exe` missing; failed updates now restore the preserved executable automatically
* Fixed background session isolation not canonicalizing symlinked working directories, which could let sessions escape their workspace folder
* Fixed auto-compact never triggering for Claude Opus 4.8 on Bedrock and `/compact` failing once over the limit
* Fixed corporate mTLS, TLS-verify, OAuth scope, and proxy settings being ignored in Claude Desktop sessions
* Fixed screen reader mode's startup announcement being cut off by the first prompt render, and the thinking status row re-rendering every few seconds to update elapsed time and token counts
* Fixed managed settings that set `OTEL_EXPORTER_OTLP_ENDPOINT` not governing all signals — lower-scope signal-specific overrides no longer redirect telemetry away from the managed endpoint
* Fixed `--resume`/`--continue` and `/resume` failing with a TypeError when a transcript has a malformed attachment entry
* Fixed Remote Control sessions not showing a pending permission prompt or dialog to viewers that connected after it appeared
* Fixed background shells sometimes becoming impossible to stop after a session is sent to the background or when the session exits on a heavily loaded machine, most visible on Windows
* Fixed a `CLAUDE.md` or `SKILL.md` paths frontmatter value with many brace groups OOM-killing or stalling the CLI at startup
* Fixed the transcript preview sitting flush against the input area when attaching to a starting background session
* Fixed `--max-budget-usd` not stopping background subagents: once the cap is reached, new spawns are denied and running background agents are halted

-----

## Claude Code changes

### New Documents

#### [desktop-ios-simulator](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/desktop-ios-simulator.md) [[Source](https://code.claude.com/docs/en/desktop-ios-simulator)]

Documents the new iOS Simulator pane in Claude Code Desktop (public beta on macOS, Pro/Max/Team plans). The pane opens automatically when Claude builds, installs, launches, or checks an app in the simulator, streaming the device live. Covers requirements (Xcode, a Mac), interacting with the device yourself (tap, rotate, screenshot/record), how sessions manage devices, granting Claude access, the `disableMobileSimulatorTools` managed setting, and troubleshooting.

### Changed documents

#### [agent-sdk/observability](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/agent-sdk/observability.md) [[Source](https://code.claude.com/docs/en/agent-sdk/observability)]

* `OTEL_LOG_TOOL_CONTENT` and `OTEL_LOG_RAW_API_BODIES` truncation is now configurable via `CLAUDE_CODE_OTEL_CONTENT_MAX_LENGTH` (requires v2.1.214+), instead of a fixed 60 KB. [[lines 224-225](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/agent-sdk/observability.md?plain=1#L224-L225)] [[Source](https://code.claude.com/docs/en/agent-sdk/observability#control-sensitive-data-in-exports)]

#### [channels](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/channels.md) [[Source](https://code.claude.com/docs/en/channels)]

* Plugin installs for channels now prompt to choose the user scope so the plugin is available across all projects. [[line 37](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/channels.md?plain=1#L37)] [[Source](https://code.claude.com/docs/en/channels#supported-channels)]
* `--channels` and `--dangerously-load-development-channels` don't appear in `claude --help` during the research preview, even though they work. [[line 324](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/channels.md?plain=1#L324)] [[Source](https://code.claude.com/docs/en/channels#research-preview)]

#### [checkpointing](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/checkpointing.md) [[Source](https://code.claude.com/docs/en/checkpointing)]

* New section: checkpointing doesn't rewind symlinked or hard-linked files — `/rewind` now skips them and shows a `Restored the code, but skipped N files` warning instead of silently writing through the link. [[line 79](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/checkpointing.md?plain=1#L79)] [[Source](https://code.claude.com/docs/en/checkpointing#symlinked-and-hard-linked-paths-not-restored)]

#### [chrome](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/chrome.md) [[Source](https://code.claude.com/docs/en/chrome)]

* Chrome integration now requires signing in with `/login` — API key or `setup-token` sessions keep it off instead of silently failing every connection attempt with a 403. [[line 30](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/chrome.md?plain=1#L30)] [[Source](https://code.claude.com/docs/en/chrome#prerequisites)]
* New section on the "Claude wants to use your browser" install prompt shown when Claude needs the browser but doesn't detect the extension. [[line 64](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/chrome.md?plain=1#L64)] [[Source](https://code.claude.com/docs/en/chrome#install-the-extension-when-claude-asks)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* `--channels` now also accepts a Console API key for authentication, not just claude.ai. [[line 62](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/cli-reference.md?plain=1#L62)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]
* `--settings` now requires the file to be a regular file no larger than 2 MiB. [[line 110](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/cli-reference.md?plain=1#L110)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/verify` and `/code-review` now run only when explicitly invoked; before v2.1.215 Claude could also run them on its own. [[line 23](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/commands.md?plain=1#L23)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]
* `/context` now shows a warning with how far over the context window you are and which command frees space, once the conversation exceeds it (v2.1.216+). [[line 50](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/commands.md?plain=1#L50)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]

#### [computer-use](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/computer-use.md) [[Source](https://code.claude.com/docs/en/computer-use)]

* Clarifies that in the Desktop app, iOS Simulator tasks now open the dedicated Simulator pane instead of screen control; from the CLI, computer use is still how Claude reaches the simulator. [[lines 26, 160](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/computer-use.md?plain=1#L26)]

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* The in-CLI usage-credits management dialog (buy credits, set spend limit, configure auto-reload) has been replaced: `/usage-credits` now just opens billing settings in the browser, based on your role (Pro/Max, Team/Enterprise with or without billing access). [[lines 29-33](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/costs.md?plain=1#L29-L33)] [[Source](https://code.claude.com/docs/en/costs#add-usage-credits-to-your-subscription)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Documents the new iOS Simulator pane and the `disableMobileSimulatorTools` managed setting to block it. [[lines 149, 614](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/desktop.md?plain=1#L614)]
* New `url` field for preview configurations, letting a preview open an address other than `http://localhost:<port>` (local HTTPS, `*.localhost` subdomains, or attaching to a server you already run). [[lines 408-429](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/desktop.md?plain=1#L408-L429)] [[Source](https://code.claude.com/docs/en/desktop#configuration-fields)]

#### [discover-plugins](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* Notes that `/reload-plugins` is needed after installing a plugin to activate it in the current session. [[line 268](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/discover-plugins.md?plain=1#L268)] [[Source](https://code.claude.com/docs/en/discover-plugins#install-plugins)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* Consolidated the spend-limit error entries into one `Could not update your spend limit` section, since `/usage-credits` no longer has its own dialog for this. [[lines 346-354](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/errors.md?plain=1#L346-L354)] [[Source](https://code.claude.com/docs/en/errors#could-not-update-your-spend-limit)]
* Rewind's skipped-files guidance now suggests `find . -type l` / `find . -type f -links +1` to locate skipped symlinked/hard-linked paths. [[line 1378](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/errors.md?plain=1#L1378)] [[Source](https://code.claude.com/docs/en/errors#restored-the-code-but-skipped-files)]

#### [headless](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* Streaming JSON output now waits up to 30 seconds (scaled to queue size) for a slow consumer to drain before exiting, up from a ~2 second cap in earlier versions that could cut off large responses. [[line 135](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/headless.md?plain=1#L135)] [[Source](https://code.claude.com/docs/en/headless#stream-responses)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)] / [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/hooks-guide.md)

* Behavior change: a `PreToolUse` prompt/agent hook that denies a call now ends the turn and shows the reason as a warning by default, instead of feeding it back to Claude as a tool error. Set `continueOnBlock: true` to restore the old (pre-v2.1.210) behavior. [[hooks.md#L2713](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/hooks.md?plain=1#L2713), [hooks-guide.md#L747](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/hooks-guide.md?plain=1#L747)]
* Clarifies `TaskCompleted` hook behavior differs depending on whether it fires from a task completion (tool-error semantics) or a teammate stopping (`TeammateIdle`-like halt). [[hooks.md#L2717](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/hooks.md?plain=1#L2717)]

#### [how-claude-code-works](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/how-claude-code-works.md) [[Source](https://code.claude.com/docs/en/how-claude-code-works)]

* Softened "every file edit is reversible" to "file edits are reversible" and notes that restores skip symlinked/hard-linked files. [[lines 120-121](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/how-claude-code-works.md?plain=1#L120-L121)] [[Source](https://code.claude.com/docs/en/how-claude-code-works#undo-changes-with-checkpoints)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Fixed: double `Esc` at an empty prompt could stop opening the rewind menu for the rest of a long-running session that used background tasks. [[line 30](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/interactive-mode.md?plain=1#L30)] [[Source](https://code.claude.com/docs/en/interactive-mode#general-controls)]
* Fixed vim-mode `.` (repeat last change): change operators like `cw`/`cc` now replay the deletion too, and `.` after `p`/`P` repeats the paste instead of the previous change. [[line 182](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/interactive-mode.md?plain=1#L182)] [[Source](https://code.claude.com/docs/en/interactive-mode#editing-normal-mode)]

#### [jetbrains](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/jetbrains.md) [[Source](https://code.claude.com/docs/en/jetbrains)]

* `/ide` now confirms a successful connection with a message like `Connected to IntelliJ IDEA.`, and auto-installs the plugin for a detected IDE that lacks it. [[line 63](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/jetbrains.md?plain=1#L63)] [[Source](https://code.claude.com/docs/en/jetbrains#from-external-terminals)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Fixed: a failed `list_changed` refresh now keeps the server's previously discovered tools/prompts/resources instead of replacing them with an empty list. [[line 160](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/mcp.md?plain=1#L160)] [[Source](https://code.claude.com/docs/en/mcp#dynamic-tool-updates)]
* Tools requiring `anthropic/requiresUserInteraction` now also withhold one-tap approval for any permission request that only the terminal dialog can render in full (safety warnings, always-allow options). [[line 970](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/mcp.md?plain=1#L970)] [[Source](https://code.claude.com/docs/en/mcp#require-approval-for-a-specific-tool)]

#### [memory](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Memory files with frontmatter now get a `modified` ISO 8601 timestamp recorded on each write, showing how current a fact is. [[line 347](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/memory.md?plain=1#L347)] [[Source](https://code.claude.com/docs/en/memory#how-it-works)]
* `/memory` opening a file in a GUI editor (e.g. VS Code) no longer blocks the session until the file is closed. [[line 356](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/memory.md?plain=1#L356)] [[Source](https://code.claude.com/docs/en/memory#view-and-edit-with-/memory)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Fallback model chains now also skip a model with a smaller context window than the primary during compaction, since summarizing there would cut off part of the conversation; if every fallback is smaller, compaction shows the original error. [[line 322](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/model-config.md?plain=1#L322)] [[Source](https://code.claude.com/docs/en/model-config#fallback-model-chains)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* New `CLAUDE_CODE_OTEL_CONTENT_MAX_LENGTH` env var configures the OTel content truncation limit (default 60 KB) for tool content, raw API bodies, and other content-bearing attributes. [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/monitoring-usage.md?plain=1#L82)] [[Source](https://code.claude.com/docs/en/monitoring-usage#common-configuration-variables)]
* Fixed: the Prometheus-only metrics scrape no longer includes OpenMetrics-only `# UNIT` lines that some scrapers rejected. [[line 432](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/monitoring-usage.md?plain=1#L432)] [[Source](https://code.claude.com/docs/en/monitoring-usage#metrics)]
* Fixed: streams carrying usage across multiple frames (behind a proxy) no longer inflate `claude_code.cost.usage` / `claude_code.token.usage`. [[line 1018](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/monitoring-usage.md?plain=1#L1018)] [[Source](https://code.claude.com/docs/en/monitoring-usage#cost-monitoring)]
* New `message.uuid`, `client_request_id`, `tool_source`, and `cost_usd_micros` attributes added across several event types for finer-grained correlation with the session transcript.

#### [plugin-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* `claude plugin marketplace list --json` now includes an `installLocation` field with the local cache path. [[line 948](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/plugin-marketplaces.md?plain=1#L948)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#plugin-marketplace-list)]
* Troubleshooting now recommends `git ls-remote <marketplace-url>` to test git authentication directly. [[line 1042](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/plugin-marketplaces.md?plain=1#L1042)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#private-repository-authentication-fails)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* `/usage-credits` from Remote Control now prints the billing URL instead of opening the removed in-CLI dialog. [[line 237](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/remote-control.md?plain=1#L237)] [[Source](https://code.claude.com/docs/en/remote-control#limitations)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* New `sandbox.filesystem.disabled` setting turns off filesystem isolation while keeping network isolation on — useful when you want to control where sandboxed commands connect without restricting what they write. Only settable from user/managed settings or `--settings`, not project settings. [[line 167](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/sandboxing.md?plain=1#L167)] [[Source](https://code.claude.com/docs/en/sandboxing#disable-filesystem-isolation)]

#### [scheduled-tasks](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/scheduled-tasks)]

* Scheduling a task now fails with an error if the project's `.claude` directory or the task file is a symlink, instead of writing through the link. [[line 196](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/scheduled-tasks.md?plain=1#L196)] [[Source](https://code.claude.com/docs/en/scheduled-tasks#limitations)]

#### [sessions](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/sessions.md) [[Source](https://code.claude.com/docs/en/sessions)]

* Resuming a session now also restores the agent it was started with (`--agent` or the `agent` setting), including its system prompt, tool restrictions, and model. [[line 26](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/sessions.md?plain=1#L26)] [[Source](https://code.claude.com/docs/en/sessions#what-a-resumed-session-restores)]
* A session that fails to load from `claude --resume` now prints `Failed to resume the conversation` with a retry command and exits, instead of failing silently. [[line 86](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/sessions.md?plain=1#L86)] [[Source](https://code.claude.com/docs/en/sessions#use-the-session-picker)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* `/verify` and `/code-review` now run only when explicitly invoked, not automatically. [[line 13](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/skills.md?plain=1#L13)] [[Source](https://code.claude.com/docs/en/skills#bundled-skills)]
* Fixed: a plugin skill's frontmatter `name` now only replaces the last segment of the command (keeping the plugin prefix and adding a bare alias), instead of replacing the whole command name. [[line 246](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/claude-code/skills.md?plain=1#L246)] [[Source](https://code.claude.com/docs/en/skills#how-a-skill-gets-its-command-name)]

-----

## API changes

### New Documents

#### [get-api-key](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/api/get-api-key.md) [[Source](https://platform.claude.com/docs/en/get-api-key)]

New page walking through creating and using a Claude API key: signing in to the Console, creating a key, storing it, setting `ANTHROPIC_API_KEY`, and how this relates to the Admin API's key-management endpoints.

### Changed documents

#### [api/rate-limits](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/api/api/rate-limits.md) [[Source](https://platform.claude.com/docs/en/api/rate-limits)]

* Clarifies that new organizations or those with limited usage history may start with limits below the standard tier limits shown on the page, increasing automatically as usage history builds. [[line 22](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/api/api/rate-limits.md?plain=1#L22)] [[Source](https://platform.claude.com/docs/en/api/rate-limits)]

#### [build-with-claude/search-results](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/api/build-with-claude/search-results.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/search-results)]

* Search results with citations now work on all active models except Claude Haiku 3, with no beta header required — previously limited to a specific model list. [[line 13](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/api/build-with-claude/search-results.md?plain=1#L13)] [[Source](https://platform.claude.com/docs/en/build-with-claude/search-results)]
* Clarifies `source` can be any stable string, not just a URL (e.g. `kb://article-1234`). [[line 54](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/api/build-with-claude/search-results.md?plain=1#L54)] [[Source](https://platform.claude.com/docs/en/build-with-claude/search-results)]
* New validation rule: within a `tool_result`, if any block is a `search_result`, all blocks must be `search_result` — mixing types returns an error. [[line 511](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/api/build-with-claude/search-results.md?plain=1#L511)] [[Source](https://platform.claude.com/docs/en/build-with-claude/search-results)]
* New limitation: `search_result` blocks can only appear in user messages (including inside tool results); assistant messages with them are rejected. [[line 588](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/api/build-with-claude/search-results.md?plain=1#L588)] [[Source](https://platform.claude.com/docs/en/build-with-claude/search-results)]

#### [cli-sdks-libraries/cli/scripting](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/api/cli-sdks-libraries/cli/scripting.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/scripting)]

* New section on authenticating `curl` requests with `ant auth login` CLI credentials instead of a static API key, using `ant auth print-credentials --access-token`. [[line 239](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/api/cli-sdks-libraries/cli/scripting.md?plain=1#L239)] [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/scripting)]

#### [manage-claude/cmek](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/api/manage-claude/cmek.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

* Clarifies which roles can configure CMEK: Organization Admins on Claude Platform, or Owners/Primary Owner on Claude Enterprise. [[line 23](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/api/manage-claude/cmek.md?plain=1#L23)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]
* Claude in Chrome added to the list of surfaces CMEK covers. [[line 66](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/api/manage-claude/cmek.md?plain=1#L66)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

#### [manage-claude/cmek-aws-kms](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/api/manage-claude/cmek-aws-kms.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms)]

* Clarifies that key validation always sends the all-zeros compartment UUID as the encryption context (since validation runs before the key is attached to a workspace), while live traffic sends the real compartment ID — the key policy's `EncryptionContext` condition must allow both. [[line 140](https://github.com/gpambrozio/ClaudeDocs/blob/af1833751147994c98e1205fe9f619655afbf89a/docs-md/api/manage-claude/cmek-aws-kms.md?plain=1#L140)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms)]
