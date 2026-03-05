# [Claude docs changes for March 5th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/405608801dab6ad1fbf6392aef227ccd7d4ca3c8) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/405608801dab6ad1fbf6392aef227ccd7d4ca3c8)]

## Executive Summary
- Claude Code 2.1.69 is a massive release with 60+ changes: new `InstructionsLoaded` hook, `git-subdir` plugin source, `/claude-api` skill, `/reload-plugins` command, and Voice STT support for 10 new languages
- System prompt flags (`--append-system-prompt-file`, `--system-prompt-file`) now work in both interactive and print modes — previously print-mode only
- Extended thinking docs removed the "Thinking redaction" section (`redacted_thinking` blocks no longer documented as a feature)
- Pricing docs expanded with a comprehensive prompt caching section detailing how cache multipliers work
- Context compaction now available in the Ruby SDK (previously Python and TypeScript only)

## New Claude Code versions

### [2.1.69](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/versions/2.1.69.md)

#### New features

* Added the `/claude-api` skill for building applications with the Claude API and Anthropic SDK. Also activates automatically when code imports `anthropic`, `@anthropic-ai/sdk`, or `claude_agent_sdk`
* Added optional name argument to `/remote-control` and `claude remote-control` (e.g. `/remote-control My Project` or `--name "My Project"`) to set a custom session title visible in claude.ai/code
* Added `InstructionsLoaded` hook event that fires when CLAUDE.md or `.claude/rules/*.md` files are loaded into context, at session start and lazily during a session
* Added `agent_id` (for subagents) and `agent_type` (for subagents and `--agent`) fields to all hook events
* Added `worktree` field to status line hook commands with name, path, branch, and original repo directory when in a `--worktree` session
* Added `includeGitInstructions` setting (and `CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS` env var) to remove built-in commit and PR workflow instructions from the system prompt
* Added `/reload-plugins` command to activate pending plugin changes without restarting
* Added plugin source type `git-subdir` to point to a subdirectory within a git repo (sparse clone for monorepos)
* Added `pathPattern` to `strictKnownMarketplaces` for regex-matching file/directory marketplace sources
* Added `pluginTrustMessage` in managed settings to append organization-specific context to plugin trust warnings
* Added `sandbox.enableWeakerNetworkIsolation` setting (macOS only) to allow Go tools like `gh`, `gcloud`, and `terraform` to verify TLS certificates when using a custom MITM proxy
* Added `${CLAUDE_SKILL_DIR}` variable for skills to reference their own directory in SKILL.md content
* Added `oauth.authServerMetadataUrl` config option for MCP servers to specify a custom OAuth metadata discovery URL
* Added Voice STT support for 10 new languages (20 total): Russian, Polish, Turkish, Dutch, Ukrainian, Greek, Czech, Danish, Swedish, Norwegian
* Added effort level display (e.g., "with low effort") to the logo and spinner
* Added agent name display in terminal title when using `claude --agent`
* Added Ctrl+U on an empty bash prompt (`!`) to exit bash mode
* Added numeric keypad support for selecting options in Claude's interview questions
* Added `${CLAUDE_SKILL_DIR}` variable for skills

#### Existing feature improvements

* Improved MCP binary content handling: tools returning PDFs, Office documents, or audio now save decoded bytes to disk with the correct file extension instead of dumping raw base64 into the conversation
* `--append-system-prompt-file` and `--system-prompt-file` now work in interactive mode (docs previously stated print mode only)
* Changed Sonnet 4.5 users on Pro/Max/Team Premium to be automatically migrated to Sonnet 4.6
* Changed the `/resume` picker to show the most recent prompt instead of the first one
* `TeammateIdle` and `TaskCompleted` hooks now support `{"continue": false, "stopReason": "..."}` JSON response to stop a teammate entirely (not just re-run it with feedback)
* `ultrathink` keyword now sets effort to high for that turn on Opus 4.6 and Sonnet 4.6 (rather than being treated as a plain prompt instruction)
* [VSCode] Added compaction display as a collapsible "Compacted chat" card with summary inside
* [VSCode] Permission mode picker now respects `permissions.disableBypassPermissionsMode` from managed settings

