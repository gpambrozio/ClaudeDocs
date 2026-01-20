# [Claude docs changes for January 20th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/d281186446990ece703c03d3c219b0638c1a4a7d) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/d281186446990ece703c03d3c219b0638c1a4a7d)]

## Claude Code changes

### Changed documents

#### [common-workflows](https://github.com/gpambrozio/ClaudeDocs/blob/d281186446990ece703c03d3c219b0638c1a4a7d/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Added documentation for Ctrl+G keyboard shortcut to open default text editor when providing custom responses to Claude's questions. [[line 437](https://github.com/gpambrozio/ClaudeDocs/blob/d281186446990ece703c03d3c219b0638c1a4a7d/docs-md/claude-code/common-workflows.md?plain=1#L437)] [[Source](https://code.claude.com/docs/en/common-workflows#let-claude-interview-you)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/d281186446990ece703c03d3c219b0638c1a4a7d/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Added Ctrl+G keyboard shortcut to general controls for opening default text editor when editing prompts or custom responses. [[line 17](https://github.com/gpambrozio/ClaudeDocs/blob/d281186446990ece703c03d3c219b0638c1a4a7d/docs-md/claude-code/interactive-mode.md?plain=1#L17)] [[Source](https://code.claude.com/docs/en/interactive-mode#general-controls)]
* Fixed tool name from BashOutput to TaskOutput for retrieving background task output. [[line 178](https://github.com/gpambrozio/ClaudeDocs/blob/d281186446990ece703c03d3c219b0638c1a4a7d/docs-md/claude-code/interactive-mode.md?plain=1#L178)] [[Source](https://code.claude.com/docs/en/interactive-mode#how-backgrounding-works)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/d281186446990ece703c03d3c219b0638c1a4a7d/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Updated introduction to explain that Skills can bundle scripts in any language (Python, Node.js, Bash, etc.) for advanced capabilities like generating interactive visualizations, querying databases, processing files, calling APIs, and producing reports. [[lines 3-4](https://github.com/gpambrozio/ClaudeDocs/blob/d281186446990ece703c03d3c219b0638c1a4a7d/docs-md/claude-code/skills.md?plain=1#L3-L4)] [[Source](https://code.claude.com/docs/en/skills)]
* Added new "Generate visual output" section demonstrating how to create an interactive codebase visualizer Skill that uses a bundled Python script to generate an HTML tree view with collapsible directories, file sizes, and color-coded file types. [[line 559](https://github.com/gpambrozio/ClaudeDocs/blob/d281186446990ece703c03d3c219b0638c1a4a7d/docs-md/claude-code/skills.md?plain=1#L559)] [[Source](https://code.claude.com/docs/en/skills#generate-visual-output)]

#### [slash-commands](https://github.com/gpambrozio/ClaudeDocs/blob/d281186446990ece703c03d3c219b0638c1a4a7d/docs-md/claude-code/slash-commands.md) [[Source](https://code.claude.com/docs/en/slash-commands)]

* Expanded /doctor command description to detail its diagnostic capabilities including checking installation health, configuration issues (invalid settings, MCP errors, keybinding problems), and context usage warnings (large CLAUDE.md files, high MCP token usage). [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/d281186446990ece703c03d3c219b0638c1a4a7d/docs-md/claude-code/slash-commands.md?plain=1#L14)] [[Source](https://code.claude.com/docs/en/slash-commands#built-in-slash-commands)]

#### [troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/d281186446990ece703c03d3c219b0638c1a4a7d/docs-md/claude-code/troubleshooting.md) [[Source](https://code.claude.com/docs/en/troubleshooting)]

* Expanded /doctor diagnostics documentation with detailed list of checks performed: installation type/version/search functionality, auto-update status, invalid settings files, MCP server configuration errors, keybinding configuration problems, context usage warnings, and plugin/agent loading errors. [[lines 425-432](https://github.com/gpambrozio/ClaudeDocs/blob/d281186446990ece703c03d3c219b0638c1a4a7d/docs-md/claude-code/troubleshooting.md?plain=1#L425-L432)] [[Source](https://code.claude.com/docs/en/troubleshooting#getting-more-help)]
