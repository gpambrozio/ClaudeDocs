# [Claude docs changes for February 28th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99)]

## Executive Summary
- **HTTP hooks**: New hook type that POSTs JSON to an HTTP endpoint, enabling server-based validation and authorization flows without shell commands
- **Sandbox filesystem controls**: New `sandbox.filesystem.allowWrite`, `denyWrite`, and `denyRead` settings give fine-grained OS-level path control for subprocess commands
- **Fast mode per-session opt-in**: New `fastModePerSessionOptIn` admin setting prevents fast mode from persisting across sessions, helping control costs in multi-session organizations
- **New Zero Data Retention guide for Claude Code**: Dedicated ZDR doc covers Enterprise-specific ZDR scope, disabled features, and how to request enablement
- **Session management for Claude Code on the web**: Users can now archive and permanently delete web sessions

## New Claude Code versions

### [2.1.63](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/versions/2.1.63.md)

#### New features

* Added `/simplify` and `/batch` bundled slash commands
* Added HTTP hooks: hooks can now POST JSON to a URL and receive JSON in response, instead of running a shell command
* Added `ENABLE_CLAUDEAI_MCP_SERVERS=false` environment variable to opt out of making claude.ai MCP servers available
* Added manual URL paste fallback during MCP OAuth authentication — if the automatic localhost redirect fails, users can paste the callback URL to complete authentication
* Added "Always copy full response" option to the `/copy` picker — when selected, future `/copy` commands skip the code block picker and copy the full response directly
* VSCode: Added session rename and remove actions to the sessions list

#### Existing feature improvements

* Project configs and auto memory are now shared across git worktrees of the same repository
* Improved `/model` command to show the currently active model in the slash command menu

#### Major bug fixes

* Fixed local slash command output (e.g. `/cost`) appearing as user-sent messages instead of system messages in the UI
* Fixed multiple memory and listener leaks: bridge polling loop, MCP OAuth flow cleanup, hooks configuration menu, interactive permission handler, bash command prefix cache, MCP tool/resource cache on server reconnect, IDE host IP detection cache, WebSocket transport reconnect, git root detection cache, JSON parsing cache, teammate AppState after conversation compaction, MCP server fetch caches on disconnect
* VSCode: Fixed remote sessions not appearing in conversation history
* Fixed a race condition in the REPL bridge where new messages could arrive interleaved with historical messages during initial connection flush, causing message ordering issues
* Fixed `/clear` not resetting cached skills, which could cause stale skill content to persist in the new conversation

-----

## Claude Code changes

### New Documents

#### [zero-data-retention](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/zero-data-retention.md) [[Source](https://code.claude.com/docs/en/zero-data-retention)]

