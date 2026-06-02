# [Claude docs changes for June 2nd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/bb3119d92df86a2957d3ab38b244111fa484a4e7) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/bb3119d92df86a2957d3ab38b244111fa484a4e7)]

## Executive Summary
- Customer-managed encryption keys (CMEK) added: new Admin API endpoints for registering AWS KMS, Google Cloud KMS, and Azure Key Vault keys to encrypt workspace data at rest, with full setup guides for each provider.
- Claude Code 2.1.160 released with security improvements (prompts before writing to shell startup files and build-tool configs), the `workflow` trigger keyword renamed to `ultracode`, and many background session/agent view bug fixes.
- New MCP quickstart guide added to Claude Code docs, covering step-by-step connection of local and hosted MCP servers with troubleshooting guidance.
- Programmatic tool calling docs clarified: `allowed_callers` is not a security boundary — it guides Claude but does not block direct API calls, and performance benchmarks added.
- Mid-conversation system messages docs substantially expanded with new use cases, placement rules, and a warning against placing untrusted content there.

## New Claude Code versions

### [2.1.160](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/versions/2.1.160.md)

#### New features

* Added prompt before writing to shell startup files (`.zshenv`, `.zlogin`, `.bash_login`) and `~/.config/git/` to prevent unintended command execution
* `acceptEdits` mode now prompts before writing build-tool config files that can grant code execution (`.npmrc`, `.yarnrc*`, `bunfig.toml`, `.bazelrc`, `.pre-commit-config.yaml`, `.devcontainer/`, etc.)
* Renamed the dynamic-workflow trigger keyword from `workflow` to `ultracode`; the trigger is now highlighted in violet in the prompt input
* New `claude daemon stop --any` command with `--keep-workers` flag for background daemon management

#### Existing feature improvements

* Edit no longer requires a separate Read after viewing a file with `grep`: single-file grep commands now satisfy the read-before-edit check
* Improved auto mode classifier latency by reducing reasoning on routine actions
* Improved performance of opening recently-inactive background agent sessions
* Improved background-session teardown to send SIGTERM before SIGKILL so cleanup handlers run
* Removed `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE` (now a no-op)
* Removed JetBrains plugin install suggestion from startup
* `ultracode` no longer offered on models that do not support it

#### Major bug fixes

* Fixed copy-on-select not writing to the Windows clipboard on WSL (now uses PowerShell interop instead of OSC 52)
* Fixed restoring a completed session from `claude agents` dropping chat history and re-running the original prompt
* Fixed background sessions re-attached after overnight retire losing their conversation and re-running the original prompt
* Fixed `claude --bg` occasionally failing with "socket missing" on cold-start
* Fixed background agents that resumed work being shown under Completed in the agents list
* Fixed `claude agents` freezing for several seconds when returning to the session list due to auto-updater re-checking on every exit
* Fixed Esc, arrow keys, and typing becoming unresponsive on Windows under heavy CPU load in agent view
* Fixed background agents emitting terminal sync-output markers to terminals that don't support them (Apple Terminal, tmux)
* Fixed CJK IME composition appearing at bottom-left instead of at the input caret in agent view
* Fixed valid `file:///C:/...` links being rewritten to a broken path on Windows
* Fixed voice mode failing to connect when the project directory or branch name contains non-ASCII characters
* Fixed auto mode unavailability message on third-party providers incorrectly blaming the model
* Fixed `/effort ultracode` incorrectly blaming the dynamic workflows setting when the model can't run xhigh
* Fixed model-not-found errors suggesting `--model` when running via the SDK where the flag doesn't apply
* Fixed Claude's past replies disappearing from scrollback when resuming a brief mode session with brief mode off
* Fixed vim mode `p` pasting on the line below instead of at the cursor

-----

## Claude Code changes

### New Documents

#### [Connect to MCP servers](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/mcp-quickstart.md) [[Source](https://code.claude.com/docs/en/mcp-quickstart)]

