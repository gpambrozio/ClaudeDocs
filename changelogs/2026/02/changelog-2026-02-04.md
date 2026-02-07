# [Claude docs changes for February 4th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/255fdf63c18994351939908df4c19216e0b64f64) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/255fdf63c18994351939908df4c19216e0b64f64)]

## Executive Summary
- New versions 2.1.30-2.1.31: PDF page-range reading, `/debug` command, and pre-configured OAuth for MCP servers
- Session sharing documentation added with visibility options for Enterprise/Teams and Max/Pro accounts
- New Zero Data Retention (ZDR) documentation covering eligible endpoints, limitations, and special cases

## Detailed Changes

## New Claude Code versions

### [2.1.30](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/versions/2.1.30.md)

#### New features

* Added `pages` parameter to the Read tool for PDFs, allowing specific page ranges to be read. Large PDFs (>10 pages) now return a lightweight reference when @ mentioned instead of being inlined into context.
* Added `/debug` command for Claude to help troubleshoot the current session
* Added pre-configured OAuth client credentials for MCP servers that don't support Dynamic Client Registration (e.g., Slack). Use `--client-id` and `--client-secret` with `claude mcp add`.

#### Existing feature improvements

* Added support for additional `git log` and `git show` flags in read-only mode (e.g., `--topo-order`, `--cherry-pick`, `--format`, `--raw`)
* Added token count, tool uses, and duration metrics to Task tool results
* Added reduced motion mode to the config
* Improved memory usage for `--resume` (68% reduction for users with many sessions) by replacing the session index with lightweight stat-based loading and progressive enrichment
* Improved `TaskStop` tool to display the stopped command/task description in the result line instead of a generic "Task stopped" message
* Improved system prompts to more clearly guide the model toward using dedicated tools (Read, Edit, Glob, Grep) instead of bash equivalents
* Changed `/model` to execute immediately instead of being queued
* [VSCode] Added multiline input support to the "Other" text input in question dialogs (use Shift+Enter for new lines)

#### Major bug fixes

* Fixed phantom "(no content)" text blocks appearing in API conversation history, reducing token waste and potential model confusion
* Fixed prompt cache not correctly invalidating when tool descriptions or input schemas changed, only when tool names changed
* Fixed 400 errors that could occur after running `/login` when the conversation contained thinking blocks
* Fixed a hang when resuming sessions with corrupted transcript files containing `parentUuid` cycles
* Fixed rate limit message showing incorrect "/upgrade" suggestion for Max 20x users when extra-usage is unavailable
* Fixed permission dialogs stealing focus while actively typing
* Fixed subagents not being able to access SDK-provided MCP tools because they were not synced to the shared application state
* Fixed a regression where Windows users with a `.bashrc` file could not run bash commands
* [VSCode] Fixed duplicate sessions appearing in the session list when starting a new conversation

### [2.1.31](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/versions/2.1.31.md)

#### New features

* Added session resume hint on exit, showing how to continue your conversation later
* Added support for full-width (zenkaku) space input from Japanese IME in checkbox selection

#### Existing feature improvements

* Improved system prompts to more clearly guide the model toward using dedicated tools (Read, Edit, Glob, Grep) instead of bash equivalents (`cat`, `sed`, `grep`, `find`), reducing unnecessary bash command usage
* Improved PDF and request size error messages to show actual limits (100 pages, 20MB)
* Reduced layout jitter in the terminal when the spinner appears and disappears during streaming
* Removed misleading Anthropic API pricing from model selector for third-party provider (Bedrock, Vertex, Foundry) users

#### Major bug fixes

* Fixed PDF too large errors permanently locking up sessions, requiring users to start a new conversation
* Fixed bash commands incorrectly reporting failure with "Read-only file system" errors when sandbox mode was enabled
* Fixed a crash that made sessions unusable after entering plan mode when project config in `~/.claude.json` was missing default fields
* Fixed `temperatureOverride` being silently ignored in the streaming API path, causing all streaming requests to use the default temperature (1) regardless of the configured override
* Fixed LSP shutdown/exit compatibility with strict language servers that reject null params

-----

## Claude Code changes

### New Documents

### Changed documents

#### [Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Updated links to point to new Agent SDK documentation paths. [[line 28](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/amazon-bedrock.md?plain=1#L28)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#2-configure-aws-credentials)]

#### [Best practices](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

