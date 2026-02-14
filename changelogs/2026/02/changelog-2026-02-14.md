# [Claude docs changes for February 14th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/936a08c51511a0621ae2b86bb9d6b56ace055db8) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/936a08c51511a0621ae2b86bb9d6b56ace055db8)]

## Executive Summary
- New Desktop quickstart guide provides streamlined onboarding for the Claude Code Desktop app
- Desktop documentation completely restructured with more comprehensive coverage of features, permission modes, and workflows
- Windows ARM64 support added to Desktop app (remote sessions only)
- New `/desktop` command enables handing off CLI sessions to the Desktop app
- Enterprise model restriction capabilities added via `availableModels` setting

## New Claude Code versions

### [2.1.42](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/versions/2.1.42.md)

#### Existing feature improvements

* Improved startup performance by deferring Zod schema construction
* Improved prompt cache hit rates by moving date out of system prompt
* Improved `/resume` to show cleaner session titles instead of interrupt messages

#### Major bug fixes

* Fixed image dimension limit errors to suggest `/compact`

-----

## Claude Code changes

### New Documents

#### [Desktop quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/desktop-quickstart.md) [[Source](https://code.claude.com/docs/en/desktop-quickstart)]

New streamlined quickstart guide for the Claude Code Desktop app. Covers installation steps for macOS, Windows x64, and Windows ARM64. Guides users through their first session including choosing an environment (Local/Remote/SSH), selecting a folder and model, and reviewing changes in Ask mode. Includes practical next steps like interrupting Claude, adding context with @-mentions and file attachments, using skills, reviewing changes with diff view, adjusting permission modes, installing plugins, working with parallel sessions, and sending long-running tasks to the cloud. Also includes a CLI comparison section for users familiar with the terminal version.

### Changed documents

#### [Agent teams](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

