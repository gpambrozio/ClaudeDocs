# [Claude docs changes for February 27th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/683440d5e700d14449c1d00595d29f599a97f9fc) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/683440d5e700d14449c1d00595d29f599a97f9fc)]

## Executive Summary
- Remote Control is now restricted to Max plans only (Pro support coming soon), narrowing availability compared to the previous Pro+Max rollout
- The `&` prefix for sending tasks to the web has been replaced by the `--remote` flag, a breaking workflow change for terminal-to-web handoffs
- New `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1` and `CLAUDE_CODE_DISABLE_FAST_MODE=1` environment variables give administrators control over adaptive reasoning and fast mode
- Agent SDK hooks expanded: `PostToolUseFailure`, `SubagentStart`, `PermissionRequest`, and `Notification` are now available in the Python SDK, plus new TypeScript-only hooks (`Setup`, `TeammateIdle`, `TaskCompleted`, `ConfigChange`, `WorktreeCreate`, `WorktreeRemove`)
- Claude Sonnet 4.6 now has its own prompt caching minimum token threshold of 2048 (separate from other Sonnet models)

## New Claude Code versions

### [2.1.61](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/versions/2.1.61.md)

#### Major bug fixes

* Fixed concurrent writes corrupting config file on Windows

### [2.1.62](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/versions/2.1.62.md)

#### Major bug fixes

* Fixed prompt suggestion cache regression that reduced cache hit rates

-----

## Claude Code changes

### Changed documents

#### [Best practices](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

