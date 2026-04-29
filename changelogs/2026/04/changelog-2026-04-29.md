# [Claude docs changes for April 29th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/cc85455) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/cc85455)]

## Executive Summary
- New `Setup` hook event added across hooks, hooks-guide, and CLI reference — fires during `--init-only`, `--init -p`, and `--maintenance -p` runs, enabling initialization-time automation
- Agent SDK MCP guide completely rebuilt from scratch (was an error 500 page) with full coverage of transports, authentication, permissions, and error handling
- Six new environment variables documented: `ANTHROPIC_BEDROCK_SERVICE_TIER`, `CLAUDE_CODE_ATTRIBUTION_HEADER`, `CLAUDE_CODE_DISABLE_POLICY_SKILLS`, `CLAUDE_CODE_EXTRA_BODY`, `CLAUDE_CODE_MCP_ALLOWLIST_ENV`, and `CLAUDE_CODE_USE_NATIVE_FILE_SEARCH`
- Four new documentation pages added: a Claude Code glossary, an installation troubleshooting guide, a team champion kit, and a team communications/rollout kit
- Sandbox network proxy security limitation documented: domain fronting can bypass the allowlist since TLS is not terminated

## New Claude Code versions

### [2.1.122](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/versions/2.1.122.md)

#### New features

* Added `ANTHROPIC_BEDROCK_SERVICE_TIER` environment variable to select a Bedrock service tier (`default`, `flex`, or `priority`), sent as the `X-Amzn-Bedrock-Service-Tier` header
* Pasting a PR/MR URL into the `/resume` search box now finds the session that created that PR (GitHub, GitHub Enterprise, GitLab, and Bitbucket)
* `/mcp` now shows claude.ai connectors hidden by a manually-added server with the same URL, with a hint to remove the duplicate
* OpenTelemetry: added `claude_code.at_mention` log event for `@`-mention resolution

#### Existing feature improvements

* OpenTelemetry: numeric attributes on `api_request`/`api_error` log events are now emitted as numbers, not strings
* Clarified the `/mcp` message shown when an MCP server is still unauthorized after the browser sign-in flow

#### Major bug fixes

* Fixed `/branch` producing forks that fail with "tool_use ids were found without tool_result blocks" when the source session contained entries from rewound timelines
* Fixed `/model` not showing the Effort option for Bedrock application inference profile ARNs, and those ARNs not receiving `output_config.effort`
* Fixed Vertex AI / Bedrock returning `invalid_request_error: output_config: Extra inputs are not permitted` on session-title generation and other structured-output queries
* Fixed Vertex AI `count_tokens` endpoint returning 400 errors for users behind proxy gateways
* Fixed `spinnerTipsOverride.excludeDefault` not suppressing the time-based spinner tips
* Fixed ToolSearch missing MCP tools that connected after session start in nonblocking mode
* Fixed `!exit` / `!quit` in bash mode terminating the CLI instead of running as a shell command
* Fixed images sent to newer models being resized to 2576px per side instead of the correct 2000px maximum
* Fixed remote control session idle status redrawing twice per second, which could flood `tmux -CC` control pipes and pause the terminal
* Fixed assistant messages appearing blank in some sessions due to a stale view preference
* Fixed a malformed hooks entry in `settings.json` no longer invalidating the entire file
* Voice mode: keybindings bound to Caps Lock now show an error since terminals don't deliver Caps Lock as a key event

### [2.1.123](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/versions/2.1.123.md)

#### Major bug fixes

* Fixed OAuth authentication failing with a 401 retry loop when `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` is set

-----

## Claude Code changes

### New Documents

#### [Champion kit](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/champion-kit.md) [[Source](https://code.claude.com/docs/en/champion-kit)]

Guide for individual engineers who want to help their team adopt Claude Code. Covers what to share (prompts, screenshots, wins), how to answer common colleague questions, a 30-day adoption playbook, and ready-made responses to skeptical concerns. Includes time estimates for each activity (e.g. 15 min/week posting wins, 20 min/week answering channel questions).

#### [Communications kit](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/communications-kit.md) [[Source](https://code.claude.com/docs/en/communications-kit)]

Guide for administrators and engineering leads rolling out Claude Code to a team. Provides copy-ready launch announcement templates (email and Slack/Teams formats), an executive sponsor variant, a pilot group variant, a champion recruitment DM, a drip tips-and-tricks campaign organized by feature area, and a quick-reference FAQ and prompt template table.

#### [Glossary](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/glossary.md) [[Source](https://code.claude.com/docs/en/glossary)]

