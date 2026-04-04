# [Claude docs changes for April 4th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/b79d40a) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/b79d40a)]

## Executive Summary
- **Ultraplan** is a new feature that hands a planning task from your local CLI to a Claude Code on the web session, letting you review, comment on, and revise the plan in your browser before choosing to execute remotely or send it back to the terminal
- **Permission modes** page was significantly rewritten with a new summary table, a dedicated `acceptEdits` section, a new "protected paths" section listing all protected directories/files, and clarified requirements for auto mode
- **Desktop scheduled tasks** were split into their own dedicated page (`desktop-scheduled-tasks.md`), separating them from the main desktop reference
- **Microsoft 365 MCP server** added as a built-in connector, providing access to SharePoint, OneDrive, Outlook, and Teams
- **Skills upload limit** increased from 8 MB to 30 MB in the API

## New Claude Code versions

### [2.1.92](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/versions/2.1.92.md)

#### New features

* Added `forceRemoteSettingsRefresh` policy setting: blocks CLI startup until remote managed settings are freshly fetched, and exits if the fetch fails (fail-closed behavior)
* Added interactive Bedrock setup wizard accessible from the login screen when selecting "3rd-party platform" — guides through AWS authentication, region configuration, credential verification, and model pinning
* Added per-model and cache-hit breakdown to `/cost` for subscription users
* `/release-notes` is now an interactive version picker
* Remote Control session names now use the hostname as the default prefix (e.g. `myhost-graceful-unicorn`), overridable with `--remote-control-session-name-prefix`
* Pro users now see a footer hint when returning to a session after the prompt cache has expired, showing roughly how many tokens the next turn will send uncached

#### Existing feature improvements

* Improved Write tool diff computation speed for large files (60% faster on files with tabs/`&`/`$`)
* Removed `/tag` command
* Removed `/vim` command (toggle vim mode via `/config` → Editor mode)
* Linux sandbox now ships the `apply-seccomp` helper in both npm and native builds, restoring unix-socket blocking for sandboxed commands

#### Major bug fixes

* Fixed subagent spawning permanently failing with "Could not determine pane count" after tmux windows are killed or renumbered during a long-running session
* Fixed prompt-type Stop hooks incorrectly failing when the small fast model returns `ok:false`, and restored `preventContinuation:true` semantics for non-Stop prompt-type hooks
* Fixed tool input validation failures when streaming emits array/object fields as JSON-encoded strings
* Fixed an API 400 error when extended thinking produced a whitespace-only text block alongside real content
* Fixed accidental feedback survey submissions from auto-pilot keypresses and consecutive-prompt digit collisions
* Fixed misleading "esc to interrupt" hint appearing alongside "esc to clear" when a text selection exists in fullscreen mode during processing
* Fixed Homebrew install update prompts to use the correct release channel (`claude-code` → stable, `claude-code@latest` → latest)
* Fixed `ctrl+e` jumping to the end of the next line when already at end of line in multiline prompts
* Fixed duplicate message appearing at two positions when scrolling up in fullscreen mode (iTerm2, Ghostty, and other terminals with DEC 2026 support)
* Fixed idle-return "/clear to save X tokens" hint showing cumulative session tokens instead of current context size
* Fixed plugin MCP servers stuck "connecting" on session start when they duplicate an unauthenticated claude.ai connector

-----

## Claude Code changes

### New Documents

#### [Desktop Scheduled Tasks](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/desktop-scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks)]

Content moved from the main Desktop page into its own dedicated reference. Covers local vs. remote task types, frequency options (manual, hourly, daily, weekdays, weekly), how scheduled tasks run, missed run catch-up behavior, per-task permission modes, and task management. Slightly expanded from the original desktop.md content.

#### [Ultraplan](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/ultraplan.md) [[Source](https://code.claude.com/docs/en/ultraplan)]

New feature in research preview. Ultraplan hands a planning task from the local CLI to a Claude Code on the web session running in plan mode. Claude drafts the plan in the cloud while your terminal stays free. Covers launching via `/ultraplan`, the `ultraplan` keyword, or from a completed local plan; reviewing with inline comments and emoji reactions in the browser; and choosing to execute on the web or send the plan back to the terminal.

#### [What's New](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/whats-new.md) [[Source](https://code.claude.com/docs/en/whats-new)]

