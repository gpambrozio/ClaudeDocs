# [Claude docs changes for June 17th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/5cc66dc1) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/5cc66dc1)]

## Executive Summary
- **New Admin Analytics APIs**: Comprehensive analytics suite added with endpoints for activity summaries, token usage, cost reporting, per-user activity, skill usage, connector usage, and chat project usage
- **New Spend Limits API**: Full API for managing per-user spend limits on Claude Enterprise, including approval workflows for member increase requests
- **New Service Accounts & Federation APIs**: Service account management (CRUD) plus OIDC/JWT federation with Issuers and Rules for non-human identity
- **New permission rule syntax `Tool(param:value)`**: Deny and ask rules can now match any top-level tool input parameter (e.g., `Agent(model:opus)` to block Opus subagents)
- **Nested `.claude/` directory support**: Skills, subagents, and workflows now load from nested directories closest to the working directory, with qualified names for conflict resolution

## New Claude Code versions

### [2.1.178](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/versions/2.1.178.md)

#### New features

* Added `Tool(param:value)` syntax for permission rules to match a tool's input parameters (with `*` wildcard), e.g., `Agent(model:opus)` to block Opus subagents
* Skills in nested `.claude/skills` directories now load when working on files there; on a name clash, the nested skill appears as `<dir>:<name>` so both stay available
* Nested `.claude/` directories: the agent, workflow, and output-style closest to the working directory now wins when names collide; project-scope workflow saves now target the closest existing `.claude/workflows/`

#### Existing feature improvements

* Improved auto mode: subagent spawns are now evaluated by the classifier before launch, closing a gap where a subagent could request a blocked action without review
* Improved `/doctor` with consistent flat tree layout across all sections, clearer section status icons, and highlighted command names
* Improved Remote Control error messages: connection failures now show a persistent red "/rc failed" indicator in the footer; the "not yet enabled" error now explains whether it's a gate, a check failure, stale entitlement, or org policy
* Improved the skill listing truncation warning to show how many skill descriptions are affected
* Changed the workflow prompt keyword to use a purple shimmer highlight and trigger only on explicit phrases like "run a workflow" or "workflow:", not on any mention of the word
* `/bug` now requires a description before submitting, and no longer uses model-refusal text as the GitHub issue title

#### Major bug fixes

* Fixed a crash (out-of-memory) when the CLI inherits a stale websocket/OAuth file-descriptor environment variable from a parent process
* Fixed Claude in Chrome silently failing to connect when the OAuth token belongs to a different account than the Claude Code login
* Fixed nested `.claude/skills` skills with directory-qualified names being blocked by permission prompts in non-interactive runs
* Fixed several subagent issues: viewing a subagent's transcript now shows tool results and live progress, messages sent while it finishes its turn are no longer dropped, and backgrounding a running subagent (ctrl+b) no longer restarts it from scratch
* Fixed `claude agents` workers failing with `401 Invalid bearer token` when the daemon was started from a shell with a custom API gateway via `ANTHROPIC_BASE_URL` and `ANTHROPIC_AUTH_TOKEN`
* Fixed compaction not honoring `--fallback-model`: compaction now falls back to the configured fallback model chain on overload or model-availability errors
* Fixed model requests continuing to fail with auth errors after credentials were refreshed outside the session, due to a stale cached request configuration
* Fixed background sessions created with `/bg` or `←←` after a turn finished showing "Working" forever in the agents list
* Fixed Linux sandbox failing to start when `.claude/skills` or `.claude/hooks` is a symlink
* Fixed MCP server-level specs (`mcp__server`, `mcp__server__*`, `mcp__*`) in subagent `disallowedTools` being silently ignored
* Fixed vim mode undo: `u` now steps through NORMAL/VISUAL-mode commands one at a time instead of merging commands in quick succession into a single undo step
* Fixed statusline links with custom URI schemes (e.g., `vscode://`) not opening when clicked in `claude agents`
* [VSCode] Fixed pressing Esc to dismiss a CJK IME candidate window canceling the running Claude task

-----

## Claude Code changes

### Changed documents

#### [advisor](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/claude-code/advisor.md) [[Source](https://code.claude.com/docs/en/advisor)]

