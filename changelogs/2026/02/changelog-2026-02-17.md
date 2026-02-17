# [Claude docs changes for February 17th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/9278972ee954289fb73ce58a32ad48ce141d4b46) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/9278972ee954289fb73ce58a32ad48ce141d4b46)]

## Executive Summary
- Plugin marketplace documentation greatly expanded with new sections on plugin sources, strict mode behavior, and version resolution/release channels
- Two new remote MCP servers added: Microsoft Learn and MSCI
- Jailbreak mitigation docs updated: model recommendation changed to Claude Haiku 4.5 and structured outputs now recommended for classification responses
- Claude Code version 2.1.43 fixes AWS auth refresh hang and structured-outputs header issues on Vertex/Bedrock

## New Claude Code versions

### [2.1.43](https://github.com/gpambrozio/ClaudeDocs/blob/9278972ee954289fb73ce58a32ad48ce141d4b46/versions/2.1.43.md)

#### Major bug fixes

* Fixed AWS auth refresh hanging indefinitely by adding a 3-minute timeout
* Fixed spurious warnings for non-agent markdown files in `.claude/agents/` directory
* Fixed structured-outputs beta header being sent unconditionally on Vertex/Bedrock

### [2.1.44](https://github.com/gpambrozio/ClaudeDocs/blob/9278972ee954289fb73ce58a32ad48ce141d4b46/versions/2.1.44.md)

#### Major bug fixes

* Fixed ENAMETOOLONG errors for deeply-nested directory paths
* Fixed auth refresh errors

-----

## Claude Code changes

### Changed documents

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/9278972ee954289fb73ce58a32ad48ce141d4b46/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Added Microsoft Learn as a new remote MCP server for searching trusted Microsoft documentation. [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/9278972ee954289fb73ce58a32ad48ce141d4b46)]

#### [Overview](https://github.com/gpambrozio/ClaudeDocs/blob/9278972ee954289fb73ce58a32ad48ce141d4b46/docs-md/claude-code/overview.md) [[Source](https://code.claude.com/docs/en/overview)]

* Updated product description: Claude Code is now described as an "AI-powered coding assistant that helps you build features, fix bugs, and automate development tasks" rather than "an agentic coding tool that reads your codebase, edits files, and runs commands."

