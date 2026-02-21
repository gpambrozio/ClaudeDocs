# [Claude docs changes for February 21st, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/8ae88ba) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/8ae88ba)]

## Executive Summary
- Claude Code Desktop gains major new features: live app preview with embedded browser, GitHub PR monitoring with auto-fix and auto-merge, and a new "Review code" button in diff view
- Fast mode pricing simplified to a single flat rate ($30/$150 per MTok) with full 1M context window included — no more premium for requests over 200K tokens
- Version 2.1.50 brings numerous memory leak fixes for long sessions, new `WorktreeCreate`/`WorktreeRemove` hook events, and agent worktree isolation support
- Programmatic tool calling updated to new tool version `code_execution_20260120`; web search and web fetch tools can now be called programmatically
- New MCP servers added across both Claude Code and API docs, including Granola, monday.com, Asana, PubMed, Box, Miro, Microsoft Learn, and many more

## New Claude Code versions

### [2.1.49](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/versions/2.1.49.md)

#### Existing feature improvements

* Improved MCP OAuth authentication with step-up auth support and discovery caching, reducing redundant network requests during server connections

### [2.1.50](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/versions/2.1.50.md)

#### New features

* Added support for `startupTimeout` configuration for LSP servers
* Added `WorktreeCreate` and `WorktreeRemove` hook events, enabling custom VCS setup and teardown when agent worktree isolation creates or removes worktrees
* Added support for `isolation: worktree` in agent definitions, allowing agents to declaratively run in isolated git worktrees
* `CLAUDE_CODE_SIMPLE` mode now also disables MCP tools, attachments, hooks, and CLAUDE.md file loading for a fully minimal experience
* Added `claude agents` CLI command to list all configured agents
* Added `CLAUDE_CODE_DISABLE_1M_CONTEXT` environment variable to disable 1M context window support
* Opus 4.6 (fast mode) now includes the full 1M context window
* VSCode: Added `/extra-usage` command support in VS Code sessions

#### Existing feature improvements

* Improved memory usage during long sessions by clearing internal caches after compaction
* Improved memory usage during long sessions by clearing large tool results after they have been processed
* Improved startup performance for headless mode (`-p` flag) by deferring Yoga WASM and UI component imports

#### Major bug fixes

* Fixed a bug where resumed sessions could be invisible when the working directory involved symlinks
* Fixed session data loss on SSH disconnect by flushing session data before hooks and analytics in the graceful shutdown sequence
* Linux: Fixed native modules not loading on systems with glibc older than 2.30 (e.g., RHEL 8)
* Fixed memory leak in agent teams where completed teammate tasks were never garbage collected from session state
* Fixed `CLAUDE_CODE_SIMPLE` to fully strip down skills, session memory, custom agents, and CLAUDE.md token counting
* Fixed `/mcp reconnect` freezing the CLI when given a server name that doesn't exist
* Fixed memory leak where completed task state objects were never removed from AppState
* Fixed bug where MCP tools were not discovered when tool search is enabled and a prompt is passed in as a launch argument
* Fixed prompt suggestion cache regression that reduced cache hit rates
* Fixed unbounded memory growth in long sessions by capping file history snapshots
* Fixed multiple memory leaks related to LSP diagnostic data, TaskOutput, CircularBuffer, and shell command execution

-----

## Claude Code changes

### Changed documents

