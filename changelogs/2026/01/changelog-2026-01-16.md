# [Claude docs changes for January 16th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852)]

## Executive Summary
- New version 2.1.9: Added MCP tool search auto-threshold, `plansDirectory` setting, and extended thinking enabled by default
- Extensive new CLI flags documented including `--remote`, `--teleport`, `--max-budget-usd`, and `--no-session-persistence`
- New documentation for scaling with MCP Tool Search and fast mode configuration

## New Claude Code version ([2.1.9](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/versions/2.1.9.md))

### New features

* Added `auto:N` syntax for configuring the MCP tool search auto-enable threshold, where N is the context window percentage (0-100)
* Added `plansDirectory` setting to customize where plan files are stored
* Added external editor support (Ctrl+G) in AskUserQuestion "Other" input field
* Added session URL attribution to commits and PRs created from web sessions
* Added support for `PreToolUse` hooks to return `additionalContext` to the model
* Added `${CLAUDE_SESSION_ID}` string substitution for skills to access the current session ID

### Major bug fixes

* Fixed long sessions with parallel tool calls failing with an API error about orphan tool_result blocks
* Fixed MCP server reconnection hanging when cached connection promise never resolves
* Fixed Ctrl+Z suspend not working in terminals using Kitty keyboard protocol (Ghostty, iTerm2, kitty, WezTerm)

-----

## Claude Code changes