* Terminology changed from "headless mode" to "non-interactive mode" throughout. [[line 498](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/best-practices.md?plain=1#L498)] [[Source](https://code.claude.com/docs/en/best-practices#run-non-interactive-mode)]
* Permissions link corrected from `settings.md` to `permissions.md`. [[line 233](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/best-practices.md?plain=1#L233)] [[Source](https://code.claude.com/docs/en/best-practices#configure-permissions)]

#### [Claude Code on the web](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* The `&` message prefix for sending tasks to the web has been replaced by `--remote` flag (e.g., `claude --remote "Fix the bug"`). [[line 76](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L76)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#from-terminal-to-web)]
* The `/remote-env` command now only references `--remote` (the `&` prefix is no longer mentioned). [[line 233](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L233)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#environment-configuration)]

#### [Common workflows](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* `MAX_THINKING_TOKENS` is now ignored on both Opus 4.6 and Sonnet 4.6 (previously only Opus 4.6). [[line 857](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/common-workflows.md?plain=1#L857)] [[Source](https://code.claude.com/docs/en/common-workflows#how-extended-thinking-works)]
* New `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1` environment variable documented for disabling adaptive thinking and reverting to a fixed thinking budget. [[line 858](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/common-workflows.md?plain=1#L858)] [[Source](https://code.claude.com/docs/en/common-workflows#how-extended-thinking-works)]

#### [Discover plugins](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* Added in-app submission forms for the official Anthropic plugin marketplace: `claude.ai/settings/plugins/submit` and `platform.claude.com/plugins/submit`. [[line 39](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/discover-plugins.md?plain=1#L39)] [[Source](https://code.claude.com/docs/en/discover-plugins#official-anthropic-marketplace)]

#### [Fast mode](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* New `CLAUDE_CODE_DISABLE_FAST_MODE=1` environment variable added as an option to disable fast mode entirely. [[line 90](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/fast-mode.md?plain=1#L90)] [[Source](https://code.claude.com/docs/en/fast-mode#enable-fast-mode-for-your-organization)]

#### [Interactive mode](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* `/rename [name]` command updated: when called without a name argument, it now auto-generates a name from conversation history (requires at least one message). [[line 94](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/interactive-mode.md?plain=1#L94)] [[Source](https://code.claude.com/docs/en/interactive-mode#built-in-commands)]
* Clarification that input history resets on `/clear` but the previous session's conversation is preserved and can be resumed. [[line 188](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/interactive-mode.md?plain=1#L188)] [[Source](https://code.claude.com/docs/en/interactive-mode#command-history)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* New MCP servers added to the marketplace: Airwallex Developer, Outreach, and several reorderings. [[line 669](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/mcp.md?plain=1#L669)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]

#### [Model config](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Added documentation for `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1` to disable adaptive reasoning on Opus 4.6 and Sonnet 4.6, reverting to fixed thinking budget. [[line 152](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/model-config.md?plain=1#L152)] [[Source](https://code.claude.com/docs/en/model-config#adjust-effort-level)]

#### [Plugins](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/plugins.md) [[Source](https://code.claude.com/docs/en/plugins)]

* New section added for submitting plugins to the official Anthropic marketplace via in-app forms on claude.ai and platform.claude.com. [[line 391](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/plugins.md?plain=1#L391)] [[Source](https://code.claude.com/docs/en/plugins#submit-your-plugin-to-the-official-marketplace)]

#### [Remote control](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Remote Control availability narrowed: now only available on Max plans (Pro plan support is coming soon, previously it was available on both Pro and Max). [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/remote-control.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/remote-control)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING` environment variable: set to `1` to disable adaptive reasoning for Opus 4.6 and Sonnet 4.6, falling back to fixed `MAX_THINKING_TOKENS` budget. [[line 910](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/settings.md?plain=1#L910)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]
* New `CLAUDE_CODE_DISABLE_FAST_MODE` environment variable: set to `1` to disable fast mode. [[line 913](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/claude-code/settings.md?plain=1#L913)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]

-----

## API changes

### Changed documents

#### [Agent SDK - Cost tracking](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/api/agent-sdk/cost-tracking.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/cost-tracking)]

* Major rewrite clarifying Python vs TypeScript SDK differences for cost tracking. Python only provides accumulated totals on the result message; TypeScript provides per-step breakdowns. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/api/agent-sdk/cost-tracking.md?plain=1#L1)] [[Source](https://platform.claude.com/docs/en/agent-sdk/cost-tracking)]
* Added a diagram illustrating the message stream from a `query()` call with token usage at each step.
* Python SDK reference added alongside the existing TypeScript SDK reference.

#### [Agent SDK - Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/api/agent-sdk/hooks.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/hooks)]

* `PostToolUseFailure`, `SubagentStart`, `PermissionRequest`, and `Notification` hooks are now available in the Python SDK (previously TypeScript-only). [[line 84](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/api/agent-sdk/hooks.md?plain=1#L84)] [[Source](https://platform.claude.com/docs/en/agent-sdk/hooks)]
* New TypeScript-only hooks added: `Setup`, `TeammateIdle`, `TaskCompleted`, `ConfigChange`, `WorktreeCreate`, `WorktreeRemove`. [[line 95](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/api/agent-sdk/hooks.md?plain=1#L95)] [[Source](https://platform.claude.com/docs/en/agent-sdk/hooks)]
* The introductory section was rewritten to explain hooks as a step-by-step flow (event fires → SDK collects hooks → matchers filter → callback executes → decision returned).

#### [Agent SDK - TypeScript](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/api/agent-sdk/typescript.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]

* `SDKAssistantMessageError` no longer includes `'max_output_tokens'` as a valid error value. [[line 585](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/api/agent-sdk/typescript.md?plain=1#L585)] [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]

#### [Agents and tools - Remote MCP servers](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* New MCP servers added: Airtable, Common Room, LSEG, Jotform, Airwallex Developer, Supermetrics, MSCI. [[line 862](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L862)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

#### [Build with Claude - Prompt caching](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* Claude Sonnet 4.6 now has its own minimum cacheable prompt length of 2048 tokens, separate from other Sonnet models (which remain at 1024). [[line 256](https://github.com/gpambrozio/ClaudeDocs/blob/683440d5e700d14449c1d00595d29f599a97f9fc/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L256)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]
