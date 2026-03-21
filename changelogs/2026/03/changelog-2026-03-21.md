# [Claude docs changes for March 21st, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/dfd9604) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/dfd9604)]

## Executive Summary
- Claude Code 2.1.81 adds a `--bare` flag for streamlined scripted use and a `--channels` permission relay to forward tool approval prompts to your phone
- Rate limit usage (5-hour and 7-day windows) is now exposed in the status line for Pro/Max subscribers
- Server-managed settings now support hooks, enabling org-wide shell command automation after tool use
- Two new global config settings (`autoConnectIde`, `autoInstallIdeExtension`) control IDE extension behavior
- Skills gain an `effort` field to override the session-level thinking effort per skill

## New Claude Code versions

### [2.1.81](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/versions/2.1.81.md)

#### New features

* Added `--bare` flag for scripted `-p` calls — skips hooks, LSP, plugin sync, and skill directory walks; requires `ANTHROPIC_API_KEY` or an `apiKeyHelper` via `--settings` (OAuth and keychain auth disabled); auto-memory fully disabled
* Added `--channels` permission relay — channel servers that declare the permission capability can forward tool approval prompts to your phone

#### Existing feature improvements

* MCP read/search tool calls now collapse into a single "Queried {server}" line (expandable with Ctrl+O)
* `!` bash mode is now more discoverable — Claude suggests it when you need to run an interactive command
* Plugin freshness improved — ref-tracked plugins now re-clone on every load to pick up upstream changes
* Remote Control session titles now refresh after your third message
* MCP OAuth updated to support Client ID Metadata Document (CIMD / SEP-991) for servers without Dynamic Client Registration
* Plan mode now hides the "clear context" option by default (restore with `"showClearContextOnPlanAccept": true`)

#### Major bug fixes

* Fixed multiple concurrent Claude Code sessions requiring repeated re-authentication when one session refreshes its OAuth token
* Fixed `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` not suppressing the structured-outputs beta header, causing 400 errors on proxy gateways forwarding to Vertex/Bedrock
* Fixed unnecessary permission prompts for Bash commands containing dashes in strings
* Fixed plugin hooks blocking prompt submission when the plugin directory is deleted mid-session
* Fixed a race condition where background agent task output could hang indefinitely when the task completed between polling intervals
* Fixed voice mode silently swallowing retry failures and showing a misleading "check your network" message
* Fixed voice mode audio not recovering when the server silently drops the WebSocket connection
* Fixed `--channels` bypass for Team/Enterprise orgs with no other managed settings configured
* Fixed a crash on Node.js 18
* Resuming a session that was in a worktree now switches back to that worktree
* Fixed Remote Control `/exit` not reliably archiving the session
* [VSCode] Fixed Windows PATH inheritance for Bash tool when using Git Bash (regression in v2.1.78)

-----

## Claude Code changes

### Changed documents

#### [channels](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/channels.md) [[Source](https://code.claude.com/docs/en/channels)]