New dedicated ZDR guide for Claude Code on Claude for Enterprise. Covers ZDR scope (what is and isn't covered), features disabled under ZDR (Claude Code on the Web, remote Desktop sessions, feedback submission), data retention for policy violations, and how to request ZDR enablement. Notes that ZDR is enabled per-organization and must be explicitly enabled for each new org.

### Changed documents

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* Added new "Managing sessions" section with instructions for archiving sessions (hidden from default list, filterable) and permanently deleting sessions (from sidebar or session menu, requires confirmation). [[lines 173-191](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L173-L191)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#managing-sessions)]

#### [data-usage](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/data-usage.md) [[Source](https://code.claude.com/docs/en/data-usage)]

* Updated ZDR description to clarify it is available for Claude Code on Claude for Enterprise and is enabled per-organization by the account team. [[line 33](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/data-usage.md?plain=1#L33)] [[Source](https://code.claude.com/docs/en/data-usage#data-retention)]
* Added note that individual Claude Code on the Web sessions can be deleted at any time, with a link to session management instructions. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/data-usage.md?plain=1#L36)] [[Source](https://code.claude.com/docs/en/data-usage#data-retention)]

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* Added new "Require per-session opt-in" section: administrators on Teams or Enterprise plans can set `fastModePerSessionOptIn: true` in managed settings to prevent fast mode from persisting across sessions. Each session starts with fast mode off and users must re-enable it with `/fast`. [[lines 93-112](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/fast-mode.md?plain=1#L93-L112)] [[Source](https://code.claude.com/docs/en/fast-mode#require-per-session-opt-in)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Updated hook type descriptions to include HTTP hooks as a fourth handler type alongside command, prompt, and agent hooks. [[line 270](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/hooks.md?plain=1#L270)] [[Source](https://code.claude.com/docs/en/hooks#hook-handler-fields)]
* Added full HTTP hook fields reference: `url` (required), `headers` (with env var interpolation via `$VAR_NAME`), and `allowedEnvVars` (required for env var interpolation). Includes a worked example sending `PreToolUse` events to a local validation service. [[lines 294-344](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/hooks.md?plain=1#L294-L344)] [[Source](https://code.claude.com/docs/en/hooks#command-hook-fields)]
* Added HTTP response handling section: 2xx with empty body = success, 2xx with JSON body = parsed as hook output, non-2xx or connection failure = non-blocking error. To block a tool call, HTTP hooks must return a 2xx response with a blocking decision in the JSON body. [[lines 552-564](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/hooks.md?plain=1#L552-L564)] [[Source](https://code.claude.com/docs/en/hooks#exit-code-2-behavior-per-event)]
* Clarified that HTTP hooks are deduplicated by URL (analogous to command hooks being deduplicated by command string). [[line 348](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/hooks.md?plain=1#L348)] [[Source](https://code.claude.com/docs/en/hooks#prompt-and-agent-hook-fields)]
* Updated security disclaimer to specify that the "full permissions" warning applies specifically to command hooks, not all hook types. [[lines 2033-2036](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/hooks.md?plain=1#L2033-L2036)] [[Source](https://code.claude.com/docs/en/hooks#security-considerations)]

#### [legal-and-compliance](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/legal-and-compliance.md) [[Source](https://code.claude.com/docs/en/legal-and-compliance)]

* Clarified that for BAA coverage, ZDR is enabled per-organization — each organization must have ZDR enabled separately to be covered under the BAA. [[line 18](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/legal-and-compliance.md?plain=1#L18)] [[Source](https://code.claude.com/docs/en/legal-and-compliance#healthcare-compliance-baa)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Added note that `sandbox.filesystem.allowWrite` can grant write access to additional paths beyond the working directory, enforced at the OS level (Seatbelt on macOS, bubblewrap on Linux), applying to all subprocess commands including `kubectl`, `terraform`, and `npm`. [[lines 33-35](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/sandboxing.md?plain=1#L33-L35)] [[Source](https://code.claude.com/docs/en/sandboxing#filesystem-isolation)]
* Added "Granting subprocess write access to specific paths" section with a configuration example and explanation of path prefix syntax (`//`, `~/`, `/`, `./`). Arrays from `allowWrite`/`denyWrite`/`denyRead` are merged across settings scopes. [[lines 113-149](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/sandboxing.md?plain=1#L113-L149)] [[Source](https://code.claude.com/docs/en/sandboxing#configure-sandboxing)]
* Updated permissions-vs-sandbox section to clarify that filesystem restrictions can now be configured via both `sandbox.filesystem` settings (OS-level, applies to all subprocesses) and permission rules (Claude's file tools), with paths from both merged together. [[lines 218-230](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/sandboxing.md?plain=1#L218-L230)] [[Source](https://code.claude.com/docs/en/sandboxing#how-sandboxing-relates-to-permissions)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `allowedHttpHookUrls` setting: allowlist of URL patterns (supports `*` wildcard) that HTTP hooks may target. Undefined = no restriction; empty array = block all HTTP hooks. Arrays merge across settings sources. [[line 150](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/settings.md?plain=1#L150)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* Added `httpHookAllowedEnvVars` setting: allowlist of environment variable names that HTTP hooks may interpolate into headers. Each hook's effective `allowedEnvVars` is the intersection with this list. [[line 151](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/settings.md?plain=1#L151)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* Added `fastModePerSessionOptIn` setting: when `true`, fast mode resets at the start of each session rather than persisting. [[line 181](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/settings.md?plain=1#L181)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* Added sandbox filesystem settings: `filesystem.allowWrite`, `filesystem.denyWrite`, and `filesystem.denyRead` with path prefix table and an example configuration. [[lines 220-228](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/settings.md?plain=1#L220-L228)] [[Source](https://code.claude.com/docs/en/settings#sandbox-settings)]
* Added documentation that array-valued settings (e.g. `sandbox.filesystem.allowWrite`, `permissions.allow`) are concatenated and deduplicated across scopes, not replaced. [[line 452](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/settings.md?plain=1#L452)] [[Source](https://code.claude.com/docs/en/settings#settings-precedence)]
* Expanded hook configuration section to document HTTP hook URL and env var allowlists (`allowedHttpHookUrls`, `httpHookAllowedEnvVars`) alongside the existing `allowManagedHooksOnly` setting. [[lines 395-430](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/claude-code/settings.md?plain=1#L395-L430)] [[Source](https://code.claude.com/docs/en/settings#hook-configuration)]

-----

## API changes

### Changed documents

#### [remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Added [Similarweb](https://docs.similarweb.com/api-v5/mcp/mcp-setup) MCP server (real-time web, mobile app, and market data) to the featured server list.
* Added [Airtable](https://support.airtable.com/docs/using-the-airtable-mcp-server) MCP server (structured data access at `https://mcp.airtable.com/mcp`) to the featured server list.

#### [zero-data-retention](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/api/build-with-claude/zero-data-retention.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/zero-data-retention)]

* Updated Claude Code ZDR eligibility: now covers two paths — pay-as-you-go API keys from a Commercial organization, and Claude Code on Claude for Enterprise with ZDR enabled on the organization. Previously, OAuth (Enterprise) was listed as not eligible. [[lines 16-25](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/api/build-with-claude/zero-data-retention.md?plain=1#L16-L25)] [[Source](https://platform.claude.com/docs/en/build-with-claude/zero-data-retention)]
* Clarified that ZDR for Claude for Enterprise product interfaces is now supported specifically for Claude Code, while other Enterprise interfaces still require Commercial API keys. [[line 22](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/api/build-with-claude/zero-data-retention.md?plain=1#L22)] [[Source](https://platform.claude.com/docs/en/build-with-claude/zero-data-retention)]
* Added per-organization ZDR enablement details and a link to the Claude Code ZDR documentation for full details on disabled features and enablement steps. [[lines 106-122](https://github.com/gpambrozio/ClaudeDocs/blob/1b1c9baf7556eb1e196dea8971cfd5c6569f3d99/docs-md/api/build-with-claude/zero-data-retention.md?plain=1#L106-L122)] [[Source](https://platform.claude.com/docs/en/build-with-claude/zero-data-retention)]
