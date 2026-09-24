# [Claude docs changes for September 24th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/0b87af04c3075af6ebf58bbbac4604da969a0f4c) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/0b87af04c3075af6ebf58bbbac4604da969a0f4c)]

## Executive Summary
- The **Claude Opus 5.5 migration guide** was rewritten from a short pointer page into a full reference: a "what every request must satisfy" checklist (thinking is always adaptive, `tool_choice` can't force a tool, sampling params must stay default, no prefill, `computer_toolset_20260801` replaces the old computer-use tool) plus a dedicated section and checklist for each starting model (Opus 5, Opus 4.8, Opus 4.7, Opus 4.6 and earlier, Sonnet 5).
- Messages API responses gained a `tool_changes` field on `compaction` blocks: it lists the `tool_addition`/`tool_removal` entries a compacted range applied, so callers using the new inline-tool-definition and MCP-tool-pinning betas can tell what tool set was in effect after a compaction.
- Claude Code 2.1.281: `AGENTS.md` now loads in every session, including Amazon Bedrock and telemetry-disabled ones, without needing Anthropic's feature-flag fetch; **cloud sessions ("Claude Code on the web") moved from research preview to generally available**.
- 2.1.281 also fixes several silent-data-loss and reliability bugs around session resume (dropped reasoning after a changed re-sent turn, large sessions restoring only their last few messages, prompt-cache loss on MCP disconnect) and closes three security gaps: a macOS path check that could be bypassed via `/.vol`/`/.nofollow`/`/.resolve`, a permission rule with a NUL byte that silently matched everything, and an unprompted recursive `rm` when its target was pure command-substitution output.
- The web fetch tool now refuses to fetch a URL that looks like it contains a credential (an API key or password) unless that credential also appears in the system prompt or a user message, closing an exfiltration path.

-----

## New Claude Code versions

### [2.1.281](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/versions/2.1.281.md)

#### New features

* Added Claude apps gateway support for newer Claude Desktop keys in `desktop` policy blocks, including `blockReadsOutsideWorkingDirectories` and `disableBypassPermissionsMode`
* Added `assume_role` on Claude apps gateway Bedrock upstreams (call Bedrock as an assumed IAM role via STS, in another AWS account if needed) and `guardrail: {id, version}` to apply a Bedrock guardrail to every request through them
* Added `telemetry.resource_attributes` to the Claude apps gateway config, and MCP URL-mode elicitation on 2026-07-28 protocol connections so servers can open a browser-based confirmation flow
* Added `"attribution": false` in `settings.json` to hide all commit and PR attribution
* Added MCP server checks to `claude plugin validate`: it now reports `.mcp.json` entries that would be silently dropped at load, undeclared `${user_config.*}` references, and insecure URLs
* Added an auto mode recommendation to `/insights` estimating how many recent permission prompts auto mode could have handled
* Added a scrollbar to the `/skills`, `/mcp`, and `/plugin` Installed lists in fullscreen mode
* [VSCode] Added a Continue/Stop prompt when auto mode falls back to billed classifier requests, replacing an unanswerable warning line
* [Claude Code on the web] Added a Fast mode switch to the composer's model menu, and a "Troubleshoot GitHub connection" link on the repository pickers
* [Claude Tag] Added a line in the Slack thread naming who pressed Stop, with a reminder to mention @Claude to continue

#### Existing feature improvements

* Improved startup: managed settings/policy fetches no longer retry unrecoverable requests, and git reads, telemetry, and Bedrock/Vertex model-upgrade checks no longer block the first frame
* Improved resume time for long sessions that read many files, and for very long compacted sessions (notably via the Agent SDK and Claude Desktop)
* Improved "Prompt is too long" recovery: an oversized first prompt is now summarized on its own instead of being dropped from the summary
* Changed auto mode: read-only and sandboxed shell commands now also wait for server-side classifier review; `CLAUDE_CODE_AUTO_MODE_SERVER` now applies on a direct Anthropic API connection too; and a denial now covers the outcome, not just the exact command
* Improved the dangerous-`rm` check to catch a removal target built from a shell variable plus a top-level directory name, a working-directory-derived variable, or a backslash-only target; changed the confirmation prompt to wait 2 minutes then deny (configurable via `CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT`)
* Changed self-hosted runners to pass system prompts to Claude Code as private files instead of command-line text — a `command` hook using `--system-prompt`/`--append-system-prompt` must switch to the `-file` variants
* Improved `--agents` to accept a path to a JSON file (with `-p`) as well as inline JSON, and to allow an empty `prompt`
* Improved `/batch` to run wherever a `WorktreeCreate` hook provides the agent worktrees, not only inside a git repository
* Changed "send now" (Ctrl+Enter) to move running tools to the background instead of cancelling the turn
* Improved plugin hook-failure errors to name the offending plugin, and added a `claude plugin validate` warning for unquoted `${CLAUDE_PLUGIN_ROOT}` in a shell-form hook

#### Major bug fixes

* Fixed resumed sessions re-sending an earlier turn in a changed form (a parallel tool call, an MCP tool call still mid-reconnect, or an interrupted tool-search result), which could make the API drop prior reasoning
* Fixed resuming a very large session sometimes restoring only its last few messages, and a session resumed mid-permission-prompt after a restart sending a different history that broke the prompt cache
* Fixed resuming a session that ended during a tool call: Claude now sees the call and is told its outcome is unknown
* Fixed the prompt cache being lost when an MCP server disconnects mid-conversation, or is still connecting after a resume, while tool search is off
* Fixed responses cut short by a proxy/gateway that closes the stream cleanly being shown as complete with no warning, and tool calls running twice on duplicated stream events
* Fixed responses failing with "Content block not found" when a proxy drops a stream event mid-response
* Fixed `CLAUDE_CODE_RETRY_WATCHDOG` sessions failing on the first 5xx or dropped connection after a run of 429/529 waits
* Fixed conversations getting permanently stuck on "tool_use.name: String should have at most 200 characters" after the model called a tool by an overlong name
* Fixed `--input-format stream-json` sessions (Agent SDK, VS Code) and scheduled cloud sessions failing every turn when an earlier assistant message had plain-string content
* Fixed a crash ("unrecoverable interface error") that could end a session while an API request was being retried, and a turn retrying indefinitely (ignoring `--max-turns`) when the model alternated unparseable tool calls and truncation
* Fixed permission dialogs and attachment checks reading a macOS path under `/.vol`, `/.nofollow`, or `/.resolve` (which can reach a network mount) before approval
* Fixed a recursive `rm` whose target is only command-substitution output (e.g. `rm -rf "$(pwd)"`) running unprompted in auto and `--dangerously-skip-permissions` mode
* Fixed a permission rule containing a NUL byte being expanded into a wildcard match
* Fixed `claude --bg` starting a background session, and running its project hooks, in a directory that hadn't passed the workspace trust prompt
* Fixed `--setting-sources`/SDK `settingSources` not being forwarded to spawned sessions (teammates, `/bg`, `claude agents`, `--worktree --tmux`)
* Fixed Read, Write, Edit, and NotebookEdit ending the whole turn on a file path containing a null byte; they now fail just that tool call with a clear error
* Fixed CLAUDE.md and rules files from an `--add-dir` directory inside the working directory being sent to the model twice in headless and SDK sessions

-----

## Claude Code changes

### Changed documents

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)] / [cloud-environments](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/claude-code/cloud-environments.md) / [web-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/claude-code/web-quickstart.md)

