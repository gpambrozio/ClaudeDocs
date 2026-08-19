# [Claude docs changes for August 19th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc)]

## Executive Summary
- The Workbench is now called **Playground** across the Claude Console and API docs — same tool, new name, referenced consistently in dozens of pages
- Claude Code 2.1.235 adds an opt-in **spellcheck** setting that underlines misspelled words in the prompt input using a locally installed `aspell`, `hunspell`, or `ispell`
- Workload Identity Federation token exchange failures now return a uniform `401 authentication_error` (`Authentication failed`) instead of `400 invalid_grant`, with deny reasons visible on a new authentication history page instead of hidden server-side
- `/goal` now clears itself on unrecoverable errors (auth failure, exhausted credits, context overflow, unavailable model) and periodically asks Claude to check on long-running background work that's holding up evaluation
- Files API storage limit doubled from 500 GB to 1 TB per organization, and both the Files API and Skills API now log create/delete/download operations to the Compliance API Activity Feed

## New Claude Code versions

### [2.1.235](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/versions/2.1.235.md)

#### New features

* Added an optional `spellcheck` setting that underlines misspelled words in the prompt input as you type, using your installed `aspell`, `hunspell`, or `ispell`

#### Existing feature improvements

* Improved memory and CPU usage while cloud sessions such as `/ultrareview` or `/autofix-pr` run in the background — their event streams are no longer re-scanned and re-rendered on every update
* Improved permission dialogs: display text and "don't ask again" options now always match what a grant would cover, and "don't ask again" is withheld when contents cannot be fully displayed
* Improved the embedded `grep` in native macOS/Linux builds: pathological patterns now fail fast instead of exhausting memory, and `-m N` with `-A/-C` prints correct context
* Improved the context-limit error to say when auto-compact is off and point to `/config` to re-enable it

#### Major bug fixes

* Fixed whole-prompt-cache invalidation when a language server disconnected or reconnected mid-session
* Fixed nested markdown list items misaligning at depth 3+ and added a hanging indent to wrapped list items in the terminal UI
* Fixed prompt input highlights (slash commands, keywords, mentions) appearing shifted by one or more characters in some multi-line prompts
* Fixed Shift+Tab inside the permission prompt's comment field approving the edit and granting session-wide edit permission instead of closing the field
* Fixed the Agent tool advertising a general-purpose default in sessions where that agent is unavailable: an omitted `subagent_type` there now gets a clear error listing the available agents
* Fixed notebook cell delete/replace approval dialogs silently omitting the existing cell content when the notebook or cell could not be read; the dialog now says why
* Fixed slash commands run while Claude is responding showing HTML entities instead of the actual characters
* Fixed the prompt footer not showing the "Update installed" restart notice after a background auto-update
* Fixed the expanded task list (`ctrl+t`) always starting collapsed when resuming or relaunching into a session that still has open tasks
* Vim mode: NORMAL mode and cursor position are now preserved when toggling the detailed transcript (ctrl+o) or closing a panel
* Dialogs: arrow keys and Enter pressed in quick succession now select the option you navigated to instead of the previously highlighted one
* `SendMessage` now refuses messages too large for cross-session delivery up front instead of silently dropping them
* Remote Control: `claude rc` now applies the same enterprise-gateway availability check as interactive startup
* [VSCode] Fixed focus jumping between open Claude tabs on its own when a window with several Claude panels is restored or reloaded

-----

## Claude Code changes

### Changed documents

#### [agent-loop](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/agent-sdk/agent-loop.md) [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop)]

