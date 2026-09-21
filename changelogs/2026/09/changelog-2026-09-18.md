# [Claude docs changes for September 18th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/b2037be67c64dfa5a61aada9673680a81e4c95c0) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/b2037be67c64dfa5a61aada9673680a81e4c95c0)]

## Executive Summary
- **Projects land in public beta**: a 462-line new page for one ongoing conversation where Claude starts a cloud-session thread per task, all sharing the project's repositories, instructions and memory. Pro and Max only, rolling out gradually to accounts that have used cloud sessions
- Skills and plugins enabled on your claude.ai account now sync into terminal sessions signed in with it (2.1.275), and claude.ai can list marketplaces — such as an organization plugin library — that you add by name with `claude plugin marketplace add --claudeai`
- New `startup_failure_reason` on SDK results, with a table of sixteen values naming exactly why Claude Code refused to start, so an application can offer the fix instead of retrying
- A send-now key (`ctrl+enter`) interrupts the current turn and sends all queued messages at once, with sent and queued messages shown in gray until the model receives them
- `/plugin install <plugin> --marketplace <source>` adds a marketplace and installs from it in one step, asking you to confirm the resolved source first

## New Claude Code versions

### [2.1.275](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/versions/2.1.275.md)

#### New features

* Added syncing of the skills and plugins enabled on your claude.ai account to terminal sessions signed in with it; opt out with `syncClaudeAiSkills: false` or `syncClaudeAiPlugins: false`
* Added a send-now key (`ctrl+enter`, or `ctrl+x ctrl+s`) that interrupts the current turn and sends all queued messages at once
* Added `/plugin install <plugin> --marketplace <source>`, which offers to add the marketplace before installing
* Added the signed-in account to Claude apps gateway sign-in: when the gateway names it, you confirm it before the credential is saved, and `/status` shows it
* Added a startup warning when a configured `otelHeadersHelper` fails, so sessions that silently export no telemetry are noticed

#### Existing feature improvements

* Improved prompt caching for a `--system-prompt` containing a `__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__` line: the text above it is now cached globally
* Improved the Artifact tool's publish and read results to say who can open the page and what the owner's Share menu offers
* Improved artifact publish results: they name the tab icon sent, warn when the page contains a NUL byte, and retry a flaky fetch of a newer page after a stale publish
* Improved the `/desktop` error when Claude Desktop doesn't open

#### Major bug fixes

* Fixed a whole family of resume crashes and hangs on malformed transcripts: a malformed task-reminder or @-file attachment entry, a malformed message entry, and a malformed message content block each used to break `--resume`, the resume picker preview, resumed background agents and the transcript view
* Fixed `/rewind` in a forked or background session restoring a **zero-filled or truncated file** when the session's file-history backups couldn't be fully copied
* Fixed plugin and marketplace messages, logs and `claude plugin marketplace list` showing a password or token stored in a git, ssh or marketplace URL
* Fixed `claude plugin marketplace update` deleting a GitHub marketplace's local copy when the fetch failed and the marketplace was named after its repository
* Fixed sandboxed Bash commands on Linux reporting exit code 0 for failed commands when the shell is zsh
* Fixed sandboxed Bash commands being unable to write to project directories named `hooks/` or `config/`
* Fixed Grep, Glob and @-file suggestions hanging or running out of memory on searches over the 20MB output cap
* Fixed a restored memory file's age note changing between requests after a compaction or resume, causing prompt cache misses
* Fixed `--resume` and `--continue` dropping earlier thinking when a built-in tool the session started with has since been switched off server-side
* Fixed `/update-config` writing `Write(path)` permission rules, which file permission checks don't match, instead of `Edit(path)` rules
* Fixed `SubagentStop` hooks with a specific `matcher` firing for every stopping subagent whose agent type was empty
* Fixed a terminal `API Error: 400` on every turn behind a network gateway that rewrites API error responses when a beta request header is rejected
* Fixed a crash at launch when `~/.claude.json` holds a malformed `mcpNeedsAuthNoticed` value

### [2.1.276](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/versions/2.1.276.md)

* Bug fixes and reliability improvements

-----

## Claude Code changes

### New Documents

#### [claude-projects](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/claude-code/claude-projects.md) [[Source](https://code.claude.com/docs/en/claude-projects)]

Projects, in public beta on Pro and Max, rolling out gradually **starting with accounts that have used cloud sessions and don't already have projects in claude.ai chat or Cowork** — not on Team or Enterprise yet, with a waitlist if the rollout hasn't reached you.

A project is one ongoing conversation in which Claude coordinates a stream of related work. Each task becomes a **thread**, and each thread is a cloud session running in parallel that keeps going after you close the laptop. The page frames it against doing the coordinating yourself:

