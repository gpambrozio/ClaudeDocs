# [Claude docs changes for January 24th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/826b462865bf19e7b86ce6a69ecafee8da759ae3) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/826b462865bf19e7b86ce6a69ecafee8da759ae3)]

## Executive Summary
- New versions 2.1.18-2.1.19: Customizable keyboard shortcuts with chord sequences and `$0`/`$1` argument shorthands for skills
- Skills without extra permissions no longer require user approval before execution
- Many new MCP servers added and code intelligence plugins documentation expanded with LSP tool support

## Detailed Changes

## New Claude Code versions

### [2.1.18](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/versions/2.1.18.md)

#### New features

* Added customizable keyboard shortcuts with support for context-specific keybindings and chord sequences. Run `/keybindings` to configure.

### [2.1.19](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/versions/2.1.19.md)

#### New features

* Added environment variable `CLAUDE_CODE_ENABLE_TASKS` to allow reverting to the old system temporarily by setting to `false`
* Added shorthand `$0`, `$1`, etc. for accessing individual arguments in custom commands
* [SDK] Added replay of `queued_command` attachment messages as `SDKUserMessageReplay` events when `replayUserMessages` is enabled
* [VSCode] Enabled session forking and rewind functionality for all users

#### Existing feature improvements

* Changed skills without additional permissions or hooks to be allowed without requiring approval
* Changed indexed argument syntax from `$ARGUMENTS.0` to `$ARGUMENTS[0]` (bracket syntax)

#### Major bug fixes

* Fixed crashes on processors without AVX instruction support
* Fixed dangling Claude Code processes when terminal is closed by catching EIO errors from `process.exit()` and using SIGKILL as fallback
* Fixed `/rename` and `/tag` not updating the correct session when resuming from a different directory (e.g., git worktrees)
* Fixed resuming sessions by custom title not working when run from a different directory
* Fixed pasted text content being lost when using prompt stash (Ctrl+S) and restore
* Fixed agent list displaying "Sonnet (default)" instead of "Inherit (default)" for agents without an explicit model setting
* Fixed backgrounded hook commands not returning early, potentially causing the session to wait on a process that was intentionally backgrounded
* Fixed file write preview omitting empty lines

-----

## Claude Code changes

### Changed documents

#### [best-practices](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

