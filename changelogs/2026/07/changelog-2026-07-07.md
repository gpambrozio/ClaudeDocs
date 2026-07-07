# [Claude docs changes for July 7th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/98866b7c5e41e7f9242cd696e70e05d5aa6181eb) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/98866b7c5e41e7f9242cd696e70e05d5aa6181eb)]

## Executive Summary
- Claude Code 2.1.202 adds a "Dynamic workflow size" `/config` setting that advises Claude to keep dynamic workflows small/medium/large, plus new `workflow.run_id`/`workflow.name` OpenTelemetry attributes for reconstructing a workflow run's activity, and fixes a long list of bugs across Remote Control, background sessions, MCP config errors, voice dictation, and the installer/updater.
- The Bash tool API docs got a substantial rewrite: it's now explicitly documented as a client tool with a full request/response round trip, a new "Tool versions" section (`bash_20250124` vs. the legacy computer-use-only `bash_20241022`), and a per-model pricing table replacing the old flat 245-token figure.
- Code execution tool docs clarify container lifecycle (30-day expiry with ~5-minute checkpointing) and that Claude Haiku 4.5 now accepts the newer `code_execution_20260120`/`code_execution_20260521` tool versions, though without programmatic tool calling or REPL persistence.
- Files API docs document the `container_upload` content block for sending files to the code execution tool and the `downloadable` metadata field that determines which files can be fetched back.
- The C# SDK reference page for Sessions Events, which had been showing a "Console temporarily unavailable" placeholder in recent crawls, is now fully populated with the real API reference.

-----

## New Claude Code versions

### [2.1.202](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/versions/2.1.202.md)

#### New features

* Added a "Dynamic workflow size" setting in `/config` for controlling how large Claude generally makes dynamic workflows (small/medium/large agent counts) — an advisory guideline, not an enforced cap
* Added `workflow.run_id` and `workflow.name` OpenTelemetry attributes to telemetry emitted by workflow-spawned agents, so a workflow run's activity can be reconstructed from OTel data

#### Existing feature improvements

* Improved `/workflows` agent list layout: wider titles, a dedicated time column, shorter model names, and no per-row tool-call counts
* Improved MCP error messages: clearer error when a server config has `url` but no `type`, suggesting `"type": "http"` instead of the misleading "command: expected string"
* Changed `/review <pr>` back to a fast single-pass review; use `/code-review <level> <pr#>` for the multi-agent review at a chosen effort level

#### Major bug fixes

* Fixed `/rename` on background sessions being reverted when the job restarts, which broke addressing the session by its new name
* Fixed commands sent from Remote Control (mobile/web) into an interactive session failing with "Unknown command"
* Fixed images and files sent from the Remote Control mobile or web app without a caption being silently dropped
* Fixed `/remote-control` sessions showing the wrong permission mode in the mobile and web apps
* Fixed opening a chat from `claude agents` sometimes failing with "currently running as a background agent" followed by a worker crash/respawn loop
* Fixed workflow scripts with unicode quote escapes in strings being corrupted before parsing; workflow parse errors now show the offending line instead of always blaming TypeScript
* Fixed voice dictation retrying in an unbounded loop when the microphone or audio recorder fails — repeated capture failures now pause voice input
* Fixed resuming a session by name, or opening the resume picker, taking minutes and using a large amount of memory in repositories with many git worktrees
* Fixed installer and updater downloads failing immediately with "aborted" when a proxy or network drops the connection mid-download — transient connection drops now retry (up to three attempts)
* Fixed re-invoking an already-loaded skill appending a duplicate copy of its instructions to context
* Fixed a crash in the inline Ctrl+R history search when accepting or cancelling while the search was still scanning the history file
* Fixed transient mTLS handshake failures when settings were re-applied during an in-place client certificate rotation
* Fixed the sign-in URL printed by `claude auth login` and `claude mcp login --no-browser` not being reliably clickable when it wraps over SSH — it is now emitted as a single hyperlink

-----

## Claude Code changes

### Changed documents

#### [Agent SDK — TypeScript](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Documented the new `parent_agent_id` field on session messages: for a nested subagent's messages, the `agentId` of the subagent that spawned it (requires v2.1.202+). [[line 246](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L246)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

