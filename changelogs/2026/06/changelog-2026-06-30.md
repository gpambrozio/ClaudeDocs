# [Claude docs changes for June 30th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/33782309) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/33782309)]

## Executive Summary
- **Claude apps gateway** is a major new self-hosted gateway (included in the `claude` binary) that sits between developers and cloud model providers (Bedrock, Agent Platform, Foundry), providing corporate SSO sign-in, managed settings by IdP group, per-user spend limits, and OTLP telemetry — without developers holding API keys
- **Background session reliability** significantly improved: in-flight work (background shell commands, dynamic workflows, `/loop` tasks) now carries over when backgrounding a session, and background agents auto-resume after daemon restarts including on Windows
- **Microsoft Foundry** gains two distinct hosting options ("Hosted on Azure" and "Hosted on Anthropic") with a feature comparison table; many features move from beta to GA on Foundry
- **Fast mode deprecation**: Opus 4.6 fast mode was silently removed (June 29); Opus 4.7 fast mode is deprecated (removed July 24 with an error)
- **Stream idle watchdog** is now on by default for all providers, aborting and retrying when a response stream stalls for 5 minutes

## New Claude Code versions

### [2.1.196](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/versions/2.1.196.md)

#### New features

* Added support for organization default models — admins set it in the org console; shows as "Org default" (or "Role default") in `/model` when not individually set
* Added readable default names for sessions at start (e.g. `my-app-3f`), making them easier to identify in the agents view
* Added clickable file attachments in chat — Cmd/Ctrl-click reveals the file in Finder/Explorer
* Security: `claude mcp list`/`get` no longer spawn `.mcp.json` servers self-approved via a committed `.claude/settings.json`; untrusted workspaces show `⏸ Pending approval`
* New `ReportFindings` tool for reporting structured code-review findings in the UI

#### Existing feature improvements

* Background session reliability: long-running commands and workflows now survive the session's process being stopped, restarted, or updated — including on Windows, where background shells are handed off instead of killed
* Background agents killed by a daemon restart are now automatically resumed from where they left off the next time the agents view opens
* `/code-review` workflow: merged five cleanup finders into one, cutting token usage by roughly 25%
* Streaming idle watchdog is now on by default for all providers — aborts and retries when a response stream produces no events for 5 minutes; set `CLAUDE_ENABLE_STREAM_WATCHDOG=0` to disable
* Remote Control is now disabled when `ANTHROPIC_BASE_URL` points at a non-Anthropic host
* Opening the agents view from a foreground session now requires a single `←` press instead of two

#### Major bug fixes

* Fixed waking a background job permanently deleting its conversation and re-running the original prompt when the transcript probe misread a real transcript; the file is now set aside, never deleted
* Fixed rate-limit warning flickering and rate-limit telemetry being over-counted when multiple parallel requests were in flight at a usage limit
* Fixed duplicate recap lines after a background session's turn when a schema-rejected StructuredOutput attempt rendered alongside its retry
* Fixed PowerShell `git diff`/`git grep`, `egrep`/`fgrep`, and quoted search patterns with `|` being reported as failures when they exit 1
* Fixed multiple `claude agents` side panel issues: keyboard focus stuck on open, background jobs losing subagent types on every open, sessions showing incorrect status while running
* Fixed `claude agents --dangerously-skip-permissions` silently falling back to auto mode instead of showing bypass disclaimer and applying bypass mode
* Fixed mid-turn crash recovery for Remote sessions — sessions interrupted by a server restart now auto-resume
* Fixed sessions moved with `/cd` reappearing in the old directory's resume list after non-graceful exit when the old path had special characters
* Fixed `claude plugin validate` skipping local plugins whose source is "." and stopping after the first error class
* Fixed Esc Esc at an idle prompt not opening the rewind menu (regression)
* Fixed MCP OAuth requesting the authorization server's full `scopes_supported` catalog, causing `invalid_scope` failures on GitLab self-hosted and other enterprise IdPs
* Fixed `/context` showing 0 tokens for all tool groups on Bedrock
* Fixed `/deep-research` misreporting verifier failures as "all claims refuted" instead of `unverified`
* Fixed plugin dependency version pins not honored when the marketplace was a local folder path backed by a git repo
* Fixed `claude agents` session status: completed rows no longer flip between "Done" and "Needs your input"; stalled agents labeled "Needs attention"; results mentioning a PR show a clickable link
* Fixed voice dictation swallowing spaces and spuriously starting recording during fast typing

