# [Claude docs changes for October 2nd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/a50fdff82f21c650e7e2dad81922509a5d710c66) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/a50fdff82f21c650e7e2dad81922509a5d710c66)]

## Executive Summary
- **Claude Mods**: Claude Code 2.1.287 introduces mods, which are plugins made of JavaScript/TypeScript event handlers that run inside Claude Code. They can draw panes and bands, redraw built-in UI, intercept tool calls and add commands. A new 10-page `plugins/mods/` guide set covers them, along with admin controls (`prependPlugins` / `appendPlugins`).
- **Sandboxing docs reworked**: the sandboxing guide was reorganized around "what the sandbox restricts", credential masking, `excludedCommands` rules and a new "admin-required" sandbox that ignores repository-level sandbox settings.
- **Self-hosted sandboxes for Managed Agents**: the single guide was split into five pages covering workers, custom tools, memory, operations and a reference.
- **New Admin API endpoints**: organization analytics (usage, cost, per-user reports, summaries, chat projects), spend limits (set, list, effective) and RBAC group member add/remove.
- **New diff panel and usage-limit auto-continue** in interactive mode, plus a big expansion of the error reference.

## New Claude Code versions

### [2.1.287](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/versions/2.1.287.md)

#### New features

* Added Claude Mods: plugins can now modify deeper behavior of Claude Code
* Added "You should know", a built-in mod where a side agent flags things you or Claude might miss (`/plugin enable cc-plugin-you-should-know@builtin`)
* Added an `n:<text>` filter to the agents view that matches session names and tasks
* Added `prompt_text` to the OpenTelemetry `user_prompt` event
* Added URL prompts from MCP servers on the 2025-11-25 protocol, for example to sign in (servers that stop connecting may need `"bareElicitationCapability": true`)
* Windows: added a startup warning when denying the Bash tool also turns off PowerShell
* Self-hosted runner: added a built-in REST-only `gh api` where the GitHub CLI isn't installed
* VS Code: added "Run in background" for running commands and sub-agents, and background shell/Monitor output in agent map cards

#### Existing feature improvements

* `/config` is easier to navigate: cycling settings step both ways with ←/→, narrow terminals stack values, PgUp/PgDn page the list
* Clearer plugin marketplace errors, plugin dependency notes, and retry of unfinished plugin installs
* Opus 4.7+ and Fable now use a 1M context window by default on Bedrock, Vertex, Foundry and the Claude apps gateway (`CLAUDE_CODE_DISABLE_1M_CONTEXT=1` keeps 200K)
* MCP `alwaysLoad: false` now defers all of that server's tools behind tool search
* Better handling of large MCP tool results (less memory, smaller session files)
* Automatic model switches after a flagged message keep your current effort level
* Replies from `claude agents` arrive as queued messages; waiting permission prompts show oldest first
* Whole-tool `Bash` allow rules and allowing hooks now prompt for shell writes to files the file tools refuse (profile store, credentials file)
* Files sent from cloud/Remote Control sessions are retried once on transient failures and large files stream from disk
* Windows: faster Bash tool

#### Major bug fixes

* Fixed a dangerous `rm` losing its always-ask safeguard when the command also redirected output to a `~` or wildcard path
* Fixed Remote Control missing messages for minutes after an unanswered reconnect request, and failing to register behind an HTTP proxy
* Fixed switching between Opus 5.5 and Sonnet 5.5 dropping earlier extended thinking
* Fixed Bedrock Guardrails mid-response blocks ending the turn with an API error
* Fixed a folder's CLAUDE.md being attached twice after resume or compaction
* Fixed cloud sessions losing earlier conversation when restarted during compaction
* Fixed `/advisor` pairing checks (Sonnet 5.5 can advise Opus 4.7 and 4.8)
* Fixed Windows interactive `claude` hanging with piped input
* Many screen reader mode fixes

-----

## Claude Code changes

### New Documents

#### [Mods admin](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/plugins/mods/admin.md) [[Source](https://code.claude.com/docs/en/plugins/mods/admin)]

How organizations manage mods: running org mods before or after user-installed ones with `prependPlugins` / `appendPlugins`, and controlling what mods may do.

#### [Mods API](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/plugins/mods/api.md) [[Source](https://code.claude.com/docs/en/plugins/mods/api)]

API a mod can call, including adding a `/command` or a tool that runs your function with no Claude turn.

#### [Mods create](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/plugins/mods/create.md) [[Source](https://code.claude.com/docs/en/plugins/mods/create)]

How to ask Claude to write a mod, or write one yourself, and load it with `--plugin-dir`.

#### [Mods events](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/plugins/mods/events.md) [[Source](https://code.claude.com/docs/en/plugins/mods/events)]

Event hooks a mod can handle: guarding or changing tool calls, following a turn, and so on.

