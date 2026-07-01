# [Claude docs changes for July 1st, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/450d6c15) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/450d6c15)]

## Executive Summary
- **Claude Sonnet 5 launches** as the new default model in Claude Code (v2.1.197), with a native 1M-token context window and promotional pricing of $2/$10 per Mtok through August 31, 2026 — the rollout touches nearly every API and Claude Code doc (pricing, platform availability, adaptive-thinking-only behavior, a new tokenizer producing ~30% more tokens than prior models)
- **New self-serve Tunnels API** (`/v1/tunnels`, beta) lets developers create and manage tunnels directly via a Workload Identity Federation token, without org-admin access; the old admin-only MCP Tunnels API (`/v1/organizations/tunnels`) is now marked deprecated with a migration window
- **Claude Desktop launches on Linux (beta)** — installable via apt or a `.deb` package on Ubuntu 22.04+/Debian 12+, with Chat, Cowork, and Code tabs (Computer Use and voice dictation not yet supported)
- **Managed Agents** gain session-level configuration overrides (swap `model`, `system`, `tools`, `mcp_servers`, or `skills` for a single session without a new agent version) and an opt-in incremental **event-delta streaming** preview for agent messages/thinking
- **Permission SDK docs clarify a common gotcha**: tools auto-approved by allow rules, `acceptEdits`, or `bypassPermissions` never reach `canUseTool` or hooks — guidance now recommends a `PreToolUse` hook for logic that must run on every tool call regardless of approval path

## New Claude Code versions

### [2.1.197](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/versions/2.1.197.md)

#### New features

* Claude Sonnet 5 is now the default model in Claude Code, with a native 1M-token context window and promotional pricing of $2/$10 per Mtok through August 31, 2026

-----

## Claude Code changes

### New Documents

#### [Claude Desktop on Linux (beta)](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/desktop-linux.md) [[Source](https://code.claude.com/docs/en/desktop-linux)]

Documents the new beta Linux release of the Claude Desktop app (Chat, Cowork, and Code tabs), supported on Ubuntu 22.04+/Debian 12+ (x86_64 or arm64). Covers installation via Anthropic's apt repository (with signing-key verification) or a downloaded `.deb` package, plus update/uninstall via standard `apt` commands. Lists what's not yet available: Computer Use, voice dictation, the Quick Entry global hotkey on native Wayland (works on X11), and Fedora/RHEL support.

### Changed documents

#### [Advisor](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/advisor.md) [[Source](https://code.claude.com/docs/en/advisor)]

* Sonnet 5 added to the advisor-eligibility table: it can call and act as an advisor for Fable, Opus, and Sonnet 5, but a Sonnet 4.6 advisor is rejected when the main model is Sonnet 5 [line 64]
* Supported main-model requirement loosened from "Sonnet 4.6" to "Sonnet 4.6 or later" [line 117]

#### [Agent SDK — Agent loop](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/agent-sdk/agent-loop.md) [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop)]

* Example model ID updated from `claude-sonnet-4-6` to `claude-sonnet-5` [line 169]

#### [Agent SDK — Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/agent-sdk/permissions.md) [[Source](https://code.claude.com/docs/en/agent-sdk/permissions)]

* New "ask rules" step added to the permission evaluation flow diagram (now 6 steps: hooks, deny rules, ask rules, permission mode, allow rules, `canUseTool`) [line 47]
* New documented behavior: auto-approved tools (via allow rules, `acceptEdits`, or `bypassPermissions`) never reach `canUseTool` — coverage depends on rule form, and a `PreToolUse` hook is recommended to guarantee checks run on every call [lines 65-66]

#### [Agent SDK — Python](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* `can_use_tool` field clarified: only invoked when the permission flow falls through to a prompt, not for calls auto-approved by `allowed_tools`, allow rules, or `permission_mode`; a `PreToolUse` hook is recommended for logic that must run on every call [lines 795, 1075]
* Code example updated to warn against listing gated tools in both `allowed_tools` and `can_use_tool` [lines 634-636]
* 1M-context beta retirement migration guidance now includes Claude Sonnet 5 as a migration target [line 1254]

#### [Agent SDK — TypeScript](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* `canUseTool` clarified to only fire when the permission flow falls through to a prompt, not for calls auto-approved by `allowedTools`, allow rules, or `permissionMode` [lines 391, 766]
* 1M-context beta retirement migration guidance now includes Claude Sonnet 5 as a migration target [line 2755]

