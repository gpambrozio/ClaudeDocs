# [Claude docs changes for March 7th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/22ccf1775f23abb720e1351289ec38ca047f0e27) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/22ccf1775f23abb720e1351289ec38ca047f0e27)]

## Executive Summary
- Scheduled tasks are now a first-class feature in the Desktop app and CLI: the new `/loop` command and cron tools enable recurring prompts, and the Desktop adds a full scheduling UI with frequency options, catch-up runs, and per-task permission management
- Two new Agent SDK documentation pages cover how the agent loop works (turns, messages, tool execution, context management) and how to use Claude Code features like CLAUDE.md, skills, and hooks in SDK agents
- Setup scripts for Claude Code on the web allow installing dependencies and configuring tools before Claude Code launches, replacing the SessionStart hook workaround
- The Agent SDK sessions guide was completely rewritten with comprehensive coverage of automatic session management, resume/fork patterns, and cross-host session handling
- Version 2.1.71 brings a large batch of bug fixes including stdin freeze in long sessions, startup freezes with voice mode and OAuth, and forked conversation plan file conflicts

## New Claude Code versions

### [2.1.71](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/versions/2.1.71.md)

#### New features

* Added `/loop` command to run a prompt or slash command on a recurring interval (e.g. `/loop 5m check the deploy`)
* Added cron scheduling tools (`CronCreate`, `CronList`, `CronDelete`) for recurring prompts within a session
* Added `voice:pushToTalk` keybinding to make the voice activation key rebindable in `keybindings.json` (default: space)
* Added `fmt`, `comm`, `cmp`, `numfmt`, `expr`, `test`, `printf`, `getconf`, `seq`, `tsort`, and `pr` to the bash auto-approval allowlist

#### Existing feature improvements

* Improved startup time by deferring native image processor loading to first use
* Improved bridge session reconnection to complete within seconds after laptop wake from sleep, instead of waiting up to 10 minutes
* Improved `/plugin uninstall` to disable project-scoped plugins in `.claude/settings.local.json` instead of modifying `.claude/settings.json`
* Improved plugin-provided MCP server deduplication — servers duplicating a manually-configured server (same command/URL) are now skipped
* Updated `/debug` to toggle debug logging on mid-session, since debug logs are no longer written by default
* Removed startup notification noise for unauthenticated org-registered claude.ai connectors

#### Major bug fixes

* Fixed stdin freeze in long-running sessions where keystrokes stop being processed but the process stays alive
* Fixed a 5–8 second startup freeze for users with voice mode enabled, caused by CoreAudio initialization blocking the main thread after system wake
* Fixed startup UI freeze when many claude.ai proxy connectors refresh an expired OAuth token simultaneously
* Fixed forked conversations (`/fork`) sharing the same plan file, causing plan edits in one fork to overwrite the other
* Fixed the Read tool putting oversized images into context when image processing failed, breaking subsequent turns in long image-heavy sessions
* Fixed false-positive permission prompts for compound bash commands containing heredoc commit messages
* Fixed plugin installations being lost when running multiple Claude Code instances
* Fixed claude.ai connectors failing to reconnect after OAuth token refresh
* Fixed claude.ai MCP connector startup notifications appearing for every org-configured connector instead of only previously connected ones
* Fixed background agent completion notifications missing the output file path, making it difficult for parent agents to recover agent results after context compaction
* Fixed duplicate output in Bash tool error messages when commands exit with non-zero status
* Fixed Chrome extension auto-detection getting permanently stuck on "not installed" after running on a machine without local Chrome
* Fixed `/plugin marketplace update` failing with merge conflicts when the marketplace is pinned to a branch/tag ref
* Fixed `/plugin marketplace add owner/repo@ref` incorrectly parsing `@` — previously only `#` worked as a ref separator
* Fixed duplicate entries in `/permissions` Workspace tab when the same directory is added with and without a trailing slash
* Fixed `--print` hanging forever when team agents are configured

-----

## Claude Code changes

### New Documents

#### [Run prompts on a schedule](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/claude-code/scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/scheduled-tasks)]

New document covering session-scoped scheduled tasks. Explains the `/loop` bundled skill for recurring prompts, one-time reminders in natural language, and direct use of the `CronCreate`/`CronList`/`CronDelete` tools. Includes interval syntax reference, jitter behavior, three-day expiry for recurring tasks, cron expression examples, and the `CLAUDE_CODE_DISABLE_CRON` environment variable.

### Changed documents

#### [Claude Code on the web](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* New **Setup scripts** section: Bash scripts that run when a new cloud session starts, before Claude Code launches, for installing dependencies and configuring the environment. Includes comparison table vs. SessionStart hooks (scope, timing, and where each is configured). [[line ~264](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L264)]
* Updated dependency management section to recommend setup scripts as the primary approach, with SessionStart hooks as an alternative for local+cloud parity
* Best practices updated: "Automate environment setup" with setup scripts replaces the previous "Use Claude Code hooks" recommendation

#### [Desktop quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/claude-code/desktop-quickstart.md) [[Source](https://code.claude.com/docs/en/desktop-quickstart)]

* Added scheduled tasks to the feature list in the introduction and as a next step after completing the quickstart