#### Major bug fixes

* Fixed security issue where nested skill discovery could load skills from gitignored directories like `node_modules`
* Fixed trust dialog silently enabling all `.mcp.json` servers on first run
* Fixed symlink bypass where writing new files through a symlinked parent directory could escape the working directory in `acceptEdits` mode
* Fixed sandbox prompting users to approve non-allowed domains when `allowManagedDomainsOnly` is enabled — non-allowed domains are now blocked automatically
* Fixed interactive tools (e.g., `AskUserQuestion`) being silently auto-allowed when listed in a skill's allowed-tools
* Fixed `--model claude-opus-4-0` and `--model claude-opus-4-1` resolving to deprecated Opus versions
* Fixed macOS keychain corruption when using multiple OAuth MCP servers
* Fixed memory leak in long-running SDK/CCR sessions where conversation messages were retained unnecessarily
* Fixed API 400 errors in forked agents when resuming sessions interrupted mid-tool-batch
* Fixed multi-GB memory spike when committing with large untracked binary files

-----

## Claude Code changes

### Changed documents

#### [CLI Reference](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* `--append-system-prompt-file` and `--system-prompt-file` flags now work in both interactive and print modes. The "Modes" column removed from the system prompt flags comparison table — all four flags now work in all modes. [[line 30](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/cli-reference.md?plain=1#L30)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [Common Workflows](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Removed reference to the `/commit-push-pr` skill from the pull request workflow section
* `ultrathink` keyword documented as setting effort to high for that turn on Opus 4.6 and Sonnet 4.6 (previously listed as a non-functional phrase alongside "think hard")

#### [Discover Plugins](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* Added documentation for `/reload-plugins` command to apply plugin changes without restarting
* Added a Security section warning that plugins can execute arbitrary code with user privileges