#### [Agent SDK — User input](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/agent-sdk/user-input.md) [[Source](https://code.claude.com/docs/en/agent-sdk/user-input)]

* New explicit statement: `canUseTool` never fires for auto-approved tools; a bare `allowed_tools` entry skips it unless an ask rule or `plan` mode routes the call back to a prompt — recommends `PreToolUse` hooks for logic that must run on every call [lines 27-29]

#### [Agent teams](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

* New documented security behavior: messages relayed between teammates via `SendMessage` are marked as coming from another Claude session, not the user; a teammate can't approve permission prompts or relay bypass-consent on another teammate's behalf, and in auto mode a relayed "approval" is treated as untrusted input [lines 220-221]

#### [Agent view](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* `@<repo>` dispatch clarified: typing `@` lists git repositories one level below the launch directory plus any directory that already has a session; directories with a space in the name are not listed [lines 225, 237-240]

#### [Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Sonnet 5 added to the models supporting the 1M-token context window on Bedrock; runs via the Mantle endpoint and always uses 1M context (no `[1m]` variant needed) [lines 280-281, 327]

#### [Claude apps gateway](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/claude-apps-gateway.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway)]

* Intro rewritten to describe when the gateway is preferred vs. when Claude Enterprise is a better fit, now pointing to a new feature-availability comparison page [line 3]
* Auto mode compatibility note broadened from "only Opus models" to "only the models eligible on third-party providers," reflecting Sonnet 5 eligibility [line 277]

#### [Claude Platform on AWS](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/claude-platform-on-aws.md) [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

* Example `ANTHROPIC_DEFAULT_SONNET_MODEL` updated to `claude-sonnet-5` [line 78]

#### [CLI reference](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* `--model` flag example updated from `claude-sonnet-4-6` to `claude-sonnet-5` [line 85]

#### [Context window](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/context-window.md) [[Source](https://code.claude.com/docs/en/context-window)]

* Sonnet 5 added to the models supporting the 1M-token context window, with a pointer to its own auto-compaction/LLM-gateway section [line 96]

