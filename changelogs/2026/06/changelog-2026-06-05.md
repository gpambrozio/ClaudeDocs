# [Claude docs changes for June 5th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/b20f023f0788d56ef82bfd4693de8fe0cc12ceef) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/b20f023f0788d56ef82bfd4693de8fe0cc12ceef)]

## Executive Summary
- Claude Code 2.1.163 adds enterprise version enforcement via `requiredMinimumVersion`/`requiredMaximumVersion` managed settings, plus Stop/SubagentStop hooks can now return `additionalContext` to give Claude feedback without triggering a hook error
- The MCP per-server `timeout` behavior changed: values below 1000 are now ignored and fall through to `MCP_TOOL_TIMEOUT` (previously they were floored to 1 second)
- WebFetch tool now has a built-in set of preapproved documentation domains that fetch without permission prompts, with explicit deny/ask/allow rules able to override them
- Compliance Access Keys for the Compliance API are now managed from "Organization settings > API" (not "Data and privacy")
- Citations API now supports URL as an input method for PDF documents (alongside base64 and file_id)

## New Claude Code versions

### [2.1.163](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/versions/2.1.163.md)

#### New features

* Added `requiredMinimumVersion` and `requiredMaximumVersion` managed settings — Claude Code refuses to start if its version is outside the allowed range
* Added `/plugin list` command to list installed plugins, with `--enabled`/`--disabled` filters
* Added "c to copy" shortcut in `/btw` that copies the raw markdown answer to the clipboard
* Stop and SubagentStop hooks can now return `hookSpecificOutput.additionalContext` to give Claude feedback and keep the turn going without being labeled a hook error
* Skills: added `\$` escape syntax to include a literal `$` before a digit in command bodies
* stdio MCP servers now receive the same `CLAUDE_CODE_SESSION_ID` as hooks/Bash on `--resume`

#### Existing feature improvements

* Background agent sessions now update to a new Claude Code version in the background, so opening a session after an update no longer waits on a cold restart
* Clearer descriptions for built-in commands and skills in the `/` menu
* Subscription-switch suggestion now shows in the startup announcement slot instead of a toast
* `claude agents` dispatching from the state-grouped view now starts the session in the directory the agent view was opened from

#### Major bug fixes

* Fixed `claude -p` hanging forever after its final result when a backgrounded command never exits — background shells are now stopped ~5s after the result once stdin closes
* Fixed `claude -p` failing with "ANTHROPIC_API_KEY required" on Bedrock/Vertex/Foundry when `CI=true` and no Anthropic API key is set
* Fixed bash commands failing under bazel and EDR-protected Go workflows: `$TMPDIR` was overridden to `/tmp/claude-{uid}` for all commands instead of only sandboxed ones (regression in 2.1.154)
* Fixed Bash commands failing on Windows with "EEXIST: file already exists" on the session-env directory inside OneDrive or with read-only attribute
* Fixed org-managed permission rules not applying for the entire session when managed settings fetch completed during startup on a fresh config directory
* Fixed background sessions in `claude agents` losing their running background tasks when reattached after a Claude Code update
* Fixed terminal misalignment and a multi-second hang when exiting the agent view by pressing Esc
* Fixed hook `if: "Bash(...)"` conditions firing on every Bash command containing `$()` or `$VAR`
* Fixed deny rules on home-directory paths (e.g. `Read(~/Desktop/**)`) not blocking Bash commands that reference the path via `$HOME`

### [2.1.165](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/versions/2.1.165.md)

#### Major bug fixes

* Bug fixes and reliability improvements

-----

## Claude Code changes

### Changed documents

#### [Agent SDK - Python](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* Added documentation for `ResultMessage.subtype` field, explaining the different subtypes (`success`, `error_during_execution`, `error_max_turns`, `error_max_budget_usd`, `error_max_structured_output_retries`) and which fields are populated for each, including `is_error`, `api_error_status`, `result`, and `errors`. [[line 1494](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/agent-sdk/python.md?plain=1#L1494)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#resultmessage)]

#### [Agent View](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* Updated `claude agents --json` description: when `status` is `waiting`, the new `waitingFor` field explains what the session is blocked on (e.g., `permission prompt` or `input needed`). [[line 391](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/agent-view.md?plain=1#L391)] [[Source](https://code.claude.com/docs/en/agent-view#manage-sessions-from-the-shell)]

#### [Claude Platform on AWS](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/claude-platform-on-aws.md) [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

* Removed the enterprise sales banner and links from the top of the page.

#### [Deep Links](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/deep-links.md) [[Source](https://code.claude.com/docs/en/deep-links)]

