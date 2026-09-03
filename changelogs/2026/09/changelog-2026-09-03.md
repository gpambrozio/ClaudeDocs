# [Claude docs changes for Sept 3rd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/3513aa7d655b577148f233e7711e5d8d31abd873) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/3513aa7d655b577148f233e7711e5d8d31abd873)]

## Executive Summary
- Claude Code 2.1.259 fixes concurrent sessions silently reverting each other's `~/.claude.json` changes, adds a `managedMcpServers` managed setting, `--permission-prompts none` for unattended headless hosts, and `--json` output for `claude plugin validate`.
- The Admin API (user management, spend limits), Claude Enterprise Analytics API, and Compliance API docs now show the required `anthropic-version` header on every request.
- The web fetch tool docs clarify exactly which URLs are fetchable: text that appears only in Claude's own output or only in the system prompt is never fetchable, and other server-side tool results (code execution, MCP connector, tool search) aren't an allowed source either.
- Task budget docs add a new "What counts as a turn" section spelling out precisely when a fresh budget starts versus when a turn continues across tool-result messages.
- Code execution and Files API docs note that Claude-generated audio files (MP3, WAV, FLAC, M4A) now also carry signed C2PA Content Credentials, alongside images and video.

## New Claude Code versions

### [2.1.259](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/versions/2.1.259.md)

#### New features

* Added `managedMcpServers` managed setting: organizations can provide HTTP/SSE MCP servers to every user (same entry shape as `.mcp.json`); entries that name a command to run are skipped
* Added `--permission-prompts none` for unattended headless hosts: anything that would prompt is denied automatically while the active permission mode (including auto mode) keeps deciding
* Added recognition of `glab mr create/merge/close/reopen/note/update` so GitLab merge requests show as `MR !N` in the collapsed tool summary and refresh the footer MR badge
* Added `--json` to `claude plugin validate` for a machine-readable validation report
* [VSCode] Added an Active quick filter and a status filter menu (Needs input, Working, Completed) to the session list sidebar

#### Existing feature improvements

* Improved terminal resize and first-render performance for long responses by reusing text measurements
* Improved `/workflows` agent detail: JSON outcomes are pretty-printed with syntax colors and real line breaks, and long outcomes fold behind an expand toggle
* Improved headless/SDK session start: the first turn begins up to 50 ms sooner when MCP servers finish connecting
* Improved `/install-github-app` to explain it is GitHub-only and point to the GitLab CI/CD docs when run inside a GitLab repository
* Improved nested background subagent results to be saved in the parent subagent's transcript, so resumed subagents keep them and shared transcripts show the delivery
* Changed `allowedMcpServers` to govern only servers users add: a literal `managed-mcp.json` server your allowlist used to filter out now loads on upgrade; use `deniedMcpServers` to keep it off

#### Major bug fixes