New quickstart guide for connecting MCP servers to Claude Code. Walks through the full add/verify/use/remove flow using a hosted docs server, covers local stdio servers (Playwright example), OAuth-authenticated servers (Sentry example), editing `.mcp.json` directly, changing server scope (local/user/project), and connecting from other surfaces (desktop, VS Code, web). Includes a troubleshooting section for common connection errors.

### Changed documents

#### [Agent SDK - claude-code-features](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/agent-sdk/claude-code-features.md) [[Source](https://code.claude.com/docs/en/agent-sdk/claude-code-features)]

* `claude.ai` MCP connectors are now loaded in SDK sessions when authenticated with a claude.ai subscription; use `strictMcpConfig: true` or `ENABLE_CLAUDEAI_MCP_SERVERS=false` to suppress them [[line ~45](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/agent-sdk/claude-code-features.md?plain=1#L45)]
* When `skills` is set and you pass an explicit `tools` list, you must include `"Skill"` in that list
* Hook callback return format changed: deprecated top-level `decision`/`reason` fields replaced with `hookSpecificOutput` containing `permissionDecision` and `permissionDecisionReason`
* Programmatic hooks now fire inside subagents; callback receives `agent_id` and `agent_type`

#### [Agent SDK - hooks](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/agent-sdk/hooks.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

* `updatedMCPToolOutput` is deprecated in favor of `updatedToolOutput`, which works for any tool type in both SDKs
* `permissionDecision: 'allow'` vs `'ask'` clarified: `'allow'` auto-approves; `'ask'` shows to the user for approval

#### [Agent SDK - plugins](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/agent-sdk/plugins.md) [[Source](https://code.claude.com/docs/en/agent-sdk/plugins)]

* Plugin manifest (`plugin.json`) is now optional; Claude Code auto-discovers components from directory layout when absent

#### [Agent SDK - python](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* `strict_mcp_config` now also suppresses `claude.ai` connectors
* Tool names corrected: `ListMcpResources` → `ListMcpResourcesTool` and `ReadMcpResource` → `ReadMcpResourceTool`
* `SandboxNetworkConfig` clarified: applies to sandboxed Bash commands only, does not restrict the WebFetch tool

#### [Agent SDK - sessions](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/agent-sdk/sessions.md) [[Source](https://code.claude.com/docs/en/agent-sdk/sessions)]

* `ClaudeSDKClient` can now call `connect()` and `disconnect()` manually as an alternative to using it as an async context manager

#### [Agent SDK - slash-commands](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/agent-sdk/slash-commands.md) [[Source](https://code.claude.com/docs/en/agent-sdk/slash-commands)]

* Argument variable numbering corrected: positional arguments now use `$0`, `$1` (0-indexed) instead of `$1`, `$2` (1-indexed)

#### [Agent SDK - streaming-output](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/agent-sdk/streaming-output.md) [[Source](https://code.claude.com/docs/en/agent-sdk/streaming-output)]

* Extended thinking is no longer listed as incompatible with streaming; it no longer blocks `StreamEvent` messages

#### [Agent SDK - streaming-vs-single-mode](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/agent-sdk/streaming-vs-single-mode.md) [[Source](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode)]

* "Hook integration" removed from the list of features unsupported in single-message input mode

#### [Agent SDK - typescript](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* `strictMcpConfig` now also suppresses `claude.ai` connectors
* Tool names corrected: `ListMcpResources` → `ListMcpResourcesTool` and `ReadMcpResource` → `ReadMcpResourceTool`
* `SandboxNetworkConfig` clarified: does not restrict WebFetch tool

#### [Agent view](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* Agent view row summaries fall back to the session's main model on third-party providers when no Haiku model is configured; new `ANTHROPIC_DEFAULT_HAIKU_MODEL` env var controls this [[~line 30](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/agent-view.md?plain=1#L30)]
* Voice dictation now works in agent view (dispatch input and peek-panel reply)
* Small set of commands (`/exit`, `/quit`, `/logout`) now run in agent view itself rather than dispatching to a new session
* Session restart persistence expanded: model, effort, and configuration flags all persist through supervisor stop/restart
* New storage path: `~/.claude/jobs/<id>/tmp/` as a per-session scratch directory; `CLAUDE_JOB_DIR` env var set on each background session
* New troubleshooting sections: daemon unresponsive recovery and macOS privacy permissions for Desktop/Documents/Downloads

#### [CLI reference](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* New `claude daemon stop --any` command documented with `--keep-workers` flag

#### [Desktop](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Desktop app now loads MCP servers from `claude_desktop_config.json` into Code tab sessions alongside `~/.claude.json` and `.mcp.json`; the standalone CLI still does not read this file

#### [Discover plugins](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* `/reload-plugins` token cost documented: newly loaded components are cache-friendly, but plugins providing MCP servers with non-deferred tools invalidate the cache

#### [Glossary](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/glossary.md) [[Source](https://code.claude.com/docs/en/glossary)]

* CLAUDE.md precedence model corrected: all discovered files are concatenated into context (ordered broadest to most specific), not overriding each other

#### [Hooks guide](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* `MessageDisplay` hook default timeout clarified as 10 seconds (shorter than the 30s for `UserPromptSubmit` and 600s for most other events)

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* `MessageDisplay` now has a 10-second default timeout for `command`, `http`, and `mcp_tool` types
* `MessageDisplay` section expanded with use-case bullets, note that Claude Code holds each batch until the hook returns, and working code examples for macOS/Linux and Windows
* `updatedMCPToolOutput` deprecated in favor of `updatedToolOutput`

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Link to the new MCP quickstart guide added at the top of the page
* MCP Tool Search description updated: "only tool names and server instructions load at session start" (previously "only tool names")

#### [Model config](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* `[1m]` suffix behavior corrected: applies to `opus` and `sonnet` aliases but does not extend the plan-mode Opus phase of `opusplan` (capped at 200K)

#### [Permission modes](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Auto mode decision order clarified: allow rules resolve immediately except writes to protected paths, which route to the classifier even when an allow rule matches

#### [Plugins reference](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* Two LSP server config fields removed: `shutdownTimeout` and `restartOnCrash` are no longer documented options

#### [Plugins](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/plugins.md) [[Source](https://code.claude.com/docs/en/plugins)]

* Plugin manifest (`plugin.json`) is now optional; any self-contained directory with skills, agents, hooks, or the manifest qualifies as a plugin

#### [Prompt caching](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/prompt-caching.md) [[Source](https://code.claude.com/docs/en/prompt-caching)]

* Cache invalidation trigger generalized: "The set of loaded tool definitions changes" replaces the more specific "An MCP server connects or disconnects"
* "Enabling or disabling a plugin" added as a new cache invalidation action
* MCP deferred tools behavior clarified: deferred tools do not invalidate cache on server changes; prefix-loaded tools do
* New section on plugin cache behavior: skills/hooks/agents are cache-friendly but plugins providing MCP servers follow the same rules as MCP connect/disconnect

#### [Voice dictation](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/voice-dictation.md) [[Source](https://code.claude.com/docs/en/voice-dictation)]

* Dictation now works in agent view (dispatch input and peek-panel reply focused)

#### [Workflows](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/claude-code/workflows.md) [[Source](https://code.claude.com/docs/en/workflows)]

* Comparison table expanded: "Agent teams" added as a fourth approach alongside subagents, skills, and workflows
* `workflow` keyword trigger dismissal shortcut corrected to `Option+W` (macOS) / `Alt+W` (Windows/Linux)
* New subsection: "Pass input to a saved workflow" — workflows can accept structured input via an `args` global parameter
* Workflow script persistence documented: every run writes its script to `~/.claude/projects/`
* Cost guidance added: run on a small slice first, and the `/workflows` view shows per-agent token usage

-----

## API changes

### New Documents

#### [cmek (Customer-managed encryption keys)](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/manage-claude/cmek.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

New overview page for Customer-Managed Encryption Keys (CMEK). Explains how CMEK works (attached per workspace, write-once, protects data written after key is enabled), prerequisites, availability (US regions only), what data is and is not encrypted, and limitations (irreversible, no retroactive encryption, latency, revocation delay up to 1 hour). Links out to provider-specific setup guides.

#### [cmek-aws-kms (Configure AWS KMS for CMEK)](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/manage-claude/cmek-aws-kms.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms)]

New step-by-step guide for configuring an AWS KMS key as a CMEK for an Anthropic organization. Covers creating a KMS key with a cross-account key policy (three required IAM statements), registering the key via the Admin API (`POST /v1/organizations/external_keys`), validating with an encrypt/decrypt roundtrip, and attaching to a workspace. Includes troubleshooting for encryption context mismatches, RCPs, and region mismatches.

#### [cmek-azure-key-vault (Configure Azure Key Vault for CMEK)](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/manage-claude/cmek-azure-key-vault.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-azure-key-vault)]

New step-by-step guide for configuring Azure Key Vault as a CMEK provider. Covers consenting the Anthropic multi-tenant app, creating an RSA key (3072-bit minimum), granting the `Key Vault Crypto User` role, verifying vault configuration (RBAC, purge protection, public access), registering and validating the key, and attaching to a workspace.

#### [cmek-google-cloud-kms (Configure Google Cloud KMS for CMEK)](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/manage-claude/cmek-google-cloud-kms.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-google-cloud-kms)]

New step-by-step guide for configuring Google Cloud KMS as a CMEK provider. Covers creating a key ring and HSM-protected symmetric key, granting the Anthropic service account encrypt/decrypt and viewer roles, registering and validating the key via Admin API, and attaching to a workspace. Includes domain-restricted sharing and VPC Service Controls troubleshooting.

#### [external_keys (External Keys Admin API)](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/api/admin/external_keys.md) [[Source](https://platform.claude.com/docs/en/api/admin/external_keys)]

New Admin API reference page for CMEK External Keys. Documents six endpoints: Create, List, Get, Update, Delete, and Validate. Includes full object schemas for AWS KMS (`kms_arn`, `role_arn`), GCP Cloud KMS (`key_name`), and Azure Key Vault (`key_name`, `tenant_id`, `vault_uri`, optional `client_id`) provider configs. The Validate endpoint returns HTTP 200 with `status: "success" | "failure"`.

#### [MCP tunnels - concepts (Architecture and components)](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/agents-and-tools/mcp-tunnels/concepts.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts)]

New reference page defining MCP tunnel architecture terms. Documents canonical names for: tunnel stack, proxy (`mcp-proxy`), cloudflared, setup component, tunnel edge, inner TLS, and upstream MCP server. Explains credential provisioning modes (programmatic via WIF vs. manual), and the connection model (outbound connection direction vs. inbound request direction).

#### [Managed Agents - reference](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/managed-agents/reference.md) [[Source](https://platform.claude.com/docs/en/managed-agents/reference)]

New consolidated reference page for Claude Managed Agents. Contains: full event type catalog (user, agent, session, span events), self-hosted worker CLI flags (`ant beta:worker`), supported MCP server types, rate limits (300 RPM for create, 600 RPM for read), and branding guidelines for partners integrating Managed Agents.

#### [Managed Agents - session-operations](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/managed-agents/session-operations.md) [[Source](https://platform.claude.com/docs/en/managed-agents/session-operations)]

New page for session lifecycle operations (spun out from sessions.md). Documents session statuses (`idle`, `running`, `rescheduling`, `terminated`), updating agent configuration mid-session (full-replacement semantics, session must be idle), and retrieve/list/archive/delete operations with code examples.

### Changed documents

#### [Admin API](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/api/admin.md) [[Source](https://platform.claude.com/docs/en/api/admin)]

* New "Admin External Keys" section added with six new CMEK endpoints for create, list, get, update, delete, and validate operations on organization-scoped external key configs [[~line 150](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/api/admin.md?plain=1#L150)]

#### [Admin workspaces - archive](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/api/admin/workspaces/archive.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/archive)]

* Workspace object schema gains two new CMEK fields: `compartment_id` (encryption compartment identifier, used in KMS key policies) and `external_key_id` (write-once CMEK config ID)

#### [Admin workspaces - create](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/api/admin/workspaces/create.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/create)]

* New optional request field `external_key_id` for attaching a CMEK config at workspace creation time (write-once constraint)
* Response schema gains `compartment_id` and `external_key_id` fields

#### [Admin workspaces - list](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/api/admin/workspaces/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/list)]

* Workspace objects in list response gain `compartment_id` and `external_key_id` fields

#### [Admin workspaces - retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/api/admin/workspaces/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/retrieve)]

* Workspace object gains `compartment_id` and `external_key_id` fields

#### [Admin workspaces - update](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/api/admin/workspaces/update.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/update)]

* New optional request field `external_key_id` for attaching a CMEK config via workspace update (write-once)
* Response schema gains `compartment_id` and `external_key_id` fields

#### [MCP tunnels - console](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/agents-and-tools/mcp-tunnels/console.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/console)]

* Role requirement clarified: now specifies "a Console role with the Manage tunnels permission" (org admins/owners have it by default)
* Prerequisites reorganized into a comparison table showing with/without programmatic access requirements side-by-side
* Token reveal/rotation events noted as recorded in the organization's Compliance API activity log

#### [MCP tunnels - deploy-compose](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/agents-and-tools/mcp-tunnels/deploy-compose.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-compose)]

* `allowed_hosts` corrected: specifies bare hostnames or wildcard patterns (e.g., `*.example.com`) and explicitly states not to include a URL scheme (previously said "must be HTTPS-prefixed")
* `--token-version` argument persistence documented: persists in `docker-compose.yaml` for future re-runs
* Certificate renewal clarification: `renew-cert --output=dir:/data` replaces the `setup` service's `command` but keeps its `entrypoint`

#### [MCP tunnels - deploy-helm](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/agents-and-tools/mcp-tunnels/deploy-helm.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm)]

* `tunnel.tokenVersion` field added to sample `values.yaml` with initial value `"1"`, with note to increment for token rotation on upgrade
* Audience mismatch warning: chart default is `api.anthropic.com` (no scheme) but Console suggests `https://api.anthropic.com`; they must match byte-for-byte
* Verify step expanded with full URL pattern for testing

#### [MCP tunnels - overview](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/agents-and-tools/mcp-tunnels/overview.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview)]

* Messages API example replaced: Python SDK example replaced with a raw `curl` example; note added that `mcp-client-2025-11-20` beta header is separate from the `mcp-tunnels` beta
* URL structure clarified: path depends on the upstream server, not the tunnel (FastMCP uses `/mcp`, others use `/`)

#### [MCP tunnels - reference](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/agents-and-tools/mcp-tunnels/reference.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/reference)]

* New "Route matching" subsection: explains `routes` is a flat string map (not a list), lookup order (exact then subdomain-strip), and that each upstream must be `scheme://host:port` (port mandatory, path rejected)
* `--token-version` flag: notes the Helm chart and Compose example pass `1` as the initial value

#### [MCP tunnels - troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/agents-and-tools/mcp-tunnels/troubleshooting.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/troubleshooting)]

* `no route for host` fix now explicitly includes the restart command (`docker compose restart mcp-proxy`)
* Upstream IP validation clarified: only IPv4 is supported for the proxy-to-upstream hop; cloudflared-to-edge egress is a different hop

#### [Mid-conversation system messages](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/build-with-claude/mid-conversation-system-messages.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages)]

* Section renamed from "Why position matters for caching" to "When to use a mid-conversation system message"
* Two new use cases added: state changes the application observes (files, settings, tools, token budget) and user input that should not interrupt an agentic loop
* New "Placement after tool results" subsection with code example showing system message insertion after tool results in an agentic loop
* New warning: do not use mid-conversation system messages to pass tool output, retrieved documents, or third-party content
* "Not a security boundary" renamed to "Not a place for untrusted content" with explicit prohibition on raw tool output or web content

#### [Programmatic tool calling](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)]

* Performance numbers added: improved performance by an average of 11% while using 24% fewer input tokens; internal benchmarks show 38% fewer billed input tokens on a 75-tool project-management test
* `allowed_callers` explicitly documented as not a security boundary: Claude is "strongly guided" but client must still handle direct `tool_use` for any tool [[~line 80](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md?plain=1#L80)]
* Error mapping corrected: `tool_not_allowed` replaced with `invalid_request_error` for `tool_choice` naming a tool whose `allowed_callers` omits `"direct"`

#### [Tool reference](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/agents-and-tools/tool-use/tool-reference.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference)]

* `allowed_callers` description updated: "only callable from" changed to "guides Claude to call only from" — making the non-enforcement nature explicit

#### [Managed Agents - define-outcomes](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/managed-agents/define-outcomes.md) [[Source](https://platform.claude.com/docs/en/managed-agents/define-outcomes)]

* File upload for rubrics now requires both `managed-agents-2026-04-01` and `files-api-2025-04-14` beta headers
* Grader output now returns "an explanation summarizing which criteria passed or failed" (previously "a per-criterion breakdown")

#### [Managed Agents - environments](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/managed-agents/environments.md) [[Source](https://platform.claude.com/docs/en/managed-agents/environments)]

* `allowed_hosts` behavior corrected: specifies bare hostnames or wildcard patterns; do not include a URL scheme (previously incorrectly stated "must be HTTPS-prefixed")

#### [Managed Agents - events-and-streaming](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/managed-agents/events-and-streaming.md) [[Source](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)]

* Full event type catalog table removed; replaced with a pointer to `managed-agents/reference.md`

#### [Managed Agents - mcp-connector](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/managed-agents/mcp-connector.md) [[Source](https://platform.claude.com/docs/en/managed-agents/mcp-connector)]

* "Supported MCP server types" section removed; content moved to `managed-agents/reference.md`

#### [Managed Agents - overview](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/managed-agents/overview.md) [[Source](https://platform.claude.com/docs/en/managed-agents/overview)]

* "Rate limits" and "Branding guidelines" sections moved to `managed-agents/reference.md`

#### [Managed Agents - self-hosted-sandboxes](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/managed-agents/self-hosted-sandboxes.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

* New "Before you begin" section with explicit prerequisites: existing agent, Linux host requirements, credentials
* Environment key generation clarified: Console-only regardless of how the environment was created
* `/workspace` default corrected: CLI's `--workdir` defaults to current directory (not `/workspace`); must explicitly pass `--workdir /workspace` to match system default
* SDK helpers significantly expanded: new documentation for `EnvironmentWorker`, `work.poller()`, and `client.beta.sessions.events.tool_runner()` with parameters
* `AgentToolContext` and `beta_agent_toolset_20260401()` APIs documented for the first time
* New "Verify the worker is connected" section with `ant beta:environments:work stats` command
* File/GitHub mounting clarified: Anthropic does not mount files into self-hosted sandboxes; pass file references via session `metadata`

#### [Managed Agents - sessions](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/managed-agents/sessions.md) [[Source](https://platform.claude.com/docs/en/managed-agents/sessions)]

* Session statuses and all session lifecycle operations (update, retrieve, list, archive, delete) moved to new `managed-agents/session-operations.md` page

#### [Managed Agents - vaults](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/managed-agents/vaults.md) [[Source](https://platform.claude.com/docs/en/managed-agents/vaults)]

* `mcp_oauth_validate` endpoint now documented with full path: `POST /v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`
* Vaults access scope clarified: "anyone with an API key for the same workspace can reference them when creating a session"

#### [Structured outputs](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/build-with-claude/structured-outputs.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

* Claude Opus 4.8 removed from the generally-available list on Amazon Bedrock

#### [Workload identity federation](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/manage-claude/workload-identity-federation.md) [[Source](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation)]

* Token lifetime formula clarified: broken into explicit parts (a) and (b) with "The result is never less than 60 seconds"

#### [Workspaces](https://github.com/gpambrozio/ClaudeDocs/blob/bb3119d92df86a2957d3ab38b244111fa484a4e7/docs-md/api/manage-claude/workspaces.md) [[Source](https://platform.claude.com/docs/en/manage-claude/workspaces)]

* MCP tunnels description restructured: now leads with the authentication mechanism (org-scoped OAuth token with `org:manage_tunnels` via WIF)
