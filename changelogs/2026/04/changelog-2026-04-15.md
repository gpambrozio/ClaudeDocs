# [Claude docs changes for April 15th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/48e212b) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/48e212b)]

## Executive Summary
- **Routines** (formerly "Cloud scheduled tasks") is a new cloud automation feature: saved Claude Code configurations that run on a schedule, via API call, or in response to GitHub events — documented in a new dedicated page
- **Claude Desktop v1.2581.0** brings a major UI overhaul: drag-and-drop workspace layout, integrated terminal, file editor pane, side chats, tasks pane, new keyboard shortcuts, and the ability to change models mid-session
- **Claude Sonnet 4 and Opus 4 deprecated**: both `claude-sonnet-4-20250514` and `claude-opus-4-20250514` are now deprecated with a retirement date of June 15, 2026; migrate to Sonnet 4.6 and Opus 4.6
- **New `CLAUDE_CODE_SKIP_PROMPT_HISTORY` env var** lets you skip writing prompt history and session transcripts to disk in any mode (previously only possible in non-interactive mode)
- **Refusal fallback model updated**: docs now recommend Haiku 4.5 (not Sonnet 4) as an alternative when encountering frequent `refusal` stop reasons with Sonnet 4.5 or Opus 4.1

## New Claude Code versions

### [2.1.108](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/versions/2.1.108.md)

#### New features

* Added `ENABLE_PROMPT_CACHING_1H` env var to opt into 1-hour prompt cache TTL on API key, Bedrock, Vertex, and Foundry (`ENABLE_PROMPT_CACHING_1H_BEDROCK` is deprecated but still honored), and `FORCE_PROMPT_CACHING_5M` to force 5-minute TTL
* Added recap feature to provide context when returning to a session, configurable in `/config` and manually invocable with `/recap`; force with `CLAUDE_CODE_ENABLE_AWAY_SUMMARY` if telemetry is disabled
* The model can now discover and invoke built-in slash commands like `/init`, `/review`, and `/security-review` via the Skill tool
* `/undo` is now an alias for `/rewind`
* Added "verbose" indicator when viewing the detailed transcript (`Ctrl+O`)
* Added a warning at startup when prompt caching is disabled via `DISABLE_PROMPT_CACHING*` environment variables

#### Existing feature improvements

* Improved `/model` to warn before switching models mid-conversation, since the next response re-reads the full history uncached
* Improved `/resume` picker to default to sessions from the current directory; press `Ctrl+A` to show all projects
* Improved error messages: server rate limits are now distinguished from plan usage limits; 5xx/529 errors show a link to status.claude.com; unknown slash commands suggest the closest match
* Reduced memory footprint for file reads, edits, and syntax highlighting by loading language grammars on demand

#### Major bug fixes

* Fixed paste not working in the `/login` code prompt (regression in 2.1.105)
* Fixed subscribers who set `DISABLE_TELEMETRY` falling back to 5-minute prompt cache TTL instead of 1 hour
* Fixed Agent tool prompting for permission in auto mode when the safety classifier's transcript exceeded its context window
* Fixed Bash tool producing no output when `CLAUDE_ENV_FILE` (e.g. `~/.zprofile`) ends with a `#` comment line
* Fixed `claude --resume <session-id>` losing the session's custom name and color set via `/rename`
* Fixed diacritical marks (accents, umlauts, cedillas) being dropped from responses when the `language` setting is configured
* Fixed Remote Control session titles set in the web UI being overwritten by auto-generated titles after the third message
* Fixed policy-managed plugins never auto-updating when running from a different project than where they were first installed

### [2.1.109](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/versions/2.1.109.md)

#### Existing feature improvements

* Improved the extended-thinking indicator with a rotating progress hint

-----

## Claude Code changes

### New Documents

#### [Routines](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)]

New document covering the **Routines** feature (research preview): saved Claude Code configurations — a prompt, repositories, and connectors — that run unattended on Anthropic-managed cloud infrastructure. Covers three trigger types (schedule, API, GitHub events), how to create and manage routines from the web/CLI/Desktop app, filter options for GitHub triggers, and usage/limits. Routines are available on Pro, Max, Team, and Enterprise plans with Claude Code on the web enabled.

