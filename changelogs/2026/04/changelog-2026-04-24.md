# [Claude docs changes for April 24th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/edc8267) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/edc8267)]

## Executive Summary
- **Memory Stores API launched**: A new set of beta API endpoints for managing persistent memory stores, individual memories, and memory versions — enabling agents to maintain state across sessions
- **Sessions now support memory store resources**: Agent sessions can attach memory stores with read/write or read-only access, with per-attachment instructions rendered into the system prompt
- **Claude Code 2.1.119**: Major release with 30+ improvements including `/config` settings now persisting to disk, multi-git-host PR support, and PostToolUse hooks gaining execution timing data
- **New Claude Code Enterprise setup guide**: A comprehensive `admin-setup.md` document walks organization admins through API provider selection, policy delivery, enforcement controls, usage visibility, and data handling

## New Claude Code versions

### [2.1.119](https://github.com/gpambrozio/ClaudeDocs/blob/edc8267/versions/2.1.119.md)

#### New features

* `/config` settings (theme, editor mode, verbose, etc.) now persist to `~/.claude/settings.json` and participate in the project/local/policy override precedence chain
* Added `prUrlTemplate` setting to point the footer PR badge at a custom code-review URL instead of github.com
* Added `CLAUDE_CODE_HIDE_CWD` environment variable to hide the working directory in the startup logo
* `--from-pr` now accepts GitLab merge-request, Bitbucket pull-request, and GitHub Enterprise PR URLs
* `--print` mode now honors the agent's `tools:` and `disallowedTools:` frontmatter, matching interactive-mode behavior
* `--agent <name>` now honors the agent definition's `permissionMode` for built-in agents
* PowerShell tool commands can now be auto-approved in permission mode, matching Bash behavior
* Hooks: `PostToolUse` and `PostToolUseFailure` hook inputs now include `duration_ms` (tool execution time)
* `owner/repo#N` shorthand links in output now use your git remote's host instead of always pointing at github.com
* Status line stdin JSON now includes `effort.level` and `thinking.enabled`
* OpenTelemetry: `tool_result` and `tool_decision` events now include `tool_use_id`; `tool_result` also includes `tool_input_size_bytes`

#### Existing feature improvements

* Subagent and SDK MCP server reconfiguration now connects servers in parallel instead of serially
* Plugins pinned by another plugin's version constraint now auto-update to the highest satisfying git tag
* Vim mode: Esc in INSERT no longer pulls a queued message back into the input
* Slash command suggestions now highlight the characters that matched your query
* Slash command picker now wraps long descriptions onto a second line instead of truncating
* Security: `blockedMarketplaces` now correctly enforces `hostPattern` and `pathPattern` entries
* Tool search is now disabled by default on Vertex AI to avoid an unsupported beta header error (opt in with `ENABLE_TOOL_SEARCH`)

#### Major bug fixes

* Fixed pasting CRLF content (Windows clipboards, Xcode console) inserting an extra blank line between every line
* Fixed multi-line paste losing newlines in terminals using kitty keyboard protocol sequences inside bracketed paste
* Fixed Glob and Grep tools disappearing on native macOS/Linux builds when the Bash tool is denied via permissions
* Fixed scrolling up in fullscreen mode snapping back to the bottom every time a tool finishes
* Fixed MCP HTTP connections failing with "Invalid OAuth error response" when servers returned non-JSON bodies for OAuth discovery requests
* Fixed auto mode overriding plan mode with conflicting "Execute immediately" instructions
* Fixed async `PostToolUse` hooks that emit no response payload writing empty entries to the session transcript
* Fixed `${ENV_VAR}` placeholders in `headers` for HTTP/SSE/WebSocket MCP servers not being substituted before requests
* Fixed MCP OAuth client secret stored via `--client-secret` not being sent during token exchange for servers requiring `client_secret_post`
* Fixed verbose output setting not persisting after restart
* Fixed Agent tool with `isolation: "worktree"` reusing stale worktrees from prior sessions
* Fixed PR not linked to session when working in a git worktree
* Fixed `/plan` and `/plan open` not acting on the existing plan when entering plan mode
* Fixed skills invoked before auto-compaction being re-executed against the next user message
* Fixed `TaskList` returning tasks in arbitrary filesystem order instead of sorted by ID
* Fixed SDK/bridge `read_file` not correctly enforcing size cap on growing files
* Windows: removed false-positive "Windows requires 'cmd /c' wrapper" MCP config warning
* [VSCode] Fixed voice dictation's first recording producing nothing on macOS while the microphone permission prompt is showing