-----

## Claude Code changes

### New Documents

#### [Claude apps gateway](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/claude-apps-gateway.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway)]

Comprehensive guide to the new self-hosted Claude apps gateway included in the `claude` binary. Covers why and when to use it over other approaches, a quickstart (register OIDC client, write `gateway.yaml`, run with Docker Compose, verify), how to connect developers via managed settings, what is enforced on developers (model access, telemetry destination, credentials, managed settings), and a detailed availability/limitations table. Requires v2.1.195+, PostgreSQL 14+, and an OIDC-compliant identity provider. Supports Bedrock, Google Cloud's Agent Platform, Foundry, and the Anthropic API as upstreams.

#### [Claude apps gateway configuration](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

Full reference for `gateway.yaml` — every field across all sections: `listen`, `oidc`, `session`, `store`, `upstreams`, `admin`, `enforcement`, `models`, `managed`, `telemetry`, and HTTP tuning (`access_control`, `limits`, `timeouts`, `rate_limits`). Covers secret expansion via `${ENV_VAR}` and `${file:/path}`, per-IdP quirks (Okta, Entra, Google Workspace, Keycloak), RBAC policy mapping, OTLP destination configuration, and a complete example config.

#### [Claude apps gateway deployment and operations](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/claude-apps-gateway-deploy.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy)]

Operational guide: registering OAuth clients per IdP, building a container image around the `claude` binary, Kubernetes Deployment setup with workload identity, Cloud Run configuration, pushing the gateway URL to developer machines, logs/health probes/outage behavior/secret rotation/upgrades, security posture (data flows, threat model, compliance), and troubleshooting keyed by error message.

#### [Deploy Claude apps gateway on Google Cloud](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/claude-apps-gateway-on-gcp.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-on-gcp)]

Worked example deploying the gateway on Google Cloud with Agent Platform as the model upstream. Covers enabling GCP APIs, IAM service account setup, Cloud SQL for PostgreSQL (private IP), Secret Manager for config/secrets, Artifact Registry, and two deployment paths: Cloud Run (with Internal Application Load Balancer) and GKE (with internal Ingress). Includes `gcloud` commands for every provisioning step.

#### [Claude apps gateway spend limits](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/claude-apps-gateway-spend-limits.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-spend-limits)]

Documents per-developer, per-group, and org-wide spend limits enforced by the gateway. Covers setting caps via the admin API (`POST /v1/organizations/spend_limits`), cap resolution order (user → most-restrictive group → org default), enforcement mechanics (pre-check Postgres query on every request, post-response metering from token counts at USD list price, client-abort billing), fail-open/fail-closed behavior on Postgres unavailability, and the full admin API reference (list, create/replace, get, delete, effective, audit).

#### [Gateways](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/gateways.md) [[Source](https://code.claude.com/docs/en/gateways)]

Overview page explaining what a gateway is, how it sits between Claude Code and a model provider, and how to choose between Claude apps gateway and an existing LLM gateway. Covers the two credential types (developer vs. provider), how subscriptions interact with gateways, and what is configured separately (model selection, non-API traffic, corporate HTTP proxies).

### Changed documents

#### [Admin setup](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/admin-setup.md) [[Source](https://code.claude.com/docs/en/admin-setup)]