* Cloud sessions moved from "research preview" to generally **available** on Pro, Max, and Team plans (and qualifying Enterprise seats). [[line 2 of each file](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L2)]

#### [claude-md](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/claude-code/claude-md.md) [[Source](https://code.claude.com/docs/en/claude-md)] / [memory](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/claude-code/memory.md)

* `AGENTS.md` reading no longer depends on a session that fetches feature flags from Anthropic: as of v2.1.281, sessions on Amazon Bedrock or with telemetry disabled read it directly like any other session; only a pre-v2.1.277 CLI or a disabled `agents-md` plugin still fall back to `CLAUDE.md`-only. [[lines 378-387, 550-557](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/claude-code/memory.md?plain=1#L378-L387)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Removed `AGENTS.md` reading from the list of things that need feature-flag fetching, matching the v2.1.281 fix above. [[line 504](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/claude-code/env-vars.md?plain=1#L504)] [[Source](https://code.claude.com/docs/en/env-vars#features-that-need-feature-flag-fetching)]

#### [feature-availability](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/claude-code/feature-availability.md) [[Source](https://code.claude.com/docs/en/feature-availability)]

* Removed the "CLAUDE.md memory" provider-difference row, since `AGENTS.md` no longer has provider-specific availability. [[line 30](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/claude-code/feature-availability.md?plain=1#L30)] [[Source](https://code.claude.com/docs/en/feature-availability#features-available-on-every-provider)]

#### [glossary](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/claude-code/glossary.md) [[Source](https://code.claude.com/docs/en/glossary)]

* Updated the `AGENTS.md` entry to drop the feature-flag-fetching caveat, matching the memory.md update. [[line 8](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/claude-code/glossary.md?plain=1#L8)] [[Source](https://code.claude.com/docs/en/glossary#a)]

-----

## API changes

### New Documents

#### [release-notes/system-prompts/claude-opus-5-5](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/api/release-notes/system-prompts/claude-opus-5-5.md) [[Source](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-opus-5-5)]

The core system prompt Anthropic ships for Claude Opus 5.5 on claude.ai and the mobile apps, dated September 22, 2026: product information Claude can share (available models, Mythos tier, other Claude surfaces), refusal handling, and child-safety instructions.

### Changed documents

#### [agents-and-tools/tool-use/tool-runner](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/api/agents-and-tools/tool-use/tool-runner.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner)]

* Java tool runner example reworked: tools are now defined as a `BetaRunnableTool` pairing an input class with a lambda that runs the tool and returns a `BetaToolResultBlockParam.Content`, replacing the earlier pattern of implementing `Supplier<String>` directly on the input class — needed so the lambda can close over application objects like a `WeatherService`. [[lines 343-404](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/api/agents-and-tools/tool-use/tool-runner.md?plain=1#L343-L404)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner#basic-usage)]

#### [agents-and-tools/tool-use/web-fetch-tool](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]

* New restriction: the tool now refuses a URL that appears to contain a credential (an API key or password) unless that credential also appears in the system prompt or a user message's text — a credential appearing only in a tool result doesn't count. Returns `url_not_allowed`. [[lines 22-30, 612, 630-637](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L630-L637)]

#### [build-with-claude/refusals-and-fallback](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/api/build-with-claude/refusals-and-fallback.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)]

* Documented that a fallback model drops Claude Opus 5.5's thinking blocks on refusal-triggered retries, except when falling back to Claude Fable 5.1 or Claude Mythos 5.1, which can read them. [[lines 1093, 1111](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/api/build-with-claude/refusals-and-fallback.md?plain=1#L1093)]

#### [build-with-claude/thinking-steering-and-cost](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/api/build-with-claude/thinking-steering-and-cost.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking-steering-and-cost)]

* Clarified that the effort-level default is `medium` on Claude Opus 5.5 specifically, versus `high` on other models, and updated the cache-invalidation example to change effort from that `medium` default down to `low` instead of from `high` to `medium`. [[lines 43-55, 202, 282, 376, 502, 575, 719, 814, 866](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/api/build-with-claude/thinking-steering-and-cost.md?plain=1#L43-L55)]

#### [manage-claude/compliance-content-data](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/api/manage-claude/compliance-content-data.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-content-data)]

* Clarified exactly when a chat reappears ahead of your saved export cursor during an `order_by=updated_at` walk: on a new message, a move into or out of a project, or a deletion — not on other edits such as a rename. [[lines 22, 61-64](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/api/manage-claude/compliance-content-data.md?plain=1#L61-L64)]

#### [manage-claude/compliance-sessions](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/api/manage-claude/compliance-sessions.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-sessions)]

* New guidance for monitoring connector (MCP) use in Claude Science transcripts: Claude Science calls connectors from code it runs through its `repl` tool rather than as separately named tools, so reviewers must parse the `repl` `tool_use` block's code (e.g. a `host.mcp(...)` call) instead of matching on a tool name as they would for Cowork or Claude Code sessions; recommends `tool_use_input_max_bytes=-1` for these sessions. [[lines 274-281](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/api/manage-claude/compliance-sessions.md?plain=1#L274-L281)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-sessions#retrieve-a-local-session-transcript)]

#### [manage-claude/spend-limits-api](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/api/manage-claude/spend-limits-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/spend-limits-api)]

* Changed behavior for a `denied` spend limit increase request: the member can now send a new request right away (only a `pending` request blocks a new one), replacing the previous 30-day cooldown on claude.ai's request button. [[line 75](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/api/manage-claude/spend-limits-api.md?plain=1#L75)] [[Source](https://platform.claude.com/docs/en/manage-claude/spend-limits-api#increase-request-lifecycle)]

#### [models/opus-5-5/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/api/models/opus-5-5/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide)]

* Rewritten from a short pointer page (~340 lines) into a full migration reference (~1,780 lines). New "What every request to Claude Opus 5.5 must satisfy" checklist: no `thinking: {type: "disabled"}` or manual budgets (adaptive-only), no forced `tool_choice` (`any`/`tool`), `temperature`/`top_p`/`top_k` must stay default, no prefilled assistant turn, and `computer_toolset_20260801` replaces `computer_20251124` on the Claude API and Google Cloud. Reorganized into one section per starting model — Opus 5, Opus 4.8, Opus 4.7, Opus 4.6 and earlier, and Sonnet 5 — each ending in its own checklist. [[lines 1-1142](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/api/models/opus-5-5/migration-guide.md?plain=1#L16-L350)] [[Source](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide#thinking-is-always-on-effort-is-the-control)]

#### Claude Opus 5.5 mechanical reference updates (well over 1,000 files, e.g. [api/beta/messages/create](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/api/api/beta/messages/create.md), [api/csharp/beta](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/api/api/csharp/beta.md), [models/opus-5/overview](https://github.com/gpambrozio/ClaudeDocs/blob/0b87af04c3075af6ebf58bbbac4604da969a0f4c/docs-md/api/models/opus-5/overview.md))

* Nearly every other changed file in today's diff is a mechanical, repeated edit: the `claude-opus-5-5` model ID and two new beta headers, `inline-tools-2026-09-15` (define or replace a tool's full definition in a mid-conversation message) and `mcp-client-2026-09-15` (pin an MCP server's fetched tool list), were added to the enum lists on every per-language, per-endpoint API reference page. On top of that, `messages/create` and its ~15 per-language/per-surface variants (Python, TypeScript, Go, Java, C#, PHP, Ruby, CLI, `beta`, `cli/beta`, ...) gained a `tool_changes` field on `compaction` blocks: an array of `tool_addition`/`tool_removal` entries (each a reference to a `tools` entry, an MCP tool/toolset, or a full `tool_definition`) recording which tools the compacted range added or removed, for callers using the two betas above. Every model overview page also had its pricing table reformatted (a footnote list replaced inline superscripts) and Claude Opus 5 was relabeled Legacy now that Opus 5.5 is current. None of these add information beyond what's already summarized above, so they aren't itemized file by file here.

-----
