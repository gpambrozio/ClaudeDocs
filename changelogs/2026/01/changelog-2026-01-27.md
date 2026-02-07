# [Claude docs changes for January 27th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/f8ead63199aed809a84306c64f9a77b278e6f9f1) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/f8ead63199aed809a84306c64f9a77b278e6f9f1)]

## Executive Summary
- New version 2.1.20: PR review status indicators in prompt footer, CLAUDE.md loading from additional directories, and task deletion
- Numerous UI improvements including shimmer animation for thinking status and vim arrow key history navigation
- New wildcard permission syntax documented and checkpoints became available in CLI

## Detailed Changes

## New Claude Code versions

### [2.1.20](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/versions/2.1.20.md)

#### New features

* Added arrow key history navigation in vim normal mode when cursor cannot move further
* Added external editor shortcut (Ctrl+G) to the help menu for better discoverability
* Added PR review status indicator to the prompt footer, showing the current branch's PR state (approved, changes requested, pending, or draft) as a colored dot with a clickable link
* Added support for loading `CLAUDE.md` files from additional directories specified via `--add-dir` flag (requires setting `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1`)
* Added ability to delete tasks via the `TaskUpdate` tool

#### Existing feature improvements

* Improved `/sandbox` command UI to show dependency status with installation instructions when dependencies are missing
* Improved thinking status text with a subtle shimmer animation
* Improved task list to dynamically adjust visible items based on terminal height
* Improved fork conversation hint to show how to resume the original session
* Changed collapsed read/search groups to show present tense ("Reading", "Searching for") while in progress, and past tense ("Read", "Searched for") when complete
* Changed `ToolSearch` results to appear as a brief notification instead of inline in the conversation
* Changed the `/commit-push-pr` skill to automatically post PR URLs to Slack channels when configured via MCP tools
* Changed the `/copy` command to be available to all users
* Changed background agents to prompt for tool permissions before launching
* Changed permission rules like `Bash(*)` to be accepted and treated as equivalent to `Bash`
* Changed config backups to be timestamped and rotated (keeping 5 most recent) to prevent data loss

#### Major bug fixes

* Fixed session compaction issues that could cause resume to load full history instead of the compact summary
* Fixed agents sometimes ignoring user messages sent while actively working on a task
* Fixed wide character (emoji, CJK) rendering artifacts where trailing columns were not cleared when replaced by narrower characters
* Fixed JSON parsing errors when MCP tool responses contain special Unicode characters
* Fixed up/down arrow keys in multi-line and wrapped text input to prioritize cursor movement over history navigation
* Fixed draft prompt being lost when pressing UP arrow to navigate command history
* Fixed ghost text flickering when typing slash commands mid-input
* Fixed marketplace source removal not properly deleting settings
* Fixed duplicate output in some commands like `/context`
* Fixed task list sometimes showing outside the main conversation view
* Fixed syntax highlighting for diffs occurring within multiline constructs like Python docstrings
* Fixed crashes when cancelling tool use

-----

## Claude Code changes

### Changed documents

#### [Best practices](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

