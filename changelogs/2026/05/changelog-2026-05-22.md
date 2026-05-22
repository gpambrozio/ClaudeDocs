# [Claude docs changes for May 22nd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/73e0bbc14c7aada457276082377e714f39c765eb) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/73e0bbc14c7aada457276082377e714f39c765eb)]

## Executive Summary
- Auto mode is now available to **all users** on the Anthropic API (previously restricted to Max, Team, Enterprise, and API plans)
- `/simplify` has been renamed to `/code-review` with new behavior: it now reports correctness bugs at a configurable effort level and can post inline GitHub PR comments with `--comment`
- Two new documents added: a dedicated guide for organizational MCP server control (`managed-mcp.md`) and a new sandbox environments comparison guide (`sandbox-environments.md`)
- MCP servers now support a per-server `timeout` field in `.mcp.json`, overriding the global `MCP_TOOL_TIMEOUT` for individual servers
- Git for Windows is now optional on native Windows installs — Claude Code falls back to the PowerShell tool when Git Bash is absent

## New Claude Code versions

### [2.1.147](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/versions/2.1.147.md)

#### New features

* Pinned background sessions (`Ctrl+T` in `claude agents`) now stay alive when idle, are restarted in place to apply Claude Code updates, and are shed under memory pressure only after non-pinned sessions
* Renamed `/simplify` to `/code-review` — it now reports correctness bugs at a chosen effort level (e.g., `/code-review high`); pass `--comment` to post findings as inline GitHub PR comments. The old cleanup-and-fix behavior has been removed

#### Existing feature improvements

* Improved auto-updater: retries transient network failures, reports specific error categories and OS error codes on failure, and shows the current version when an update fails
* Improved diff rendering performance for large file edits
* Prompt history no longer records consecutive duplicate entries — recalling a prompt with arrow-up and submitting it again won't add another copy

#### Major bug fixes

* Fixed enterprise login restrictions (`forceLoginOrgUUID` and `forceLoginMethod` managed-settings) not being enforced against third-party-provider and API-key sessions
* Fixed `&` in `!` command output displaying as `&amp;`, which broke copy-pasting URLs from commands like `gcloud auth login` on headless machines
* Fixed unknown slash commands silently doing nothing in headless/SDK mode — they now show an error message
* Fixed plugin agents that declare multiple `Agent(...)` types in `tools:` frontmatter dropping all but the last entry
* Fixed hook `if` conditions like `PowerShell(git push*)` never matching — only `PowerShell(*)` worked
* Fixed PowerShell tool failing on Windows with exit code 1 when `pwsh` is installed via winget or the Microsoft Store
* Fixed paginating MCP servers dropping resources, templates, and prompts past page 1
* Fixed auto mode suppressing `AskUserQuestion` when the user or a skill explicitly relies on it
* Fixed pasted text being delivered to agents as an unreadable `[Pasted text #N]` placeholder instead of the actual content
* Fixed backgrounded sessions re-prompting for tool permissions you already granted with "don't ask again"
* Fixed `CLAUDE_CODE_SUBAGENT_MODEL` not applying to teammate processes spawned by agent teams
* Fixed slash commands followed by a tab or newline being treated as an unknown command
* Fixed an uncaught exception at the end of streaming sessions when running via the Agent SDK

### [2.1.148](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/versions/2.1.148.md)

#### Major bug fixes

* Fixed the Bash tool returning exit code 127 on every command for some users (a regression introduced in 2.1.147)

-----

## Claude Code changes

### New Documents

#### [Control MCP server access for your organization](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/managed-mcp.md) [[Source](https://code.claude.com/docs/en/managed-mcp)]

New dedicated guide for administrators controlling MCP server access in an organization. Covers deploying a fixed server set with `managed-mcp.json` (including how to disable MCP entirely), restricting servers with `allowedMcpServers`/`deniedMcpServers` allowlists and denylists, how a server is evaluated through the full chain of checks, how restrictions appear to users, and monitoring MCP usage via OpenTelemetry. The managed MCP configuration content was previously embedded in `mcp.md` and has been moved and significantly expanded here.

#### [Choose a sandbox environment](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/sandbox-environments.md) [[Source](https://code.claude.com/docs/en/sandbox-environments)]

New comparison guide covering all available isolation approaches: the sandboxed Bash tool, sandbox runtime (`@anthropic-ai/sandbox-runtime`), dev containers, custom containers, virtual machines, and Claude Code on the web. Explains how isolation relates to permission modes (including `--dangerously-skip-permissions` and auto mode), and covers how organizations can enforce isolation across all developers.

### Changed documents

#### [Admin setup](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/admin-setup.md) [[Source](https://code.claude.com/docs/en/admin-setup)]

