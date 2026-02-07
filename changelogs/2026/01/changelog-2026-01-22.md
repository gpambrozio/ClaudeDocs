# [Claude docs changes for January 22nd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/2fd40c0332a3d490db0ca7a466e49103c0feddb6) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/2fd40c0332a3d490db0ca7a466e49103c0feddb6)]

## Executive Summary
- New version 2.1.15: npm installation deprecation notifications and improved UI rendering with React Compiler
- Four major new documentation pages created: best-practices, features-overview, how-claude-code-works, and ide-integrations
- Desktop and web platforms gained a new diff view for reviewing changes before creating PRs

## Detailed Changes

## New Claude Code versions

### [2.1.15](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/versions/2.1.15.md)

#### Existing feature improvements

* Added deprecation notification for npm installations - run `claude install` or see installation docs for more options
* Improved UI rendering performance with React Compiler

#### Major bug fixes

* Fixed the "Context left until auto-compact" warning not disappearing after running `/compact`
* Fixed MCP stdio server timeout not killing child process, which could cause UI freezes

-----

## Claude Code changes

### New Documents

#### [best-practices](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

Comprehensive best practices guide for working effectively with Claude Code. Covers giving Claude verification criteria, the explore-plan-implement-commit workflow, providing specific context in prompts, configuring your environment (CLAUDE.md, permissions, CLI tools, MCP servers, slash commands, plugins, hooks, subagents, skills), effective communication strategies, session management, automation patterns, and common failure patterns to avoid.

#### [features-overview](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/features-overview.md) [[Source](https://code.claude.com/docs/en/features-overview)]

Overview of Claude Code's extension layer, explaining how to customize what Claude knows, connect to external services, and automate workflows. Covers CLAUDE.md for persistent context, Skills for reusable knowledge and workflows, MCP for external service connections, Subagents for isolated execution, and Hooks for deterministic automation. Includes guidance on matching features to goals, comparing similar features, combining features, and understanding context costs by feature type.

#### [how-claude-code-works](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/how-claude-code-works.md) [[Source](https://code.claude.com/docs/en/how-claude-code-works)]

Explains Claude Code's core architecture including the agentic loop (gather context, take action, verify results), models for reasoning, built-in tools (file operations, search, execution, web), what Claude can access, session management, context window behavior, and safety mechanisms with checkpoints and permissions. Includes tips for working effectively with Claude Code.

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

New document explaining how Claude Code runs in VS Code, JetBrains IDEs, and other environments. Covers the two integration patterns: native extensions (VS Code, Cursor) with deep IDE integration, and IDE connection via `/ide` command for other editors. Explains automatic and manual IDE connection, connection status, and CLI-first vs GUI-first approaches.

### Changed documents

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* Added new diff view feature for reviewing Claude's changes before creating PRs. [[lines 85-107](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L85-L107)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#from-terminal-to-web)]
* Updated workflow step to mention reviewing changes in diff view and iterating with comments. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L9)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#what-is-claude-code-on-the-web)]

#### [common-workflows](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Updated page description to focus on practical workflows for everyday development. [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/common-workflows.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/common-workflows)]

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* Fixed broken link to plan mode documentation. [[line 65](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/costs.md?plain=1#L65)] [[Source](https://code.claude.com/docs/en/costs#manage-context-proactively)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Added new diff view feature for reviewing Claude's changes file by file before creating PRs, with ability to comment on specific lines to iterate further. [[lines 18-35](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/desktop.md?plain=1#L18-L35)] [[Source](https://code.claude.com/docs/en/desktop#installation)]

#### [discover-plugins](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* Added ability to filter plugin list by name or description in the Installed tab. [[line 44](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/discover-plugins.md?plain=1#L44)] [[Source](https://code.claude.com/docs/en/discover-plugins#code-intelligence)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Added new hook lifecycle diagram and table showing when each hook fires during a Claude Code session. [[lines 5-24](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/hooks.md?plain=1#L5-L24)] [[Source](https://code.claude.com/docs/en/hooks#hook-lifecycle)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Added history-based autocomplete for `!` bash commands - type a partial command and press Tab to complete from previous commands in current project. [[line 109](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/interactive-mode.md?plain=1#L109)] [[Source](https://code.claude.com/docs/en/interactive-mode#vim-editor-mode)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Removed duplicate Hex MCP server entry from examples. [[line 491](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/mcp.md?plain=1#L491)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]

#### [memory](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Renamed "Enterprise policy" to "Managed policy" for clarity. [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/memory.md?plain=1#L11)] [[Source](https://code.claude.com/docs/en/memory#determine-memory-type)]

#### [plugin-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Added ability to pin GitHub plugins to specific branch, tag, or commit using `ref` and `sha` fields. [[lines 172-186](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/plugin-marketplaces.md?plain=1#L172-L186)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#create-the-marketplace-file)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added new `DISABLE_INSTALLATION_CHECKS` environment variable to disable installation warnings. [[line 890](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/settings.md?plain=1#L890)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]

#### [slash-commands](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/slash-commands.md) [[Source](https://code.claude.com/docs/en/slash-commands)]

* Changed page title from "Built-in slash commands" to "Extend Claude with skills" to better reflect the page's focus on skills and custom commands. [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/slash-commands.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/slash-commands)]

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Updated command menu description to reference plan usage (`/usage`) instead of account usage. [[line 69](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/claude-code/vs-code.md?plain=1#L69)] [[Source](https://code.claude.com/docs/en/vs-code#use-the-prompt-box)]

-----

## API changes

### Changed documents

#### [build-with-claude/files](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Updated contact email address for requesting higher rate limits during beta. [[line 284](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/api/build-with-claude/files.md?plain=1#L284)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

#### [agents-and-tools/remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Removed duplicate Hex MCP server entry from the remote servers table. [[line 134](https://github.com/gpambrozio/ClaudeDocs/blob/2fd40c0332a3d490db0ca7a466e49103c0feddb6/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L134)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
