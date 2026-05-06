# [Claude docs changes for May 6th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/a5ffe77d33c788b0a20fcdf730a67762c9a1f25b) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/a5ffe77d33c788b0a20fcdf730a67762c9a1f25b)]

## Executive Summary
- Claude Code 2.1.129 is a major release with new plugin URL loading, auto-update support, multiagent panel fixes, and over a dozen bug fixes including critical OAuth and prompt cache TTL issues
- New Managed Agents beta (`managed-agents-2026-04-01`) introduces multiagent coordinator support: agents can now define a roster of sub-agents they can spawn within sessions
- New Sessions Threads API added for listing, retrieving, and archiving execution threads within a managed agent session
- New Webhooks API documents event types for session and vault lifecycle changes
- New `manage-claude` documentation section introduced, consolidating API management topics like authentication, data retention, rate limits, and workload identity federation

## New Claude Code versions

### [2.1.129](https://github.com/gpambrozio/ClaudeDocs/blob/a5ffe77d33c788b0a20fcdf730a67762c9a1f25b/versions/2.1.129.md)

#### New features

* Added `--plugin-url <url>` flag to fetch a plugin `.zip` archive from a URL for the current session
* Added `CLAUDE_CODE_FORCE_SYNC_OUTPUT=1` env var to force-enable synchronized output on terminals that auto-detection misses (e.g. Emacs `eat`)
* Added `CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE`: when set on Homebrew or WinGet installations, automatically runs the upgrade command in the background and prompts to restart
* Plugin manifests: `themes` and `monitors` should now be declared under `"experimental": { ... }` (top-level declarations still work but `claude plugin validate` will warn)

#### Existing feature improvements

* Gateway `/v1/models` discovery for the `/model` picker is now opt-in via `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1` (was automatic in 2.1.126–2.1.128)
* Ctrl+R history picker now defaults to searching all prompts across all projects (matching pre-2.1.124 behavior); press Ctrl+S to narrow to current project or session
* Third-party deployments (Bedrock, Vertex, Foundry, or `ANTHROPIC_BASE_URL` gateway) no longer see spinner tips pointing at first-party Anthropic surfaces
* `skillOverrides` setting now works: `off` hides from model and `/`, `user-invocable-only` hides from model only, `name-only` collapses description
* The `claude_code.pull_request.count` OTel metric now counts PRs/MRs created via MCP tools, not just shell commands
* Policy refusal error messages now include the API Request ID for easier support debugging

#### Major bug fixes

* Fixed OAuth refresh race after wake-from-sleep that could log out all running sessions
* Fixed 1-hour prompt cache TTL being silently downgraded to 5 minutes
* Fixed agent panel below the prompt being hidden when subagents are running (regression in 2.1.122)
* Fixed API errors with unrecognized 400 status codes showing raw JSON instead of the underlying error message
* Fixed `/context` dumping its rendered ASCII visualization grid into the conversation, wasting ~1.6k tokens per call
* Fixed server-managed settings policy not applying for enterprise/team users whose stored OAuth credentials lacked the `user:inference` scope
* Fixed `Bash(mkdir *)`, `Bash(touch *)` and similar allow rules not being honored for in-project paths
* Fixed `deniedMcpServers` patterns with a `*://` scheme wildcard not matching mixed-case hostnames
* Fixed cache-miss warning appearing spuriously after `/clear` or compaction when changing `/effort` or `/model`
* Fixed external-editor handoff (Ctrl+G) blanking the conversation history above the prompt
* [VSCode] Fixed `/clear` not clearing the conversation context and displayed transcript

### [2.1.131](https://github.com/gpambrozio/ClaudeDocs/blob/a5ffe77d33c788b0a20fcdf730a67762c9a1f25b/versions/2.1.131.md)

#### Major bug fixes

* Fixed VS Code extension failing to activate on Windows due to a hardcoded build path in the bundled SDK (`createRequire` polyfill bug)
* Fixed Mantle endpoint authentication failing with missing `x-api-key` header

-----

## Claude Code changes

No changes.

-----

## API changes

### New Documents

#### [api/beta/sessions/threads](https://github.com/gpambrozio/ClaudeDocs/blob/a5ffe77d33c788b0a20fcdf730a67762c9a1f25b/docs-md/api/api/beta/sessions/threads.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions/threads)]

New Sessions Threads API reference documenting execution threads within a managed agent session. Each session has one primary thread plus zero or more child threads spawned by the coordinator. Endpoints include list, retrieve, archive, and thread event streaming. Thread objects include the resolved agent snapshot, model config, skill bindings, and tool configuration at creation time.

