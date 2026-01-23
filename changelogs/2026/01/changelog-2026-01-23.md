# [Claude docs changes for January 23rd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/bb00727242a56829032c3094ccf15d8876c36282) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/bb00727242a56829032c3094ccf15d8876c36282)]

## New Claude Code versions

### [2.1.16](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/versions/2.1.16.md)

#### New features

* Added new task management system with dependency tracking capabilities
* [VSCode] Added native plugin management support
* [VSCode] Added ability for OAuth users to browse and resume remote Claude sessions from the Sessions dialog

#### Major bug fixes

* Fixed out-of-memory crashes when resuming sessions with heavy subagent usage
* Fixed an issue where the "context remaining" warning was not hidden after running `/compact`
* Fixed session titles on the resume screen not respecting the user's language setting
* [IDE] Fixed a race condition on Windows where the Claude Code sidebar view container would not appear on start

### [2.1.17](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/versions/2.1.17.md)

#### Major bug fixes

* Fixed crashes on processors without AVX instruction support

-----

## Claude Code changes

### Changed documents

#### [best-practices](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

* Added reference to "How Claude Code works" documentation for understanding the agentic loop. [[line 6](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/best-practices.md?plain=1#L6)] [[Source](https://code.claude.com/docs/en/best-practices#claude-codes-context-window-fills-up-fast-and-performance-degrades-as-it-fills)]
* Added reference to "Reduce token usage" documentation for context management strategies. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/best-practices.md?plain=1#L12)] [[Source](https://code.claude.com/docs/en/best-practices#claude-codes-context-window-fills-up-fast-and-performance-degrades-as-it-fills)]
* Added reference to "Extend Claude Code" documentation for extension features overview. [[line 143](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/best-practices.md?plain=1#L143)] [[Source](https://code.claude.com/docs/en/best-practices#configure-your-environment)]
* Added guidance that CLAUDE.md should only include broadly applicable content, with domain knowledge moved to skills. [[lines 168-169](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/best-practices.md?plain=1#L168-L169)] [[Source](https://code.claude.com/docs/en/best-practices#write-an-effective-claude-md)]
* Reorganized extension configuration section to prioritize hooks and skills over plugins. [[lines 235-289](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/best-practices.md?plain=1#L235-L289)] [[Source](https://code.claude.com/docs/en/best-practices#set-up-hooks)]
* Added guidance on customizing compaction behavior with CLAUDE.md instructions. [[line 401](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/best-practices.md?plain=1#L401)] [[Source](https://code.claude.com/docs/en/best-practices#manage-context-aggressively)]
* Added "Related resources" section with links to key documentation. [[lines 580-590](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/best-practices.md?plain=1#L580-L590)] [[Source](https://code.claude.com/docs/en/best-practices#related-resources)]

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* Added new allowed domains for limited network access: docs.claude.com, code.claude.com, npm.pkg.github.com, pkg-npm.githubusercontent.com, gcr.io, index.crates.io, sentry.io, sourceforge.net, datadoghq domains, and modelcontextprotocol.io. [[lines 319-550](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L319-L550)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#limited-network-access)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Updated subagent model parameter to include "inherit" option and clarified that it defaults to inheriting the main conversation's model. [[line 80](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/cli-reference.md?plain=1#L80)] [[Source](https://code.claude.com/docs/en/cli-reference#define-custom-subagents)]

#### [common-workflows](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Added reference to "Best practices" documentation. [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/common-workflows.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/common-workflows)]
* Removed "Create custom skills and commands" and "Let Claude interview you" sections (content consolidated elsewhere). [[lines 324-450](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/common-workflows.md?plain=1#L324-L450)] [[Source](https://code.claude.com/docs/en/common-workflows#use-plan-mode-for-safe-code-analysis)]
* Updated "Next steps" section with links to Best practices, How Claude Code works, and Extend Claude Code documentation. [[lines 1132-1140](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/common-workflows.md?plain=1#L1132-L1140)] [[Source](https://code.claude.com/docs/en/common-workflows#next-steps)]

#### [features-overview](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/features-overview.md) [[Source](https://code.claude.com/docs/en/features-overview)]

* Clarified that subagents are useful when context window is getting full, as subagent work doesn't consume main context. [[line 55](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/features-overview.md?plain=1#L55)] [[Source](https://code.claude.com/docs/en/features-overview#skills-and-subagents)]
* Added new section explaining how features layer at multiple levels (user-wide, per-project, via plugins, managed policies) with override and merge behavior. [[lines 78-85](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/features-overview.md?plain=1#L78-L85)] [[Source](https://code.claude.com/docs/en/features-overview#understand-how-features-layer)]

#### [gitlab-ci-cd](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/gitlab-ci-cd.md) [[Source](https://code.claude.com/docs/en/gitlab-ci-cd)]

* Simplified allowedTools syntax by removing glob patterns (e.g., "Bash Read Edit Write" instead of "Bash(*) Read(*) Edit(*) Write(*)"). [[lines 83-375](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/gitlab-ci-cd.md?plain=1#L83-L375)] [[Source](https://code.claude.com/docs/en/gitlab-ci-cd#configure-gitlab-mcp-server)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Split Stop and SubagentStop input documentation into separate sections with distinct fields. [[lines 752-777](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/hooks.md?plain=1#L752-L777)] [[Source](https://code.claude.com/docs/en/hooks#stop-input)]
* Added cwd field to Stop hook input. [[line 766](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/hooks.md?plain=1#L766)] [[Source](https://code.claude.com/docs/en/hooks#stop-input)]
* Added new SubagentStop hook input documentation with agent_id and agent_transcript_path fields. [[lines 773-777](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/hooks.md?plain=1#L773-L777)] [[Source](https://code.claude.com/docs/en/hooks#subagentstop-input)]
* Added cwd and model fields to SessionStart hook input, with explanation of source field values. [[lines 843-851](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/hooks.md?plain=1#L843-L851)] [[Source](https://code.claude.com/docs/en/hooks#sessionstart-input)]
* Added new SubagentStart hook input documentation with agent_id and agent_type fields. [[lines 854-870](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/hooks.md?plain=1#L854-L870)] [[Source](https://code.claude.com/docs/en/hooks#subagentstart-input)]

#### [iam](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/iam.md) [[Source](https://code.claude.com/docs/en/iam)]

* Added clarification about gitignore pattern matching behavior and how to allow all file access. [[line 157](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/iam.md?plain=1#L157)] [[Source](https://code.claude.com/docs/en/iam#tool-specific-syntaxes)]

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* Added new section for resuming remote Claude.ai sessions from VS Code with OAuth subscription. [[lines 93-115](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/ide-integrations.md?plain=1#L93-L115)] [[Source](https://code.claude.com/docs/en/ide-integrations#resume-remote-sessions-from-claude-ai)]
* Added new section documenting the graphical plugin management interface in VS Code. [[lines 141-173](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/ide-integrations.md?plain=1#L141-L173)] [[Source](https://code.claude.com/docs/en/ide-integrations#manage-plugins)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Added new section documenting the task list feature with Ctrl+T toggle, persistence, and CLAUDE_CODE_TASK_LIST_ID environment variable. [[lines 253-260](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/interactive-mode.md?plain=1#L253-L260)] [[Source](https://code.claude.com/docs/en/interactive-mode#task-list)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Added Webflow MCP server to the built-in integrations list. [[lines 397-401](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/mcp.md?plain=1#L397-L401)] [[Source](https://code.claude.com/docs/en/mcp#built-in-integrations)]
* Added clarification that "local scope" for MCP servers differs from general local settings file locations. [[line 701](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/mcp.md?plain=1#L701)] [[Source](https://code.claude.com/docs/en/mcp#local-scope)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Added WSL2 support documentation with bubblewrap and socat installation prerequisites. [[lines 47-78](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/sandboxing.md?plain=1#L47-L78)] [[Source](https://code.claude.com/docs/en/sandboxing#how-it-works)]
* Updated platform support to specify WSL2 support and WSL1 limitations. [[line 229](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/sandboxing.md?plain=1#L229)] [[Source](https://code.claude.com/docs/en/sandboxing#limitations-and-considerations)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Updated sandboxing documentation to include WSL2 support. [[lines 274-282](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/settings.md?plain=1#L274-L282)] [[Source](https://code.claude.com/docs/en/settings#sandboxing)]
* Updated allowFilesMatchingPatterns description to clarify it excludes files from discovery and denies read operations. [[line 495](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/settings.md?plain=1#L495)] [[Source](https://code.claude.com/docs/en/settings#file-access-control)]
* Added CLAUDE_CODE_TASK_LIST_ID environment variable documentation. [[line 868](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/settings.md?plain=1#L868)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]
* Replaced TodoWrite tool with four new task management tools: TaskCreate, TaskGet, TaskList, and TaskUpdate. [[lines 935-938](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/settings.md?plain=1#L935-L938)] [[Source](https://code.claude.com/docs/en/settings#tools)]

#### [setup](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* Added note that WSL2 supports sandboxing while WSL1 does not. [[line 225](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/setup.md?plain=1#L225)] [[Source](https://code.claude.com/docs/en/setup#windows-installation)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Clarified skill priority override behavior and plugin skill namespacing. [[line 92](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/skills.md?plain=1#L92)] [[Source](https://code.claude.com/docs/en/skills#choose-skill-scope)]

#### [troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/troubleshooting.md) [[Source](https://code.claude.com/docs/en/troubleshooting)]

* Added new section for WSL2 sandbox setup with package installation instructions. [[lines 56-79](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/troubleshooting.md?plain=1#L56-L79)] [[Source](https://code.claude.com/docs/en/troubleshooting#wsl2-sandbox-setup)]
* Removed "allowed tools" from configuration file locations description. [[lines 223-255](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/troubleshooting.md?plain=1#L223-L255)] [[Source](https://code.claude.com/docs/en/troubleshooting#configuration-files)]

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Added new section for resuming remote Claude.ai sessions from VS Code with OAuth subscription. [[lines 93-115](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/vs-code.md?plain=1#L93-L115)] [[Source](https://code.claude.com/docs/en/vs-code#resume-remote-sessions-from-claude-ai)]
* Added new section documenting the graphical plugin management interface in VS Code. [[lines 141-173](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/claude-code/vs-code.md?plain=1#L141-L173)] [[Source](https://code.claude.com/docs/en/vs-code#manage-plugins)]

-----

## API changes

### Changed documents

#### [agents-and-tools/remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Added Webflow MCP server to the integrations list for managing CMS, pages, assets and sites. [[lines 555-561](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L555-L561)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers#available-integrations)]

#### [api/client-sdks](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/api/api/client-sdks.md) [[Source](https://platform.claude.com/docs/en/api/client-sdks)]

* Added minimum SDK version requirements: Python SDK 0.22.0 and TypeScript SDK 0.37.0. [[lines 15-31](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/api/api/client-sdks.md?plain=1#L15-L31)] [[Source](https://platform.claude.com/docs/en/api/client-sdks#python)]

#### [build-with-claude/extended-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Changed error behavior when toggling thinking mid-turn to graceful degradation instead of hard errors - thinking is now automatically disabled with silent stripping of thinking blocks. [[lines 211-226](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L211-L226)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#graceful-thinking-degradation)]
* Updated guidance on thinking blocks in cached contexts - now thinking content is stripped when disabled rather than causing request failures. [[line 295](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L295)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#extended-thinking-with-prompt-caching)]

#### [build-with-claude/prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* Added important notice that prompt caching will use workspace-level isolation starting February 5, 2026 (applies to Claude API and Azure only). [[line 338](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L338)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#cache-storage-and-sharing)]

#### [build-with-claude/workspaces](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/api/build-with-claude/workspaces.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/workspaces)]

* Added note that prompt caches will be workspace-isolated starting February 5, 2026 (Claude API and Azure only). [[line 172](https://github.com/gpambrozio/ClaudeDocs/blob/bb00727242a56829032c3094ccf15d8876c36282/docs-md/api/build-with-claude/workspaces.md?plain=1#L172)] [[Source](https://platform.claude.com/docs/en/build-with-claude/workspaces#workspace-scoped-resources)]