New weekly digest index page linking to feature highlights for recent weeks. Currently covers Week 13 (v2.1.83–v2.1.85, March 23–27) and Week 14 (v2.1.86–v2.1.91, March 30–April 3).

#### [What's New – Week 13](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/whats-new/2026-w13.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w13)]

Digest for v2.1.83–v2.1.85 (March 23–27, 2026). Covers: Auto mode research preview, Computer use in the Desktop app, PR auto-fix for Claude Code on the web, transcript search with `/`, native PowerShell tool for Windows, and conditional `if` hooks.

#### [What's New – Week 14](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/whats-new/2026-w14.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w14)]

Digest for v2.1.86–v2.1.91 (March 30–April 3, 2026). Covers: Computer use in the CLI (research preview), `/powerup` interactive lessons, flicker-free alt-screen rendering, per-tool MCP result-size override (up to 500K characters), and plugin executables on the Bash tool's `PATH`.

### Changed documents

#### [Agent Teams](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

* Clarified that when a subagent definition runs as a teammate, its body is appended to the teammate's system prompt as additional instructions rather than replacing it; `skills` and `mcpServers` frontmatter fields are not applied on this path [[lines 213-219](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/agent-teams.md?plain=1#L213-L219)] [[Source](https://code.claude.com/docs/en/agent-teams#use-subagent-definitions-for-teammates)]
* Added that the lead assigns every teammate a name at spawn time, and any teammate can message any other by that name [[lines 241-243](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/agent-teams.md?plain=1#L241-L243)] [[Source](https://code.claude.com/docs/en/agent-teams#context-and-communication)]

#### [Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Added guidance for AWS Organizations users: the use-case form can be submitted once from the management account using the `PutUseCaseForModelAccess` API, with approval extending to child accounts automatically [[lines 18-20](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/amazon-bedrock.md?plain=1#L18-L20)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#1-submit-use-case-details)]

#### [Claude Code on the Web](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* Added mention of ultraplan for drafting and reviewing plans in a web session from the CLI [[line 126](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L126)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#tips-for-remote-tasks)]

#### [Commands](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* Added `/ultraplan <prompt>` command to the reference table [[line 70](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/commands.md?plain=1#L70)] [[Source](https://code.claude.com/docs/en/commands)]

#### [Desktop](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Removed the entire "Schedule recurring tasks" section (~89 lines); all scheduling content now lives in the dedicated [Desktop Scheduled Tasks](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/desktop-scheduled-tasks.md) page, with links updated throughout

#### [Desktop Quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/desktop-quickstart.md) [[Source](https://code.claude.com/docs/en/desktop-quickstart)]

* Reorganized the page: download links moved to the top before the intro paragraph; install and sign-in collapsed into a single step; ARM64 installer now listed inline rather than in a separate note

#### [Environment Variables](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Removed `CLAUDE_CODE_SKIP_FAST_MODE_NETWORK_ERRORS` environment variable [[line 114](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/env-vars.md?plain=1#L114)] [[Source](https://code.claude.com/docs/en/env-vars)]
* Updated `CLAUDE_CODE_TMPDIR` documentation: on Unix, Claude Code now appends `/claude-{uid}/` (not just `/claude/`), and the default is clarified as `/tmp` on macOS and `os.tmpdir()` on Linux/Windows [[line 123](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/env-vars.md?plain=1#L123)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [Headless / Non-interactive Mode](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* Added documentation for using `--permission-mode` with `-p`: explains that `dontAsk` denies anything not in `permissions.allow` (useful for locked-down CI) and `acceptEdits` allows file writes without prompting while shell commands still require explicit allowance [[lines 133-140](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/headless.md?plain=1#L133-L140)] [[Source](https://code.claude.com/docs/en/headless#auto-approve-tools)]

#### [Legal and Compliance](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/legal-and-compliance.md) [[Source](https://code.claude.com/docs/en/legal-and-compliance)]

* Updated OAuth authentication description to include Team and Enterprise subscription plans and link to the support article on logging in [[line 30](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/legal-and-compliance.md?plain=1#L30)] [[Source](https://code.claude.com/docs/en/legal-and-compliance#authentication-and-credential-use)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Added Microsoft 365 as a built-in MCP connector (SharePoint, OneDrive, Outlook, Teams) with command `claude mcp add microsoft-365 --transport http https://microsoft365.mcp.claude.com/mcp` [[lines 435-440](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/mcp.md?plain=1#L435-L440)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]

#### [Permission Modes](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Added a summary table at the top of the page listing all modes, what runs without asking, and best use cases [[lines 12-19](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/permission-modes.md?plain=1#L12-L19)] [[Source](https://code.claude.com/docs/en/permission-modes#available-modes)]
* Added a new dedicated section for `acceptEdits` mode explaining its behavior and when to use it [[lines 45-55](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/permission-modes.md?plain=1#L45-L55)] [[Source](https://code.claude.com/docs/en/permission-modes#switch-permission-modes)]
* Clarified the `Shift+Tab` cycle: `dontAsk` never appears, `bypassPermissions` and `auto` only appear when enabled, and optional modes slot in after `plan` [[lines 98-105](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/permission-modes.md?plain=1#L98-L105)] [[Source](https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode)]
* Clarified all requirements for auto mode: plan (Team, Enterprise, or API — not Pro/Max), admin enablement for Team/Enterprise, model (Sonnet 4.6 or Opus 4.6), and provider (Anthropic API only, not Bedrock/Vertex/Foundry) [[lines 262-278](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/permission-modes.md?plain=1#L262-L278)] [[Source](https://code.claude.com/docs/en/permission-modes#see-also)]
* Added Ultraplan as an option from the plan mode approval dialog [[line 243](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/permission-modes.md?plain=1#L243)] [[Source](https://code.claude.com/docs/en/permission-modes#see-also)]
* Added a new "Protected paths" section explicitly listing all protected directories (`.git`, `.vscode`, `.idea`, `.husky`, `.claude`) and protected files (`.gitconfig`, `.gitmodules`, shell rc files, `.mcp.json`, `.claude.json`) [[lines 393-420](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/permission-modes.md?plain=1#L393-L420)] [[Source](https://code.claude.com/docs/en/permission-modes#see-also)]
* Improved auto mode fallback documentation: denied actions appear in `/permissions` → Recently denied and can be retried with `r`; total counter persists for the session and resets only when its own limit triggers [[lines 323-327](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/permission-modes.md?plain=1#L323-L327)] [[Source](https://code.claude.com/docs/en/permission-modes#see-also)]

#### [Remote Control](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Added limitation note: starting an ultraplan session disconnects any active Remote Control session [[line 116](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/remote-control.md?plain=1#L116)] [[Source](https://code.claude.com/docs/en/remote-control#limitations)]
* Added Ultraplan to the related resources section [[line 177](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/remote-control.md?plain=1#L177)] [[Source](https://code.claude.com/docs/en/remote-control#related-resources)]

#### [Sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Clarified that when a subagent definition is used as an agent team teammate, its `tools` and `model` are used and the body is appended as additional instructions; links to agent-teams.md for which frontmatter fields apply [[line 187](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/sub-agents.md?plain=1#L187)] [[Source](https://code.claude.com/docs/en/sub-agents#choose-the-subagent-scope)]

#### [VS Code](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Removed `auto` from the list of accepted values for `initialPermissionMode` (auto mode must be configured via `defaultMode` in `settings.json` instead) [[line 242](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/vs-code.md?plain=1#L242)] [[Source](https://code.claude.com/docs/en/vs-code#extension-settings)]
* Updated `allowDangerouslySkipPermissions` description to note that auto mode has plan, admin, model, and provider requirements and may remain unavailable even with the toggle on [[line 251](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/claude-code/vs-code.md?plain=1#L251)] [[Source](https://code.claude.com/docs/en/vs-code#extension-settings)]

-----

## API changes

### Changed documents

#### [Remote MCP Servers](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Added Microsoft 365 as a supported remote MCP server providing access to SharePoint, OneDrive, Outlook, and Teams at `https://microsoft365.mcp.claude.com/mcp` [[lines 551-558](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L551-L558)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

#### [Skills Guide](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/api/build-with-claude/skills-guide.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/skills-guide)]

* Skill upload size limit increased from 8 MB to 30 MB (all files combined) [[line 391](https://github.com/gpambrozio/ClaudeDocs/blob/b79d40a/docs-md/api/build-with-claude/skills-guide.md?plain=1#L391)] [[Source](https://platform.claude.com/docs/en/build-with-claude/skills-guide)]
