# [Claude docs changes for May 19th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/435a884) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/435a884)]

## Executive Summary
- **MCP tunnels (Research Preview):** New feature lets you connect Claude to MCP servers running in your private network via outbound-only connections, with full deployment guides (Docker Compose, Helm), Admin API, and security documentation
- **Self-hosted sandboxes for Managed Agents:** New guide and security model for running Managed Agent tool execution in your own infrastructure instead of Anthropic-managed cloud containers
- **Cache diagnostics (beta):** New `cache-diagnosis-2026-04-07` beta feature lets you pass the previous response ID to identify exactly why a prompt cache miss occurred (model changed, system changed, tools changed, messages changed)
- **Computer use improvements:** Added model-specific thinking `effort` recommendations, click accuracy guidance (instruction before screenshot), macOS Retina display scaling notes, and a click diagnostics troubleshooting table
- **Claude Code 2.1.144:** Major release with `/model` now session-scoped, `/usage-credits` rename, many background session improvements, and over 25 bug fixes including startup hang and terminal display corruption

## New Claude Code versions

### [2.1.144](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/versions/2.1.144.md)

#### New features

* Added `/resume` support for background sessions — sessions started via `claude --bg` or agent view now appear alongside interactive ones, marked with `bg`
* Added elapsed duration to background subagent completion notifications (e.g. "Agent completed · 3h 2m 5s")
* `/plugin` browse and discover panes now show when a plugin was last updated
* `/model` now changes the model for the current session only; press `d` in the model picker to set a default for new sessions
* Renamed "extra usage" to "usage credits" across CLI copy; `/extra-usage` is now `/usage-credits` (old name still works)

#### Existing feature improvements

* Improved recovery from rare pre-response stream stalls — now retries streaming once instead of falling back to a slower non-streaming request
* Improved SDK/headless MCP startup: pre-wait now overlaps startup instead of blocking before the first turn (up to 2s faster with slow MCP servers)
* `/doctor` now shows an exec-form example when a command hook is missing the `command` field
* `/plugin` now returns to the Installed list after enabling, disabling, or uninstalling a plugin
* Skill-listing truncation is no longer shown as a startup notification — run `/doctor` for the full breakdown
* Background session worktree isolation guard now applies for non-git VCS users with `WorktreeCreate` hooks configured
* `claude agents`/`--bg` rejection messages now name the specific gate (non-TTY, env var, or setting) instead of a generic message
* `claude --bg --name <label>` now echoes the name in the post-spawn confirmation
* `/bg` and `←`-detach now preserve directories added via `/add-dir`

#### Major bug fixes

* Fixed startup hanging up to 75s when `api.anthropic.com` is unreachable (captive portal, firewall, VPN issues) — side-channel API calls now time out after 15s
* Fixed garbled terminal output after a missed window-resize event (e.g. dragging a VS Code split-pane divider) — now self-heals on the next frame instead of requiring Ctrl+L
* Fixed progressive terminal display corruption in very long sessions that only cleared on terminal resize or restart
* Fixed macOS background sessions crashing with "exit 1 before init" when the project lives under a Full Disk Access-protected folder (regression in 2.1.143)
* Fixed unrecoverable conversation when reading a file whose image extension doesn't match its contents (e.g. HTML saved as .png)
* Fixed `head`/`tail` file views not satisfying the read-before-edit check; "no matches" result (exit code 1) from `egrep`, `fgrep`, `git grep`, or `git diff` is no longer reported as a command failure
* Fixed `/branch` failing with "No conversation to branch" after entering a worktree or in some background sessions
* Fixed pressing Escape in the AskUserQuestion notes field aborting the turn instead of returning to answer selection
* Fixed model selection not applying when changed via the IDE model picker or `applyFlagSettings` after startup
* Fixed Bedrock and Vertex users unable to select "Opus (1M context)" from the `/model` picker (regression in v2.1.129)
* Fixed remote-session login failing with "Can't access this organization" for users with `forceLoginMethod` and `forceLoginOrgUUID` set
* Fixed MCP servers with paginated `tools/list` responses only returning the first page, silently dropping tools
* Fixed MCP images with unsupported MIME types (e.g. SVG) breaking the conversation — now saved to disk and referenced in the tool result
* Fixed file descriptor exhaustion when a build runs inside a skill directory — non-`.md` files no longer trigger skill reloads
* Fixed Skill tool failing with permission error in headless mode (regression in v2.1.141)
* Fixed `claude mcp list` silently reporting no servers when `.mcp.json` can't be parsed (e.g. using VS Code's `"servers"` key)
* Fixed scrolling in attached background sessions on Windows (PgUp/PgDn, mouse wheel, Ctrl+O)
* Fixed crash when closing the terminal while attached to a background session
* Fixed `! <cmd>` exec sessions not responding to Ctrl+C while attached
* Fixed `/resume` picker not showing sessions forked from a background session
* Fixed background Bash tasks spawned by subagents staying "Running" in SDK task panels after the process exits
* Fixed markdown links in `claude agents` attached sessions rendering as plain text instead of clickable hyperlinks

