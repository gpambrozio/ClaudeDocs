# [Claude docs changes for February 25th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/e7fdc94) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/e7fdc94)]

## Executive Summary
- **Remote Control** is a new feature (research preview for Pro/Max) that lets you control a local Claude Code session from a browser or mobile phone without moving anything to the cloud
- **Managed settings** now support macOS plist (via MDM configuration profiles) and Windows Registry (via Group Policy/Intune) in addition to JSON files, giving IT admins more deployment options
- **npm plugin support** is now fully implemented: plugins can be installed from npm packages with version pinning and custom private registries
- **Authentication** got a major overhaul with a new `claude auth` set of subcommands (`login`, `logout`, `status`) and improved documentation for all account types
- **Troubleshooting** was massively expanded with a comprehensive installation error table and detailed fix guides for macOS, Linux, and Windows

## New Claude Code versions

### [2.1.51](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/versions/2.1.51.md)

#### New features

* Added `claude remote-control` subcommand for external builds, enabling local environment serving for all users
* Added support for custom npm registries and specific version pinning when installing plugins from npm sources
* Added `CLAUDE_CODE_ACCOUNT_UUID`, `CLAUDE_CODE_USER_EMAIL`, and `CLAUDE_CODE_ORGANIZATION_UUID` environment variables for SDK callers to provide account info synchronously, eliminating a race condition where early telemetry events lacked account metadata

#### Existing feature improvements

* BashTool now skips login shell (`-l` flag) by default when a shell snapshot is available, improving command execution performance (previously required setting `CLAUDE_BASH_NO_LOGIN=true`)
* Tool results larger than 50K characters are now persisted to disk (previously 100K), reducing context window usage and improving conversation longevity
* The `/model` picker now shows human-readable labels (e.g., "Sonnet 4.5") instead of raw model IDs for pinned model versions, with an upgrade hint when a newer version is available
* Managed settings can now be set via macOS plist or Windows Registry

#### Major bug fixes

* Fixed a security issue where `statusLine` and `fileSuggestion` hook commands could execute without workspace trust acceptance in interactive mode
* Fixed a bug where duplicate `control_response` messages (e.g., from WebSocket reconnects) could cause API 400 errors by pushing duplicate assistant messages into the conversation
* Fixed slash command autocomplete crashing when a plugin's SKILL.md description is a YAML array or other non-string type

### [2.1.53](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/versions/2.1.53.md)

#### Major bug fixes

* Fixed a UI flicker where user input would briefly disappear after submission before the message rendered
* Fixed bulk agent kill (Ctrl+F) to send a single aggregate notification instead of one per agent, and to properly clear the command queue
* Fixed graceful shutdown sometimes leaving stale sessions when using Remote Control
* Fixed `--worktree` sometimes being ignored on first launch
* Fixed multiple crashes on Windows (panic on corrupted value, process spawning, WebAssembly interpreter, Windows ARM64 crash after 2 minutes)

### [2.1.55](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/versions/2.1.55.md)

#### Major bug fixes

* Fixed BashTool failing on Windows with EINVAL error

### [2.1.56](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/versions/2.1.56.md)

#### Major bug fixes

* VS Code: Fixed another cause of "command 'claude-vscode.editor.openLast' not found" crashes

-----

## Claude Code changes

### New Documents

#### [Remote Control](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

New feature (research preview for Pro/Max plans) that connects claude.ai/code or the Claude mobile app to a Claude Code session running on your local machine. Lets you start a task at your desk and continue it from your phone or another browser without moving anything to the cloud. Covers setup requirements, how to start sessions with `claude remote-control` or `/remote-control`, connecting from other devices via URL or QR code, security model (outbound HTTPS only, no inbound ports), and comparison with Claude Code on the web.

#### [Terminal Guide](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/terminal-guide.md) [[Source](https://code.claude.com/docs/en/terminal-guide)]

A beginner-friendly guide for users who have never used a terminal before. Covers how to open a terminal on macOS, Linux, and Windows; install Claude Code; and take first steps. Includes platform-specific troubleshooting for common errors (command not found, SSL errors, Git Bash missing, etc.).

### Changed Documents

#### [Authentication](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/authentication.md) [[Source](https://code.claude.com/docs/en/authentication)]