Comprehensive A–W glossary defining Claude Code-specific terminology with links to in-depth documentation pages for each concept. Covers ~35 terms including Agent teams, Agentic loop, Auto memory, Auto mode, Bare mode, Bundled skills, Channel, Checkpoint, Compaction, Dispatch, Hook, Managed settings, MCP Tool Search, Permission mode, Plan mode, Plugin, Prompt injection, Remote Control, Sandboxing, Session, Skill, Subagent, Surface, Teleport, Worktree isolation, and more. Also includes a deprecated/renamed terms table.

#### [Troubleshoot installation and login](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/troubleshoot-install.md) [[Source](https://code.claude.com/docs/en/troubleshoot-install)]

New dedicated installation troubleshooting guide covering errors encountered during install or first login (distinct from runtime issues). Includes a quick lookup table mapping error messages to fixes, and detailed sections for: `command not found` / PATH issues, install script returning HTML, curl write failures, low-memory Linux installs, TLS/SSL errors, network/proxy connectivity, wrong Windows shell commands, WSL Git Bash requirement, and OAuth/login issues.

### Changed documents

#### [agent-sdk/hooks](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/agent-sdk/hooks.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

* `PostToolUse` hook's `hookSpecificOutput` now also supports `updatedToolOutput` to replace the tool's output entirely before Claude sees it (previously only `additionalContext` was mentioned). [[line 126](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L126)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#available-hooks)]

#### [agent-sdk/mcp](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/agent-sdk/mcp.md) [[Source](https://code.claude.com/docs/en/agent-sdk/mcp)]

* Entire file replaced: was previously an error 500 page, now a complete guide titled "Connect to external tools with MCP." Covers quickstart, adding MCP servers in-code vs. via `.mcp.json`, tool naming (`mcp__<server>__<tool>`), granting access with `allowedTools` and wildcards, all three transport types (stdio, HTTP/SSE, SDK in-process), MCP authentication (env vars, HTTP headers, OAuth 2.1), error handling via `system/init` message, and troubleshooting.

#### [agent-sdk/overview](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/agent-sdk/overview.md) [[Source](https://code.claude.com/docs/en/agent-sdk/overview)]

* New comparison section: "Agent SDK vs Managed Agents" with a table covering where each runs, interface type, session state, custom tools, and recommended use cases. Notes that prototyping with the Agent SDK and moving to Managed Agents for production is a common migration path. [[lines ~329–379](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/agent-sdk/overview.md?plain=1#L329)]

#### [agent-sdk/plugins](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/agent-sdk/plugins.md) [[Source](https://code.claude.com/docs/en/agent-sdk/plugins)]

* Clarified that the `type` field in plugin loading must be `"local"` — the only accepted value. To use a marketplace or remote plugin, download it first and provide the local path. [[line ~23](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/agent-sdk/plugins.md?plain=1#L23)]

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* `SandboxNetworkConfig` now documents three previously missing properties: `allowedDomains`, `deniedDomains`, and `allowManagedDomainsOnly`. [[lines ~3029–3082](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/agent-sdk/python.md?plain=1#L3029)]
* Security note added: the built-in sandbox proxy enforces `allowedDomains` based on the client-supplied hostname without terminating TLS, so domain fronting can bypass the allowlist. Recommends a TLS-terminating custom proxy for stronger guarantees.

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Same sandbox proxy domain fronting security note added as in `python.md`. [[lines ~2851–2853](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L2851)]

#### [amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* New section: Service tiers. `ANTHROPIC_BEDROCK_SERVICE_TIER` env var selects `default`, `flex`, or `priority`, sent as the `X-Amzn-Bedrock-Service-Tier` header. Availability varies by model and region. [[lines ~271–278](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/amazon-bedrock.md?plain=1#L271)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* `--init` flag: now documented as running Setup hooks with the `init` matcher in print mode (`-p`) only. [[lines ~65–73](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/cli-reference.md?plain=1#L65)]
* `--init-only` flag: now documented as running Setup and SessionStart hooks then exiting.
* `--maintenance` flag: now documented as running Setup hooks with the `maintenance` matcher, in print mode only.

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/heapdump` now writes to the home directory on Linux systems without a Desktop folder (previously only `~/Desktop` was mentioned). [[line ~41](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/commands.md?plain=1#L41)]

#### [common-workflows](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* PR session resume: you can now paste a PR/MR URL directly into the `/resume` picker search box to find the session that created it (GitHub, GitHub Enterprise, GitLab, Bitbucket). [[line ~443](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/common-workflows.md?plain=1#L443)]
* Notification hook: two new event types documented — `elicitation_complete` and `elicitation_response`. [[line ~848](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/common-workflows.md?plain=1#L848)]

#### [debug-your-config](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/debug-your-config.md) [[Source](https://code.claude.com/docs/en/debug-your-config)]

* Troubleshooting link split: now distinguishes between the new `troubleshoot-install.md` (for command not found, PATH, auth issues) and `troubleshooting.md` (for performance and runtime issues). [[lines ~83–85](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/debug-your-config.md?plain=1#L83)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Six new environment variables added: [[lines ~15–153](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/env-vars.md?plain=1#L15)]
  * `ANTHROPIC_BEDROCK_SERVICE_TIER` — Bedrock service tier (`default`, `flex`, `priority`)
  * `CLAUDE_CODE_ATTRIBUTION_HEADER` — Set to `0` to omit the client version + prompt fingerprint block from the system prompt (improves prompt-cache hit rates with LLM gateways)
  * `CLAUDE_CODE_DISABLE_POLICY_SKILLS` — Set to `1` to skip loading skills from the managed skills directory (useful in container/CI)
  * `CLAUDE_CODE_EXTRA_BODY` — JSON object merged into every API request body for provider-specific parameters
  * `CLAUDE_CODE_MCP_ALLOWLIST_ENV` — Set to `1` to spawn stdio MCP servers with only a safe baseline environment instead of inheriting the full shell environment
  * `CLAUDE_CODE_USE_NATIVE_FILE_SEARCH` — Set to `1` to use Node.js file APIs instead of ripgrep for discovering commands, subagents, and output styles
* `CLAUDE_ENV_FILE`: now also populated by `Setup` hooks (in addition to SessionStart, CwdChanged, FileChanged).

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* `model not found` error: now gives inline guidance to check the model priority order (flag → env var → settings files); adds a note for Vertex AI users to check Vertex AI troubleshooting. [[lines ~427–429](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/errors.md?plain=1#L427)]

#### [fullscreen](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/fullscreen.md) [[Source](https://code.claude.com/docs/en/fullscreen)]

* New feature documented: pressing `Ctrl+L` twice within two seconds runs `/clear` in fullscreen rendering mode. First press clears the input box and shows a hint; second press clears the conversation. On macOS, double-pressing `Cmd+K` also triggers `/clear`. [[lines ~103–106](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/fullscreen.md?plain=1#L103)]
* Running `/terminal-setup` in iTerm2 now enables the OSC 52 clipboard permission automatically. [[line ~122](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/fullscreen.md?plain=1#L122)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* New `Setup` hook event added to the event table with its matcher values (`init`, `maintenance`). [[line ~411](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/hooks-guide.md?plain=1#L411)]
* Exit code 2 behavior clarified: for `Setup`, `SessionStart`, `Notification`, and similar events, exit 2 shows stderr to the user but does not block execution. [[line ~490](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/hooks-guide.md?plain=1#L490)]
* New clarification: files modified via the `Bash` tool bypass Edit/Write hooks. If all file changes need to be caught (e.g. compliance), add a Stop hook or also match `Bash`. [[lines ~535–542](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/hooks-guide.md?plain=1#L535)]
* `SubagentStart` built-in agent type renamed from `"Bash"` to `"general-purpose"` in matcher documentation.

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Hook lifecycle diagram updated to show `Setup` preceding `SessionStart`. [[lines ~14–16](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/hooks.md?plain=1#L14)]
* New `Setup` hook event fully documented: fires on `--init-only` or when `--init`/`--maintenance` is used with `-p`. Full input schema, decision control, `CLAUDE_ENV_FILE` support, and matcher values (`init`, `maintenance`) documented. [[lines ~575–635](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/hooks.md?plain=1#L575)]
* New central documentation for `additionalContext` field: comprehensive guidance on delivery timing per event type, length limits (>10,000 chars → file), phrasing (factual not imperative), and behavior on session resume. [[lines ~756–807](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/hooks.md?plain=1#L756)]
* `SubagentStart` built-in agent type renamed from `"Bash"` to `"general-purpose"` throughout.
* `Notification` hook: `additionalContext` support removed; these hooks are now "intended for side effects only." [[line ~837](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/hooks.md?plain=1#L837)]
* New notification event types: `elicitation_complete` and `elicitation_response`. [[lines ~925–1295](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/hooks.md?plain=1#L925)]

#### [jetbrains](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/jetbrains.md) [[Source](https://code.claude.com/docs/en/jetbrains)]

* WSL Configuration section fully rewritten: now provides step-by-step instructions for two fixes — (1) creating a Windows Firewall rule to allow WSL2 internal traffic, and (2) switching WSL2 to mirrored networking mode. Notes that mirrored networking requires Windows 11 22H2+. [[lines ~91–132](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/jetbrains.md?plain=1#L91)]

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* `chat:clearInput` (`Ctrl+L`): in fullscreen rendering, pressing twice within two seconds runs `/clear`. [[lines ~100–102](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/keybindings.md?plain=1#L100)]
* New `chat:clearScreen` action (`Cmd+K`): in fullscreen rendering, pressing twice within two seconds runs `/clear`.
* `Caps Lock` added to the list of keys that cannot be rebound (terminals don't deliver it as a key event). [[line ~423](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/keybindings.md?plain=1#L423)]

#### [llm-gateway](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/llm-gateway.md) [[Source](https://code.claude.com/docs/en/llm-gateway)]

* New documentation: Claude Code prepends a short attribution block (client version + conversation fingerprint) to the system prompt. The Anthropic API strips it, but LLM gateways with their own prompt cache keyed on the full request body should set `CLAUDE_CODE_ATTRIBUTION_HEADER=0` to omit it and improve cache hit rates. [[lines ~38–40](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/llm-gateway.md?plain=1#L38)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* New behavior documented: a Claude Code-added MCP server takes precedence over a claude.ai connector pointing at the same URL. `/mcp` will list the connector as hidden and show a hint on how to remove the duplicate. [[line ~1602](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/mcp.md?plain=1#L1602)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* `status_code` attribute type corrected to number in `api_error` and `api_retries_exhausted` events (was incorrectly documented as string). [[line ~537](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/monitoring-usage.md?plain=1#L537)]
* New `claude_code.at_mention` telemetry event documented: logged when Claude Code resolves an `@`-mention. Attributes include `mention_type` (`"file"`, `"directory"`, `"agent"`, `"mcp_resource"`) and `success`. Not every mention emits an event (permission denials and oversized files do not). [[lines ~687–703](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/monitoring-usage.md?plain=1#L687)]
* Security note updated: distinguishes OpenTelemetry export (opt-in) from Anthropic's separate operational telemetry, with a link to data-usage.md for how to disable the latter. [[line ~847](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/monitoring-usage.md?plain=1#L847)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* `Setup` hook event added to the event table. [[line ~98](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/plugins-reference.md?plain=1#L98)]

#### [plugins](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/plugins.md) [[Source](https://code.claude.com/docs/en/plugins)]

* Added note: to keep a plugin internal to your organization, host the marketplace in a private repository. [[line ~322](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/plugins.md?plain=1#L322)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* New limitation: WSL1 does not support sandboxing (requires WSL2 Linux namespace primitives); the error message is documented. [[lines ~50–55](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/sandboxing.md?plain=1#L50)]
* New limitation: on WSL2, sandboxed commands cannot launch Windows binaries (`cmd.exe`, `powershell.exe`, paths under `/mnt/c/`). Workaround: add the command to `excludedCommands`. [[line ~55](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/sandboxing.md?plain=1#L55)]
* Security limitations section expanded: network proxy makes allow decisions from the client-supplied hostname without TLS inspection; domain fronting can bypass the allowlist. Recommends a TLS-terminating custom proxy for stronger guarantees. [[lines ~205–208](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/sandboxing.md?plain=1#L205)]

#### [agent-sdk/secure-deployment](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/agent-sdk/secure-deployment.md) [[Source](https://code.claude.com/docs/en/agent-sdk/secure-deployment)]

* Security consideration updated: explicitly states the sandbox proxy makes allow decisions from the client-supplied hostname without terminating TLS; domain fronting is a potential bypass. Points to the sandboxing security limitations section and the TLS-terminating proxy option. [[line ~89](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/agent-sdk/secure-deployment.md?plain=1#L89)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* PowerShell tool: on Windows without Git Bash installed, the tool is now enabled automatically (no longer just "rolling out progressively" in all cases). [[line ~90](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/tools-reference.md?plain=1#L90)]

#### [troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/troubleshooting.md) [[Source](https://code.claude.com/docs/en/troubleshooting)]

* File restructured into a thin routing page: all installation troubleshooting content moved to the new `troubleshoot-install.md`. Now routes users to: `troubleshoot-install.md` (install/login), `debug-your-config.md` (settings/hooks/MCP), `errors.md` (API errors), IDE-specific pages, and a retained "Performance and stability" section.
* Added: `claude --resume` can recover a session after Claude Code becomes unresponsive.

#### [ultrareview](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/ultrareview.md) [[Source](https://code.claude.com/docs/en/ultrareview)]

* Billing clarification: a run counts once the remote session starts. Stopping early or encountering a failure still uses one free run. For paid reviews, extra usage is billed only for the portion that ran. [[line ~48](https://github.com/gpambrozio/ClaudeDocs/blob/cc85455/docs-md/claude-code/ultrareview.md?plain=1#L48)]

-----

## API changes

No significant API documentation changes today.