* Added recommendation to install code intelligence plugins for typed languages to give Claude precise symbol navigation and automatic error detection after edits. [[line 329](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/best-practices.md?plain=1#L329)] [[Source](https://code.claude.com/docs/en/best-practices#install-plugins)]

#### [common-workflows](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Added tip to install code intelligence plugins for precise "go to definition" and "find references" navigation when exploring the codebase. [[line 125](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/common-workflows.md?plain=1#L125)] [[Source](https://code.claude.com/docs/en/common-workflows#find-relevant-code)]

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* Added new section on installing code intelligence plugins for typed languages, explaining how they reduce token usage by providing precise symbol navigation instead of text-based search and reporting type errors automatically after edits. [[lines 88-90](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/costs.md?plain=1#L88-L90)] [[Source](https://code.claude.com/docs/en/costs#install-code-intelligence-plugins-for-typed-languages)]

#### [discover-plugins](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* Updated code intelligence plugins description to clarify they enable Claude Code's built-in LSP tool. [[line 43](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/discover-plugins.md?plain=1#L43)] [[Source](https://code.claude.com/docs/en/discover-plugins#code-intelligence)]
* Added Kotlin language server (`kotlin-lsp`) to the code intelligence plugins table. [[line 52](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/discover-plugins.md?plain=1#L52)] [[Source](https://code.claude.com/docs/en/discover-plugins#code-intelligence)]
* Added new section explaining what Claude gains from code intelligence plugins: automatic diagnostics after file edits and code navigation capabilities. [[lines 64-71](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/discover-plugins.md?plain=1#L64-L71)] [[Source](https://code.claude.com/docs/en/discover-plugins#what-claude-gains-from-code-intelligence-plugins)]
* Added code intelligence troubleshooting section covering language server startup issues, high memory usage, and false positive diagnostics in monorepos. [[lines 434-438](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/discover-plugins.md?plain=1#L434-L438)] [[Source](https://code.claude.com/docs/en/discover-plugins#code-intelligence-issues)]

#### [github-actions](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/github-actions.md) [[Source](https://code.claude.com/docs/en/github-actions)]

* Changed `custom_instructions` parameter mapping from `--system-prompt` to `--append-system-prompt` in the breaking changes reference and examples. [[lines 79, 117](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/github-actions.md?plain=1#L79)]

#### [how-claude-code-works](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/how-claude-code-works.md) [[Source](https://code.claude.com/docs/en/how-claude-code-works)]

* Added new "Code intelligence" category to the built-in tools table, describing type error detection, jump to definitions, and find references capabilities (requires code intelligence plugins). [[line 31](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/how-claude-code-works.md?plain=1#L31)] [[Source](https://code.claude.com/docs/en/how-claude-code-works#tools)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Replaced "Explorium Business Data Hub" with "Harmonic" MCP server for discovering, researching, and enriching companies and people. [[lines 79-83](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/mcp.md?plain=1#L79-L83)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* Added new "VibeProspecting" MCP server for finding company & contact data. [[lines 103-106](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/mcp.md?plain=1#L103-L106)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* Added new "Ahrefs" MCP server for SEO & AI search analytics. [[lines 149-152](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/mcp.md?plain=1#L149-L152)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* Added new "AirOps" MCP server for crafting content that wins AI search. [[lines 154-157](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/mcp.md?plain=1#L154-L157)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* Added new "Amplitude" MCP server for searching, accessing, and getting insights on Amplitude data. [[lines 159-162](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/mcp.md?plain=1#L159-L162)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* Added new "Pigment" MCP server for analyzing business data. [[lines 377-378](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/mcp.md?plain=1#L377-L378)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* Added new "Similarweb Website Traffic" MCP server for real-time web analytics & competitive intelligence. [[lines 387-390](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/mcp.md?plain=1#L387-L390)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* Added new "WordPress.com" MCP server for secure AI access to manage WordPress.com sites. [[lines 443-446](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/mcp.md?plain=1#L443-L446)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]

#### [microsoft-foundry](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/microsoft-foundry.md) [[Source](https://code.claude.com/docs/en/microsoft-foundry)]

* Updated `ANTHROPIC_FOUNDRY_BASE_URL` example to include `/anthropic` suffix in the URL path. [[line 70](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/microsoft-foundry.md?plain=1#L70)] [[Source](https://code.claude.com/docs/en/microsoft-foundry#3-configure-claude-code)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `ANTHROPIC_FOUNDRY_BASE_URL` environment variable for specifying full base URL for Foundry resource as alternative to `ANTHROPIC_FOUNDRY_RESOURCE`. [[line 851](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/settings.md?plain=1#L851)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]
* Added `ANTHROPIC_FOUNDRY_RESOURCE` environment variable documentation explaining it's required if `ANTHROPIC_FOUNDRY_BASE_URL` is not set. [[line 852](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/settings.md?plain=1#L852)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]
* Added `CLAUDE_CODE_ENABLE_TELEMETRY` environment variable for enabling OpenTelemetry data collection. [[line 874](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/settings.md?plain=1#L874)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]
* Added LSP tool to the tools available to Claude, describing automatic diagnostics and code navigation capabilities requiring code intelligence plugins. [[line 945](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/claude-code/settings.md?plain=1#L945)] [[Source](https://code.claude.com/docs/en/settings#tools-available-to-claude)]

-----

## API changes

### Changed documents

#### [agents-and-tools/remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Replaced "Explorium Business Data Hub" with "Harmonic" MCP server for discovering, researching, and enriching companies and people. [[lines 55-61](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L55-L61)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
* Added new "VibeProspecting" MCP server for finding company & contact data. [[lines 95-101](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L95-L101)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
* Added new "Ahrefs" MCP server for SEO & AI search analytics. [[lines 165-171](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L165-L171)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
* Added new "AirOps" MCP server for crafting content that wins AI search. [[lines 173-179](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L173-L179)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
* Added new "Pigment" MCP server for analyzing business data. [[lines 519-523](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L519-L523)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
* Added new "Similarweb Website Traffic" MCP server for real-time web analytics & competitive intelligence. [[lines 541-547](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L541-L547)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
* Added new "WordPress.com" MCP server for secure AI access to manage WordPress.com sites. [[lines 609-615](https://github.com/gpambrozio/ClaudeDocs/blob/826b462865bf19e7b86ce6a69ecafee8da759ae3/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L609-L615)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