* Added a new "Log in to Claude Code" section at the top documenting the first-launch browser login flow and all supported account types (Pro/Max, Teams/Enterprise, Console, cloud providers). [[lines 1-20](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/authentication.md?plain=1#L1-L20)] [[Source](https://code.claude.com/docs/en/authentication)]
* Updated cloud provider list to include Microsoft Foundry (was previously "Microsoft Azure"). [[line 92](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/authentication.md?plain=1#L92)] [[Source](https://code.claude.com/docs/en/authentication#claude-console-authentication)]

#### [CLI Reference](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Added three new `claude auth` subcommands: `claude auth login` (with `--email` and `--sso` flags), `claude auth logout`, and `claude auth status` (outputs JSON; `--text` for human-readable; exit code 0 if logged in). [[lines 13-15](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/cli-reference.md?plain=1#L13-L15)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-commands)]
* Added `claude remote-control` subcommand for starting a Remote Control session. [[line 18](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/cli-reference.md?plain=1#L18)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-commands)]

#### [Claude Code on the Web](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* Added Android app link alongside iOS. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L15)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#what-is-claude-code-on-the-web)]
* Added reference to Remote Control as an option for using the web UI while running locally. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L15)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#what-is-claude-code-on-the-web)]

#### [Data Usage](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/data-usage.md) [[Source](https://code.claude.com/docs/en/data-usage)]

* Clarified that Remote Control sessions follow the local Claude Code data flow since all execution happens on the user's machine. [[line 42](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/data-usage.md?plain=1#L42)] [[Source](https://code.claude.com/docs/en/data-usage#data-access)]

#### [How Claude Code Works](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/how-claude-code-works.md) [[Source](https://code.claude.com/docs/en/how-claude-code-works)]

* Updated the built-in tool categories count from 4 to 5. [[line 23](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/how-claude-code-works.md?plain=1#L23)] [[Source](https://code.claude.com/docs/en/how-claude-code-works#tools)]
* Added a new "Environments and interfaces" section explaining the three execution environments (Local, Cloud, Remote Control) and available interfaces (terminal, desktop, IDE, web, Remote Control, Slack, CI/CD). [[lines 58-70](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/how-claude-code-works.md?plain=1#L58-L70)] [[Source](https://code.claude.com/docs/en/how-claude-code-works#environments-and-interfaces)]

#### [Index / Overview](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/index.md) [[Source](https://code.claude.com/docs/en/index)]

* Added Windows requirement for Git for Windows to the installation section. [[line 57](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/index.md?plain=1#L57)] [[Source](https://code.claude.com/docs/en/index#get-started)]
* Added Remote Control to the "Work from anywhere" section and the interface comparison table. [[lines 198-210](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/index.md?plain=1#L198-L210)] [[Source](https://code.claude.com/docs/en/index#what-you-can-do)]

#### [Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Clarified that `/path` patterns are relative to the project root (not the settings file). [[line 135](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/permissions.md?plain=1#L135)] [[Source](https://code.claude.com/docs/en/permissions#read-and-edit)]
* Added four new managed-only settings: `allowManagedMcpServersOnly` (restricts MCP servers to admin allowlist only), `blockedMarketplaces` (pre-download blocklist for marketplace sources), `sandbox.network.allowManagedDomainsOnly` (restricts allowed domains to managed settings only), and `allow_remote_sessions` (controls whether users can start Remote Control and web sessions). [[lines 221-230](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/permissions.md?plain=1#L221-L230)] [[Source](https://code.claude.com/docs/en/permissions#managed-only-settings)]
* Updated managed settings description to reflect that settings can now be delivered through MDM/OS-level policies, managed settings files, or server-managed settings. [[line 213](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/permissions.md?plain=1#L213)] [[Source](https://code.claude.com/docs/en/permissions#managed-settings)]

#### [Plugin Marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Added full documentation for npm package sources, including version pinning (`version` field) and custom private registries (`registry` field). [[lines 387-440](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/plugin-marketplaces.md?plain=1#L387-L440)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#npm-packages)]
* Added troubleshooting section for git operation timeouts with instructions for the `CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS` environment variable. [[lines 936-953](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/plugin-marketplaces.md?plain=1#L936-L953)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#git-operations-time-out)]
* Removed the warning that npm source is not yet fully implemented.

#### [Quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/quickstart.md) [[Source](https://code.claude.com/docs/en/quickstart)]

* Added link to the new terminal guide for users new to the command line. [[line 10](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/quickstart.md?plain=1#L10)] [[Source](https://code.claude.com/docs/en/quickstart#before-you-begin)]
* Added Windows requirement note for Git for Windows. [[line 60](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/quickstart.md?plain=1#L60)] [[Source](https://code.claude.com/docs/en/quickstart#step-1-install-claude-code)]

#### [Security](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/security.md) [[Source](https://code.claude.com/docs/en/security)]

* Added explanation of how Remote Control sessions work from a security standpoint: traffic flows through the Anthropic API over TLS, code executes locally, no cloud VMs or sandboxing, and uses multiple short-lived narrowly scoped credentials. [[line 93](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/security.md?plain=1#L93)] [[Source](https://code.claude.com/docs/en/security#cloud-execution-security)]

#### [Server-Managed Settings](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* Updated endpoint-managed settings description to reflect new delivery options: MDM configuration profiles, registry policies, or managed settings files (in addition to the existing JSON file approach). [[lines 18-24](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/server-managed-settings.md?plain=1#L18-L24)] [[Source](https://code.claude.com/docs/en/server-managed-settings#choose-between-server-managed-and-endpoint-managed-settings)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Expanded the managed settings section to document three delivery mechanisms: server-managed settings, MDM/OS-level policies (macOS `com.anthropic.claudecode` plist via Jamf/Kandji; Windows `HKLM\SOFTWARE\Policies\ClaudeCode` registry via Group Policy/Intune), and file-based (`managed-settings.json`). [[lines 27-35](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/settings.md?plain=1#L27-L35)] [[Source](https://code.claude.com/docs/en/settings#when-to-use-each-scope)]
* Added new settings: `allowManagedMcpServersOnly`, `blockedMarketplaces`, and `network.allowManagedDomainsOnly`. [[lines 43-59](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/settings.md?plain=1#L43-L59)] [[Source](https://code.claude.com/docs/en/settings#when-to-use-each-scope)]
* Added new environment variables: `CLAUDE_CODE_ACCOUNT_UUID`, `CLAUDE_CODE_USER_EMAIL`, `CLAUDE_CODE_ORGANIZATION_UUID` (for SDK account info), and `CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS` (git operation timeout for plugins). [[lines 100-119](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/settings.md?plain=1#L100-L119)] [[Source](https://code.claude.com/docs/en/settings#settings-files)]
* Added precedence ordering within the managed tier: server-managed > MDM/OS-level > `managed-settings.json` > HKCU registry. [[line 72](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/settings.md?plain=1#L72)] [[Source](https://code.claude.com/docs/en/settings#settings-files)]
* Added documentation for the `/status` command to verify which settings sources are active and their origins. [[lines 80-82](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/settings.md?plain=1#L80-L82)] [[Source](https://code.claude.com/docs/en/settings#settings-files)]

#### [Setup](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* Major restructure: added Windows Git Bash requirement to system requirements, added a new "Verify your installation" section, improved the Windows setup section (Git Bash path configuration in settings.json), and reorganized the update and install sections for clarity. [[lines 1-200](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/setup.md?plain=1#L1-L200)] [[Source](https://code.claude.com/docs/en/setup)]
* Deprecated npm installation section now includes explicit migration steps from npm to native binary. [[lines 380-415](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/setup.md?plain=1#L380-L415)] [[Source](https://code.claude.com/docs/en/setup#deprecated-npm-installation)]
* Binary integrity and code signing information moved and clarified (SHA256 checksums URL format, macOS/Windows signing details). [[lines 410-430](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/setup.md?plain=1#L410-L430)] [[Source](https://code.claude.com/docs/en/setup#install-with-npm)]

#### [Sub-Agents](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Removed the incorrect statement that MCP tools are not available in background subagents. [[line 728](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/sub-agents.md?plain=1#L728)] [[Source](https://code.claude.com/docs/en/sub-agents#auto-compaction)]

#### [Troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/troubleshooting.md) [[Source](https://code.claude.com/docs/en/troubleshooting)]

* Massively expanded with a comprehensive installation troubleshooting section: a quick-reference error table mapping common error messages to solutions, and detailed fix guides for network connectivity, PATH issues, Windows-specific errors (Git Bash, irm not recognized), Linux binary mismatches, macOS binary issues, and more. [[lines 1-600](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/claude-code/troubleshooting.md?plain=1#L1-L600)] [[Source](https://code.claude.com/docs/en/troubleshooting#troubleshoot-installation-issues)]

-----

## API changes

### Changed Documents

#### [Remote MCP Servers](https://github.com/gpambrozio/ClaudeDocs/blob/e7fdc94/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Reordering of MCP server entries in the listing (no new servers or substantive content changes).
