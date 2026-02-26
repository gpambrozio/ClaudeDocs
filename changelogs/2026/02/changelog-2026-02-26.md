# [Claude docs changes for February 26th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/28c9bd521d905bb031dfa9f0f3472da93655eafe) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/28c9bd521d905bb031dfa9f0f3472da93655eafe)]

## Executive Summary
- Auto-memory is now enabled by default in Claude Code, replacing the previous gradual rollout. Users can toggle it via `/memory` or configure it with the new `autoMemoryEnabled` setting.
- The `/copy` command now shows an interactive picker when code blocks are present, allowing selection of individual code blocks or the full response.
- Structured outputs now document property ordering behavior: required properties always appear before optional properties in output objects.
- Multiple critical bug fixes in 2.1.59: MCP OAuth token refresh race condition, config file corruption, and missing error messages when the working directory is deleted.

## New Claude Code versions

### [2.1.58](https://github.com/gpambrozio/ClaudeDocs/blob/28c9bd521d905bb031dfa9f0f3472da93655eafe/versions/2.1.58.md)

#### New features

* Expanded Remote Control to more users

### [2.1.59](https://github.com/gpambrozio/ClaudeDocs/blob/28c9bd521d905bb031dfa9f0f3472da93655eafe/versions/2.1.59.md)

#### New features

* Claude automatically saves useful context to auto-memory — manage with `/memory`
* Added `/copy` command interactive picker: when code blocks are present, allows selection of individual code blocks or the full response

#### Existing feature improvements

* Improved "always allow" prefix suggestions for compound bash commands (e.g. `cd /tmp && git fetch && git push`) to compute smarter per-subcommand prefixes instead of treating the whole command as one
* Improved ordering of short task lists
* Improved memory usage in multi-agent sessions by releasing completed subagent task state

#### Major bug fixes

* Fixed MCP OAuth token refresh race condition when running multiple Claude Code instances simultaneously
* Fixed shell commands not showing a clear error message when the working directory has been deleted
* Fixed config file corruption that could wipe authentication when multiple Claude Code instances ran simultaneously

-----

## Claude Code changes

### Changed documents

#### [Discover Plugins](https://github.com/gpambrozio/ClaudeDocs/blob/28c9bd521d905bb031dfa9f0f3472da93655eafe/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* Added a code example showing how to configure `extraKnownMarketplaces` in the project's `.claude/settings.json` for team marketplace setup. [[line ~450](https://github.com/gpambrozio/ClaudeDocs/blob/28c9bd521d905bb031dfa9f0f3472da93655eafe/docs-md/claude-code/discover-plugins.md?plain=1#L450)]

#### [Interactive Mode](https://github.com/gpambrozio/ClaudeDocs/blob/28c9bd521d905bb031dfa9f0f3472da93655eafe/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Updated `/copy` command description: now shows an interactive picker when code blocks are present, allowing selection of individual code blocks or the full response. [[line ~100](https://github.com/gpambrozio/ClaudeDocs/blob/28c9bd521d905bb031dfa9f0f3472da93655eafe/docs-md/claude-code/interactive-mode.md?plain=1#L100)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/28c9bd521d905bb031dfa9f0f3472da93655eafe/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* MCP server list reorganized with entries reordered. Smartsheet documentation link updated to the new help article URL.

#### [Memory](https://github.com/gpambrozio/ClaudeDocs/blob/28c9bd521d905bb031dfa9f0f3472da93655eafe/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Auto-memory is now enabled by default (previously was rolling out gradually). [[line ~31](https://github.com/gpambrozio/ClaudeDocs/blob/28c9bd521d905bb031dfa9f0f3472da93655eafe/docs-md/claude-code/memory.md?plain=1#L31)]
* The `/memory` selector now includes an auto-memory toggle to turn the feature on or off. [[line ~71](https://github.com/gpambrozio/ClaudeDocs/blob/28c9bd521d905bb031dfa9f0f3472da93655eafe/docs-md/claude-code/memory.md?plain=1#L71)]
* New `autoMemoryEnabled` setting added to both user-level (`~/.claude/settings.json`) and project-level (`.claude/settings.json`) to control auto-memory. [[lines ~73-90](https://github.com/gpambrozio/ClaudeDocs/blob/28c9bd521d905bb031dfa9f0f3472da93655eafe/docs-md/claude-code/memory.md?plain=1#L73)]
* Documented that `CLAUDE_CODE_DISABLE_AUTO_MEMORY` environment variable takes precedence over both the toggle and `settings.json`, making it useful for CI/managed environments. [[line ~95](https://github.com/gpambrozio/ClaudeDocs/blob/28c9bd521d905bb031dfa9f0f3472da93655eafe/docs-md/claude-code/memory.md?plain=1#L95)]

-----

## API changes

### Changed documents

#### [MCP Connector](https://github.com/gpambrozio/ClaudeDocs/blob/28c9bd521d905bb031dfa9f0f3472da93655eafe/docs-md/api/agents-and-tools/mcp-connector.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)]

* Minor code formatting improvements to JSON examples (no substantive content changes).

#### [Remote MCP Servers](https://github.com/gpambrozio/ClaudeDocs/blob/28c9bd521d905bb031dfa9f0f3472da93655eafe/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* MCP server list reorganized with many entries reordered. New servers added: LSEG (financial data and analytics), MSCI (index data and analytics), and Common Room (contacts and accounts intelligence).

#### [Structured Outputs](https://github.com/gpambrozio/ClaudeDocs/blob/28c9bd521d905bb031dfa9f0f3472da93655eafe/docs-md/api/build-with-claude/structured-outputs.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

* New "Property ordering" section added: documents that required properties always appear before optional properties in structured output objects, regardless of their order in the schema definition. Includes example schema and resulting output ordering. [[lines ~401-445](https://github.com/gpambrozio/ClaudeDocs/blob/28c9bd521d905bb031dfa9f0f3472da93655eafe/docs-md/api/build-with-claude/structured-outputs.md?plain=1#L401)]
