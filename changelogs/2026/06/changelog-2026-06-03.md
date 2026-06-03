# [Claude docs changes for June 3rd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/0f09b199ca2ba34e2de3af433acb933a45758c5e) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/0f09b199ca2ba34e2de3af433acb933a45758c5e)]

## Executive Summary
- Auto mode is now available on Amazon Bedrock, Google Cloud Vertex AI, and Microsoft Foundry via the new `CLAUDE_CODE_ENABLE_AUTO_MODE` env var (previously Anthropic API only)
- The workflow trigger keyword changed from `workflow` to `ultracode`; natural-language requests like "use a workflow" also work
- Advisor tool gains a `max_tokens` parameter to cap advisor output per call, with a new `stop_reason` field on results
- `claude-opus-4-8` is now listed in all API beta endpoint model enums; `mid-conversation-system-2026-04-07` beta header removed
- Protected paths list significantly expanded to cover more config dirs and dotfiles (`.config/git`, `.devcontainer`, `.yarn`, `.mvn`, and many shell/toolchain configs)

## New Claude Code versions

### [2.1.161](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/versions/2.1.161.md)

#### New features

* `OTEL_RESOURCE_ATTRIBUTES` values are now included as labels on metric datapoints, enabling slicing of usage metrics by custom dimensions like team or repo
* `/mcp` now collapses claude.ai connectors you've never signed in to behind a "Show unused connectors" row

#### Existing feature improvements

* `claude agents` rows now show `done/total` before the detail when work is fanned out; peek shows the longest-running item
* Parallel tool calls: a failed Bash command no longer cancels other calls in the same batch — each tool returns its own result independently
* Fullscreen mode: clipboard now uses `wl-copy`/`xclip`/`xsel` on Linux when available, copies to both clipboard and PRIMARY selection for middle-click paste, and the "hold {key} for native selection" hint now shows the correct key per terminal
* Improved terminal rendering performance by stabilizing the layout engine's JIT compilation profile
* Improved rendering performance for large file writes
* [VSCode] Added a tip suggesting disabling terminal GPU acceleration (or running `/terminal-setup`) to fix garbled glyphs

#### Major bug fixes