* Added note about using Ctrl+G to open the plan in your text editor for direct editing before Claude proceeds. [[line 75](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/best-practices.md?plain=1#L75)] [[Source](https://code.claude.com/docs/en/best-practices#explore-first,-then-plan,-then-code)]

#### [Common workflows](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Added note about using Ctrl+G to open the plan in your default text editor for direct editing before Claude proceeds. [[line 391](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/common-workflows.md?plain=1#L391)] [[Source](https://code.claude.com/docs/en/common-workflows#example:-planning-a-complex-refactor)]

#### [IDE integrations](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* Updated the comparison table to show that checkpoints are now available in CLI (previously "Coming soon"). [[line 227](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/ide-integrations.md?plain=1#L227)] [[Source](https://code.claude.com/docs/en/ide-integrations#vs-code-extension-vs-claude-code-cli)]
* Added new section "Rewind with checkpoints" explaining how checkpoints work in VS Code extension with three options for rewinding. [[lines 231-239](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/ide-integrations.md?plain=1#L231-L239)] [[Source](https://code.claude.com/docs/en/ide-integrations#rewind-with-checkpoints)]

#### [Interactive mode](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Added note about reverting to the previous TODO list by setting `CLAUDE_CODE_ENABLE_TASKS=false`. [[line 261](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/interactive-mode.md?plain=1#L261)] [[Source](https://code.claude.com/docs/en/interactive-mode#task-list)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Added Box MCP server for searching, accessing and getting insights on Box content. [[lines 213-217](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/mcp.md?plain=1#L213-L217)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* Added Clay MCP server for finding prospects, researching accounts, and personalizing outreach. [[lines 237-241](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/mcp.md?plain=1#L237-L241)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* Updated Figma description to include "Generate diagrams and better code from Figma context" (previously just "Create better code with Figma context"). [[line 285](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/mcp.md?plain=1#L285)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* Updated Similarweb name from "Similarweb Website Traffic" to just "Similarweb" and description to "Real time web, mobile app, and market data." [[lines 399-401](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/mcp.md?plain=1#L399-L401)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]

#### [Overview](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/overview.md) [[Source](https://code.claude.com/docs/en/overview)]

* Added new section "Use Claude Code everywhere" with links to different interfaces: Terminal, Web, Desktop app, VS Code, JetBrains, GitHub Actions, GitLab CI/CD, Slack, and Chrome. [[lines 95-107](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/overview.md?plain=1#L95-L107)] [[Source](https://code.claude.com/docs/en/overview#use-claude-code-everywhere)]
* Updated "Next steps" section to link to Desktop app instead of IDE setup, with updated description. [[lines 117-119](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/overview.md?plain=1#L117-L119)] [[Source](https://code.claude.com/docs/en/overview#next-steps)]

#### [Plugin marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Updated private repository documentation to explain that manual installation uses git credential helpers, while background auto-updates need environment tokens. [[lines 432-433](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/plugin-marketplaces.md?plain=1#L432-L433)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#private-repositories)]
* Added example showing how to use `hostPattern` source type to allow all marketplaces from an internal git server using regex pattern matching. [[lines 557-571](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/plugin-marketplaces.md?plain=1#L557-L571)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#common-configurations)]
* Updated "How restrictions work" section to note that `hostPattern` sources use regex matching while other sources use exact matching. [[lines 575-581](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/plugin-marketplaces.md?plain=1#L575-L581)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#how-restrictions-work)]
* Updated troubleshooting section for private repository authentication to separate manual installation from background auto-updates. [[lines 672-687](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/plugin-marketplaces.md?plain=1#L672-L687)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#private-repository-authentication-fails)]

#### [Quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/quickstart.md) [[Source](https://code.claude.com/docs/en/quickstart)]

* Added note that Claude Code is available through supported cloud providers. [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/quickstart.md?plain=1#L11)] [[Source](https://code.claude.com/docs/en/quickstart#before-you-begin)]
* Added paragraph explaining Claude Code is available on multiple interfaces beyond terminal CLI. [[line 13](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/quickstart.md?plain=1#L13)] [[Source](https://code.claude.com/docs/en/quickstart#before-you-begin)]
* Updated authentication section to mention Amazon Bedrock, Google Vertex AI, and Microsoft Foundry as third-party cloud providers. [[line 101](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/quickstart.md?plain=1#L101)] [[Source](https://code.claude.com/docs/en/quickstart#step-2:-log-in-to-your-account)]
* Removed all `>` prompts from code examples to match standard command-line format. [[multiple lines](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/quickstart.md?plain=1#L131)]
* Added "Pro tips for beginners" link to best practices and common workflows. [[line 350](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/quickstart.md?plain=1#L350)] [[Source](https://code.claude.com/docs/en/quickstart#pro-tips-for-beginners)]
* Updated "What's next" section with new links to "How Claude Code works", "Best practices", and "Extend Claude Code" instead of CLI reference and configuration. [[lines 401-409](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/quickstart.md?plain=1#L401-L409)] [[Source](https://code.claude.com/docs/en/quickstart#what’s-next)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `hostPattern` as a new source type for marketplace restrictions using regex pattern matching. [[line 599](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/settings.md?plain=1#L599)] [[Source](https://code.claude.com/docs/en/settings#extraknownmarketplaces)]
* Updated `strictKnownMarketplaces` description to note it uses exact matching except for `hostPattern` which uses regex. [[line 615](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/settings.md?plain=1#L615)] [[Source](https://code.claude.com/docs/en/settings#strictknownmarketplaces)]
* Updated supported source types count from six to seven. [[line 624](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/settings.md?plain=1#L624)] [[Source](https://code.claude.com/docs/en/settings#strictknownmarketplaces)]
* Added detailed documentation for host pattern matching source type with examples and host extraction rules. [[lines 708-726](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/settings.md?plain=1#L708-L726)] [[Source](https://code.claude.com/docs/en/settings#strictknownmarketplaces)]
* Added configuration example showing how to allow all marketplaces from an internal git server using hostPattern. [[lines 771-785](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/settings.md?plain=1#L771-L785)] [[Source](https://code.claude.com/docs/en/settings#strictknownmarketplaces)]
* Added `CLAUDE_CODE_ENABLE_TASKS` environment variable documentation for reverting to previous TODO list. [[line 913](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/settings.md?plain=1#L913)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]

#### [Skills](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Added `$ARGUMENTS[N]` variable for accessing specific arguments by 0-based index. [[line 205](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/skills.md?plain=1#L205)] [[Source](https://code.claude.com/docs/en/skills#available-string-substitutions)]
* Added `$N` variable as shorthand for `$ARGUMENTS[N]`. [[line 206](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/skills.md?plain=1#L206)] [[Source](https://code.claude.com/docs/en/skills#available-string-substitutions)]
* Added examples showing how to use `$ARGUMENTS[N]` and `$N` for positional argument access in skills. [[lines 339-368](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/skills.md?plain=1#L339-L368)] [[Source](https://code.claude.com/docs/en/skills#pass-arguments-to-skills)]
* Added clarification that skills with `allowed-tools` grant Claude access to those tools without per-use approval when the skill is active. [[line 459](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/skills.md?plain=1#L459)] [[Source](https://code.claude.com/docs/en/skills#restrict-claude’s-skill-access)]

#### [VS Code](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Updated comparison table to show that checkpoints are now available in CLI (previously "Coming soon"). [[line 227](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/vs-code.md?plain=1#L227)] [[Source](https://code.claude.com/docs/en/vs-code#vs-code-extension-vs-claude-code-cli)]
* Added new section "Rewind with checkpoints" explaining how checkpoints work in VS Code extension with three options for rewinding. [[lines 231-239](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/claude-code/vs-code.md?plain=1#L231-L239)] [[Source](https://code.claude.com/docs/en/vs-code#rewind-with-checkpoints)]

-----

## API changes

### Changed documents

#### [Remote MCP servers](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Added Clay remote MCP server for finding prospects, researching accounts, and personalizing outreach. [[lines 251-256](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L251-L256)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
* Updated Figma description to include "Generate diagrams and better code from Figma context". [[line 331](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L331)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
* Updated Similarweb name from "Similarweb Website Traffic" to just "Similarweb" and description to "Real time web, mobile app, and market data." [[lines 549-551](https://github.com/gpambrozio/ClaudeDocs/blob/f8ead63199aed809a84306c64f9a77b278e6f9f1/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L549-L551)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
