# [Claude docs changes for September 25th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/2a4d4457642c76a5475c6592531eb7bcccc6a5e9) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/2a4d4457642c76a5475c6592531eb7bcccc6a5e9)]

## Executive Summary
- **Claude Code plugin docs were overhauled**: the old single-page guides were rewritten into short overview pages and split into a new `docs-md/claude-code/plugins/` section of 20 focused pages (installing, creating, publishing, org controls, dependencies, measuring cost/usage, troubleshooting, and more).
- **Claude Code 2.1.282** ships a large set of reliability fixes for resumed/continued sessions losing extended thinking or re-sending turns in a changed form, several vim-mode and rendering bugs, a new `maxProseWidth` setting, telemetry-ignored-variable startup warnings, and a big Slack/Claude Tag and cloud-sessions bug-fix batch.
- **Claude API is resuming billing for pre-output refusals** in the `bio`, `frontier_llm`, and `reasoning_extraction` categories (previously every pre-output refusal was free); mid-stream refusals are unaffected.
- **Cache diagnostics graduated from beta to GA** on the Claude API — no beta header needed, just send the `diagnostics` object.
- **Claude Code Projects threads can now run on your own machine** through Remote Control instead of only in the cloud, and auto mode's server-side classifier review now covers read-only/sandboxed shell commands and denies actions when the server gives no verdict.

-----

## New Claude Code versions

### [2.1.282](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/versions/2.1.282.md)

#### New features

