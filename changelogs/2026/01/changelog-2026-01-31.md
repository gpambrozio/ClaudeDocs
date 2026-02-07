# [Claude docs changes for January 31st, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/74a62ca8d633775e9b075f04454fe2ab8837a224) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/74a62ca8d633775e9b075f04454fe2ab8837a224)]

## Executive Summary
- New version 2.1.27: Added `--from-pr` flag to resume sessions linked to GitHub PRs with automatic PR linking
- Hooks system received a complete documentation rewrite with new prompt-based and agent-based hook types
- New MCP servers added: Google BigQuery, LILT, Make, Wyndham Hotels

## New Claude Code versions

### [2.1.27](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/versions/2.1.27.md)

#### New features

* Added `--from-pr` flag to resume sessions linked to a specific GitHub PR number or URL
* Sessions are now automatically linked to PRs when created via `gh pr create`

#### Existing feature improvements

* Added tool call failures and denials to debug logs
* Windows: Improved bash command execution for users with `.bashrc` files
* Windows: Reduced console windows flashing when spawning child processes

#### Major bug fixes

* Fixed context management validation error for gateway users, ensuring `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` avoids the error
* Fixed /context command not displaying colored output
* Fixed status bar duplicating background task indicator when PR status was shown
* VSCode: Fixed OAuth token expiration causing 401 errors after extended sessions

-----

## Claude Code changes

### Changed documents

#### [Analytics](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/analytics.md) [[Source](https://code.claude.com/docs/en/analytics)]

