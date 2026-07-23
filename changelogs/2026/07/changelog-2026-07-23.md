# [Claude docs changes for July 23rd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/2efbe9e6246276abcf3cfe07c882d021711b2eeb) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/2efbe9e6246276abcf3cfe07c882d021711b2eeb)]

## Executive Summary
- New **Dreams API** (beta): asynchronous "memory consolidation" jobs (`/v1/dreams`) that distill session transcripts and/or an existing memory store into durable agent memories.
- Extended thinking docs got a major overhaul: adaptive thinking is now the primary (and on newer models, only) reasoning mode, with new dedicated pages for steering/cost, tool-use workflows, and troubleshooting, plus a new `xhigh` effort level.
- New **Claude Security** plugin — a local multi-agent vulnerability scanner (`/plugin install claude-security@claude-plugins-official`, then `/claude-security`) that scans a codebase or diff and produces reviewed, manually-applied patches.
- Managed Agents/Sessions API adds `initial_events` to seed a session with a message or outcome definition at creation time, a new per-agent `effort` control, thread-level streaming previews, and new Environment/Memory Store webhook events.
- Claude Code 2.1.218 moves `/code-review` to a background subagent, turns off nested subagent spawning by default (with new depth/concurrency env vars), and ships numerous accessibility, sandbox-trust, and stability fixes.

## New Claude Code versions

### [2.1.218](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/versions/2.1.218.md)

#### New features

* Changed `/code-review` to run as a background subagent, so review work no longer fills your conversation and keeps stacked slash commands as its review target
* Added screen-reader announcements of deleted text for word and line deletions (`Option+Delete`, `Ctrl+W`, `Cmd+Backspace`, `Ctrl+U`, `Ctrl+K`) in `--ax-screen-reader` mode
* Added HTTP status and error text to `claude mcp list` and `/mcp` when a server fails to connect, plus a warning for MCP config values with hidden leading or trailing whitespace
* Added an announcement when fast mode changes as a result of switching models via `/config model=<x>` or Remote Control
* Added `yes`/`no`/`on`/`off`/`1`/`0` (case-insensitive) as accepted values for skill and plugin frontmatter booleans, alongside `true`/`false`

#### Existing feature improvements

* Improved `/ultrareview` error feedback so Claude can correct an invalid argument instead of retrying it unchanged, and fixed it failing on descriptive arguments like "review my auth changes" — they now run a review of your current branch with the text applied as a note to the findings
* Fixed `/code-review ultra` silently running a local review in non-interactive sessions — it now launches the cloud review
* Improved auto mode: the dangerous-rm, background-`&`, and suspicious-Windows-path checks no longer open permission dialogs; the auto-mode classifier adjudicates them instead
* Changed plan mode with auto to no longer prompt for Bash commands the static analyzer can't prove read-only; the auto-mode classifier judges them instead
* Improved sandbox command restrictions for IDE interactions
* Improved trust dialogs to name the repository root the grant covers
* Changed server-managed settings so benign feature and cost toggles no longer trigger the settings-approval prompt
* Changed skills with `context: fork` to run in the background by default; opt out per skill with `background: false`
* Changed `/deep-research` to start only when invoked manually; Claude no longer launches it on its own
* Changed agent markdown files to reject agent names containing `:`, which is reserved for plugin namespacing
* Fixed gateway spend metering to price Bedrock application-inference-profile ARNs and other config-mapped upstream model IDs at the configured model's rates

#### Major bug fixes

* Fixed Windows paths with `\u`-prefixed segments (like `C:\Users\unicorn`) being corrupted into CJK characters in tool inputs, which made those files inaccessible
* Fixed the left arrow key discarding the conversation with no undo: presses right after editing now ask to confirm, and Esc in the agent view returns to the conversation it backgrounded
* Fixed multi-line paste collapsing into one line with `j` in place of newlines in terminals that encode pasted newlines as Ctrl+J
* Fixed `/context` reporting stale pre-compact token usage after compacting from the message picker
* Fixed mojibake when a long IDE selection was truncated mid-emoji, and a case where a tool executor error could be silently dropped
* Fixed an engine teardown race that could start and abandon a phantom turn, and made input pushed after close consistently rejected
* Fixed spurious "[Request interrupted by user]" messages after interrupted tool calls, and an unpaired `tool_use` block left in the transcript when a tool aborted mid-response
* Fixed crashes (maximum call stack exceeded) when a deeply nested watched directory tree was deleted or moved, and when rendering deeply nested UI trees
* Fixed pull request events occasionally being lost when a session exited immediately after creating or linking a PR
* Fixed the Bedrock setup wizard failing profile verification for assume-role profiles in partitioned AWS regions and on proxy-only networks
* Fixed rare negative or incorrect turn duration measurements after a system clock adjustment by timing turns with a monotonic clock
* Fixed the "N MCP servers need authentication" startup notice over-counting claude.ai connectors that aren't connected in claude.ai
* Fixed prompt history entries being dropped or duplicated when history writes raced or failed
* Fixed a retry loop that re-sent identical doomed requests after a context-overflow error with a large thinking budget; `Ctrl+B` backgrounding now applies the same background-shell caps as other paths
* Fixed agent frontmatter hooks running from untrusted folders: hooks now require the agent file's own folder to have accepted workspace trust
* Fixed fork-session lineage being lost after compaction in headless and SDK sessions
* Fixed a resumed session failing every turn, or crashing on resume, when its history held a malformed delta attachment
* Fixed remote sessions continuing to send heartbeats after their worker was replaced, which left long-lived desktop and IDE processes retrying a rejected request every few seconds forever

-----

## Claude Code changes

### New Documents

#### [claude-security](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/claude-security.md) [[Source](https://code.claude.com/docs/en/claude-security)]

New documentation page for the **Claude Security plugin**, a multi-agent vulnerability scanner that runs locally inside a Claude Code session (distinct from the managed, Enterprise-only "Claude Security" hosted product). It requires Claude Code v2.1.154+ on a paid plan (for dynamic workflows), Python 3.9.6+ as `python3` on PATH, and Git for change-scoped scans. Installed via `/plugin install claude-security@claude-plugins-official` and activated with `/reload-plugins`, it adds a single `/claude-security` command offering three jobs: scanning a whole codebase, scanning only a diff (branch, PR, or single commit), and turning chosen findings into reviewed patches. Results are written to a timestamped `CLAUDE-SECURITY-<timestamp>/` directory (`CLAUDE-SECURITY-RESULTS.md`/`.jsonl` plus a revision-stamp JSON tying findings to the exact commit/effort scanned), and patches (one `F<n>.patch` per finding) are independently reviewed but never auto-applied — developers apply them manually via `git apply`.

### Changed documents

#### [accessibility](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/accessibility.md) [[Source](https://code.claude.com/docs/en/accessibility)]