* Fixed `forceLoginOrgUUID`/`forceLoginMethod` managed-settings policies blocking third-party provider sessions (Bedrock, Vertex, Foundry, Mantle) alongside the org pin (regression in 2.1.146)
* Fixed background subagent output corrupting `claude -p` stdout when using `--output-format text` or `json`
* Fixed `/autofix-pr` reporting "cannot run on the default branch" when the session is inside a git worktree or another repository
* Fixed `--resume` picker not showing sessions from the current directory when it isn't a git worktree (e.g., jj workspaces)
* Fixed Windows hooks that invoke bash explicitly (e.g., `/usr/bin/bash script.sh`) failing with "command not found" or "cannot execute binary file"
* Fixed OpenTelemetry log events being silently dropped when emitted before telemetry initialization completed
* Fixed `claude mcp` list/get/add printing secrets to the terminal: `${VAR}` references are no longer expanded, and credential headers and URL secrets are redacted
* Fixed Workflow agents spawned with `isolation: "worktree"` in background sessions being blocked from editing files inside their own worktree
* Fixed background sessions dispatched from `claude agents` booting on a stale model from the daemon's environment instead of the model in `settings.json`
* Fixed completed subagents getting stuck showing as running when an error occurs while finalizing their result
* Fixed `EADDRINUSE` errors from tools that bind Unix sockets under `$TMPDIR` when `CLAUDE_CODE_TMPDIR` is set to a deep path

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/hooks](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/agent-sdk/hooks.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

* Matchers now have documented comparison rules: a matcher with only letters, digits, `_`, and `|` is compared as an exact string with `|` as an OR separator; anything else is evaluated as a regex. `*` or empty string matches all occurrences. Updated the "Filter with regex matchers" section to "Filter with multi-tool matchers" to reflect this. [[line 158](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L158)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#matchers)]

#### [agent-view](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* Clarification that attached sessions always render in fullscreen mode, with notes on scrolling (`PgUp`/`PgDn`, mouse wheel) and why the `tui` setting does not apply. [[line 154](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/agent-view.md?plain=1#L154)] [[Source](https://code.claude.com/docs/en/agent-view#attach-to-a-session)]

#### [auto-mode-config](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/auto-mode-config.md) [[Source](https://code.claude.com/docs/en/auto-mode-config)]

* Updated availability note: auto mode on Bedrock, Vertex AI, and Foundry now requires `CLAUDE_CODE_ENABLE_AUTO_MODE` rather than being fully unavailable. [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/auto-mode-config.md?plain=1#L11)] [[Source](https://code.claude.com/docs/en/auto-mode-config)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/terminal-setup` description updated: Windsurf replaced by Devin Desktop in the list of terminals requiring setup. [[line 119](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/commands.md?plain=1#L119)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Auto mode availability updated: for Enterprise deployments routing Desktop to Google Cloud Vertex AI, auto mode is off until `CLAUDE_CODE_ENABLE_AUTO_MODE` is set, and only Opus 4.7/4.8 are supported there. [[line 74](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/desktop.md?plain=1#L74)] [[Source](https://code.claude.com/docs/en/desktop#choose-a-permission-mode)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_ENABLE_AUTO_MODE` env var: enables auto mode on Amazon Bedrock, Google Cloud Vertex AI, and Microsoft Foundry (only Opus 4.7/4.8 supported on these providers). [[line 172](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/env-vars.md?plain=1#L172)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN` clarification: does not apply to background sessions opened from agent view, which always use fullscreen rendering. [[line 150](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/env-vars.md?plain=1#L150)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE` marked as removed in v2.1.160 and now a no-op; guidance updated to use `/model` + `/fast on` instead. [[line 207](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/env-vars.md?plain=1#L207)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* "There's an issue with the selected model" error now has surface-specific guidance: interactive CLI runs `/model`, non-interactive mode uses `--model` flag or `ANTHROPIC_MODEL`, and Agent SDK surfaces a structured `model_not_found` error for programmatic handling. [[line 518](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/errors.md?plain=1#L518)] [[Source](https://code.claude.com/docs/en/errors#there’s-an-issue-with-the-selected-model)]

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* Removed mention of `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE` (removed in v2.1.160). [[line 44](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/fast-mode.md?plain=1#L44)] [[Source](https://code.claude.com/docs/en/fast-mode#toggle-fast-mode)]

#### [fullscreen](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/fullscreen.md) [[Source](https://code.claude.com/docs/en/fullscreen)]

* Added note that background sessions opened from agent view or `claude attach` always use fullscreen rendering, and `tui`/`CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN` do not apply to them. [[line 148](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/fullscreen.md?plain=1#L148)] [[Source](https://code.claude.com/docs/en/fullscreen#research-preview)]

#### [glossary](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/glossary.md) [[Source](https://code.claude.com/docs/en/glossary)]

* Auto mode definition generalized: removed "Anthropic API only" qualifier now that it's available on other providers with an opt-in flag. [[line 40](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/glossary.md?plain=1#L40)] [[Source](https://code.claude.com/docs/en/glossary#auto-mode)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Shift+Enter setup table updated: Windsurf replaced by Devin Desktop. [[line 72](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/interactive-mode.md?plain=1#L72)] [[Source](https://code.claude.com/docs/en/interactive-mode#multiline-input)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Auto mode availability expanded: now available on Bedrock, Vertex AI, and Foundry for Opus 4.7/4.8 by setting `CLAUDE_CODE_ENABLE_AUTO_MODE=1`. New "Enable auto mode on Bedrock, Vertex AI, or Foundry" section with configuration examples. [[lines 149-176](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/permission-modes.md?plain=1#L149-L176)] [[Source](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode)]
* Protected paths list significantly expanded. New protected directories: `.config/git`, `.devcontainer`, `.yarn`, `.mvn`. New protected files: `.bash_login`, `.bash_aliases`, `.bash_logout`, `.zshenv`, `.zlogin`, `.zlogout`, `.envrc`, `.npmrc`, `.yarnrc`, `.yarnrc.yml`, `.pnp.cjs`, `.pnp.loader.mjs`, `.pnpmfile.cjs`, `bunfig.toml`, `.bunfig.toml`, `.bazelrc`, `.bazelversion`, `.bazeliskrc`, `.pre-commit-config.yaml`, `lefthook.yml/yaml`, `gradle-wrapper.properties`, `maven-wrapper.properties`, `.devcontainer.json`, `pyrightconfig.json`. [[lines 281-300](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/permission-modes.md?plain=1#L281-L300)] [[Source](https://code.claude.com/docs/en/permission-modes#protected-paths)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* `bypassPermissions` description updated to include newly protected dirs: `.config/git`, `.devcontainer`, `.yarn`, `.mvn`. [[line 47](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/permissions.md?plain=1#L47)] [[Source](https://code.claude.com/docs/en/permissions#permission-modes)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* `tui` setting description updated: background sessions opened from agent view always use fullscreen regardless of this setting. [[line 244](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/settings.md?plain=1#L244)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* `workflowKeywordTriggerEnabled` updated: now controls the `ultracode` keyword (not `workflow`), and its display name in `/config` is now "Ultracode keyword trigger". [[line 247](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/settings.md?plain=1#L247)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* `bypassPermissions` description updated to include newly protected dirs: `.config/git`, `.devcontainer`, `.yarn`, `.mvn`. [[line 399](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/sub-agents.md?plain=1#L399)] [[Source](https://code.claude.com/docs/en/sub-agents#permission-modes)]

#### [terminal-config](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* Windsurf replaced by Devin Desktop throughout the Shift+Enter configuration table and `/terminal-setup` description. [[lines 28-33](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/terminal-config.md?plain=1#L28-L33)] [[Source](https://code.claude.com/docs/en/terminal-config#enter-multiline-prompts)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* `grep`, `egrep`, and `fgrep` (on a single file with no pipes or redirects) now satisfy the read-before-edit requirement in addition to `cat`, `head`, `tail`, `sed`. Also clarified that the recognized-for-deny-rules set differs from the read-before-edit list. [[lines 129-130](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/tools-reference.md?plain=1#L129-L130)] [[Source](https://code.claude.com/docs/en/tools-reference#edit-tool-behavior)]

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* VS Code forks list updated: Windsurf replaced by Devin Desktop. [[line 30](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/vs-code.md?plain=1#L30)] [[Source](https://code.claude.com/docs/en/vs-code#install-the-extension)]

#### [workflows](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/workflows.md) [[Source](https://code.claude.com/docs/en/workflows)]

* Workflow trigger keyword changed from `workflow` to `ultracode`. Natural-language requests ("use a workflow", "run a workflow") also now trigger workflows. The `/config` toggle renamed to "Ultracode keyword trigger". [[lines 111-119](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/claude-code/workflows.md?plain=1#L111-L119)] [[Source](https://code.claude.com/docs/en/workflows#have-claude-write-a-workflow)]

-----

## API changes

### Changed documents

#### [agents-and-tools/tool-use/advisor-tool](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/api/agents-and-tools/tool-use/advisor-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

* New `max_tokens` parameter on the advisor tool definition to cap the advisor's total output (thinking + text) per call. Minimum 1024. Setting it above the advisor model's own output cap returns a 400 error. [[line 94](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L94)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]
* New `stop_reason` field on `advisor_result` and `advisor_redacted_result` variants, present when `max_tokens` is set on the tool definition. Carries the sub-call's stop reason (`"end_turn"` or `"max_tokens"`). [[lines 143-145](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L143-L145)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]
* New "Capping advisor output" section with benchmark data: `max_tokens: 2048` reduces mean advisor output ~7x with ~0% truncation; `max_tokens: 1024` reduces ~10x but truncates ~10% of calls. [[lines 418-465](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L418-L465)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

#### [agents-and-tools/tool-use/handle-tool-calls](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/api/agents-and-tools/tool-use/handle-tool-calls.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)]

* Added a security warning about prompt injection via tool results: content from tool results (web pages, uploads, third-party APIs) should be treated as untrusted, and instructions from those sources may attempt to redirect Claude. Recommends keeping untrusted content inside `tool_result` blocks rather than `system` prompts or plain `user` text. [[line 61](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/api/agents-and-tools/tool-use/handle-tool-calls.md?plain=1#L61)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)]

#### [agents-and-tools/tool-use/troubleshooting-tool-use](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/api/agents-and-tools/tool-use/troubleshooting-tool-use.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)]

* New "Claude flags tool results as prompt injection" troubleshooting section: when Claude refuses to act on a tool result, the fix is to move instructions out of the `tool_result` block into a subsequent `user` turn or a mid-conversation system message. [[lines 44-47](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/api/agents-and-tools/tool-use/troubleshooting-tool-use.md?plain=1#L44-L47)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)]

#### [agents-and-tools/tool-use/web-search-tool](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/api/agents-and-tools/tool-use/web-search-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]

* New "When Claude searches" section documenting when Claude triggers a web search (recent events, current data, explicit requests) vs. answers directly (stable facts, creative tasks, analysis of provided content). [[lines 22-38](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/api/agents-and-tools/tool-use/web-search-tool.md?plain=1#L22-L38)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]
* Practical `max_uses` guidance added: simple queries typically use 1–3 searches; `max_uses: 3` bounds cost for latency-sensitive lookups; 15–20 or omit for research agents. [[line 132](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/api/agents-and-tools/tool-use/web-search-tool.md?plain=1#L132)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]

#### [api/beta](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* `mid-conversation-system-2026-04-07` beta header removed from the `AnthropicBeta` enum (now "23 more" instead of "24 more"). [[line 13](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/api/api/beta.md?plain=1#L13)] [[Source](https://platform.claude.com/docs/en/api/beta)]
* `BetaOutputTokensDetails` object now formally documented as a named type with a detailed description of the `thinking_tokens` field, including how it's computed and how it relates to `output_tokens`. [[lines 12589-12602](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/api/api/beta.md?plain=1#L12589-L12602)] [[Source](https://platform.claude.com/docs/en/api/beta)]
* `output_tokens_details` fields across all usage objects now reference `BetaOutputTokensDetails` by type link instead of inline `object { thinking_tokens }`. [[line 9212](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/api/api/beta.md?plain=1#L9212)] [[Source](https://platform.claude.com/docs/en/api/beta)]

#### [api/beta/agents](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/api/api/beta/agents.md) [[Source](https://platform.claude.com/docs/en/api/beta/agents)]

* `claude-opus-4-8` added to `BetaManagedAgentsModel` enum as the new first/top model option across all agent create/update/list/retrieve endpoints. [[line 71](https://github.com/gpambrozio/ClaudeDocs/blob/0f09b199ca2ba34e2de3af433acb933a45758c5e/docs-md/api/api/beta/agents.md?plain=1#L71)] [[Source](https://platform.claude.com/docs/en/api/beta/agents)]
* `mid-conversation-system-2026-04-07` beta header removed from the beta enum across all beta API endpoint reference files.
