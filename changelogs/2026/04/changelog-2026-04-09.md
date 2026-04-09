# [Claude docs changes for April 9th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/5ca75828d63fd74fe093472cc0909906edccb2fa) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/5ca75828d63fd74fe093472cc0909906edccb2fa)]

## Executive Summary
- New **claude-mythos-preview** model added to the API: "New class of intelligence, strongest in coding and cybersecurity"
- New **Managed Agents API** (beta): full CRUD API for Agents, Sessions, Environments, and Vaults — enabling stateful, long-running agent sessions in cloud containers
- New **`ant` CLI** added as a first-class SDK: terminal client for the Claude API with typed flags, response transforms, pagination, and native Claude Code integration
- **Managed Agents pricing** documented: $0.08/session-hour for runtime, plus standard token pricing (replaces Code Execution container-hour billing)
- Claude Code 2.1.97 brings many fixes and improvements including a focus view toggle, status line refresh interval, live subagent indicators, and dozens of bug fixes

## New Claude Code versions

### [2.1.97](https://github.com/gpambrozio/ClaudeDocs/blob/5ca75828d63fd74fe093472cc0909906edccb2fa/versions/2.1.97.md)

#### New features

* Added focus view toggle (`Ctrl+O`) in `NO_FLICKER` mode showing prompt, one-line tool summary with edit diffstats, and final response
* Added `refreshInterval` status line setting to re-run the status line command every N seconds
* Added `workspace.git_worktree` to the status line JSON input, set when the current directory is inside a linked git worktree
* Added `● N running` indicator in `/agents` next to agent types with live subagent instances
* Added syntax highlighting for Cedar policy files (`.cedar`, `.cedarpolicy`)

#### Existing feature improvements

* Improved Accept Edits mode to auto-approve filesystem commands prefixed with safe env vars or process wrappers (e.g. `LANG=C rm foo`, `timeout 5 mkdir out`)
* Improved auto mode and bypass-permissions mode to auto-approve sandbox network access prompts
* Improved sandbox: `sandbox.network.allowMachLookup` now takes effect on macOS
* Improved image handling: pasted and attached images are now compressed to the same token budget as images read via the Read tool
* Improved slash command and `@`-mention completion to trigger after CJK sentence punctuation
* Improved Bridge sessions to show the local git repo, branch, and working directory on the claude.ai session card
* Improved footer layout: indicators (Focus, notifications) now stay on the mode-indicator row instead of wrapping below
* Improved context-low warning to show as a transient footer notification instead of a persistent row
* Improved markdown blockquotes to show a continuous left bar across wrapped lines
* Improved session transcript size by skipping empty hook entries and capping stored pre-edit file copies
* Improved transcript accuracy: per-block entries now carry the final token usage instead of the streaming placeholder
* Improved Bash tool OTEL tracing: subprocesses now inherit a W3C `TRACEPARENT` env var when tracing is enabled
* Updated `/claude-api` skill to cover Managed Agents alongside the Claude API

#### Major bug fixes

* Fixed `--dangerously-skip-permissions` being silently downgraded to accept-edits mode after approving a write to a protected path
* Fixed Bash tool permissions, tightening checks around env-var prefixes and network redirects, and reducing false prompts
* Fixed permission rules with names matching JavaScript prototype properties (e.g. `toString`) causing `settings.json` to be silently ignored
* Fixed managed-settings allow rules remaining active after an admin removed them until process restart
* Fixed `permissions.additionalDirectories` changes in settings not applying mid-session
* Fixed MCP HTTP/SSE connections accumulating ~50 MB/hr of unreleased buffers when servers reconnect
* Fixed MCP OAuth `oauth.authServerMetadataUrl` not being honored on token refresh after restart, fixing ADFS and similar IdPs
* Fixed 429 retries burning all attempts in ~13 seconds — exponential backoff now applies as a minimum
* Fixed rate-limit upgrade options disappearing after context compaction
* Fixed several `/resume` picker issues (uneditable sessions, search wipe on reload, empty list navigation, and more)
* Fixed file-edit diffs disappearing on `--resume` when the edited file was larger than 10KB
* Fixed messages typed while Claude is working not being persisted to the transcript
* Fixed `Stop`/`SubagentStop` hooks failing on long sessions
* Fixed subagents with worktree isolation leaking their working directory back to the parent session's Bash tool
* Fixed compaction writing duplicate multi-MB subagent transcript files on prompt-too-long retries
* Fixed `claude plugin update` incorrectly reporting "already at the latest version" for git-based marketplace plugins
* Fixed slash command picker breaking when a plugin's `name` is a YAML boolean keyword
* Fixed Korean/Japanese/Unicode text becoming garbled when copied in no-flicker mode on Windows
* Fixed Bedrock SigV4 authentication failing when `AWS_BEARER_TOKEN_BEDROCK` or `ANTHROPIC_BEDROCK_BASE_URL` are set to empty strings
* Fixed several `NO_FLICKER` mode issues: scroll artifacts, crash on MCP hover, memory leak on retries, slow mouse-wheel scrolling on Windows Terminal, missing custom status line on short terminals, Shift+Enter/Alt+Cmd+arrow shortcuts in Warp

