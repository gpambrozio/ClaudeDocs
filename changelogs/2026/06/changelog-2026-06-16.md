# [Claude docs changes for June 16th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/769966ef) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/769966ef)]

## Executive Summary
- Claude Opus 4 and Sonnet 4 are now officially **retired** (except on specific third-party platforms) — reflected across all model reference tables and the code execution, computer use, batch processing, and multilingual benchmark docs
- **CMEK now supports Claude Enterprise** with organization-level scoping — the CMEK overview and all three provider guides (AWS, Azure, GCP) have been expanded with Claude Enterprise setup flows
- Six new settings were documented in `settings.json`: `agentPushNotifEnabled`, `autoCompactEnabled`, `fileCheckpointingEnabled`, `inputNeededNotifEnabled`, `theme`, and `verbose`
- **Version 2.1.178** ships `Tool(param:value)` syntax for permission rules, nested `.claude/skills` directory support, and fixes for 13+ bugs including an out-of-memory crash and subagent transcript/messaging issues
- Two new weekly digests cover Weeks 23 and 24: auto mode on Bedrock/Vertex/Foundry, `/cd` command, nested sub-agents, and `--safe-mode`

## New Claude Code versions

### [2.1.178](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/versions/2.1.178.md)

#### New features

* Added `Tool(param:value)` syntax for permission rules to match a tool's input parameters (with `*` wildcard), e.g. `Agent(model:opus)` to block Opus subagents
* Skills in nested `.claude/skills` directories now load when working on files there; on a name clash, the nested skill appears as `<dir>:<name>` so both stay available

#### Existing feature improvements

* Nested `.claude/` directories: the agent, workflow, and output-style closest to the working directory now wins on name collisions; project-scope workflow saves target the closest existing `.claude/workflows/`
* Improved auto mode: subagent spawns are now evaluated by the classifier before launch, closing a gap where a subagent could request a blocked action without review
* Improved `/doctor` with consistent flat tree layout, clearer section status icons, and highlighted command names
* Improved skill listing truncation warning to show how many skill descriptions are affected
* Changed the workflow prompt keyword to use a purple shimmer highlight and trigger only on explicit phrases like "run a workflow" or "workflow:", not on any mention of the word
* Improved Remote Control error messages: connection failures show a persistent red "/rc failed" indicator; the "not yet enabled" error now explains whether it's a gate, a check failure, stale entitlement, or org policy
* `/bug` now requires a description before submitting, and no longer uses model-refusal text as the GitHub issue title

#### Major bug fixes

* Fixed a crash (out-of-memory) when the CLI inherits a stale websocket/OAuth file-descriptor environment variable from a parent process
* Fixed Claude in Chrome silently failing to connect when the OAuth token belongs to a different account than the Claude Code login
* Fixed nested `.claude/skills` skills with directory-qualified names being blocked by permission prompts in non-interactive runs
* Fixed several subagent issues: viewing a subagent's transcript now shows tool results and live progress, messages sent while it finishes its turn are no longer dropped, and backgrounding a running subagent (ctrl+b) no longer restarts it from scratch
* Fixed `claude agents` workers failing with `401 Invalid bearer token` when the daemon was started from a shell with a custom API gateway via `ANTHROPIC_BASE_URL` and `ANTHROPIC_AUTH_TOKEN`
* Fixed compaction not honoring `--fallback-model`
* Fixed model requests continuing to fail with auth errors after credentials were refreshed outside the session
* Fixed background sessions created with `/bg` or `←←` after a turn finished showing "Working" forever in the agents list
* Fixed MCP server-level specs in subagent `disallowedTools` being silently ignored
* Fixed vim mode undo: `u` now steps through commands one at a time instead of merging quick successive commands into a single undo step
* Fixed statusline links with custom URI schemes (e.g. `vscode://`) not opening when clicked in `claude agents`
* [VSCode] Fixed pressing Esc to dismiss a CJK IME candidate window canceling the running Claude task

-----

## Claude Code changes

### New Documents

#### [What's new — Week 23](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/claude-code/whats-new/2026-w23.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w23)]

Week 23 digest (June 1–5, 2026, v2.1.158–v2.1.165) covering: auto mode now available on Bedrock, Vertex, and Foundry for Opus 4.7/4.8 (opt in with `CLAUDE_CODE_ENABLE_AUTO_MODE=1`); safer automatic edits that prompt before writing shell startup files, git config, and build-tool configs in `acceptEdits` mode; `/plugin list` command for inline plugin listing with `--enabled`/`--disabled` filters; and `requiredMinimumVersion`/`requiredMaximumVersion` managed settings for enforcing approved Claude Code version ranges.

