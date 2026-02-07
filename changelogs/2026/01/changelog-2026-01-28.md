# [Claude docs changes for January 28th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/bb437c932a13e623b3cf5be546c4f101586c54a5) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/bb437c932a13e623b3cf5be546c4f101586c54a5)]

## Executive Summary
- New versions 2.1.21-2.1.22: Automatic Python virtual environment activation in VS Code and improved tool preference for file operations
- Permission wildcard syntax updated from `:*` to ` *` (space before asterisk) across all documentation
- New enterprise Skills governance guide published and desktop app documentation completely rewritten

## Detailed Changes

## New Claude Code versions

### [2.1.21](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/versions/2.1.21.md)

#### New features

* Added support for full-width (zenkaku) number input from Japanese IME in option selection prompts
* [VSCode] Added automatic Python virtual environment activation, ensuring `python` and `pip` commands use the correct interpreter (configurable via `claudeCode.usePythonEnvironment` setting)

#### Existing feature improvements

* Improved read/search progress indicators to show "Reading…" while in progress and "Read" when complete
* Improved Claude to prefer file operation tools (Read, Edit, Write) over bash equivalents (cat, sed, awk)

#### Major bug fixes

* Fixed shell completion cache files being truncated on exit
* Fixed API errors when resuming sessions that were interrupted during tool execution
* Fixed auto-compact triggering too early on models with large output token limits
* Fixed task IDs potentially being reused after deletion
* Fixed file search not working in VS Code extension on Windows
* [VSCode] Fixed message action buttons having incorrect background colors

### [2.1.22](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/versions/2.1.22.md)

#### Major bug fixes

* Fixed structured outputs for non-interactive (-p) mode

-----

## Claude Code changes

### New Documents

#### [Skills for enterprise](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/api/agents-and-tools/agent-skills/enterprise.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise)]