* MCP server control row updated to reference the new `managed-mcp.md` guide and now explicitly mentions deploying a fixed server set via `managed-mcp.json` [[line 66](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/admin-setup.md?plain=1#L66)] [[Source](https://code.claude.com/docs/en/admin-setup#decide-what-to-enforce)]

#### [Agent SDK TypeScript reference](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Added clarification on the `signal` field in `SpawnOptions`: the signal does not fire the instant `abortController` aborts — the SDK first closes stdin and waits ~2 seconds for clean shutdown before aborting [[line 2864](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L2864)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#spawnoptions)]

#### [Agent view](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* Pinned sessions (`Ctrl+T`) now keep their process running while idle, and idle pinned sessions are restarted in place onto new Claude Code versions [[line 382](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/agent-view.md?plain=1#L382)] [[Source](https://code.claude.com/docs/en/agent-view#the-supervisor-process)]
* When the host runs low on memory, the supervisor stops idle non-pinned sessions first [[line 384](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/agent-view.md?plain=1#L384)] [[Source](https://code.claude.com/docs/en/agent-view#the-supervisor-process)]

#### [Auto mode configuration](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/auto-mode-config.md) [[Source](https://code.claude.com/docs/en/auto-mode-config)]

* Auto mode is now available to all users on the Anthropic API (previously Max, Team, Enterprise, and API plans only) [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/auto-mode-config.md?plain=1#L11)] [[Source](https://code.claude.com/docs/en/auto-mode-config)]

#### [Commands](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* Added `/code-review` command entry with full description: reviews the diff for correctness bugs at a configurable effort level, supports `--comment` to post inline GitHub PR comments, formerly `/simplify` [[line 42](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/commands.md?plain=1#L42)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]
* Removed `/simplify` entry (replaced by `/code-review`)
* Updated "Before you ship" workflow tip to reference `/code-review` instead of `/simplify`

#### [Desktop](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Auto mode plan requirements updated: now available to all users on the Anthropic API, not just Max/Team/Enterprise/API plans [[line 74](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/desktop.md?plain=1#L74)] [[Source](https://code.claude.com/docs/en/desktop#choose-a-permission-mode)]

#### [Dev container](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/devcontainer.md) [[Source](https://code.claude.com/docs/en/devcontainer)]

* Added link to new `sandbox-environments.md` in the "See also" section [[line 178](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/devcontainer.md?plain=1#L178)] [[Source](https://code.claude.com/docs/en/devcontainer#next-steps)]

#### [Environment variables](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `MCP_TOOL_TIMEOUT` description now notes that a per-server `timeout` field in `.mcp.json` overrides it for that server, and values below 1000 are floored to one second [[line 306](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/env-vars.md?plain=1#L306)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CLAUDE_CODE_ALT_SCREEN_FULL_REPAINT` description updated to note it is also auto-enabled for agent view on Windows (not just background sessions) [[line 136](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/env-vars.md?plain=1#L136)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [Errors](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* Added new "Unable to resize image" error section covering four variants of the error with specific fix guidance [[lines 465-483](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/errors.md?plain=1#L465-L483)] [[Source](https://code.claude.com/docs/en/errors#image-was-too-large)]
* 5xx error messages now reflect the inference provider (Bedrock, Vertex AI, Foundry, or custom gateway) rather than being Anthropic-specific [[lines 64-100](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/errors.md?plain=1#L64-L100)] [[Source](https://code.claude.com/docs/en/errors#automatic-retries)]
* 429 rate limit error: trailing sentence now also names Foundry and custom `ANTHROPIC_BASE_URL` gateways [[line 201](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/errors.md?plain=1#L201)] [[Source](https://code.claude.com/docs/en/errors#request-rejected-429)]

#### [Glossary](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/glossary.md) [[Source](https://code.claude.com/docs/en/glossary)]

* Auto mode entry updated: now available to all users on the Anthropic API [[line 40](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/glossary.md?plain=1#L40)] [[Source](https://code.claude.com/docs/en/glossary#auto-mode)]
* Bundled skills entry updated to reference `/code-review` instead of `/simplify` [[line 52](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/glossary.md?plain=1#L52)] [[Source](https://code.claude.com/docs/en/glossary#bundled-skills)]

#### [Interactive mode](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Added note that submitting the same prompt twice records only one history entry [[line 208](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/interactive-mode.md?plain=1#L208)] [[Source](https://code.claude.com/docs/en/interactive-mode#command-history)]

#### [Keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* `permission:toggleDebug` is now unbound — the previous default of `Ctrl+D` was removed in v2.1.146 because it shadowed `app:exit` [[line 152](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/keybindings.md?plain=1#L152)] [[Source](https://code.claude.com/docs/en/keybindings#permission-actions)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Added per-server `timeout` field: set `"timeout": <ms>` in a server's `.mcp.json` entry to override `MCP_TOOL_TIMEOUT` for that server only. Values below 1000 are floored to 1 second; HTTP/SSE first-byte budget has a 60-second minimum [[lines 157-159](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/mcp.md?plain=1#L157-L159)] [[Source](https://code.claude.com/docs/en/mcp#push-messages-with-channels)]
* The large "Managed MCP configuration" section has been replaced with a short pointer to the new `managed-mcp.md` guide [[line 996](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/mcp.md?plain=1#L996)] [[Source](https://code.claude.com/docs/en/mcp#managed-mcp-configuration)]

#### [Model configuration](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* `CLAUDE_CODE_SUBAGENT_MODEL` now applies to agent teams in addition to subagents, and supports `inherit` to use normal model resolution [[line 273](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/model-config.md?plain=1#L273)] [[Source](https://code.claude.com/docs/en/model-config#environment-variables)]

#### [Permission modes](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Auto mode plan requirement updated: now available on all plans; supported models list no longer distinguishes Max vs. other plans [[lines 141-144](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/permission-modes.md?plain=1#L141-L144)] [[Source](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode)]
* Auto mode now notes it still allows `AskUserQuestion` when a prompt or skill explicitly relies on it [[line 141](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/permission-modes.md?plain=1#L141)] [[Source](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode)]

#### [Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* `allowManagedPermissionRulesOnly` clarified: it does not affect the MCP server allowlist; use `allowManagedMcpServersOnly` for that [[line 302](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/permissions.md?plain=1#L302)] [[Source](https://code.claude.com/docs/en/permissions#managed-only-settings)]

#### [Plugin marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Three new reserved marketplace names added: `claude-for-legal`, `claude-for-financial-services`, `financial-services-plugins` [[line 171](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/plugin-marketplaces.md?plain=1#L171)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#required-fields)]

#### [Sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Major restructure: renamed to "Configure the sandboxed Bash tool" with new step-by-step setup guide (`/sandbox` → choose mode → run a command) [[lines 18-50](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/sandboxing.md?plain=1#L18-L50)] [[Source](https://code.claude.com/docs/en/sandboxing)]
* Ubuntu 24.04 AppArmor check now includes a command to verify whether the restriction applies before applying the profile fix [[line 85](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/sandboxing.md?plain=1#L85)] [[Source](https://code.claude.com/docs/en/sandboxing#set-up-linux-and-wsl2)]
* Added new "How sandboxing relates to permissions and permission modes" section with a clear table comparing sandbox settings vs. permission rules [[lines 165-210](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/sandboxing.md?plain=1#L165-L210)] [[Source](https://code.claude.com/docs/en/sandboxing#configure-sandboxing)]
* Default read behavior now explicitly warns that credential files (`~/.aws/credentials`, `~/.ssh/`) are readable by default and should be added to `denyRead` to block them [[line 172](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/sandboxing.md?plain=1#L172)] [[Source](https://code.claude.com/docs/en/sandboxing#filesystem-isolation)]
* `allowUnsandboxedCommands: false` ("Strict sandbox mode") now shown in the `/sandbox` Overrides tab [[line 133](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/sandboxing.md?plain=1#L133)] [[Source](https://code.claude.com/docs/en/sandboxing#configure-sandboxing)]

#### [Scheduled tasks](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/scheduled-tasks)]

* Removed the statement that the built-in maintenance prompt "isn't available to everyone yet"; it now simply states it is unavailable on Bedrock, Vertex AI, and Foundry [[line 85](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/scheduled-tasks.md?plain=1#L85)] [[Source](https://code.claude.com/docs/en/scheduled-tasks#run-the-built-in-maintenance-prompt)]

#### [Security](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/security.md) [[Source](https://code.claude.com/docs/en/security)]

* Added link to new `sandbox-environments.md` in related resources [[line 132](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/security.md?plain=1#L132)] [[Source](https://code.claude.com/docs/en/security#related-resources)]

#### [Server-managed settings](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* Limitation note updated: clarifies that `managed-mcp.json` cannot be distributed through server-managed settings, but `allowedMcpServers` and `deniedMcpServers` policy keys can be [[line 123](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/server-managed-settings.md?plain=1#L123)] [[Source](https://code.claude.com/docs/en/server-managed-settings#current-limitations)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* `forceLoginMethod` now documented to block API key, `apiKeyHelper`, and third-party provider sessions when set in managed settings [[line 201](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/settings.md?plain=1#L201)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* `forceLoginOrgUUID` similarly clarified to block API key and third-party provider sessions (organization membership cannot be verified for them) [[line 202](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/settings.md?plain=1#L202)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

#### [Setup](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* Git for Windows is now optional on native Windows — Claude Code uses the PowerShell tool when Git Bash is absent [[lines 91-117](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/setup.md?plain=1#L91-L117)] [[Source](https://code.claude.com/docs/en/setup#set-up-on-windows)]
* Windows setup section renamed from "Native Windows with Git Bash" to "Native Windows" [[line 91](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/setup.md?plain=1#L91)] [[Source](https://code.claude.com/docs/en/setup#set-up-on-windows)]

#### [Skills](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Updated bundled skills list to reference `/code-review` instead of `/simplify` [[lines 12-16](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/skills.md?plain=1#L12-L16)] [[Source](https://code.claude.com/docs/en/skills)]

#### [Terminal guide](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/terminal-guide.md) [[Source](https://code.claude.com/docs/en/terminal-guide)]

* Git for Windows install step now marked as optional; updated description clarifies it enables the Bash tool, and Claude Code falls back to PowerShell without it [[lines 65-70](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/terminal-guide.md?plain=1#L65-L70)] [[Source](https://code.claude.com/docs/en/terminal-guide#windows)]
* Error message fix for "Claude Code on Windows requires either Git for Windows or PowerShell": guidance reordered to lead with ensuring `powershell.exe` is on PATH [[lines 241-250](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/terminal-guide.md?plain=1#L241-L250)] [[Source](https://code.claude.com/docs/en/terminal-guide#windows-troubleshooting)]

#### [Tools reference](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* PowerShell tool now documented to spawn with `-ExecutionPolicy Bypass` at process scope; does not override Group Policy. Set `CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY=1` to use the machine's effective policy instead [[line 211](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/tools-reference.md?plain=1#L211)] [[Source](https://code.claude.com/docs/en/tools-reference#enable-the-powershell-tool)]

#### [Troubleshoot install](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/troubleshoot-install.md) [[Source](https://code.claude.com/docs/en/troubleshoot-install)]

* Added `curl: (22) 403` error to the quick-reference table and expanded the install-script-returns-HTML section to explain bare 403 responses (can be a proxy/firewall issue, not just regional blocking) [[lines 18-20, 272-279](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/troubleshoot-install.md?plain=1#L18-L20)]
* `curl: (56)` section now also covers `curl: (23)` and explains the difference between the two exit codes [[line 313](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/troubleshoot-install.md?plain=1#L313)] [[Source](https://code.claude.com/docs/en/troubleshoot-install#curl-56-failure-writing-output-to-destination)]
* Windows shell error guidance updated: Git for Windows is now optional; fix leads with adding `powershell.exe` to PATH [[lines 494-504](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/claude-code/troubleshoot-install.md?plain=1#L494-L504)] [[Source](https://code.claude.com/docs/en/troubleshoot-install#claude-desktop-overrides-the-claude-command-on-windows)]

-----

## API changes

### Changed documents

#### [Deploy MCP tunnels with Docker Compose](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/api/agents-and-tools/mcp-tunnels/deploy-compose.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-compose)]

* Container and config file renamed from `mcp-gateway` to `mcp-proxy` throughout: service name, volume mount (`mcp-gateway.yaml` → `mcp-proxy.yaml`), and `network_mode` reference [[lines 103-130, 194](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/api/agents-and-tools/mcp-tunnels/deploy-compose.md?plain=1#L103-L130)]

#### [MCP tunnels quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/api/agents-and-tools/mcp-tunnels/quickstart.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/quickstart)]

* Docker Compose service and config file renamed from `mcp-gateway` to `mcp-proxy` in all quickstart examples and log commands [[lines 123-177](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/api/agents-and-tools/mcp-tunnels/quickstart.md?plain=1#L123-L177)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/quickstart)]

#### [MCP tunnels reference](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/api/agents-and-tools/mcp-tunnels/reference.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/reference)]

* Default `--output` Kubernetes secret name changed from `k8s-secret:mcp-gateway` to `k8s-secret:mcp-tunnel` for both the `setup` and `renew-cert` subcommands [[lines 81, 93](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/api/agents-and-tools/mcp-tunnels/reference.md?plain=1#L81)]

#### [MCP tunnels troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/api/agents-and-tools/mcp-tunnels/troubleshooting.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/troubleshooting)]

* Troubleshooting table and restart commands updated to use `mcp-proxy` service name instead of `mcp-gateway` [[lines 14-15, 35, 109](https://github.com/gpambrozio/ClaudeDocs/blob/73e0bbc14c7aada457276082377e714f39c765eb/docs-md/api/agents-and-tools/mcp-tunnels/troubleshooting.md?plain=1#L14-L15)]