* Cross-source lock key exception added: sandbox allowlist locks and `allowAllClaudeAiMcps` are honored when set by any admin-controlled source, not just the winning priority source [[line ~34](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/admin-setup.md?plain=1#L34)]
* Server-managed delivery now includes Claude apps gateway as an alternative to the claude.ai admin console for gateway sign-in sessions [[line ~38](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/admin-setup.md?plain=1#L38)]
* `disableSideloadFlags` added as a plugin marketplace control option to reject CLI flags that sideload plugins/agents/MCP servers for a single run
* Claude apps gateway added as a first-class option for per-user usage attribution, OTLP metrics with spend limits, and per-request audit logging with IdP identity

#### [Agent SDK — Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/agent-sdk/hooks.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

* Matcher character set for exact matching expanded to include hyphens (v2.1.195); regex matchers documented as unanchored with guidance to use `^` and `$`
* `mirror_error` retry behavior updated: failed batches are retried up to 3 times total; timeouts are not retried

#### [Agent SDK — Python](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* New `skills` parameter added to agent invocation: accepts a list of skill names or `"all"`
* Monitor tool now supports WebSocket source (`ws` field with `url` and optional `protocols`); mutually exclusive with `command` (v2.1.195)

#### [Agent SDK — Session storage](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/agent-sdk/session-storage.md) [[Source](https://code.claude.com/docs/en/agent-sdk/session-storage)]

* `append()` retry behavior: failed batches retried up to 3 times total (2 retries); timed-out calls not retried; implementers must deduplicate by `entry.uuid` since retries can re-deliver entries

#### [Agent SDK — TypeScript](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* New `reinitialize()` method on the query object: re-sends the `initialize` control request after a transport gap; existing pending permission requests are re-dispatched to `canUseTool` (v2.1.195)
* `prompt_id` field added to context: UUID correlating to OTel events (v2.1.196)
* Monitor tool gains `ws` WebSocket source option (v2.1.195)

#### [Agent teams](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

* `"auto"` mode for iTerm2 split panes now requires the `it2` CLI to be on `PATH`

#### [Agent view](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* Single `←` press now backgrounds a foreground session (two presses were required before); if tools are running, waits ~10 seconds then offers immediate background (v2.1.196)
* In-flight work handoff: background shell commands, backgrounded subagents, dynamic workflows, and `/loop` tasks carry over to the background session; set `CLAUDE_DISABLE_ADOPT=1` to stop (v2.1.196)
* Default session names appear in listings and `--json` output (v2.1.196)
* Misread transcripts on restart now renamed with `.orphaned-` suffix instead of deleted (v2.1.196)
* New "Version history" table added documenting all behavioral changes since v2.1.139

#### [Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* New troubleshooting entry: `/context` showing 0 token counts for tools on Bedrock is fixed in v2.1.196 (Bedrock's count-tokens API rejected schemas with extra fields)

#### [Authentication](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/authentication.md) [[Source](https://code.claude.com/docs/en/authentication)]

* Claude apps gateway added as a new authentication option: sign in with corporate SSO via `/login`; gateway sessions outrank all other credential methods

#### [Auto mode configuration](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/auto-mode-config.md) [[Source](https://code.claude.com/docs/en/auto-mode-config)]

* `autoMode.classifyAllShell` setting documented: suspends all shell allow rules in auto mode so every shell command goes through the classifier (v2.1.193)
* New trust/sensitivity slots documented: Internal package registry, PII/regulated-data locations, Sensitive remote targets, Protected IaC scopes (v2.1.195)
* Classifier denial reason now appears in the transcript, denial notification, and Recently denied tab (v2.1.193)

#### [CLI reference](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* New `claude gateway` command (v2.1.195): starts the self-hosted Claude apps gateway server; requires `--config` pointing at a `gateway.yaml`

#### [Commands](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* Two new slash commands: `/design-login` (authorizes design-system access) and `/design-sync [hint]` (converts repo's React design system and uploads to Claude Design); not available on Bedrock/Vertex/Foundry

#### [Computer use](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/computer-use.md) [[Source](https://code.claude.com/docs/en/computer-use)]

* Computer use lock is now held until the session exits, not just until the task finishes; stopping with Esc or Ctrl+C keeps the lock until session exit (v2.1.195)

#### [Costs](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* Claude apps gateway documented as providing per-user usage attribution, OTLP metrics with token counts, and per-user spend limits on Bedrock/Vertex/Foundry

#### [Data usage](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/data-usage.md) [[Source](https://code.claude.com/docs/en/data-usage)]

* Bug reports on Bedrock/Vertex/Foundry/gateway sessions now write to a local archive under `~/.claude/feedback-bundles/` instead of uploading to Anthropic
* Claude apps gateway sessions: usage analytics, error reporting, and survey ratings to Anthropic are disabled by the gateway credential with no way to re-enable them

#### [Deep links](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/deep-links.md) [[Source](https://code.claude.com/docs/en/deep-links)]

* `cwd` parameter now also rejects paths containing invisible or bidirectional control characters

#### [Discover plugins](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* `https://` prefix required for URL marketplaces; v2.1.196 explicitly rejects hosts without scheme
* `claude plugin install` now opens a details page where you choose scope; `--scope` flag available for non-interactive installs
* As of v2.1.195, project-enabled plugins from external sources require each user to install and trust the plugin before it runs

#### [Environment variables](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `ANTHROPIC_BASE_URL`: Remote Control now disabled when pointing at a non-`api.anthropic.com` host (v2.1.196)
* New `CLAUDE_CODE_DISABLE_BG_EXIT_HANDOFF`: stops handing off background shell commands and dynamic workflows when the supervisor stops/restarts (v2.1.196)
* New `CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP`: stops terminating background shell commands on memory pressure (v2.1.193); no effect on Windows
* New `CLAUDE_CODE_DISABLE_MOUSE_CLICKS`: disables click/drag/hover in fullscreen while keeping wheel scroll (v2.1.195)
* New `CLAUDE_CODE_DISABLE_NOTIFICATION_PRESENCE_CHECK`: sends desktop notification even when active in the terminal (v2.1.193)
* `CLAUDE_ENABLE_STREAM_WATCHDOG`: now **on by default for all providers** — set to `0` to disable (v2.1.196)
* New `CLAUDE_DISABLE_ADOPT`: stops carrying in-flight background work when backgrounding a session (v2.1.195)
* New `OTEL_LOG_ASSISTANT_RESPONSES`: enables logging of assistant response text (v2.1.193)

#### [Errors](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New error entry: "Remote Control is only available when using Claude via api.anthropic.com" — now triggered by a non-Anthropic `ANTHROPIC_BASE_URL` (v2.1.196)

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Hyphenated matcher names (e.g. `code-reviewer`) now match exactly as of v2.1.195; earlier versions treated them as unanchored regex
* Regex matchers documented as unanchored (`RegExp.prototype.test`); guidance added to use `^` and `$` for whole-string match
* New `prompt_id` environment variable on hook events: UUID correlating the hook to OTel events (v2.1.196)
* `UserPromptSubmit` timeout behavior documented: canceled hook output is discarded and the prompt still reaches Claude; v2.1.196 adds a transcript notice when this happens

#### [Interactive mode](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* File path autocomplete in Bash tool documented (v2.1.193): type `/` to trigger dropdown for files and directories; `Tab` to accept
* Memory pressure reap behavior documented (v2.1.193): idle background shell commands terminated on macOS/Linux after 30 minutes of session idle time

#### [LLM gateway (Other LLM gateways)](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/llm-gateway.md) [[Source](https://code.claude.com/docs/en/llm-gateway)]

* Scope narrowed to third-party/other gateways now that Claude apps gateway has its own pages; Google Vertex AI renamed to "Google Cloud's Agent Platform" throughout

#### [LLM gateway connect](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/llm-gateway-connect.md) [[Source](https://code.claude.com/docs/en/llm-gateway-connect)]

* Remote Control also disabled when `ANTHROPIC_BASE_URL` points at a non-Anthropic host (v2.1.196); must unset both the gateway credential and `ANTHROPIC_BASE_URL` to restore
* Google Vertex AI section renamed to "Google Cloud's Agent Platform"

#### [LLM gateway protocol](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/llm-gateway-protocol.md) [[Source](https://code.claude.com/docs/en/llm-gateway-protocol)]

* Claude apps gateway serves a machine-readable protocol spec at `GET /protocol`
* `defer_loading: true` cannot be combined with `cache_control`; returns 400
* Tool use examples now work with tool search

#### [LLM gateway rollout](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/llm-gateway-rollout.md) [[Source](https://code.claude.com/docs/en/llm-gateway-rollout)]

* Clarified that `forceLoginMethod` with any value (not just specific values) blocks `ANTHROPIC_API_KEY` and similar credentials

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* `enableAllProjectMcpServers` and `enabledMcpjsonServers` in a project's `.claude/settings.json` are now ignored in an untrusted folder (v2.1.196)
* OAuth token refresh failure now immediately shows a notice pointing to `/mcp` for re-authentication (v2.1.195)
* OAuth scope request no longer fetches the full `scopes_supported` catalog to avoid `invalid_scope` errors (v2.1.196)
* Bearer token auto-retry on 401/403: re-runs `headersHelper`, reconnects, and retries once before marking the server as needing auth (v2.1.193)
* New `CLAUDE_PLUGIN_ROOT` environment variable exposed to `headersHelper` for plugin-provided servers (v2.1.195)

#### [Model configuration](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Resumed sessions: `ANTHROPIC_DEFAULT_OPUS_MODEL` family variables now take precedence over the restored model, same as `--model` and `ANTHROPIC_MODEL` (v2.1.195)

#### [Monitoring usage](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* New `OTEL_LOG_ASSISTANT_RESPONSES` env var: logs assistant response text; falls back to `OTEL_LOG_USER_PROMPTS` when unset (v2.1.193)
* New `claude_code.assistant_response` OTel event documented: logged after each API request returning text; includes `response_length`, `response`, `model`, `request_id`, `query_source` (v2.1.193)
* Claude apps gateway identity stamping: on gateway sessions, `user.id` is the IdP subject, `user.email` is the signed-in email, `user.groups` carries IdP group membership, and `identity.source: gateway-oidc` is set

#### [Network configuration](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/network-config.md) [[Source](https://code.claude.com/docs/en/network-config)]

* OS certificate store reading (`CLAUDE_CODE_CERT_STORE`) requires `tls.getCACertificates`; npm installs need Node 22.15+

#### [Permission modes](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* `"auto"` mode now cycles in without a confirmation prompt
* Claude apps gateway sessions require `CLAUDE_CODE_ENABLE_AUTO_MODE=1` and only support Opus 4.7 and 4.8
* New auto-mode block categories documented (v2.1.195): writing to secret managers, merging unapproved PRs, production feature flag changes, IaC apply to protected scopes, DaemonSets, interactive shells into sensitive targets, public internet tunnels, PII access
* New auto-mode allow categories (v2.1.195): deleting jobs Claude created in the same session, security code review, inter-agent messages, data sent to trusted domains

#### [Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* `disableSideloadFlags` listed as a new managed-settings-only permission control
* Claude apps gateway listed as a valid managed settings delivery channel

#### [Plugin dependencies](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/plugin-dependencies.md) [[Source](https://code.claude.com/docs/en/plugin-dependencies)]

* Local folder marketplace git repos now support tag-based version constraints (v2.1.196)

#### [Plugin marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* New `renames` field in `marketplace.json`: maps former plugin names to current names or `null` for removed plugins; automatic migration for users; requires v2.1.193
* `disableSideloadFlags` paired with `strictKnownMarketplaces` for lockdown documented

#### [Plugins reference](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* Plugin `name` field: the marketplace entry name (not `plugin.json` name) is what `enabledPlugins` keys use when names differ

#### [Remote control](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Remote Control now disabled when `ANTHROPIC_BASE_URL` points at a non-`api.anthropic.com` host (v2.1.196), even with a claude.ai sign-in
* Auto-connect setting now has three states: `true` (always), `false` (never), or unset (follow org default)

#### [Scheduled tasks](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/scheduled-tasks)]

* As of v2.1.196, scheduled fires only run skills Claude is allowed to invoke on its own; built-in commands, `disable-model-invocation: true` skills, withheld skills, and MCP prompts are passed as plain text
* Backgrounding a session now carries `/loop` tasks to the background session

#### [Server-managed settings](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* `policyHelper` now preempts all other managed sources including server-managed settings (was previously described as replacing only file-based)
* New `claudeMd` value can be delivered through managed settings
* Claude apps gateway documented as equivalent managed-settings delivery for Bedrock/Vertex/Foundry; gateway clients exit at startup with an error if the gateway is unreachable (not fail-open)

#### [Sessions](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/sessions.md) [[Source](https://code.claude.com/docs/en/sessions)]

* Default session names added (v2.1.196): interactive sessions that are never named get a display name like `my-app-3f` appearing in agent view and `claude agents --json`
* `/export` now opens a menu instead of going directly to clipboard; passing a filename still skips the menu

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New `autoMode.classifyAllShell` (v2.1.193): forces all shell commands through classifier in auto mode
* New `disableSideloadFlags` (v2.1.193): blocks `--plugin-dir`, `--plugin-url`, `--agents`, and `--mcp-config` CLI flags at startup
* `enableAllProjectMcpServers`/`enabledMcpjsonServers` now only honored in untrusted folders from settings files not checked into the repo (v2.1.196)
* New `enableArtifact` setting: enables/disables the Artifact tool per user (v2.1.196)
* `env` setting: identity variables like `CLAUDE_CODE_REMOTE` are ignored when set here (v2.1.195)
* New `forceLoginMethod: "gateway"` and `forceLoginGatewayUrl` settings for locking login to a Claude apps gateway
* `maxSkillDescriptionChars` renamed to `skillListingMaxDescChars`
* `statusLine` gains optional `padding`, `refreshInterval`, and `hideVimModeIndicator` fields
* Cross-source lock key exceptions documented: sandbox locks and `allowAllClaudeAiMcps` are honored when set by any admin-controlled source

#### [Skills](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* `disable-model-invocation: true` now also prevents a skill from running when a scheduled task fires with it as the prompt (v2.1.196)
* New `${CLAUDE_PROJECT_DIR}` substitution available in skill body and `allowed-tools` frontmatter (v2.1.196)
* `maxSkillDescriptionChars` renamed to `skillListingMaxDescChars`

#### [Statusline](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/statusline.md) [[Source](https://code.claude.com/docs/en/statusline)]

* New `prompt_id` field: UUID identifying the current user prompt; matches OTel events; requires v2.1.196

#### [Sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Duplicate agent name detection: `/doctor` now reports same-scope duplicates and shows which definition is active (v2.1.196)
* Plugin-scoped agent names (e.g. `my-plugin:db-agent`) contain a colon and are evaluated as unanchored regex in hook matchers; must be anchored with `^` and `$`
* Hyphenated matchers (e.g. `db-agent`) now match exactly as of v2.1.195

#### [Third-party integrations](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/third-party-integrations.md) [[Source](https://code.claude.com/docs/en/third-party-integrations)]

* Google Vertex AI renamed to "Google Cloud's Agent Platform" throughout

#### [Tools reference](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* Monitor tool now supports WebSocket source (`ws` input) in addition to shell commands; new section documenting URL requirements, denial rules for private/metadata IPs, event handling, and approval behavior (v2.1.195)
* New `ReportFindings` tool (v2.1.196): reports code-review findings as a typed structured list; only invoke when active code-review instructions specify it
* `SendUserFile` tool: new optional `display` input with values `render`, `attach`, or unset (v2.1.196)
* Computer vision: images over 500KB after initial resize are now re-encoded as JPEG at reduced quality (v2.1.196)

#### [Voice dictation](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/voice-dictation.md) [[Source](https://code.claude.com/docs/en/voice-dictation)]

* Three-word auto-submit threshold now correctly counts individual words for Japanese, Chinese, and Thai (v2.1.195)
* New error: "Voice mode is disabled by your organization's policy"

#### [What's new (2026-W23)](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/whats-new/2026-w23.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w23)]

* Updated weekly changelog with changes from the past week

#### [Workflows](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/claude-code/workflows.md) [[Source](https://code.claude.com/docs/en/workflows)]

* Verifier agents that cannot confirm a claim now mark it as `unverified` instead of `refuted` (v2.1.196)

-----

## API changes

### Changed documents

#### [Agent Skills overview](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/api/agents-and-tools/agent-skills/overview.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)]

* Agent Skills on Microsoft Foundry now require a "Hosted on Anthropic" deployment

#### [MCP connector](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/api/agents-and-tools/mcp-connector.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)]

* MCP connector on Microsoft Foundry now requires a "Hosted on Anthropic" deployment

#### [Fine-grained tool streaming](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/api/agents-and-tools/tool-use/fine-grained-tool-streaming.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)]

* `eager_input_streaming` per-tool field documented as replacing the legacy `fine-grained-tool-streaming-2025-05-14` beta header
* Guidance added: check `stop_reason` for `max_tokens` as it can truncate parameters mid-stream
* Invalid JSON handling rewritten: wrap in `{"INVALID_JSON": ...}` object and return with `is_error: true`

#### [Programmatic tool calling](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)]

* Programmatic tool calling on Microsoft Foundry now requires a "Hosted on Anthropic" deployment

#### [Tool search tool](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/api/agents-and-tools/tool-use/tool-search-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)]

* New model compatibility table listing which models support which tool search variants
* `defer_loading: true` cannot be combined with `cache_control` (returns 400)
* Tool use examples now documented as working with tool search (previously listed as incompatible)
* New error codes: `invalid_tool_input` (renamed from `invalid_pattern`), `execution_time_exceeded`
* BM25 query max length documented: 500 characters
* "Continuing the conversation" section added with explicit guidance on follow-up requests

#### [Web fetch tool](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]

* Web fetch on Microsoft Foundry now requires "Hosted on Anthropic" deployment
* Documented behavior when mixing server tools and client tools in the same request: API returns `stop_reason: "tool_use"` before the fetch runs; fetch runs when you return the client `tool_result`

#### [Web search tool](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/api/agents-and-tools/tool-use/web-search-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]

* Web search on Microsoft Foundry now requires a "Hosted on Anthropic" deployment

#### [Claude in Microsoft Foundry](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/api/build-with-claude/claude-in-microsoft-foundry.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)]

* Two new hosting options documented: "Hosted on Azure" and "Hosted on Anthropic" — with a full feature comparison table; many features (structured outputs, server-side tools, MCP connector, Agent Skills, programmatic tool calling, Files API) are only available on "Hosted on Anthropic"
* "US Data Zone Standard" deployment type added (equivalent to `inference_geo: "us"`)
* Claude Consumption Units (CCUs) documented for Azure Marketplace billing
* Deployment steps and key retrieval steps rewritten for new Foundry portal layout
* Azure RBAC role updated to "Foundry User" (formerly "Azure AI User") or "Cognitive Services User"
* Migration between hosting options procedure documented
* Claude Opus 4.8 gains 1M token context window on Foundry

#### [Compaction](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/api/build-with-claude/compaction.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]

* `trigger` parameter default documented as full object: `{"type": "input_tokens", "value": 150000}`
* `usage.iterations` is now included in every response when compaction beta is enabled, even when no compaction occurred
* Budget-tracking pattern examples added in multiple languages with cURL tabs

#### [Context windows](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/api/build-with-claude/context-windows.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]

* New context window sizes table including Fable 5 and Mythos 5
* Thinking block preservation behavior now model-dependent: Opus 4.5+, Sonnet 4.6+, Fable 5, Mythos 5 keep previous thinking blocks by default; earlier models strip them
* Interleaved thinking is now automatic on adaptive thinking models; Opus 4.5, Sonnet 4.5, and earlier Claude 4 require the `interleaved-thinking-2025-05-14` beta header

#### [Fast mode](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/api/build-with-claude/fast-mode.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]

* Claude Opus 4.6 fast mode removed as of June 29, 2026: requests with `speed: "fast"` silently run at standard speed and billing
* Claude Opus 4.7 fast mode deprecated June 25, 2026; removed July 24, 2026 — will error (no silent fallback)

#### [Mid-conversation system messages](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/api/build-with-claude/mid-conversation-system-messages.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages)]

* Microsoft Foundry now supports mid-conversation system messages (previously documented as unavailable)

#### [Build with Claude overview](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/api/build-with-claude/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

* Multiple features moved from Beta to GA on Microsoft Foundry: context windows, adaptive thinking, citations, effort, extended thinking, PDF support, search results, structured outputs, prompt caching (automatic, 5m, 1hr), token counting, memory, text editor, bash, programmatic tool calling, tool search
* Features marked as requiring "Hosted on Anthropic" deployments on Foundry denoted with `†` footnote

#### [Prompt caching](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* Microsoft Foundry references no longer marked as beta; workspace-level cache isolation confirmed for Foundry

#### [Structured outputs](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/api/build-with-claude/structured-outputs.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

* Structured outputs on Microsoft Foundry moved from beta to GA; requires "Hosted on Anthropic" deployment

#### [Data residency](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/api/manage-claude/data-residency.md) [[Source](https://platform.claude.com/docs/en/manage-claude/data-residency)]

* `inference_geo` not applicable to Foundry; "US Data Zone Standard" deployment type achieves the same for Hosted on Azure, with the same 1.1x pricing multiplier

#### [Workspaces](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/api/manage-claude/workspaces.md) [[Source](https://platform.claude.com/docs/en/manage-claude/workspaces)]

* Microsoft Foundry "beta" qualifier removed from prompt cache workspace isolation

#### [Memory](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/api/managed-agents/memory.md) [[Source](https://platform.claude.com/docs/en/managed-agents/memory)]

* Memory store mount path: directory name is now the store's display name sanitized to a filesystem slug (lowercase, non-alphanumeric runs become a single hyphen); exact path returned in `mount_path` field
* Writes to paths outside the mount path land in container-local scratch and are not persisted
* System prompt description updated to include the display name and mount path

#### [Skills](https://github.com/gpambrozio/ClaudeDocs/blob/33782309/docs-md/api/managed-agents/skills.md) [[Source](https://platform.claude.com/docs/en/managed-agents/skills)]

* New "Create a custom skill" section with code examples for uploading via cURL, CLI, and SDKs
* `version` parameter for custom skills now documented as optional (defaults to `"latest"`)
