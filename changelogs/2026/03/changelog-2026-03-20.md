# [Claude docs changes for March 20th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/2ae325d5989f8f6d725f8af582c00427b8786256) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/2ae325d5989f8f6d725f8af582c00427b8786256)]

## Executive Summary
- **Channels (research preview)**: Claude Code v2.1.80 introduces a new `--channels` flag that lets MCP servers push events into a running session, enabling Telegram/Discord chat bridges and webhook-driven automation
- **Effort level for skills & subagents**: Skills and subagents can now override the session effort level via `effort` frontmatter, enabling fine-grained control over model reasoning depth per task
- **Plugin marketplace via settings**: Plugins can now be declared inline in `settings.json` using `source: 'settings'`, without needing a separate marketplace
- **Prompt caching documentation overhauled**: The explanation of how cache breakpoints, writes, and the 20-block lookback window work has been rewritten for clarity, with a new "common mistake" example
- **Go SDK updated to v1.27.1**: Now requires Go 1.23+, and adds a new `param.SetJSON` API for round-trip deserialization of param types

## New Claude Code versions

### [2.1.80](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/versions/2.1.80.md)

#### New features

* Added `--channels` (research preview) — allow MCP servers to push messages into your session from Telegram, Discord, webhooks, or custom sources
* Added `rate_limits` field to statusline scripts for displaying Claude.ai rate limit usage (5-hour and 7-day windows with `used_percentage` and `resets_at`)
* Added `source: 'settings'` plugin marketplace source — declare plugin entries inline in settings.json
* Added CLI tool usage detection to plugin tips, in addition to file pattern matching
* Added `effort` frontmatter support for skills and slash commands to override the model effort level when invoked

#### Existing feature improvements

* Improved responsiveness of `@` file autocomplete in large git repositories
* Improved `/effort` to show what auto currently resolves to, matching the status bar indicator
* Improved `/permissions` — Tab and arrow keys now switch tabs from within a list
* Improved background tasks panel — left arrow now closes from the list view
* Simplified plugin install tips to use a single `/plugin install` command instead of a two-step flow
* Reduced memory usage on startup in large repositories (~80 MB saved on 250k-file repos)

#### Major bug fixes

* Fixed `--resume` dropping parallel tool results — sessions with parallel tool calls now restore all tool_use/tool_result pairs instead of showing `[Tool result missing]` placeholders
* Fixed voice mode WebSocket failures caused by Cloudflare bot detection on non-browser TLS fingerprints
* Fixed 400 errors when using fine-grained tool streaming through API proxies, Bedrock, or Vertex
* Fixed `/remote-control` appearing for gateway and third-party provider deployments where it cannot function
* Fixed managed settings (`enabledPlugins`, `permissions.defaultMode`, policy-set env vars) not being applied at startup when `remote-settings.json` was cached from a prior session

-----

## Claude Code changes

### New Documents

#### [Channels](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/channels.md) [[Source](https://code.claude.com/docs/en/channels)]

New file documenting the Channels research preview feature (requires v2.1.80+). Channels are MCP servers that push events into a running Claude Code session, enabling Claude to react to external events while you're away from the terminal. Covers setup for Telegram and Discord bots (including pairing/allowlist security), a localhost demo via fakechat, enterprise controls (`channelsEnabled` managed setting), and the `--channels` CLI flag.

#### [Channels reference](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/channels-reference.md) [[Source](https://code.claude.com/docs/en/channels-reference)]

New developer reference for building custom channel servers. Explains the MCP `claude/channel` capability, notification format (`notifications/claude/channel`), a full walkthrough for building a webhook receiver, how to add a two-way reply tool, sender allowlist gating to prevent prompt injection, the `--dangerously-load-development-channels` flag for local testing, and how to package channels as plugins.

### Changed documents

