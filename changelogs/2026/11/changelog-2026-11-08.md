# [Claude docs changes for November 8th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/6fce44fd4bf314dd5194598f4a6fac0b14776787) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/6fce44fd4bf314dd5194598f4a6fac0b14776787)]

## Executive Summary
- `PermissionRequest` hooks that auto-approve `ExitPlanMode` or `AskUserQuestion` must now return `updatedInput`. Without it Claude Code ignores the allow and still shows the prompt.
- The hooks guide examples now use `jq` to echo `tool_input` back as `updatedInput`.
- MCP task answers are now documented as more lenient. Claude Code accepts a missing `createdAt`, `lastUpdatedAt` or `ttlMs`, and a `null` `pollIntervalMs`. Before v2.1.317 these caused an error.

## New Claude Code versions

No new versions today.

-----

## Claude Code changes

### Changed documents

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/6fce44fd4bf314dd5194598f4a6fac0b14776787/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* The auto-approval section now says that tools which require user interaction, such as `ExitPlanMode`, need `updatedInput` in the allow decision, or the prompt still appears. [[line 420](https://github.com/gpambrozio/ClaudeDocs/blob/6fce44fd4bf314dd5194598f4a6fac0b14776787/docs-md/claude-code/hooks-guide.md?plain=1#L420)] [[Source](https://code.claude.com/docs/en/hooks-guide#auto-approve-specific-permission-prompts)]
* The example hook command now uses `jq` to pass `.tool_input` back as `updatedInput`. [[line 433](https://github.com/gpambrozio/ClaudeDocs/blob/6fce44fd4bf314dd5194598f4a6fac0b14776787/docs-md/claude-code/hooks-guide.md?plain=1#L433)] [[Source](https://code.claude.com/docs/en/hooks-guide#auto-approve-specific-permission-prompts)]
* The `acceptEdits` mode-switch example is now a one-line `jq` command that includes `updatedInput` and `updatedPermissions`. It replaces the raw JSON block. [[lines 452-456](https://github.com/gpambrozio/ClaudeDocs/blob/6fce44fd4bf314dd5194598f4a6fac0b14776787/docs-md/claude-code/hooks-guide.md?plain=1#L452-L456)] [[Source](https://code.claude.com/docs/en/hooks-guide#auto-approve-specific-permission-prompts)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/6fce44fd4bf314dd5194598f4a6fac0b14776787/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* The `updatedInput` field description now notes that `AskUserQuestion` and `ExitPlanMode` require it. [[line 2165](https://github.com/gpambrozio/ClaudeDocs/blob/6fce44fd4bf314dd5194598f4a6fac0b14776787/docs-md/claude-code/hooks.md?plain=1#L2165)] [[Source](https://code.claude.com/docs/en/hooks#permissionrequest-decision-control)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/6fce44fd4bf314dd5194598f4a6fac0b14776787/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* The task-result error conditions are corrected. The call fails only when `taskId` or a valid `status` is missing. [[line 595](https://github.com/gpambrozio/ClaudeDocs/blob/6fce44fd4bf314dd5194598f4a6fac0b14776787/docs-md/claude-code/mcp.md?plain=1#L595)] [[Source](https://code.claude.com/docs/en/mcp#answer-the-call-with-a-task)]
* `createdAt`, `lastUpdatedAt` and `ttlMs` are now described as required by the tasks extension rather than by Claude Code. `pollIntervalMs` may be `null`, and Claude Code then uses the 2000 ms default. [[lines 615-616](https://github.com/gpambrozio/ClaudeDocs/blob/6fce44fd4bf314dd5194598f4a6fac0b14776787/docs-md/claude-code/mcp.md?plain=1#L615-L616)] [[Source](https://code.claude.com/docs/en/mcp#answer-the-call-with-a-task)]
* A new note says Claude Code accepts task answers that omit those three fields. Before v2.1.317 such answers failed. Server authors who want to support older versions should keep sending them. [[line 620](https://github.com/gpambrozio/ClaudeDocs/blob/6fce44fd4bf314dd5194598f4a6fac0b14776787/docs-md/claude-code/mcp.md?plain=1#L620)] [[Source](https://code.claude.com/docs/en/mcp#answer-the-call-with-a-task)]

-----

## API changes

No API documentation changes today.