* Updated link to Agent SDK documentation. [[line 109](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/best-practices.md?plain=1#L109)] [[Source](https://code.claude.com/docs/en/best-practices#explore-first-then-plan-then-code)]

#### [Claude Code on the web](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* Added documentation for sharing web sessions, including different visibility options for Enterprise/Teams accounts (Private and Team) and Max/Pro accounts (Private and Public). [[lines 147-172](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L147-L172)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#sharing-sessions)]
* Updated allowed domains for "Limited" network access mode, changing docs.claude.com to platform.claude.com. [[line 346](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L346)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#anthropic-services)]

#### [CLI reference](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Updated links to point to new Agent SDK documentation paths instead of old docs.claude.com URLs. [[lines 43, 55, 166](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/cli-reference.md?plain=1#L43)]

#### [Common workflows](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Updated links to Agent SDK documentation paths. [[lines 82, 128, 207](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/common-workflows.md?plain=1#L82)]

#### [Data usage](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/data-usage.md) [[Source](https://code.claude.com/docs/en/data-usage)]

* Updated link to Agent SDK sessions documentation. [[line 103](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/data-usage.md?plain=1#L103)] [[Source](https://code.claude.com/docs/en/data-usage#default-behaviors-by-api-provider)]

#### [Discover plugins](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* Updated link to Agent SDK documentation. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/discover-plugins.md?plain=1#L15)] [[Source](https://code.claude.com/docs/en/discover-plugins#how-marketplaces-work)]

#### [GitHub Actions](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/github-actions.md) [[Source](https://code.claude.com/docs/en/github-actions)]

* Updated links to Agent SDK documentation paths. [[lines 37, 165, 168, 262](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/github-actions.md?plain=1#L37)]

#### [GitLab CI/CD](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/gitlab-ci-cd.md) [[Source](https://code.claude.com/docs/en/gitlab-ci-cd)]

* Updated links to Agent SDK documentation paths. [[lines 32, 211](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/gitlab-ci-cd.md?plain=1#L32)]

#### [Google Vertex AI](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/google-vertex-ai.md) [[Source](https://code.claude.com/docs/en/google-vertex-ai)]

* Updated links to Agent SDK documentation paths. [[lines 28, 44](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/google-vertex-ai.md?plain=1#L28)]

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Updated links to Agent SDK documentation paths. [[lines 106, 292](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/hooks.md?plain=1#L106)]

#### [How Claude Code works](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/how-claude-code-works.md) [[Source](https://code.claude.com/docs/en/how-claude-code-works)]

* Updated link to Agent SDK documentation. [[line 42](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/how-claude-code-works.md?plain=1#L42)] [[Source](https://code.claude.com/docs/en/how-claude-code-works#tools)]

#### [Index](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/index.md) [[Source](https://code.claude.com/docs/en/index)]

* Updated domain references from docs.claude.com to platform.claude.com. [[line 108](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/index.md?plain=1#L108)] [[Source](https://code.claude.com/docs/en/index#use-claude-code-everywhere)]

#### [Keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* Updated link to Agent SDK documentation. [[line 148](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/keybindings.md?plain=1#L148)] [[Source](https://code.claude.com/docs/en/keybindings#transcript-actions)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Removed extensive list of remote MCP server examples (similar to API documentation changes), keeping only a link to find more servers on GitHub. [[lines 25+](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/mcp.md?plain=1#L25)]

#### [Model config](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Updated link to Agent SDK documentation. [[line 70](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/model-config.md?plain=1#L70)] [[Source](https://code.claude.com/docs/en/model-config#default-model-setting)]

#### [Overview](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/overview.md) [[Source](https://code.claude.com/docs/en/overview)]

* Updated domain references from docs.claude.com to platform.claude.com. [[line 23](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/overview.md?plain=1#L23)] [[Source](https://code.claude.com/docs/en/overview#get-started-in-30-seconds)]

#### [Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Updated link to Agent SDK documentation. [[line 161](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/permissions.md?plain=1#L161)] [[Source](https://code.claude.com/docs/en/permissions#task-subagents)]

#### [Plugin marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Updated link to Agent SDK documentation. [[line 39](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/plugin-marketplaces.md?plain=1#L39)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#walkthrough-create-a-local-marketplace)]

#### [Quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/quickstart.md) [[Source](https://code.claude.com/docs/en/quickstart)]

* Fixed anchor links in section headers to use hyphens instead of colons throughout the document. [[lines 15, 75, 105, 122, 188, 209, 255, 285](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/quickstart.md?plain=1#L15)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Updated link to Agent SDK documentation. [[line 92](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/settings.md?plain=1#L92)] [[Source](https://code.claude.com/docs/en/settings#settings-files)]

#### [Setup](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* Expanded and improved system requirements documentation with better formatting for operating systems and platform-specific setup instructions. [[lines 2-8](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/setup.md?plain=1#L2-L8)] [[Source](https://code.claude.com/docs/en/setup#system-requirements)]
* Added dedicated "Platform-specific setup" section with detailed instructions for Windows and Alpine Linux. [[lines 94-107](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/setup.md?plain=1#L94-L107)] [[Source](https://code.claude.com/docs/en/setup#platform-specific-setup)]

#### [Skills](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Fixed anchor link formatting in heading. [[line 425](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/skills.md?plain=1#L425)] [[Source](https://code.claude.com/docs/en/skills#example-research-skill-using-explore-agent)]

#### [Slack](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/slack.md) [[Source](https://code.claude.com/docs/en/slack)]

* Added documentation clarifying that Slack sessions have Team visibility by default and explaining visibility options. [[lines 82-98](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/slack.md?plain=1#L82-L98)] [[Source](https://code.claude.com/docs/en/slack#context-gathering)]

#### [Sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Updated link to Agent SDK documentation. [[line 57](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/sub-agents.md?plain=1#L57)] [[Source](https://code.claude.com/docs/en/sub-agents#built-in-subagents)]

#### [Troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/troubleshooting.md) [[Source](https://code.claude.com/docs/en/troubleshooting)]

* Updated links to Agent SDK documentation paths. [[lines 113, 139, 185, 235](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/claude-code/troubleshooting.md?plain=1#L113)]

-----

## API changes

### New Documents

#### [Zero Data Retention (ZDR)](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/api/build-with-claude/zero-data-retention.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/zero-data-retention)]

New comprehensive documentation about Zero Data Retention policies, including what endpoints and features are ZDR-eligible, important limitations, and special cases. Details coverage for the Messages API, Token Counting API, and explains why Batch API, Files API, Skills, and Context Management are not ZDR-eligible. Includes sections on CORS limitations, Claude Code eligibility based on authentication method, and FAQs about ZDR arrangements.

### Changed documents

#### [Remote MCP servers](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Removed extensive list of remote MCP server examples, keeping only a link to find more servers on GitHub. This simplifies the documentation and points users to the canonical server list. [[lines 23+](https://github.com/gpambrozio/ClaudeDocs/blob/255fdf63c18994351939908df4c19216e0b64f64/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L23)]
