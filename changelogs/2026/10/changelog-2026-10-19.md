# [Claude docs changes for October 19th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/c3784c4e2f4d63cdb6396cd6b5ee7c1cbe678cb8) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/c3784c4e2f4d63cdb6396cd6b5ee7c1cbe678cb8)]

## Executive Summary
- The hooks reference and guide were reorganized to explain more clearly how exit codes, malformed JSON output, timeouts and HTTP hook failures are handled, and how to make a hook block on failure with `onFailure: "block"`.
- The sandbox runtime instructions now install `@anthropic-ai/sandbox-runtime` globally and launch with `srt claude` instead of `npx`.
- Claude Code 2.1.303 was released with only minor bug fixes and reliability improvements.

## New Claude Code versions

### [2.1.303](https://github.com/gpambrozio/ClaudeDocs/blob/c3784c4e2f4d63cdb6396cd6b5ee7c1cbe678cb8/versions/2.1.303.md)

#### Major bug fixes

* Only general bug fixes and reliability improvements (no notable changes)

-----

## Claude Code changes

### Changed documents

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/c3784c4e2f4d63cdb6396cd6b5ee7c1cbe678cb8/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Clarified that setting `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION` to `true` keeps the near-usage-limit pause from applying until the limit is reached. [[line 287](https://github.com/gpambrozio/ClaudeDocs/blob/c3784c4e2f4d63cdb6396cd6b5ee7c1cbe678cb8/docs-md/claude-code/env-vars.md?plain=1#L287)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/c3784c4e2f4d63cdb6396cd6b5ee7c1cbe678cb8/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Exit code section rewritten: non-0/2 exit codes without valid JSON let the action proceed unless the hook is one whose failure blocks the action (for example `onFailure: "block"`). Exit 2 and "any other exit code" behavior was reorganized by what the hook printed to stdout. [[lines 586-595](https://github.com/gpambrozio/ClaudeDocs/blob/c3784c4e2f4d63cdb6396cd6b5ee7c1cbe678cb8/docs-md/claude-code/hooks-guide.md?plain=1#L586-L595)] [[Source](https://code.claude.com/docs/en/hooks-guide#hook-output)]
* `PreToolUse` `permissionDecision` explanation condensed into prose: `"ask"` shows the normal prompt and `"allow"` skips it, with deny/ask rules, network-path reads, `requiresUserInteraction` MCP tools and org-`ask` connector tools still applying. [[line 615](https://github.com/gpambrozio/ClaudeDocs/blob/c3784c4e2f4d63cdb6396cd6b5ee7c1cbe678cb8/docs-md/claude-code/hooks-guide.md?plain=1#L615)] [[Source](https://code.claude.com/docs/en/hooks-guide#structured-json-output)]
* Constraints section restructured into "what still holds over `allow`" and "`deny` in every permission mode", which still blocks even with `bypassPermissions`. [[line 944](https://github.com/gpambrozio/ClaudeDocs/blob/c3784c4e2f4d63cdb6396cd6b5ee7c1cbe678cb8/docs-md/claude-code/hooks-guide.md?plain=1#L944)] [[Source](https://code.claude.com/docs/en/hooks-guide#hooks-and-permission-modes)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/c3784c4e2f4d63cdb6396cd6b5ee7c1cbe678cb8/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Exit 0 with unparsable or schema-invalid JSON is now explicitly a non-blocking error. Stdout parsing rules were reworded, with advice to print only a single JSON object. [[lines 782-793](https://github.com/gpambrozio/ClaudeDocs/blob/c3784c4e2f4d63cdb6396cd6b5ee7c1cbe678cb8/docs-md/claude-code/hooks.md?plain=1#L782-L793)] [[Source](https://code.claude.com/docs/en/hooks#exit-code-0)]
* Troubleshooting guidance for the `Failed with non-blocking status code:` notice and for hooks that never ran because of a missing script path. [[lines 829-845](https://github.com/gpambrozio/ClaudeDocs/blob/c3784c4e2f4d63cdb6396cd6b5ee7c1cbe678cb8/docs-md/claude-code/hooks.md?plain=1#L829-L845)] [[Source](https://code.claude.com/docs/en/hooks#other-exit-codes)]
* Timeout behavior consolidated: a `PreModelSwitch` hook canceled at timeout blocks the switch, while timed-out `PreToolUse` command/http/mcp_tool hooks don't block unless `onFailure: "block"` is set. [[line 851](https://github.com/gpambrozio/ClaudeDocs/blob/c3784c4e2f4d63cdb6396cd6b5ee7c1cbe678cb8/docs-md/claude-code/hooks.md?plain=1#L851)] [[Source](https://code.claude.com/docs/en/hooks#timeouts)]
* HTTP hooks: `onFailure: "block"` and 2xx JSON decision fields are now introduced before the outcome table. [[line 991](https://github.com/gpambrozio/ClaudeDocs/blob/c3784c4e2f4d63cdb6396cd6b5ee7c1cbe678cb8/docs-md/claude-code/hooks.md?plain=1#L991)] [[Source](https://code.claude.com/docs/en/hooks#http-response-handling)]
* `PreModelSwitch`: other exit codes are a non-blocking error so the switch goes ahead, except for hooks whose failure blocks it. [[line 3420](https://github.com/gpambrozio/ClaudeDocs/blob/c3784c4e2f4d63cdb6396cd6b5ee7c1cbe678cb8/docs-md/claude-code/hooks.md?plain=1#L3420)] [[Source](https://code.claude.com/docs/en/hooks#premodelswitch-timeouts-and-other-exit-codes)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/c3784c4e2f4d63cdb6396cd6b5ee7c1cbe678cb8/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Reworded the usage-limit prompt suggestion skip: the env var keeps the skip from applying until the limit is reached. [[line 412](https://github.com/gpambrozio/ClaudeDocs/blob/c3784c4e2f4d63cdb6396cd6b5ee7c1cbe678cb8/docs-md/claude-code/interactive-mode.md?plain=1#L412)] [[Source](https://code.claude.com/docs/en/interactive-mode#when-claude-code-skips-suggestions)]

#### [sandbox-environments](https://github.com/gpambrozio/ClaudeDocs/blob/c3784c4e2f4d63cdb6396cd6b5ee7c1cbe678cb8/docs-md/claude-code/sandbox-environments.md) [[Source](https://code.claude.com/docs/en/sandbox-environments)]

* Replaced `npx @anthropic-ai/sandbox-runtime claude` with a global install (under a prefix outside any writable allowed path) followed by `srt claude` from the project directory. [[lines 102-114](https://github.com/gpambrozio/ClaudeDocs/blob/c3784c4e2f4d63cdb6396cd6b5ee7c1cbe678cb8/docs-md/claude-code/sandbox-environments.md?plain=1#L102-L114)] [[Source](https://code.claude.com/docs/en/sandbox-environments#set-up-and-launch-the-runtime)]

-----

## API changes

No API documentation changes today.