-----

## Claude Code changes

No new or changed Claude Code documentation files.

-----

## API changes

### New Documents

#### [API/beta/agents](https://github.com/gpambrozio/ClaudeDocs/blob/5ca75828d63fd74fe093472cc0909906edccb2fa/docs-md/api/api/beta/agents.md) [[Source](https://platform.claude.com/docs/en/api/beta/agents)]

New Managed Agents API reference covering full CRUD operations for `Agent` resources: Create, List, Get, Update, Archive, and List Versions. Agents define the model, system prompt, tools (built-in toolsets, MCP toolsets, custom tools), skills, and MCP server connections used by sessions.

#### [API/beta/environments](https://github.com/gpambrozio/ClaudeDocs/blob/5ca75828d63fd74fe093472cc0909906edccb2fa/docs-md/api/api/beta/environments.md) [[Source](https://platform.claude.com/docs/en/api/beta/environments)]

New Environments API reference for creating and managing cloud execution environments for agent sessions. Environments configure networking (unrestricted or limited with allowed hosts, MCP servers, and package managers) and pre-installed packages (apt, pip, npm, go, cargo, gem).

#### [API/beta/sessions](https://github.com/gpambrozio/ClaudeDocs/blob/5ca75828d63fd74fe093472cc0909906edccb2fa/docs-md/api/api/beta/sessions.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions)]

New Sessions API reference for stateful agent sessions running in cloud containers. Covers Create, List, Get, Update, Delete, and Archive operations, plus sub-resources: Events (list, send, stream), Resources (file and GitHub repository mounts).

#### [API/beta/vaults](https://github.com/gpambrozio/ClaudeDocs/blob/5ca75828d63fd74fe093472cc0909906edccb2fa/docs-md/api/api/beta/vaults.md) [[Source](https://platform.claude.com/docs/en/api/beta/vaults)]

New Vaults API reference for securely storing credentials used by agents during sessions. Vaults hold credentials with MCP OAuth (including refresh token support) or static bearer token authentication types. Sub-resource: Credentials (Create, List, Get, Update, Delete, Archive).

#### [API/sdks/cli](https://github.com/gpambrozio/ClaudeDocs/blob/5ca75828d63fd74fe093472cc0909906edccb2fa/docs-md/api/api/sdks/cli.md) [[Source](https://platform.claude.com/docs/en/api/sdks/cli)]

New documentation for the `ant` CLI — a terminal client for the Claude API. Covers installation (Homebrew, curl, Go), authentication, command structure (`resource action` pattern with `beta:` prefix for beta resources), output formats (JSON, YAML, JSONL, interactive explorer TUI), GJSON transforms, request body input (flags, stdin, `@file` references), version-controlling API resources, scripting patterns, and shell completion. Claude Code understands how to use `ant` natively.

### Changed documents

#### [about-claude/models/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/5ca75828d63fd74fe093472cc0909906edccb2fa/docs-md/api/about-claude/models/migration-guide.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]