* Removed the statement that Fable 5 does not appear in the `/advisor` picker — Fable is now selectable directly from the picker [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/5cc66dc1)]
* New behavior: subagents now inherit the configured advisor and apply the same pairing check against their own model
* Client-side validation changed: if the advisor is less capable than the main model, it is now silently not attached (with a notification) rather than producing an API error

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Added clarification that `resolvedModel` can differ from the requested model when `availableModels` or another override applies
* `team_name` field in `TaskCreated`, `TaskCompleted`, and `TeammateIdle` hook events is now documented as deprecated ("will be removed in a future release"); example values changed to session-derived format `"session-a1b2c3d4"`

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Added that alias environment variables (`ANTHROPIC_DEFAULT_OPUS_MODEL`, etc.) cannot redirect an allowed alias to a model outside `availableModels`
* `/fast` now refuses to toggle when it would switch to an Opus model outside `availableModels`
* Clarified that an `opusplan` Haiku session stays on Haiku in plan mode when Sonnet is excluded from `availableModels`

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* New "Match by input parameter" section: deny and ask rules can now match any top-level tool input parameter using `Tool(param:value)` syntax (e.g., `Agent(model:opus)`, `Bash(run_in_background:true)`) with wildcard support [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/5cc66dc1)]
* Added clarification that a broad deny rule overrides a narrower allow rule — deny rules cannot carry allowlist exceptions
* `--add-dir` now loads subagents from `.claude/agents/` directories in the added paths

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* New "Check connection status" section: documents `/rc active` footer indicator, which turns red and reads `/rc failed` on connection failure with a dismiss option
* New error documented: "Couldn't verify Remote Control eligibility" (added in v2.1.178) caused by inability to reach the feature-flag service when offline or behind a proxy
* Error message for "Remote Control is not yet enabled" rewritten — now directs users to `claude auth logout`/`login` to refresh entitlements

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New `footerLinksRegexes` setting (v2.1.176+): renders clickable footer badges when a regex matches turn output, with named capture groups for URL/label templating; supports max 5 badges, allowlisted URL schemes, and is scoped to user/managed settings only
* New `enforceAvailableModels` setting referenced as a way to constrain the Default model picker
* `language` setting now also applies to auto-generated session titles (as of v2.1.176)
* `availableModels` merge behavior clarified: managed/policy values fully replace lower-precedence entries

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Added that a user/project skill overrides a same-named bundled skill
* New content on nested skill loading in monorepos: skills in subdirectory `.claude/skills/` become available when working in that directory, with conflicts resolved via directory-qualified names (e.g., `/apps/web:deploy`)

#### [statusline](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/claude-code/statusline.md) [[Source](https://code.claude.com/docs/en/statusline)]

* Added a note pointing to `footerLinksRegexes` for clickable footer badges, clarifying they are independent of the status line script

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Added v2.1.178 behavior: when multiple nested `.claude/agents/` directories define the same `name`, the definition closest to the working directory wins
* `--add-dir` directories are now scanned for `.claude/agents/` subagent definitions
* MCP server-level patterns now accepted in `tools`/`disallowedTools`: `mcp__<server>` or `mcp__<server>__*` grants/removes all tools from a server; `mcp__*` in `disallowedTools` removes every MCP tool
* Fork mode updated: forks are now spawned only when Claude explicitly requests the `fork` subagent type; spawns without a subagent type still use the general-purpose subagent

#### [workflows](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/claude-code/workflows.md) [[Source](https://code.claude.com/docs/en/workflows)]

* New nested workflow loading behavior (v2.1.178): saving a workflow writes to the closest `.claude/workflows/` directory; project workflows load from every `.claude/workflows/` along the path from cwd to repo root, with the closest-to-cwd definition taking precedence on name conflicts

-----

## API changes

### New Documents

#### [admin/analytics](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/api/api/admin/analytics.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics)]

New API reference for the Analytics Admin API. Includes activity summary endpoint (`GET /v1/organizations/analytics/summaries`) returning DAU, WAU, MAU, adoption rates, Cowork active users, and seat counts.

#### [admin/analytics/cost](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/api/api/admin/analytics/cost.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/cost)]

New cost analytics endpoints: `GET /v1/organizations/analytics/cost_report` and `GET /v1/organizations/analytics/user_cost_report`. Returns `CostBucket` objects with `amount`, `list_amount`, and `cost_type` (`tokens`/`web_search`/`code_execution`).

#### [admin/analytics/users](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/api/api/admin/analytics/users.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/users)]

New per-user activity analytics endpoint (`GET /v1/organizations/analytics/users`). Returns detailed per-product metrics: chat (conversations, files, artifacts, skills, connectors), Claude Code (commits, PRs, lines added/removed, tool accept/reject counts), Cowork, Design, and Office products (Excel, Outlook, PowerPoint, Word).

#### [admin/analytics/usage](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/api/api/admin/analytics/usage.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/usage)]