* **Send work to one place**: paste a bug report, stack trace or task list into the conversation, and Claude either starts a thread or passes it to the thread already working in that area, answering quick questions in place.
* **Set context once**: every new thread starts with the project's repositories, instructions and memory, so a rule stated once — such as which branch to target — reaches all of them.
* **Come back to finished work**: the **Overview** pane shows which threads finished, which pull requests are ready, and which thread is waiting on you.

Its twenty-odd sections cover creating a project from scratch or from an existing cloud session, GitHub access, reviewing a thread's pull request, opening a thread when you need direct control, choosing models and letting Claude manage context, unblocking a thread waiting on approval, writing project instructions, deciding which repositories to add, getting skills, plugins, connectors and tools into threads, and a full settings reference.

Two details worth flagging: project settings are changed at claude.ai/code or in the desktop app, **not in `settings.json`**; and changes to instructions, repositories, plugins and environment reach **new** threads only, not ones already running. **Pause** stops everything at once — running threads, the conversation, new threads and routines — until you resume.

### Changed documents

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* New `startup_failure_reason` field with a sixteen-value enum naming exactly why Claude Code refused to start — "so your application can offer the fix instead of a retry". The values run from `org_pin_api_key_conflict` and `org_pin_mismatch` through `proxy_invalid`, `temp_dir_unusable`, `cwd_unavailable`, `shell_tool_missing`, `worktree_resume_refused` and `cli_version_too_old` to `bypass_root`, each with a table row explaining what stopped the session. Requires Agent SDK v0.3.274. [[lines 1416-1464](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1416-L1464)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#startup_failure_reason)]
* By default the result is written only for three specific failures — the two worktree refusals and a refused `continue` of a background-held conversation. **Set `CLAUDE_CODE_STARTUP_FAILURE_RESULTS=1` to get it for every value**; otherwise the rest end with stderr output, a non-zero exit, and no result message at all. [[lines 1420-1423](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1420-L1423)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#startup_failure_reason)]
* New `mcpServer` field on `mcp__*` tool entries naming the server that serves the tool and where its definition came from, plus a `source` field on each `mcp_servers` entry. Requires Agent SDK v0.3.274. [[lines 995-1505](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L995-L1505)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#canusetool)]

#### [discover-plugins](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* New "Add from claude.ai" section. In sessions where plugins sync from your claude.ai account, `claude plugin marketplace list` prints a `From claude.ai:` section, and `claude plugin marketplace add --claudeai <name>` adds one. Claude Code registers it under a local `claudeai-`-prefixed name derived from the claude.ai listing — "Organization library" becomes `claudeai-organization-library`. Requires v2.1.273. [[lines 274-284](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/claude-code/discover-plugins.md?plain=1#L274-L284)] [[Source](https://code.claude.com/docs/en/discover-plugins#add-from-claudeai)]
* On sign-out or an account switch, such a marketplace stays configured but shows no plugins, while **plugins you already installed from it keep loading**. [[line 286](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/claude-code/discover-plugins.md?plain=1#L286)] [[Source](https://code.claude.com/docs/en/discover-plugins#add-from-claudeai)]
* New "Add a marketplace and install in one command" section for `--marketplace`. The source takes the usual forms but **can't contain spaces**, the plugin name must be given bare without an `@marketplace` suffix, and Claude Code shows the resolved source and asks you to confirm before adding — declining cancels the install and adds nothing. Requires v2.1.275. [[lines 334-344](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/claude-code/discover-plugins.md?plain=1#L334-L344)] [[Source](https://code.claude.com/docs/en/discover-plugins#add-a-marketplace-and-install-in-one-command)]
* Marketplaces added from claude.ai get auto-update enabled by default, alongside `claude-plugins-official` and most official Anthropic marketplaces. [[line 496](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/claude-code/discover-plugins.md?plain=1#L496)] [[Source](https://code.claude.com/docs/en/discover-plugins#configure-auto-updates)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_STARTUP_FAILURE_RESULTS`, `CLAUDE_CODE_MCP_STARTUP_WAIT_MS` (v2.1.274), `CLAUDE_CODE_AUTO_MODE_SERVER`, `CLAUDE_CODE_DISABLE_WINDOWS_SHELL_LAUNCHER`, `CLAUDE_CODE_GATEWAY_MODEL_DISCOVERY_TIMEOUT_MS` and `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS`. [[lines 206-388](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/claude-code/env-vars.md?plain=1#L206-L388)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CLAUDE_CODE_BG_TASKS_REPORT_RUNNING` documents a default flip: a non-interactive session now keeps reporting a **running** status past turn end while background work is live, so a host watching the status doesn't announce that Claude is waiting for input mid-work. Background shell commands don't hold it. Set `0` to opt out; on versions before v2.1.269 you had to set `1` to opt in. [[line 209](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/claude-code/env-vars.md?plain=1#L209)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` explains the memory tradeoff behind its default of 16: each running agent's transcript stays in Claude Code's memory. [[line 388](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/claude-code/env-vars.md?plain=1#L388)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CLAUDE_CODE_RESUME_INTERRUPTED_TURN_MAX_AGE_MS` gets a fuller entry: unset or `0` means no bound **except** that a turn whose last request failed with an API error resumes only while that error is under six hours old, a positive value bounds every turn, and a negative or non-numeric value applies a one-hour bound. [[line 338](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/claude-code/env-vars.md?plain=1#L338)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `MCP_CONNECTION_NONBLOCKING` now spells out the exceptions to non-blocking startup: `alwaysLoad: true` servers still make startup wait (unless served from the discovery cache), and `-p` without `--input-format stream-json` waits for pending servers before the first turn regardless. [[line 443](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/claude-code/env-vars.md?plain=1#L443)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* A large batch of new error entries, most of them authentication: `Claude login not accepted` for a cloud session the server refuses with a 401, four MCP re-authentication variants (including `headersHelper` and config-`Authorization` credential rejections and an insufficient-scope form), Google Cloud and Microsoft Foundry credential failures, `Gateway refused the request`, and `Single sign-on authorization needed`. [[lines 65-189](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/claude-code/errors.md?plain=1#L65-L189)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]
* Two new output-style errors — custom styles can't be selected over Remote Control or from a relayed message, and styles saved to `.claude/settings.local.json` in a session that doesn't load it. [[lines 197-198](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/claude-code/errors.md?plain=1#L197-L198)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]
* New symlink-race entries for Read and Grep: `its symlink resolution changed after permission was checked`. [[line 225](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/claude-code/errors.md?plain=1#L225)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]

-----

## API changes

### Changed documents

#### [build-with-claude/compaction](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/api/build-with-claude/compaction.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]

* The on-demand compaction section added two days earlier gained its remaining SDK language examples, including C#, alongside a note that a conversation with no `system` prompt or tools sends neither on the summarization request. `max_tokens` capping the whole call including thinking is now repeated inline in the examples. [[lines 3427-3554](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/api/build-with-claude/compaction.md?plain=1#L3427-L3554)] [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction#request-a-summary)]

#### [build-with-claude/thinking](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/api/build-with-claude/thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking)]

* Streaming examples filled out across Python, Java and PHP, handling `ThinkingDelta` alongside text deltas and the `content_block_start` block types. [[lines 563-728](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/api/build-with-claude/thinking.md?plain=1#L563-L728)] [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking#streaming-thinking)]
* Claude Mythos Preview accepts `max_tokens` up to 128K, and **the Batches beta ceiling isn't available for it**. [[line 1160](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/api/build-with-claude/thinking.md?plain=1#L1160)] [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking#output-limits)]

#### [managed-agents/events-and-streaming](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/api/managed-agents/events-and-streaming.md) [[Source](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)] and [managed-agents/migration](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/api/managed-agents/migration.md)

* Both pages gained worked event-loop examples in more SDK languages, showing how to branch on `ManagedAgentsAgentMessageEvent`, `ManagedAgentsAgentCustomToolUseEvent` and `ManagedAgentsSessionStatusIdleEvent`, and how to detect an end-of-turn stop reason in each. [[lines 1146-1238](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/api/managed-agents/migration.md?plain=1#L1146-L1238)] [[Source](https://platform.claude.com/docs/en/managed-agents/migration#code-comparison)]

#### [agents-and-tools/tool-use/fine-grained-tool-streaming](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/api/agents-and-tools/tool-use/fine-grained-tool-streaming.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)] and [build-with-claude/handling-stop-reasons](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/api/build-with-claude/handling-stop-reasons.md)

* Both gained PHP and Python examples, including distinguishing a `max_tokens` cutoff from natural completion by reading `usage.output_tokens` alongside the stop reason. [[lines 3429-3434](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/api/build-with-claude/handling-stop-reasons.md?plain=1#L3429-L3434)] [[Source](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons#getting-maximum-tokens-without-knowing-input-size)]

#### [api/compliance](https://github.com/gpambrozio/ClaudeDocs/blob/b2037be67c64dfa5a61aada9673680a81e4c95c0/docs-md/api/api/compliance.md) [[Source](https://platform.claude.com/docs/en/api/compliance)]

* The compliance activity catalog expanded again across `compliance.md`, `compliance/activities.md` and the list endpoint, with new activity types and their object schemas.