#### [common-workflows](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Clarified worktree flag docs: `--worktree` is the full flag and `-w` is the shorthand (previously inconsistent) [[line 973](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/claude-code/common-workflows.md?plain=1#L973)] [[Source](https://code.claude.com/docs/en/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Added new "Preview your app" section documenting the live dev server preview feature, including how Claude auto-starts servers, takes screenshots, inspects the DOM, and iterates on findings [[line 67](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/claude-code/desktop.md?plain=1#L67)] [[Source](https://code.claude.com/docs/en/desktop#preview-your-app)]
* Added full "Configure preview servers" reference with `.claude/launch.json` format, `autoVerify` option, all configuration fields, and examples for Next.js, monorepos, and Node.js scripts [[line 147](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/claude-code/desktop.md?plain=1#L147)] [[Source](https://code.claude.com/docs/en/desktop#install-plugins)]
* Added "Review your code" feature: clicking "Review code" in the diff view toolbar has Claude evaluate diffs and leave inline comments [[line 84](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/claude-code/desktop.md?plain=1#L84)] [[Source](https://code.claude.com/docs/en/desktop#review-changes-with-diff-view)]
* Added "Monitor pull request status" section: CI status bar with auto-fix and auto-merge toggles powered by the GitHub CLI [[line 106](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/claude-code/desktop.md?plain=1#L106)] [[Source](https://code.claude.com/docs/en/desktop#manage-sessions)]
* Permission modes renamed: "Ask" → "Ask permissions", "Code" → "Auto accept edits", "Act" → "Bypass permissions" [[line 43](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/claude-code/desktop.md?plain=1#L43)] [[Source](https://code.claude.com/docs/en/desktop#add-files-and-context-to-prompts)]
* Windows ARM64 devices are now fully supported (previous note about local session limitations removed) [[line 504](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/claude-code/desktop.md?plain=1#L504)] [[Source](https://code.claude.com/docs/en/desktop#windows-specific-issues)]
* Cowork tab is now available on Windows on all supported hardware (previously macOS Apple Silicon only) [[line 507](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/claude-code/desktop.md?plain=1#L507)] [[Source](https://code.claude.com/docs/en/desktop#windows-specific-issues)]
* Managed settings key updated from `permissions.disableBypassPermissionsMode` to `disableBypassPermissionsMode`; added reference to `allowManagedPermissionRulesOnly` and `allowManagedHooksOnly` [[line 351](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/claude-code/desktop.md?plain=1#L351)] [[Source](https://code.claude.com/docs/en/desktop#admin-console-controls)]
* Updated note on `MAX_THINKING_TOKENS`: on Opus, setting is ignored except for `0` because adaptive reasoning controls thinking depth [[line 322](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/claude-code/desktop.md?plain=1#L322)] [[Source](https://code.claude.com/docs/en/desktop#local-sessions)]

#### [desktop-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/claude-code/desktop-quickstart.md) [[Source](https://code.claude.com/docs/en/desktop-quickstart)]

* Updated feature list to include live app preview and GitHub PR monitoring with auto-merge [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/claude-code/desktop-quickstart.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/desktop-quickstart)]
* Added note that the desktop app includes Claude Code — no separate Node.js or CLI install needed [[line 45](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/claude-code/desktop-quickstart.md?plain=1#L45)] [[Source](https://code.claude.com/docs/en/desktop-quickstart#install)]
* Removed Windows ARM64 limitation note (now fully supported)
* Updated Git requirements: Git is required on Windows for local sessions; most Macs include it by default [[line 58](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/claude-code/desktop-quickstart.md?plain=1#L58)] [[Source](https://code.claude.com/docs/en/desktop-quickstart#start-your-first-session)]

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* Corrected worktree flag docs: `--worktree` is the long form, `-w` is the shorthand [[line 320](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/claude-code/ide-integrations.md?plain=1#L320)] [[Source](https://code.claude.com/docs/en/ide-integrations#use-git-worktrees-for-parallel-tasks)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Added new MCP servers: Granola, monday.com, Asana, PubMed, Box, Miro, Scholar Gateway, Clinical Trials, GoDaddy, bioRxiv, ZoomInfo, Bitly, Coupler.io, Microsoft Learn, AWS Marketplace, WordPress.com, BioRender, Crypto.com, NPI Registry, CMS Coverage, ChEMBL, ICD-10 Codes, Trivago, Open Targets, Clockwise, CData Connect AI, MT Newswires, Similarweb, Candid, lastminute.com, Consensus, Udemy Business, Harmonic, Workato, PostHog, PlanetScale, Aura, Dice, Chronograph

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Corrected worktree flag docs: `--worktree` is the long form, `-w` is the shorthand [[line 320](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/claude-code/vs-code.md?plain=1#L320)] [[Source](https://code.claude.com/docs/en/vs-code#use-git-worktrees-for-parallel-tasks)]

-----

## API changes

### Changed documents

#### [administration-api](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/build-with-claude/administration-api.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/administration-api)]

* Simplified the Workspaces section: removed inline code examples and redirected to the Workspaces guide [[line 94](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/build-with-claude/administration-api.md?plain=1#L94)] [[Source](https://platform.claude.com/docs/en/build-with-claude/administration-api)]
* Condensed usage/cost and Claude Code analytics sections to brief summaries with links [[line 177](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/build-with-claude/administration-api.md?plain=1#L177)] [[Source](https://platform.claude.com/docs/en/build-with-claude/administration-api)]
* Removed duplicate workspace FAQ items (moved to the Workspaces page) [[line 207](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/build-with-claude/administration-api.md?plain=1#L207)] [[Source](https://platform.claude.com/docs/en/build-with-claude/administration-api)]

#### [bash-tool](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/agents-and-tools/tool-use/bash-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool)]

* Added note about multi-environment behavior: when using both the bash tool and the code execution tool, state is not shared between them, with a link to guidance [[line 262](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/agents-and-tools/tool-use/bash-tool.md?plain=1#L262)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool)]

#### [code-execution-tool](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

* Added new "Using code execution with other execution tools" section with system prompt guidance for multi-computer environments where Claude may confuse separate execution contexts [[line 84](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L84)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]
* Web search and web fetch tools removed from the "not supported for programmatic calling" list — they are now supported

#### [develop-tests](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/test-and-evaluate/develop-tests.md) [[Source](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)]

* Page renamed from "Create strong empirical evaluations" to "Define success criteria and build evaluations"; merged in the content previously on the separate "Define success criteria" page [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/test-and-evaluate/develop-tests.md?plain=1#L1)] [[Source](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)]
* Added detailed guidance on writing good success criteria (Specific, Measurable, Achievable, Relevant) with examples [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/test-and-evaluate/develop-tests.md?plain=1#L14)] [[Source](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)]

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/build-with-claude/fast-mode.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]

* Fast mode is now ZDR (Zero Data Retention) eligible [[line 8](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/build-with-claude/fast-mode.md?plain=1#L8)] [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]
* Pricing simplified: removed tiered pricing for >200K tokens; now a single flat rate of $30/MTok input and $150/MTok output for the full context window [[line 48](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/build-with-claude/fast-mode.md?plain=1#L48)] [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]

#### [increase-consistency](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/test-and-evaluate/strengthen-guardrails/increase-consistency.md) [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency)]

* Added new "Keep Claude in character" section with guidance on using system prompts for role-based applications and an enterprise chatbot example [[line 43](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/test-and-evaluate/strengthen-guardrails/increase-consistency.md?plain=1#L43)] [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency)]

#### [intro](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/intro.md) [[Source](https://platform.claude.com/docs/en/intro)]

* Replaced the simple "Get started" links section with a numbered 4-step "Recommended path for new developers" (quickstart → Messages API → models → features) [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/intro.md?plain=1#L14)] [[Source](https://platform.claude.com/docs/en/intro)]

#### [overview (build-with-claude)](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/build-with-claude/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

* Added new intro section summarizing the five API surface areas with guidance on where to start [[line 4](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/build-with-claude/overview.md?plain=1#L4)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

#### [pricing](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* Fast mode pricing simplified: removed the two-tier table (≤200K and >200K tokens); now a single $30/MTok input, $150/MTok output rate that applies to the full context window [[line 72](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/about-claude/pricing.md?plain=1#L72)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]
* Clarified that standard-speed long context pricing does not apply to fast mode requests [[line 110](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/about-claude/pricing.md?plain=1#L110)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

#### [programmatic-tool-calling](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)]

* Updated tool version identifier from `code_execution_20250825` to `code_execution_20260120` throughout all examples and reference tables [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md?plain=1#L14)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)]

#### [remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Added new MCP servers: Granola, monday.com, Box, Miro, Scholar Gateway, Indeed, S&P Global, GoDaddy, PitchBook Premium, Morningstar, Microsoft Learn, Kiwi.com, ICD-10 Codes, Daloopa, Moody's, Open Targets, Clockwise, CData Connect AI, MT Newswires, Learning Commons Knowledge Graph, Bitly, Coupler.io, Similarweb, Candid, lastminute.com, Consensus, Udemy Business, Harmonic, Workato, Supermetrics, Chronograph, Aura, Dice, Google Compute Engine, Common Room

#### [zero-data-retention](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/build-with-claude/zero-data-retention.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/zero-data-retention)]

* Added Fast Mode as a ZDR-eligible endpoint [[line 43](https://github.com/gpambrozio/ClaudeDocs/blob/8ae88ba/docs-md/api/build-with-claude/zero-data-retention.md?plain=1#L43)] [[Source](https://platform.claude.com/docs/en/build-with-claude/zero-data-retention)]
