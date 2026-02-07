# [Claude docs changes for January 19th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b)]

## Executive Summary
- Clarified permission rule syntax for `--allowedTools` flag and `Bash(*)` vs `Bash` matching behavior
- New MCP server integrations added: Gamma, Guru, Klaviyo, Wix, Port IO, and Hex
- Comprehensive 'Permission rule syntax' section added to settings documentation

## Claude Code changes

### Changed documents

#### [CLI Reference](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* The `--allowedTools` flag description now references the permission rule syntax documentation for pattern matching details. [[line 25](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/claude-code/cli-reference.md?plain=1#L25)] [[Source](https://code.claude.com/docs/en/cli-reference#flags)]

#### [Headless](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* Added explanation that `--allowedTools` flag uses permission rule syntax, with `:*` suffix enabling prefix matching for command patterns. [[lines 115-116](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/claude-code/headless.md?plain=1#L115-L116)] [[Source](https://code.claude.com/docs/en/headless#non-interactive-mode)]

#### [Identity and Access Management (IAM)](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/claude-code/iam.md) [[Source](https://code.claude.com/docs/en/iam)]

* Clarified rule evaluation order: deny rules are checked first, then ask, then allow rules, with the first match winning. [[line 72](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/claude-code/iam.md?plain=1#L72)] [[Source](https://code.claude.com/docs/en/iam#configuring-permissions)]
* Added note that `Bash(*)` does not match all Bash commands; use `Bash` without parentheses to match all uses. [[line 78](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/claude-code/iam.md?plain=1#L78)] [[Source](https://code.claude.com/docs/en/iam#configuring-permissions)]
* Added reference to permission rule syntax documentation in settings for wildcard patterns. [[line 80](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/claude-code/iam.md?plain=1#L80)] [[Source](https://code.claude.com/docs/en/iam#configuring-permissions)]

#### [MCP Servers](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Added Gamma MCP server for creating presentations, docs, socials, and sites. [[lines 109-112](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/claude-code/mcp.md?plain=1#L109-L112)] [[Source](https://code.claude.com/docs/en/mcp#marketing-productivity)]
* Fixed Atlassian MCP server URL from `/v1/sse` to `/v1/mcp`. [[line 153](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/claude-code/mcp.md?plain=1#L153)] [[Source](https://code.claude.com/docs/en/mcp#work-communication)]
* Added Guru MCP server for searching and interacting with company knowledge. [[lines 259-262](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/claude-code/mcp.md?plain=1#L259-L262)] [[Source](https://code.claude.com/docs/en/mcp#work-communication)]
* Added Klaviyo MCP server for reporting, strategizing, and creating with real-time Klaviyo data. [[lines 299-302](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/claude-code/mcp.md?plain=1#L299-L302)] [[Source](https://code.claude.com/docs/en/mcp#marketplaces-servers)]
* Added Wix MCP server for managing and building sites and apps on Wix. [[lines 397-400](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/claude-code/mcp.md?plain=1#L397-L400)] [[Source](https://code.claude.com/docs/en/mcp#data-analytics)]
* Added Port IO MCP server for searching context lake and safely running actions. [[lines 459-462](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/claude-code/mcp.md?plain=1#L459-L462)] [[Source](https://code.claude.com/docs/en/mcp#data-analytics)]
* Added Hex MCP server entry with public URL for answering questions with Hex agent. [[lines 491-494](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/claude-code/mcp.md?plain=1#L491-L494)] [[Source](https://code.claude.com/docs/en/mcp#data-analytics)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added comprehensive "Permission rule syntax" section documenting rule evaluation order, matching all uses of a tool, using specifiers, and wildcard patterns. [[lines 177-265](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/claude-code/settings.md?plain=1#L177-L265)] [[Source](https://code.claude.com/docs/en/settings#permission-rule-syntax)]
* Updated permission settings table to reference the new permission rule syntax section. [[lines 170-172](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/claude-code/settings.md?plain=1#L170-L172)] [[Source](https://code.claude.com/docs/en/settings#permissions)]
* Updated "See also" section to include more specific references to IAM documentation sections. [[lines 1021-1023](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/claude-code/settings.md?plain=1#L1021-L1023)] [[Source](https://code.claude.com/docs/en/settings#see-also)]

-----

## API changes

### Changed documents

#### [Remote MCP Servers](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Added Gamma MCP server for creating presentations, docs, socials, and sites. [[lines 111-116](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L111-L116)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers#marketing-productivity)]
* Added Guru MCP server for searching and interacting with company knowledge. [[lines 313-318](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L313-L318)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers#work-communication)]
* Added Klaviyo MCP server for reporting, strategizing, and creating with real-time Klaviyo data. [[lines 399-404](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L399-L404)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers#marketplaces-servers)]
* Added Wix MCP server for managing and building sites and apps on Wix. [[lines 555-560](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L555-L560)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers#data-analytics)]
* Added Port IO MCP server for searching context lake and safely running actions. [[lines 643-648](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L643-L648)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers#data-analytics)]
* Added Hex MCP server entry with public URL for answering questions with Hex agent. [[lines 695-700](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L695-L700)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers#data-analytics)]

#### [Extended thinking](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Changed contact link for full thinking output access from email protection link to direct sales email. [[line 98](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L98)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#summarized-thinking)]

#### [Files](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Changed contact link from direct sales email to email protection link for requesting higher rate limits. [[line 284](https://github.com/gpambrozio/ClaudeDocs/blob/987d53584e3bbce9cd839afaa1d8f87cc75d6a3b/docs-md/api/build-with-claude/files.md?plain=1#L284)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files#rate-limits)]
