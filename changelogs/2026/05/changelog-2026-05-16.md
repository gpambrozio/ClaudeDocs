# [Claude docs changes for May 16th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f)]

## Executive Summary
- The Tool Runner is now available in C#, Go, Java, and PHP SDKs (previously only Python, TypeScript, and Ruby), with a significantly clarified "taking over message history" workflow
- MCP tool search is now supported on Vertex AI for Claude Sonnet 4.5+ and Opus 4.5+, reversing the previous blanket disable
- Bedrock and Vertex AI now default the small/fast (background) model to the primary model instead of Haiku, since Haiku may not be available in every account/region
- Claude Code 2.1.143 adds plugin dependency enforcement, a new `worktree.bgIsolation: "none"` setting, and extensive `claude agents` CLI improvements
- The `/feedback` command now saves a local redacted archive on third-party providers (Bedrock, Vertex, Foundry) instead of failing silently

## New Claude Code versions

### [2.1.143](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/versions/2.1.143.md)

#### New features

* Added plugin dependency enforcement: `claude plugin disable` now refuses when another enabled plugin depends on the target (with a copy-pasteable disable-chain hint), and `claude plugin enable` force-enables transitive dependencies
* Added projected context cost (per-turn and per-invocation token estimates) to the `/plugin` marketplace browse pane
* Added `worktree.bgIsolation: "none"` setting to let background sessions edit the working copy directly without `EnterWorktree`, for repos where worktrees are impractical
* `claude agents` now accepts `--add-dir`, `--settings`, `--mcp-config`, `--plugin-dir`, `--permission-mode`, `--model`, `--effort`, and `--dangerously-skip-permissions`, applying them to the dashboard and sessions dispatched from it

#### Existing feature improvements

* PowerShell tool now passes `-ExecutionPolicy Bypass` by default; opt out with `CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY=1`
* PowerShell tool is now enabled by default on Windows for Bedrock, Vertex, and Foundry users (opt out with `CLAUDE_CODE_USE_POWERSHELL_TOOL=0`)
* Background sessions now preserve the model and effort level set after waking from idle
* Shift+Tab in attached agent sessions now includes auto mode in the cycle
* `/bg` now preserves `--mcp-config`, `--settings`, `--add-dir`, `--plugin-dir`, `--strict-mcp-config`, `--fallback-model`, and `--allow-dangerously-skip-permissions` so backgrounded sessions keep their configuration across respawn
* Background sessions launched from `claude agents` now honor `permissions.defaultMode` from settings.json
* `--agent <name>` now finds plugin-contributed agents without requiring the `plugin:` prefix
* `--bg --dangerously-skip-permissions` now persists across retire→wake
* Worktree cleanup no longer falls back to `rm -rf` when `git worktree remove` fails, preventing loss of gitignored or in-progress files

#### Major bug fixes

* Fixed corrupt `.credentials.json` with a non-array `scopes` value hanging the CLI on startup or silently aborting OAuth token refresh
* Fixed right-click paste in `claude agents` on Windows Terminal and WSL
* Fixed stop hooks that block repeatedly looping forever — the turn now ends with a warning after 8 consecutive blocks (override via `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`)
* Fixed Esc/Ctrl+C not cancelling a pending `/loop` wakeup while Claude is idle between iterations
* Fixed `/goal` evaluator firing while background shells or delegated subagents are still running
* Fixed `NO_COLOR`/`FORCE_COLOR` in settings.json `env` stripping Claude Code's own UI colors — they now apply to subprocesses only
* Fixed agent view spawning repeated PowerShell processes on Windows when listing sessions
* Fixed `/bg` without a prompt sending "continue" to the forked session — the fork now waits for input
* Fixed deleting a session from agent view not removing its transcript file
* Fixed stale-fragment rendering when scrolling in attached background sessions on Windows Terminal
* Fixed background agents false-positive worker-stall detection storm after host sleep or macOS App Nap
* Fixed 5xx error messages pointing at status.claude.com instead of naming the configured gateway or cloud provider
* Fixed background sessions silently capturing IDE file references into the warm spare's input
* Fixed background-job sessions on macOS getting "Operation not permitted" errors when reading files under `~/Documents`, `~/Desktop`, or `~/Downloads`, even with Full Disk Access granted
* Fixed: on Windows, pressing ← in `claude agents` while a response was streaming could leave the agents list unresponsive to all input
* Fixed `claude agents --allow-dangerously-skip-permissions` defaulting dispatched sessions to bypass mode instead of making it available in the permission cycle
* Fixed background daemon spawn falling back to the running binary when the `~/.local/bin/claude` launcher is missing or non-executable

