# [Claude docs changes for February 24th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/aa8b0a3) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/aa8b0a3)]

## Executive Summary
- Claude Code 2.1.51 adds a new `claude remote-control` subcommand for external builds, BashTool performance improvements, and a security fix for hooks executing without workspace trust
- The prompt engineering best practices guide was significantly overhauled and consolidated into a single comprehensive reference, replacing individual topic pages
- New extensive guidance on multi-session software development patterns using memory files, git checkpointing, and context recovery for long-running agent workflows
- Introduced the concept of "context rot" — how accuracy degrades as context grows — with new recommendations on context curation for agentic systems
- New C# SDK endpoint for the Files API: Upload File (beta)

## New Claude Code versions

### [2.1.51](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/versions/2.1.51.md)

#### New features

* Added `claude remote-control` subcommand for external builds, enabling local environment serving for all users
* Added support for custom npm registries and specific version pinning when installing plugins from npm sources
* Added `CLAUDE_CODE_ACCOUNT_UUID`, `CLAUDE_CODE_USER_EMAIL`, and `CLAUDE_CODE_ORGANIZATION_UUID` environment variables for SDK callers to provide account info synchronously, eliminating a race condition where early telemetry events lacked account metadata

#### Existing feature improvements

* Updated plugin marketplace default git timeout from 30s to 120s; added `CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS` to configure it
* BashTool now skips login shell (`-l` flag) by default when a shell snapshot is available, improving command execution performance (previously required setting `CLAUDE_BASH_NO_LOGIN=true`)
* Tool results larger than 50K characters are now persisted to disk (previously 100K threshold), reducing context window usage and improving conversation longevity
* The `/model` picker now shows human-readable labels (e.g., "Sonnet 4.5") instead of raw model IDs for pinned model versions, with an upgrade hint when a newer version is available

#### Major bug fixes

* Fixed a security issue where `statusLine` and `fileSuggestion` hook commands could execute without workspace trust acceptance in interactive mode
* Fixed a bug where duplicate `control_response` messages (e.g. from WebSocket reconnects) could cause API 400 errors by pushing duplicate assistant messages into the conversation
* Fixed slash command autocomplete crashing when a plugin's SKILL.md description is a YAML array or other non-string type

### [2.1.52](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/versions/2.1.52.md)

#### Major bug fixes

* VS Code: Fixed extension crash on Windows ("command 'claude-vscode.editor.openLast' not found")

-----

## Claude Code changes

### Changed documents

#### [Agent teams](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