* Fixed concurrent sessions silently reverting each other's `~/.claude.json` changes — workspace trust no longer resets and MCP/project state is no longer lost when running many sessions at once
* Fixed a conversation whose thinking was rejected once being rejected again on every later turn
* Fixed Bash `Read()` deny rules not covering files given as option values (`--ignore-revs-file=.env`, `-f.env`, `@file`), `git diff`/`git grep` file operands, or `cd DIR && cat FILE` compounds; `grep -r`/`cp -r` over a directory holding a denied file now asks
* Fixed the prompt cache being invalidated when the OAuth token refreshed in sessions with telemetry disabled
* Fixed fullscreen mode showing a blank conversation after a long turn with hundreds of tool calls
* Fixed auto mode running a turn on a model it doesn't support when a command or skill's frontmatter `model:` named one; the turn now keeps the session model
* Fixed `CLAUDE_CODE_MAX_CONTEXT_TOKENS` being ignored for Vertex-style model IDs (`@YYYYMMDD` suffix) of model versions Claude Code doesn't recognize
* Fixed the live output preview of a running shell command hiding its newest lines when an earlier line wrapped
* Fixed a background GitHub connection check that ran on every launch for claude.ai users; the result is now remembered across launches
* Fixed `--resume` failing (and `--continue` opening an empty conversation) when a saved session contains an attachment entry with no payload
* Fixed frontmatter `model:` on custom commands and skills being ignored in interactive sessions
* Fixed Artifact publishing failing once with an "unexpected parameter `note`" error in conversations continued from an older version
* Fixed managed `forceRemoteSettingsRefresh` being ignored at startup when a policy helper configured by MDM or the managed settings file had already run
* Fixed worktree isolation refusing hook-created worktrees on machines where `git rev-parse` fails with a message other than "not a git repository"
* Fixed OpenTelemetry metrics and events from cloud sessions missing the `user.email`, `organization.id`, and `user.account_uuid` attributes
* Fixed MCP servers that disconnect while their tools are being listed at startup showing as connected with no tools instead of reporting the error
* Fixed the file edit permission dialog sometimes showing a changed line cut short with no indication
* Fixed repository detection dropping a known repo identity after a transient git probe failure
* Fixed managed settings silently going unenforced when the managed-settings file, a drop-in, the MDM plist, or the HKLM value cannot be parsed: Claude Code now refuses to start and names the source
* Fixed Stop not actually stopping background agents and workflows in remote-control sessions: killed tasks now stay visible and re-stoppable until their processes exit
* Fixed resuming a workflow run while its previous stopped run was still exiting, which could run duplicate copies of its agents
* Fixed marketplace repo URLs on github.com with a trailing slash or dangling `?`/`#` producing an unusable `.git` clone URL
* Fixed blocking Stop hooks causing the turn after a block to lose the model's reasoning from that turn and, on some models, miss the prompt cache
* Fixed remote (claude.ai) sessions taking 60 seconds to start a turn after a browser-hosted MCP server's page had gone away
* Fixed worktree-isolated sessions refusing common Bash loops, xargs pipelines and launcher-wrapped commands that cannot reach the main checkout
* Fixed remote and scheduled sessions doing nothing after a connector-tool permission prompt was approved while the session was paused

-----

## Claude Code changes