### Changed documents

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* New `--allow-dangerously-skip-permissions` flag to enable permission bypassing as an option without immediately activating it [[line 24](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/cli-reference.md?plain=1#L24)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]
* New `--append-system-prompt-file` flag to load additional system prompt text from a file [[line 27](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/cli-reference.md?plain=1#L27)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]
* New `--disable-slash-commands` flag to disable all skills and slash commands for a session [[line 33](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/cli-reference.md?plain=1#L33)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]
* New `--max-budget-usd` flag to set maximum dollar amount to spend on API calls before stopping [[line 41](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/cli-reference.md?plain=1#L41)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]
* New `--no-session-persistence` flag to disable session persistence so sessions are not saved to disk [[line 46](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/cli-reference.md?plain=1#L46)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]
* New `--remote` flag to create a new web session on claude.ai with the provided task description [[line 52](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/cli-reference.md?plain=1#L52)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]
* New `--teleport` flag to resume a web session in your local terminal [[line 60](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/cli-reference.md?plain=1#L60)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]
* Updated system prompt flags section to include `--append-system-prompt-file` as the fourth flag option [[lines 104-153](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/cli-reference.md?plain=1#L104-L153)] [[Source](https://code.claude.com/docs/en/cli-reference#system-prompt-flags)]

#### [common-workflows](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Extended thinking is now enabled by default with up to 31,999 tokens budget [[line 774](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/common-workflows.md?plain=1#L774)] [[Source](https://code.claude.com/docs/en/common-workflows#use-extended-thinking-thinking-mode)]
* Clarified that phrases like "think", "ultrathink", etc. are interpreted as regular prompt instructions and don't allocate thinking tokens [[line 777](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/common-workflows.md?plain=1#L777)] [[Source](https://code.claude.com/docs/en/common-workflows#use-extended-thinking-thinking-mode)]
* Simplified thinking mode configuration table - removed per-request ultrathink section [[lines 779-787](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/common-workflows.md?plain=1#L779-L787)] [[Source](https://code.claude.com/docs/en/common-workflows#configure-thinking-mode)]
* `MAX_THINKING_TOKENS` now limits the budget rather than enabling thinking [[lines 805-808](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/common-workflows.md?plain=1#L805-L808)] [[Source](https://code.claude.com/docs/en/common-workflows#how-extended-thinking-token-budgets-work)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* PreToolUse hooks can now provide context to Claude using `additionalContext` field [[lines 886-903](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/hooks.md?plain=1#L886-L903)] [[Source](https://code.claude.com/docs/en/hooks#pretooluse-decision-control)]

#### [iam](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/iam.md) [[Source](https://code.claude.com/docs/en/iam)]

* Expanded URL filtering guidance to recommend restricting Bash network tools and using PreToolUse hooks [[lines 124-130](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/iam.md?plain=1#L124-L130)] [[Source](https://code.claude.com/docs/en/iam#permission-types)]

#### [index](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/index.md) [[Source](https://code.claude.com/docs/en/)]

* Added clarification that native installations auto-update in the background [[line 44](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/index.md?plain=1#L44)] [[Source](https://code.claude.com/docs/en/)]
* Added note that Homebrew and WinGet installations do not auto-update [[lines 54, 64](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/index.md?plain=1#L54)] [[Source](https://code.claude.com/docs/en/)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* New "Scale with MCP Tool Search" section explaining dynamic on-demand tool loading when MCP tools exceed context threshold [[lines 1115-1175](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/mcp.md?plain=1#L1115-L1175)] [[Source](https://code.claude.com/docs/en/mcp#scale-with-mcp-tool-search)]

#### [overview](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/overview.md) [[Source](https://code.claude.com/docs/en/overview)]

* Added clarification that native installations auto-update in the background [[line 44](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/overview.md?plain=1#L44)] [[Source](https://code.claude.com/docs/en/overview)]
* Added note that Homebrew and WinGet installations do not auto-update [[lines 54, 64](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/overview.md?plain=1#L54)] [[Source](https://code.claude.com/docs/en/overview)]

#### [quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/quickstart.md) [[Source](https://code.claude.com/docs/en/quickstart)]

* Added clarification that native installations auto-update in the background [[line 51](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/quickstart.md?plain=1#L51)] [[Source](https://code.claude.com/docs/en/quickstart#step-1-install-claude-code)]
* Added note that Homebrew and WinGet installations do not auto-update [[lines 59, 69](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/quickstart.md?plain=1#L59)] [[Source](https://code.claude.com/docs/en/quickstart#step-1-install-claude-code)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New `plansDirectory` setting to customize where plan files are stored [[line 159](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/settings.md?plain=1#L159)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* New `showTurnDuration` setting to show/hide turn duration messages [[line 160](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/settings.md?plain=1#L160)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* New `CLAUDE_CODE_TMPDIR` environment variable to override the temp directory [[line 773](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/settings.md?plain=1#L773)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]
* New `ENABLE_TOOL_SEARCH` environment variable to control MCP tool search [[line 801](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/settings.md?plain=1#L801)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]
* Updated `MAX_THINKING_TOKENS` description - now overrides budget instead of enabling thinking [[line 805](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/settings.md?plain=1#L805)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]

#### [setup](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* Updated macOS system requirement from 10.15+ to 13.0+ [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/setup.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/setup#system-requirements)]
* Added clarification about auto-update behavior for different installation methods [[lines 52, 60, 70](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/setup.md?plain=1#L52)] [[Source](https://code.claude.com/docs/en/setup#native-installation)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* New section on automatic discovery of Skills from nested directories (supports monorepo setups) [[lines 136-138](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/skills.md?plain=1#L136-L138)] [[Source](https://code.claude.com/docs/en/skills#automatic-discovery-from-nested-directories)]
* New section on available string substitutions including `$ARGUMENTS` and `${CLAUDE_SESSION_ID}` [[lines 200-225](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/skills.md?plain=1#L200-L225)] [[Source](https://code.claude.com/docs/en/skills#available-string-substitutions)]

#### [slash-commands](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/slash-commands.md) [[Source](https://code.claude.com/docs/en/slash-commands)]

* `/config` now supports typing to search and filter settings [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/slash-commands.md?plain=1#L11)] [[Source](https://code.claude.com/docs/en/slash-commands#built-in-slash-commands)]
* `/doctor` now shows Updates section with auto-update channel and available npm versions [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/slash-commands.md?plain=1#L14)] [[Source](https://code.claude.com/docs/en/slash-commands#built-in-slash-commands)]
* `/stats` now supports pressing `r` to cycle date ranges [[line 41](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/slash-commands.md?plain=1#L41)] [[Source](https://code.claude.com/docs/en/slash-commands#built-in-slash-commands)]

#### [statusline](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/statusline.md) [[Source](https://code.claude.com/docs/en/statusline)]

* Added `used_percentage` and `remaining_percentage` pre-calculated fields to context_window object [[lines 237-238](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/statusline.md?plain=1#L237-L238)] [[Source](https://code.claude.com/docs/en/statusline#context-window-usage)]
* Added simple example using pre-calculated percentages for context window display [[lines 246-260](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/claude-code/statusline.md?plain=1#L246-L260)] [[Source](https://code.claude.com/docs/en/statusline#context-window-usage)]

-----

## API changes

### Changed documents

#### [agent-sdk/hooks](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/api/agent-sdk/hooks.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/hooks)]

* `additionalContext` field now supported in PreToolUse hooks (previously only PostToolUse and other hooks) [[line 240](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/api/agent-sdk/hooks.md?plain=1#L240)] [[Source](https://platform.claude.com/docs/en/agent-sdk/hooks#hook-callback-returns)]

#### [agent-sdk/permissions](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/api/agent-sdk/permissions.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/permissions)]

* Added warning that subagents inherit `bypassPermissions` mode and it cannot be overridden [[line 57](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/api/agent-sdk/permissions.md?plain=1#L57)] [[Source](https://platform.claude.com/docs/en/agent-sdk/permissions#permission-modes)]

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/api/agent-sdk/python.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]

* Added security warning about `allowUnixSockets` granting access to powerful system services like Docker [[line 1960](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/api/agent-sdk/python.md?plain=1#L1960)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python#sandboxsettings)]
* Added warning about combining `bypassPermissions` with `allow_unsandboxed_commands` allowing silent sandbox escape [[line 2043](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/api/agent-sdk/python.md?plain=1#L2043)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python#allow-unsandboxed-commands)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/api/agent-sdk/typescript.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]

* Added security warning about `allowUnixSockets` granting access to powerful system services like Docker [[line 2081](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/api/agent-sdk/typescript.md?plain=1#L2081)] [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript#sandboxsettings)]
* Added warning about combining `bypassPermissions` with `allowUnsandboxedCommands` allowing silent sandbox escape [[line 2164](https://github.com/gpambrozio/ClaudeDocs/blob/f2b35b2e9e6f5ec9acb26c1edfc1e64d2b3f1852/docs-md/api/agent-sdk/typescript.md?plain=1#L2164)] [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript#allow-unsandboxed-commands)]
