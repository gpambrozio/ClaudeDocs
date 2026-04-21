# [Claude docs changes for April 21st, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad)]

## Executive Summary
- Claude Haiku 3 (`claude-3-haiku-20240307`) was officially retired on April 20, 2026 — all API requests to this model now return an error; migrate to Claude Haiku 4.5
- A new `workspace_restricted_developer` role was added to the Admin API for workspace members, along with response examples for invite, user, and workspace member delete endpoints
- Terminal configuration documentation was completely rewritten with a symptom-based navigation structure, improving discoverability for common terminal issues
- Claude Code Desktop now supports pre-configuring SSH connections for teams via the `sshConfigs` managed setting
- Agent hooks (`type: "agent"`) are now explicitly marked as experimental in both hooks reference and hooks guide

## New Claude Code versions

### [2.1.116](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/versions/2.1.116.md)

#### New features

* `/resume` on large sessions is significantly faster (up to 67% on 40MB+ sessions) and handles sessions with many dead-fork entries more efficiently
* Faster MCP startup when multiple stdio servers are configured; `resources/templates/list` is now deferred to first `@`-mention
* `/terminal-setup` now configures scroll sensitivity in VS Code, Cursor, and Windsurf for smoother fullscreen scrolling
* Thinking spinner now shows progress inline ("still thinking", "thinking more", "almost done thinking"), replacing the separate hint row
* `/config` search now matches option values (e.g. searching "vim" finds the Editor mode setting)
* `/doctor` can now be opened while Claude is responding, without waiting for the current turn to finish
* `/reload-plugins` and background plugin auto-update now auto-install missing plugin dependencies from marketplaces you've already added
* Agent frontmatter `hooks:` now fire when running as a main-thread agent via `--agent`

#### Existing feature improvements

* Bash tool now surfaces a hint when `gh` commands hit GitHub's API rate limit, so agents can back off instead of retrying
* The Usage tab in Settings now shows your 5-hour and weekly usage immediately and no longer fails when the usage endpoint is rate-limited
* Slash command menu now shows "No commands match" when your filter has zero results, instead of disappearing
* Security: sandbox auto-allow no longer bypasses the dangerous-path safety check for `rm`/`rmdir` targeting `/`, `$HOME`, or other critical system directories

#### Major bug fixes

* Fixed Devanagari and other Indic scripts rendering with broken column alignment in the terminal UI
* Fixed Ctrl+- not triggering undo in terminals using the Kitty keyboard protocol (iTerm2, Ghostty, kitty, WezTerm, Windows Terminal)
* Fixed Cmd+Left/Right not jumping to line start/end in terminals that use the Kitty keyboard protocol
* Fixed Ctrl+Z hanging the terminal when Claude Code is launched via a wrapper process (e.g. `npx`, `bun run`)
* Fixed scrollback duplication in inline mode where resizing the terminal or large output bursts would repeat earlier conversation history
* Fixed modal search dialogs overflowing the screen at short terminal heights, hiding the search box and keyboard hints
* Fixed scattered blank cells and disappearing composer chrome in the VS Code integrated terminal during scrolling
* Fixed an intermittent API 400 error related to cache control TTL ordering
* Fixed `/branch` rejecting conversations with transcripts larger than 50MB
* Fixed `/resume` silently showing an empty conversation on large session files instead of reporting the load error
* Fixed `/plugin` Installed tab showing the same item twice when it appears under Needs attention or Favorites
* Fixed `/update` and `/tui` not working after entering a worktree mid-session

-----

## Claude Code changes

### Changed documents

#### [Agent SDK / TypeScript](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Added new `SDKTaskUpdatedMessage` type to the SDK message union — emitted when a background task transitions state (e.g. `running` → `completed`), with a `patch` object containing optional `status`, `description`, `end_time`, `total_paused_ms`, `error`, and `is_backgrounded` fields. [[line 791](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L791)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkmessage)]