-----

## Claude Code changes

### New Documents

#### [admin-setup](https://github.com/gpambrozio/ClaudeDocs/blob/edc8267/docs-md/claude-code/admin-setup.md) [[Source](https://code.claude.com/docs/en/admin-setup)]

New comprehensive guide for deploying Claude Code across an organization. Covers API provider selection (Teams/Enterprise, Console, Bedrock, Vertex AI, Foundry), the four mechanisms for delivering managed policy to developer machines (server-managed, plist/registry, file-based, Windows user registry), enforcement controls (permission rules, sandboxing, MCP/plugin restrictions, hooks, version floor), usage visibility setup, and data handling review. Includes a verification step using `/status` to confirm active enterprise settings.

-----

## API changes

### New Documents

#### [Memory Stores](https://github.com/gpambrozio/ClaudeDocs/blob/edc8267/docs-md/api/api/beta/memory_stores.md) [[Source](https://platform.claude.com/docs/en/api/beta/memory_stores)]

New beta API section introducing Memory Stores — persistent, named stores of key-value memories that can be attached to agent sessions. Documents full CRUD endpoints for memory stores (`/v1/memory_stores`), individual memories within a store (`/v1/memory_stores/{id}/memories`), and memory versions (`/v1/memory_stores/{id}/memory_versions`). Memory versions support a `redact` operation. Available across all SDK languages (cURL, Python, TypeScript, Go, Java, Ruby, C#).

### Changed documents

#### [agent-skills/quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/edc8267/docs-md/api/agents-and-tools/agent-skills/quickstart.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart)]

* Simplified the file download API call: the explicit `betas=["files-api-2025-04-14"]` parameter was removed from `client.beta.files.download()`. [[line 102](https://github.com/gpambrozio/ClaudeDocs/blob/edc8267/docs-md/api/agents-and-tools/agent-skills/quickstart.md?plain=1#L102)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart)]

#### [api/beta](https://github.com/gpambrozio/ClaudeDocs/blob/edc8267/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* Removed the `user-profiles-2026-03-24` beta flag from the `AnthropicBeta` union type. [[line 62](https://github.com/gpambrozio/ClaudeDocs/blob/edc8267/docs-md/api/api/beta.md?plain=1#L62)] [[Source](https://platform.claude.com/docs/en/api/beta)]
* Removed the `xhigh` effort level from the `BetaEffortCapability` model, reducing it from 3 extra fields to 2. [[line 290](https://github.com/gpambrozio/ClaudeDocs/blob/edc8267/docs-md/api/api/beta.md?plain=1#L290)] [[Source](https://platform.claude.com/docs/en/api/beta)]

#### [api/beta/agents/create](https://github.com/gpambrozio/ClaudeDocs/blob/edc8267/docs-md/api/api/beta/agents/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/agents/create)]

* Removed the `user-profiles-2026-03-24` beta flag from the accepted `AnthropicBeta` values. [[line 68](https://github.com/gpambrozio/ClaudeDocs/blob/edc8267/docs-md/api/api/beta/agents/create.md?plain=1#L68)] [[Source](https://platform.claude.com/docs/en/api/beta/agents/create)]

#### [api/beta/messages/create](https://github.com/gpambrozio/ClaudeDocs/blob/edc8267/docs-md/api/api/beta/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]

* Removed the `user-profiles-2026-03-24` beta flag from accepted beta values. [[line 72](https://github.com/gpambrozio/ClaudeDocs/blob/edc8267/docs-md/api/api/beta/messages/create.md?plain=1#L72)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]
* Removed `xhigh` from the `effort` field in `output_config`; valid effort levels are now `low`, `medium`, `high`, and `max`. [[line 2849](https://github.com/gpambrozio/ClaudeDocs/blob/edc8267/docs-md/api/api/beta/messages/create.md?plain=1#L2849)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]
* Removed `task_budget` from `output_config`; the `BetaOutputConfig` object no longer accepts a token budget parameter. [[line 2833](https://github.com/gpambrozio/ClaudeDocs/blob/edc8267/docs-md/api/api/beta/messages/create.md?plain=1#L2833)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]
* Removed `encrypted_content` from `BetaCompactionBlock` and `BetaCompactionBlockParam`; the opaque round-trip metadata field is no longer part of the compaction API. [[line 2497](https://github.com/gpambrozio/ClaudeDocs/blob/edc8267/docs-md/api/api/beta/messages/create.md?plain=1#L2497)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]
* Removed `user_profile_id` request parameter. [[line 4757](https://github.com/gpambrozio/ClaudeDocs/blob/edc8267/docs-md/api/api/beta/messages/create.md?plain=1#L4757)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]

#### [api/beta/sessions](https://github.com/gpambrozio/ClaudeDocs/blob/edc8267/docs-md/api/api/beta/sessions.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions)]

* Added `BetaManagedAgentsMemoryStoreResourceParam` as a new resource type for session creation, allowing memory stores to be attached with `read_write` or `read_only` access and optional per-attachment instructions. [[line 136](https://github.com/gpambrozio/ClaudeDocs/blob/edc8267/docs-md/api/api/beta/sessions.md?plain=1#L136)] [[Source](https://platform.claude.com/docs/en/api/beta/sessions)]
* `BetaManagedAgentsSessionResource` union type now includes `BetaManagedAgentsMemoryStoreResource` alongside GitHub repository and file resources. [[line 6206](https://github.com/gpambrozio/ClaudeDocs/blob/edc8267/docs-md/api/api/beta/sessions.md?plain=1#L6206)] [[Source](https://platform.claude.com/docs/en/api/beta/sessions)]

#### [api/beta/sessions/create](https://github.com/gpambrozio/ClaudeDocs/blob/edc8267/docs-md/api/api/beta/sessions/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions/create)]

* `resources` parameter now accepts `BetaManagedAgentsMemoryStoreResourceParam` in addition to GitHub repository and file resources. Includes `memory_store_id`, `access` (read_write/read_only), and optional `instructions` fields. [[line 102](https://github.com/gpambrozio/ClaudeDocs/blob/edc8267/docs-md/api/api/beta/sessions/create.md?plain=1#L102)] [[Source](https://platform.claude.com/docs/en/api/beta/sessions/create)]
* New `BetaManagedAgentsMemoryStoreResource` response model documented, including `mount_path` (filesystem path derived from store name), `description`, `name`, and `instructions` fields. [[line 544](https://github.com/gpambrozio/ClaudeDocs/blob/edc8267/docs-md/api/api/beta/sessions/create.md?plain=1#L544)] [[Source](https://platform.claude.com/docs/en/api/beta/sessions/create)]

#### [api/beta/sessions/resources](https://github.com/gpambrozio/ClaudeDocs/blob/edc8267/docs-md/api/api/beta/sessions/resources.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions/resources)]

* `BetaManagedAgentsSessionResource` union type now includes `BetaManagedAgentsMemoryStoreResource` as a third variant alongside GitHub repository and file resources. [[line 92](https://github.com/gpambrozio/ClaudeDocs/blob/edc8267/docs-md/api/api/beta/sessions/resources.md?plain=1#L92)] [[Source](https://platform.claude.com/docs/en/api/beta/sessions/resources)]