* Added visual diagrams comparing subagent vs agent team architectures in both light and dark modes. [[lines 29-32](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/agent-teams.md?plain=1#L29-L32)] [[Source](https://code.claude.com/docs/en/agent-teams#compare-with-subagents)]

#### [Best practices](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

* Updated reference from "Claude Desktop" to "Claude Code desktop app" for consistency. [[line 520](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/best-practices.md?plain=1#L520)] [[Source](https://code.claude.com/docs/en/best-practices#run-multiple-claude-sessions)]

#### [Chrome integration](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/chrome.md) [[Source](https://code.claude.com/docs/en/chrome)]

* Corrected subscription plan reference from "Team" to "Teams". [[line 27](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/chrome.md?plain=1#L27)] [[Source](https://code.claude.com/docs/en/chrome#prerequisites)]

#### [Use Claude Code Desktop](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

Major restructure and expansion of the Desktop documentation:

* Changed page title from "Claude Code on desktop" to "Use Claude Code Desktop" and removed preview status. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/desktop.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/desktop)]
* Reorganized into clear sections: Start a session, Work with code, Manage sessions, Extend Claude Code, and Environment configuration. [[line 7](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/desktop.md?plain=1#L7)] [[Source](https://code.claude.com/docs/en/desktop)]
* Added detailed "Start a session" section explaining environment, project folder, model, and permission mode selection. [[lines 11-20](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/desktop.md?plain=1#L11-L20)] [[Source](https://code.claude.com/docs/en/desktop#start-a-session)]
* Expanded permission modes documentation with detailed table showing Ask, Code, Plan, and Act modes with their settings keys and behaviors. [[lines 35-48](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/desktop.md?plain=1#L35-L48)] [[Source](https://code.claude.com/docs/en/desktop#add-files-and-context-to-prompts)]
* Added comprehensive diff view section explaining how to review changes, add line comments, and submit feedback with keyboard shortcuts (Cmd+Enter on macOS, Ctrl+Enter on Windows). [[lines 52-63](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/desktop.md?plain=1#L52-L63)] [[Source](https://code.claude.com/docs/en/desktop#choose-a-permission-mode)]
* Enhanced parallel sessions documentation with details on worktree storage location customization, branch prefix configuration, and session filtering. [[lines 70-78](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/desktop.md?plain=1#L70-L78)] [[Source](https://code.claude.com/docs/en/desktop#work-in-parallel-with-sessions)]
* Added "Continue in another surface" section documenting the new ability to hand off sessions to Claude Code on the Web or your IDE. [[lines 84-89](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/desktop.md?plain=1#L84-L89)] [[Source](https://code.claude.com/docs/en/desktop#continue-in-another-surface)]
* Expanded connectors section with management instructions and clarification that connectors are MCP servers with graphical setup. [[lines 96-100](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/desktop.md?plain=1#L96-L100)] [[Source](https://code.claude.com/docs/en/desktop#connect-external-tools)]
* Added comprehensive plugins section covering installation, management, and scoping (user/project/local-only). [[lines 107-109](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/desktop.md?plain=1#L107-L109)] [[Source](https://code.claude.com/docs/en/desktop#install-plugins)]
* Added environment configuration section distinguishing Local, Remote, and SSH environments. [[lines 111-123](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/desktop.md?plain=1#L111-L123)] [[Source](https://code.claude.com/docs/en/desktop#install-plugins)]

#### [Interactive mode](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Added new `/desktop` command that hands off the current CLI session to the Claude Code Desktop app (macOS and Windows only). [[line 102](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/interactive-mode.md?plain=1#L102)] [[Source](https://code.claude.com/docs/en/interactive-mode#built-in-commands)]

#### [Model configuration](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Added comprehensive "Restrict model selection" section documenting the new `availableModels` setting for enterprise administrators to control which models users can select. [[lines 71-123](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/model-config.md?plain=1#L71-L123)] [[Source](https://code.claude.com/docs/en/model-config#restrict-model-selection)]
* Documented Default model behavior showing that Max/Team/Pro subscribers get Opus 4.6 while pay-as-you-go users get Sonnet 4.5. [[lines 81-90](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/model-config.md?plain=1#L81-L90)] [[Source](https://code.claude.com/docs/en/model-config#restrict-model-selection)]
* Explained how to combine `availableModels` with `model` setting to fully control the model experience. [[lines 92-119](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/model-config.md?plain=1#L92-L119)] [[Source](https://code.claude.com/docs/en/model-config#default-model-behavior)]

#### [Network configuration](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/network-config.md) [[Source](https://code.claude.com/docs/en/network-config)]

* Simplified required URLs list to three essential endpoints: `api.anthropic.com` for Claude API, `claude.ai` for claude.ai account authentication, and `platform.claude.com` for Anthropic Console account authentication. [[lines 93-96](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/network-config.md?plain=1#L93-L96)] [[Source](https://code.claude.com/docs/en/network-config#network-access-requirements)]

#### [Overview](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/overview.md) [[Source](https://code.claude.com/docs/en/overview)]

* Added Windows ARM64 download link with note that it supports remote sessions only. [[line 111](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/overview.md?plain=1#L111)] [[Source](https://code.claude.com/docs/en/overview#get-started)]
* Added clarification that Desktop app requires a paid subscription. [[line 113](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/overview.md?plain=1#L113)] [[Source](https://code.claude.com/docs/en/overview#get-started)]
* Expanded "Work from anywhere" section to describe session handoff capabilities between different surfaces using `/teleport` and `/desktop` commands. [[lines 194-198](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/overview.md?plain=1#L194-L198)] [[Source](https://code.claude.com/docs/en/overview#what-you-can-do)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `availableModels` setting to the settings reference table with description and example. [[line 151](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/settings.md?plain=1#L151)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

#### [Slack integration](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/slack.md) [[Source](https://code.claude.com/docs/en/slack)]

* Corrected subscription plan reference from "Team" to "Teams" in requirements table. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/claude-code/slack.md?plain=1#L19)] [[Source](https://code.claude.com/docs/en/slack#prerequisites)]

-----

## API changes

### Changed documents

#### [Adaptive thinking](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/api/build-with-claude/adaptive-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

* Updated obfuscated email address in sales team contact link. [[line 170](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/api/build-with-claude/adaptive-thinking.md?plain=1#L170)] [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

#### [Extended thinking](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Updated obfuscated email address in sales team contact link. [[line 105](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L105)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

#### [Files](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Updated obfuscated email address in contact link for higher file API limits. [[line 284](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/api/build-with-claude/files.md?plain=1#L284)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

#### [Remote MCP servers](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Added Razorpay MCP server for Razorpay Dashboard Assistant functionality at `https://mcp.razorpay.com/mcp`. [[lines 651-656](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L651-L656)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
* Added Common Room MCP server for querying contacts and accounts at `https://mcp.commonroom.io/mcp`. [[lines 827-832](https://github.com/gpambrozio/ClaudeDocs/blob/936a08c51511a0621ae2b86bb9d6b56ace055db8/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L827-L832)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