#### [Explore the .claude directory](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* Added note that on Windows, `~/.claude` resolves to `%USERPROFILE%\.claude`.
* Added new "Choose the right file" table mapping common customization goals (context, permissions, hooks, env vars, etc.) to the correct file and reference. [[line 117](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/claude-directory.md?plain=1#L117)] [[Source](https://code.claude.com/docs/en/claude-directory#what’s-not-shown)]
* Added new "Troubleshoot configuration" section with a symptom/cause/fix table covering common issues: hooks not firing, settings ignored, skill file placement, MCP server problems, and more. [[line 165](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/claude-directory.md?plain=1#L165)] [[Source](https://code.claude.com/docs/en/claude-directory#file-reference)]

#### [Commands](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/terminal-setup` description updated: Cursor, Windsurf, and Zed now listed as terminals requiring setup (Alacritty removed from the inline description).
* `/ultrareview` free runs for Pro and Max now expire on May 5, 2026 (previously described as "one-time" with no expiry). [[line 84](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/commands.md?plain=1#L84)] [[Source](https://code.claude.com/docs/en/commands)]

#### [Common Workflows](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Added new section "Work in notes and non-code folders" describing how Claude Code works in any directory including notes vaults and documentation folders. [[line 422](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/common-workflows.md?plain=1#L422)] [[Source](https://code.claude.com/docs/en/common-workflows#work-in-notes-and-non-code-folders)]

#### [Desktop](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Added new section "Pre-configure SSH connections for your team" showing how admins can distribute SSH connections via `sshConfigs` in managed settings. Includes a full JSON example and field descriptions. [[line 483](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/desktop.md?plain=1#L483)] [[Source](https://code.claude.com/docs/en/desktop#pre-configure-ssh-connections-for-your-team)]
* Added `sshConfigs` to the managed settings table. [[line 527](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/desktop.md?plain=1#L527)] [[Source](https://code.claude.com/docs/en/desktop#managed-settings)]

#### [Environment Variables](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `CLAUDE_ENV_FILE` description clarified: the file's contents are run as a script preamble in the same shell process (not just sourced), making exports visible to the subsequent command. [[line 144](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/env-vars.md?plain=1#L144)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [Hooks Guide](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* The direnv integration example now adds a `SessionStart` hook alongside `CwdChanged` to load env vars for the initial directory, not just on directory changes. Commands changed from `>>` to `>` to overwrite rather than append. [[line 299](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/hooks-guide.md?plain=1#L299)] [[Source](https://code.claude.com/docs/en/hooks-guide#reload-environment-when-directory-or-files-change)]
* Added note that `direnv allow` must be run once per directory, and that devbox/nix can use the same pattern.
* The `if` field description updated: it now fires when any subcommand of a compound Bash command matches (e.g. `npm test && git push` triggers `Bash(git *)`), and always fires when the command is too complex to parse. [[line 645](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/hooks-guide.md?plain=1#L645)] [[Source](https://code.claude.com/docs/en/hooks-guide#filter-by-tool-name-and-arguments-with-the-if-field)]
* `if` field no longer works on `PermissionDenied` events — supported events are now `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, and `PermissionRequest` only. [[line 646](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/hooks-guide.md?plain=1#L646)] [[Source](https://code.claude.com/docs/en/hooks-guide#filter-by-tool-name-and-arguments-with-the-if-field)]
* Agent hooks (`type: "agent"`) now explicitly marked as experimental with a warning to prefer command hooks for production workflows. [[line 695](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/hooks-guide.md?plain=1#L695)] [[Source](https://code.claude.com/docs/en/hooks-guide#prompt-based-hooks)]

#### [Hooks Reference](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* The `if` field in common hook fields now clarifies it fires when any Bash subcommand matches (after stripping `VAR=value` assignments), and that it always runs when a command is too complex to parse. Also notes `if` accepts exactly one permission rule with no `&&`/`||`/list syntax. [[line 277](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/hooks.md?plain=1#L277)] [[Source](https://code.claude.com/docs/en/hooks#common-fields)]
* `if` field no longer applies to `PermissionDenied` events — removed from supported event list. [[line 281](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/hooks.md?plain=1#L281)] [[Source](https://code.claude.com/docs/en/hooks#common-fields)]
* Agent hooks marked as experimental in both the hook type list and the agent-based hooks section. [[lines 268-270](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/hooks.md?plain=1#L268)] [[Source](https://code.claude.com/docs/en/hooks#hook-handler-fields)]

#### [Interactive Mode](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Added `u` (undo) to the Vim NORMAL mode key table. [[line 151](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/interactive-mode.md?plain=1#L151)] [[Source](https://code.claude.com/docs/en/interactive-mode#editing-normal-mode)]
* Shift+Enter terminal compatibility table updated: Warp and Apple Terminal added to "works natively"; VS Code, Cursor, Windsurf, Alacritty, and Zed listed as needing `/terminal-setup`. [[line 58](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/interactive-mode.md?plain=1#L58)] [[Source](https://code.claude.com/docs/en/interactive-mode#multiline-input)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `sshConfigs` setting: allows pre-configuring SSH connections for the Desktop environment dropdown. Supports `id`, `name`, `sshHost` (required), and `sshPort`, `sshIdentityFile`, `startDirectory` (optional). Read from managed and user settings only. [[line 201](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/settings.md?plain=1#L201)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

#### [Terminal Config](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* Page completely rewritten with a symptom-based structure. Now opens with a list of common problems (Shift+Enter submits, Option key shortcuts do nothing, no notification sound, etc.) and links directly to the fix. Each section is self-contained. Notable new/reorganized sections include: multiline prompts with a terminal compatibility table, enabling Option key as Meta per terminal, setting up Notification hooks for sound alerts, and a consolidated tmux configuration block combining `allow-passthrough` and `extended-keys` settings.

#### [Ultrareview](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/ultrareview.md) [[Source](https://code.claude.com/docs/en/ultrareview)]

* Pro and Max free ultrareview runs now have an expiry date: 3 free runs are available through May 5, 2026. After that date (or after the 3 runs are used), each review is billed as extra usage. [[line 41](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/ultrareview.md?plain=1#L41)] [[Source](https://code.claude.com/docs/en/ultrareview#pricing-and-free-runs)]

#### [VS Code](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Extended thinking description updated: Claude's reasoning now appears as collapsed blocks in the conversation; `Ctrl+O` expands or collapses all thinking blocks in the session. [[line 76](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/claude-code/vs-code.md?plain=1#L76)] [[Source](https://code.claude.com/docs/en/vs-code#use-the-prompt-box)]

-----

## API changes

### Changed documents

#### [Admin API Reference](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/api/admin.md) [[Source](https://platform.claude.com/docs/en/api/admin)]

* Added `InviteDeleteResponse` object type (`{ id, type: "invite_deleted" }`) to the API reference. [[line 106](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/api/admin.md?plain=1#L106)] [[Source](https://platform.claude.com/docs/en/api/admin)]
* Added `UserDeleteResponse` object type (`{ id, type: "user_deleted" }`) to the API reference. [[line 180](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/api/admin.md?plain=1#L180)] [[Source](https://platform.claude.com/docs/en/api/admin)]
* Added new `workspace_restricted_developer` role to workspace member role enum and `MemberDeleteResponse` type to the workspaces section. [[line 254](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/api/admin.md?plain=1#L254)] [[Source](https://platform.claude.com/docs/en/api/admin)]

#### [Admin API - Create Invite](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/api/admin/invites/create.md) [[Source](https://platform.claude.com/docs/en/api/admin/invites/create)]

* Added HTTP 200 response examples showing the full invite object structure. [[line 101](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/api/admin/invites/create.md?plain=1#L101)] [[Source](https://platform.claude.com/docs/en/api/admin/invites/create)]

#### [Admin API - Delete Invite](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/api/admin/invites/delete.md) [[Source](https://platform.claude.com/docs/en/api/admin/invites/delete)]

* Added HTTP 200 response example showing the `invite_deleted` response object. [[line 35](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/api/admin/invites/delete.md?plain=1#L35)] [[Source](https://platform.claude.com/docs/en/api/admin/invites/delete)]

#### [Admin API - Create Workspace](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/api/admin/workspaces/create.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/create)]

* Added HTTP 200 response examples showing the full workspace object structure including `data_residency` fields. [[line 100](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/api/admin/workspaces/create.md?plain=1#L100)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/create)]

#### [Admin API - Workspace Members](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/api/admin/workspaces/members.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/members)]

* Added `workspace_restricted_developer` as a valid workspace member role. [[line 42](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/api/admin/workspaces/members.md?plain=1#L42)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/members)]
* Added `MemberDeleteResponse` type definition. [[line 62](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/api/admin/workspaces/members.md?plain=1#L62)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/members)]

#### [Admin API - Create Workspace Member](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/api/admin/workspaces/members/create.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/members/create)]

* Added `workspace_restricted_developer` as a valid role for creating workspace members. [[line 20](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/api/admin/workspaces/members/create.md?plain=1#L20)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/members/create)]
* Added HTTP 200 response examples. [[line 81](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/api/admin/workspaces/members/create.md?plain=1#L81)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/members/create)]

#### [Admin API - Update Workspace Member](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/api/admin/workspaces/members/update.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/members/update)]

* Added `workspace_restricted_developer` as a valid role. [[line 20](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/api/admin/workspaces/members/update.md?plain=1#L20)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/members/update)]
* Added HTTP 200 response examples. [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/api/admin/workspaces/members/update.md?plain=1#L82)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/members/update)]

#### [Model Deprecations](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/about-claude/model-deprecations.md) [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]

* Claude Haiku 3 (`claude-3-haiku-20240307`) status updated from "Deprecated" to "Retired" (retired April 20, 2026). Added retirement notice to the deprecation history entry. [[line 73](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/about-claude/model-deprecations.md?plain=1#L73)] [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]

#### [Models Migration Guide](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/about-claude/models/migration-guide.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]

* Removed the Haiku 3 → Haiku 4.5 migration code example since Haiku 3 is now retired. [[line 569](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/about-claude/models/migration-guide.md?plain=1#L569)] [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]

#### [Content Moderation Guide](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/about-claude/use-case-guides/content-moderation.md) [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/content-moderation)]

* Updated all cost examples and code samples to use Claude Haiku 4.5 instead of the now-retired Claude Haiku 3. New pricing reflects $1.00/$5.00 per MTok (input/output) vs the old $0.25/$1.25 rates. [[line 76](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/about-claude/use-case-guides/content-moderation.md?plain=1#L76)] [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/content-moderation)]

#### [Legal Summarization Guide](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/about-claude/use-case-guides/legal-summarization.md) [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization)]

* Updated cost comparison to use Claude Haiku 4.5 pricing ($1.00/$5.00 per MTok) instead of retired Haiku 3 ($0.25/$1.25 per MTok). [[line 80](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/about-claude/use-case-guides/legal-summarization.md?plain=1#L80)] [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization)]

#### [Prompt Caching](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* Removed Claude Haiku 3 from the minimum cacheable prompt length table. [[line 254](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L254)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

#### [Claude on Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/build-with-claude/claude-on-amazon-bedrock.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock)]

* Removed Claude Haiku 3 (`anthropic.claude-3-haiku-20240307-v1:0`) from the Bedrock model availability table. [[line 85](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/build-with-claude/claude-on-amazon-bedrock.md?plain=1#L85)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock)]

#### [Claude on Vertex AI](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/build-with-claude/claude-on-vertex-ai.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

* Removed Claude Haiku 3 (`claude-3-haiku@20240307`) from the Vertex AI model list. [[line 68](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/build-with-claude/claude-on-vertex-ai.md?plain=1#L68)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

#### [Rate Limits](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/api/rate-limits.md) [[Source](https://platform.claude.com/docs/en/api/rate-limits)]

* Removed Claude Haiku 3 row from the rate limits table. [[line 155](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/api/rate-limits.md?plain=1#L155)] [[Source](https://platform.claude.com/docs/en/api/rate-limits)]

#### [Release Notes Overview](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* Added April 20, 2026 entry: Claude Haiku 3 (`claude-3-haiku-20240307`) has been retired; all requests now return an error. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/4ed6f5332bb7e9abbfe5919f70ff1edcd70031ad/docs-md/api/release-notes/overview.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/release-notes/overview)]