#### [Mods gallery](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/plugins/mods/gallery.md) [[Source](https://code.claude.com/docs/en/plugins/mods/gallery)]

Example mods with code.

#### [Mods interface](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/plugins/mods/interface.md) [[Source](https://code.claude.com/docs/en/plugins/mods/interface)]

Drawing panes and bands with tabs, buttons and text fields, and changing what Claude Code already draws (tool rows, spinner, dialogs).

#### [Mods overview](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/plugins/mods/overview.md) [[Source](https://code.claude.com/docs/en/plugins/mods/overview)]

What mods are, how they differ from settings hooks, skills and MCP servers, how to install them, sample mods, trust considerations, and where mods run (CLI and Desktop Code tab).

#### [Mods reference](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/plugins/mods/reference.md) [[Source](https://code.claude.com/docs/en/plugins/mods/reference)]

Reference for mod files, hooks and calls.

#### [Mods test](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/plugins/mods/test.md) [[Source](https://code.claude.com/docs/en/plugins/mods/test)]

How to test a mod.

#### [Mods troubleshoot](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/plugins/mods/troubleshoot.md) [[Source](https://code.claude.com/docs/en/plugins/mods/troubleshoot)]

Troubleshooting mods that don't load or behave as expected.

### Changed documents

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Added an "Auto mode availability" section: available to all Anthropic API users on Opus 4.6+, Sonnet 4.6+ or Fable.

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_DISABLE_AUTH_REFRESH_LOCK` and `CLAUDE_CODE_DISABLE_WEB_FETCH` variables. [[line 228](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/env-vars.md?plain=1#L228)] [[line 263](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/env-vars.md?plain=1#L263)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CLAUDE_AX_PREPARK_MS` default changed from `50` to `0`. [[line 188](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/env-vars.md?plain=1#L188)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `ANTHROPIC_FOUNDRY_RESOURCE` now refuses a URL or host name. [[line 163](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/env-vars.md?plain=1#L163)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* Many new entries: advisor less capable than main model, Foundry resource must be a resource name, piped input in interactive mode, GitHub IP allow list/SSO/Conditional Access blocks, `/recap` in routines, WebFetch preflight failures, network-share publish failures, and expanded sign-in and retry guidance.

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Notes that plugins can register function hooks (mods). [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/hooks.md?plain=1#L9)] [[Source](https://code.claude.com/docs/en/hooks#hooks-reference)]
* `/hooks` browser description simplified; added an `All events` entry. [[lines 670-678](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/hooks.md?plain=1#L670-L678)] [[Source](https://code.claude.com/docs/en/hooks#the-hooks-menu)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* New diff panel (v2.1.287+) in fullscreen rendering: `ask` button to attach a file's diff, per-turn `source` picker, and `Ctrl+X B` to change the comparison base. The classic renderer keeps a diff dialog.
* Documented auto-continue after a usage limit resets, including the case where the computer slept.

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* New "Effort level after a fallback" section: the fallback model keeps the flagged request's effort level. [[lines 517-528](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/model-config.md?plain=1#L517-L528)] [[Source](https://code.claude.com/docs/en/model-config#effort-level-after-a-fallback)]

#### [memory](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Auto memory toggle can't be turned back on in background sessions or sessions started by another Claude Code session. Clarified lazy loading of subdirectory `CLAUDE.md` files and path-scoped rules.

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Server-side auto mode review now applies to `-p`, Agent SDK, VS Code and desktop sessions on any plan. [[line 321](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/permission-modes.md?plain=1#L321)] [[Source](https://code.claude.com/docs/en/permission-modes#server-side-classifier-review)]
* A mod handling `tool.check` can approve actions before the classifier. [[line 495](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/permission-modes.md?plain=1#L495)] [[Source](https://code.claude.com/docs/en/permission-modes#how-auto-mode-evaluates-actions)]
* Reading another organization's public artifact needs approval, which `dontAsk` mode can't give. Directories loaded with `--plugin-dir` are now protected.
* Removed "as of v2.1.198" version qualifiers from classifier block rules.

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Documented how mods extending permissions interact with ask rules, PreToolUse blocks, the classifier and deny rules.

#### [plugins/loading](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/plugins/loading.md) [[Source](https://code.claude.com/docs/en/plugins/loading)]

* New rules for installing a plugin's npm/Bun dependencies from a lockfile: registry packages only, pinned versions, `https` downloads, no overrides or patches.

#### [prompt-library](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/prompt-library.md) [[Source](https://code.claude.com/docs/en/prompt-library)]

* Prompts reworked to use fill-in `{slot}` placeholders with example values and "teaches" descriptions.

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Reorganized with "What the sandbox restricts" and "What runs outside the sandbox" sections (file/web tools, hooks, MCP servers, `!` commands, excluded commands, unsandboxed retries).
* Explained how each permission mode handles the unsandboxed retry, and added strict sandbox mode.
* Added `excludedCommands` matching rules and "admin-required" sandbox, where repository settings are ignored.
* Credential masking now covers environment variables and credential files, with `injectHosts`, TLS termination and macOS/Linux differences.

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* New `prependPlugins` and `appendPlugins` settings for org-run mods. [[line 556](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/settings-reference.md?plain=1#L556)] [[Source](https://code.claude.com/docs/en/settings-reference#settings-index)]
* Managed permission-only setting now also makes v2.1.282+ ignore `allowed-tools` frontmatter in untrusted skills. [[line 1339](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/settings-reference.md?plain=1#L1339)] [[Source](https://code.claude.com/docs/en/settings-reference#allowmanagedpermissionrulesonly)]
* Sandbox settings now note limits on project/local scopes; `failIfUnavailable` behavior clarified; `excludedCommands` skips `git clone`/`init`/`worktree` with outside paths. [[line 1817](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/settings-reference.md?plain=1#L1817)] [[Source](https://code.claude.com/docs/en/settings-reference#sandboxexcludedcommands)]
* AWS credential re-signing pairing rules documented. [[line 2386](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/settings-reference.md?plain=1#L2386)] [[Source](https://code.claude.com/docs/en/settings-reference#sandboxcredentialsawspairs)]
* `claudeInChromeDefaultEnabled` now also applies to the VS Code extension. [[line 583](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/claude-code/settings-reference.md?plain=1#L583)] [[Source](https://code.claude.com/docs/en/settings-reference#settings-index)]

-----

## API changes

### New Documents

#### [Add RBAC Group Member](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/api/api/beta/organization/rbac_groups/members/add.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/rbac_groups/members/add)]

`POST /v1/organizations/rbac_groups/{rbac_group_id}/members` adds a user to an RBAC group. SCIM-provisioned groups can't be modified this way.

#### [Remove RBAC Group Member](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/api/api/beta/organization/rbac_groups/members/remove.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/rbac_groups/members/remove)]

Removes a user from an RBAC group.

#### [Analytics reports](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/api/api/beta/organization/analytics/summaries.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/analytics/summaries)]

New organization analytics endpoints under `/v1/organizations/analytics/`: `summaries` (activity summaries), `usage_report`, `cost_report`, `user_usage_report` and `user_cost_report` (per-user token usage and cost), and `apps/chat/projects` (per-project chat activity with cursor pagination). Each has a list page.

#### [Spend limits](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/api/api/beta/organization/spend_limits/set.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/spend_limits/set)]

New `POST /v1/organizations/spend_limits` to set (upsert by scope and period) a spend limit, plus `list` and `effective` (list effective spend limits) endpoints.

#### [Self-hosted sandboxes: custom tools](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/api/managed-agents/self-hosted-sandboxes-custom-tools.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-custom-tools)]

Serve custom tools from a self-hosted sandbox worker, and wrap an MCP server inside your network as custom tools without a tunnel.

#### [Self-hosted sandboxes: memory](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/api/managed-agents/self-hosted-sandboxes-memory.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-memory)]

Attach memory stores to self-hosted sandbox sessions: prepare the host, configure sync, handle read-only stores and conflicts.

#### [Self-hosted sandboxes: operations](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/api/managed-agents/self-hosted-sandboxes-operations.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-operations)]

Read queue depth, stop sessions and workers without losing work, and fix common failures.

#### [Self-hosted sandboxes: reference](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/api/managed-agents/self-hosted-sandboxes-reference.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-reference)]

`ant` CLI flags, environment variables, host requirements, filesystem paths and SDK helper options for workers.

#### [Self-hosted sandboxes: workers](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/api/managed-agents/self-hosted-sandboxes-workers.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-workers)]

How workers claim work (always-on or webhook-triggered) and where sessions run (one process or one sandbox per session).

### Changed documents

#### [Self-hosted sandboxes](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/api/managed-agents/self-hosted-sandboxes.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

* Trimmed to an overview; detailed content moved into the five new sub-pages above.

#### [Beta API reference (messages, memory stores, organization, SDKs)](https://github.com/gpambrozio/ClaudeDocs/blob/a50fdff82f21c650e7e2dad81922509a5d710c66/docs-md/api/api/beta/memory_stores.md) [[Source](https://platform.claude.com/docs/en/api/beta/memory_stores)]

* Added the `spend-limit-reads-2026-09-26` beta header value across the beta endpoints and the language SDK references (Go, Java, Python, TypeScript, Ruby, C#, PHP, CLI).
* The spend limits, increase requests and organization analytics (users, skills, connectors) references were substantially regenerated; much of the remaining churn in the beta pages is field reordering.