* Added a new "How channels compare" section with a table comparing Channels to web sessions, Slack integration, standard MCP servers, and Remote Control. [[lines 332-347](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/channels.md?plain=1#L332-L347)] [[Source](https://code.claude.com/docs/en/channels#research-preview)]
* Clarification that the `--channels` flag also serves as a permission relay. Added to the intro paragraph. [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/channels.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/channels)]
* Telegram and Discord token config files are now saved to `~/.claude/channels/<name>/.env` (user-level), not `.claude/channels/<name>/.env` in the project. [[lines 65, 178](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/channels.md?plain=1#L65)]
* Added troubleshooting tip: if a plugin is not found, run `/plugin marketplace add anthropics/claude-plugins-official` first. [[lines 47, 160, 256](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/channels.md?plain=1#L47)]

#### [channels-reference](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/channels-reference.md) [[Source](https://code.claude.com/docs/en/channels-reference)]

* Clarified that the MCP config location is no longer specifically `.mcp.json` — references updated to "your MCP config" and note that user-level config lives in `~/.claude.json`. [[lines 122, 140, 158](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/channels-reference.md?plain=1#L122)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Updated `--channels` flag description to note it is a research preview, requires Claude.ai authentication, and clarified what the argument format accepts. [[line 33](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/cli-reference.md?plain=1#L33)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Admin settings descriptions updated: "Enable or disable the Code tab" renamed to "Code in the desktop"; "Disable Claude Code on the web" replaced with separate "Code in the web" and "Remote Control" toggles. [[lines 412-415](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/desktop.md?plain=1#L412)] [[Source](https://code.claude.com/docs/en/desktop#admin-console-controls)]

#### [discover-plugins](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* Added a link to the plugin catalog at `claude.com/plugins` for browsing available plugins. [[line 23](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/discover-plugins.md?plain=1#L23)] [[Source](https://code.claude.com/docs/en/discover-plugins#how-marketplaces-work)]
* Install example updated to use a concrete plugin name (`github@claude-plugins-official`) instead of a placeholder. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/discover-plugins.md?plain=1#L36)] [[Source](https://code.claude.com/docs/en/discover-plugins#official-anthropic-marketplace)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `CLAUDE_CODE_IDE_SKIP_AUTO_INSTALL` description now cross-references the equivalent `autoInstallIdeExtension` setting in settings.md. [[line 52](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/env-vars.md?plain=1#L52)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Removed the `allow_remote_sessions` managed settings key. Access to Remote Control and web sessions is now controlled via the admin UI at `claude.ai/admin-settings/claude-code`, not a settings key. [[line 236](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/permissions.md?plain=1#L236)] [[Source](https://code.claude.com/docs/en/permissions#managed-only-settings)]

#### [plugin-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Removed `pip` as a supported plugin source type from the source types table. [[line 269](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/plugin-marketplaces.md?plain=1#L269)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#plugin-sources)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Improved "Remote Control is disabled" troubleshooting: recommends running `/status` first, and clarifies that the Team/Enterprise admin toggle is a server-side org setting, not a managed settings key. [[lines 161-164](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/remote-control.md?plain=1#L161)] [[Source](https://code.claude.com/docs/en/remote-control#”remote-control-is-disabled-by-your-organization’s-policy”)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Added clarification that `.` in `allowRead` resolves relative to where the settings file lives (project root for project settings, `~/.claude` for user settings). [[lines 165-167](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/sandboxing.md?plain=1#L165)] [[Source](https://code.claude.com/docs/en/sandboxing#granting-subprocess-write-access-to-specific-paths)]

#### [server-managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* Documented that server-managed settings now support `hooks` and environment variables in addition to standard settings. Added a hooks configuration example that runs an org-wide audit script after every file edit. [[lines 36, 58-83](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/server-managed-settings.md?plain=1#L58)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `autoConnectIde` global config setting: automatically connect to a running IDE when Claude Code starts from an external terminal. [[line 197](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/settings.md?plain=1#L197)] [[Source](https://code.claude.com/docs/en/settings#global-config-settings)]
* Added `autoInstallIdeExtension` global config setting: automatically install the Claude Code IDE extension when running from a VS Code terminal. [[line 198](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/settings.md?plain=1#L198)] [[Source](https://code.claude.com/docs/en/settings#global-config-settings)]
* Added `settings` as an inline marketplace source type for `extraKnownMarketplaces`, allowing small plugin sets to be declared directly in `settings.json` without a separate hosted repository. [[lines 635-668](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/settings.md?plain=1#L635)] [[Source](https://code.claude.com/docs/en/settings#extraknownmarketplaces)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Added `effort` field to skill frontmatter: overrides the session effort level for this skill. Options: `low`, `medium`, `high`, `max` (Opus 4.6 only). [[line 229](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/skills.md?plain=1#L229)] [[Source](https://code.claude.com/docs/en/skills#frontmatter-reference)]

#### [statusline](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/statusline.md) [[Source](https://code.claude.com/docs/en/statusline)]

* Added `rate_limits` fields to the status line JSON schema: `rate_limits.five_hour.used_percentage`, `rate_limits.five_hour.resets_at`, `rate_limits.seven_day.used_percentage`, and `rate_limits.seven_day.resets_at`. Only present for Claude.ai Pro/Max subscribers after the first API response. [[lines 183-185](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/statusline.md?plain=1#L183)] [[Source](https://code.claude.com/docs/en/statusline#available-data)]
* Added example Bash script showing how to display 5-hour and 7-day rate limit usage alongside the model name, with graceful handling when `rate_limits` is absent. [[lines 523-561](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/statusline.md?plain=1#L523)] [[Source](https://code.claude.com/docs/en/statusline#clickable-links)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Clarified `tools` vs `disallowedTools` with separate examples: `tools` is an exclusive allowlist, `disallowedTools` removes specific tools while inheriting the rest. Added rule that when both are set, `disallowedTools` is applied first. [[lines 269-304](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/claude-code/sub-agents.md?plain=1#L269)] [[Source](https://code.claude.com/docs/en/sub-agents#available-tools)]

-----

## API changes

### Changed documents

#### [overview](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/api/build-with-claude/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

* Added "(GA)" availability status labels to all generally available features in the capabilities, tools, and context management tables (e.g., "Claude API" → "Claude API (GA)"). [[lines 33-95](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/api/build-with-claude/overview.md?plain=1#L33)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

#### [remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Various MCP server entries reordered throughout the listing.
* Added Airtable as a new remote MCP server entry: "Bring your structured data to Claude" at `https://mcp.airtable.com/mcp`. [[line 302](https://github.com/gpambrozio/ClaudeDocs/blob/dfd9604/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L302)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