-----

## Claude Code changes

### Changed documents

#### [amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* The default small/fast model on Bedrock is now "same as primary model" (was `us.anthropic.claude-haiku-4-5-20251001-v1:0`). Background tasks default to the primary model because Haiku may not be enabled in every account or region. [[line 180](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/amazon-bedrock.md?plain=1#L180)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#4-pin-model-versions)]
* Clarified that `ANTHROPIC_SMALL_FAST_MODEL_AWS_REGION` only takes effect when `ANTHROPIC_DEFAULT_HAIKU_MODEL` or the deprecated `ANTHROPIC_SMALL_FAST_MODEL` is also set. [[line 147](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/amazon-bedrock.md?plain=1#L147)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#3-configure-claude-code)]

#### [claude-directory](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* Added `feedback-bundles/` to the list of temporary directories: redacted transcript archives written by `/feedback` on third-party providers. [[line 200](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/claude-directory.md?plain=1#L200)] [[Source](https://code.claude.com/docs/en/claude-directory#cleaned-up-automatically)]

#### [data-usage](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/data-usage.md) [[Source](https://code.claude.com/docs/en/data-usage)]

* Updated `/feedback` description: users can now choose how much history to include (current session only, or other sessions from the same project over 24 hours or 7 days). [[line 90](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/data-usage.md?plain=1#L90)] [[Source](https://code.claude.com/docs/en/data-usage#telemetry-services)]
* Added: on third-party providers (Bedrock, Vertex, or no Anthropic credentials), `/feedback` writes a redacted local archive to `~/.claude/feedback-bundles/` instead of sending data to Anthropic. [[line 91](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/data-usage.md?plain=1#L91)] [[Source](https://code.claude.com/docs/en/data-usage#telemetry-services)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Updated `ANTHROPIC_SMALL_FAST_MODEL_AWS_REGION` documentation: on Bedrock, this only takes effect when `ANTHROPIC_DEFAULT_HAIKU_MODEL` or the deprecated `ANTHROPIC_SMALL_FAST_MODEL` is also set. [[line 45](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/env-vars.md?plain=1#L45)] [[Source](https://code.claude.com/docs/en/env-vars)]
* Updated `ENABLE_TOOL_SEARCH` documentation: Vertex AI now supports tool search for Sonnet 4.5+ and Opus 4.5+; requests fail on earlier Vertex AI models. [[line 213](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/env-vars.md?plain=1#L213)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* Updated `/feedback` description: on Bedrock, Vertex AI, Foundry, and other third-party providers, `/feedback` now saves a local archive you can send to your Anthropic account representative instead of failing. [[line 574](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/errors.md?plain=1#L574)] [[Source](https://code.claude.com/docs/en/errors#report-an-error)]

#### [google-vertex-ai](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/google-vertex-ai.md) [[Source](https://code.claude.com/docs/en/google-vertex-ai)]

* MCP tool search is now supported on Vertex AI for Claude Sonnet 4.5+ and Opus 4.5+. Earlier models still reject the required beta header. [[line 131](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/google-vertex-ai.md?plain=1#L131)] [[Source](https://code.claude.com/docs/en/google-vertex-ai#4-configure-claude-code)]
* The default small/fast model on Vertex AI is now "same as primary model" (was `claude-haiku-4-5@20251001`). Background tasks default to the primary model because Haiku may not be enabled in every project or region. [[line 152](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/google-vertex-ai.md?plain=1#L152)] [[Source](https://code.claude.com/docs/en/google-vertex-ai#5-pin-model-versions)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Updated tool search documentation: Vertex AI now supports tool search for Claude Sonnet 4.5+ and Opus 4.5+. [[line 895](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/mcp.md?plain=1#L895)] [[Source](https://code.claude.com/docs/en/mcp#configure-tool-search)]

#### [microsoft-foundry](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/microsoft-foundry.md) [[Source](https://code.claude.com/docs/en/microsoft-foundry)]

* Added explanation that on Foundry, Claude Code defaults background tasks to the primary model because not every account has a Haiku deployment. Instructions provided to enable Haiku via `ANTHROPIC_DEFAULT_HAIKU_MODEL`. [[line 88](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/microsoft-foundry.md?plain=1#L88)] [[Source](https://code.claude.com/docs/en/microsoft-foundry#4-pin-model-versions)]

#### [agent-sdk/slash-commands](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/agent-sdk/slash-commands.md) [[Source](https://code.claude.com/docs/en/agent-sdk/slash-commands)]

* Code examples updated: result checks now require `message.subtype === "success"` in addition to `message.type === "result"`. [[lines 49, 200](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/agent-sdk/slash-commands.md?plain=1#L49)]

#### [agent-sdk/streaming-vs-single-mode](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/agent-sdk/streaming-vs-single-mode.md) [[Source](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode)]

* Code examples updated: `SDKUserMessage` type is now imported and used explicitly; `parent_tool_use_id: null` added to yielded messages; result checks now require `message.subtype === "success"`. [[lines 57-109](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/agent-sdk/streaming-vs-single-mode.md?plain=1#L57)] [[Source](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode#implementation-example)]

#### [agent-sdk/subagents](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/agent-sdk/subagents.md) [[Source](https://code.claude.com/docs/en/agent-sdk/subagents)]

* Python example updated: imports `ToolUseBlock` and uses `isinstance(block, ToolUseBlock)` instead of checking the `type` attribute string. [[line 221](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/agent-sdk/subagents.md?plain=1#L221)] [[Source](https://code.claude.com/docs/en/agent-sdk/subagents#detecting-subagent-invocation)]
* TypeScript helper updated: message type guard now checks `message.type !== "assistant" && message.type !== "user"` instead of `"message" in message`. [[line 280](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/agent-sdk/subagents.md?plain=1#L280)] [[Source](https://code.claude.com/docs/en/agent-sdk/subagents#resuming-subagents)]

#### [agent-sdk/tool-search](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/agent-sdk/tool-search.md) [[Source](https://code.claude.com/docs/en/agent-sdk/tool-search)]

* Updated: tool search is now supported on Vertex AI for Claude Sonnet 4.5+ and Opus 4.5+ (previously described as disabled across all of Vertex AI). [[line 27](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/agent-sdk/tool-search.md?plain=1#L27)] [[Source](https://code.claude.com/docs/en/agent-sdk/tool-search#configure-tool-search)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* `session_id` in the `SDKUserMessage` type is now optional (`session_id?: string`). [[line 938](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L938)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkusermessage)]

-----

## API changes

### Changed documents

#### [agents-and-tools/tool-use/advisor-tool](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/api/agents-and-tools/tool-use/advisor-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

* Updated guidance for trimming advisor output length: the recommended conciseness instruction should now be placed in the **user message** (not system prompt), as the advisor reliably follows direct instructions. A specific example is provided. The guidance notes `max_tokens` does not bound advisor output. [[lines 405-420](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L405)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

#### [agents-and-tools/tool-use/parallel-tool-use](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/api/agents-and-tools/tool-use/parallel-tool-use.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use)]

* New "Execution semantics" section: tool calls in a single assistant turn are unordered and can be run concurrently, sequentially, or in any order. Claude issues dependent calls across separate turns. [[lines 9-24](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/api/agents-and-tools/tool-use/parallel-tool-use.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use)]
* New troubleshooting item: when batched tool calls turn out to depend on each other, return `is_error: true` with the natural error message — Claude will recover and reissue the call. [[line 204](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/api/agents-and-tools/tool-use/parallel-tool-use.md?plain=1#L204)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use)]

#### [agents-and-tools/tool-use/tool-runner](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/api/agents-and-tools/tool-use/tool-runner.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner)]

* The Tool Runner beta is now available in **C#, Go, Java, and PHP SDKs** in addition to the existing Python, TypeScript, and Ruby SDKs. All code examples now include tabs for these new languages. [[line 10](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/api/agents-and-tools/tool-use/tool-runner.md?plain=1#L10)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner)]
* Advanced usage section significantly rewritten: the per-iteration lifecycle is now documented step-by-step, clarifying when the runner appends message history automatically vs. when your code takes over. [[lines 152-175](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/api/agents-and-tools/tool-use/tool-runner.md?plain=1#L152)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner)]
* New "Taking over message history" section explains how and when to use `append_messages()` to manually manage conversation state, and clarifies that `set_messages_params()` does not trigger a takeover. [[lines 176-220](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/api/agents-and-tools/tool-use/tool-runner.md?plain=1#L176)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner)]
* "Automatic context management with compaction" moved into its own subsection under Advanced usage. [[line 228](https://github.com/gpambrozio/ClaudeDocs/blob/3cfd0c74b5a6d9fa45f4ad4b3fc52f6ef4af678f/docs-md/api/agents-and-tools/tool-use/tool-runner.md?plain=1#L228)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner)]