* Added new section on choosing an appropriate team size: recommends starting with 3–5 teammates, explains that token costs scale linearly per teammate, and that coordination overhead increases with more agents. [[line 337](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/claude-code/agent-teams.md?plain=1#L337)] [[Source](https://code.claude.com/docs/en/agent-teams#choose-an-appropriate-team-size)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Added **GraphOS MCP Tools** (Apollo GraphQL) — search Apollo docs, specs, and best practices. [[line 672](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/claude-code/mcp.md?plain=1#L672)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* Various reordering of remote MCP server entries in the marketplace list

#### [Terminal config](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* Updated notification setup documentation: Kitty and Ghostty now noted as supporting desktop notifications without additional configuration; simplified iTerm 2 setup steps; clarified that other terminals (including macOS Terminal) do not support native notifications and should use notification hooks instead. [[line 32](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/claude-code/terminal-config.md?plain=1#L32)] [[Source](https://code.claude.com/docs/en/terminal-config#notification-setup)]

-----

## API changes

### New Documents

#### [Prompting tools](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/build-with-claude/prompt-engineering/prompting-tools.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-tools)]

New guide to Claude Console prompting tools. Documents the **prompt generator** (for creating first-draft prompts), **prompt templates and variables** (using `{{double brackets}}` for dynamic content), and the **prompt improver** (which enhances prompts through 4 automated steps: example identification, initial draft, chain-of-thought refinement, and example enhancement).

#### [Upload File (C# beta)](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/api/csharp/beta/files/upload.md) [[Source](https://platform.claude.com/docs/en/api/csharp/beta/files/upload)]

New C# SDK reference for the `Beta.Files.Upload` method (`POST /v1/files`). Documents the `FileUploadParams` input, all supported beta headers, and the `FileMetadata` return type (ID, created timestamp, filename, MIME type, size, and downloadable flag).

### Changed documents

#### [Customer support chat](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/about-claude/use-case-guides/customer-support-chat.md) [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/customer-support-chat)]

* Internal links updated from individual prompt engineering topic pages to the consolidated `claude-prompting-best-practices.md` reference

#### [Remote MCP servers](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Added **Pendo** — connect to Pendo for product and user insights (user-specific URL). [[line 425](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L425)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
* Added **Open Targets** — drug target discovery and prioritisation platform (`https://mcp.platform.opentargets.org/mcp`). [[line 436](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L436)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
* Added **Honeycomb** and **Consensus** to the API-level remote MCP list (previously only in the Claude Code MCP page)
* Various reordering of MCP server entries throughout the list

#### [Bash tool](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/agents-and-tools/tool-use/bash-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool)]

* Added Terminal-Bench 2.0 benchmark results note highlighting performance gains with a persistent bash session. [[line 4](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/agents-and-tools/tool-use/bash-tool.md?plain=1#L4)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool)]
* Added new **Git-based checkpointing** section with a 4-step pattern for using git as a structured recovery mechanism in long-running agent workflows (baseline commit, per-feature commits, state reconstruction, revert-on-failure). [[line 239](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/agents-and-tools/tool-use/bash-tool.md?plain=1#L239)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool)]

#### [Computer use tool](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]

* Added WebArena benchmark results note (state-of-the-art among single-agent systems for autonomous web navigation). [[line 4](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md?plain=1#L4)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]
* Added guidance for multi-session agents: run end-to-end verification at the start of each session (not only after implementation), with a link to the "Effective harnesses for long-running agents" engineering article. [[line 278](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md?plain=1#L278)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]

#### [Implement tool use](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/agents-and-tools/tool-use/implement-tool-use.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use)]

* Added three new tool design best practices: consolidate related operations into fewer tools (use an `action` parameter instead of separate tools), use meaningful namespacing in tool names (prefix by service), and design tool responses to return only high-signal information (semantic identifiers, minimal fields). [[line 50](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/agents-and-tools/tool-use/implement-tool-use.md?plain=1#L50)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use)]
* Added reference to the "Writing tools for agents" engineering article. [[line 58](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/agents-and-tools/tool-use/implement-tool-use.md?plain=1#L58)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use)]

#### [Memory tool](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/agents-and-tools/tool-use/memory-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)]

* Added explanation of the just-in-time context retrieval principle: store what agents learn in memory and pull it back on demand rather than loading everything upfront. [[line 6](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/agents-and-tools/tool-use/memory-tool.md?plain=1#L6)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)]
* Added new **Multi-session software development pattern** section: describes a 3-phase workflow (initializer session, subsequent sessions, end-of-session update) using memory files as a structured recovery mechanism, with the principle of completing one feature at a time and verifying end-to-end before marking complete. [[line 451](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/agents-and-tools/tool-use/memory-tool.md?plain=1#L451)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)]

#### [Tool use overview](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/agents-and-tools/tool-use/overview.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)]

* Added benchmark results illustrating the impact of tool access (LAB-Bench FigQA and SWE-bench). [[line 4](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/agents-and-tools/tool-use/overview.md?plain=1#L4)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)]
* Added link to "Advanced tool use" article as a next step for workflows with many tools. [[line 249](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/agents-and-tools/tool-use/overview.md?plain=1#L249)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)]

#### [Programmatic tool calling](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)]

* Added BrowseComp and DeepSearchQA benchmark results showing programmatic tool calling as the key factor unlocking agent performance on multi-step research tasks. [[line 4](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md?plain=1#L4)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)]
* Added concrete efficiency example: checking budget compliance for 20 employees goes from 20 model round-trips to a single script, reducing context from hundreds of KB to a few lines. [[line 7](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md?plain=1#L7)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)]

#### [Tool search tool](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/agents-and-tools/tool-use/tool-search-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)]

* Improved context bloat explanation with concrete numbers: a typical multi-server setup (GitHub, Slack, Sentry, Grafana, Splunk) can consume ~55K tokens in definitions; tool search typically reduces this by over 85%. [[line 7](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/agents-and-tools/tool-use/tool-search-tool.md?plain=1#L7)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)]
* Added best practice recommendation for consistent namespacing in tool names (prefix by service, e.g. `github_`, `slack_`). [[line 495](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/agents-and-tools/tool-use/tool-search-tool.md?plain=1#L495)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)]

#### [C# beta SDK reference (beta.md and related files)](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/api/csharp/beta.md) [[Source](https://platform.claude.com/docs/en/api/csharp/beta)]

* Added new `code_execution_20260120` beta enum value across code execution tool types
* Added `BetaCodeExecutionTool20260120` class with `DeferLoading` and `Strict` fields
* Internal class renamed from `UnionMember2` to `All` for `BetaAllThinkingTurns`

#### [C# beta Files (beta/files.md)](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/api/csharp/beta/files.md) [[Source](https://platform.claude.com/docs/en/api/csharp/beta/files)]

* Added the `Upload File` endpoint (`Beta.Files.Upload`) to the Files API index

#### [Compaction](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/build-with-claude/compaction.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]

* Expanded description to explain that compaction isn't only about staying under token limits — long contexts cause models to lose focus, and compaction actively keeps the active context performant. Added link to "Effective context engineering" article. [[line 7](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/build-with-claude/compaction.md?plain=1#L7)] [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]

#### [Context editing](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/build-with-claude/context-editing.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/context-editing)]

* Enhanced explanation: context editing is about actively curating what Claude sees, not just cost optimization. Context is a finite resource with diminishing returns, and irrelevant content degrades model focus. Added link to "Effective context engineering" article. [[line 8](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/build-with-claude/context-editing.md?plain=1#L8)] [[Source](https://platform.claude.com/docs/en/build-with-claude/context-editing)]

#### [Context windows](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/build-with-claude/context-windows.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]

* Introduced "context rot" concept: accuracy and recall degrade as token count grows, making context curation as important as available context size. [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/build-with-claude/context-windows.md?plain=1#L11)] [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]
* Added Claude's state-of-the-art results on MRCR and GraphWalks long-context retrieval benchmarks. [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/build-with-claude/context-windows.md?plain=1#L14)] [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]
* Added guidance for multi-session agents: design state artifacts for fast context recovery at session start, with a reference to the memory tool's multi-session pattern. [[line 155](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/build-with-claude/context-windows.md?plain=1#L155)] [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]

#### [IP addresses](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/api/ip-addresses.md) [[Source](https://platform.claude.com/docs/en/api/ip-addresses)]

* The four previously "pending phase-out" IP addresses (`34.162.46.92`, `34.162.102.82`, `34.162.136.91`, `34.162.142.92`) are now confirmed phased out and grouped with the existing phased-out address (`34.162.183.95`). Users should remove all five from firewall allowlists. [[line 22](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/api/ip-addresses.md?plain=1#L22)] [[Source](https://platform.claude.com/docs/en/api/ip-addresses)]

#### [Claude prompting best practices](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/build-with-claude/prompt-engineering/claude-prompting-best-practices.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)]

* Major restructure: the document is now the single comprehensive prompt engineering reference, consolidating content previously spread across multiple topic pages
* Added "golden rule" analogy for instruction clarity: show your prompt to a colleague with minimal context — if they'd be confused, Claude will be too. [[line 35](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/build-with-claude/prompt-engineering/claude-prompting-best-practices.md?plain=1#L35)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)]
* Added detailed guidance on using examples effectively (few-shot prompting): relevance, diversity, use of `<example>` tags, and 3–5 examples as a target. [[line 31](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/build-with-claude/prompt-engineering/claude-prompting-best-practices.md?plain=1#L31)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)]
* Added dedicated sections on XML tag structuring, giving Claude a role, long-context prompting (put longform data at top, use XML for documents, ground responses in quotes), and model self-knowledge prompts. [[line 56](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/build-with-claude/prompt-engineering/claude-prompting-best-practices.md?plain=1#L56)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)]
* Added new "Output and formatting" section covering format control strategies (tell what to do vs. not to do, XML format indicators, matching prompt style to desired output style). [[line 112](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/build-with-claude/prompt-engineering/claude-prompting-best-practices.md?plain=1#L112)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)]

#### [Prompt engineering overview](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/build-with-claude/prompt-engineering/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)]

* Removed the step-by-step ordered list of prompting techniques and replaced with a single pointer to `claude-prompting-best-practices.md` as the living reference. Added link to the new prompting tools page. [[line 24](https://github.com/gpambrozio/ClaudeDocs/blob/aa8b0a3/docs-md/api/build-with-claude/prompt-engineering/overview.md?plain=1#L24)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)]