#### [Manage multiple agents with agent view](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* A name set with `/rename` or `Ctrl+R` on a background session now persists when the supervisor stops and restarts its process, instead of reverting to the dispatch-time name and breaking `claude --resume <name>` (v2.1.202). [[line 374](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/agent-view.md?plain=1#L374)] [[Source](https://code.claude.com/docs/en/agent-view)]

#### [Claude Code on Claude Platform on AWS](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/claude-platform-on-aws.md) [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

* Removed the "Deploying Claude Code across your organization? Talk to sales..." enterprise promo banner from the top of the page — the third flip on this banner in as many days (removed July 5th, re-added July 6th). [[lines 1-4](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/claude-platform-on-aws.md?plain=1#L1-L4)] [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

#### [Commands](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/review`'s description no longer says it uses "the same review engine as `/code-review`", matching the v2.1.202 change that made `/review` a fast single-pass review again. [[lines 13](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/commands.md?plain=1#L13)] [[line 99](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/commands.md?plain=1#L99)] [[Source](https://code.claude.com/docs/en/commands)]
* `/security-review`'s description changed from "gives a deeper read-only pass" to "checks the diff for security vulnerabilities". [[line 13](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/commands.md?plain=1#L13)] [[Source](https://code.claude.com/docs/en/commands)]

#### [Claude Desktop on Linux (beta)](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/desktop-linux.md) [[Source](https://code.claude.com/docs/en/desktop-linux)]

* Added a note that fresh Debian/Ubuntu installs may lack `curl`, needed to download the apt signing key, with the `sudo apt install curl` fix if the download fails with `sudo: curl: command not found`. [[line 22](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/desktop-linux.md?plain=1#L22)] [[Source](https://code.claude.com/docs/en/desktop-linux)]
* Added troubleshooting for `apt install ./claude-desktop_*.deb` failing with `E: Unsupported file ... given on commandline`, which means the glob didn't match a downloaded `.deb` in the current directory. [[line 72](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/desktop-linux.md?plain=1#L72)] [[Source](https://code.claude.com/docs/en/desktop-linux)]

#### [Environment variables](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `OTEL_LOG_TOOL_DETAILS` now also gates including user-authored workflow names in OpenTelemetry traces and logs. [[line 342](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/env-vars.md?plain=1#L342)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [Error reference](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* Added a new "The connection dropped while downloading the update" entry: `claude install`/`claude update`/the automatic updater now retry up to three times on a dropped connection, stalled transfer, or failed checksum instead of failing immediately with the bare error `aborted` (fixed in v2.1.202). [[lines 848-864](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/errors.md?plain=1#L848-L864)] [[Source](https://code.claude.com/docs/en/errors)]
* Added guidance that if Sonnet 5 refuses a request citing a suspected prompt injection on v2.1.200 or earlier, `claude update` picks up the v2.1.201 fix. [[line 918](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/errors.md?plain=1#L918)] [[Source](https://code.claude.com/docs/en/errors)]

#### [Hooks reference](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Documented that async hook JSON output is now validated against the same output schema as synchronous hooks, dropping fields with the wrong type (visible with `--debug`) instead of crashing the session — a crash that previously recurred on every resume (fixed in v2.1.202). [[line 2802](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/hooks.md?plain=1#L2802)] [[Source](https://code.claude.com/docs/en/hooks)]

#### [Interactive mode](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* `Esc` now closes an open dialog (such as a permission prompt) instead of interrupting Claude and leaving the dialog open (v2.1.202). [[line 27](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/interactive-mode.md?plain=1#L27)] [[Source](https://code.claude.com/docs/en/interactive-mode)]
* Accepting or cancelling a `Ctrl+R` history search now works immediately even while history is still loading, instead of sometimes reporting an internal error (v2.1.202). [[line 221](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/interactive-mode.md?plain=1#L221)] [[Source](https://code.claude.com/docs/en/interactive-mode)]

#### [Connect Claude Code to tools via MCP](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Documented the clearer error for a JSON server entry with `url` but no `type` (`add "type": "http" (or "sse" / "ws")`), replacing the old confusing `command: expected string, received undefined` message (v2.1.202). [[line 70](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/mcp.md?plain=1#L70)] [[Source](https://code.claude.com/docs/en/mcp)]

#### [Monitoring](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Documented new `workflow.run_id` and `workflow.name` span attributes on API and tool-call spans for agents spawned by a Workflow tool run; `workflow.name` is replaced with `custom` for user-authored workflows unless `OTEL_LOG_TOOL_DETAILS=1` (requires v2.1.202+). [[lines 166-167](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/monitoring-usage.md?plain=1#L166-L167)] [[lines 390-391](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/monitoring-usage.md?plain=1#L390-L391)] [[Source](https://code.claude.com/docs/en/monitoring-usage)]

#### [Enterprise network configuration](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/network-config.md) [[Source](https://code.claude.com/docs/en/network-config)]

* Clarified that Claude Code re-reads mTLS certificate/key files each time it applies settings, so rotating the certificate is just a matter of replacing the files at the same paths — related to the v2.1.202 fix for transient handshake failures during in-place rotation. [[line 83](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/network-config.md?plain=1#L83)] [[Source](https://code.claude.com/docs/en/network-config)]

#### [Choose a permission mode](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Documented that the Remote Control mode dropdown now reflects the local session's actual mode, including modes set from the terminal, and updates live — before v2.1.202 the dropdown didn't report the session's mode at all, though permission prompts were always generated correctly. [[line 75](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/permission-modes.md?plain=1#L75)] [[Source](https://code.claude.com/docs/en/permission-modes)]

#### [Configure permissions](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Clarified that a compound `cd && git` command only prompts when the `cd` actually changes directory (since a new directory could run different git hooks); a `cd` that resolves to the current directory is a no-op and stays prompt-free. [[line 167](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/permissions.md?plain=1#L167)] [[Source](https://code.claude.com/docs/en/permissions)]
* Documented that approving a file path with "Yes, don't ask again" now escapes gitignore-pattern characters (`[`, `]`, `*`, etc.) in the generated rule, fixing rules for paths like `[2024-06] Reports` that previously could fail to match themselves or match unintended siblings (v2.1.202). [[line 250](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/permissions.md?plain=1#L250)] [[Source](https://code.claude.com/docs/en/permissions)]

#### [Continue local sessions from any device with Remote Control](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Added "Send images and files from your phone or browser" as a headline capability; attachments sent without a caption used to be silently dropped before reaching the session (fixed v2.1.202). [[line 10](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/remote-control.md?plain=1#L10)] [[Source](https://code.claude.com/docs/en/remote-control)]

#### [Run prompts on a schedule](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/scheduled-tasks)]

* Documented that self-paced `/loop` now ends explicitly via `ScheduleWakeup` with `stop: true`, and that a fallback wakeup fires ~20 minutes later if an iteration neither reschedules nor stops (previously, not rescheduling was the only way to end a loop). [[line 114](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/scheduled-tasks.md?plain=1#L114)] [[Source](https://code.claude.com/docs/en/scheduled-tasks)]

#### [Claude Code settings](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Documented the new `workflowSizeGuideline` setting (`unrestricted`/`small`/`medium`/`large`, shown as **Dynamic workflow size** in `/config`), sent to Claude as advisory guidance on agent counts for dynamic workflows it writes (requires v2.1.202+). [[line 309](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/settings.md?plain=1#L309)] [[Source](https://code.claude.com/docs/en/settings)]

#### [Advanced setup](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* Added the same "install curl first" note as the Linux desktop guide to the apt-repository install instructions. [[line 286](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/setup.md?plain=1#L286)] [[Source](https://code.claude.com/docs/en/setup)]

#### [Extend Claude with skills](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Documented that re-invoking a skill whose rendered content is unchanged now adds a short "already loaded" note instead of appending a full duplicate copy of its instructions; changed content (different arguments or dynamic context) still appends in full (v2.1.202). [[line 324](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/skills.md?plain=1#L324)] [[Source](https://code.claude.com/docs/en/skills)]

#### [Tools reference](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* Documented that `ScheduleWakeup` now accepts `stop: true` to end a self-paced loop by cancelling the pending wakeup (requires v2.1.202+). [[line 32](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/tools-reference.md?plain=1#L32)] [[Source](https://code.claude.com/docs/en/tools-reference)]

#### [Troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/troubleshooting.md) [[Source](https://code.claude.com/docs/en/troubleshooting)]

* Added a row pointing update/install download failures (`aborted`, "connection dropped") to the new Error reference entry. [[line 8](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/troubleshooting.md?plain=1#L8)] [[Source](https://code.claude.com/docs/en/troubleshooting)]

#### [Find bugs with ultrareview](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/ultrareview.md) [[Source](https://code.claude.com/docs/en/ultrareview)]

* Updated the comparison table now that `/review <pr>` is "a single-pass review at the session's effort" (seconds to a few minutes) rather than "the medium `/code-review` engine", matching the v2.1.202 change. [[lines 82-83](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/ultrareview.md?plain=1#L82-L83)] [[Source](https://code.claude.com/docs/en/ultrareview)]

#### [Voice dictation](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/voice-dictation.md) [[Source](https://code.claude.com/docs/en/voice-dictation)]

* Clarified that the "Voice input is failing repeatedly and has been paused" counter now counts both startup failures and a recorder that starts and then produces no audio, not just startup failures (v2.1.202). [[line 151](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/voice-dictation.md?plain=1#L151)] [[Source](https://code.claude.com/docs/en/voice-dictation)]

#### [Orchestrate subagents at scale with dynamic workflows](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/workflows.md) [[Source](https://code.claude.com/docs/en/workflows)]

* Added a new "Set a size guideline" section documenting the `/config` **Dynamic workflow size** setting and its four values (`unrestricted` = no guideline/default, `small` < 5 agents, `medium` < 15 agents, `large` < 50 agents) — advisory only, still bounded by the runtime's hard agent caps. [[lines 284-294](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/claude-code/workflows.md?plain=1#L284-L294)] [[Source](https://code.claude.com/docs/en/workflows)]

-----

## API changes

### Changed documents

#### [Bash tool](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/agents-and-tools/tool-use/bash-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool)]

* Rewritten to lead with the client-tool model: Claude only returns the `tool_use` block naming a command, your application runs it and returns the output — includes a full example `tool_use` response and the request/response round trip. [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/agents-and-tools/tool-use/bash-tool.md?plain=1#L11)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool)]
* Added a new "Tool versions" section: `bash_20250124` is current and needs no beta header (Sonnet 3.7 onward); the legacy `bash_20241022` is computer-use-beta-only and limited to the original Claude Sonnet 3.5. [[lines 104-108](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/agents-and-tools/tool-use/bash-tool.md?plain=1#L104-L108)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool)]
* Replaced the flat "245 input tokens" pricing figure with a per-model table: 325 tokens for Claude Opus 4.7/4.8, 244 tokens for Opus 4.6, Sonnet 4.6, and earlier. [[lines 335-342](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/agents-and-tools/tool-use/bash-tool.md?plain=1#L335-L342)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool)]
* Rewrote the security guidance: the allowlist check in the implementation walkthrough is now framed as "a tripwire for obvious mistakes, not an enforcement boundary" — real isolation is running the session in a container or VM — and added "redact credentials and secrets from output" to the recommended controls. [[line 333](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/agents-and-tools/tool-use/bash-tool.md?plain=1#L333)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool)]

#### [Code execution tool](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

* Claude Haiku 4.5 now supports `code_execution_20260120` and `code_execution_20260521`, though programmatic tool calling and the REPL state persistence they add still aren't available on Haiku, so the newer versions behave like `code_execution_20250825` there. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L36)] [[lines 39-43](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L39-L43)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]
* Clarified container reuse: containers expire 30 days after creation, are checkpointed after ~5 minutes of inactivity, and restore automatically when a request references them within the 30-day window; an expired container can't be reused and must be recreated by omitting the `container` parameter. Removed the separate `container_expired` error code in favor of this description. [[line 478](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L478)] [[line 425](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L425)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]
* Spelled out that the sandbox container has no internet access, so Claude can only use the pre-installed libraries and can't install packages at runtime. [[line 108](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L108)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]
* Result block field names were changed to snake_case (`numLines`→`num_lines`, `oldStart`→`old_start`, etc.) and result `type` values are now specific to the operation (`text_editor_code_execution_view_result`, `..._create_result`, `..._str_replace_result`) instead of one shared `text_editor_code_execution_result`. [[lines 307-345](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L307-L345)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

#### [Files API](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Documented the `container_upload` content block for sending files to the code execution tool, and the `downloadable` metadata field (`false` for uploaded files, `true` only for files created by skills or code execution). [[line 72](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/build-with-claude/files.md?plain=1#L72)] [[lines 154-158](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/build-with-claude/files.md?plain=1#L154-L158)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]
* Documented that .csv and .md files can now be uploaded through the Files API with an explicit `text/plain` content type, as an alternative to inlining their content as plain text. [[line 167](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/build-with-claude/files.md?plain=1#L167)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]
* Added a "Not downloadable (400)" error case: downloading a file you uploaded (rather than one created by skills or code execution) returns a 400. [[line 286](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/build-with-claude/files.md?plain=1#L286)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

#### [PDF support](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/build-with-claude/pdf-support.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/pdf-support)]

* The 100-page limit now applies to any request whose context window is under 1M tokens, rather than being tied specifically to "models with a 200k-token context window". [[line 27](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/build-with-claude/pdf-support.md?plain=1#L27)] [[Source](https://platform.claude.com/docs/en/build-with-claude/pdf-support)]
* Noted that Microsoft Foundry doesn't support the Files API for deployments hosted on Azure. [[line 95](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/build-with-claude/pdf-support.md?plain=1#L95)] [[Source](https://platform.claude.com/docs/en/build-with-claude/pdf-support)]

#### [Coordinates and bounding boxes](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/build-with-claude/vision-coordinates.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/vision-coordinates)]

* Added guidance that for small elements, precision loss from downscaling can be avoided by cropping the region of interest (offsetting returned coordinates by the crop origin) or by using a high-resolution-tier model. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/build-with-claude/vision-coordinates.md?plain=1#L19)] [[Source](https://platform.claude.com/docs/en/build-with-claude/vision-coordinates)]
* Clarified that for most photos/screenshots the visual token limit — not the edge limit — determines the final resize, and gave a worked example (1920×1080 → 1456×819, not the edge-limit-implied 1568×882) plus a high-resolution-tier counter-example where the same scanned page isn't resized at all. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/build-with-claude/vision-coordinates.md?plain=1#L36)] [[Source](https://platform.claude.com/docs/en/build-with-claude/vision-coordinates)]

#### [Session start](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/managed-agents/sessions.md) [[Source](https://platform.claude.com/docs/en/managed-agents/sessions)]

* Added SDK examples (Python, TypeScript, C#, Go, Java, PHP, Ruby) for the model-override/system-prompt-clearing session example, which previously only showed cURL and CLI. [[line 59](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/managed-agents/sessions.md?plain=1#L59)] [[Source](https://platform.claude.com/docs/en/managed-agents/sessions)]

#### [Events](https://github.com/gpambrozio/ClaudeDocs/blob/98866b7c5e41e7f9242cd696e70e05d5aa6181eb/docs-md/api/api/csharp/beta/sessions/events.md) [[Source](https://platform.claude.com/docs/en/api/csharp/beta/sessions/events)]

* The C# SDK reference for the Sessions Events API (list, send, and stream session events, plus the full set of `BetaManagedAgents*Event` model definitions) is now fully populated. Recent crawls of this page had been returning a "Console temporarily unavailable" placeholder instead of real content.

### Minor edits (not itemized individually)

* `adaptive-thinking.md`, `citations.md`, `extended-thinking.md`, `overview.md`, `prompt-caching.md`, `task-budgets.md`, and `manage-claude/workspaces.md` had small wording/link fixes, including automatic prompt caching now being GA on Google Cloud (previously Bedrock and Google Cloud were both listed as unsupported; only Bedrock still is).