#### [What's new — Week 24](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/claude-code/whats-new/2026-w24.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w24)]

Week 24 digest (June 8–12, 2026, v2.1.166–v2.1.176) covering: `/cd` command to move the current session to a different working directory without rebuilding the prompt cache; sub-agents can now spawn their own sub-agents (background chains capped at five levels deep); `--safe-mode` / `CLAUDE_CODE_SAFE_MODE` launches with all customizations disabled for troubleshooting; and `fallbackModel` now configures up to three ordered fallback models and applies to interactive sessions too.

### Changed documents

#### [Agent view](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* `claude daemon status` now warns when the running supervisor is on a different version than the `claude` binary you invoked (can happen after an update before the supervisor restarts); it shows both versions and tells you to run `claude daemon stop --any` to pick up the new version. [[lines 428-429](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/claude-code/agent-view.md?plain=1#L428-L429)] [[Source](https://code.claude.com/docs/en/agent-view#where-state-is-stored)]

#### [Desktop](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Updated the "Still stuck?" support guidance: users are now directed to use **Help → Get Support** in the desktop app first, and GitHub Issues is reserved for problems that also reproduce in the standalone `claude` CLI.

#### [Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Added clarification that the label shown for a tool in the transcript and permission dialog can differ from its canonical name (e.g., `Stop Task` in the UI vs. `TaskStop` canonical name); permission rules and hook matchers match only the canonical name. [[line 111](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/claude-code/permissions.md?plain=1#L111)] [[Source](https://code.claude.com/docs/en/permissions#tool-name-wildcards)]

#### [Remote control](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Mobile push notifications now have **two separate toggles**: "Push when Claude decides" for proactive notifications and "Push when actions required" for permission prompts and questions. Both toggles can be enabled independently via `/config`. [[lines 125, 153](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/claude-code/remote-control.md?plain=1#L125)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `agentPushNotifEnabled` setting — controls proactive push notifications to your phone when Remote Control is connected (e.g., when a long task finishes). [[line 179](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/claude-code/settings.md?plain=1#L179)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* Added `autoCompactEnabled` setting — automatically compact the conversation when context approaches the limit; controllable via `DISABLE_AUTO_COMPACT` env var. [[line 190](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/claude-code/settings.md?plain=1#L190)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* Added `fileCheckpointingEnabled` setting — snapshot files before each edit so `/rewind` can restore them; controllable via `CLAUDE_CODE_DISABLE_FILE_CHECKPOINTING` env var. [[line 226](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/claude-code/settings.md?plain=1#L226)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* Added `inputNeededNotifEnabled` setting — send a push notification when a permission prompt or question is waiting for input (requires Remote Control). [[line 236](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/claude-code/settings.md?plain=1#L236)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* Added `theme` setting — configure the color theme directly in `settings.json` (supports `auto`, `dark`, `light`, daltonized, ANSI, and custom theme variants). [[line 272](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/claude-code/settings.md?plain=1#L272)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* Added `verbose` setting — show full tool output instead of truncated summaries; the `--verbose` flag overrides this for one session. [[line 276](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/claude-code/settings.md?plain=1#L276)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

#### [Troubleshoot install](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/claude-code/troubleshoot-install.md) [[Source](https://code.claude.com/docs/en/troubleshoot-install)]

