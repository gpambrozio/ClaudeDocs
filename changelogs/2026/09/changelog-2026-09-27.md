# [Claude docs changes for September 27th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/b1a8237ae74a190f76895277a2bac7b45d6837d3) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/b1a8237ae74a190f76895277a2bac7b45d6837d3)]

## Executive Summary

- MCP tool hooks no longer require the target server to already be connected: on blocking events like `PreToolUse` or `Stop`, Claude Code now waits (up to `MCP_TIMEOUT`) for a `cached`-status server to connect before calling the tool.
- The `cross-session-messaging` doc was substantially trimmed, removing version-history callouts (e.g. behavior "before v2.1.xxx") and several redundant asides now that those changes are no longer new.

No new Claude Code versions were released today.

-----

## Claude Code changes

### Changed documents

#### [cross-session-messaging](https://github.com/gpambrozio/ClaudeDocs/blob/b1a8237ae74a190f76895277a2bac7b45d6837d3/docs-md/claude-code/cross-session-messaging.md) [[Source](https://code.claude.com/docs/en/cross-session-messaging)]

* Extensive cleanup removing stale version-history notes (e.g. behavior differences "before v2.1.225", "before v2.1.236", "before v2.1.239", "before v2.1.247", "before v2.1.251", "before v2.1.271") now that those changes are no longer recent, along with several redundant clarifying asides. No new behavior is described; the page is shortened and simplified.

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/b1a8237ae74a190f76895277a2bac7b45d6837d3/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* MCP tool hooks (`type: "mcp_tool"`) no longer require the target server to already be connected — the doc's wording changed from "already-connected" to "configured" MCP server. [[line 392](https://github.com/gpambrozio/ClaudeDocs/blob/b1a8237ae74a190f76895277a2bac7b45d6837d3/docs-md/claude-code/hooks.md?plain=1#L392)] [[Source](https://code.claude.com/docs/en/hooks#hook-handler-fields)]
* New subsection **"When the server is still connecting"**: on blocking events such as `PreToolUse` or `Stop`, Claude Code now waits for a `cached`-status server to connect (up to `MCP_TIMEOUT` and the hook's own `timeout`) before calling the tool; on observational events like `Notification` or `SessionEnd` it doesn't wait. The hook still never triggers an OAuth flow. [[lines 558-562](https://github.com/gpambrozio/ClaudeDocs/blob/b1a8237ae74a190f76895277a2bac7b45d6837d3/docs-md/claude-code/hooks.md?plain=1#L558-L562)] [[Source](https://code.claude.com/docs/en/hooks#when-the-server-is-still-connecting)]
* The example configuration for triggering `load_context` via a `SessionStart` `mcp_tool` hook was removed, and the explanation of which events fire before MCP servers are available was consolidated into a new **"Events that fire before MCP servers are available"** subsection. [[lines 564-566](https://github.com/gpambrozio/ClaudeDocs/blob/b1a8237ae74a190f76895277a2bac7b45d6837d3/docs-md/claude-code/hooks.md?plain=1#L564-L566)] [[Source](https://code.claude.com/docs/en/hooks#events-that-fire-before-mcp-servers-are-available)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/b1a8237ae74a190f76895277a2bac7b45d6837d3/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Updated the `mcp_tool` hook type description from "an already-connected MCP server" to "a configured MCP server", matching the connection-waiting behavior now described in `hooks.md`. [[line 503](https://github.com/gpambrozio/ClaudeDocs/blob/b1a8237ae74a190f76895277a2bac7b45d6837d3/docs-md/claude-code/hooks-guide.md?plain=1#L503)] [[Source](https://code.claude.com/docs/en/hooks-guide#how-hooks-work)]

-----

## API changes

No API documentation changes today.