-----

## Claude Code changes

*(No Claude Code documentation changes this day)*

-----

## API changes

### New Documents

#### [Admin: MCP Tunnels](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/api/admin/mcp_tunnels.md) [[Source](https://platform.claude.com/docs/en/api/admin/mcp_tunnels)]

Admin API reference for managing MCP tunnels. Documents endpoints to get, list, reveal token, rotate token, and archive tunnels, along with tunnel certificate management (create, list, retrieve, archive). Includes the `MCPTunnelRetrieveResponse` model with fields like `id`, `domain`, `archived_at`, `display_name`, and `type`.

#### [Beta: Environments Work](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/api/beta/environments/work.md) [[Source](https://platform.claude.com/docs/en/api/beta/environments/work)]

New Work queue API for self-hosted sandbox environments. Documents the `BetaSelfHostedWork` model and endpoints for polling work items, acknowledging work, recording heartbeats, stopping work, listing work items, updating work item metadata, and retrieving queue statistics (`depth`, `pending`, `oldest_queued_at`, `workers_polling`).

#### [Beta: Skills - Download Skill Version Content](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/api/beta/skills/versions/download.md) [[Source](https://platform.claude.com/docs/en/api/beta/skills/versions/download)]

New endpoint `GET /v1/skills/{skill_id}/versions/{version}/content` to download a skill version's content as a zip archive. Requires the `skills-2025-10-02` beta header.

#### [Build with Claude: Cache Diagnostics](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/build-with-claude/cache-diagnostics.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics)]

New guide for the `cache-diagnosis-2026-04-07` beta feature. Explains how to pass `diagnostics.previous_message_id` on each turn to identify prompt cache divergences. Documents all `cache_miss_reason` types (`model_changed`, `system_changed`, `tools_changed`, `messages_changed`, `previous_message_not_found`, `unavailable`), how to combine diagnostics with `cache_read_input_tokens`, streaming usage, data retention, and limitations.

#### [MCP Tunnels: Console Setup](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/agents-and-tools/mcp-tunnels/console.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/console)]

Guide for creating and managing MCP tunnels in the Claude Console, including how to add CA certificates and retrieve tunnel connection details.

#### [MCP Tunnels: Deploy with Docker Compose](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/agents-and-tools/mcp-tunnels/deploy-compose.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-compose)]

Step-by-step deployment guide for running an MCP tunnel stack on a VM using Docker Compose, covering both programmatic (Workload Identity Federation) and manual credential authentication.

#### [MCP Tunnels: Deploy with Helm](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/agents-and-tools/mcp-tunnels/deploy-helm.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm)]

Step-by-step deployment guide for installing an MCP tunnel on a Kubernetes cluster using the Anthropic Helm chart.

#### [MCP Tunnels: Overview](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/agents-and-tools/mcp-tunnels/overview.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview)]

Overview of the MCP tunnels Research Preview feature. Explains how outbound-only tunnel connections via `cloudflared` and an Anthropic proxy let Claude reach private-network MCP servers without inbound firewall changes. Covers the three-layer security model (outer mTLS, inner TLS, OAuth), shared responsibility model, network requirements, and how to use tunneled servers from both Managed Agents Console and the Messages API.

#### [MCP Tunnels: Quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/agents-and-tools/mcp-tunnels/quickstart.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/quickstart)]

Quickstart guide for getting a working MCP tunnel locally using Docker Compose with a sample MCP server.

#### [MCP Tunnels: Reference](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/agents-and-tools/mcp-tunnels/reference.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/reference)]

Reference documentation covering proxy configuration fields, the Tunnels API, certificate requirements, and the setup CLI.

#### [MCP Tunnels: Security](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/agents-and-tools/mcp-tunnels/security.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/security)]

Security hardening guidance for MCP tunnels: credential rotation procedures, breach response steps, and hardening recommendations for the proxy and MCP servers.

#### [MCP Tunnels: Troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/agents-and-tools/mcp-tunnels/troubleshooting.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/troubleshooting)]

Troubleshooting guide for diagnosing connectivity, TLS, and routing issues with MCP tunnels.

#### [Managed Agents: Self-Hosted Sandboxes](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/managed-agents/self-hosted-sandboxes.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

New guide for running Managed Agent tool execution in your own infrastructure. Covers the environment worker concept (always-on vs webhook-triggered), sandbox filesystem layout (`/workspace`, `/mnt/session/outputs`), in-process and container-per-session deployment patterns with the `ant` CLI and SDK, session creation targeting a self-hosted environment, and monitoring operations (queue depth, graceful session stop). Includes integration notes for Cloudflare, Daytona, Modal, and Vercel platforms.

#### [Managed Agents: Self-Hosted Sandboxes Security](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/managed-agents/self-hosted-sandboxes-security.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-security)]

Security model for self-hosted sandboxes defining the shared responsibility boundary: container image hardening, network egress controls, environment key rotation, tool-execution blast radius, and log retention are all the operator's responsibility.

### Changed documents

