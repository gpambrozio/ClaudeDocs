# [Claude docs changes for September 6th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/312db9ed37ad68bb1448c66ba778a221f6d3d274) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/312db9ed37ad68bb1448c66ba778a221f6d3d274)]

## Executive Summary
- New `--append-subagent-system-prompt-file` CLI flag lets you load subagent system prompt additions from a file instead of passing them inline, useful for long text.
- Version 2.1.263 shipped with general bug fixes and reliability improvements.

-----

## Claude Code changes

### Changed documents

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/312db9ed37ad68bb1448c66ba778a221f6d3d274/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Added a new `--append-subagent-system-prompt-file` flag that loads text from a file and appends it to subagent system prompts, as an alternative to `--append-subagent-system-prompt` for text too long to pass on the command line; the two flags can't be combined. Requires Claude Code v2.1.261 or later. [[line 58](https://github.com/gpambrozio/ClaudeDocs/blob/312db9ed37ad68bb1448c66ba778a221f6d3d274/docs-md/claude-code/cli-reference.md?plain=1#L58)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/312db9ed37ad68bb1448c66ba778a221f6d3d274/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `CLAUDE_CODE_ENABLE_APPEND_SUBAGENT_PROMPT` documentation updated to note it is also set automatically by the new `--append-subagent-system-prompt-file` flag. [[line 245](https://github.com/gpambrozio/ClaudeDocs/blob/312db9ed37ad68bb1448c66ba778a221f6d3d274/docs-md/claude-code/env-vars.md?plain=1#L245)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/312db9ed37ad68bb1448c66ba778a221f6d3d274/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Documented that when subagent system prompt text is too long for the command line, it can be saved to a file and passed via `--append-subagent-system-prompt-file` (requires Claude Code v2.1.261 or later). [[line 223](https://github.com/gpambrozio/ClaudeDocs/blob/312db9ed37ad68bb1448c66ba778a221f6d3d274/docs-md/claude-code/sub-agents.md?plain=1#L223)] [[Source](https://code.claude.com/docs/en/sub-agents#write-subagent-files)]