#### [api/beta/vaults/credentials/mcp\_oauth\_validate](https://github.com/gpambrozio/ClaudeDocs/blob/a5ffe77d33c788b0a20fcdf730a67762c9a1f25b/docs-md/api/api/beta/vaults/credentials/mcp_oauth_validate.md) [[Source](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate)]

New `POST /v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate` endpoint for live-probing a vault credential against its configured MCP server. Returns a validation result including whether a refresh token is present, the outcome of a token refresh attempt, and details of any failing MCP probe step (HTTP response, status code, method that failed).

#### [api/beta/webhooks](https://github.com/gpambrozio/ClaudeDocs/blob/a5ffe77d33c788b0a20fcdf730a67762c9a1f25b/docs-md/api/api/beta/webhooks.md) [[Source](https://platform.claude.com/docs/en/api/beta/webhooks)]

New Webhooks API reference documenting the `BetaWebhookEvent` model and all supported event types. Covers lifecycle events for sessions (`session.created`, `session.pending`, `session.running`, `session.idled`, `session.requires_action`, `session.archived`, `session.deleted`), session status transitions, session threads (`session.thread_created`, `session.thread_idled`, `session.thread_terminated`), session outcome evaluation, and vault/vault credential events. Includes an `unwrap` utility function for parsing webhook payloads.

#### [manage-claude/api-and-data-retention](https://github.com/gpambrozio/ClaudeDocs/blob/a5ffe77d33c788b0a20fcdf730a67762c9a1f25b/docs-md/api/manage-claude/api-and-data-retention.md) [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

New `manage-claude` documentation section consolidates API management content previously spread across `build-with-claude`. Includes: API and data retention policies (ZDR scope, HIPAA readiness, per-feature eligibility table), authentication, Claude Code analytics API, data residency, rate limits API, usage cost API, workspaces, and workload identity federation (with provider-specific guides for AWS, Azure, GCP, GitHub Actions, Kubernetes, Okta, and SPIFFE).

### Changed documents

#### [api/beta](https://github.com/gpambrozio/ClaudeDocs/blob/a5ffe77d33c788b0a20fcdf730a67762c9a1f25b/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* New `managed-agents-2026-04-01` beta header value added to the `AnthropicBeta` enum (count increased from 20 to 21). [[line 77](https://github.com/gpambrozio/ClaudeDocs/blob/a5ffe77d33c788b0a20fcdf730a67762c9a1f25b/docs-md/api/api/beta.md?plain=1#L77)] [[Source](https://platform.claude.com/docs/en/api/beta)]
* `BetaCitationContentBlockLocation` fields now include detailed descriptions: `cited_text` explains the concatenated block range text; `start_block_index` clarifies it is 0-based; `end_block_index` clarifies it is exclusive with `end = start + 1` for single-block citations.
* `BetaCitationSearchResultLocation.search_result_index` now documents that it is 0-based and counted separately from `document_index` (server-side web search results excluded).

#### [api/beta/agents/create](https://github.com/gpambrozio/ClaudeDocs/blob/a5ffe77d33c788b0a20fcdf730a67762c9a1f25b/docs-md/api/api/beta/agents/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/agents/create)]

* New optional `multiagent` request parameter of type `coordinator` enables a multi-agent topology where the agent orchestrates work by spawning session threads, each running an agent drawn from a roster. [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/a5ffe77d33c788b0a20fcdf730a67762c9a1f25b)]
* The `agents` roster supports 1–20 entries: agent ID strings, versioned `{"type":"agent","id","version"}` references, or `{"type":"self"}` for recursive self-invocation. Referenced agents must not themselves have `multiagent` set (depth limit 1).
* `BetaManagedAgentsAgent` response object now includes a `multiagent` field returning the resolved coordinator topology with concrete agent references (each pinned to a specific version).

#### [api/beta/sessions/create](https://github.com/gpambrozio/ClaudeDocs/blob/a5ffe77d33c788b0a20fcdf730a67762c9a1f25b/docs-md/api/api/beta/sessions/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions/create)]

* Session response objects now include a `multiagent` field documenting the resolved coordinator topology (mirrors the new agent `multiagent` field). [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/a5ffe77d33c788b0a20fcdf730a67762c9a1f25b)]
* New `managed-agents-2026-04-01` beta flag documented on this endpoint.