* Added troubleshooting entry and fix for Homebrew error `Cask 'claude-code' is unavailable: No Cask with this name exists` — caused by a stale local cask index; fix is `brew update && brew install --cask claude-code`. Also notes that the stable cask is ~1 week behind the latest release and `claude-code@latest` cask can be used for newer versions. [[lines 19, 337-346](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/claude-code/troubleshoot-install.md?plain=1#L337-L346)]

-----

## API changes

### Changed documents

#### [Batch processing](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/api/build-with-claude/batch-processing.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing)]

* Claude Opus 4 and Claude Sonnet 4 status updated from "deprecated" to "retired, except on Vertex AI / Bedrock and Vertex AI" respectively in the pricing table.

#### [Code execution tool](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

* Removed Claude Opus 4 (`claude-opus-4-20250514`) and Claude Sonnet 4 (`claude-sonnet-4-20250514`) from the supported models list for the code execution tool, reflecting their retirement.

#### [Computer use tool](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]

* Updated model status: Claude Sonnet 4 is now "retired, except on Bedrock and Vertex AI" and Claude Opus 4 is "retired, except on Vertex AI" (previously both were labeled "deprecated").

#### [CMEK](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/api/manage-claude/cmek.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

* Major expansion: CMEK now officially supports **Claude Enterprise** in addition to Claude Platform. The overview doc now distinguishes between the two products: on Claude Platform CMEK is scoped per workspace and configured via the Admin API; on Claude Enterprise CMEK is scoped per organization and configured in `claude.ai > Organization settings > Data and privacy`. [[line 21](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/api/manage-claude/cmek.md?plain=1#L21)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]
* Added Claude Enterprise-specific breakdowns for what CMEK encrypts (chat content, attachments, Claude Code on CLI), what is disabled under CMEK (conversation history search, Analytics API, audit log exports, signed URLs), and what is not encrypted (Claude Code Desktop, web, Cowork, Office agents, Slack).

#### [CMEK — AWS KMS](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/api/manage-claude/cmek-aws-kms.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms)]

* Added a new "Register the key with Anthropic" section header with separate tabbed flows for Claude Platform (Admin API) and Claude Enterprise (Console UI). [[line 119](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/api/manage-claude/cmek-aws-kms.md?plain=1#L119)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms)]

#### [CMEK — Azure Key Vault](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/api/manage-claude/cmek-azure-key-vault.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-azure-key-vault)]

* Same as AWS KMS: added "Register the key with Anthropic" section with separate Claude Platform and Claude Enterprise tabs.

#### [CMEK — Google Cloud KMS](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/api/manage-claude/cmek-google-cloud-kms.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-google-cloud-kms)]

* Same as AWS KMS: added "Register the key with Anthropic" section with separate Claude Platform and Claude Enterprise tabs.

#### [Analytics API](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/api/manage-claude/analytics-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/analytics-api)]

* Updated the URL for creating Claude Enterprise Analytics API keys: the path changed from `claude.ai/analytics/api-keys` to `claude.ai/admin-settings/api-access` (Organization settings > API). [[line 17](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/api/manage-claude/analytics-api.md?plain=1#L17)] [[Source](https://platform.claude.com/docs/en/manage-claude/analytics-api)]

#### [Compliance API access](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/api/manage-claude/compliance-api-access.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-api-access)]

* Updated the Analytics API key creation URL in the key types table from `claude.ai/analytics/api-keys` to `claude.ai/admin-settings/api-access`.

#### [Extended thinking](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Updated model status for Claude Opus 4 and Sonnet 4 from "deprecated" to "retired, except on Vertex AI / Bedrock and Vertex AI" in the interleaved thinking compatibility list.

#### [Handling stop reasons](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/api/build-with-claude/handling-stop-reasons.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)]

* Significant doc restructuring: code examples now show multi-language tabs (cURL, CLI, Python, TypeScript, C#, Go, Java, PHP, Ruby) and use `claude-opus-4-8` as the default model. The detailed `end_turn` empty-response troubleshooting section and `max_tokens` incomplete-tool-use code block were simplified to section headings, with their content removed. Handle-truncated-response example was simplified to a single code path.

#### [Multilingual support](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/api/build-with-claude/multilingual-support.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/multilingual-support)]

* Removed Claude Opus 4 (deprecated) and Claude Sonnet 4 (deprecated) columns from the multilingual benchmark table, reflecting their retirement.

#### [Prompt caching](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* Updated Claude Opus 4 and Sonnet 4 status from "deprecated" to "retired, except on Vertex AI / Bedrock and Vertex AI" in both the pricing table and the minimum cache token size list.

#### [Search results](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/api/build-with-claude/search-results.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/search-results)]

* Updated Claude Opus 4 and Sonnet 4 status from "deprecated" to "retired" in the supported models list.

#### [Streaming](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/api/build-with-claude/streaming.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/streaming)]

* Added a "Next steps" section at the end of the doc with links to: stop reasons and fallback, fine-grained tool streaming, extended thinking, and client SDKs. [[line 565](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/api/build-with-claude/streaming.md?plain=1#L565)] [[Source](https://platform.claude.com/docs/en/build-with-claude/streaming)]

#### [Token counting](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/api/build-with-claude/token-counting.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/token-counting)]

* Added a "Next steps" section with links to: the token counting API reference, context windows, rate limits, and prompt caching. [[line 286](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/api/build-with-claude/token-counting.md?plain=1#L286)] [[Source](https://platform.claude.com/docs/en/build-with-claude/token-counting)]

#### [Tool use overview](https://github.com/gpambrozio/ClaudeDocs/blob/769966ef/docs-md/api/agents-and-tools/tool-use/overview.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)]

* Updated Claude Opus 4 and Sonnet 4 status from "deprecated" to "retired, except on Vertex AI / Bedrock and Vertex AI" in the tool use token cost table.