* Changed how deep link launch notification is shown: now a `Prompt from an external link` warning line below the input box that stays visible until the prompt is sent or cleared (was a banner above the input). [[line 32](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/deep-links.md?plain=1#L32)] [[Source](https://code.claude.com/docs/en/deep-links#what-a-launched-session-shows)]
* Simplified repo path display in deep links: the welcome header shows which path was selected (removed previous note about last fetch time from remote). [[line 76](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/deep-links.md?plain=1#L76)] [[Source](https://code.claude.com/docs/en/deep-links#choose-between-cwd-and-repo)]

#### [Environment Variables](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Clarified `MCP_TOOL_TIMEOUT` behavior: the per-server `timeout` field in `.mcp.json` now ignores values below 1000 (previously floored to one second); the env variable still floors to one second. [[line 302](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/env-vars.md?plain=1#L302)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Rewrote the `claude mcp add` option-ordering note: clarified that `--` separates Claude's own options from the server command, and added a warning that `--env` must not be immediately followed by the server name (place another option between them). [[line 98](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/mcp.md?plain=1#L98)] [[Source](https://code.claude.com/docs/en/mcp#option-3-add-a-local-stdio-server)]
* Updated per-server `timeout` behavior: values below 1000 are now ignored and fall through to `MCP_TOOL_TIMEOUT` (or its ~28-hour default). Before v2.1.162, they were floored to one second. [[line 169](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/mcp.md?plain=1#L169)] [[Source](https://code.claude.com/docs/en/mcp#push-messages-with-channels)]
* Added note that some Anthropic-hosted connectors (Microsoft 365, Gmail, Google Calendar) require connecting via claude.ai Settings → Connectors because the upstream identity provider only accepts the claude.ai redirect URL. [[line 736](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/mcp.md?plain=1#L736)] [[Source](https://code.claude.com/docs/en/mcp#use-mcp-servers-from-claude-ai)]

#### [Memory](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Added `.devin/rules/` to the list of tool configs that `/init` reads when generating a `CLAUDE.md` from an existing repo. [[line 124](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/memory.md?plain=1#L124)] [[Source](https://code.claude.com/docs/en/memory#agents-md)]

#### [Monitoring Usage](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Added `tool_use_id` and `gen_ai.tool.call.id` attributes to tool spans and tool result spans, enabling correlation of spans with tool result/decision events and hook payloads. [[lines 194-195](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/monitoring-usage.md?plain=1#L194-L195)] [[Source](https://code.claude.com/docs/en/monitoring-usage#span-attributes)]
* Added `skill.kind` attribute (value `"workflow"` for workflow skills, absent otherwise) to skill invocation events. [[line 762](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/monitoring-usage.md?plain=1#L762)] [[Source](https://code.claude.com/docs/en/monitoring-usage#skill-activated-event)]

#### [Terminal Guide](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/terminal-guide.md) [[Source](https://code.claude.com/docs/en/terminal-guide)]

* Split PATH troubleshooting into two separate code blocks for Zsh (macOS default) and Bash (Linux default) for clarity.

#### [Tools Reference](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* Updated LSP tool capability description: "List symbols in a file" and "Search for a symbol by name across the workspace" are now listed separately (was "List symbols in a file or workspace"). [[line 157](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/tools-reference.md?plain=1#L157)] [[Source](https://code.claude.com/docs/en/tools-reference#lsp-tool-behavior)]
* WebFetch now has a built-in set of preapproved documentation domains that fetch without a permission prompt. Explicit `WebFetch(domain:...)` rules in `deny`, `ask`, or `allow` override the preapproved set. [[lines 250-251](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/tools-reference.md?plain=1#L250-L251)] [[Source](https://code.claude.com/docs/en/tools-reference#webfetch-tool-behavior)]

#### [Troubleshoot Install](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/troubleshoot-install.md) [[Source](https://code.claude.com/docs/en/troubleshoot-install)]

* Added a note that in PowerShell, `curl.exe -sI` must be used instead of `curl -sI` (PowerShell aliases `curl` to `Invoke-WebRequest` which rejects those flags). [[line 50](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/troubleshoot-install.md?plain=1#L50)] [[Source](https://code.claude.com/docs/en/troubleshoot-install#check-network-connectivity)]

#### [VS Code](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Updated VS Code extension data removal instructions with platform-specific paths and commands for macOS, Linux, and Windows PowerShell (replaces the previous single cross-platform path). [[lines 458-476](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/claude-code/vs-code.md?plain=1#L458-L476)] [[Source](https://code.claude.com/docs/en/vs-code#uninstall-the-extension)]

-----

## API changes

### Changed documents

#### [Code Execution Tool](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

* Added guidance on when Claude chooses to run code vs. answer directly: code runs for non-trivial math, data analysis, algorithm execution, and explicit run requests; direct answers for simple arithmetic, conversational, or creative requests. [[lines 84-99](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L84-L99)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

#### [Citations](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/api/build-with-claude/citations.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/citations)]

* PDF documents can now be provided as a URL (in addition to base64-encoded data or `file_id`). [[line 218](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/api/build-with-claude/citations.md?plain=1#L218)] [[Source](https://platform.claude.com/docs/en/build-with-claude/citations)]

#### [Compliance API Access](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/api/manage-claude/compliance-api-access.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-api-access)]

* Compliance Access Keys are now created and managed from `claude.ai > Organization settings > API` (was `Data and privacy`). All instructions and links throughout the page updated to reflect the new location. [[lines 15-27](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/api/manage-claude/compliance-api-access.md?plain=1#L15-L27)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-api-access)]

#### [Dreams (Managed Agents)](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/api/managed-agents/dreams.md) [[Source](https://platform.claude.com/docs/en/managed-agents/dreams)]

* Added new "Steer with instructions" section explaining how the optional `instructions` field works: it steers synthesis focus, merge/drop decisions, and output structure, but is not a text editor for specific lines. [[lines 72-76](https://github.com/gpambrozio/ClaudeDocs/blob/b20f023f0788d56ef82bfd4693de8fe0cc12ceef/docs-md/api/managed-agents/dreams.md?plain=1#L72-L76)] [[Source](https://platform.claude.com/docs/en/managed-agents/dreams)]