* Added clarification that contribution metrics only cover users within your claude.ai organization. Usage through the Claude Console API or third-party integrations is not included. [[line 22](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/analytics.md?plain=1#L22)] [[Source](https://code.claude.com/docs/en/analytics#enable-contribution-metrics)]
* Added disclaimer that metrics are deliberately conservative and represent an underestimate of Claude Code's actual impact. [[line 60](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/analytics.md?plain=1#L60)] [[Source](https://code.claude.com/docs/en/analytics#review-summary-metrics)]

#### [CLI reference](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Added new `--from-pr` flag to resume sessions linked to a specific GitHub PR. Accepts a PR number or URL. Sessions are automatically linked when created via `gh pr create`. [[line 37](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/cli-reference.md?plain=1#L37)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [Common workflows](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Added documentation for automatic PR session linking: when you create a PR using `gh pr create`, the session is automatically linked to that PR and can be resumed later with `claude --from-pr <number>`. [[line 520](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/common-workflows.md?plain=1#L520)] [[Source](https://code.claude.com/docs/en/common-workflows#create-pull-requests)]
* Added `claude --from-pr 123` as a new option for resuming sessions linked to a specific pull request. [[line 780](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/common-workflows.md?plain=1#L780)] [[Source](https://code.claude.com/docs/en/common-workflows#resume-previous-conversations)]

#### [Features overview](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/features-overview.md) [[Source](https://code.claude.com/docs/en/features-overview)]

* Expanded hooks description to clarify they fire at specific lifecycle events like tool execution, session boundaries, prompt submission, permission requests, and compaction. [[line 151](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/features-overview.md?plain=1#L151)] [[Source](https://code.claude.com/docs/en/features-overview#understand-how-features-load)]
* Updated hooks link title from "Run scripts on Claude Code events" to "Automate workflows with hooks" and changed target to hooks-guide.md. [[line 169](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/features-overview.md?plain=1#L169)] [[Source](https://code.claude.com/docs/en/features-overview#learn-more)]

#### [Headless](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* Added new section on streaming responses with `--output-format stream-json`, `--verbose`, and `--include-partial-messages` flags. [[lines 89-112](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/headless.md?plain=1#L89-L112)] [[Source](https://code.claude.com/docs/en/headless#stream-responses)]
* Included example of using `jq` to filter for text deltas and display streaming text. [[lines 89-112](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/headless.md?plain=1#L89-L112)] [[Source](https://code.claude.com/docs/en/headless#stream-responses)]

#### [Hooks guide](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Complete page restructure: Changed title from "Get started with Claude Code hooks" to "Automate workflows with hooks"
* Added new introduction explaining that hooks can be prompt-based or agent-based, not just shell commands
* Added new walkthrough section with step-by-step first hook setup
* Reorganized examples into common patterns: notifications, auto-formatting, protected file blocking, and context re-injection
* Added new "How hooks work" section explaining event firing and hook types
* Added new sections on hook input/output, matchers, and configuration locations
* Added documentation for prompt-based hooks and agent-based hooks
* Added new troubleshooting section with common issues and solutions

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Complete page rewrite repositioned as reference documentation instead of getting started guide
* Added new "How a hook resolves" section with detailed flow diagram explanation
* Expanded configuration section with three-level nesting explanation (event → matcher → handler)
* Added new matcher patterns section with comprehensive table of event-specific matchers
* Added new hook handler fields section documenting command, prompt, and agent hook types
* Added new sections for: Match MCP tools, Reference scripts by path, Hook input and output with JSON schemas, Exit code output behavior
* Removed `Setup` event from the hook lifecycle
* Added `Notification` event to hook lifecycle table

#### [Interactive mode](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Added "Purple: merged" to the PR status indicator colors. [[line 274](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/interactive-mode.md?plain=1#L274)] [[Source](https://code.claude.com/docs/en/interactive-mode#pr-review-status)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Removed Granola MCP server from the list
* Added Google Cloud BigQuery MCP server with add command
* Added LILT MCP server with add command
* Added Make MCP server with add command
* Added Wyndham Hotels and Resorts MCP server with add command

#### [Plugins](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/plugins.md) [[Source](https://code.claude.com/docs/en/plugins)]

* Updated hook example to show hooks receive JSON on stdin: changed from `"command": "npm run lint:fix $FILE"` to using `jq` to extract file path from JSON input: `"command": "jq -r '.tool_input.file_path' | xargs npm run lint:fix"`. [[line 428](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/plugins.md?plain=1#L428)] [[Source](https://code.claude.com/docs/en/plugins#migration-steps)]

#### [Plugins reference](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* Removed `Setup` event from the list of supported hook events in plugins. [[line 117](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/plugins-reference.md?plain=1#L117)] [[Source](https://code.claude.com/docs/en/plugins-reference#hooks)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added new `network.allowAllUnixSockets` setting: "Allow all Unix socket connections in sandbox. Default: false". [[line 259](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/settings.md?plain=1#L259)] [[Source](https://code.claude.com/docs/en/settings#sandbox-settings)]
* Added new `network.allowedDomains` setting: "Array of domains to allow for outbound network traffic. Supports wildcards (e.g., `*.example.com`)". [[line 261](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/settings.md?plain=1#L261)] [[Source](https://code.claude.com/docs/en/settings#sandbox-settings)]
* Clarified ANTHROPIC_CUSTOM_HEADERS environment variable: added "newline-separated for multiple headers" to the description. [[line 868](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/settings.md?plain=1#L868)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]

#### [Skills](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Updated hooks reference link from generic "Hooks" to specific "Hooks in skills and agents" section. [[line 196](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/skills.md?plain=1#L196)] [[Source](https://code.claude.com/docs/en/skills#frontmatter-reference)]

#### [Sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Clarified that all hook events are supported in subagents. [[line 379](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/sub-agents.md?plain=1#L379)] [[Source](https://code.claude.com/docs/en/sub-agents#hooks-in-subagent-frontmatter)]
* Added explanation to Stop event: "When the subagent finishes (converted to `SubagentStop` at runtime)". [[line 385](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/sub-agents.md?plain=1#L385)] [[Source](https://code.claude.com/docs/en/sub-agents#hooks-in-subagent-frontmatter)]
* Clarified SubagentStop matcher behavior: "`SubagentStop` fires for all subagent completions regardless of matcher values". [[line 420](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/sub-agents.md?plain=1#L420)] [[Source](https://code.claude.com/docs/en/sub-agents#project-level-hooks-for-subagent-events)]

#### [Troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/troubleshooting.md) [[Source](https://code.claude.com/docs/en/troubleshooting)]

* Updated hook example link from generic "markdown formatting hook example" to specific "Auto-format code after edits" section reference. [[line 425](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/claude-code/troubleshooting.md?plain=1#L425)] [[Source](https://code.claude.com/docs/en/troubleshooting#missing-language-tags-in-code-blocks)]

-----

## API changes

### Changed documents

#### [Remote MCP servers](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Removed Granola MCP server from the list. [[line 63](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L63)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
* Added Google Cloud BigQuery MCP server: "BigQuery: Advanced analytical insights for agents" (URL: `https://bigquery.googleapis.com/mcp`). [[line 367](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L367)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
* Added LILT MCP server: "High-quality translation with human verification" (URL: `https://mcp.lilt.com/mcp`). [[line 455](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L455)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
* Added Make MCP server: "Run Make scenarios and manage your Make account" (URL: `https://mcp.make.com`). [[line 471](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L471)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
* Added Wyndham Hotels and Resorts MCP server: "Discover the right Wyndham Hotel for you, faster" (URL: `https://mcp.wyndhamhotels.com/claude/mcp`). [[line 679](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L679)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

#### [Text editor tool](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/api/agents-and-tools/tool-use/text-editor-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool)]

* Corrected parameter name from `new_str` to `insert_text` for the insert command. [[line 160](https://github.com/gpambrozio/ClaudeDocs/blob/74a62ca8d633775e9b075f04454fe2ab8837a224/docs-md/api/agents-and-tools/tool-use/text-editor-tool.md?plain=1#L160)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool)]
