# [Claude docs changes for March 22nd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/577c75b48802b56bed2622093b07afc7c0cc791f) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/577c75b48802b56bed2622093b07afc7c0cc791f)]

## Executive Summary
- Plugin agents now support additional frontmatter fields (`model`, `effort`, `maxTurns`, `disallowedTools`, `isolation`), giving developers more control over agent behavior in plugins
- New `editorMode` global config key (`"normal"` or `"vim"`) provides a file-based way to configure Vim key bindings without using `/vim`
- OpenTelemetry monitoring gains a new `user.account_id` attribute and two event-only correlation attributes (`prompt.id`, `workspace.host_paths`)
- tmux users must set `allow-passthrough on` in their tmux config to receive notifications and terminal progress bar updates through to the outer terminal

-----

## Claude Code changes

### Changed documents

#### [channels](https://github.com/gpambrozio/ClaudeDocs/blob/577c75b48802b56bed2622093b07afc7c0cc791f/docs-md/claude-code/channels.md) [[Source](https://code.claude.com/docs/en/channels)]

* Improved plugin marketplace troubleshooting instructions: now advises running `/plugin marketplace update claude-plugins-official` to refresh an outdated marketplace, or `/plugin marketplace add` if it hasn't been added, followed by `/reload-plugins` to activate the plugin. [[line 50](https://github.com/gpambrozio/ClaudeDocs/blob/577c75b48802b56bed2622093b07afc7c0cc791f/docs-md/claude-code/channels.md?plain=1#L50)] [[Source](https://code.claude.com/docs/en/channels#supported-channels)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/577c75b48802b56bed2622093b07afc7c0cc791f/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS` description updated to clarify that setting it to `1` also removes the git status snapshot from Claude's system prompt, not just the commit/PR workflow instructions. [[line 40](https://github.com/gpambrozio/ClaudeDocs/blob/577c75b48802b56bed2622093b07afc7c0cc791f/docs-md/claude-code/env-vars.md?plain=1#L40)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [github-actions](https://github.com/gpambrozio/ClaudeDocs/blob/577c75b48802b56bed2622093b07afc7c0cc791f/docs-md/claude-code/github-actions.md) [[Source](https://code.claude.com/docs/en/github-actions)]

* `--allowedTools` is now documented as the canonical flag name (camelCase), with `--allowed-tools` noted as a working alias. [[line 663](https://github.com/gpambrozio/ClaudeDocs/blob/577c75b48802b56bed2622093b07afc7c0cc791f/docs-md/claude-code/github-actions.md?plain=1#L663)] [[Source](https://code.claude.com/docs/en/github-actions#pass-cli-arguments)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/577c75b48802b56bed2622093b07afc7c0cc791f/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* `OTEL_METRICS_INCLUDE_ACCOUNT_UUID` now controls the new `user.account_id` attribute in addition to `user.account_uuid`. [[line 101](https://github.com/gpambrozio/ClaudeDocs/blob/577c75b48802b56bed2622093b07afc7c0cc791f/docs-md/claude-code/monitoring-usage.md?plain=1#L101)] [[Source](https://code.claude.com/docs/en/monitoring-usage#metrics-cardinality-control)]
* New `user.account_id` standard attribute documented: provides the account ID in tagged format matching Anthropic admin APIs (e.g. `user_01BWBeN28...`). [[line 260](https://github.com/gpambrozio/ClaudeDocs/blob/577c75b48802b56bed2622093b07afc7c0cc791f/docs-md/claude-code/monitoring-usage.md?plain=1#L260)] [[Source](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)]
* New event-only attributes documented: `prompt.id` (UUID correlating a user prompt with all subsequent events) and `workspace.host_paths` (host workspace directories selected in the desktop app). These are not attached to metrics to avoid unbounded cardinality. [[lines 264-267](https://github.com/gpambrozio/ClaudeDocs/blob/577c75b48802b56bed2622093b07afc7c0cc791f/docs-md/claude-code/monitoring-usage.md?plain=1#L264-L267)] [[Source](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)]
* Metrics segmentation section updated to include `user.account_id` alongside other segmentation dimensions. [[line 487](https://github.com/gpambrozio/ClaudeDocs/blob/577c75b48802b56bed2622093b07afc7c0cc791f/docs-md/claude-code/monitoring-usage.md?plain=1#L487)] [[Source](https://code.claude.com/docs/en/monitoring-usage#alerting-and-segmentation)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/577c75b48802b56bed2622093b07afc7c0cc791f/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* Plugin agent frontmatter example now includes `model`, `effort`, `maxTurns`, and `disallowedTools` fields. [[lines 55-60](https://github.com/gpambrozio/ClaudeDocs/blob/577c75b48802b56bed2622093b07afc7c0cc791f/docs-md/claude-code/plugins-reference.md?plain=1#L55-L60)] [[Source](https://code.claude.com/docs/en/plugins-reference#agents)]
* New documentation clarifying all supported plugin agent frontmatter fields: `name`, `description`, `model`, `effort`, `maxTurns`, `tools`, `disallowedTools`, `skills`, `memory`, `background`, and `isolation`. The only valid `isolation` value is `"worktree"`. For security, `hooks`, `mcpServers`, and `permissionMode` are not supported. [[line 66](https://github.com/gpambrozio/ClaudeDocs/blob/577c75b48802b56bed2622093b07afc7c0cc791f/docs-md/claude-code/plugins-reference.md?plain=1#L66)] [[Source](https://code.claude.com/docs/en/plugins-reference#agents)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/577c75b48802b56bed2622093b07afc7c0cc791f/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* `includeGitInstructions` description updated to note it controls both the built-in commit/PR workflow instructions and the git status snapshot in Claude's system prompt. [[line 150](https://github.com/gpambrozio/ClaudeDocs/blob/577c75b48802b56bed2622093b07afc7c0cc791f/docs-md/claude-code/settings.md?plain=1#L150)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* New `editorMode` global config setting documented: accepts `"normal"` or `"vim"`, written automatically by `/vim`, and appears in `/config` as **Key binding mode**. [[line 202](https://github.com/gpambrozio/ClaudeDocs/blob/577c75b48802b56bed2622093b07afc7c0cc791f/docs-md/claude-code/settings.md?plain=1#L202)] [[Source](https://code.claude.com/docs/en/settings#global-config-settings)]
* `terminalProgressBarEnabled` updated to list specifically supported terminals: ConEmu, Ghostty 1.2.0+, and iTerm2 3.6.6+ (previously listed "Windows Terminal" and iTerm2 without version). [[line 205](https://github.com/gpambrozio/ClaudeDocs/blob/577c75b48802b56bed2622093b07afc7c0cc791f/docs-md/claude-code/settings.md?plain=1#L205)] [[Source](https://code.claude.com/docs/en/settings#global-config-settings)]

#### [terminal-config](https://github.com/gpambrozio/ClaudeDocs/blob/577c75b48802b56bed2622093b07afc7c0cc791f/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* New section documenting tmux passthrough: users running Claude Code inside tmux must add `set -g allow-passthrough on` to their tmux config for desktop notifications and the terminal progress bar to reach the outer terminal. [[lines 46-55](https://github.com/gpambrozio/ClaudeDocs/blob/577c75b48802b56bed2622093b07afc7c0cc791f/docs-md/claude-code/terminal-config.md?plain=1#L46-L55)] [[Source](https://code.claude.com/docs/en/terminal-config#terminal-notifications)]
* Vim Mode section now documents setting `editorMode` to `"vim"` directly in `~/.claude.json` as an alternative to using `/vim`. [[line 75](https://github.com/gpambrozio/ClaudeDocs/blob/577c75b48802b56bed2622093b07afc7c0cc791f/docs-md/claude-code/terminal-config.md?plain=1#L75)] [[Source](https://code.claude.com/docs/en/terminal-config#vim-mode)]

-----

## API changes

### Changed documents

#### [remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/577c75b48802b56bed2622093b07afc7c0cc791f/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* New MCP server integrations added: Calendly (manage event types, availability, and bookings), Intuit TurboTax (estimate tax refunds and connect with live tax experts), and Tango (search for US Government Contracting Data). Several existing entries were reordered.