#### [Desktop](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* New **Schedule recurring tasks** section covering the full scheduling UI: creating tasks, frequency options (manual/hourly/daily/weekdays/weekly), how tasks run locally, missed run catch-up behavior (one catch-up run for most recently missed time in the last seven days), permission management, and task management actions (run now, pause, edit, delete, review history). [[line ~312](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/claude-code/desktop.md?plain=1#L312)]
* Feature list now uses anchor links to sections
* CLI comparison table updated with a "Recurring tasks" row comparing cron jobs/CI pipelines (CLI) versus scheduled tasks (Desktop)

#### [Claude Code index](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/claude-code/index.md) [[Source](https://code.claude.com/docs/en/index)]

* Desktop app description updated to include "schedule recurring tasks" in the feature summary

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* New MCP servers added: Wix (manage and build sites and apps), Similarweb (web/mobile/market data), Vibe Prospecting (company & contact data), PostHog (product analytics), Midpage Legal Research, Clerk (authentication/organizations/billing), Postman (API context for coding agents)

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `CLAUDE_CODE_DISABLE_CRON` environment variable to disable the scheduler, `/loop` skill, and cron tools entirely [[line ~688](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/claude-code/settings.md?plain=1#L688)]

#### [Skills](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Added `/loop [interval] <prompt>` to the bundled skills list with description and link to the scheduled tasks guide [[line ~700](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/claude-code/skills.md?plain=1#L700)]

-----

## API changes

### New Documents

#### [How the agent loop works](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/api/agent-sdk/agent-loop.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/agent-loop)]

Comprehensive new document explaining the Agent SDK's execution loop. Covers the turn-by-turn cycle (prompt → evaluate → tool execution → repeat), all five message types (`SystemMessage`, `AssistantMessage`, `UserMessage`, `StreamEvent`, `ResultMessage`), built-in tools table, parallel vs. sequential tool execution, control options (max turns, budget, effort, permission mode), context window management and automatic compaction, session continuity, and result subtypes including `stop_reason`. Includes a complete worked example combining all concepts.

#### [Use Claude Code features in the SDK](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/api/agent-sdk/claude-code-features.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/claude-code-features)]

New guide for enabling Claude Code filesystem features in SDK agents via `settingSources`. Covers the three sources (`"project"`, `"user"`, `"local"`), CLAUDE.md load locations at each level, skills discovery, and both filesystem hooks (from `settings.json`) and programmatic hook callbacks. Includes a feature selection table mapping common goals to the right SDK surface.

### Changed documents

#### [Python SDK reference](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/api/agent-sdk/python.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]

* `max_turns` description clarified to "Maximum agentic turns (tool-use round trips)" [[line ~536](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/api/agent-sdk/python.md?plain=1#L536)]
* `stop_reason: str | None` field added to `ResultMessage` [[line ~1075](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/api/agent-sdk/python.md?plain=1#L1075)]

#### [Sessions](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/api/agent-sdk/sessions.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/sessions)]

* Complete rewrite of the session management guide. New content includes: a decision table for choosing the right approach (one-shot vs. multi-turn vs. specific resume vs. fork), `ClaudeSDKClient` for automatic Python session management, TypeScript `continue: true` pattern, capturing session IDs from `ResultMessage`, resume-by-ID with common use cases, fork semantics with a two-branch example, and cross-host session handling (session file location, encoding scheme, alternatives to file transfer)

#### [Subagents](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/api/agent-sdk/subagents.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/subagents)]

* New **What subagents inherit** section with a table showing exactly what context a subagent receives (its own system prompt, Task prompt, project CLAUDE.md) versus what it does not (parent conversation history, parent system prompt, skills unless explicitly listed) [[line ~120](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/api/agent-sdk/subagents.md?plain=1#L120)]

#### [TypeScript SDK reference](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/api/agent-sdk/typescript.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]

* `maxTurns` description clarified to "Maximum agentic turns (tool-use round trips)" [[line ~158](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/api/agent-sdk/typescript.md?plain=1#L158)]

#### [Remote MCP servers](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* New MCP servers added: Wix, Gusto (Gusto data queries), Yardi Virtuoso (real-time Yardi data), MailerLite (email marketing), Mem (AI notebook), Wyndham Hotels and Resorts, PagerDuty (incidents/services/on-call), Postman (API context), Microsoft Learn

#### [Ruby SDK](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/api/api/sdks/ruby.md) [[Source](https://platform.claude.com/docs/en/api/sdks/ruby)]

* Fixed pagination example: changed `if page.next_page?` to `while page.next_page?` so all pages are iterated, not just the second one [[line ~208](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/api/api/sdks/ruby.md?plain=1#L208)]

#### [Vision](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/api/build-with-claude/vision.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/vision)]

* Added explanation of why Files API is preferred in multi-turn conversations: base64 images are resent on every turn, increasing payload size and latency as conversation grows; referencing by `file_id` keeps payloads small [[line ~176](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/api/build-with-claude/vision.md?plain=1#L176)]

#### [Working with messages](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/api/build-with-claude/working-with-messages.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)]

* Vision section updated to document `file` as a supported image source type (alongside `base64` and `url`), referencing images uploaded via the Files API [[line ~146](https://github.com/gpambrozio/ClaudeDocs/blob/22ccf1775f23abb720e1351289ec38ca047f0e27/docs-md/api/build-with-claude/working-with-messages.md?plain=1#L146)]