#### [CLI reference](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Added `--channels` flag for enabling named channel servers to push messages into a session. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/cli-reference.md?plain=1#L36)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]
* Added `--dangerously-load-development-channels` flag for testing custom channels not on the approved allowlist. [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/cli-reference.md?plain=1#L38)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Added `resume` as a new `SessionEnd` matcher value, triggered when a session is switched via interactive `/resume`. [[line 187](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/hooks.md?plain=1#L187)] [[Source](https://code.claude.com/docs/en/hooks#matcher-patterns)]
* Clarified that the SessionEnd hook timeout applies to session switching via `/resume` in addition to exit and `/clear`. [[line 1916](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/hooks.md?plain=1#L1916)] [[Source](https://code.claude.com/docs/en/hooks#sessionend-input)]

#### [Index](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/index.md) [[Source](https://code.claude.com/docs/en/index)]

* Added Channels to the "I want to…" quick reference table. [[line 211](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/index.md?plain=1#L211)] [[Source](https://code.claude.com/docs/en/index#use-claude-code-everywhere)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Added a note that MCP servers can act as Channels to push events into a session. [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/mcp.md?plain=1#L14)] [[Source](https://code.claude.com/docs/en/mcp#what-you-can-do-with-mcp)]
* Added Miro to the popular MCP servers list. [[line 91](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/mcp.md?plain=1#L91)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* Reordered several MCP server entries (Miro moved up, PubMed/Supabase swapped, Ahrefs/NetSuite swapped, ZoomInfo/Scholar Gateway positions changed).

#### [Model config](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Added that skill and subagent frontmatter can now override effort level via the `effort` field. [[line 155](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/model-config.md?plain=1#L155)] [[Source](https://code.claude.com/docs/en/model-config#adjust-effort-level)]
* Clarified the effort level precedence order: env var > configured level > model default, with frontmatter overriding session level but not env var. [[line 157](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/model-config.md?plain=1#L157)] [[Source](https://code.claude.com/docs/en/model-config#adjust-effort-level)]

#### [Overview](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/overview.md) [[Source](https://code.claude.com/docs/en/overview)]

* Added Channels to the "I want to…" quick reference table. [[line 211](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/overview.md?plain=1#L211)] [[Source](https://code.claude.com/docs/en/overview#use-claude-code-everywhere)]

#### [Remote control](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Added Channels as a related resource in the "Related resources" section. [[line 189](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/remote-control.md?plain=1#L189)] [[Source](https://code.claude.com/docs/en/remote-control#related-resources)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `channelsEnabled` managed setting that controls whether Team/Enterprise users can receive channel messages. [[line 174](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/settings.md?plain=1#L174)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

#### [Statusline](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/statusline.md) [[Source](https://code.claude.com/docs/en/statusline)]

* Added a "Workspace trust required" troubleshooting section: the status line command only runs after accepting the workspace trust dialog, and shows `statusline skipped · restart to fix` if trust isn't accepted. [[line 655](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/statusline.md?plain=1#L655)] [[Source](https://code.claude.com/docs/en/statusline#troubleshooting)]

#### [Sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Added `effort` as a supported frontmatter field for subagents, overriding the session effort level when that subagent is active. [[line 253](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/sub-agents.md?plain=1#L253)] [[Source](https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields)]
* Updated `--agents` flag documentation to include `effort`, `background`, and `isolation` as supported JSON fields. [[line 204](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/sub-agents.md?plain=1#L204)] [[Source](https://code.claude.com/docs/en/sub-agents#choose-the-subagent-scope)]
* Memory scope option label changed from "Enable" to "User scope" in the configure memory UI step. [[line 130](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/claude-code/sub-agents.md?plain=1#L130)] [[Source](https://code.claude.com/docs/en/sub-agents#quickstart-create-your-first-subagent)]

-----

## API changes

### Changed documents

#### [Extended thinking](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Minor wording improvements throughout (no new information added — phrasing polished for clarity).

#### [Fast mode](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/api/build-with-claude/fast-mode.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]

* Availability classification updated from "research preview" to "beta: research preview" in title and description. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/api/build-with-claude/fast-mode.md?plain=1#L1)] [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]

#### [Overview (Build with Claude)](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/api/build-with-claude/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

* Added a new "Feature availability" section defining the classification stages: Beta, Generally available (GA), Deprecated, and Retired — with a note that beta features use a beta header. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/api/build-with-claude/overview.md?plain=1#L15)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

#### [Prompt caching](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* Rewrote the "How automatic prefix checking works" section with three clearer principles: cache writes happen only at the breakpoint; cache reads look backward for prior writes; the lookback window is 20 blocks. [[line 208](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L208)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]
* Replaced the abstract lookback example with a concrete "growing conversation" example (Turn 1 → Turn 2 → Turn 3) showing exactly how cache entries accumulate. [[line 219](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L219)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]
* Added a new "Common mistake" section explaining why placing `cache_control` on a block that changes every request (e.g. timestamps) results in zero cache hits. [[line 225](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L225)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]
* Updated the key takeaway and "When to use multiple breakpoints" section to reflect the corrected mental model. [[line 232](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L232)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]
* Updated troubleshooting tip to explain that the lookback only finds prior writes, not stable content. [[line 432](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L432)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

#### [Remote MCP servers](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Reordered several MCP server entries in the directory listing (Miro/Granola, PubMed/Supabase, ClickUp/Indeed positions swapped, and others).

#### [Go SDK](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/api/api/sdks/go.md) [[Source](https://platform.claude.com/docs/en/api/sdks/go)]

* Updated pinned version from v1.19.0 to v1.27.1. [[line 20](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/api/api/sdks/go.md?plain=1#L20)] [[Source](https://platform.claude.com/docs/en/api/sdks/go)]
* Updated minimum Go version requirement from 1.22 to 1.23. [[line 24](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/api/api/sdks/go.md?plain=1#L24)] [[Source](https://platform.claude.com/docs/en/api/sdks/go)]
* Added a new "Deserializing params" section explaining how to use `param.SetJSON` (available since v1.20.0) for round-trip deserialization of param types, with a full code example. [[line 156](https://github.com/gpambrozio/ClaudeDocs/blob/2ae325d5989f8f6d725f8af582c00427b8786256/docs-md/api/api/sdks/go.md?plain=1#L156)] [[Source](https://platform.claude.com/docs/en/api/sdks/go)]