New token usage analytics endpoints: `GET /v1/organizations/analytics/usage_report` and `GET /v1/organizations/analytics/user_usage_report`. Returns `UsageBucket` objects with breakdowns by input/output token type, inference geo (`global`/`us`), context window size, speed (`fast`/`standard`), and product (`chat`, `claude_code`, `cowork`, `office_agent`, etc.).

#### [admin/analytics/connectors](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/api/api/admin/analytics/connectors.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/connectors)]

New connector usage analytics endpoint (`GET /v1/organizations/analytics/connectors`). Returns per-product connector usage metrics across chat, Claude Code, Cowork, and Office products.

#### [admin/analytics/skills](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/api/api/admin/analytics/skills.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/skills)]

New skill usage analytics endpoint (`GET /v1/organizations/analytics/skills`). Returns per-product skill usage metrics.

#### [admin/analytics/chat_projects](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/api/api/admin/analytics/chat_projects.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects)]

New chat project usage analytics endpoint (`GET /v1/organizations/analytics/apps/chat/projects`). Returns `ChatProjectUsage` with distinct conversation count, distinct user count, message count, project ID/name, and creation metadata.

#### [admin/federation_issuers](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/api/api/admin/federation_issuers.md) [[Source](https://platform.claude.com/docs/en/api/admin/federation_issuers)]

New Federation Issuers API reference (5 endpoints: Create, Get, List, Update, Archive). `FederationIssuer` object includes `issuer_url`, JWKS config (discovery/explicit URL/inline), JTI checking, max JWT lifetime, and polling status fields.

#### [admin/federation_rules](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/api/api/admin/federation_rules.md) [[Source](https://platform.claude.com/docs/en/api/admin/federation_rules)]

New Federation Rules API reference (5 endpoints + workspace sub-endpoints). `FederationRule` object includes `match` conditions (audience, claims, CEL expression, subject prefix), target service account, OAuth scope, token lifetime, and workspace applicability.

#### [admin/service_accounts](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/api/api/admin/service_accounts.md) [[Source](https://platform.claude.com/docs/en/api/admin/service_accounts)]

New Service Accounts API reference (5 endpoints: Create, Get, List, Update, Archive + workspace membership sub-endpoints). `ServiceAccount` object includes `organization_role` (`developer`/`admin`) and federation-related actor fields.

#### [admin/spend_limits](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/api/api/admin/spend_limits.md) [[Source](https://platform.claude.com/docs/en/api/admin/spend_limits)]

New Spend Limits API reference (4 endpoints for spend limits + 4 for increase requests). `SpendLimit` object with `amount`, `period`, and polymorphic `scope` (user, seat_tier, rbac_group, organization). Includes approval/denial workflow for member-submitted increase requests.

#### [admin/workspaces/service_accounts](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/api/api/admin/workspaces/service_accounts.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts)]

New Workspace Service Account Membership API reference (5 endpoints: Create, Get, List, Update, Delete). Documents `ServiceAccountCreateResponse` with `workspace_role` values including `workspace_user`, `workspace_developer`, `workspace_restricted_developer`, `workspace_admin`.

#### [manage-claude/spend-limits-api](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/api/manage-claude/spend-limits-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/spend-limits-api)]

New guide for the Spend Limits API (Claude Enterprise only). Covers the spend limit hierarchy (user override → seat tier → RBAC group → org default), how monetary values are expressed in minor currency units, the increase request lifecycle (pending/approved/denied), and quick-start curl examples. Requires scoped Admin API key with `read:spend_limits`/`write:spend_limits` scope.

### Changed documents

#### [api/admin](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/api/api/admin.md) [[Source](https://platform.claude.com/docs/en/api/admin)]

* Massive expansion: added new top-level sections for Analytics, Spend Limits, Service Accounts, Federation Issuers, and Federation Rules with all their endpoints and model schemas [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/5cc66dc1)]
* `ExternalKeyListResponse` schema restructured: was `{ data, next_page }` list wrapper; now represents a single CMEK config object with immutability language about encrypted data
* Workspace Service Accounts sub-section added with 5 new endpoints for managing service account workspace membership

#### [api/admin/external_keys](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/api/api/admin/external_keys.md) [[Source](https://platform.claude.com/docs/en/api/admin/external_keys)]

* `ExternalKeyListResponse` schema changed from a paginated list wrapper `{ data, next_page }` to a single CMEK config object; `next_page` field removed; added immutability note about workspace-referenced configs

#### [api/admin/workspaces](https://github.com/gpambrozio/ClaudeDocs/blob/5cc66dc1/docs-md/api/api/admin/workspaces.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces)]

* Added 5 new Service Account Workspace Member endpoints under the existing workspaces section with full `ServiceAccountCreateResponse`, `ServiceAccountRetrieveResponse`, etc. model definitions