* Minor wording clarifications around CLAUDE.md summarization instructions and error handling; the "manual compaction" doc link now points at the merged commands section in `skills.md`. [[line 236](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/agent-sdk/agent-loop.md?plain=1#L236)] [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop#automatic-compaction)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/agent-sdk/skills.md) [[Source](https://code.claude.com/docs/en/agent-sdk/skills)]

* This page was rewritten and now also serves as the SDK's command documentation (the old `slash-commands.md` content was folded in): it covers discovering commands via `slash_commands` in the `init` message, dispatching commands by name, using `/compact`, and pre-approving tools for skills. [[lines 1-98](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/agent-sdk/skills.md?plain=1#L1-L98)] [[Source](https://code.claude.com/docs/en/agent-sdk/skills)]
* New "Commands in Agent SDK sessions" section distinguishes built-in commands, bundled skills, user skills, and legacy command files. [[line 98](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/agent-sdk/skills.md?plain=1#L98)] [[Source](https://code.claude.com/docs/en/agent-sdk/skills#commands-in-agent-sdk-sessions)]
* New "Pre-approve tools for skills" section replaces the old tool-restrictions guidance, clarifying that `allowed-tools` frontmatter only applies to the CLI, not SDK sessions. [[line 324](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/agent-sdk/skills.md?plain=1#L324)] [[Source](https://code.claude.com/docs/en/agent-sdk/skills#pre-approve-tools-for-skills)]
* New "Invalid skill name error" section documents the exact TypeScript/Python errors raised when a `skills` list entry can't work as an exact name. [[line 446](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/agent-sdk/skills.md?plain=1#L446)] [[Source](https://code.claude.com/docs/en/agent-sdk/skills#invalid-skill-name-error)]

#### [subagents](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/agent-sdk/subagents.md) [[Source](https://code.claude.com/docs/en/agent-sdk/subagents)]

* Documents the new `subagent_type is required` error when the Agent tool is called with no `subagent_type` and no `general-purpose` fallback is available (e.g. `CLAUDE_AGENT_SDK_DISABLE_BUILTIN_AGENTS=1`); before v2.1.235 this failed with `Agent type 'general-purpose' not found`. [[line 179](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/agent-sdk/subagents.md?plain=1#L179)] [[Source](https://code.claude.com/docs/en/agent-sdk/subagents#filesystem-based-definition-alternative)]

#### [agent-teams](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

* Clarifies that an in-process teammate's `run_in_background: true` request now also fails (with an error, or by silently running in the foreground) rather than only being refused when the subagent's frontmatter sets `background: true`. [[line 421](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/agent-teams.md?plain=1#L421)] [[Source](https://code.claude.com/docs/en/agent-teams#limitations)]

#### [amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Clarifies that Sonnet 5 always runs with the 1M token context window on both the Invoke API and the Mantle endpoint on Amazon Bedrock. [[line 343](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/amazon-bedrock.md?plain=1#L343)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#1m-token-context-window)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* Updated the `/goal` description to reflect that the goal can now also clear for other reasons (see the `goal` doc changes below). [[line 71](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/commands.md?plain=1#L71)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]

#### [cross-session-messaging](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/cross-session-messaging.md) [[Source](https://code.claude.com/docs/en/cross-session-messaging)]

* New limitation: same-machine cross-session messages are capped at about a million serialized characters; Claude Code now refuses oversized messages in the sending session before they leave, instead of silently dropping them. [[line 234](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/cross-session-messaging.md?plain=1#L234)] [[Source](https://code.claude.com/docs/en/cross-session-messaging#limitations)]

#### [debug-your-config](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/debug-your-config.md) [[Source](https://code.claude.com/docs/en/debug-your-config)]

* The MCP troubleshooting table now also covers `.mcp.json` files that use a top-level `servers` key (VS Code's format) instead of `mcpServers`. [[line 91](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/debug-your-config.md?plain=1#L91)] [[Source](https://code.claude.com/docs/en/debug-your-config#check-common-causes)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_GOAL_CHECKIN_MINUTES` variable controls how long background work can keep an active goal waiting (default 30 minutes) before Claude is asked to check on it; set to `0` to disable check-ins. [[line 262](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/env-vars.md?plain=1#L262)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New "Context limit reached" interactive-mode error message replaces the plain `Prompt is too long` wording shown in the terminal, and now names when auto-compact is off and how to re-enable it via `/config`. [[lines 82-83](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/errors.md?plain=1#L82-L83)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]
* New "subagent_type is required" error entry, matching the `subagents.md` change above. [[line 134](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/errors.md?plain=1#L134)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]
* New "Message too large for cross-session delivery" entry documenting the refusal message and remediation steps. [[line 139](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/errors.md?plain=1#L139)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]
* New "The remote sent a reply this version can't display" entry for `/context` and `/btw` version mismatches against an attached cloud session; before v2.1.235 this showed a raw JavaScript error instead. [[line 78](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/errors.md?plain=1#L78)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]

#### [goal](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/goal.md) [[Source](https://code.claude.com/docs/en/goal)]

* New "Errors you have to fix clear the goal" section: an authentication failure, exhausted credit balance, uncompactable context overflow, or unavailable model now clears an active goal with a warning telling you to fix the cause and rerun `/goal`. [[line 109](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/goal.md?plain=1#L109)] [[Source](https://code.claude.com/docs/en/goal#errors-you-have-to-fix-clear-the-goal)]
* New "Background work defers evaluation" section: after 30 minutes (configurable) of background work keeping a goal waiting, Claude Code now asks Claude to check on it at each turn end. [[lines 120-123](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/goal.md?plain=1#L120-L123)] [[Source](https://code.claude.com/docs/en/goal#background-work-defers-evaluation)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* New "Check spelling as you type" section documents the v2.1.235 `spellcheck` feature end to end: prerequisites (`aspell`/`hunspell`/`ispell`), where the `spellcheck` setting can be set, per-checker/language/color options, what gets skipped (code-like text, CJK/Thai/Lao/Khmer/Myanmar text), and how to debug a checker that isn't underlining anything. [[line 362](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/interactive-mode.md?plain=1#L362)] [[Source](https://code.claude.com/docs/en/interactive-mode#check-spelling-as-you-type)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* New "Add a server from setup instructions written for another client" section walks through converting a URL, a launch command, or an `mcpServers` JSON block (as written for Claude Desktop, Cursor, etc.) into the equivalent `claude mcp add` / `claude mcp add-json` command. [[line 131](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/mcp.md?plain=1#L131)] [[Source](https://code.claude.com/docs/en/mcp#add-a-server-from-setup-instructions-written-for-another-client)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New `spellcheck` settings-reference entry, readable only from user settings, `--settings`, and managed settings (not project settings). [[line 303](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/settings.md?plain=1#L303)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* New line noting that an Agent tool call omitting `subagent_type` now fails with `subagent_type is required` when no `general-purpose` fallback exists. [[line 67](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/claude-code/sub-agents.md?plain=1#L67)] [[Source](https://code.claude.com/docs/en/sub-agents#built-in-subagents)]

-----

## API changes

### Changed documents

#### [access-transparency](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/access-transparency.md) [[Source](https://platform.claude.com/docs/en/manage-claude/access-transparency)]

* "Anthropic Workbench" renamed to "Playground (Claude Console)" in the Access Transparency coverage table. [[line 171](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/access-transparency.md?plain=1#L171)] [[Source](https://platform.claude.com/docs/en/manage-claude/access-transparency)]

#### [admin-api](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/admin-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api)]

* Role permissions table now says "Playground" instead of "Workbench" for the user, claude_code_user, developer, and billing roles. [[lines 82-85](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/admin-api.md?plain=1#L82-L85)] [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api)]

#### [agent-skills/enterprise](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/agents-and-tools/agent-skills/enterprise.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise)]

* New "Skill content scanning" section: Claude Enterprise orgs can turn on beta automated security scanning for custom Skills uploaded in claude.ai and Claude Cowork; a Skill that fails scanning is blocked, one that passes with a warning stays usable behind a caution notice. Scanning doesn't cover Skills uploaded via the Skills API or Claude Console. [[line 43](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/agents-and-tools/agent-skills/enterprise.md?plain=1#L43)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise)]
* Versioning strategy now warns that omitting `version` means requests use the latest version, so any workspace member's upload immediately changes what production agents run. [[line 164](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/agents-and-tools/agent-skills/enterprise.md?plain=1#L164)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise)]

#### [agent-skills/overview](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/agents-and-tools/agent-skills/overview.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)]

* Links to the new Skill content scanning feature described above. [[line 225](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/agents-and-tools/agent-skills/overview.md?plain=1#L225)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)]
* New pointer to the Skills API audit logging section (see `skills-guide.md` below). [[line 256](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/agents-and-tools/agent-skills/overview.md?plain=1#L256)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)]

#### [api-and-data-retention](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/api-and-data-retention.md) [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

* ZDR and HIPAA "what's not covered" sections now say "Claude Console, including Playground" instead of "Console and Workbench". [[lines 33, 54](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/api-and-data-retention.md?plain=1#L33-L54)]

#### [api/overview](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/api/overview.md) [[Source](https://platform.claude.com/docs/en/api/overview)]

* "Workbench" renamed to "Playground" when describing how to get API keys. [[line 56](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/api/overview.md?plain=1#L56)] [[Source](https://platform.claude.com/docs/en/api/overview)]

#### [build-with-claude/files](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Total storage limit per organization doubled from 500 GB to 1 TB. [[lines 249, 274](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/build-with-claude/files.md?plain=1#L249-L274)]
* New "Audit logging" section: Files API uploads, downloads, and deletions now appear in the Compliance API Activity Feed as `platform_file_uploaded`/`platform_file_content_downloaded`/`platform_file_deleted` activities (list/metadata calls are not recorded). [[line 260](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/build-with-claude/files.md?plain=1#L260)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]
* Files API rate limit raised out of beta from ~100 to ~500 requests per minute. [[line 305](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/build-with-claude/files.md?plain=1#L305)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

#### [build-with-claude/skills-guide](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/build-with-claude/skills-guide.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/skills-guide)]

* Production guidance now warns that omitting `version` or setting it to `"latest"` means any workspace member's upload changes production behavior immediately. [[line 576](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/build-with-claude/skills-guide.md?plain=1#L576)] [[Source](https://platform.claude.com/docs/en/build-with-claude/skills-guide)]
* New "Audit logging" section: Skill and Skill version creation/deletion now appear in the Compliance API Activity Feed. [[line 709](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/build-with-claude/skills-guide.md?plain=1#L709)] [[Source](https://platform.claude.com/docs/en/build-with-claude/skills-guide)]

#### [build-with-claude/vision](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/build-with-claude/vision.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/vision)]

* "Workbench" renamed to "Playground" as a way to try vision requests. [[line 16](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/build-with-claude/vision.md?plain=1#L16)] [[Source](https://platform.claude.com/docs/en/build-with-claude/vision)]

#### [cmek](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/cmek.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

* New guidance: attach a CMEK key to a *new* workspace before sending it traffic; attaching to a workspace that already receives requests can take up to a day to take effect, during which data is still encrypted with Anthropic-managed keys. [[line 23](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/cmek.md?plain=1#L23)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]
* "Encrypted" / "Not encrypted" sections renamed to "Encrypted with CMEK key" / "Encrypted with Anthropic key" for clarity. [[lines 53, 90](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/cmek.md?plain=1#L53-L90)]
* The personal-preferences disablement bullet was removed from the "disabled under CMEK" list and replaced with a new bullet: the "Instructions for Claude" section of personal preferences is now listed as encrypted with the Anthropic key (account-level, shared across orgs) instead of disabled. [[line 106](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/cmek.md?plain=1#L106)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

#### [cmek-aws-kms](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/cmek-aws-kms.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms)], [cmek-azure-key-vault](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/cmek-azure-key-vault.md), [cmek-google-cloud-kms](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/cmek-google-cloud-kms.md)

* Each provider guide adds the same new-workspace-first / up-to-a-day-to-take-effect guidance as `cmek.md` above. [[cmek-aws-kms line 187](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/cmek-aws-kms.md?plain=1#L187)] [[cmek-azure-key-vault line 221](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/cmek-azure-key-vault.md?plain=1#L221)] [[cmek-google-cloud-kms line 215](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/cmek-google-cloud-kms.md?plain=1#L215)]

#### [home](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/home.md) [[Source](https://platform.claude.com/docs/en/home)]

* "Try the Workbench" link renamed to "Try the API in Playground". [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/home.md?plain=1#L82)] [[Source](https://platform.claude.com/docs/en/home)]

#### [intro](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/intro.md) [[Source](https://platform.claude.com/docs/en/intro)]

* Developer Console description now points to Playground instead of the Workbench. [[line 66](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/intro.md?plain=1#L66)] [[Source](https://platform.claude.com/docs/en/intro)]

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* New August 18, 2026 entry formally announcing the Workbench → Playground rename: Playground supports every Messages API parameter, includes feature-demo templates, and shows the full SDK request/response for each run. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/release-notes/overview.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

#### [usage-cost-api](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/usage-cost-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/usage-cost-api)]

* FAQ heading and answer updated from "Anthropic Workbench" to "Playground", noting usage from the legacy Workbench is handled the same way. [[line 319](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/usage-cost-api.md?plain=1#L319)] [[Source](https://platform.claude.com/docs/en/manage-claude/usage-cost-api)]

#### [wif-providers/aws](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/wif-providers/aws.md) [[Source](https://platform.claude.com/docs/en/manage-claude/wif-providers/aws)], [wif-providers/azure](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/wif-providers/azure.md), [wif-providers/gcp](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/wif-providers/gcp.md), [wif-providers/github-actions](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/wif-providers/github-actions.md), [wif-providers/kubernetes](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/wif-providers/kubernetes.md), [wif-providers/okta](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/wif-providers/okta.md), [wif-providers/spiffe](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/wif-providers/spiffe.md)

* Each provider guide's "Verify the setup" section now describes a failed token exchange as an opaque `401 authentication_error` (`Authentication failed`) and points to the new authentication history page to find the deny reason, replacing the old `400 invalid_grant` wording. [[aws.md line 178](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/wif-providers/aws.md?plain=1#L178)] [[azure.md line 207](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/wif-providers/azure.md?plain=1#L207)] [[gcp.md line 174](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/wif-providers/gcp.md?plain=1#L174)] [[github-actions.md line 150](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/wif-providers/github-actions.md?plain=1#L150)] [[kubernetes.md line 155](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/wif-providers/kubernetes.md?plain=1#L155)] [[okta.md line 125](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/wif-providers/okta.md?plain=1#L125)] [[spiffe.md line 211](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/wif-providers/spiffe.md?plain=1#L211)]

#### [wif-reference](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/wif-reference.md) [[Source](https://platform.claude.com/docs/en/manage-claude/wif-reference)]

* All token-exchange failure causes that previously returned `400 invalid_grant` now return a uniform `401 authentication_error` with the fixed message `Authentication failed`; the specific deny reason (e.g. `match_subject_prefix`, `workspace_id_required`) is now visible on a new authentication history page instead of being logged server-side only. [[lines 217-224](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/wif-reference.md?plain=1#L217-L224)] [[Source](https://platform.claude.com/docs/en/manage-claude/wif-reference)]
* The `workspace_id_required` case moved from a `400 invalid_request` to this same `401` family, and a new `400 invalid_request_error` case covers a malformed (rather than missing) `workspace_id`. [[line 222](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/wif-reference.md?plain=1#L222)] [[Source](https://platform.claude.com/docs/en/manage-claude/wif-reference)]
* "Troubleshoot a failed exchange" section updated to match the new `401`/authentication-history behavior. [[line 238](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/wif-reference.md?plain=1#L238)] [[Source](https://platform.claude.com/docs/en/manage-claude/wif-reference)]

#### [workspaces](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/workspaces.md) [[Source](https://platform.claude.com/docs/en/manage-claude/workspaces)]

* Workspace User role description now says "Use Playground only" instead of "Use the Anthropic Workbench only". [[line 37](https://github.com/gpambrozio/ClaudeDocs/blob/a4c0b7cc904864ceafdbb4d43d5b0b31ba9256fc/docs-md/api/manage-claude/workspaces.md?plain=1#L37)] [[Source](https://platform.claude.com/docs/en/manage-claude/workspaces)]

*Note: several `docs-md/api/api/compliance/**` pages (activities/list, organizations, organizations/list, roles, roles/permissions, roles/permissions/list, roles/retrieve, settings, users, users/list) showed large diffs today, but these were crawl failures — the pages rendered as repeated "Loading" placeholders rather than real content — so they're excluded from this changelog as not reflecting an actual documentation change.*