#### [Plugin marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/9278972ee954289fb73ce58a32ad48ce141d4b46/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Clarified `strict` field description: now explains that `true` makes `plugin.json` the authority for component definitions (with marketplace entry able to supplement), while `false` means the marketplace entry defines everything. [[line 248](https://github.com/gpambrozio/ClaudeDocs/blob/9278972ee954289fb73ce58a32ad48ce141d4b46/docs-md/claude-code/plugin-marketplaces.md?plain=1#L248)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#optional-plugin-fields)]
* Added new "Plugin sources" section with a reference table listing all supported source types (relative path, github, url, npm, pip) and their fields. [[lines 262-281](https://github.com/gpambrozio/ClaudeDocs/blob/9278972ee954289fb73ce58a32ad48ce141d4b46/docs-md/claude-code/plugin-marketplaces.md?plain=1#L262-L281)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#plugin-sources)]
* Added clarification distinguishing marketplace sources (where to fetch `marketplace.json`) from plugin sources (where to fetch individual plugins), with a concrete example. [[lines 283-292](https://github.com/gpambrozio/ClaudeDocs/blob/9278972ee954289fb73ce58a32ad48ce141d4b46/docs-md/claude-code/plugin-marketplaces.md?plain=1#L283-L292)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#relative-paths)]
* Added a dedicated "Strict mode" section explaining the behavior of `strict: true` vs `strict: false` in detail, including when to use each. [[lines 448-463](https://github.com/gpambrozio/ClaudeDocs/blob/9278972ee954289fb73ce58a32ad48ce141d4b46/docs-md/claude-code/plugin-marketplaces.md?plain=1#L448-L463)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#advanced-plugin-entries)]
* Added new "Version resolution and release channels" section explaining how plugin versions determine cache paths and update detection, plus guidance on setting up stable/latest release channels via separate marketplaces. [[lines 657-764](https://github.com/gpambrozio/ClaudeDocs/blob/9278972ee954289fb73ce58a32ad48ce141d4b46/docs-md/claude-code/plugin-marketplaces.md?plain=1#L657-L764)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#how-restrictions-work)]
* Simplified external dependency guidance: removed "Option 2: Restructure your marketplace" approach, leaving only symlinks as the recommended solution for accessing files outside the plugin directory.

#### [Plugins reference](https://github.com/gpambrozio/ClaudeDocs/blob/9278972ee954289fb73ce58a32ad48ce141d4b46/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* Clarified that marketplace plugins are installed to `~/.claude/plugins/cache` and that `--plugin-dir` plugins are only available for the duration of a session. [[lines 406-412](https://github.com/gpambrozio/ClaudeDocs/blob/9278972ee954289fb73ce58a32ad48ce141d4b46/docs-md/claude-code/plugins-reference.md?plain=1#L406-L412)] [[Source](https://code.claude.com/docs/en/plugins-reference#plugin-caching-and-file-resolution)]
* Added note that version bumps in `plugin.json` are required for cached plugins to propagate updates to existing users, with guidance for marketplace-managed versions. [[lines 772-773](https://github.com/gpambrozio/ClaudeDocs/blob/9278972ee954289fb73ce58a32ad48ce141d4b46/docs-md/claude-code/plugins-reference.md?plain=1#L772-L773)] [[Source](https://code.claude.com/docs/en/plugins-reference#version-management)]

-----

## API changes

### Changed documents

#### [Adaptive thinking](https://github.com/gpambrozio/ClaudeDocs/blob/9278972ee954289fb73ce58a32ad48ce141d4b46/docs-md/api/build-with-claude/adaptive-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

* Updated obfuscated email link for contacting sales about full thinking output for Claude 4 models (no content change, URL encoding updated).

#### [Extended thinking](https://github.com/gpambrozio/ClaudeDocs/blob/9278972ee954289fb73ce58a32ad48ce141d4b46/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Updated obfuscated email link for contacting sales about full thinking output for Claude 4 models (no content change, URL encoding updated).

#### [Files](https://github.com/gpambrozio/ClaudeDocs/blob/9278972ee954289fb73ce58a32ad48ce141d4b46/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Updated obfuscated email link for contacting support about higher rate limits (no content change, URL encoding updated).

#### [Mitigate jailbreaks](https://github.com/gpambrozio/ClaudeDocs/blob/9278972ee954289fb73ce58a32ad48ce141d4b46/docs-md/api/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks.md) [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)]

* Removed claim that Claude is "far more resistant to jailbreaking than other major LLMs, thanks to Constitutional AI."
* Updated harmlessness screen recommendation from Claude Haiku 3 to Claude Haiku 4.5, and added recommendation to use structured outputs to constrain classifier responses to a simple classification. [[lines 7-8](https://github.com/gpambrozio/ClaudeDocs/blob/9278972ee954289fb73ce58a32ad48ce141d4b46/docs-md/api/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks.md?plain=1#L7-L8)] [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)]

#### [Remote MCP servers](https://github.com/gpambrozio/ClaudeDocs/blob/9278972ee954289fb73ce58a32ad48ce141d4b46/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Added Microsoft Learn as a new remote MCP server for searching trusted Microsoft documentation (`https://learn.microsoft.com/api/mcp`). [[lines 559-565](https://github.com/gpambrozio/ClaudeDocs/blob/9278972ee954289fb73ce58a32ad48ce141d4b46/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L559-L565)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
* Added MSCI as a new remote MCP server for querying MSCI indexes (`https://mcp.msci.com/index/index-mcp/v1.0/mcp`). [[lines 599-605](https://github.com/gpambrozio/ClaudeDocs/blob/9278972ee954289fb73ce58a32ad48ce141d4b46/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L599-L605)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
