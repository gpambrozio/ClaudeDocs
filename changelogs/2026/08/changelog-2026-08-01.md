# [Claude docs changes for August 1st, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/4e201639897f8e8ffe9f8b5c964baf4fe9dd66d4) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/4e201639897f8e8ffe9f8b5c964baf4fe9dd66d4)]

## Executive Summary
- The Agent SDK's permission mode table now includes a "Use case" column for each mode, and gained a new note that `"bypassPermissions"` requires `allowDangerouslySkipPermissions: true` in the TypeScript SDK.
- The Agent SDK quickstart no longer duplicates the permission modes table; it now links to the canonical table in "How the agent loop works" instead.
- The Claude Code on Claude Platform on AWS page dropped its enterprise sales promo banner.

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/agent-loop](https://github.com/gpambrozio/ClaudeDocs/blob/4e201639897f8e8ffe9f8b5c964baf4fe9dd66d4/docs-md/claude-code/agent-sdk/agent-loop.md) [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop)]

* The permission mode table gained a "Use case" column describing when to reach for each mode (e.g. `"acceptEdits"` for trusted prototyping, `"dontAsk"` for locked-down headless agents). [[lines 193-199](https://github.com/gpambrozio/ClaudeDocs/blob/4e201639897f8e8ffe9f8b5c964baf4fe9dd66d4/docs-md/claude-code/agent-sdk/agent-loop.md?plain=1#L193-L199)] [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop#permission-mode)]
* `"default"` mode's description now explicitly names the `canUseTool` callback. `"bypassPermissions"` now notes that the TypeScript SDK also requires `allowDangerouslySkipPermissions: true` in `options`. [[lines 194](https://github.com/gpambrozio/ClaudeDocs/blob/4e201639897f8e8ffe9f8b5c964baf4fe9dd66d4/docs-md/claude-code/agent-sdk/agent-loop.md?plain=1#L194), [199](https://github.com/gpambrozio/ClaudeDocs/blob/4e201639897f8e8ffe9f8b5c964baf4fe9dd66d4/docs-md/claude-code/agent-sdk/agent-loop.md?plain=1#L199)]

#### [agent-sdk/quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/4e201639897f8e8ffe9f8b5c964baf4fe9dd66d4/docs-md/claude-code/agent-sdk/quickstart.md) [[Source](https://code.claude.com/docs/en/agent-sdk/quickstart)]

* Removed the standalone permission modes table and replaced it with a short explanation plus a link to the canonical table in [How the agent loop works](https://github.com/gpambrozio/ClaudeDocs/blob/4e201639897f8e8ffe9f8b5c964baf4fe9dd66d4/docs-md/claude-code/agent-sdk/agent-loop.md), avoiding duplicated/divergent documentation. [[line 326](https://github.com/gpambrozio/ClaudeDocs/blob/4e201639897f8e8ffe9f8b5c964baf4fe9dd66d4/docs-md/claude-code/agent-sdk/quickstart.md?plain=1#L326)] [[Source](https://code.claude.com/docs/en/agent-sdk/quickstart#key-concepts)]

#### [claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/4e201639897f8e8ffe9f8b5c964baf4fe9dd66d4/docs-md/claude-code/claude-platform-on-aws.md) [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

* Removed the enterprise sales promo banner ("Deploying Claude Code across your organization?" with "View plans" / "Contact sales" links) from the top of the page. [[lines 1-5](https://github.com/gpambrozio/ClaudeDocs/blob/4e201639897f8e8ffe9f8b5c964baf4fe9dd66d4/docs-md/claude-code/claude-platform-on-aws.md?plain=1#L1-L5)] [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

-----

## API changes

No significant documentation changes today. The only edits to `docs-md/api` were regenerated Cloudflare email-obfuscation links in [files](https://github.com/gpambrozio/ClaudeDocs/blob/4e201639897f8e8ffe9f8b5c964baf4fe9dd66d4/docs-md/api/build-with-claude/files.md) and [thinking](https://github.com/gpambrozio/ClaudeDocs/blob/4e201639897f8e8ffe9f8b5c964baf4fe9dd66d4/docs-md/api/build-with-claude/thinking.md), which carry no content change.
