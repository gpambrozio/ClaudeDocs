# [Claude docs changes for February 2nd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b)]

## Executive Summary
- Session quality surveys can now be disabled via `CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY` environment variable
- Hooks decision control documentation expanded with comprehensive tables and examples for each event type
- New prompt suggestions feature documented with Tab/Enter acceptance and environment variable to disable

## Claude Code changes

### Changed documents

#### [Data Usage](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/data-usage.md) [[Source](https://code.claude.com/docs/en/data-usage)]

* Session quality surveys can now be disabled using the `CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY=1` environment variable. The survey is also automatically disabled when using third-party providers (Bedrock, Vertex, Foundry) or when telemetry is disabled. [[line 20](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/data-usage.md?plain=1#L20)] [[Source](https://code.claude.com/docs/en/data-usage#session-quality-surveys)]
* Added Foundry API to the table of default behaviors by API provider, with session quality surveys row showing all third-party providers now disable surveys by default. [[lines 70-78](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/data-usage.md?plain=1#L70-L78)] [[Source](https://code.claude.com/docs/en/data-usage#default-behaviors-by-api-provider)]

#### [Hooks Guide](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Clarified that `permissionDecision` options (allow, deny, ask) are specific to `PreToolUse` hooks, and that other events use different decision patterns. Added reference to summary table in the hooks reference. [[lines 392-398](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/hooks-guide.md?plain=1#L392-L398)] [[Source](https://code.claude.com/docs/en/hooks-guide#structured-json-output)]
* Fixed example output in troubleshooting section from `{"decision": "allow"}` to `{"decision": "block", "reason": "Not allowed"}` to correctly demonstrate a blocking hook. [[line 672](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/hooks-guide.md?plain=1#L672)] [[Source](https://code.claude.com/docs/en/hooks-guide#json-validation-failed)]

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Updated hook script example to use the proper `hookSpecificOutput` structure with `permissionDecision` instead of deprecated top-level `decision` field for PreToolUse hooks. [[lines 68-73](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/hooks.md?plain=1#L68-L73)] [[Source](https://code.claude.com/docs/en/hooks#how-a-hook-resolves)]
* Expanded JSON output documentation to clarify that hooks must choose between exit codes and JSON output, and reorganized to explain universal fields, top-level decision/reason fields, and hookSpecificOutput structure. [[lines 477-482](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/hooks.md?plain=1#L477-L482)] [[Source](https://code.claude.com/docs/en/hooks#json-output)]
* Added new "Decision control" section with a comprehensive table showing which events use which decision patterns (top-level `decision`, `hookSpecificOutput`, etc.) and examples for each pattern. [[lines 505-567](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/hooks.md?plain=1#L505-L567)] [[Source](https://code.claude.com/docs/en/hooks#decision-control)]
* Clarified that PreToolUse uses `hookSpecificOutput` for richer control compared to other events' top-level decision field, with note about deprecated fields. [[lines 842-869](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/hooks.md?plain=1#L842-L869)] [[Source](https://code.claude.com/docs/en/hooks#pretooluse-decision-control)]

#### [IDE Integrations](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* Added documentation for the "Learn Claude Code" onboarding checklist that appears when first opening the panel, including how to dismiss and reopen it. [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/ide-integrations.md?plain=1#L38)] [[Source](https://code.claude.com/docs/en/ide-integrations#get-started)]
* Simplified tutorial documentation by removing the interactive checklist reference and keeping only the VS Code walkthrough command. [[lines 58-58](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/ide-integrations.md?plain=1#L58)] [[Source](https://code.claude.com/docs/en/ide-integrations#get-started)]
* Added instruction to add JSON schema URL to settings.json for autocomplete and inline validation of Claude Code settings in VS Code. [[lines 198-199](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/ide-integrations.md?plain=1#L198-L199)] [[Source](https://code.claude.com/docs/en/ide-integrations#configure-settings)]

#### [Interactive Mode](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Added new "Prompt suggestions" section documenting the feature that provides grayed-out example commands in the prompt input, how to accept them with Tab/Enter, and how to disable them using `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false`. [[lines 256-274](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/interactive-mode.md?plain=1#L256-L274)] [[Source](https://code.claude.com/docs/en/interactive-mode#prompt-suggestions)]

#### [Memory](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Clarified that relative paths in imports resolve relative to the file containing the import, not the working directory, and recommended using `CLAUDE.local.md` for private per-project preferences. [[lines 36-37](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/memory.md?plain=1#L36-L37)] [[Source](https://code.claude.com/docs/en/memory#claude-md-imports)]
* Added explanation that home-directory imports are useful for sharing personal instructions across multiple git worktrees. [[lines 38-48](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/memory.md?plain=1#L38-L48)] [[Source](https://code.claude.com/docs/en/memory#claude-md-imports)]
* Added documentation for the one-time approval dialog that appears when external imports are first encountered in a project. [[lines 48-48](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/memory.md?plain=1#L48)] [[Source](https://code.claude.com/docs/en/memory#claude-md-imports)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `$schema` field to the example settings.json and documented that it enables autocomplete and inline validation in VS Code and other editors. [[lines 103-129](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/settings.md?plain=1#L103-L129)] [[Source](https://code.claude.com/docs/en/settings#settings-files)]
* Added `CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY` environment variable to disable session quality surveys. [[line 894](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/settings.md?plain=1#L894)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]
* Added `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION` environment variable to disable prompt suggestions. [[line 900](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/settings.md?plain=1#L900)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]

#### [VS Code](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Added documentation for the "Learn Claude Code" onboarding checklist that appears when first opening the panel, including how to dismiss and reopen it. [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/vs-code.md?plain=1#L38)] [[Source](https://code.claude.com/docs/en/vs-code#get-started)]
* Simplified tutorial documentation by removing the interactive checklist reference and keeping only the VS Code walkthrough command. [[lines 58-58](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/vs-code.md?plain=1#L58)] [[Source](https://code.claude.com/docs/en/vs-code#get-started)]
* Added instruction to add JSON schema URL to settings.json for autocomplete and inline validation of Claude Code settings in VS Code. [[lines 198-199](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/claude-code/vs-code.md?plain=1#L198-L199)] [[Source](https://code.claude.com/docs/en/vs-code#configure-settings)]

-----

## API changes

### Changed documents

#### [Extended Thinking](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Updated contact email obfuscation link for accessing full thinking output for Claude 4 models. [[line 98](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L98)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

#### [Files](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Updated contact email obfuscation link for requesting higher rate limits during the beta period. [[line 284](https://github.com/gpambrozio/ClaudeDocs/blob/29c89979ba3e7a31e9dd169fb4e76ec38f2dbc0b/docs-md/api/build-with-claude/files.md?plain=1#L284)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]