#### [Hooks Guide](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Added `InstructionsLoaded` event to the hook events table — fires when CLAUDE.md or `.claude/rules/*.md` files are loaded

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Added `InstructionsLoaded` hook event with full input schema documentation (`file_path`, `memory_type`, `load_reason`, `globs`, `trigger_file_path`, `parent_file_path`). [[line 795](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/hooks.md?plain=1#L795)] [[Source](https://code.claude.com/docs/en/hooks#persist-environment-variables)]
* Added `agent_id` and `agent_type` to the common input fields table for hooks running inside subagents or `--agent` sessions [[line 478](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/hooks.md?plain=1#L478)] [[Source](https://code.claude.com/docs/en/hooks#common-input-fields)]
* `TeammateIdle` and `TaskCompleted` hooks now support `{"continue": false, "stopReason": "..."}` JSON to stop a teammate entirely, in addition to exit code 2 to re-run with feedback [[line 1453](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/hooks.md?plain=1#L1453)] [[Source](https://code.claude.com/docs/en/hooks#teammateidle-input)]
* Clarified that `SessionStart` only supports `type: "command"` hooks

#### [Interactive Mode](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Added `/reload-plugins` to the slash commands table
* Bash mode now exits with `Ctrl+U` in addition to `Escape` and `Backspace`

#### [Memory](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Added mention of the `InstructionsLoaded` hook as a debugging tool for tracking which instruction files are loaded and when

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Updated MCP server listing: various reordering and new entries added to the featured servers list

#### [Model Config](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Opus 4.6 defaults to medium effort for Max and Team subscribers
* Effort level now displayed next to the logo and spinner (e.g., "with low effort") so the active setting is visible without opening `/model`

#### [Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Settings precedence now explicitly documented that managed settings cannot be overridden by command line arguments
* `sandbox.network.allowManagedDomainsOnly` clarified: non-allowed domains are now blocked automatically without prompting the user

#### [Plugin Marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Added `git-subdir` plugin source type for pointing to a subdirectory within a git repo, with full documentation including `url`, `path`, `ref`, and `sha` fields [[line 267](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/plugin-marketplaces.md?plain=1#L267)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#plugin-sources)]
* Added `pathPattern` to `strictKnownMarketplaces` for regex-matching filesystem-based marketplace paths [[line 762](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/plugin-marketplaces.md?plain=1#L762)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#common-configurations)]

#### [Remote Control](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Added `--name` argument (and positional name argument to `/remote-control`) to set a custom session title visible in claude.ai/code session list

#### [Sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Clarified that when `allowManagedDomainsOnly` is enabled, non-allowed domains are blocked automatically without triggering a permission prompt

#### [Server-Managed Settings](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* Clarified that server-managed settings cannot be overridden by any other level, including command line arguments

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `includeGitInstructions` setting to remove built-in commit/PR workflow instructions from the system prompt
* Added `pluginTrustMessage` managed-only setting to append organization-specific context to plugin trust warnings before installation
* Added `sandbox.enableWeakerNetworkIsolation` setting (macOS only) for Go-based tools with custom MITM proxy and custom CA
* Added `CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS` environment variable
* Updated `sandbox.network.allowManagedDomainsOnly` description to note non-allowed domains are blocked automatically
* Settings precedence updated to explicitly note managed settings override even command line arguments

#### [Skills](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Added `/claude-api` bundled skill description: loads Claude API reference material and Agent SDK reference, covers tool use, streaming, batches, structured outputs, and common pitfalls
* Added `${CLAUDE_SKILL_DIR}` variable for referencing the skill's own directory regardless of current working directory

#### [Status Line](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/statusline.md) [[Source](https://code.claude.com/docs/en/statusline)]

* Added `worktree` fields to the status line JSON input documentation: `worktree.name`, `worktree.path`, `worktree.branch`, `worktree.original_cwd`, `worktree.original_branch` [[line 189](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/statusline.md?plain=1#L189)] [[Source](https://code.claude.com/docs/en/statusline#available-data)]
* Added Windows configuration section with examples for invoking PowerShell or Bash scripts from Git Bash [[line 562](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/claude-code/statusline.md?plain=1#L562)] [[Source](https://code.claude.com/docs/en/statusline#cache-expensive-operations)]
* Added debugging tips: use `claude --debug` to log exit code and stderr from the first status line invocation

-----

## API changes

### Changed documents

#### [Adaptive Thinking](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/api/build-with-claude/adaptive-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

* Removed the "Thinking redaction" section entirely, including the `redacted_thinking` block explanation, example output, and test trigger string

#### [Citations](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/api/build-with-claude/citations.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/citations)]

* Code example for combining citations with prompt caching changed from Python to Shell/curl

#### [Context Editing](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/api/build-with-claude/context-editing.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/context-editing)]

* Client-side compaction (SDK) is now available in the Python, TypeScript, **and Ruby** SDKs (Ruby was not previously listed)
* `max_tokens` in compaction examples updated from 1024 to 16000 to be more realistic

#### [Context Windows](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/api/build-with-claude/context-windows.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]

* Removed references to `redacted_thinking` blocks from thinking token documentation

#### [Effort](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/api/build-with-claude/effort.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]

* Best practices updated: recommendation changed from "Start with high" to "Set effort explicitly" since the right starting point depends on model and workload

#### [Extended Thinking](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Removed the "Thinking redaction" section and the "Example: Working with redacted thinking blocks" section entirely. The model handling note updated to remove redaction references

#### [Pricing](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* Added a comprehensive "Prompt caching" subsection under "Feature-specific pricing" explaining how caching works, pricing multipliers (1.25x for 5-min writes, 2x for 1-hour writes, 0.1x for reads), and when caching pays off [[line 53](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/api/about-claude/pricing.md?plain=1#L53)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]
* The model pricing table's footnote now links to the new expanded section instead of repeating multipliers inline

#### [Remote MCP Servers](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Updated MCP server listings: new entries added (Smartsheet, Airtable, Similarweb, Daloopa, ICD-10 Codes), other servers reordered

#### [Streaming](https://github.com/gpambrozio/ClaudeDocs/blob/405608801dab6ad1fbf6392aef227ccd7d4ca3c8/docs-md/api/build-with-claude/streaming.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/streaming)]

* Added PHP SDK streaming support via `createStream()`
* Documented streaming accumulation patterns for Go (`message.Accumulate(event)`), Java (`MessageAccumulator`), Ruby (`.accumulated_message`), and PHP