* New feature: Claude Code now announces deleted text when a word or line is removed from the input (`Ctrl+W`, `Option+Delete`, `Ctrl+Backspace`, `Ctrl+U`, `Cmd+Backspace`, `Ctrl+K`), requires v2.1.218+. [[lines 50-56](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/accessibility.md?plain=1#L50-L56)] [[Source](https://code.claude.com/docs/en/accessibility#what-your-screen-reader-hears)]
* `CLAUDE_CODE_ACCESSIBILITY` cursor tracking extended: now follows keyboard focus into menus/panels (e.g. `/config`, `/plugin`), not just the input caret; requires v2.1.218+. [[line 93](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/accessibility.md?plain=1#L93)] [[Source](https://code.claude.com/docs/en/accessibility#accessibility-settings-beyond-screen-reader-mode)]

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* `tools` field default behavior clarified: omitting it now inherits only the tools available to subagents, not literally "all tools." [[line 1093](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/agent-sdk/python.md?plain=1#L1093)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#agentdefinition)]

#### [agent-sdk/subagents](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/agent-sdk/subagents.md) [[Source](https://code.claude.com/docs/en/agent-sdk/subagents)]

* Nested subagent spawning behavior changed: subagents can no longer spawn subagents by default; new `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` env var (default 1) controls depth. Previously (v2.1.172-v2.1.216) nesting was allowed by default up to 5 layers. [[line 174](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/agent-sdk/subagents.md?plain=1#L174)] [[Source](https://code.claude.com/docs/en/agent-sdk/subagents#agentdefinition-configuration)]
* New clarification: a tool left out of `tools` isn't in the subagent's session at all — Claude works without it silently (no permission prompt or error). [[lines 526-531](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/agent-sdk/subagents.md?plain=1#L526-L531)] [[Source](https://code.claude.com/docs/en/agent-sdk/subagents#tool-restrictions-2)]
* `tools` omission clarified to mean "every tool available to subagents" rather than "all tools," and tool definitions inherited by subagents are now noted as "filtered for background runs." [[lines 156](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/agent-sdk/subagents.md?plain=1#L156), [191](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/agent-sdk/subagents.md?plain=1#L191)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* `tools` field default behavior clarified: omitting it inherits only tools available to subagents, not literally "all tools from parent." [[line 640](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L640)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#agentdefinition)]

#### [authentication](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/authentication.md) [[Source](https://code.claude.com/docs/en/authentication)]

* Login-expiry warning threshold changed from 5 days to 3 days before expiration (v2.1.217+). [[line 152](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/authentication.md?plain=1#L152)] [[Source](https://code.claude.com/docs/en/authentication#renew-an-expiring-login)]

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* New documented behavior: if Claude asks a question and a cloud session sits idle, you can still answer later (up to environment expiry) and the session continues from your answer. [[line 596](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L596)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#from-terminal-to-web)]
* New clarification on teleport: the terminal gets its own copy of the session, so new local work doesn't propagate back to the cloud session; to keep steering from the phone after teleporting, start `/remote-control` locally. [[line 649](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L649)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#from-web-to-terminal)]

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* `/usage` breakdown now also flags behaviors (e.g. long context, cache misses) accounting for ≥10% of recent usage. [[line 25](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/costs.md?plain=1#L25)] [[Source](https://code.claude.com/docs/en/costs#using-the-/usage-command)]
* New section explaining why usage climbs in long sessions: full-context resends, cache misses (cache lifetime 1hr on subscription/5min once on usage credits or with API key/cloud provider), scheduled tasks firing while idle, agent teammates consuming tokens until exit, and `/compact` being itself a large request (vs. free `/clear`). [[lines 240-250](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/costs.md?plain=1#L240-L250)] [[Source](https://code.claude.com/docs/en/costs#why-usage-climbs-in-a-long-session)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Environment option renamed from "Remote" to "Cloud" for Anthropic-hosted cloud sessions (throughout the doc). [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/desktop.md?plain=1#L36)] [[Source](https://code.claude.com/docs/en/desktop#start-a-session)]

#### [desktop-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/desktop-quickstart.md) [[Source](https://code.claude.com/docs/en/desktop-quickstart)]

* Environment option renamed from "Remote" to "Cloud" for Anthropic-hosted cloud sessions. [[line 60](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/desktop-quickstart.md?plain=1#L60)] [[Source](https://code.claude.com/docs/en/desktop-quickstart#start-your-first-session)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New env var `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`: caps concurrently running subagents per session (default 20), v2.1.217+. [[line 241](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/env-vars.md?plain=1#L241)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New env var `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`: sets allowed subagent nesting depth below main conversation (default 1, i.e. no nesting by default), v2.1.217+. [[line 246](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/env-vars.md?plain=1#L246)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* "Agent would be spawned with zero tools" error reworked with three distinct failure categories, including new detail that background subagents (the default) drop tools only available to foreground subagents. [[lines 1223-1227](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/errors.md?plain=1#L1223-L1227)] [[Source](https://code.claude.com/docs/en/errors#agent-would-be-spawned-with-zero-tools)]
* New fix guidance: remove entries for tools background subagents drop (e.g. `LSP`, `TaskCreate`) or run the subagent in the foreground; a `tools` list containing only `Agent` resolves to zero tools unless nested spawning is enabled. [[lines 1238-1240](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/errors.md?plain=1#L1238-L1240)] [[Source](https://code.claude.com/docs/en/errors#agent-would-be-spawned-with-zero-tools)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* New requirement: frontmatter hooks in a project subagent only run after the workspace trust dialog has been accepted for the folder the agent file came from; before v2.1.218 they could run from untrusted folders. [[line 529](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/hooks.md?plain=1#L529)] [[Source](https://code.claude.com/docs/en/hooks#hooks-in-skills-and-agents)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* New emoji shortcode input feature: type `:name:` to insert an emoji, or `:` plus 2+ chars for a suggestion popup (Tab/Enter to insert); requires v2.1.217+; toggle via `emojiCompletionEnabled`. [[lines 76](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/interactive-mode.md?plain=1#L76), [317-325](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/interactive-mode.md?plain=1#L317-L325)]
* Background commands owned by a subagent now get a separate 60-minute termination (configurable via `CLAUDE_SUBAGENT_BG_SHELL_MAX_MS`); before v2.1.218 `Ctrl+B`-backgrounded commands weren't covered by either memory-pressure or time limits. [[line 265](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/interactive-mode.md?plain=1#L265)] [[Source](https://code.claude.com/docs/en/interactive-mode#how-backgrounding-works)]
* PR status badge now always renders as a hyperlink even when hyperlink support can't be detected (e.g. over SSH/tmux); set `FORCE_HYPERLINK=0` to force plain text. [[line 382](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/interactive-mode.md?plain=1#L382)] [[Source](https://code.claude.com/docs/en/interactive-mode#pr-review-status)]

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* Footer navigation context now includes artifacts, with a new `footer:dismiss` action (Backspace/Delete) to dismiss an artifact link from the footer without affecting the published artifact; requires v2.1.217+. [[lines 53](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/keybindings.md?plain=1#L53), [228](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/keybindings.md?plain=1#L228)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Startup notice for servers needing auth now only counts servers you can sign in to from Claude Code; before v2.1.218 it also incorrectly counted disconnected claude.ai connectors (which can only be connected from claude.ai settings). [[line 485](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/mcp.md?plain=1#L485)] [[Source](https://code.claude.com/docs/en/mcp#authenticate-with-remote-mcp-servers)]

#### [memory](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* New documented limit on brace-expansion in `paths` rules: a shared budget of 1,000 expanded patterns and 4 MiB per rule; patterns exceeding it are used unexpanded (matching nothing). Before v2.1.217, many brace groups could stall or crash the CLI at startup. [[lines 208-209](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/memory.md?plain=1#L208-L209)] [[Source](https://code.claude.com/docs/en/memory#path-specific-rules)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* New section: a generic `OTEL_EXPORTER_OTLP_ENDPOINT`/credential variable set in managed settings now governs all signals' endpoints, stripping any signal-specific endpoint override set at lower precedence (user settings/shell) at startup with a debug warning. Before v2.1.217, signal-specific overrides could redirect telemetry away from the managed collector. [[lines 59-75](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/monitoring-usage.md?plain=1#L59-L75)] [[Source](https://code.claude.com/docs/en/monitoring-usage#managed-endpoints-govern-signal-specific-endpoints)]

#### [security-guidance](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/security-guidance.md) [[Source](https://code.claude.com/docs/en/security-guidance)]

* Added a new "deep scan" row for the Claude Security plugin: a multi-agent vulnerability scan of a repo or diff with independently reviewed findings and patches, distinct from the single-pass `/security-review`. [[line 212](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/security-guidance.md?plain=1#L212)] [[Source](https://code.claude.com/docs/en/security-guidance#how-this-fits-with-other-security-tools)]

#### [sessions](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/sessions.md) [[Source](https://code.claude.com/docs/en/sessions)]

* Clarified/changed `/branch` semantics: it copies the transcript and switches the same process to write to it, so "allow for this session" permission grants now DO carry over to the branch (previously documented as not carrying over); only `--fork-session` (separate process) requires re-approving. Also documents that in-flight background subagents/Bash commands keep running and their output goes to the new branch, not the original. [[lines 104-111](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/sessions.md?plain=1#L104-L111)] [[Source](https://code.claude.com/docs/en/sessions#branch-a-session)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New `emojiCompletionEnabled` setting (default `true`) to control emoji shortcode suggestions/replacement; requires v2.1.217+. [[line 242](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/settings.md?plain=1#L242)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* New `filesystem.disabled` sandbox setting to skip filesystem isolation entirely (network isolation stays enforced); only honored from user/managed/CLI `--settings`; requires v2.1.216+. [[lines 386](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/settings.md?plain=1#L386), [445](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/settings.md?plain=1#L445)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Nested subagent spawning is now off by default (previously on by default, fixed 5-level depth, not configurable). New env var `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` sets how many layers of nesting are allowed. [[lines 755-773](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/sub-agents.md?plain=1#L755-L773)] [[Source](https://code.claude.com/docs/en/sub-agents#let-subagents-spawn-their-own-subagents)]
* New "Concurrent subagent limit": default cap of 20 simultaneously-running subagents spawned via the Agent tool; fails with `Concurrent subagent limit reached` when exceeded; configurable via `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`; not enforced for ultracode sessions. Requires v2.1.217+. [[lines 777-786](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/sub-agents.md?plain=1#L777-L786)] [[Source](https://code.claude.com/docs/en/sub-agents#session-subagent-limit)]
* Available-tools model reworked into two filters: a short always-removed list (now including `Agent` until nested spawning is enabled, plus newly added `TaskOutput` and `Workflow`), and a second filter that gives background subagents (the default) a much smaller built-in tool set — only `Read, Grep, Glob, Bash, PowerShell, Edit, Write, NotebookEdit, WebFetch, WebSearch, TodoWrite, Skill, ToolSearch, EnterWorktree, ExitWorktree, Monitor, TaskStop, SendMessage, Artifact` (plus all MCP tools). [[lines 285-286](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/sub-agents.md?plain=1#L285-L286)] [[Source](https://code.claude.com/docs/en/sub-agents#available-tools)]
* Worktree-isolation Bash check hardened: commands that try to redirect git into the main checkout (via `git -C`, `--git-dir`, `GIT_DIR`/`GIT_WORK_TREE`, or `cd` first) now fail with an error. [[line 221](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/sub-agents.md?plain=1#L221)] [[Source](https://code.claude.com/docs/en/sub-agents#write-subagent-files)]
* Subagent memory is now tied to the auto-memory feature: turning off auto memory (`autoMemoryEnabled` or `CLAUDE_CODE_DISABLE_AUTO_MEMORY`) makes the subagent `memory` field a no-op. [[line 446](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/sub-agents.md?plain=1#L446)] [[Source](https://code.claude.com/docs/en/sub-agents#enable-persistent-memory)]
* Resuming a session with `claude --agent` now restores the agent's system prompt, tool restrictions, and model along with the conversation; if the named agent no longer exists, the session falls back to defaults with a warning. [[line 643](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/sub-agents.md?plain=1#L643)] [[Source](https://code.claude.com/docs/en/sub-agents#invoke-subagents-explicitly)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* New documented behavior: when you answer `AskUserQuestion` by typing free text, Claude Code relays it with neutral wording so Claude follows the instruction as written; new dedicated "AskUserQuestion tool behavior" section split out. [[lines 13](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/tools-reference.md?plain=1#L13), [104-112](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/tools-reference.md?plain=1#L104-L112)]
* New "Windows encoding and exit codes" section for PowerShell (v2.1.214+): `>`/`>>` redirection now writes UTF-8 on PowerShell 5.1, piped stdin to native commands is UTF-8 encoded, and exit code 1 from `where.exe`/`fc.exe`/`diff.exe` is treated as a valid negative result rather than a failure. [[lines 307-315](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/claude-code/tools-reference.md?plain=1#L307-L315)] [[Source](https://code.claude.com/docs/en/tools-reference#windows-encoding-and-exit-codes)]

-----

## API changes

### New Documents

#### [dreams](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/dreams.md) [[Source](https://platform.claude.com/docs/en/api/beta/dreams)]

Overview page for a new beta resource, the **Dreams API** (`/v1/dreams`), gated behind the `dreaming-2026-04-21` beta header. A "Dream" is an asynchronous memory-consolidation job: it reads an input memory store and/or a set of session transcripts, and writes consolidated memories into a new output memory store, letting an agent "sleep on" its accumulated session history to distill it into durable memories. The page documents the `BetaDream` object (`id`, `status` lifecycle of `pending`/`running`/`completed`/`failed`/`canceled`, `inputs`, `outputs`, `model`, `usage`, `error`) and notes the feature is explicitly in "research preview." It ties into the broader "agent memory" feature set alongside the `memory_stores` resource and reuses the same `ModelConfig` shape as the Agents API.

#### [dreams/archive](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/dreams/archive.md) [[Source](https://platform.claude.com/docs/en/api/beta/dreams/archive)]

Documents `POST /v1/dreams/{dream_id}/archive`, which archives a Dream job (setting `archived_at`) so it's excluded from default `list` results unless `include_archived` is set.

#### [dreams/cancel](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/dreams/cancel.md) [[Source](https://platform.claude.com/docs/en/api/beta/dreams/cancel)]

Documents `POST /v1/dreams/{dream_id}/cancel`, which stops a pending or running Dream job, transitioning it to `canceled` status.

#### [dreams/create](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/dreams/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/dreams/create)]

Documents `POST /v1/dreams`, which starts a Dream job. The request body takes `inputs` (either a `memory_store` reference the dream reads without mutating, or a `sessions` reference listing `session_ids` whose transcripts feed the consolidation), an optional `instructions` string, and a `model`. The response is a `BetaDream` object beginning in `pending` status.

#### [dreams/list](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/dreams/list.md) [[Source](https://platform.claude.com/docs/en/api/beta/dreams/list)]

Documents `GET /v1/dreams`, which lists Dream jobs with pagination and filtering by `created_at[gt]`/`created_at[lt]`, `statuses`, and `include_archived`.

#### [dreams/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/dreams/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/beta/dreams/retrieve)]

Documents `GET /v1/dreams/{dream_id}`, returning the full `BetaDream` object for a single job, including cumulative `usage` and `error` detail if the job failed.

#### [thinking](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/build-with-claude/thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking)]

New primary "Thinking" overview page, largely superseding the old `extended-thinking.md` page (which lost ~760 lines in this same commit and is now a legacy/migration reference). Explains the modern **adaptive thinking** model (`thinking: {"type": "adaptive"}`), where Claude decides whether and how deeply to reason, versus the older manual `budget_tokens` scheme. Covers the `display` field (`"summarized"` vs `"omitted"`, with per-model defaults), thinking + tool-use rules, interleaved thinking, thinking-block preservation/caching per model, `redacted_thinking` blocks, and thinking encryption via the `signature` field.

#### [thinking-steering-and-cost](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/build-with-claude/thinking-steering-and-cost.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking-steering-and-cost)]

New page on steering adaptive thinking via `output_config.effort` (`max`/`xhigh`/`high`/`medium`/`low`) plus prompt-based steering as a secondary lever. Also covers cost mechanics: `max_tokens` as the hard cap covering thinking + text combined, how effort/thinking-config changes invalidate prompt caching, and `usage.output_tokens_details.thinking_tokens` for billed reasoning-token counts.

#### [thinking-tool-workflows](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/build-with-claude/thinking-tool-workflows.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking-tool-workflows)]

New page with a complete, runnable two-turn tool-use walkthrough with thinking enabled, showing how to echo the assistant's `thinking` + `tool_use` content blocks back unmodified when submitting a `tool_result`, and how interleaved thinking changes where reasoning appears between chained tool calls.

#### [thinking-troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/build-with-claude/thinking-troubleshooting.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking-troubleshooting)]

New symptom-to-fix reference for thinking-related errors: a per-model table of which `thinking.type` values are supported/default/rejected, plus fixes for common 400 errors, empty `thinking` fields, missing thinking blocks under adaptive mode, `stop_reason: "max_tokens"` truncation, and cache-hit drops after changing thinking/effort settings.

### Changed documents

#### [use-case-guides/content-moderation](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/about-claude/use-case-guides/content-moderation.md) [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/content-moderation)]

* Code examples no longer set `temperature=0`; that guidance was dropped from all four sample functions. [[lines 151-161](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/about-claude/use-case-guides/content-moderation.md?plain=1#L151-L161)] [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/content-moderation)]
* Response parsing changed from `response.content[0].text` to a pattern that finds the text block explicitly, accounting for other block types like thinking. [[line 161](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/about-claude/use-case-guides/content-moderation.md?plain=1#L161)] [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/content-moderation)]
* Code samples now show multi-language tabs (Python/TypeScript/C#/Go/Java/PHP/Ruby) instead of Python-only. [[line 42](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/about-claude/use-case-guides/content-moderation.md?plain=1#L42)] [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/content-moderation)]

#### [use-case-guides/customer-support-chat](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/about-claude/use-case-guides/customer-support-chat.md) [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/customer-support-chat)]

* Removed the note recommending the Claude Console's Evaluation tool for testing prompts. [[lines 552-554](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/about-claude/use-case-guides/customer-support-chat.md?plain=1#L552-L554)] [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/customer-support-chat)]
* ChatBot walkthrough is now generalized/multi-language: added language tabs, and clarifies the Streamlit UI section is Python-only while the ChatBot class can be ported to any language. [[lines 394-500](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/about-claude/use-case-guides/customer-support-chat.md?plain=1#L394-L500)] [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/customer-support-chat)]

#### [use-case-guides/ticket-routing](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/about-claude/use-case-guides/ticket-routing.md) [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/ticket-routing)]

* The recommendation to use the Claude Console's "prompt generator" tool was replaced with a pointer to the metaprompt recipe from the Claude Cookbook. [[line 137](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/about-claude/use-case-guides/ticket-routing.md?plain=1#L137)] [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/ticket-routing)]

#### [tool-use/computer-use-tool](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]

* "Extended thinking" cross-reference renamed to "Thinking," now pointing to the new `build-with-claude/thinking.md` page. [[line 290](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md?plain=1#L290)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]

#### [tool-use/define-tools](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/agents-and-tools/tool-use/define-tools.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)]

* References to "extended thinking" updated to "thinking," pointing to the new `build-with-claude/thinking.md` page; `tool_choice: any/tool` with thinking now documented to result in an error. [[lines 20](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/agents-and-tools/tool-use/define-tools.md?plain=1#L20), [197](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/agents-and-tools/tool-use/define-tools.md?plain=1#L197)]

#### [tool-use/tool-use-with-prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/agents-and-tools/tool-use/tool-use-with-prompt-caching.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)]

* Cache-invalidation table entry expanded: changing thinking parameters now always invalidates the messages cache, and on models that render thinking config ahead of tools/system prompt, it also invalidates the tool and system caches. [[line 66](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/agents-and-tools/tool-use/tool-use-with-prompt-caching.md?plain=1#L66)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)]
* New table row: changing `output_config.effort` has the same cache-invalidation behavior as thinking parameters; explicitly setting the model's default effort is equivalent to omitting it. [[line 67](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/agents-and-tools/tool-use/tool-use-with-prompt-caching.md?plain=1#L67)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)]

#### [tool-use/troubleshooting-tool-use](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/agents-and-tools/tool-use/troubleshooting-tool-use.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)]

* "Every request is a cache miss" row now also lists variation in thinking configuration or `output_config.effort` as likely causes, with a new link to "Thinking and prompt caching." [[line 35](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/agents-and-tools/tool-use/troubleshooting-tool-use.md?plain=1#L35)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)]

#### [beta](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* New `"dreaming-2026-04-21"` beta header added to the `AnthropicBeta` enum. [[line 77](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta.md?plain=1#L77)] [[Source](https://platform.claude.com/docs/en/api/beta)]
* New **BetaDreams** endpoint group added: create/list/get/cancel/archive a Dream — a wholly new managed-agents resource. [[lines 789-807](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta.md?plain=1#L789-L807)] [[Source](https://platform.claude.com/docs/en/api/beta)]
* Seven new webhook `data.type` values added: `environment.archived/created/deleted/updated` and `memory_store.archived/created/deleted` — new "Environment" and "Memory Store" resources with lifecycle webhooks. [[lines 874-880](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta.md?plain=1#L874-L880)] [[Source](https://platform.claude.com/docs/en/api/beta)]

#### [beta/agents](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/agents.md) [[Source](https://platform.claude.com/docs/en/api/beta/agents)]

* New `effort` field added to `BetaManagedAgentsModelConfig`: sets `output_config.effort` (low/medium/high/xhigh/max) applied to every Messages call the agent's session makes. [[line 141](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/agents.md?plain=1#L141)] [[Source](https://platform.claude.com/docs/en/api/beta/agents)]
* New `effort` field added to `BetaManagedAgentsModelConfigParams` (create/update variant): accepts a bare level string or `{"type": "high"}` object. [[line 1723](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/agents.md?plain=1#L1723)] [[Source](https://platform.claude.com/docs/en/api/beta/agents)]

#### [beta/agents/archive](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/agents/archive.md) [[Source](https://platform.claude.com/docs/en/api/beta/agents/archive)]

* Adds the new `effort` field to `BetaManagedAgentsModelConfig`. [[line 207](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/agents/archive.md?plain=1#L207)] [[Source](https://platform.claude.com/docs/en/api/beta/agents/archive)]

#### [beta/agents/create](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/agents/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/agents/create)]

* New `effort` parameter added to the create-agent `model` body param (bare level string or `{type}` object; omitting resolves per-model default). [[lines 248-251](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/agents/create.md?plain=1#L248-L251)] [[Source](https://platform.claude.com/docs/en/api/beta/agents/create)]
* Response schema/examples now show `model.effort` alongside `model.speed`. [[lines 1132-1135](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/agents/create.md?plain=1#L1132-L1135)] [[Source](https://platform.claude.com/docs/en/api/beta/agents/create)]

#### [beta/agents/list](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/agents/list.md) [[Source](https://platform.claude.com/docs/en/api/beta/agents/list)]

* Adds the new `effort` field to `BetaManagedAgentsModelConfig`. [[line 225](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/agents/list.md?plain=1#L225)] [[Source](https://platform.claude.com/docs/en/api/beta/agents/list)]

#### [beta/agents/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/agents/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/beta/agents/retrieve)]

* Adds the new `effort` field to `BetaManagedAgentsModelConfig`. [[line 213](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/agents/retrieve.md?plain=1#L213)] [[Source](https://platform.claude.com/docs/en/api/beta/agents/retrieve)]

#### [beta/agents/update](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/agents/update.md) [[Source](https://platform.claude.com/docs/en/api/beta/agents/update)]

* **Schema change:** the top-level `version` body parameter (previously required, for optimistic-concurrency control) is now optional — update succeeds unconditionally if `version` is omitted, and only enforces the concurrency check when a version is supplied. [[lines 665-667](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/agents/update.md?plain=1#L665-L667)] [[Source](https://platform.claude.com/docs/en/api/beta/agents/update)]
* New `effort` parameter added to the update-agent `model` body param, with the same create/update semantics as agents/create. [[lines 276-279](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/agents/update.md?plain=1#L276-L279)] [[Source](https://platform.claude.com/docs/en/api/beta/agents/update)]

#### [beta/agents/versions/list](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/agents/versions/list.md) [[Source](https://platform.claude.com/docs/en/api/beta/agents/versions/list)]

* Adds the new `effort` field to `BetaManagedAgentsModelConfig`. [[line 217](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/agents/versions/list.md?plain=1#L217)] [[Source](https://platform.claude.com/docs/en/api/beta/agents/versions/list)]

#### [beta/environments/work](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/environments/work.md) [[Source](https://platform.claude.com/docs/en/api/beta/environments/work)]

* Adds new `secret` field to `BetaSelfHostedWork`: credential payload used by the environment worker to execute the work item, populated only when polling for work. [[line 93](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/environments/work.md?plain=1#L93)] [[Source](https://platform.claude.com/docs/en/api/beta/environments/work)]

#### [beta/environments/work/ack](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/environments/work/ack.md) [[Source](https://platform.claude.com/docs/en/api/beta/environments/work/ack)]

* Adds the new `secret` field to `BetaSelfHostedWork`. [[line 151](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/environments/work/ack.md?plain=1#L151)] [[Source](https://platform.claude.com/docs/en/api/beta/environments/work/ack)]

#### [beta/environments/work/list](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/environments/work/list.md) [[Source](https://platform.claude.com/docs/en/api/beta/environments/work/list)]

* Adds the new `secret` field to `BetaSelfHostedWork`. [[line 161](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/environments/work/list.md?plain=1#L161)] [[Source](https://platform.claude.com/docs/en/api/beta/environments/work/list)]

#### [beta/environments/work/poll](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/environments/work/poll.md) [[Source](https://platform.claude.com/docs/en/api/beta/environments/work/poll)]

* Adds the new `secret` field to `BetaSelfHostedWork`. [[line 163](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/environments/work/poll.md?plain=1#L163)] [[Source](https://platform.claude.com/docs/en/api/beta/environments/work/poll)]

#### [beta/environments/work/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/environments/work/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/beta/environments/work/retrieve)]

* Adds the new `secret` field to `BetaSelfHostedWork`. [[line 151](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/environments/work/retrieve.md?plain=1#L151)] [[Source](https://platform.claude.com/docs/en/api/beta/environments/work/retrieve)]

#### [beta/environments/work/stop](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/environments/work/stop.md) [[Source](https://platform.claude.com/docs/en/api/beta/environments/work/stop)]

* Adds the new `secret` field to `BetaSelfHostedWork`. [[line 157](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/environments/work/stop.md?plain=1#L157)] [[Source](https://platform.claude.com/docs/en/api/beta/environments/work/stop)]

#### [beta/environments/work/update](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/environments/work/update.md) [[Source](https://platform.claude.com/docs/en/api/beta/environments/work/update)]

* Adds the new `secret` field to `BetaSelfHostedWork`. [[line 157](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/environments/work/update.md?plain=1#L157)] [[Source](https://platform.claude.com/docs/en/api/beta/environments/work/update)]

#### [beta/messages](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/messages.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages)]

* New refusal `category` value `"general_harms"` added, with explanatory text now added for every category (`cyber`, `bio`, `frontier_llm`, `reasoning_extraction`, `general_harms`). [[line 3698](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/messages.md?plain=1#L3698)] [[Source](https://platform.claude.com/docs/en/api/beta/messages)]
* `speed` field description filled in/clarified: "fast" now documented as premium-priced and rejecting invalid model/speed combinations at create time. [[line 9106](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/messages.md?plain=1#L9106)] [[Source](https://platform.claude.com/docs/en/api/beta/messages)]
* `BetaFallbackParam` doc note reworded: override fields on a fallback entry now "set the corresponding parameter" rather than strictly "replace" the top-level field. [[lines 8957-8960](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/messages.md?plain=1#L8957-L8960)] [[Source](https://platform.claude.com/docs/en/api/beta/messages)]

#### [beta/messages/batches](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/messages/batches.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/batches)]

* New refusal `category` value `"general_harms"` added with descriptive text for all category values. [[line 1654](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/messages/batches.md?plain=1#L1654)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/batches)]
* `speed` field description filled in/clarified. [[line 2562](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/messages/batches.md?plain=1#L2562)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/batches)]

#### [beta/messages/batches/results](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/messages/batches/results.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/batches/results)]

* New refusal category `"general_harms"` added to the `category` enum, plus explanatory descriptions added for all existing categories. [[line 1490](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/messages/batches/results.md?plain=1#L1490)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/batches/results)]
* `speed` field description changed from a short blurb to a fuller explanation noting premium pricing and rejected invalid model/speed combinations. [[line 2398](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/messages/batches/results.md?plain=1#L2398)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/batches/results)]

#### [beta/messages/count_tokens](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/messages/count_tokens.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/count_tokens)]

* `speed` field description updated with the same premium-pricing/rejected-combinations wording. [[line 4145](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/messages/count_tokens.md?plain=1#L4145)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/count_tokens)]

#### [beta/messages/create](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]

* `speed` request param description filled in with premium-pricing/rejection wording. [[line 4315](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/messages/create.md?plain=1#L4315)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]
* New refusal `category` value `"general_harms"` added with descriptions for all values. [[line 8420](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/messages/create.md?plain=1#L8420)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]

#### [beta/sessions](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions)]

* New `effort` field added to `BetaManagedAgentsModelConfigParams` used for session model overrides, and to the response-side `BetaManagedAgentsModelConfig` for session/subagent model blocks. [[lines 257](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions.md?plain=1#L257), [1041](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions.md?plain=1#L1041)]

#### [beta/sessions/archive](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/archive.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions/archive)]

* New `effort` field added to `model` config (request and response shapes), with response examples now showing `model.effort: {"type": "low"}` for both the top-level agent and subagents. [[lines 205, 367](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/archive.md?plain=1#L205)]

#### [beta/sessions/create](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions/create)]

* **New capability:** `initial_events` array parameter — lets a session-create call seed up to 50 initial events processed in order, supporting `user.message` (text/image/document content) and `user.define_outcome` (task description + rubric, inline or file reference). [[lines 655-869](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/create.md?plain=1#L655-L869)] [[Source](https://platform.claude.com/docs/en/api/beta/sessions/create)]
* Within `initial_events`, `user.define_outcome` supports `max_iterations` (default 3, max 20) controlling eval→revision cycles before giving up. [[lines 869-871](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/create.md?plain=1#L869-L871)] [[Source](https://platform.claude.com/docs/en/api/beta/sessions/create)]
* New `effort` field added to `model`/`model_config` params. [[line 305](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/create.md?plain=1#L305)] [[Source](https://platform.claude.com/docs/en/api/beta/sessions/create)]

#### [beta/sessions/events](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/events.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions/events)]

* `BetaManagedAgentsSessionRetriesExhausted` description reworded to decouple this stop reason from `max_iterations`: now purely "repeated errors exhausted the retry budget," a distinct terminal condition from outcome-eval exhaustion. [[line 5435](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/events.md?plain=1#L5435)] [[Source](https://platform.claude.com/docs/en/api/beta/sessions/events)]
* New `effort` field added to `model` config in event payloads. [[line 6217](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/events.md?plain=1#L6217)] [[Source](https://platform.claude.com/docs/en/api/beta/sessions/events)]

#### [beta/sessions/events/list](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/events/list.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions/events/list)]

* `retries_exhausted` description reworded (same decoupling from `max_iterations`), and new `effort` field added to `model` config. [[lines 2042, 2827](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/events/list.md?plain=1#L2042)]

#### [beta/sessions/events/stream](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/events/stream.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions/events/stream)]

* `retries_exhausted` description reworded, and new `effort` field added to `model` config. [[lines 2014, 2799](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/events/stream.md?plain=1#L2014)]

#### [beta/sessions/list](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/list.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions/list)]

* New `effort` field added to `model` config (request/response shapes), and list response examples now include `model.effort` for sessions and subagents. [[lines 275, 1235-1238](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/list.md?plain=1#L275)]

#### [beta/sessions/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions/retrieve)]

* New `effort` field added to `model` config, with retrieve response examples now including `model.effort`. [[lines 205, 1155-1158](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/retrieve.md?plain=1#L205)]

#### [beta/sessions/threads](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/threads.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions/threads)]

* `retries_exhausted` description reworded (decoupled from `max_iterations`), and new `effort` field added to `model` config. [[lines 2481, 133](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/threads.md?plain=1#L2481)]

#### [beta/sessions/threads/events/list](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/threads/events/list.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions/threads/events/list)]

* `retries_exhausted` description reworded, and new `effort` field added to `model` config. [[lines 2012, 2797](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/threads/events/list.md?plain=1#L2012)]

#### [beta/sessions/threads/events/stream](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/threads/events/stream.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions/threads/events/stream)]

* **New capability:** new query parameter `event_deltas` opts a thread-level SSE stream into best-effort streaming preview deltas (`event_start`, `event_delta`) before the final event arrives, for `agent.message` (incremental content fragments) and `agent.thinking` (start-only signal). Mirrors a capability already present on the session-level stream endpoint but new for the thread-level endpoint. [[lines 21-30](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/threads/events/stream.md?plain=1#L21-L30)] [[Source](https://platform.claude.com/docs/en/api/beta/sessions/threads/events/stream)]
* Corresponding new `event_start`/`event_delta` SSE event schemas documented, gated on the `event_deltas` opt-in. [[lines 3499-3536](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/threads/events/stream.md?plain=1#L3499-L3536)] [[Source](https://platform.claude.com/docs/en/api/beta/sessions/threads/events/stream)]

#### [beta/sessions/threads/list](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/threads/list.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions/threads/list)]

* New `effort` field added to `model` config, with thread list response examples now showing `model.effort`. [[line 217](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/threads/list.md?plain=1#L217)] [[Source](https://platform.claude.com/docs/en/api/beta/sessions/threads/list)]

#### [beta/sessions/threads/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/threads/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve)]

* New `effort` field added to `model` config, with response examples now showing `model.effort`. [[line 209](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/threads/retrieve.md?plain=1#L209)] [[Source](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve)]

#### [beta/sessions/update](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/update.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions/update)]

* New `effort` field added to `model` config for session updates (request/response shapes), with update response examples now including `model.effort`. [[lines 461, 1412-1415, 1431-1434](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/sessions/update.md?plain=1#L461)]

#### [beta/webhooks](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/webhooks.md) [[Source](https://platform.claude.com/docs/en/api/beta/webhooks)]

* Seven new webhook event data schemas added, corresponding to two new webhook-emitting resources: `BetaWebhookEnvironmentCreatedEventData`/`UpdatedEventData`/`ArchivedEventData`/`DeletedEventData`, and `BetaWebhookMemoryStoreCreatedEventData`/`ArchivedEventData`/`DeletedEventData`. [[lines 253-943](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/webhooks.md?plain=1#L253-L943)] [[Source](https://platform.claude.com/docs/en/api/beta/webhooks)]
* `BetaWebhookEventData` discriminated union grew from "33 more" to "40 more" member types to accommodate the new environment/memory-store event data variants. [[line 953](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/api/beta/webhooks.md?plain=1#L953)] [[Source](https://platform.claude.com/docs/en/api/beta/webhooks)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/errors.md) [[Source](https://platform.claude.com/docs/en/errors)]

* Claude Sonnet 5 added to the list of models that reject assistant-message prefill. [[line 141](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/errors.md?plain=1#L141)] [[Source](https://platform.claude.com/docs/en/errors)]
* Three new error sections added: "Extended thinking not supported" (Opus 4.7/4.8, Sonnet 5, Fable 5, Mythos 5 reject `thinking.type.enabled`), "Adaptive thinking not supported" (older models reject `thinking.type.adaptive`), and "Thinking cannot be disabled" (Fable 5/Mythos 5 reject `thinking.type.disabled`). [[line 169](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/errors.md?plain=1#L169)] [[Source](https://platform.claude.com/docs/en/errors)]

#### [messages](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/messages.md) [[Source](https://platform.claude.com/docs/en/messages)]

* New refusal category `"general_harms"` added alongside `cyber`/`bio`/`frontier_llm`/`reasoning_extraction`, each now with a one-line explanation. [[line 7247](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/messages.md?plain=1#L7247)] [[Source](https://platform.claude.com/docs/en/messages)]

#### [messages/batches](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/messages/batches.md) [[Source](https://platform.claude.com/docs/en/messages/batches)]

* Same new `"general_harms"` refusal category addition. [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/messages/batches.md?plain=1#L11)] [[Source](https://platform.claude.com/docs/en/messages/batches)]

#### [messages/batches/results](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/messages/batches/results.md) [[Source](https://platform.claude.com/docs/en/messages/batches/results)]

* Same `"general_harms"` category addition. [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/messages/batches/results.md?plain=1#L11)] [[Source](https://platform.claude.com/docs/en/messages/batches/results)]

#### [messages/create](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/messages/create.md) [[Source](https://platform.claude.com/docs/en/messages/create)]

* Same `"general_harms"` category addition. [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/messages/create.md?plain=1#L11)] [[Source](https://platform.claude.com/docs/en/messages/create)]

#### [models/list](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/models/list.md) [[Source](https://platform.claude.com/docs/en/models/list)]

* New beta feature id `"dreaming-2026-04-21"` added to the model capabilities/features enum. [[line 111](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/models/list.md?plain=1#L111)] [[Source](https://platform.claude.com/docs/en/models/list)]

#### [models/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/models/retrieve.md) [[Source](https://platform.claude.com/docs/en/models/retrieve)]

* Same new `"dreaming-2026-04-21"` feature id added. [[line 95](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/models/retrieve.md?plain=1#L95)] [[Source](https://platform.claude.com/docs/en/models/retrieve)]

#### [build-with-claude/context-windows](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/build-with-claude/context-windows.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]

* New detail: Claude Haiku 4.5 does **not** support interleaved thinking (previously only Opus 4.5/Sonnet 4.5/earlier Claude 4 models were said to need the beta header; now explicitly excludes Haiku 4.5). [[line 96](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/build-with-claude/context-windows.md?plain=1#L96)] [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]

#### [build-with-claude/effort](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/build-with-claude/effort.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]

* Effort parameter availability walked back from "all supported models" to "the following models," and a new note explains `xhigh` is a newer effort level that some `max`-supporting models don't support. [[lines 11, 50](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/build-with-claude/effort.md?plain=1#L11)]
* The detailed per-model effort/thinking-mode breakdown was removed and replaced by a pointer to the new thinking docs; Opus 4.5 is now called out as "the only extended-thinking-only model that supports effort." [[line 165](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/build-with-claude/effort.md?plain=1#L165)] [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]
* New best practice: changing `effort` between requests invalidates prompt caching, so effort should be held constant within a cached conversation. [[line 175](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/build-with-claude/effort.md?plain=1#L175)] [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]

#### [build-with-claude/extended-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Page heavily trimmed (~760 lines removed): the old supported-models table, "how it works," and best-practices sections were deleted, with the content moved to the new `thinking.md`, `thinking-steering-and-cost.md`, and `thinking-tool-workflows.md` pages. The page is now scoped to legacy manual/extended thinking (`budget_tokens`), explicitly noted as deprecated (but functional) on Opus 4.6/Sonnet 4.6 and rejected with a 400 on Opus 4.7/4.8, Sonnet 5, Fable 5, and Mythos 5. A new "Migrating to adaptive thinking" section with a before/after config example was added. [[line 13](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L13)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

#### [build-with-claude/overview](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/build-with-claude/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

* The features table's "Extended thinking" row was replaced with a "Thinking" row, and adaptive thinking is now listed as the only thinking mode on Sonnet 5, Fable 5, and Mythos 5, in addition to Opus 4.7/4.8. [[lines 45, 55](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/build-with-claude/overview.md?plain=1#L45)]

#### [build-with-claude/prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* Cache-invalidation table updated: "Thinking parameters" now shows "Model-specific" invalidation, and a new row documents that changing `output_config.effort` always invalidates message-block caching. [[lines 336-337](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L336-L337)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]
* Troubleshooting checklist and cache pre-warming guidance both now call out keeping thinking configuration and effort consistent across calls. [[lines 470, 574](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L470)]

#### [build-with-claude/prompt-engineering/overview](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/build-with-claude/prompt-engineering/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)]

* The "Prompt generator" link (Claude Console dashboard tool) was replaced with a "Prompt generator notebook" pointing to the Cookbook's metaprompt Colab notebook, and the reference to Console prompting tools was removed. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/build-with-claude/prompt-engineering/overview.md?plain=1#L19)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)]

#### [cli-sdks-libraries/libraries/apple-foundation-models](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/cli-sdks-libraries/libraries/apple-foundation-models.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/apple-foundation-models)]

* Sample code updated to use `.sonnet5` instead of `.sonnet4_6` as the recommended default model throughout the guide. [[line 57](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/cli-sdks-libraries/libraries/apple-foundation-models.md?plain=1#L57)] [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/apple-foundation-models)]

#### [cli-sdks-libraries/sdks/java](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/cli-sdks-libraries/sdks/java.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/java)]

* Java SDK version bumped from 2.48.0 to 2.50.0 in the Maven install snippet. [[line 24](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/cli-sdks-libraries/sdks/java.md?plain=1#L24)] [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/java)]

#### [manage-claude/api-and-data-retention](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/manage-claude/api-and-data-retention.md) [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

* "Extended thinking" row removed from the ZDR/HIPAA eligibility table and replaced with a "Thinking" row, still Yes/Yes eligible. [[line 207](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/manage-claude/api-and-data-retention.md?plain=1#L207)] [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

#### [manage-claude/cmek](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/manage-claude/cmek.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

* Expanded warning box on enabling CMEK: Anthropic keeps no key copy, misconfiguration causes permanent data loss, and a new requirement to verify Anthropic's identifier against published production identities before granting key access. [[line 21](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/manage-claude/cmek.md?plain=1#L21)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

#### [managed-agents/agent-setup](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/agent-setup.md) [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup)]

* Agent's `model` object now accepts an `effort` level, settable at agent creation; a per-session `model` override's `effort` is ignored. [[line 20](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/agent-setup.md?plain=1#L20)] [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup)]
* Updating an agent's `version` field is now optional: omitting it applies the update unconditionally (last write wins) instead of requiring an exact version match. [[line 99](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/agent-setup.md?plain=1#L99)] [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup)]

#### [managed-agents/cloud-sandboxes-reference](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/cloud-sandboxes-reference.md) [[Source](https://platform.claude.com/docs/en/managed-agents/cloud-sandboxes-reference)]

* Default sandbox networking changed: API-created environments now default to `unrestricted` networking, while Studio-provisioned sandboxes default to `limited` (previously simply "disabled by default"). [[line 73](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/cloud-sandboxes-reference.md?plain=1#L73)] [[Source](https://platform.claude.com/docs/en/managed-agents/cloud-sandboxes-reference)]

#### [managed-agents/define-outcomes](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/define-outcomes.md) [[Source](https://platform.claude.com/docs/en/managed-agents/define-outcomes)]

* New capability: an outcome can now be defined directly in the session-create request via a single `user.define_outcome` event in `initial_events`, instead of requiring a separate follow-up call. [[line 119](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/define-outcomes.md?plain=1#L119)] [[Source](https://platform.claude.com/docs/en/managed-agents/define-outcomes)]

#### [managed-agents/dreams](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/dreams.md) [[Source](https://platform.claude.com/docs/en/managed-agents/dreams)]

* Dream runtime guidance changed from "minutes to tens of minutes" to "minutes to a few hours," driven by the number of input transcripts. [[line 92](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/dreams.md?plain=1#L92)] [[Source](https://platform.claude.com/docs/en/managed-agents/dreams)]
* Clarified that the archiving/deletion guard while a dream is running applies only to the dream resource itself, not its input/output stores; `input_session_unavailable` now only fires on session deletion (not archival). [[line 149](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/dreams.md?plain=1#L149)] [[Source](https://platform.claude.com/docs/en/managed-agents/dreams)]

#### [managed-agents/events-and-streaming](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/events-and-streaming.md) [[Source](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)]

* `system.message` behavior changed: it now appends system-level context to subsequent turns rather than replacing the system prompt, and can no longer be sent while idle with `stop_reason: requires_action` unless it trails a tool-result event in the same request. [[lines 17, 418](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/events-and-streaming.md?plain=1#L17)]
* New capability: event-delta previews (`event_deltas[]`) now supported on session **thread** streams, not just the session-level stream; new "Preview session thread events" section added. [[lines 95, 217](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/events-and-streaming.md?plain=1#L95)]
* Usage reporting changed: `cache_creation_input_tokens` replaced by a `cache_creation` object broken down by cache lifetime (`ephemeral_5m_input_tokens`, `ephemeral_1h_input_tokens`). [[line 432](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/events-and-streaming.md?plain=1#L432)] [[Source](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)]

#### [managed-agents/files](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/files.md) [[Source](https://platform.claude.com/docs/en/managed-agents/files)]

* Max files per session increased from 100 to 500. [[line 72](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/files.md?plain=1#L72)] [[Source](https://platform.claude.com/docs/en/managed-agents/files)]
* `mount_path` semantics changed: the path is now rooted under the session's uploads directory (e.g. `/data.csv` → `/mnt/session/uploads/data.csv`) rather than being the exact path. [[line 143](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/files.md?plain=1#L143)] [[Source](https://platform.claude.com/docs/en/managed-agents/files)]

#### [managed-agents/mcp-connector](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/mcp-connector.md) [[Source](https://platform.claude.com/docs/en/managed-agents/mcp-connector)]

* MCP tool output overflow threshold changed from 100,000 tokens to 100,000 characters (~25,000 tokens) — a much lower effective limit. [[line 98](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/mcp-connector.md?plain=1#L98)] [[Source](https://platform.claude.com/docs/en/managed-agents/mcp-connector)]
* Credential URL matching now normalizes scheme/host case, default ports, and trailing slashes instead of requiring an exact match, and `mcp_authentication_failed_error` was broadened to also cover missing-credential and OAuth-refresh failures. [[lines 116, 125](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/mcp-connector.md?plain=1#L116)]

#### [managed-agents/multiagent-orchestration](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/multiagent-orchestration.md) [[Source](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration)]

* Behavior change: referencing an agent with its own `multiagent.agents` roster (depth > 1) now fails the create/update request with a validation error, instead of being silently ignored. [[line 66](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/multiagent-orchestration.md?plain=1#L66)] [[Source](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration)]

#### [managed-agents/reference](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/reference.md) [[Source](https://platform.claude.com/docs/en/managed-agents/reference)]

* `user.message` now supports image and document content, not just text. [[line 43](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/reference.md?plain=1#L43)] [[Source](https://platform.claude.com/docs/en/managed-agents/reference)]
* MCP servers that only support the deprecated SSE transport now work via automatic fallback (previously streamable HTTP was required). [[line 66](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/reference.md?plain=1#L66)] [[Source](https://platform.claude.com/docs/en/managed-agents/reference)]

#### [managed-agents/scheduled-deployments](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/scheduled-deployments.md) [[Source](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments)]

* Deployments now accept `user.define_outcome` (not just `user.message`) as the required initial event. [[line 20](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/scheduled-deployments.md?plain=1#L20)] [[Source](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments)]
* Scheduled-run jitter changed from "up to 10 seconds" to "up to 15% of the interval between runs, min 5s, max 9 minutes." [[line 68](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/scheduled-deployments.md?plain=1#L68)] [[Source](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments)]

#### [managed-agents/self-hosted-sandboxes](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/self-hosted-sandboxes.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

* Output location changed: self-hosted sandboxes no longer use `/mnt/session/outputs`; deliverables now land under the working directory, with the sample Dockerfile/spawn-script mounting `/workspace` instead. [[line 47](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L47)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]
* `ant` CLI version bumped from 1.17.0 to 1.19.0; custom-tool description length limit increased from 1,024 to 4,096 characters. [[lines 132, 503](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L132)]
* Self-hosted sandboxes now explicitly reject any session with a `resources` entry (broader restriction than the previous "memory not supported" note), and operations endpoints (`work.stats`, `work.stop`) now accept either the org API key or the environment key. [[lines 314, 515](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L314)]
* `work.stop` now defaults to a graceful async "stopping" transition confirmed by the worker's next lease heartbeat, rather than immediate in-flight-call draining; `force: true` still stops immediately. [[line 555](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L555)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

#### [managed-agents/session-operations](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/session-operations.md) [[Source](https://platform.claude.com/docs/en/managed-agents/session-operations)]

* `terminated` status now also occurs on normal completion, not just unrecoverable error. [[line 22](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/session-operations.md?plain=1#L22)] [[Source](https://platform.claude.com/docs/en/managed-agents/session-operations)]

#### [managed-agents/sessions](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/sessions.md) [[Source](https://platform.claude.com/docs/en/managed-agents/sessions)]

* New "Seed the session with initial events" section: `initial_events` (up to 50 `user.message`/`user.define_outcome` events) lets you create a session and start work in one call, entering `running` status immediately. [[line 43](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/sessions.md?plain=1#L43)] [[Source](https://platform.claude.com/docs/en/managed-agents/sessions)]
* New override rule: clearing `mcp_servers` now returns a 400 if `tools` still references one of its `mcp_toolset` entries. [[line 99](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/sessions.md?plain=1#L99)] [[Source](https://platform.claude.com/docs/en/managed-agents/sessions)]

#### [managed-agents/skills](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/skills.md) [[Source](https://platform.claude.com/docs/en/managed-agents/skills)]

* Skill `version` pinning (vs. `latest`) now applies to both Anthropic pre-built skills and custom skills, previously custom-only. [[line 53](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/skills.md?plain=1#L53)] [[Source](https://platform.claude.com/docs/en/managed-agents/skills)]

#### [managed-agents/tools](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/tools.md) [[Source](https://platform.claude.com/docs/en/managed-agents/tools)]

* Same tool-output overflow threshold change (100,000 tokens → 100,000 characters / ~25,000 tokens) as mcp-connector. [[line 30](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/tools.md?plain=1#L30)] [[Source](https://platform.claude.com/docs/en/managed-agents/tools)]

#### [managed-agents/webhooks](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/webhooks.md) [[Source](https://platform.claude.com/docs/en/managed-agents/webhooks)]

* New "Environment events" and "Memory store events" event types added to the webhook catalog. [[line 33](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/webhooks.md?plain=1#L33)] [[Source](https://platform.claude.com/docs/en/managed-agents/webhooks)]
* Signature headers changed from a single `X-Webhook-Signature` to `webhook-id`/`webhook-timestamp`/`webhook-signature`; event `id` format changed to a `whe_`-prefixed ID. [[line 66](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/webhooks.md?plain=1#L66)] [[Source](https://platform.claude.com/docs/en/managed-agents/webhooks)]
* Delivery/retry policy rewritten: now up to 3 attempts with jittered exponential backoff (5–120s), dropped after final failure with no durability guarantee; auto-disable now triggers on immediate 3xx/invalid-IP or "sustained" failure windows. [[line 139](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/managed-agents/webhooks.md?plain=1#L139)] [[Source](https://platform.claude.com/docs/en/managed-agents/webhooks)]

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* New "July 22, 2026" changelog entry added, summarizing agent `effort` config, environment/memory-store webhooks, session `initial_events`, optional agent `version` on update, and thread-level event deltas. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/2efbe9e6246276abcf3cfe07c882d021711b2eeb/docs-md/api/release-notes/overview.md?plain=1#L15)] [[Source](https://platform.claude.com/docs/en/release-notes/overview)]
