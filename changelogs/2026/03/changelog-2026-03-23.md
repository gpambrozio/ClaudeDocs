# [Claude docs changes for March 23rd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/ae8af7d6ed211664f84218975d50b3a2cd387439) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/ae8af7d6ed211664f84218975d50b3a2cd387439)]

## Executive Summary
- New `--bare` mode for headless/scripted Claude Code calls: skips hooks, plugins, MCP servers, CLAUDE.md, and auto memory for faster, reproducible CI/script execution — and will become the default for `-p` in a future release
- Channels now support **permission relay**: two-way channel servers can forward tool approval prompts to you remotely (e.g. on your phone) so you can approve or deny without being at the terminal
- Blocking PreToolUse hooks now take precedence over allow rules, clarifying hook vs. permission rule evaluation order
- New `showClearContextOnPlanAccept` setting to restore the "clear context" option on plan accept screens
- OAuth support for MCP servers extended to include Client ID Metadata Document (CIMD) discovery in addition to Dynamic Client Registration

-----

## Claude Code changes

### Changed documents

#### [channels](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/claude-code/channels.md) [[Source](https://code.claude.com/docs/en/channels)]

* Updated description of behavior when Claude hits a permission prompt while away from terminal: channel servers that declare the permission relay capability can now forward prompts for remote approval. [[line 299](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/claude-code/channels.md?plain=1#L299)] [[Source](https://code.claude.com/docs/en/channels#quickstart)]
* Added security note that the sender allowlist also gates permission relay — only allowlist senders you trust with tool-use approval authority. [[line 313](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/claude-code/channels.md?plain=1#L313)] [[Source](https://code.claude.com/docs/en/channels#security)]

#### [channels-reference](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/claude-code/channels-reference.md) [[Source](https://code.claude.com/docs/en/channels-reference)]

* Added new `capabilities.experimental['claude/channel/permission']` capability field: declaring it opts the channel server in to receiving permission relay requests from Claude Code. [[line 222](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/claude-code/channels-reference.md?plain=1#L222)] [[Source](https://code.claude.com/docs/en/channels-reference#server-options)]
* Added troubleshooting tips for when a webhook event doesn't reach Claude: how to diagnose "curl succeeds but nothing arrives" vs "connection refused". [[line 186](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/claude-code/channels-reference.md?plain=1#L186)] [[Source](https://code.claude.com/docs/en/channels-reference#example-build-a-webhook-receiver)]
* Major new section: **Relay permission prompts** (requires v2.1.81+). Covers the full relay flow, `notifications/claude/channel/permission_request` payload fields, three-step implementation guide (declare capability, handle inbound request, intercept verdict in inbound handler), and a complete `webhook.ts` example with permission relay, reply tool, sender gating, and SSE event stream. [[lines 511-872](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/claude-code/channels-reference.md?plain=1#L511-L872)] [[Source](https://code.claude.com/docs/en/channels-reference#relay-permission-prompts)]
* Updated two-way webhook example to use SSE (`GET /events`) for watching outbound replies live via `curl -N`. [[line 381](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/claude-code/channels-reference.md?plain=1#L381)] [[Source](https://code.claude.com/docs/en/channels-reference#expose-a-reply-tool)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* New `--bare` flag added: minimal mode that skips auto-discovery of hooks, skills, plugins, MCP servers, auto memory, and CLAUDE.md for faster scripted calls. Sets `CLAUDE_CODE_SIMPLE`. [[line 35](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/claude-code/cli-reference.md?plain=1#L35)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Updated `CLAUDE_CODE_SIMPLE` description to clarify it disables auto-discovery of hooks, skills, plugins, MCP servers, and auto memory (not just MCP tools/hooks), and that `--bare` sets this variable. [[line 67](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/claude-code/env-vars.md?plain=1#L67)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [headless](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* New **"Start faster with bare mode"** section documenting `--bare`: explains what it skips, why it's useful for CI/scripts, what tools remain available, how to supply context explicitly via flags, authentication requirements, and that it will become the default for `-p` in a future release. [[lines 41-69](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/claude-code/headless.md?plain=1#L41-L69)] [[Source](https://code.claude.com/docs/en/headless#start-faster-with-bare-mode)]

#### [how-claude-code-works](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/claude-code/how-claude-code-works.md) [[Source](https://code.claude.com/docs/en/how-claude-code-works)]

* Added "auto memory" to the list of items stored in the context window. [[line 110](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/claude-code/how-claude-code-works.md?plain=1#L110)] [[Source](https://code.claude.com/docs/en/how-claude-code-works#the-context-window)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Expanded `Ctrl+O` (toggle verbose output) description: it also expands MCP read and search calls that otherwise collapse to a single summary line (e.g. "Queried slack"). [[line 20](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/claude-code/interactive-mode.md?plain=1#L20)] [[Source](https://code.claude.com/docs/en/interactive-mode#general-controls)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Clarified OAuth setup: Claude Code now also supports MCP servers that use a Client ID Metadata Document (CIMD) instead of Dynamic Client Registration, and discovers these automatically. [[line 1380](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/claude-code/mcp.md?plain=1#L1380)] [[Source](https://code.claude.com/docs/en/mcp#use-pre-configured-oauth-credentials)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Clarified that a blocking PreToolUse hook (exit code 2) takes precedence over allow rules — the block applies even when an allow rule would otherwise permit the call. Includes guidance on combining an allow rule with a selective blocking hook. [[line 193](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/claude-code/permissions.md?plain=1#L193)] [[Source](https://code.claude.com/docs/en/permissions#extend-permissions-with-hooks)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New `showClearContextOnPlanAccept` setting: shows the "clear context" option on the plan accept screen. Defaults to `false`; set to `true` to restore the option. [[line 184](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/claude-code/settings.md?plain=1#L184)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

-----

## API changes

### Changed documents

#### [remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/ae8af7d6ed211664f84218975d50b3a2cd387439/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Several new MCP servers added to the directory: Aiwyn Tax (federal & state tax returns), Base44 (app building/management), Bigdata.com (real-time financial data), Calendly (event scheduling), Common Room (GTM Copilot), Intuit TurboTax (tax refund estimates), Qlik (data analytics), and tldraw (sketching/diagramming with Claude).
* Clockwise (scheduling) removed from the MCP server list.