* Added note that the guide covers the Messages API and points Managed Agents users to a separate migration guide. [[line 4](https://github.com/gpambrozio/ClaudeDocs/blob/5ca75828d63fd74fe093472cc0909906edccb2fa/docs-md/api/about-claude/models/migration-guide.md?plain=1#L4)] [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]

#### [about-claude/models/whats-new-claude-4-6](https://github.com/gpambrozio/ClaudeDocs/blob/5ca75828d63fd74fe093472cc0909906edccb2fa/docs-md/api/about-claude/models/whats-new-claude-4-6.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6)]

* Added language labels (Python, Shell) to code blocks for clarity.

#### [about-claude/pricing](https://github.com/gpambrozio/ClaudeDocs/blob/5ca75828d63fd74fe093472cc0909906edccb2fa/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* Replaced "Agent use case pricing examples" section with "Claude Managed Agents pricing" section. Documents two billing dimensions: tokens (at standard rates; batch API, fast mode, data residency, long context, and third-party platform modifiers do not apply) and session runtime ($0.08/session-hour while session is in `running` status). Includes a worked example for a one-hour coding session. [[line 282+](https://github.com/gpambrozio/ClaudeDocs/blob/5ca75828d63fd74fe093472cc0909906edccb2fa/docs-md/api/about-claude/pricing.md?plain=1#L282)]

#### [agents-and-tools/agent-skills/best-practices](https://github.com/gpambrozio/ClaudeDocs/blob/5ca75828d63fd74fe093472cc0909906edccb2fa/docs-md/api/agents-and-tools/agent-skills/best-practices.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)]

* Removed links to Agent SDK skills documentation from navigation footer.

#### [agents-and-tools/agent-skills/enterprise](https://github.com/gpambrozio/ClaudeDocs/blob/5ca75828d63fd74fe093472cc0909906edccb2fa/docs-md/api/agents-and-tools/agent-skills/enterprise.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise)]

* Removed link to Agent SDK secure deployment documentation from navigation footer.

#### [agents-and-tools/agent-skills/overview](https://github.com/gpambrozio/ClaudeDocs/blob/5ca75828d63fd74fe093472cc0909906edccb2fa/docs-md/api/agents-and-tools/agent-skills/overview.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)]

* Removed "Claude Agent SDK" section describing how Skills work in the Agent SDK. Navigation footer link to Agent SDK skills also removed.

#### [agents-and-tools/agent-skills/quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/5ca75828d63fd74fe093472cc0909906edccb2fa/docs-md/api/agents-and-tools/agent-skills/quickstart.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart)]

* Updated code examples from Python SDK to CLI (`ant`) for listing skills and creating messages with skills.

#### [agents-and-tools/mcp-connector](https://github.com/gpambrozio/ClaudeDocs/blob/5ca75828d63fd74fe093472cc0909906edccb2fa/docs-md/api/agents-and-tools/mcp-connector.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)]

* Removed mention of Agent SDK from guidance on when to use client-side MCP helpers vs. the `mcp_servers` API parameter.

#### [api/beta](https://github.com/gpambrozio/ClaudeDocs/blob/5ca75828d63fd74fe093472cc0909906edccb2fa/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* Added new model `claude-mythos-preview` to the model enum, described as "New class of intelligence, strongest in coding and cybersecurity". [[line 7155+](https://github.com/gpambrozio/ClaudeDocs/blob/5ca75828d63fd74fe093472cc0909906edccb2fa/docs-md/api/api/beta.md?plain=1#L7155)]
* Removed `user-profiles-2026-03-24` beta header from the list of available beta features.

#### [api/beta-headers](https://github.com/gpambrozio/ClaudeDocs/blob/5ca75828d63fd74fe093472cc0909906edccb2fa/docs-md/api/api/beta-headers.md) [[Source](https://platform.claude.com/docs/en/api/beta-headers)]

* Added "Endpoint-specific headers" section documenting the `managed-agents-2026-04-01` beta header required for all Managed Agents endpoints (`/v1/agents`, `/v1/sessions`, `/v1/environments`). [[line 53+](https://github.com/gpambrozio/ClaudeDocs/blob/5ca75828d63fd74fe093472cc0909906edccb2fa/docs-md/api/api/beta-headers.md?plain=1#L53)]
* Updated the code example in the quick-start from Python to cURL.

#### [api/client-sdks](https://github.com/gpambrozio/ClaudeDocs/blob/5ca75828d63fd74fe093472cc0909906edccb2fa/docs-md/api/api/client-sdks.md) [[Source](https://platform.claude.com/docs/en/api/client-sdks)]

* Added the `ant` CLI as the first SDK listed, with the description "Shell scripting, typed flags, response transforms". Updated quick installation and quick start examples to use CLI instead of Python.

#### [api/errors](https://github.com/gpambrozio/ClaudeDocs/blob/5ca75828d63fd74fe093472cc0909906edccb2fa/docs-md/api/api/errors.md) [[Source](https://platform.claude.com/docs/en/api/errors)]

* Updated request-ID example from Python SDK to the `ant` CLI (`ant --debug`).
