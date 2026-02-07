# [Claude docs changes for February 5th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/468fec2b3bf4b520ffb8870b6d16969c1f89e49c) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/468fec2b3bf4b520ffb8870b6d16969c1f89e49c)]

## Executive Summary
- Chrome integration documentation restructured with improved clarity, Windows-specific troubleshooting, and tab-sharing behavior
- 100+ new MCP server integrations added including Circleback, Day AI, Linear, Netlify, Asana, Atlassian, Notion, and Slack
- New `prefersReducedMotion` accessibility setting and `@browser` integration for VS Code documented

## Detailed Changes

## Claude Code changes

### Changed documents

#### [Best practices](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

* Clarified that the Claude in Chrome extension "opens new tabs in your browser" rather than just "opens a browser". [[line 29](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/best-practices.md?plain=1#L29)] [[Source](https://code.claude.com/docs/en/best-practices#give-claude-a-way-to-verify-its-work)]

#### [Use Claude Code with Chrome (beta)](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/chrome.md) [[Source](https://code.claude.com/docs/en/chrome)]

* Major restructuring and expansion of Chrome integration documentation with improved clarity throughout
* Added explicit note that Chrome opens new tabs for browser tasks and shares browser's login state. [[lines 4-5](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/chrome.md?plain=1#L4-L5)] [[Source](https://code.claude.com/docs/en/chrome)]
* Simplified capabilities list and removed "How the integration works" and "Set up the integration" sections
* Clarified that a "direct Anthropic plan" is required (not third-party providers). [[line 29](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/chrome.md?plain=1#L29)] [[Source](https://code.claude.com/docs/en/chrome#prerequisites)]
* Streamlined "Get started in the CLI" section with clearer instructions. [[lines 32-75](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/chrome.md?plain=1#L32-L75)] [[Source](https://code.claude.com/docs/en/chrome#get-started-in-the-cli)]
* Added new section on Windows-specific issues and common error messages. [[lines 220-233](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/chrome.md?plain=1#L220-L233)] [[Source](https://code.claude.com/docs/en/chrome#connection-drops-during-long-sessions)]
* Updated troubleshooting section with more detailed instructions for native messaging host installation. [[lines 203-210](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/chrome.md?plain=1#L203-L210)] [[Source](https://code.claude.com/docs/en/chrome#extension-not-detected)]

#### [IDE integrations (VS Code & JetBrains)](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* Clarified that `Shift+Enter` for multi-line input also works in the "Other" free-text input of question dialogs. [[line 68](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/ide-integrations.md?plain=1#L68)] [[Source](https://code.claude.com/docs/en/ide-integrations#use-the-prompt-box)]
* Added note about reading specific pages from large PDFs (single page, ranges, or open-ended). [[line 83](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/ide-integrations.md?plain=1#L83)] [[Source](https://code.claude.com/docs/en/ide-integrations#reference-files-and-folders)]
* Added new section "Automate browser tasks with Chrome" with instructions for using `@browser` in VS Code. [[lines 173-188](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/ide-integrations.md?plain=1#L173-L188)] [[Source](https://code.claude.com/docs/en/ide-integrations#automate-browser-tasks-with-chrome)]

#### [Overview (Claude Code)](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/index.md) [[Source](https://code.claude.com/docs/en/index)]

* Added note about Claude Code running in multiple platforms (VS Code, JetBrains, desktop app, web, Slack). [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/index.md?plain=1#L82)] [[Source](https://code.claude.com/docs/en/index#get-started-in-30-seconds)]
* Updated "Why developers love Claude Code" to say "Meets you where you work" instead of "Works in your terminal". [[line 93](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/index.md?plain=1#L93)] [[Source](https://code.claude.com/docs/en/index#why-developers-love-claude-code)]

#### [Interactive mode](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Added new `/debug [description]` command for troubleshooting the current session by reading the session debug log. [[line 81](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/interactive-mode.md?plain=1#L81)] [[Source](https://code.claude.com/docs/en/interactive-mode#built-in-commands)]
* Clarified that `/model` changes take effect immediately without waiting for the current response to finish. [[line 89](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/interactive-mode.md?plain=1#L89)] [[Source](https://code.claude.com/docs/en/interactive-mode#built-in-commands)]

#### [MCP (Model Context Protocol)](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Added 100+ new MCP server integrations including Circleback, Day AI, bioRxiv, Linear, Netlify, Asana, Atlassian, Notion, Slack, Stripe, and many more. [[lines 25-620](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/mcp.md?plain=1#L25-L620)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* Added new section "Use pre-configured OAuth credentials" for MCP servers that don't support automatic OAuth setup. [[lines 1043-1109](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/mcp.md?plain=1#L1043-L1109)] [[Source](https://code.claude.com/docs/en/mcp#use-pre-configured-oauth-credentials)]
* Updated "Add MCP servers from JSON configuration" section with example for pre-configured OAuth credentials. [[line 1135](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/mcp.md?plain=1#L1135)] [[Source](https://code.claude.com/docs/en/mcp#add-mcp-servers-from-json-configuration)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added new `prefersReducedMotion` setting to reduce or disable UI animations for accessibility. [[line 172](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/settings.md?plain=1#L172)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* Added two new environment variables: `MCP_CLIENT_SECRET` for OAuth client secrets and `MCP_OAUTH_CALLBACK_PORT` for fixed OAuth redirect callback ports. [[lines 886-887](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/settings.md?plain=1#L886-L887)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]

#### [Sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Added new `memory` field to enable persistent memory for subagents across conversations. [[line 223](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/sub-agents.md?plain=1#L223)] [[Source](https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields)]
* Added new section "Enable persistent memory" explaining memory scopes (user, project, local) and how to configure them. [[lines 295-343](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/sub-agents.md?plain=1#L295-L343)] [[Source](https://code.claude.com/docs/en/sub-agents#enable-persistent-memory)]

#### [Use Claude Code in VS Code](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Clarified that `Shift+Enter` for multi-line input also works in the "Other" free-text input of question dialogs. [[line 68](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/vs-code.md?plain=1#L68)] [[Source](https://code.claude.com/docs/en/vs-code#use-the-prompt-box)]
* Added note about reading specific pages from large PDFs. [[line 83](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/vs-code.md?plain=1#L83)] [[Source](https://code.claude.com/docs/en/vs-code#reference-files-and-folders)]
* Added new section "Automate browser tasks with Chrome" with instructions for using `@browser` in VS Code. [[lines 173-188](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/claude-code/vs-code.md?plain=1#L173-L188)] [[Source](https://code.claude.com/docs/en/vs-code#automate-browser-tasks-with-chrome)]

-----

## API changes

### Changed documents

#### [Agent SDK Overview](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/api/agent-sdk/overview.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/overview)]

* Reorganized "Get started" section to appear earlier in the document, before "Capabilities". [[lines 33-94](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/api/agent-sdk/overview.md?plain=1#L33-L94)] [[Source](https://platform.claude.com/docs/en/agent-sdk/overview)]
* Removed the "Install Claude Code" step from the getting started guide - SDK no longer requires Claude Code CLI installation. [[line 33](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/api/agent-sdk/overview.md?plain=1#L33)] [[Source](https://platform.claude.com/docs/en/agent-sdk/overview)]

#### [Agent SDK Quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/api/agent-sdk/quickstart.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/quickstart)]

* Removed the "Install Claude Code" step entirely - Agent SDK no longer requires Claude Code CLI to be installed. [[line 22](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/api/agent-sdk/quickstart.md?plain=1#L22)] [[Source](https://platform.claude.com/docs/en/agent-sdk/quickstart)]
* Simplified API key setup instructions, removing references to Claude Code authentication. [[lines 52-66](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/api/agent-sdk/quickstart.md?plain=1#L52-L66)] [[Source](https://platform.claude.com/docs/en/agent-sdk/quickstart)]
* Updated troubleshooting section to remove "Claude Code not found" error reference. [[line 160](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/api/agent-sdk/quickstart.md?plain=1#L160)] [[Source](https://platform.claude.com/docs/en/agent-sdk/quickstart)]

#### [Agent SDK User input](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/api/agent-sdk/user-input.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/user-input)]

* Removed the 60-second timeout limitation for `canUseTool` callbacks. [[lines 32, 445](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/api/agent-sdk/user-input.md?plain=1#L32)]

#### [Build with Claude - Overview](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/api/build-with-claude/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

* Updated Structured outputs availability: now generally available on Amazon Bedrock (was Beta). [[line 23](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/api/build-with-claude/overview.md?plain=1#L23)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

#### [Extended thinking](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Updated contact sales team email link. [[line 98](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L98)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

#### [Files](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Updated contact us email link. [[line 284](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/api/build-with-claude/files.md?plain=1#L284)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

#### [MCP Connector](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/api/agents-and-tools/mcp-connector.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)]

* Added new section "Client-side MCP helpers (TypeScript)" with helper functions for converting between MCP types and Claude API types. [[lines 370-477](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/api/agents-and-tools/mcp-connector.md?plain=1#L370-L477)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)]
* Documented four new helper functions: `mcpTools`, `mcpMessages`, `mcpResourceToContent`, and `mcpResourceToFile`. [[lines 398-404](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/api/agents-and-tools/mcp-connector.md?plain=1#L398-L404)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)]

#### [Structured outputs](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/api/build-with-claude/structured-outputs.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

* Updated availability status: Structured outputs are now generally available on Amazon Bedrock (no longer in beta). [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/468fec2b3bf4b520ffb8870b6d16969c1f89e49c/docs-md/api/build-with-claude/structured-outputs.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]