### Changed documents

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` now also disables the PR/MR status badge checks described in the updated `interactive-mode` doc. [[line 233](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/claude-code/env-vars.md?plain=1#L233)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Rewrote how the PR status badge refreshes: it no longer polls on a fixed interval, instead refreshing after a `git push` or PR-changing `gh pr`/`glab mr` command, and now needs a discoverable GitHub token (`GH_TOKEN`/`GITHUB_TOKEN`, `gh auth login`, or the Enterprise equivalents) rather than just an authenticated `gh` CLI. [[lines 576-592](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/claude-code/interactive-mode.md?plain=1#L576-L592)] [[Source](https://code.claude.com/docs/en/interactive-mode#pr-review-status)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* Documented the new `claude plugin validate` command, including `--strict` and the new `--json` machine-readable report format. [[line 1117](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/claude-code/plugins-reference.md?plain=1#L1117)] [[Source](https://code.claude.com/docs/en/plugins-reference#plugin-validate)]

#### [prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/claude-code/prompt-caching.md) [[Source](https://code.claude.com/docs/en/prompt-caching)]

* Added a new "Accumulating many images" cache-invalidation trigger: once a request would exceed the API's image/PDF count or size limits, Claude Code drops a batch of the oldest images/PDFs, which reprocesses the conversation from that point. [[line 136](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/claude-code/prompt-caching.md?plain=1#L136)] [[Source](https://code.claude.com/docs/en/prompt-caching#accumulating-many-images)]
* Documented that `/fork`-copied sessions and workflow fan-outs (held for up to 5 seconds by default) can also read a prefix cached by an earlier request. [[line 260](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/claude-code/prompt-caching.md?plain=1#L260)] [[Source](https://code.claude.com/docs/en/prompt-caching#subagents-and-the-cache)]

#### [self-hosted-environments-deploy](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/claude-code/self-hosted-environments-deploy.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy)]

* Clarified that `--kill-session-after-min` is a hard backstop that kills sessions even mid-use, and recommended setting it well above the longest expected session (e.g., 480 minutes) rather than using it to reclaim idle slots. [[line 389](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L389)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#some-sessions-don’t-count-as-idle)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Added a new "Run every subagent on one model" section explaining how `CLAUDE_CODE_SUBAGENT_MODEL` and `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` combine to override every subagent's, teammate's, and workflow agent's model, including the built-in Explore and Plan subagents. [[line 316](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/claude-code/sub-agents.md?plain=1#L316)] [[Source](https://code.claude.com/docs/en/sub-agents#run-every-subagent-on-one-model)]

-----

## API changes

### Changed documents

#### [agents-and-tools/tool-use/code-execution-tool](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

* Audio files (MP3, WAV, FLAC, M4A) that Claude generates in the code execution sandbox now also carry signed C2PA Content Credentials, alongside the existing image and video formats. [[line 197](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L197)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

#### [agents-and-tools/tool-use/web-fetch-tool](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]

* Rewrote the "cannot fetch" rule: URLs that appear only in Claude's own output or only in the system prompt aren't fetchable, and results from other server-side tools (code execution, MCP connector, tool search) aren't an allowed source either. Client-side tool results remain allowed even when they echo Claude-produced text. [[line 338](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L338)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]

#### [build-with-claude/files](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Noted that audio files Claude produces with the code execution tool (including via skills) now also carry signed C2PA Content Credentials on download. [[line 246](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/build-with-claude/files.md?plain=1#L246)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

#### [build-with-claude/mid-conversation-system-messages](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/build-with-claude/mid-conversation-system-messages.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages)]

* Added a placement exception: `tool_addition`/`tool_removal` blocks aren't accepted immediately after a paused assistant turn (one ending in a server tool result), though `text` blocks are; resume the paused turn first. [[line 343](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/build-with-claude/mid-conversation-system-messages.md?plain=1#L343)] [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages)]

#### [build-with-claude/preserved-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/build-with-claude/preserved-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking)]

* Added a new FAQ section covering thinking invalidation across account resets, tool list or effort changes, compaction, instruction file edits, session resumption, model switches, and non-Claude routed turns. [[line 307](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/build-with-claude/preserved-thinking.md?plain=1#L307)] [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking)]

#### [build-with-claude/task-budgets](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/build-with-claude/task-budgets.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/task-budgets)]

* Added a new "What counts as a turn" section: a user message with no tool results starts a fresh budget, a user message carrying `tool_result` blocks continues the current turn, and server-side compaction during a turn doesn't reset the budget. [[line 57](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/build-with-claude/task-budgets.md?plain=1#L57)] [[Source](https://platform.claude.com/docs/en/build-with-claude/task-budgets)]
* Reworked the worked example to distinguish "requests" from "turns" and clarified exactly which tokens to pass as `remaining` when compacting message history yourself. [[line 211](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/build-with-claude/task-budgets.md?plain=1#L211)] [[Source](https://platform.claude.com/docs/en/build-with-claude/task-budgets)]

#### [cli-sdks-libraries/sdks/java](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/cli-sdks-libraries/sdks/java.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/java)]

* Bumped the recommended Java SDK version to 2.60.0. [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/cli-sdks-libraries/sdks/java.md?plain=1#L14)] [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/java)]

#### [cli-sdks-libraries/sdks/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/cli-sdks-libraries/sdks/typescript.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/typescript)]

* Raised the minimum supported TypeScript version from 4.9 to 5.0. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/cli-sdks-libraries/sdks/typescript.md?plain=1#L19)] [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/typescript)]

#### [intro](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/intro.md) [[Source](https://platform.claude.com/docs/en/intro)]

* Added a new "Explore the latest generation of Claude models" section with per-model summaries and links, mirroring the model picker on the home page. [[line 16](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/intro.md?plain=1#L16)] [[Source](https://platform.claude.com/docs/en/intro)]

#### [manage-claude/analytics-api](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/manage-claude/analytics-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/analytics-api)]

* Added a "Versioning" section: the `anthropic-version` header must now be sent on every request to this API. [[line 103](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/manage-claude/analytics-api.md?plain=1#L103)] [[Source](https://platform.claude.com/docs/en/manage-claude/analytics-api)]

#### [manage-claude/api-and-data-retention](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/manage-claude/api-and-data-retention.md) [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

* Noted that remote session transcripts are retained for 6 years unless a user deletes the session sooner. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/manage-claude/api-and-data-retention.md?plain=1#L19)] [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

#### [manage-claude/cmek-aws-kms](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/manage-claude/cmek-aws-kms.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms)]

* Added a follow-up step to the key-attachment troubleshooting flow: after fixing a `SourceArn` or encryption-context mismatch, restore the `ArnLike` condition on both service-principal policy statements. [[line 307](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/manage-claude/cmek-aws-kms.md?plain=1#L307)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms)]

#### [manage-claude/compliance-api](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/manage-claude/compliance-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-api)]

* Added a "Versioning" section: the `anthropic-version` header must now be sent on every Compliance API request. [[line 68](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/manage-claude/compliance-api.md?plain=1#L68)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-api)]

#### [manage-claude/compliance-integration-patterns](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/manage-claude/compliance-integration-patterns.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-integration-patterns)]

* Noted that remote sessions a user deletes are no longer listed and return 404 on the messages endpoint, and updated retention/export guidance to cover remote session deletion alongside chat deletion. [[line 153](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/manage-claude/compliance-integration-patterns.md?plain=1#L153)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-integration-patterns)]

#### [manage-claude/compliance-sessions](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/manage-claude/compliance-sessions.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-sessions)]

* Documented that the remote session endpoints no longer return a session once a user deletes it, and its transcript can't be recovered through the Compliance API. [[line 439](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/manage-claude/compliance-sessions.md?plain=1#L439)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-sessions)]

#### [manage-claude/spend-limits-api](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/manage-claude/spend-limits-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/spend-limits-api)]

* Added a "Versioning" section: the `anthropic-version` header must now be sent on every request. [[line 79](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/manage-claude/spend-limits-api.md?plain=1#L79)] [[Source](https://platform.claude.com/docs/en/manage-claude/spend-limits-api)]

#### [manage-claude/user-management](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/manage-claude/user-management.md) [[Source](https://platform.claude.com/docs/en/manage-claude/user-management)]

* Added a "Versioning" section, and removed the note that group endpoints were exempt from the `anthropic-version` header requirement — they now require it like the rest of the Admin API. [[lines 97-284](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/manage-claude/user-management.md?plain=1#L97-L284)] [[Source](https://platform.claude.com/docs/en/manage-claude/user-management)]

#### [managed-agents/self-hosted-sandboxes](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/managed-agents/self-hosted-sandboxes.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

* Bumped the recommended `ant` CLI version from 1.27.0 to 1.29.0 in the install and Dockerfile snippets. [[line 103](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L103)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

#### [models/fable-5-1/whats-new-fable-5-1](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/models/fable-5-1/whats-new-fable-5-1.md) [[Source](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1)]

* Noted that Claude Fable 5.1's generated audio files now also carry signed C2PA Content Credentials, alongside images and video. [[line 126](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/models/fable-5-1/whats-new-fable-5-1.md?plain=1#L126)] [[Source](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1)]

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* Announced that the Admin API (user management, spend limits), Claude Enterprise Analytics API, and Compliance API guides now show the required `anthropic-version` header on every request. [[line 22](https://github.com/gpambrozio/ClaudeDocs/blob/3513aa7d655b577148f233e7711e5d8d31abd873/docs-md/api/release-notes/overview.md?plain=1#L22)] [[Source](https://platform.claude.com/docs/en/release-notes/overview)]