#### [Desktop application](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* New Linux (beta) download entry added, linking to the new Linux page; Linux is no longer described as unsupported [lines 13-16]
* Auto mode model requirement loosened to "Sonnet 4.6 or later"; Vertex AI Enterprise auto-mode support expanded to include Sonnet 5 [line 72]
* Sonnet 5 added to the models that always use adaptive reasoning (fixed-budget override doesn't apply) [line 467]
* Linux limitation entry updated: desktop app now available (beta), but Computer Use isn't yet supported on Linux [line 643]
* Update-checking troubleshooting note added: Linux updates go through `apt`, not app auto-update [line 675]

#### [Desktop quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/desktop-quickstart.md) [[Source](https://code.claude.com/docs/en/desktop-quickstart)]

* New Linux (beta) download entry (apt or `.deb`) and Linux-specific install/sign-in steps (launcher instead of Applications/Start menu) [lines 13-16, 36]

#### [Environment variables](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` / `CLAUDE_CODE_AUTO_COMPACT_WINDOW`: now note Sonnet 5 has its own default proactive-compaction threshold [lines 130, 142]
* `CLAUDE_CODE_DISABLE_1M_CONTEXT`: now documents that setting this also forces Sonnet 5 sessions down to a 200K window [line 152]
* `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING`: documented as having no effect on Sonnet 5 (in addition to Fable 5 and Opus 4.7+) [line 153]
* `CLAUDE_CODE_SHELL`: description substantially expanded — only accepts a path to a `bash`/`zsh` binary (other shells like `fish` unsupported), falls back to auto-detection otherwise, and documents the detection algorithm (`$SHELL`, then first working `zsh` then `bash` on `PATH`) [line 242]

#### [Errors](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* "thinking.type.enabled is not supported" error now also attributed to Claude Code versions older than the Sonnet 5 minimum [line 643]
* New version requirement documented: Sonnet 5 needs Claude Code v2.1.197+ (TypeScript SDK v0.3.197+) [lines 651, 653]

#### [GitHub Actions](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/github-actions.md) [[Source](https://code.claude.com/docs/en/github-actions)]

* Example model IDs updated from `claude-sonnet-4-6` to `claude-sonnet-5` across config examples [lines 93, 106, 603, 610]

#### [Glossary](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/glossary.md) [[Source](https://code.claude.com/docs/en/glossary)]

* "Effort level" entry: supported model list loosened to "Sonnet 4.6 and later" [line 103]

#### [Google Vertex AI](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/google-vertex-ai.md) [[Source](https://code.claude.com/docs/en/google-vertex-ai)]

* Example `ANTHROPIC_DEFAULT_SONNET_MODEL` updated to `claude-sonnet-5`; Sonnet 5 added to the 1M-token context-window model list (always 1M, no `[1m]` variant needed) [lines 136, 176]

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* New documented limitation: `PreToolUse` does not fire for files referenced with `@` in a prompt (inserted directly, no tool call); use a `Read` deny rule to block specific paths instead [lines 1234-1235]
* New PowerShell guidance: `${CLAUDE_PROJECT_DIR}` substitution in shell-form commands only works for plugin hooks; `settings.json` hooks on PowerShell should use `$env:CLAUDE_PROJECT_DIR` or exec form, with a new example [lines 2877-2886]

#### [Microsoft Foundry](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/microsoft-foundry.md) [[Source](https://code.claude.com/docs/en/microsoft-foundry)]

* Example `ANTHROPIC_DEFAULT_SONNET_MODEL` updated to `claude-sonnet-5` [line 78]

#### [Model configuration](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* On the Anthropic API, the `sonnet` alias now resolves to Sonnet 5 (previously Sonnet 4.6); requires Claude Code v2.1.197+ [lines 29, 31]
* Default model table updated: Pro/Team Standard/Enterprise seats now default to Sonnet 5 [line 197]
* Effort-level tables updated: Sonnet 5 added at the `low/medium/high/xhigh/max` tier, defaulting to `high` [lines 284, 287, 301]
* New dedicated "Sonnet 5 context window" subsection: always runs with 1M context (no 200K variant, no `[1m]` suffix, no usage credits needed), auto-compacts around 967K tokens by default; documents two exceptions that budget it at 200K (behind an LLM gateway without explicitly selecting `sonnet[1m]`, or `CLAUDE_CODE_DISABLE_1M_CONTEXT=1`) [lines 347-349, 370-378]
* Sonnet 5 added to models that always use adaptive reasoning [line 330]

#### [Monitoring usage](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Example `model` attribute values updated from `claude-sonnet-4-6` to `claude-sonnet-5` across telemetry attribute tables [lines 421, 443, 461, 572, 595]

#### [Permission modes](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Auto mode model requirement loosened to "Sonnet 4.6 or later"; third-party provider (Bedrock/Vertex/Foundry/gateway) support expanded to include Sonnet 5, alongside Opus 4.7/4.8 [lines 143, 151]

#### [Server-managed settings](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* Security framing strengthened: explicitly states server-managed settings are "not a security boundary" — bypassing on unmanaged devices doesn't require admin/sudo access [line 205]
* New rows in the security-considerations table: a modified binary bypasses client-side controls; an old Claude Code version predating server-managed settings never fetches them; intercepted/redirected network traffic can alter received settings [lines 211-212, 216]
* New reference to "Tenant Restrictions" (network-level access control) in the Claude Help Center [line 219]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* `enforceAvailableModels` clarified: fallback to the first allowlisted entry only occurs when the account-type default model is *not* already allowlisted [line 229]
* Example `fallbackModel`/`model` values and default commit-attribution trailer updated to Sonnet 5 [lines 231, 248, 437]

#### [Setup](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* Desktop app download callout now includes a Linux download link alongside macOS and Windows [line 26]

#### [Skills](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* New documented capability: skill entries can be symlinks to directories elsewhere on disk — Claude Code follows the symlink and reads `SKILL.md` from the target, deduplicating shared targets; plugin skills handle symlinks differently [line 105]

#### [Sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Full model ID example updated from `claude-sonnet-4-6` to `claude-sonnet-5` [line 269]

#### [Terminal guide](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/terminal-guide.md) [[Source](https://code.claude.com/docs/en/terminal-guide)]

* Desktop app download callout now includes a Linux download link [line 8]

#### [Troubleshoot installation](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/claude-code/troubleshoot-install.md) [[Source](https://code.claude.com/docs/en/troubleshoot-install)]

* New troubleshooting entry for `A parameter cannot be found that matches parameter name 'fsSL'` — covers running the macOS/Linux curl installer in Windows PowerShell (where `curl` aliases to `Invoke-WebRequest`), with a link to the correct PowerShell command [lines 21, 40, 436-442]
* Desktop app download callout now includes a Linux download link [line 40]

-----

## API changes

### New Documents

#### [Tunnels](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/api/beta/tunnels.md) [[Source](https://platform.claude.com/docs/en/api/beta/tunnels)]

New self-serve, non-admin **Tunnels API** at `/v1/tunnels` (research preview, requires the `anthropic-beta: mcp-tunnels-2026-06-22` header). It supersedes the org-admin-only Tunnels API (`/v1/organizations/tunnels`): the underlying resources (`BetaTunnel`, `BetaTunnelToken`, `BetaTunnelCertificate`) and operations (create/list/retrieve/archive tunnel, reveal/rotate token, and a certificates sub-resource with create/list/retrieve/archive) are the same, but authorization now uses a Workload Identity Federation token scoped to `workspace:manage_tunnels` (previously `org:manage_tunnels`), and `POST /v1/tunnels` can allocate a brand-new tunnel programmatically instead of only attaching to a Console-created one. Equivalent per-language SDK reference pages were also added under each language's `beta/tunnels/` path.

### Changed documents

#### [Admin](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/api/admin.md) [[Source](https://platform.claude.com/docs/en/api/admin)]

* All MCP Tunnels endpoints (tunnel and tunnel-certificate operations) are now marked **Deprecated** in the endpoint index [lines 366-410]

#### [Admin — Analytics](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/api/admin/analytics.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics)]

* `assigned_seat_count`, `daily_adoption_rate`, `monthly_adoption_rate`, `weekly_adoption_rate`, and `pending_invite_count` are now documented as `null` when a response is scoped to an RBAC group

#### [Admin — Chat Projects usage](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/api/admin/analytics/chat_projects.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects)]

* `distinct_conversation_count` changed from a required field to `optional number`, now `null` on aggregated rows where a distinct count can't be computed [lines 20-60]

#### [Admin — Get Activity Summaries](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/api/admin/analytics/retrieve_summaries.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/retrieve_summaries)]

* Same RBAC-group `null` behavior added for `assigned_seat_count`, `daily_adoption_rate`, `monthly_adoption_rate`, `weekly_adoption_rate`, `pending_invite_count` [lines 40-92]

#### [Admin — Get Per-User Cost](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/api/admin/analytics/cost/list_by_user.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user)]

* Clarified this endpoint only includes cost attributable to seat users; org-wide totals (including direct API-key/automation traffic) require the new bucketed `/v1/organizations/analytics/cost_report` endpoint [lines 11-17]

#### [Admin — Get Per-User Token Usage](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/api/admin/analytics/usage/list_by_user.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/usage/list_by_user)]

* Clarified this endpoint only includes usage attributable to seat users; org-wide totals require the new bucketed `/v1/organizations/analytics/usage_report` endpoint [lines 11-17]

#### [Admin — Users analytics](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/api/admin/analytics/users.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/users)]

* New `bioscience_metrics` object added to per-user analytics: `delegation_count`, `distinct_session_count`, `message_count`, `remote_compute_job_count`, `skills_used_count` [lines 20-45]
* `chat_metrics.connectors_used_count` redefined as "Number of MCP connector invocations" (no longer nullable/distinct-based); new `chat_metrics.distinct_connectors_used_count` field added (nullable on aggregated rows) [lines 48-60]

#### [Admin — External keys](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/api/admin/external_keys.md) [[Source](https://platform.claude.com/docs/en/api/admin/external_keys)]

* AWS `provider_config.role_arn` is now deprecated and optional (previously required) — Anthropic reaches the KMS key via a managed intermediate role, and the field is ignored if supplied; applies across create/list/retrieve/update

#### [Admin — MCP Tunnels](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/api/admin/mcp_tunnels.md) [[Source](https://platform.claude.com/docs/en/api/admin/mcp_tunnels)]

* All endpoints (Create/Get/List/Archive Tunnel, Reveal/Rotate Token, and the Tunnel Certificates create/list/retrieve/archive sub-resource) are now marked **Deprecated**, superseded by the new `/v1/tunnels` beta API; existing integrations keep working with the old header (`mcp-tunnels-2026-05-19`) and scope (`org:manage_tunnels`) during a migration window [line 9 in each endpoint page]

#### [Admin — Approve Spend Limit Increase Request](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/api/admin/spend_limits/increase_requests/approve.md) [[Source](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve)]

* Example response `status` corrected from `"pending"` to `"approved"`, reflecting the endpoint's actual post-approval state [lines 372, 438]

#### [Admin — List Effective Spend Limits](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/api/admin/spend_limits/list_effective.md) [[Source](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective)]

* Terminology clarified from "cap" to "spend limit" throughout (no behavior change)

#### [Beta](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* New Tunnels and Tunnel Certificates endpoint groups indexed (see the new Tunnels page above) [line 785]

#### [MCP tunnels — Architecture and components](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/agents-and-tools/mcp-tunnels/concepts.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts)]

* Required WIF scope renamed from `org:manage_tunnels` to `workspace:manage_tunnels` [line 31]

#### [MCP tunnels — Manage tunnels in the Console](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/agents-and-tools/mcp-tunnels/console.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/console)]

* Same scope rename (`org:manage_tunnels` → `workspace:manage_tunnels`) in prerequisites and federation-rule setup steps [lines 18, 42]

#### [MCP tunnels — Deploy with Docker Compose](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/agents-and-tools/mcp-tunnels/deploy-compose.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-compose)]

* Tunnel creation is no longer required up front: leaving `TUNNEL_ID` unset now lets the setup component create the tunnel itself [line 17]
* `mcp-proxy` image digest bumped; install/rotation instructions updated so `TUNNEL_ID` is optional; `setup init` reruns now reuse the stored tunnel ID and never create a second tunnel [lines 89, 133, 174, 189, 196, 268]

#### [MCP tunnels — Deploy with Helm](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/agents-and-tools/mcp-tunnels/deploy-helm.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm)]

* Chart now supports creating a new tunnel during install (not only attaching to a pre-existing Console tunnel); Helm chart version bumped from 1.0.0 to 2.0.0 [lines 11, 16, 131, 183, 196, 255, 273]
* `values.yaml` schema changed: `api.wif.tunnelId` removed in favor of a new `tunnel.id` field (empty = auto-create); new guidance on reading the auto-created tunnel's domain from the `mcp-tunnel` Secret [lines 148-155, 205-215]
* New "Upgrade from chart 1.x" section documenting the `api.wif.tunnelId` → `tunnel.id` migration and required scope rename [lines 244-246]

#### [MCP tunnels overview](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/agents-and-tools/mcp-tunnels/overview.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview)]

* Prerequisites updated: a tunnel can now be created via the API or auto-created by the Helm setup hook, not only via the Console; WIF scope renamed to `workspace:manage_tunnels` [lines 29, 31]

#### [MCP tunnels quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/agents-and-tools/mcp-tunnels/quickstart.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/quickstart)]

* `mcp-proxy` image digest bumped to match the new build [line 149]

#### [MCP tunnels reference](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/agents-and-tools/mcp-tunnels/reference.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/reference)]

* Major rewrite of the "Tunnels API" section: points to the new `/v1/tunnels` beta API as primary, with the old admin API called out as deprecated with a migration window and explicit migration steps [lines 39-49]
* Required scope updated to `workspace:manage_tunnels`, required beta header updated to `mcp-tunnels-2026-06-22`; CA certificate upload path updated to `/v1/tunnels/{tunnel_id}/certificates` [lines 51, 61, 69]
* `setup init` / `--tunnel-id` flag: now optional — omitting it creates a new tunnel, a previously-stored ID is reused on reruns [lines 97, 100]

#### [MCP tunnels security](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/agents-and-tools/mcp-tunnels/security.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/security)]

* "Archive over the API" link retargeted from the deprecated admin API to the new beta Tunnels API archive endpoint [line 55]

#### [Troubleshoot MCP tunnels](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/agents-and-tools/mcp-tunnels/troubleshooting.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/troubleshooting)]

* WIF scope in the 403 troubleshooting tip renamed to `workspace:manage_tunnels` [line 85]

#### [Computer use tool](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]

* Claude Sonnet 5 added to models supporting the `computer-use-2025-11-24` beta and enhanced actions (e.g. zoom); added to the higher screenshot resolution tier (up to 2576px long edge) [lines 10-13, 297-300, 568-571]

#### [Web fetch tool](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]

* Claude Sonnet 5 added to the models supporting dynamic filtering in `web_fetch_20260318` [lines 6-8]

#### [Web search tool](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/agents-and-tools/tool-use/web-search-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]

* Claude Sonnet 5 added to the models supporting dynamic filtering in `web_search_20260318` [lines 6-8]

#### [API reference (all SDKs) — Messages: create, count_tokens, batches](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/api/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/messages/create)]

* New refusal `category` enum value `military_weapons` (alongside `cyber`, `bio`, `frontier_llm`, `reasoning_extraction`)
* New tool versions `web_search_20260318`/`web_fetch_20260318` adding `allowed_callers`, `defer_loading`, `use_cache`, `max_content_tokens`, and `response_inclusion` (`full`/`excluded` — controls whether nested `server_tool_use`/result blocks are dropped when consumed by a same-turn `code_execution` call)
* New header `anthropic-user-profile-id` (optional) on `count_tokens` and batch `create` to attribute requests to a user profile (requires the `user-profiles` beta header)

#### [API reference (all SDKs) — Beta Messages: create, count_tokens, batches](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/api/beta/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]

* New header `anthropic-user-profile-id` (optional) on create/count_tokens/batch-create to attribute a request to a user profile, requiring the `user-profiles` beta header; **removes** the previous `user_profile_id` body field it supersedes
* Same new `web_search_20260318`/`web_fetch_20260318` tool versions and `military_weapons` refusal category as the non-beta Messages API

#### [Adaptive thinking](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/build-with-claude/adaptive-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

* Claude Sonnet 5 added as a supported model: adaptive thinking is on by default, manual `{type: "enabled", budget_tokens: N}` is rejected with a 400 error, and `{type: "disabled"}` turns it off; added to `max`/`xhigh` effort levels and to models where `thinking.display` defaults to `"omitted"` [lines 11, 28, 79-80, 139-141, 215, 226, 243]

#### [Batch processing](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/build-with-claude/batch-processing.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing)]

* New Batch API pricing for Sonnet 5: $1/$5 per MTok through August 31, 2026, then $1.50/$7.50 per MTok from September 1, 2026; added to the `output-300k-2026-03-24` beta (300k max_tokens for batch requests) [lines 97-98, 432]

#### [Claude in Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/build-with-claude/claude-in-amazon-bedrock.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)]

* Sonnet 5 now open to all Bedrock customers (`anthropic.claude-sonnet-5`), including via the global (non-regional) endpoint [lines 15, 184, 221]

#### [Claude in Microsoft Foundry](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/build-with-claude/claude-in-microsoft-foundry.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)]

* Claude Sonnet 5 (preview) added to the Foundry model table with 1M-token context window support [lines 266, 311]

#### [Claude on Amazon Bedrock (legacy)](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/build-with-claude/claude-on-amazon-bedrock-legacy.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)]

* Note added: Sonnet 5 is not available on the legacy ARN-based Bedrock surface — use Claude in Amazon Bedrock or Claude Platform on AWS instead [line 88]

#### [Claude on Google Cloud](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/build-with-claude/claude-on-vertex-ai.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

* `claude-sonnet-5` added to the Vertex AI model table and the 1M-token context-window model list [lines 70, 159]

#### [Claude Platform on AWS (API)](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/build-with-claude/claude-platform-on-aws.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)]

* `claude-sonnet-5` added to the list of models available on Claude Platform on AWS [line 292]

#### [Compaction](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/build-with-claude/compaction.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]

* Claude Sonnet 5 added to the models supporting compaction [line 41]

#### [Context windows](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/build-with-claude/context-windows.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]

* Claude Sonnet 5 added to the 1M-token context-window list, context-awareness support (1M budget vs. 200k for Sonnet 4.5/Haiku 4.5), and beta server-side compaction support [lines 37, 108, 120, 142]

#### [Effort](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/build-with-claude/effort.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]

* Claude Sonnet 5 added as supporting the effort parameter and the `max`/`xhigh` tiers; new "Recommended effort levels for Claude Sonnet 5" subsection (defaults to `high`) [lines 15, 44-45, 54-63, 131-132]
* New note on Sonnet 5's adaptive-thinking/effort interaction: manual thinking unsupported (400 error), `{type:"disabled"}` turns thinking off [line 166]

#### [Extended thinking](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Claude Sonnet 5 added to the model-support table: manual extended thinking not supported (400 error) — use adaptive thinking + effort instead; added to the 128k max-output-token group, the `interleaved-thinking-2025-05-14` deprecated/ignored group, and the thinking-behavior comparison table [lines 23, 101, 111, 187, 441, 453-454, 675]

#### [Prompt caching](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* New prompt-caching pricing for Sonnet 5: $2/$2.50/$4/$0.20/$10 per MTok through August 31, 2026, then $3/$3.75/$6/$0.30/$15 per MTok from September 1, 2026; added to the 1,024-token minimum cacheable prompt length group [lines 91-92, 280]

#### [Search results](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/build-with-claude/search-results.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/search-results)]

* `claude-sonnet-5` added to the models supporting the search results feature [line 18]

#### [Using Agent Skills with the API](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/build-with-claude/skills-guide.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/skills-guide)]

* Corrected the "delete all skill versions" CLI example: replaced a shell loop piping `versions list` into `versions delete` with an explicit two-step (list, then delete each version id) [lines 388-397]

#### [Structured outputs](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/build-with-claude/structured-outputs.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

* Claude Sonnet 5 added to the Claude API, Google Cloud, and Amazon Bedrock general-availability lists for structured outputs [line 16]

#### [Task budgets](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/build-with-claude/task-budgets.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/task-budgets)]

* Claude Sonnet 5 added to the task-budgets model-support table as "Not supported" [line 256]

#### [Token counting](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/build-with-claude/token-counting.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/token-counting)]

* New note: Opus 4.7+ models, Fable 5, Mythos 5/Preview, and Sonnet 5 use a newer tokenizer producing ~30% more tokens for the same input text than earlier models — recommends recounting prompts per target model [lines 31, 33]

#### [Vision](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/build-with-claude/vision.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/vision)]

* Claude Sonnet 5 added to the high-resolution image tier (2576px max long edge, 4784 max visual tokens) [line 230]
* Cost-estimate example switched from Sonnet 4.6 to Haiku 4.5 as the standard-tier example [line 246]

#### [Using the Messages API](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/build-with-claude/working-with-messages.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)]

* Claude Sonnet 5 added to the models where response prefilling is unsupported (400 error) [line 127]

#### [Intro to Claude](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/intro.md) [[Source](https://platform.claude.com/docs/en/intro)]

* Model lineup updated: Claude Sonnet 5 replaces Claude Sonnet 4.6 as the frontier Sonnet-tier model, with a link to the announcement [line 17]

#### [Create an Admin API key](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/manage-claude/admin-api-keys.md) [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api-keys)]

* Compliance API scope table merges `read:compliance_org_settings` into `read:compliance_org_data`: reading org metadata and effective settings now only requires `read:compliance_org_data` [line 78]

#### [API and data retention](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/manage-claude/api-and-data-retention.md) [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

* MCP tunnels API endpoint path updated from `/v1/organizations/tunnels` to `/v1/tunnels` [line 188]

#### [Get access to the Compliance API](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/manage-claude/compliance-api-access.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-api-access)]

* `read:compliance_org_settings` scope removed from the scope-selection table; `read:compliance_org_data` now also grants read access to effective org settings [lines 77-80]

#### [Handle Compliance API errors](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/manage-claude/compliance-errors.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-errors)]

* `read:compliance_org_settings` scope retired as of June 30, 2026; the settings endpoint now requires `read:compliance_org_data` — existing keys with only the retired scope will fail on every call; fix is to create a new key with the new scope [lines 137-160]

#### [List organizations, users, roles, groups, and settings](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/manage-claude/compliance-org-data.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-org-data)]

* `read:compliance_org_settings` scope retired in favor of `read:compliance_org_data` [lines 13, 240-247]
* New `api_keys` array added to the effective org settings response, listing every Compliance Access Key on the parent org (`id`, `name`, `scopes`, `is_active`, `created_at`, `expires_at`, `created_by_id`); secret values are never returned, and deactivated/retired-scope keys remain listed for audit [lines 290-300, 310-313]

#### [Usage and Cost API](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/manage-claude/usage-cost-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/usage-cost-api)]

* Removed "Priority Tier optimization" as a stated use case of the Usage & Cost API [line 18]

#### [Manage WIF with the Admin API](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/manage-claude/wif-admin-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/wif-admin-api)]

* OAuth scope renamed: `org:manage_tunnels` → `workspace:manage_tunnels` [lines 220-221]

#### [Use WIF with Microsoft Entra ID](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/manage-claude/wif-providers/azure.md) [[Source](https://platform.claude.com/docs/en/manage-claude/wif-providers/azure)]

* New required step: register a dedicated Entra app registration/service principal as the "Claude API audience" (`api://<APP_ID>`) before token exchange will succeed [lines 9-63]
* New guidance: managed-identity tokens need up to a 24-hour lifetime, requiring `max_jwt_lifetime_seconds: 86400` on the federation issuer (the wizard's default `7500` is insufficient) [lines 158-163]
* New documented App Service/Functions/Container Apps token endpoint (`IDENTITY_ENDPOINT`/`IDENTITY_HEADER`) as an alternative to IMDS [lines 100-105]
* Full step-by-step AKS Entra Workload Identity path added (issuer/cluster setup, federated credential, service account annotation, two-hop token exchange); new "If your tokens are v1.0" section on legacy claim differences [lines 250-446, 492-502]

#### [WIF reference](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/manage-claude/wif-reference.md) [[Source](https://platform.claude.com/docs/en/manage-claude/wif-reference)]

* OAuth scope renamed to `workspace:manage_tunnels`; its granted actions now include **create** tunnel (previously list/get/certs/reveal/rotate/archive only) [line 132]

#### [Workload Identity Federation](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/manage-claude/workload-identity-federation.md) [[Source](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation)]

* Default MCP tunnels rule scope renamed from `org:manage_tunnels` to `workspace:manage_tunnels` [line 44]

#### [Workspaces](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/manage-claude/workspaces.md) [[Source](https://platform.claude.com/docs/en/manage-claude/workspaces)]

* MCP tunnels are now managed with a workspace-scoped `workspace:manage_tunnels` OAuth token instead of the org-scoped `org:manage_tunnels` [lines 212-214]

#### [Define your agent](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/managed-agents/agent-setup.md) [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup)]

* New capability: session-level overrides for `model`, `system`, `tools`, `mcp_servers`, and `skills` without creating a new agent version [line 27]

#### [Session event stream](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/managed-agents/events-and-streaming.md) [[Source](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)]

* New "Event deltas" opt-in incremental streaming preview for `agent.message`/`agent.thinking` via a new `event_deltas[]` query parameter on the events-stream endpoint; new non-persisted `event_start`/`event_delta` event types with their own wire format [lines 18, 89-208]
* Documented limitations: best-effort/lossy under load, no replay on reconnect, primary-thread-text-only, thinking previews are start-only, deltas never persisted in event history [lines 202-208]

#### [Multi-agent sessions](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/managed-agents/multi-agent.md) [[Source](https://platform.claude.com/docs/en/managed-agents/multi-agent)]

* Session-level configuration overrides now apply to the coordinator and its `self` copies (not roster entries referenced by ID); session-creation overrides can now replace the coordinator's MCP servers [lines 19, 60, 88]

#### [Managed Agents reference](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/managed-agents/reference.md) [[Source](https://platform.claude.com/docs/en/managed-agents/reference)]

* New "Event deltas" event-type category added alongside User/Session/Span/Agent/System events [lines 15, 37-40]

#### [Scheduled deployments](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/managed-agents/scheduled-deployments.md) [[Source](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments)]

* New webhook events for deployment lifecycle changes and deployment run outcomes; new endpoint `GET /v1/deployment_runs/{deployment_run_id}` to retrieve a single run by ID [lines 84, 126]
* Unrecoverable session-creation errors (e.g. archived environment or vault), not just `agent_archived_error`, now auto-pause the deployment and record a failed run [line 166]

#### [Session operations](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/managed-agents/session-operations.md) [[Source](https://platform.claude.com/docs/en/managed-agents/session-operations)]

* Clarified: only `tools` and `mcp_servers` can be updated on an existing session; `model`, `system`, `skills` require the new session-creation overrides instead [lines 28-29]
* New pagination documentation for `GET /v1/sessions`: `limit`, `next_page`/`prev_page` cursors, `order` (default `desc`); cursors are order-specific [lines 64-68]

#### [Start a session](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/managed-agents/sessions.md) [[Source](https://platform.claude.com/docs/en/managed-agents/sessions)]

* New "Override agent configuration for a session" feature: pass `agent` as `type: agent_with_overrides` with an `id`, optional `version`, and any of `model`/`system`/`tools`/`mcp_servers`/`skills` to override for a single session, with detailed field-clearing semantics [lines 43-77]

#### [Authenticate with vaults](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/managed-agents/vaults.md) [[Source](https://platform.claude.com/docs/en/managed-agents/vaults)]

* New capability: `injection_location` on environment-variable credentials can now be updated/rotated (previously only secret values and `display_name` were mutable); updates propagate to running sessions without restart [line 143]

#### [Subscribe to webhooks](https://github.com/gpambrozio/ClaudeDocs/blob/450d6c15/docs-md/api/managed-agents/webhooks.md) [[Source](https://platform.claude.com/docs/en/managed-agents/webhooks)]

* New webhook event categories: Agent events, Deployment events, Deployment run events, alongside existing Session/Vault events [lines 21-31]