#### [Admin](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/api/admin.md) [[Source](https://platform.claude.com/docs/en/api/admin)]

* Added the new **AdminMCP Tunnels** section with endpoints: Get Tunnel, List Tunnels, Reveal Tunnel Token, Rotate Tunnel Token, Archive Tunnel. [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/435a884)]

#### [Admin: Workspaces - Archive](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/api/admin/workspaces/archive.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/archive)]

* `Workspace` object now includes a `tags` field (user-defined `map[string]` key-value pairs; keys may not begin with `anthropic`).

#### [Admin: Workspaces - Create](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/api/admin/workspaces/create.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/create)]

* Added optional `anthropic-beta` header parameter documentation.
* New optional `tags` body parameter (`map[string]`) added to workspace creation.
* `Workspace` response object updated to include `tags`.

#### [Admin: Workspaces - List](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/api/admin/workspaces/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/list)]

* `Workspace` object now includes the `tags` field.

#### [Admin: Workspaces - Retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/api/admin/workspaces/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/retrieve)]

* `Workspace` object now includes the `tags` field.

#### [Admin: Workspaces - Update](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/api/admin/workspaces/update.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/update)]

* `Workspace` object now includes the `tags` field.

#### [Beta: Environments](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/api/beta/environments.md) [[Source](https://platform.claude.com/docs/en/api/beta/environments)]

* `BetaEnvironment.config` now accepts `BetaSelfHostedConfig { type: "self_hosted" }` in addition to `BetaCloudConfig`.
* New `scope` field on `BetaEnvironment` (`"organization"` or `"account"`) controls environment visibility.

#### [Beta: Environments - Create](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/api/beta/environments/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/environments/create)]

* `config` body parameter now accepts `BetaSelfHostedConfigParams { type: "self_hosted" }` for creating self-hosted environments.
* New optional `scope` parameter (`"organization"` or `"account"`) for self-hosted environment visibility.
* Added `cache-diagnosis-2026-04-07` to the list of accepted beta headers.

#### [Beta: Environments - Update](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/api/beta/environments/update.md) [[Source](https://platform.claude.com/docs/en/api/beta/environments/update)]

* `config` body parameter now accepts `BetaSelfHostedConfigParams` for updating to self-hosted configuration.
* New optional `scope` parameter for updating visibility.
* Added `cache-diagnosis-2026-04-07` to the list of accepted beta headers.

#### [Beta: Messages](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/api/beta/messages.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages)]

* Added `BetaCacheMiss*` model types (`MessagesChanged`, `ModelChanged`, `SystemChanged`, `ToolsChanged`, `PreviousMessageNotFound`, `Unavailable`) documenting all possible `cache_miss_reason` variants.
* Added `BetaDiagnostics` response envelope model with `cache_miss_reason` field.

#### [Beta: Messages - Create](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/api/beta/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]

* Added `cache-diagnosis-2026-04-07` to accepted beta headers.
* New optional `diagnostics` request body field (`BetaDiagnosticsParam { previous_message_id }`) for opting into cache miss reporting.
* `BetaMessage` response now includes a `diagnostics` field with `cache_miss_reason` explaining the first point of prompt divergence.

#### [Beta: Messages - Count Tokens](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/api/beta/messages/count_tokens.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/count_tokens)]

* Added `cache-diagnosis-2026-04-07` to the list of accepted beta headers.

#### [Beta: Sessions](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/api/beta/sessions.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions)]

* Added `BetaManagedAgentsSessionAgentUpdate` type for mid-session agent configuration updates, allowing full replacement of `tools` and `mcp_servers` arrays without restarting the session.
* Outcome evaluation state values updated to use code formatting.

#### [Beta: Sessions - Create](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/api/beta/sessions/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions/create)]

* Added `cache-diagnosis-2026-04-07` to the list of accepted beta headers.

#### [Beta: Skills](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/api/beta/skills.md) [[Source](https://platform.claude.com/docs/en/api/beta/skills)]

* Added reference to the new **Download Skill Version Content** endpoint (`GET /v1/skills/{skill_id}/versions/{version}/content`).

#### [Computer Use Tool](https://github.com/gpambrozio/ClaudeDocs/blob/435a884/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]

* New best practice tip: place instruction text *before* the screenshot image in the user turn `content` array to improve click accuracy.
* Added model-specific recommended `thinking.effort` settings for computer use: `high` default for Opus 4.7; `medium` default for Sonnet 4.6 and Opus 4.6 (avoid `max`; `low` is cost-efficient on these models).
* Added macOS Retina display note: screenshots capture at 2× device pixel ratio — downscale by 2× before sending or halve the returned coordinates.
* New **Diagnose click issues** section with a symptom/cause/fix table covering offset clicks, near-miss clicks, wrong-element clicks, and consistently poor accuracy.
* Added model precision guidance: Sonnet 4.6 is more mechanically precise than Opus 4.6; Opus 4.7 narrows that gap and has a higher resolution limit.
* New **Manage screenshot history for prompt caching** section header added to implementation best practices.