### Changed documents

#### [Claude Code on the web](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* References to "Cloud scheduled tasks" page replaced with the new [Routines](routines.md) page, which covers schedule, API, and GitHub event triggers. [[line 30](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L30)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#github-authentication-options)]

#### [The .claude directory](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* The new `CLAUDE_CODE_SKIP_PROMPT_HISTORY` environment variable can now skip writing transcripts and prompt history in any mode (interactive or not), replacing the previous non-interactive-only `--no-session-persistence` approach. [[line 202](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/claude-directory.md?plain=1#L202)] [[Source](https://code.claude.com/docs/en/claude-directory#plaintext-storage)]

#### [Commands](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/branch` description clarified: branching now explicitly "preserves the original" conversation so you can return to it with `/resume`. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/commands.md?plain=1#L15)] [[Source](https://code.claude.com/docs/en/commands)]
* `/schedule` now points to the [Routines](routines.md) page. [[line 66](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/commands.md?plain=1#L66)] [[Source](https://code.claude.com/docs/en/commands)]

#### [Common workflows](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Extended thinking progress: progress hints now appear below the thinking indicator to show Claude is actively working. [[line 531](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/common-workflows.md?plain=1#L531)] [[Source](https://code.claude.com/docs/en/common-workflows#use-extended-thinking-thinking-mode)]
* Scheduling options table updated: "Cloud scheduled tasks" replaced with "Routines", which can also trigger on API calls or GitHub events, and the URL updated to `claude.ai/code/routines`. [[line 931](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/common-workflows.md?plain=1#L931)] [[Source](https://code.claude.com/docs/en/common-workflows#run-claude-on-a-schedule)]

#### [Desktop quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/desktop-quickstart.md) [[Source](https://code.claude.com/docs/en/desktop-quickstart)]

* Desktop app description updated to highlight the new sidebar, drag-and-drop layout, and integrated terminal/file editor. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/desktop-quickstart.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/desktop-quickstart)]
* Model can now be changed after the session starts (previously locked at session start). [[line 69](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/desktop-quickstart.md?plain=1#L69)] [[Source](https://code.claude.com/docs/en/desktop-quickstart#start-your-first-session)]
* New tip: **Arrange your workspace** — drag panes (chat, diff, terminal, file, preview) into any layout; open terminal with `Ctrl+\``. [[line 28](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/desktop-quickstart.md?plain=1#L28)] [[Source](https://code.claude.com/docs/en/desktop-quickstart#install)]
* Updated "Scale up" section to mention the new tasks pane for watching subagents and a new side chat feature. [[line 31](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/desktop-quickstart.md?plain=1#L31)] [[Source](https://code.claude.com/docs/en/desktop-quickstart#install)]

#### [Desktop scheduled tasks](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/desktop-scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks)]

* "Cloud scheduled tasks" references replaced with "Routines" throughout; added note that routines can also trigger on API calls or GitHub events. [[lines 43-72](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/desktop-scheduled-tasks.md?plain=1#L43-L72)] [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks#create-a-scheduled-task)]

#### [Use Claude Code Desktop](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Requires **Claude Desktop v1.2581.0** or later for new workspace features. [[line 20](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/desktop.md?plain=1#L20)] [[Source](https://code.claude.com/docs/en/desktop)]
* Model can now be changed mid-session from the same dropdown (previously locked after session start). [[line 29](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/desktop.md?plain=1#L29)] [[Source](https://code.claude.com/docs/en/desktop#start-a-session)]
* Preview pane can now open static HTML files, PDFs, and images — click any such path in the chat to open it. [[line 122](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/desktop.md?plain=1#L122)] [[Source](https://code.claude.com/docs/en/desktop#open-and-edit-files)]
* Auto-archive: sessions can now archive themselves automatically when their PR merges or closes. [[line 131](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/desktop.md?plain=1#L131)] [[Source](https://code.claude.com/docs/en/desktop#open-files-in-other-apps)]
* New **Arrange your workspace** section: drag-and-drop panes (chat, diff, preview, terminal, file, plan, tasks, subagent); integrated terminal (`Ctrl+\``); file pane with inline editing; right-click context menu for file paths; view modes (Normal / Verbose / Summary); full keyboard shortcut table. [[lines 136-198](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/desktop.md?plain=1#L136-L198)] [[Source](https://code.claude.com/docs/en/desktop#switch-view-modes)]
* New **Ask a side question without derailing the session** section: side chats (`Cmd+;` / `Ctrl+;`) that read session context but don't add to the main thread. [[line 224](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/desktop.md?plain=1#L224)] [[Source](https://code.claude.com/docs/en/desktop#app-permissions)]
* New **Watch background tasks** section: tasks pane shows subagents, shell commands, and workflows running in the current session. [[line 228](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/desktop.md?plain=1#L228)] [[Source](https://code.claude.com/docs/en/desktop#app-permissions)]
* Parallel sessions: new keyboard shortcut `Cmd+N` / `Ctrl+N` for new session and `Ctrl+Tab` to cycle through sessions. [[line 213](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/desktop.md?plain=1#L213)] [[Source](https://code.claude.com/docs/en/desktop#enable-computer-use)]
* Policy-managed plugins are now available in Desktop sessions the same way they are in the CLI. [[line 248](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/desktop.md?plain=1#L248)] [[Source](https://code.claude.com/docs/en/desktop#work-in-parallel-with-sessions)]
* SSH sessions now explicitly require Linux or macOS on the remote machine. [[line 257](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/desktop.md?plain=1#L257)] [[Source](https://code.claude.com/docs/en/desktop#ask-a-side-question-without-derailing-the-session)]
* Enterprise: Desktop now supports Vertex AI and gateway providers via managed settings (not just Anthropic's API directly). [[line 300](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/desktop.md?plain=1#L300)] [[Source](https://code.claude.com/docs/en/desktop#use-skills)]
* `--verbose` CLI flag equivalent is now the **Verbose view mode** in the Transcript view dropdown. [[line 282](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/desktop.md?plain=1#L282)] [[Source](https://code.claude.com/docs/en/desktop#sessions-from-dispatch)]

#### [Environment variables](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_DISABLE_VIRTUAL_SCROLL` env var: disables virtual scrolling in fullscreen rendering if blank regions appear. [[line 321](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/env-vars.md?plain=1#L321)] [[Source](https://code.claude.com/docs/en/env-vars#see-also)]
* New `CLAUDE_CODE_MAX_CONTEXT_TOKENS` env var: override the context window size assumed for the active model (only takes effect when `DISABLE_COMPACT` is also set; useful for gateway routing). [[line 329](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/env-vars.md?plain=1#L329)] [[Source](https://code.claude.com/docs/en/env-vars#see-also)]
* New `CLAUDE_CODE_SKIP_PROMPT_HISTORY` env var: skip writing prompt history and session transcripts to disk in any mode; sessions started with this won't appear in `--resume`, `--continue`, or up-arrow history. [[line 337](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/env-vars.md?plain=1#L337)] [[Source](https://code.claude.com/docs/en/env-vars#see-also)]

#### [Index / Overview](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/index.md) [[Source](https://code.claude.com/docs/en/index)]

* Improved Windows installation error message: added detection for `'irm' is not recognized` (CMD vs PowerShell disambiguation). [[line 39](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/index.md?plain=1#L39)] [[Source](https://code.claude.com/docs/en/index#get-started)]
* "Cloud scheduled tasks" replaced with "Routines" (can also trigger on API calls or GitHub events). [[line 146](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/index.md?plain=1#L146)] [[Source](https://code.claude.com/docs/en/index#what-you-can-do)]

#### [Plugins reference](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* Glob and Grep tools now skip orphaned plugin version directories during searches, so results don't include outdated plugin code. [[line 470](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/plugins-reference.md?plain=1#L470)] [[Source](https://code.claude.com/docs/en/plugins-reference#plugin-caching-and-file-resolution)]

#### [Plugins](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/plugins.md) [[Source](https://code.claude.com/docs/en/plugins)]

* The `name` field in `SKILL.md` frontmatter is no longer required; only `description` is needed. [[line 203](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/plugins.md?plain=1#L203)] [[Source](https://code.claude.com/docs/en/plugins#add-skills-to-your-plugin)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* `cleanupPeriodDays` description updated to reference `CLAUDE_CODE_SKIP_PROMPT_HISTORY` as the cross-mode way to disable transcripts. [[line 157](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/settings.md?plain=1#L157)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* New `minimumVersion` setting: prevents the auto-updater from downgrading below a specific version; automatically set when switching to the stable channel. [[line 184](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/claude-code/settings.md?plain=1#L184)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

-----

## API changes

### New Documents

#### [Trigger a routine via API](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/api/api/claude-code/routines-fire.md) [[Source](https://platform.claude.com/docs/en/api/claude-code/routines-fire)]

New experimental API reference for triggering a Claude Code routine via HTTP (`POST /v1/claude_code/routines/{routine_id}/fire`). Documents authentication (per-routine bearer tokens, not API keys), request/response shapes, error codes, rate limits, and differences from the standard Claude Platform API surface. Requires the `anthropic-beta: experimental-cc-routine-2026-04-01` header.

### Changed documents

#### [Model deprecations](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/api/about-claude/model-deprecations.md) [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]

* `claude-sonnet-4-20250514` and `claude-opus-4-20250514` are now **deprecated** as of April 14, 2026, with retirement scheduled for **June 15, 2026**. Recommended replacements: `claude-sonnet-4-6` and `claude-opus-4-6` respectively. [[lines 68-77](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/api/about-claude/model-deprecations.md?plain=1#L68-L77)] [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]

#### [Claude on Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/api/build-with-claude/claude-on-amazon-bedrock.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock)]

* Claude Sonnet 4 and Claude Opus 4 marked with ⚠️ deprecation indicator in the model table. [[lines 76-80](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/api/build-with-claude/claude-on-amazon-bedrock.md?plain=1#L76-L80)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock)]

#### [Claude on Vertex AI](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/api/build-with-claude/claude-on-vertex-ai.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

* Claude Sonnet 4 and Claude Opus 4 marked with ⚠️ deprecation indicator in the model table. [[lines 63-67](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/api/build-with-claude/claude-on-vertex-ai.md?plain=1#L63-L67)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

#### [Handling stop reasons](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/api/build-with-claude/handling-stop-reasons.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)]

* Updated recommendation for frequent `refusal` stop reasons: now suggests **Haiku 4.5** (`claude-haiku-4-5-20251001`) instead of Sonnet 4 (which is deprecated). [[line 291](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/api/build-with-claude/handling-stop-reasons.md?plain=1#L291)] [[Source](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)]

#### [Managed agents — Files](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/api/managed-agents/files.md) [[Source](https://platform.claude.com/docs/en/managed-agents/files)]

* CLI tab added to the code examples for mounting files and listing/downloading session files. [[lines 55-100](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/api/managed-agents/files.md?plain=1#L55-L100)] [[Source](https://platform.claude.com/docs/en/managed-agents/files)]

#### [Release notes overview](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* April 14, 2026 entry added: deprecation of Claude Sonnet 4 and Claude Opus 4, retiring June 15, 2026. [[lines 9-11](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/api/release-notes/overview.md?plain=1#L9-L11)] [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

#### [CLI SDK reference](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/api/api/sdks/cli.md) [[Source](https://platform.claude.com/docs/en/api/sdks/cli)]

* `--environment` flag renamed to `--environment-id` in the `sessions create` command examples. [[lines 203-372](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/api/api/sdks/cli.md?plain=1#L203-L372)] [[Source](https://platform.claude.com/docs/en/api/sdks/cli)]

#### [Handle streaming refusals](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/api/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals.md) [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)]

* Updated alternative model recommendation for `refusal` stop reasons: now Haiku 4.5 instead of Sonnet 4 (deprecated). [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/48e212b/docs-md/api/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals.md?plain=1#L36)] [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)]
