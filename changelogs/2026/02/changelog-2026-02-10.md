# [Claude docs changes for February 10th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/30ee630fb2aa3c23c18f76749b00276906741246) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/30ee630fb2aa3c23c18f76749b00276906741246)]

## Executive Summary
- Complete redesign of overview and index pages with tabbed environment selection for easier onboarding
- New CLAUDE.md documentation explaining how to provide project-specific instructions to Claude Code
- Added Act mode to desktop app, enabling fully autonomous operation in trusted environments
- Version 2.1.38 released with multiple bug fixes including VS Code terminal scrolling and Tab key autocomplete

## New Claude Code versions

### [2.1.38](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/versions/2.1.38.md)

#### Major bug fixes

* Fixed VS Code terminal scroll-to-top regression introduced in 2.1.37
* Fixed Tab key queueing slash commands instead of autocompleting
* Fixed bash permission matching for commands using environment variable wrappers
* Fixed text between tool uses disappearing when not using streaming
* Fixed duplicate sessions when resuming in VS Code extension
* Improved heredoc delimiter parsing to prevent command smuggling
* Blocked writes to `.claude/skills` directory in sandbox mode

-----

## Claude Code changes

### New Documents

#### [CLAUDE.md](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/claude-code/claude-md.md) [[Source](https://code.claude.com/docs/en/claude-md)]

New documentation page explaining CLAUDE.md files - markdown files placed in project roots that Claude Code reads at the start of every session. Use them to set coding standards, architecture decisions, preferred libraries, and review checklists. The page currently shows as a 404 error but provides links to related documentation on skills, best practices, and memory.

### Changed documents

#### [Claude Code on the web](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* Clarified availability for Enterprise users: now explicitly states "Enterprise users with premium seats or Chat + Claude Code seats" instead of just "Enterprise premium seat users". [[line 25](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L25)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#who-can-use-claude-code-on-the-web)]
* Added new section explaining that custom environment images and snapshots are not yet supported, with SessionStart hooks as a workaround. [[lines 250-251](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L250-L251)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#dependency-management)]
* Updated SessionStart hook example to include `CLAUDE_CODE_REMOTE` environment variable check, allowing hooks to execute only in remote environments. [[lines 283-285](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L283-L285)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#dependency-management)]
* Added new "Dependency management limitations" section documenting four key limitations: hooks fire for all sessions, requires network access, proxy compatibility issues, and runs on every session start. [[lines 301-305](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L301-L305)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#dependency-management-limitations)]

#### [Desktop](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Added new "Act" mode to the mode selector documentation, which runs without permission checks and automatically executes file edits and terminal commands. [[lines 103-106](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/claude-code/desktop.md?plain=1#L103-L106)] [[Source](https://code.claude.com/docs/en/desktop#choose-a-permission-mode)]
* Added explanation that Act mode runs in `bypassPermissions` mode and should only be used in isolated environments like containers or VMs. Documented that it requires admin enablement for Team/Enterprise and personal settings enablement for personal accounts. [[line 106](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/claude-code/desktop.md?plain=1#L106)] [[Source](https://code.claude.com/docs/en/desktop#choose-a-permission-mode)]

#### [Claude Code overview](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/claude-code/overview.md) [[Source](https://code.claude.com/docs/en/overview)]

* Complete page restructure: Changed from simple prerequisites and installation instructions to a comprehensive overview with tabbed environment selection (Terminal, VS Code, Desktop app, Web, JetBrains). [[lines 1-85](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/claude-code/overview.md?plain=1#L1-L85)] [[Source](https://code.claude.com/docs/en/overview)]
* Replaced "What Claude Code does for you" and "Why developers love Claude Code" sections with new "What you can do" section featuring practical use cases with code examples. [[lines 87-141](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/claude-code/overview.md?plain=1#L87-L141)] [[Source](https://code.claude.com/docs/en/overview#get-started)]
* Added new content sections: "Automate the work you keep putting off", "Build features and fix bugs", "Create commits and pull requests", "Connect your tools with MCP", "Customize with instructions, skills, and hooks", "Run agent teams and build custom agents", "Pipe, script, and automate with the CLI", and "Work from anywhere". [[lines 89-158](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/claude-code/overview.md?plain=1#L89-L158)] [[Source](https://code.claude.com/docs/en/overview#get-started)]
* Restructured "Use Claude Code everywhere" section into a comparison table showing best options for different use cases. [[lines 163-170](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/claude-code/overview.md?plain=1#L163-L170)] [[Source](https://code.claude.com/docs/en/overview#what-you-can-do)]
* Simplified "Next steps" section from multiple linked cards to a bulleted list with Quickstart, best practices, settings, troubleshooting, and code.claude.com links. [[lines 175-180](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/claude-code/overview.md?plain=1#L175-L180)] [[Source](https://code.claude.com/docs/en/overview#what-you-can-do)]

#### [index](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/claude-code/index.md) [[Source](https://code.claude.com/docs/en/index)]

* Identical restructuring to overview.md - the index and overview pages now share the same comprehensive content with tabbed environment selection and practical use cases. [[lines 1-180](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/claude-code/index.md?plain=1#L1-L180)] [[Source](https://code.claude.com/docs/en/index)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Fixed Blockscout MCP server URL by removing trailing slash. [[line 211](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/claude-code/mcp.md?plain=1#L211)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* Updated Workato documentation link from `/mcp/mcp-cloud.html` to `/mcp.html`. [[line 531](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/claude-code/mcp.md?plain=1#L531)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]

-----

## API changes

### Changed documents

#### [Adaptive thinking](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/api/build-with-claude/adaptive-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

* Updated sales team contact email address. [[line 172](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/api/build-with-claude/adaptive-thinking.md?plain=1#L172)] [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

#### [Extended thinking](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Updated sales team contact email address. [[line 105](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L105)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

#### [Files](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Updated contact email address for requesting higher file API limits. [[line 284](https://github.com/gpambrozio/ClaudeDocs/blob/30ee630fb2aa3c23c18f76749b00276906741246/docs-md/api/build-with-claude/files.md?plain=1#L284)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]
