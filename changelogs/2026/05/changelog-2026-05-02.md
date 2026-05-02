# [Claude docs changes for May 2nd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/35e4e957bc7b38337e01e44065cf37d4a9600571) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/35e4e957bc7b38337e01e44065cf37d4a9600571)]

## Executive Summary
- Claude Managed Agents sessions are now visible in the Console with a timeline view, tool execution details, and debugging tips
- Claude Managed Agents does not support the `inference_geo` parameter and is not covered by Zero Data Retention (ZDR)
- The `agents` field in the plugin manifest now accepts an array instead of a directory string, enabling more granular agent file targeting

-----

## Claude Code changes

### Changed documents

#### [Desktop](https://github.com/gpambrozio/ClaudeDocs/blob/35e4e957bc7b38337e01e44065cf37d4a9600571/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Clarified that on Linux, users should use the CLI instead of the desktop app, with a direct link to the CLI quickstart. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/35e4e957bc7b38337e01e44065cf37d4a9600571/docs-md/claude-code/desktop.md?plain=1#L19)] [[Source](https://code.claude.com/docs/en/desktop)]

#### [Desktop Quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/35e4e957bc7b38337e01e44065cf37d4a9600571/docs-md/claude-code/desktop-quickstart.md) [[Source](https://code.claude.com/docs/en/desktop-quickstart)]

* Clarified that on Linux, users should use the CLI instead of the desktop app, with a direct link to the CLI quickstart. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/35e4e957bc7b38337e01e44065cf37d4a9600571/docs-md/claude-code/desktop-quickstart.md?plain=1#L19)] [[Source](https://code.claude.com/docs/en/desktop-quickstart)]

#### [Environment Variables](https://github.com/gpambrozio/ClaudeDocs/blob/35e4e957bc7b38337e01e44065cf37d4a9600571/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Expanded `CLAUDE_CODE_SHELL_PREFIX` description to clarify it wraps Bash tool calls, hook commands, and stdio MCP server startup commands (not just bash commands). [[line 137](https://github.com/gpambrozio/ClaudeDocs/blob/35e4e957bc7b38337e01e44065cf37d4a9600571/docs-md/claude-code/env-vars.md?plain=1#L137)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [Plugins Reference](https://github.com/gpambrozio/ClaudeDocs/blob/35e4e957bc7b38337e01e44065cf37d4a9600571/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* The `agents` field in the plugin manifest now takes an array of file paths (e.g. `["./custom/agents/reviewer.md"]`) instead of a directory string. [[line 352](https://github.com/gpambrozio/ClaudeDocs/blob/35e4e957bc7b38337e01e44065cf37d4a9600571/docs-md/claude-code/plugins-reference.md?plain=1#L352)] [[Source](https://code.claude.com/docs/en/plugins-reference#complete-schema)]

-----

## API changes

### Changed documents

#### [API and Data Retention](https://github.com/gpambrozio/ClaudeDocs/blob/35e4e957bc7b38337e01e44065cf37d4a9600571/docs-md/api/build-with-claude/api-and-data-retention.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention)]

* Added clarification that Claude Managed Agents is not covered by Zero Data Retention (ZDR): sessions are stateful resources, transcripts can be deleted manually but there is no automatic deletion. [[line 32](https://github.com/gpambrozio/ClaudeDocs/blob/35e4e957bc7b38337e01e44065cf37d4a9600571/docs-md/api/build-with-claude/api-and-data-retention.md?plain=1#L32)] [[Source](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention)]

#### [Data Residency](https://github.com/gpambrozio/ClaudeDocs/blob/35e4e957bc7b38337e01e44065cf37d4a9600571/docs-md/api/build-with-claude/data-residency.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/data-residency)]

* Added note that Claude Managed Agents does not support the `inference_geo` parameter, but respects the workspace geo configured in the Console. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/35e4e957bc7b38337e01e44065cf37d4a9600571/docs-md/api/build-with-claude/data-residency.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/build-with-claude/data-residency)]

#### [Events and Streaming](https://github.com/gpambrozio/ClaudeDocs/blob/35e4e957bc7b38337e01e44065cf37d4a9600571/docs-md/api/managed-agents/events-and-streaming.md) [[Source](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)]

* Added a new "Console observability" section describing the visual timeline view for agent sessions in the Console, including session list, tracing view (for Developers/Admins), and tool execution details. [[lines 221-230](https://github.com/gpambrozio/ClaudeDocs/blob/35e4e957bc7b38337e01e44065cf37d4a9600571/docs-md/api/managed-agents/events-and-streaming.md?plain=1#L221-L230)] [[Source](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)]
* Added a "Debugging tips" section with guidance on checking session events, reviewing tool results, tracking token usage, and using system prompts for reasoning visibility. [[lines 232-238](https://github.com/gpambrozio/ClaudeDocs/blob/35e4e957bc7b38337e01e44065cf37d4a9600571/docs-md/api/managed-agents/events-and-streaming.md?plain=1#L232-L238)] [[Source](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)]