New comprehensive enterprise guide for Agent Skills governance and management. Covers security review and vetting with risk tier assessment (code execution, instruction manipulation, MCP server references, network access, credentials, file system access). Includes detailed review checklist for evaluating third-party Skills. Provides guidance on evaluation frameworks (triggering accuracy, isolation, coexistence, instruction following, output quality), lifecycle management (plan, create, test, deploy, monitor, iterate/deprecate), organizing Skills at scale (recall limits, consolidation strategies, role-based bundles), and distribution via Git and Skills API with versioning strategies. [[lines 1-188](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/api/agents-and-tools/agent-skills/enterprise.md?plain=1#L1-L188)]

### Changed documents

#### [Best practices](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

* Updated Bash permission examples to use new ` *` wildcard syntax instead of deprecated `:*` syntax. [[line 113](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/best-practices.md?plain=1#L113)] [[Source](https://code.claude.com/docs/en/best-practices#explore-first,-then-plan,-then-code)]

#### [CLI reference](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Updated `--allowedTools` and `--disallowedTools` flag examples to use new ` *` wildcard syntax. [[lines 61-62](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/cli-reference.md?plain=1#L61-L62)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [Claude Code on the web](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* Added three new allowed domains for Limited network access mode: plugins.gradle.org, kotlin.org, and www.kotlin.org. [[lines 455-457](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L455-L457)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#package-managers-jvm)]

#### [Common workflows](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Added documentation for `/commit-push-pr` skill that commits, pushes, and opens a PR in one step. [[lines 471-479](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/common-workflows.md?plain=1#L471-L479)] [[Source](https://code.claude.com/docs/en/common-workflows#create-pull-requests)]
* Added note about automatic Slack posting when PR URLs are created and Slack MCP server is configured with channels in CLAUDE.md. [[lines 481-481](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/common-workflows.md?plain=1#L481)] [[Source](https://code.claude.com/docs/en/common-workflows#create-pull-requests)]

#### [Desktop](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Complete major rewrite and restructuring of the desktop app documentation. Added new "Getting Started" section with step-by-step installation and setup guide. [[lines 7-46](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/desktop.md?plain=1#L7-L46)] [[Source](https://code.claude.com/docs/en/desktop)]
* Added three-tab explanation (Chat, Cowork, Code) clarifying which tab this documentation covers. [[lines 14-20](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/desktop.md?plain=1#L14-L20)] [[Source](https://code.claude.com/docs/en/desktop)]
* Added comprehensive "Getting started" tutorial with folder selection, session starting, and change review workflow. [[lines 48-82](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/desktop.md?plain=1#L48-L82)] [[Source](https://code.claude.com/docs/en/desktop#installation-and-setup)]
* Added detailed section on permission modes (Ask, Code, Plan) with explanations and use cases. [[lines 107-137](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/desktop.md?plain=1#L107-L137)] [[Source](https://code.claude.com/docs/en/desktop#work-in-parallel-with-sessions)]
* Added section on session management including parallel sessions and automatic session recovery. [[lines 139-159](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/desktop.md?plain=1#L139-L159)] [[Source](https://code.claude.com/docs/en/desktop#create-custom-skills)]
* Added comprehensive remote sessions section explaining cloud-based sessions for long-running tasks. [[lines 161-186](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/desktop.md?plain=1#L161-L186)] [[Source](https://code.claude.com/docs/en/desktop#cli-flag-equivalents)]
* Added "Extending Claude Code" section covering MCP connectors, skills, and hooks. [[lines 188-231](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/desktop.md?plain=1#L188-L231)] [[Source](https://code.claude.com/docs/en/desktop#what’s-different)]
* Added detailed environment configuration section with CLAUDE.md and .claudeignore usage. [[lines 233-279](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/desktop.md?plain=1#L233-L279)] [[Source](https://code.claude.com/docs/en/desktop#app-won’t-quit)]
* Added Desktop vs CLI comparison table highlighting key differences and shared capabilities. [[lines 281-305](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/desktop.md?plain=1#L281-L305)] [[Source](https://code.claude.com/docs/en/desktop#related-resources)]
* Added comprehensive troubleshooting section covering common issues and solutions. [[lines 307-356](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/desktop.md?plain=1#L307-L356)] [[Source](https://code.claude.com/docs/en/desktop#related-resources)]

#### [Headless](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* Updated Bash permission examples to use new ` *` wildcard syntax instead of `:*`. [[lines 95-96](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/headless.md?plain=1#L95-L96)] [[Source](https://code.claude.com/docs/en/headless#auto-approve-tools)]
* Added clarification that the space before `*` is significant for word boundary matching. [[line 98](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/headless.md?plain=1#L98)] [[Source](https://code.claude.com/docs/en/headless#auto-approve-tools)]

#### [IAM](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/iam.md) [[Source](https://code.claude.com/docs/en/iam)]

* Updated Bash permission wildcard syntax documentation, changing from `:*` to ` *` (space before asterisk) for prefix matching with word boundaries. [[lines 199-210](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/iam.md?plain=1#L199-L210)] [[Source](https://code.claude.com/docs/en/iam#settings-precedence)]
* Added clarification that `:*` syntax is deprecated but still equivalent to ` *`. [[line 210](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/iam.md?plain=1#L210)] [[Source](https://code.claude.com/docs/en/iam#settings-precedence)]
* Updated all examples throughout the document to use new ` *` syntax. [[lines 197-218](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/iam.md?plain=1#L197-L218)] [[Source](https://code.claude.com/docs/en/iam#managed-settings)]

#### [Interactive mode](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Added new `/copy` command to copy the last assistant response to clipboard. [[line 97](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/interactive-mode.md?plain=1#L97)] [[Source](https://code.claude.com/docs/en/interactive-mode#built-in-commands)]
* Added clarification that in vim normal mode, arrow keys navigate command history when cursor is at input boundaries and cannot move further. [[line 144](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/interactive-mode.md?plain=1#L144)] [[Source](https://code.claude.com/docs/en/interactive-mode#navigation-normal-mode)]
* Added new "PR review status" section documenting color-coded PR link indicators in footer (green=approved, yellow=pending, red=changes requested, gray=draft) with Cmd/Ctrl+click to open in browser. [[lines 266-277](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/interactive-mode.md?plain=1#L266-L277)] [[Source](https://code.claude.com/docs/en/interactive-mode#pr-review-status)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Fixed MCP server name from "VibeProspecting" to "Vibe Prospecting" with updated command name to `vibe-prospecting`. [[line 223](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/mcp.md?plain=1#L223)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]

#### [Memory](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Added new section on loading memory files from additional directories using `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD` environment variable with `--add-dir` flag. [[lines 64-75](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/memory.md?plain=1#L64-L75)] [[Source](https://code.claude.com/docs/en/memory#load-memory-from-additional-directories)]

#### [Sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Added note that `/sandbox` menu displays installation instructions when sandbox dependencies are missing. [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/sandboxing.md?plain=1#L82)] [[Source](https://code.claude.com/docs/en/sandboxing#enable-sandboxing)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added note that Claude Code automatically creates timestamped backups of configuration files and retains the five most recent backups. [[line 93](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/settings.md?plain=1#L93)] [[Source](https://code.claude.com/docs/en/settings#settings-files)]
* Updated all Bash permission examples throughout the document to use new ` *` wildcard syntax instead of `:*`. [[lines 106, 110, 172-174](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/settings.md?plain=1#L106)]
* Replaced two-wildcard syntax table with simplified single glob pattern documentation, emphasizing that space before `*` matters for word boundary matching. [[lines 217-238](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/settings.md?plain=1#L217-L238)] [[Source](https://code.claude.com/docs/en/settings#wildcard-patterns)]
* Added note that legacy `:*` suffix syntax is deprecated but equivalent to ` *`. [[line 240](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/settings.md?plain=1#L240)] [[Source](https://code.claude.com/docs/en/settings#wildcard-patterns)]
* Added `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD` to environment variables table. [[line 331](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/settings.md?plain=1#L331)] [[Source](https://code.claude.com/docs/en/settings#attribution-settings)]
* Updated TaskUpdate tool description to note it can delete tasks from the list. [[line 438](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/settings.md?plain=1#L438)] [[Source](https://code.claude.com/docs/en/settings#settings-precedence)]

#### [Skills](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Updated all Bash permission examples in skill configurations to use new ` *` wildcard syntax. [[lines 94, 147, 173](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/skills.md?plain=1#L94)]

#### [Sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Clarified that background subagents prompt for all required permissions upfront before launching. [[line 100](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/claude-code/sub-agents.md?plain=1#L100)] [[Source](https://code.claude.com/docs/en/sub-agents#quickstart:-create-your-first-subagent)]

-----

## API changes

### Changed documents

#### [Remote MCP servers](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Fixed MCP server name from "VibeProspecting" to "Vibe Prospecting". [[line 62](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L62)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
* Updated LSEG server URL from `/mcp` to `/mcp/server-cl`. [[line 56](https://github.com/gpambrozio/ClaudeDocs/blob/bb437c932a13e623b3cf5be546c4f101586c54a5/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L56)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
