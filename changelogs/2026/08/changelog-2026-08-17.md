# [Claude docs changes for August 17th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/1611964261ad0c066eec064bde65ca80589f885c) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/1611964261ad0c066eec064bde65ca80589f885c)]

## Executive Summary
- The Agent SDK adds a new `SDKContextUsage` payload: sending `/context` as a prompt now attaches a structured `context_usage` field (token breakdown by category, MCP tool, memory file, agent, and skill) to the assistant message that delivers the result, requiring Agent SDK v0.3.232+.
- The `permission_prompt` Notification hook now fires in Claude Desktop and VS Code extension sessions (hosted through the Agent SDK's `canUseTool` callback), about six seconds after a permission ask; a new `CLAUDE_CODE_DISABLE_PERMISSION_PROMPT_NOTIFY_HOOKS` env var turns it off there.
- A new `CLAUDE_CODE_TOOL_MEMORY_LIMIT` env var caps the memory Bash and PowerShell tool commands can use on Linux and WSL via a memory cgroup, guarding against one runaway command starving the rest of the session.
- `strictKnownMarketplaces` and `extraKnownMarketplaces` gain settings-key aliases (`allowedMarketplaces` and `additionalMarketplaces`) on Claude Code v2.1.232+.
- WebFetch's 15-minute response cache TTL is now configurable via `CLAUDE_CODE_WEBFETCH_CACHE_TTL_MS`.

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/hooks](https://github.com/gpambrozio/ClaudeDocs/blob/1611964261ad0c066eec064bde65ca80589f885c/docs-md/claude-code/agent-sdk/hooks.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

* Clarifies that in SDK sessions, `permission_prompt` now fires (once a request has waited about six seconds on `canUseTool`, requiring TypeScript SDK v0.3.233+ or Python SDK v0.2.139+) alongside the elicitation notification types; other notification types remain interactive-UI only. [[lines 653-659](https://github.com/gpambrozio/ClaudeDocs/blob/1611964261ad0c066eec064bde65ca80589f885c/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L653-L659)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#forward-notifications-to-slack)]

#### [agent-sdk/session-storage](https://github.com/gpambrozio/ClaudeDocs/blob/1611964261ad0c066eec064bde65ca80589f885c/docs-md/claude-code/agent-sdk/session-storage.md) [[Source](https://code.claude.com/docs/en/agent-sdk/session-storage)]

* The TypeScript SDK now also strips the `additionalMarketplaces` alias (not just `extraKnownMarketplaces`) when seeding a temporary config directory for store-backed resume, as of Agent SDK v0.3.232. [[line 277](https://github.com/gpambrozio/ClaudeDocs/blob/1611964261ad0c066eec064bde65ca80589f885c/docs-md/claude-code/agent-sdk/session-storage.md?plain=1#L277)] [[Source](https://code.claude.com/docs/en/agent-sdk/session-storage#resume-from-the-store)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/1611964261ad0c066eec064bde65ca80589f885c/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Documents the new `SDKContextUsage` and `SDKContextUsageCategory` types: a structured, display-field-free copy of the `/context` breakdown (model, token totals, over-limit info, and per-category/MCP-tool/memory-file/agent/skill token attribution). [[lines 1424-1517](https://github.com/gpambrozio/ClaudeDocs/blob/1611964261ad0c066eec064bde65ca80589f885c/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1424-L1517)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkcontextusage)]
* `SDKAssistantMessage` gains an optional `context_usage` field carrying that payload when a `/context` prompt's result is delivered; requires Agent SDK v0.3.232+. [[lines 1112-1126](https://github.com/gpambrozio/ClaudeDocs/blob/1611964261ad0c066eec064bde65ca80589f885c/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1112-L1126)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkassistantmessage)]
* `SDKControlGetContextUsageResponse` docs note the new `rawMaxTokens` and `percentage` fields, and that sending `/context` as a prompt attaches the new `SDKContextUsage` payload to the result message. [[lines 630-637](https://github.com/gpambrozio/ClaudeDocs/blob/1611964261ad0c066eec064bde65ca80589f885c/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L630-L637)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkcontrolgetcontextusageresponse)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/1611964261ad0c066eec064bde65ca80589f885c/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_DISABLE_PERMISSION_PROMPT_NOTIFY_HOOKS`: set to `1` to stop the `permission_prompt` Notification hook from firing in Claude Desktop/VS Code-extension (`canUseTool`-hosted) sessions. Requires v2.1.233+. [[line 228](https://github.com/gpambrozio/ClaudeDocs/blob/1611964261ad0c066eec064bde65ca80589f885c/docs-md/claude-code/env-vars.md?plain=1#L228)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `CLAUDE_CODE_TOOL_MEMORY_LIMIT`: caps memory for Bash/PowerShell tool commands on Linux/WSL (e.g. `4G`); `0` or `off` disables it. Requires v2.1.233+. [[line 341](https://github.com/gpambrozio/ClaudeDocs/blob/1611964261ad0c066eec064bde65ca80589f885c/docs-md/claude-code/env-vars.md?plain=1#L341)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `CLAUDE_CODE_WEBFETCH_CACHE_TTL_MS`: overrides WebFetch's default 15-minute (`900000`ms) response cache TTL. Requires v2.1.233+. [[line 350](https://github.com/gpambrozio/ClaudeDocs/blob/1611964261ad0c066eec064bde65ca80589f885c/docs-md/claude-code/env-vars.md?plain=1#L350)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/1611964261ad0c066eec064bde65ca80589f885c/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* New: in sessions where permission requests go through the Agent SDK's `canUseTool` callback (Claude Desktop, VS Code extension), `permission_prompt` now fires about six seconds after Claude asks for permission, doesn't defer while typing, and can be disabled with `CLAUDE_CODE_DISABLE_PERMISSION_PROMPT_NOTIFY_HOOKS`. Didn't fire in these sessions before v2.1.233. [[lines 1983-1989](https://github.com/gpambrozio/ClaudeDocs/blob/1611964261ad0c066eec064bde65ca80589f885c/docs-md/claude-code/hooks.md?plain=1#L1983-L1989)] [[Source](https://code.claude.com/docs/en/hooks#notification)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/1611964261ad0c066eec064bde65ca80589f885c/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Notes that `permission_prompt` timing now differs between terminal sessions and Agent-SDK-hosted sessions (Claude Desktop, VS Code extension, etc.), pointing to the full timing breakdown in the hooks reference. [[line 181](https://github.com/gpambrozio/ClaudeDocs/blob/1611964261ad0c066eec064bde65ca80589f885c/docs-md/claude-code/hooks-guide.md?plain=1#L181)] [[Source](https://code.claude.com/docs/en/hooks-guide#get-notified-when-claude-needs-input)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/1611964261ad0c066eec064bde65ca80589f885c/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New "Marketplace key aliases" section: on v2.1.232+, `extraKnownMarketplaces` can also be written as `additionalMarketplaces` and `strictKnownMarketplaces` as `allowedMarketplaces`; older versions ignore the alias, and Claude Code prefers the canonical key if both are set. [[lines 891-899](https://github.com/gpambrozio/ClaudeDocs/blob/1611964261ad0c066eec064bde65ca80589f885c/docs-md/claude-code/settings.md?plain=1#L891-L899)] [[Source](https://code.claude.com/docs/en/settings#marketplace-key-aliases)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/1611964261ad0c066eec064bde65ca80589f885c/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* New "Memory limit on Linux and WSL" section documenting `CLAUDE_CODE_TOOL_MEMORY_LIMIT`: applied via a memory cgroup to all of a session's Bash/PowerShell commands combined, with a changed value taking effect on the next `claude` launch. Requires v2.1.233+. [[lines 165-174](https://github.com/gpambrozio/ClaudeDocs/blob/1611964261ad0c066eec064bde65ca80589f885c/docs-md/claude-code/tools-reference.md?plain=1#L165-L174)] [[Source](https://code.claude.com/docs/en/tools-reference#memory-limit-on-linux-and-wsl)]
* Notes WebFetch's 15-minute cache TTL is now configurable via `CLAUDE_CODE_WEBFETCH_CACHE_TTL_MS` on v2.1.233+. [[line 394](https://github.com/gpambrozio/ClaudeDocs/blob/1611964261ad0c066eec064bde65ca80589f885c/docs-md/claude-code/tools-reference.md?plain=1#L394)] [[Source](https://code.claude.com/docs/en/tools-reference#web-fetch)]