* Added a `maxProseWidth` setting that caps the width of Claude's prose in wide terminals while tables and code blocks keep the full width
* Added a startup notice, and `/status` and `claude doctor` entries, listing telemetry variables in a project's settings files that were ignored or that turned telemetry off
* Added the `allowClaudeInChromeWithManagedMcp` managed setting to let `claude --chrome` run alongside an exclusive `managed-mcp.json`; the error shown when Chrome is blocked now names it
* Added `store.readiness_grace_seconds` to the Claude apps gateway so `/readyz` can stay ready through a short Postgres outage such as a database failover
* Added a scrollbar to the `/feedback` drafts list in fullscreen mode
* [Cloud sessions] Added Claude GitHub App status to Settings › Connectors › GitHub, plus "Open repository"/"Open compare page" links for non-GitHub repositories and support for attaching a repository from a different GitHub owner (such as a fork's upstream) to a running cloud session

#### Existing feature improvements

* Changed auto mode to use the server-side classifier by default on a direct Anthropic API connection when telemetry is off (`CLAUDE_CODE_AUTO_MODE_SERVER=0` opts out)
* Changed `sandbox.excludedCommands` to ignore project and local settings entries when managed settings, `--settings`, or `allowManagedDomainsOnly` restrict unsandboxed commands or domains
* Changed project and local settings to ignore OpenTelemetry variables that turn on export, set its endpoint, or capture content (e.g. `CLAUDE_CODE_ENABLE_TELEMETRY`, `OTEL_LOG_*`)
* Changed Windows/WSL managed settings so an invalid or unreadable admin policy no longer blocks user-writable HKCU and WSL `/etc/claude-code` settings from applying
* Changed `Skill(anthropic-skills:*)`/`Skill(claude-ai:*)` allow rules, skill/command loading, and MCP servers named `anthropic-skills` or `claude-ai` to only apply to content actually synced from claude.ai, not plugins or MCP servers that merely reuse the name
* Improved the time to resume very large sessions, including ones never compacted
* Improved `/artifacts`: aligned titles, whole-item detail truncation, and PgUp/PgDn/Home/End/mouse-wheel support
* Improved the Windows EBADF resume error and the Claude Desktop unknown-model error messages
* Updated the `claude-api` skill: refusal billing links to the new docs, mid-stream refusals bill at normal rates, pre-output refusals count against rate limits, and it recommends `ant apply` for Managed Agents resources
* [Cloud sessions] Improved load time for the Routines page and sidebar Scheduled list for accounts with many past scheduled check-ins
* [Claude Tag] Changed bordered Slack cards (plans, tables, details) to render wide by default, and newly connected Slack workspaces now follow the current default model

#### Major bug fixes

* Fixed every request failing with a 400 when conversation history holds web search results the API can't decrypt (e.g. from a turn answered through a third-party gateway)
* Fixed `--continue`/`--resume` sessions re-sending earlier messages in a changed form, which could make the API drop Claude's earlier reasoning, including when thinking was dropped by an immediate slash command or a `--tools` list missing a previously offered built-in tool
* Fixed sessions failing every turn with an "Invalid `data` in `redacted_thinking` block" error by dropping thinking blocks and retrying once
* Fixed compaction failing on a refused summarization request by retrying on a fallback model
* Fixed a failed turn after a safety-related model switch in sessions with thinking off and effort above high
* Fixed model-switch and Fable usage-credit prompt handling in SDK-hosted and Remote Control sessions
* Fixed a login error blocking requests for up to a minute after another Claude Code process refreshing auth was closed or killed mid-refresh
* Fixed CLAUDE.md/rules being read through a repository symlink that reaches macOS's `/Network` or a `/.vol`-style kernel path
* Fixed Bash permission rules with a mid-pattern `:*` being skipped in settings files while `--allowedTools` honored them
* Fixed managed settings ignoring a mistyped boolean lock key (e.g. `disableClaudeAiConnectors`, `allowManagedPermissionRulesOnly`) instead of enforcing the locked value
* Fixed managed `permissions`, `autoMode`, `worktree`, and `attribution` settings being ignored entirely when one nested value was invalid
* Fixed skills/commands/skills-directory plugin manifests pre-approving their own tools via `allowed-tools` under `allowManagedPermissionRulesOnly`
* Fixed tool input validation errors naming only one bad parameter when several were invalid in the same call
* Fixed several rendering/input bugs: pasted multi-line text submitted line-by-line after bracketed-paste reset, blank-screen flash before fullscreen's first frame, garbled rows after the terminal shrank, a stale character after a wrapped CJK/emoji redraw, and cursor placement issues in `/skills` search and vim mode (`>>`, `r`, `2J`, `dd`/`dj`/`dG`/`p`/`P`, `.` repeat counts)
* Fixed `/install-github-app` continuing remaining steps after "cancelled", and `/feedback`/`/bug`/`/share` on third-party providers still saving reports after a cancelled save
* Fixed plugin uninstall deleting a plugin's saved options/secrets when its settings file was unreadable or the installed-plugins list couldn't be read
* [VSCode] Fixed long replies falling behind the stream, the dictation mic covering the input scrollbar, and Remote Control sessions started locally not opening from the Web session list
* [Claude Tag] Fixed several Slack/Enterprise Grid bugs: auto-join patterns ignored org-wide, cross-workspace channel routing, retired-model fallback loops, table captions on uploaded files, thread naming in Agents & tools view, and inflated cost/token totals after a worker restart

-----

## Claude Code changes

### New Documents

The plugin documentation was split out of a handful of long top-level pages into a dedicated `docs-md/claude-code/plugins/` section:

#### [overview](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugins/overview.md) [[Source](https://code.claude.com/docs/en/plugins/overview)]

What a plugin is, when to use one instead of a standalone skill/subagent/hook/MCP server, and what an enabled plugin costs in context and permissions.

#### [install](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugins/install.md) [[Source](https://code.claude.com/docs/en/plugins/install)]

Install and manage plugins on any surface (terminal, desktop, IDE, cloud), choose an install scope, add marketplaces, and keep plugins updated.

#### [create](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugins/create.md) [[Source](https://code.claude.com/docs/en/plugins/create)]

Build a plugin with skills, agents, hooks, and MCP servers, and develop it locally with `--plugin-dir` before publishing.

#### [create-marketplace](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugins/create-marketplace.md) [[Source](https://code.claude.com/docs/en/plugins/create-marketplace)]

Build and test a `marketplace.json` locally before hosting it.

#### [host-marketplace](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugins/host-marketplace.md) [[Source](https://code.claude.com/docs/en/plugins/host-marketplace)]

Host a marketplace, including authenticating archive downloads with a `headersHelper` command.

#### [publish](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugins/publish.md) [[Source](https://code.claude.com/docs/en/plugins/publish)]

Share a plugin without a marketplace, or submit it to Anthropic's community marketplace.

#### [manifest-reference](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugins/manifest-reference.md) [[Source](https://code.claude.com/docs/en/plugins/manifest-reference)]

Full `plugin.json` field reference: types, defaults, path rules, `userConfig`, channels, and environment variables.

#### [marketplace-reference](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugins/marketplace-reference.md) [[Source](https://code.claude.com/docs/en/plugins/marketplace-reference)]

Reference for every field a marketplace entry accepts, including the `command` plugin source.

#### [components](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugins/components.md) [[Source](https://code.claude.com/docs/en/plugins/components)]

Every component type a plugin can hold (skills, agents, hooks, MCP servers, LSP servers, monitors) with an interactive plugin-directory explorer.

#### [loading](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugins/loading.md) [[Source](https://code.claude.com/docs/en/plugins/loading)]

How plugins are found on disk, cached, auto-updated, and synced from claude.ai, plus Node.js package dependencies.

#### [dependencies](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugins/dependencies.md) [[Source](https://code.claude.com/docs/en/plugins/dependencies)]

Declare version-constrained plugin dependencies and bundle a curated plugin set behind one install (mirrors the rewritten `plugin-dependencies.md`).

#### [relevance](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugins/relevance.md) [[Source](https://code.claude.com/docs/en/plugins/relevance)]

Add a `relevance` block to marketplace entries so Claude Code suggests plugins based on session signals (mirrors the rewritten `plugin-relevance.md`).

#### [cli-hints](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugins/cli-hints.md) [[Source](https://code.claude.com/docs/en/plugins/cli-hints)]

Emit a `<claude-code-hint />` tag from your own CLI/SDK to prompt users to install your official-marketplace plugin (mirrors the rewritten `plugin-hints.md`).

#### [measure](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugins/measure.md) [[Source](https://code.claude.com/docs/en/plugins/measure)]

New page: measure a plugin's token cost and usage, and pick telemetry events for org-wide plugin questions.

#### [org](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugins/org.md) [[Source](https://code.claude.com/docs/en/plugins/org)]

Managed-settings controls for administrators: require/allowlist marketplaces, pre-install plugins, and restrict what users can install.

#### [security](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugins/security.md) [[Source](https://code.claude.com/docs/en/plugins/security)]

Plugin security and trust model, and Anthropic's official marketplace names.

#### [anthropic-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugins/anthropic-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugins/anthropic-marketplaces)]

Distinguishes Anthropic's official, community, and demo marketplaces from Claude Marketplace (claude.com/marketplace).

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugins/cli-reference.md) [[Source](https://code.claude.com/docs/en/plugins/cli-reference)]

Reference for every `claude plugin` shell subcommand.

#### [code-intelligence](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugins/code-intelligence.md) [[Source](https://code.claude.com/docs/en/plugins/code-intelligence)]

Ship LSP servers and other code-intelligence components in a plugin.

#### [troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugins/troubleshooting.md) [[Source](https://code.claude.com/docs/en/plugins/troubleshooting)]

Every `claude plugin validate` message and load/dependency error with its fix.

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

New comprehensive reference for every `gateway.yaml` option: listener/TLS, OIDC, session, Postgres store, per-provider upstreams (Anthropic, Bedrock, Claude Platform on AWS, Google Cloud, Microsoft Foundry), static upstream headers, model routing, managed policies, and telemetry.

### Changed documents

#### [claude-projects](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/claude-projects.md) [[Source](https://code.claude.com/docs/en/claude-projects)]

* Project threads can now run on your own machine through [Remote Control](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/claude-projects.md?plain=1#L381-L389) instead of only as cloud sessions, when a task needs something only your computer has; requires Claude Code v2.1.280+ on that machine and doesn't work with **Require trusted devices** on.

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* Added [The server returned no safety verdict](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/errors.md?plain=1#L1930) covering auto mode's new denial-on-no-verdict behavior and the 10-in-a-row turn stop
* Added recovery documentation for `role 'system' must precede an 'assistant' message` (Claude Code now retries once with the text as a user message) and `Invalid encrypted_content in search_result block` / `Failed to decrypt web search result content`

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* Added a **Text fields** section clarifying that a bound bare letter/digit/Space still types normally in a focused text field (e.g. the "Other" answer to a Claude question)

#### [managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/managed-settings.md) [[Source](https://code.claude.com/docs/en/managed-settings)]

* Documents that claude.ai now itself enforces the admin console's `strictKnownMarketplaces`/`blockedMarketplaces` lists when a marketplace is added from claude.ai or Cowork's **Customize** tab
* Added a full table of fallback behavior when a managed boolean/allowlist key (e.g. `allowManagedHooksOnly`, `disableCommandPluginSources`, `crossSessionInbound`) is present but invalid, matching 2.1.282's fix

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Rewrote [Server-side classifier review](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/permission-modes.md?plain=1#L310-L322) to cover which session types ask the server by default (now including telemetry-disabled direct-API sessions as of 2.1.282) and the two non-review outcomes (fallback to local classifier vs. denial on no verdict)
* Documents that read-only and sandboxed shell commands now also wait for server-side review and are blocked if flagged

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Documents that project/local settings can no longer set `CLAUDE_CODE_ENABLE_TELEMETRY` and other OpenTelemetry variables that turn on export or capture content (requires v2.1.282); the off-values that still apply are listed separately

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* Expanded [Variables Claude Code ignores in `env`](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/settings-reference.md?plain=1#L2747-L2772) with the full telemetry-variable ignore list, the startup notice, and how `/status`/`claude doctor` report it

#### plugins.md, plugins-reference.md, discover-plugins.md, plugin-marketplaces.md

* Rewritten into shorter overview/landing pages ([Plugins overview](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugins.md), [Plugin manifest reference](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugins-reference.md), [Install and manage plugins](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/discover-plugins.md), [Create a marketplace](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugin-marketplaces.md)) that route into the new `plugins/` section rather than covering everything themselves

#### plugin-dependencies.md, plugin-relevance.md, plugin-hints.md, plugin-evals.md

* [plugin-dependencies](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugin-dependencies.md), [plugin-relevance](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugin-relevance.md), and [plugin-hints](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugin-hints.md) were reworded and now mirror the content of their new `plugins/` counterparts
* [plugin-evals](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/claude-code/plugin-evals.md) (renamed "Test plugins with evals") got an updated intro; it remains distinct from the new `plugins/measure.md` cost/usage page

Many other pages (`claude-directory.md`, `admin-setup.md`, `sub-agents.md`, `settings-example.md`, etc.) changed only in the links they use to point at the new `plugins/` paths, with no content change.

-----

## API changes

### New Documents

#### [managed-agents/quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/api/managed-agents/quickstart.md) [[Source](https://platform.claude.com/docs/en/managed-agents/quickstart)]

New end-to-end tutorial for Claude Managed Agents: install the `ant` CLI and SDKs, create an agent and environment, start a session, and stream its events, plus links to four framework-specific "build a complete app" quickstarts (Chat SDK, assistant-ui, CopilotKit).

### Changed documents

#### [about-claude/models/optimizing-for-cost-and-intelligence](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/api/about-claude/models/optimizing-for-cost-and-intelligence.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence)]

* Added a new **Show the model elapsed time** technique: a system-prompt instruction plus a per-turn elapsed-time message, benchmarked by Anthropic on DRACO, HLE, and an internal physics set, showing meaningful time/cost cuts for a small, benchmark-dependent score change

#### [build-with-claude/cache-diagnostics](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/api/build-with-claude/cache-diagnostics.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics)]

* Cache diagnostics is now **GA** on the Claude API: the `cache-diagnosis-2026-04-07` beta header is no longer required, sending the `diagnostics` object is itself the opt-in, and the response field is now `null` (not omitted) whenever diagnostics wasn't requested

#### [build-with-claude/refusals-and-fallback](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/api/build-with-claude/refusals-and-fallback.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)]

* [How refusals are billed](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/api/build-with-claude/refusals-and-fallback.md?plain=1#L196-L206) now documents that pre-output refusals in the `bio`, `frontier_llm`, and `reasoning_extraction` categories are billed at normal rates (to deter attempts to circumvent safeguards at scale); other categories, and mid-stream refusals' existing billing, are unchanged. Applies on every platform.

#### [build-with-claude/mid-conversation-system-messages](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/api/build-with-claude/mid-conversation-system-messages.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages)]

* Mid-conversation tool changes on the Claude API now use a single `inline-tools-2026-09-15` beta header (covering both tool-reference changes and inline tool definitions); the older `mid-conversation-tool-changes-2026-07-01` header still works for by-reference changes on the Claude API, Amazon Bedrock, and Google Cloud, but not for inline tool definitions

#### [build-with-claude/structured-outputs](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/api/build-with-claude/structured-outputs.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

* The deprecated `output_format` parameter now requires the `structured-outputs-2025-11-13` beta header again; without it the API returns a 400 (previously accepted without a header during a transition period)

#### [build-with-claude/preserved-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/api/build-with-claude/preserved-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking)]

* Clarifies that `"drop_block"` doesn't fix the underlying prefix edit and can *increase* a session's token usage, since Claude may re-derive the reasoning it lost; recommends alerting on `prefix_binding_mismatch` entries and fixing the edit instead

#### [manage-claude/compliance-activity-feed](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/api/manage-claude/compliance-activity-feed.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed)]

* Documents that, as of September 24, 2026, `filename`/`title` fields on file, project-document, and artifact activities are always empty/omitted (including on past activities); names must now be looked up by ID through the [metadata endpoints](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/api/manage-claude/compliance-content-data.md) with `read:compliance_user_data`

#### [manage-claude/compliance-sessions](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/api/manage-claude/compliance-sessions.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-sessions)]

* Compliance API local session endpoints are now **stable** (out of beta) for Claude for Microsoft 365 sessions (Excel, PowerPoint, Word, Outlook), alongside Cowork and Claude Code; Claude Science and Claude in Chrome remain beta

#### [manage-claude/inference-hooks](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/api/manage-claude/inference-hooks.md) [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks)]

* Added [Continue a conversation after a denied request](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/api/manage-claude/inference-hooks.md?plain=1#L1) with per-app recovery steps (claude.ai/Desktop, Claude Code `/rewind`, Cowork, Claude Tag's `!restart`) for removing denied content before retrying

#### [manage-claude/cmek-aws-kms](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/api/manage-claude/cmek-aws-kms.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms)]

* Expanded key-policy and troubleshooting guidance: locating a workspace's compartment ID, the optional `EncryptionContext`/`aws:SourceArn` conditions that scope a key to specific workspaces, and diagnosing a denied attach via CloudTrail

#### [managed-agents/self-hosted-sandboxes](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/api/managed-agents/self-hosted-sandboxes.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

* Added Go SDK support for self-hosted workers (`EnvironmentWorker`, `work.poller()`/`HandleItem()`, `agenttoolset.BetaAgentToolset20260401`), alongside Python and TypeScript
* Documents `memory_sync_interval`/`memory_sync_deletions` for tuning how attached memory stores reconcile and handle local deletions, and how to run custom tools or MCP-backed tools through the SDK worker

#### [managed-agents/environments](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/api/managed-agents/environments.md) [[Source](https://platform.claude.com/docs/en/managed-agents/environments)]

* Added `allow_package_managers`, which opens outbound access to a maintained list of public package registries/code hosts; required whenever an environment specifies `packages`, with a note on the prompt-injection/exfiltration risk of host-level (not per-operation) network access

#### API reference (all languages)

* The full per-language API reference (`api/api/beta/**` under `cli`, `csharp`, `go`, `java`, `php`, `python`, `ruby`, `typescript`) was regenerated with expanded parameter documentation and constraints for existing and new `beta.messages.create` fields: request-level `compaction`, `diagnostics` (cache diagnostics, now unconditional), `speed: "fast"`, `thinking.block_binding` drop-on-mismatch controls, response `container` info, and sparse per-member overrides for agent-team requests. Representative page: [api/beta/messages/create](https://github.com/gpambrozio/ClaudeDocs/blob/2a4d4457642c76a5475c6592531eb7bcccc6a5e9/docs-md/api/api/beta/messages/create.md).
