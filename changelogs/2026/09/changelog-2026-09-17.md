# [Claude docs changes for September 17th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/2ea274ea98ab85fc4f6cf1c4a29a80961770177d) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/2ea274ea98ab85fc4f6cf1c4a29a80961770177d)]

## Executive Summary
- Skills and plugins enabled on your claude.ai account now sync automatically into terminal sessions when you're signed in, no longer requiring non-interactive mode or an env var for skills, and extending plugin sync beyond Cowork/cloud sessions for the first time
- 2.1.274 adds a critical-memory warning with recovery steps, and fixes several stuck-session bugs: endless "unexpected tool_use_id" retries, a lost `/goal` after resuming a compacted session, and hook-driven sessions failing with "Prompt is too long" instead of compacting
- Marketplace and plugin git clones no longer download Git LFS content at all — files arrive as pointers, and the `skipLfs` field is now a no-op
- The Compliance API's local session endpoints now cover Claude in Chrome sessions (`claude_in_chrome`), in beta for Claude Enterprise organizations
- The Agent SDK's Python `system_prompt` gains an object form (`SystemPromptCustom`) with `snapshot` control, and hooks can now inject mid-session instruction updates via `additionalContext` without touching the recorded system prompt

## New Claude Code versions

### [2.1.274](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/versions/2.1.274.md)

#### New features

* Added a visible warning when memory usage is critical, with steps to free memory or restart safely
* Added `CLAUDE_CODE_MCP_STARTUP_WAIT_MS` to bound how long the first non-interactive turn waits for connecting MCP servers (`0` = don't wait)
* Added click-to-expand for collapsed teammate and agent messages in fullscreen mode
* Added `claude_code.managed_settings_resolved` OTel event, and an `effort` attribute on the `claude_code.llm_request` trace span
* [VSCode] Added continuation of the step a window reload interrupted, with a Claude Code: Continue After Reload setting to turn it off
* [VSCode] Added Memory and Instructions entries to the Customize menu, and a `claudeCode.lockEditorGroups` setting
* [Claude Code on the web] Added a "Compare against" branch picker to a cloud session's diff view
* [Claude Tag] Added a Guests setting to the Add channel and Add workspace forms in admin settings

#### Existing feature improvements

* Changed Bedrock, Vertex, Foundry and telemetry-disabled installs to use the v2 MCP client and MCP 2026-07-28 negotiation with direct HTTP servers by default
* Changed marketplace and plugin repository clones to leave Git LFS files as pointers instead of downloading them
* Changed `/code-review` to use leaner inline review prompts instead of spawning many review subagents
* Improved `OTEL_LOG_RAW_API_BODIES=file:<dir>` output with a new `index.jsonl` linking each response to its request file and transcript message
* Improved Claude apps gateway boot (retries the first Postgres connection) and its spend-limit check (one database round trip instead of four)
* Improved headless and SDK sessions to answer already-queued background-task completions with a single model call instead of one per task
* [VSCode] Improved screen reader navigation of the conversation

#### Major bug fixes

* Fixed sessions getting stuck endlessly retrying "unexpected tool_use_id" 400 errors; corrupted transcripts now self-heal where possible
* Fixed hook-driven sessions (such as an active `/goal`) ending with "Prompt is too long" instead of compacting, and fixed an active `/goal` being lost when resuming a compacted session
* Fixed MCP servers configured as `http` that only speak legacy HTTP+SSE failing to connect on a 422 or other 4xx first response
* Fixed Streamable HTTP MCP tool calls timing out after about 5 minutes even with a longer per-server `timeout`
* Fixed MCP tool calls refused with 403 insufficient_scope being reported as an expired sign-in instead of naming the missing permissions
* Fixed `claude agents` losing `--model`, `--effort`, `--permission-mode`, and other flags after an auto-update relaunch
* Fixed subagents with `model: "opus"` on Bedrock, Vertex, or Foundry leaving the session's model when its id has no recognizable model family
* Fixed self-hosted runner sessions failing every turn with a 401 after a few failed token refreshes
* Fixed a per-turn slowdown when a language server publishes project-wide diagnostics for thousands of files
* Fixed the Bash tool re-sourcing the shell profile after every plugin reload instead of only when plugins' `bin/` directories changed
* Fixed Bash permission checks and worktree-isolated session checks for certain special shell variables and nested shell expansions
* Fixed background commands being stopped after 30 idle minutes under mild memory pressure instead of only when memory is critically low

-----

## Claude Code changes

### Changed documents

#### [admin-setup](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/admin-setup.md) [[Source](https://code.claude.com/docs/en/admin-setup)]

* Added a "Disable claude.ai sync" managed-settings row: `syncClaudeAiSkills`/`syncClaudeAiPlugins` stop skill/plugin syncing, and turning off Skills for the org on claude.ai now also removes already-synced copies on v2.1.273+. [[line 92](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/admin-setup.md?plain=1#L92)] [[Source](https://code.claude.com/docs/en/admin-setup#decide-what-to-enforce)]

#### [agent-sdk/modifying-system-prompts](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/agent-sdk/modifying-system-prompts.md) [[Source](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts)]

* New "Update Claude's instructions mid-session" section: send new instructions in the next user message, or return `additionalContext` from a `UserPromptSubmit`/`PostToolUse` hook, instead of changing `systemPrompt`. [[line 346](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/agent-sdk/modifying-system-prompts.md?plain=1#L346)] [[Source](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts#update-claudes-instructions-mid-session)]
* Clarified that turning `snapshot` off to iterate on prompt wording is now documented for both TypeScript and Python, and that recording defaults to on outside cloud sessions and bare mode. [[line 353](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/agent-sdk/modifying-system-prompts.md?plain=1#L353)] [[Source](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts#turn-recording-off-while-you-iterate-on-wording)]

#### [agent-sdk/observability](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/agent-sdk/observability.md) [[Source](https://code.claude.com/docs/en/agent-sdk/observability)]

* `OTEL_LOG_TOOL_CONTENT=1` now documented as producing a named `tool.output` span event, with span attributes gated separately. [[line 223](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/agent-sdk/observability.md?plain=1#L223)] [[Source](https://code.claude.com/docs/en/agent-sdk/observability#control-sensitive-data-in-exports)]

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* Added `SystemPromptCustom`, an object form of `system_prompt` (`{"type": "custom", "prompt": ..., "snapshot": ...}`) equivalent to a plain string but with `snapshot` control; requires `claude-agent-sdk` v0.2.153+. [[lines 726-893](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/agent-sdk/python.md?plain=1#L888-L901)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#claudeagentoptions)]

#### [desktop-changelog](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/desktop-changelog.md) [[Source](https://code.claude.com/docs/en/desktop-changelog)] / [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/desktop.md)

* Documented that Claude Code terminal sessions now also load the skills and plugins enabled on your claude.ai account when signed in with the same account. [[line 389](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/desktop-changelog.md?plain=1#L389)] [[Source](https://code.claude.com/docs/en/desktop-changelog#extend-claude-code)]
* Reworded the skills section: local sessions load `~/.claude/skills/` and also sync claude.ai skills; cloud sessions load synced skills instead. [[line 409](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/desktop-changelog.md?plain=1#L409)] [[Source](https://code.claude.com/docs/en/desktop-changelog#use-skills)]

#### [discover-plugins](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* Noted that plugins enabled on claude.ai sync into sessions without a marketplace install. [[line 7](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/discover-plugins.md?plain=1#L7)] [[Source](https://code.claude.com/docs/en/discover-plugins#discover-and-install-prebuilt-plugins-through-marketplaces)]
* The plugin menu's **Installed** tab now lists synced plugins with a `synced` source, manageable there unless required by the org; available in terminal sessions on v2.1.273+. [[line 325](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/discover-plugins.md?plain=1#L325)] [[Source](https://code.claude.com/docs/en/discover-plugins#manage-installed-plugins)]
* `/reload-plugins` now also fires after a claude.ai sync adds, updates, or removes a plugin. [[line 397](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/discover-plugins.md?plain=1#L397)] [[Source](https://code.claude.com/docs/en/discover-plugins#apply-plugin-changes-without-restarting)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE` now describes skipping the re-clone when a marketplace refresh can't reach or authenticate to the remote, not just on a failed `git pull`. [[line 319](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/env-vars.md?plain=1#L319)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CLAUDE_CODE_SYNC_SKILLS` and `CLAUDE_CODE_SYNC_SKILLS_INSTALL_TIMEOUT_MS` rewritten: terminal sessions signed in with claude.ai now sync skills automatically (resyncing every ~10 minutes) without needing this variable; it's now only for making a `-p` run wait for the current list on its first query. [[line 364](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/env-vars.md?plain=1#L364)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `MCP_PROTOCOL_NEGOTIATION`/`MCP_SDK_GENERATION`: without the variable, Claude Code now also probes claude.ai connector servers and defaults to the v2 runtime in more sessions, tied to feature-flag fetching rather than a fixed list of platforms. [[lines 444-446](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/env-vars.md?plain=1#L444-L446)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* With feature-flag fetching off, sessions can no longer sync claude.ai skills/plugins into the terminal, and only lose the connector-server protocol probe rather than the whole v2 MCP runtime. [[lines 503-506](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/env-vars.md?plain=1#L503-L506)] [[Source](https://code.claude.com/docs/en/env-vars#features-that-need-feature-flag-fetching)]

#### [llm-gateway-protocol](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/llm-gateway-protocol.md) [[Source](https://code.claude.com/docs/en/llm-gateway-protocol)]

* Documented the `bound to a different conversation` thinking-signature rejection: it comes from the API's preserved-thinking check and can be caused by a gateway that rewrites `system`, `tools`, or earlier `messages` content. [[lines 145-148](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/llm-gateway-protocol.md?plain=1#L145-L148)] [[Source](https://code.claude.com/docs/en/llm-gateway-protocol#automatic-retry-and-error-forwarding)]

#### [managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/managed-settings.md) [[Source](https://code.claude.com/docs/en/managed-settings)]

* Added `syncClaudeAiPlugins` to the list of cross-source keys where a `false` from any admin source turns the behavior off. [[line 162](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/managed-settings.md?plain=1#L162)] [[Source](https://code.claude.com/docs/en/managed-settings#keys-read-from-every-admin-source)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* The v1/v2 MCP client runtime choice is now framed around whether the session fetches feature flags rather than a fixed platform list, and on v2.1.274+ the v2 runtime becomes the default even in sessions that don't fetch feature flags (except Bedrock/AWS/GCP/Foundry, gateway sign-ins, and telemetry-off sessions). [[line 315](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/mcp.md?plain=1#L315)] [[Source](https://code.claude.com/docs/en/mcp#mcp-client-runtimes)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Documented the new `tool.output` span event in detail: which tools/conditions produce it, its attributes (`content`, `output`, `diff`, `file_path`, `bash_command`), and their individual gates. [[line 263](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/monitoring-usage.md?plain=1#L263)] [[Source](https://code.claude.com/docs/en/monitoring-usage#span-attributes)]
* Added `request_body_id` on `api_request_body`/`api_response_body` events, and `message.id`/`message.uuid` on the response event, to pair requests, responses, and transcript messages; also documents the new `index.jsonl` file for `file:<dir>` mode. [[lines 820-845](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/monitoring-usage.md?plain=1#L820-L845)] [[Source](https://code.claude.com/docs/en/monitoring-usage#api-request-body-event)]

#### [plugin-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Marketplace and plugin repository clones now never download Git LFS content; LFS-tracked files always arrive as pointer files. [[line 738](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/plugin-marketplaces.md?plain=1#L738)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#host-and-distribute-marketplaces)]
* Background auto-update mechanics changed: instead of `git pull`, Claude Code checks the remote for new commits and, if any are found (or the check can't authenticate), re-clones and swaps in the new checkout, leaving the existing one in place on failure. [[line 770](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/plugin-marketplaces.md?plain=1#L770)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#background-auto-updates)]
* Updated the offline/airgapped troubleshooting entry to match the new check-then-reclone behavior (previously described as a failing `git pull`). [[line 1452](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/plugin-marketplaces.md?plain=1#L1452)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#marketplace-updates-fail-in-offline-environments)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* Major rewrite of "Plugins synced from claude.ai": terminal sessions signed in with a claude.ai account now sync enabled plugins automatically in the background (v2.1.273+), not just Cowork/cloud sessions; covers required-by-org plugins, `/reload-plugins` prompts, and the new `syncClaudeAiPlugins` opt-out. [[line 409](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/plugins-reference.md?plain=1#L409)] [[Source](https://code.claude.com/docs/en/plugins-reference#edit-reload-and-disable-a-skills-directory-plugin)]
* Documents that a required org plugin can't be disabled via `claude plugin disable`, with the exact refusal message. [[line 429](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/plugins-reference.md?plain=1#L429)] [[Source](https://code.claude.com/docs/en/plugins-reference#edit-reload-and-disable-a-skills-directory-plugin)]
* Plugins are now specified in three ways instead of two, adding claude.ai account sync alongside `--plugin-dir`/marketplace. [[line 799](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/plugins-reference.md?plain=1#L799)] [[Source](https://code.claude.com/docs/en/plugins-reference#plugin-caching-and-file-resolution)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* Added `syncClaudeAiPlugins` setting (v2.1.273+): stops downloading/loading plugins synced from claude.ai, mirroring `syncClaudeAiSkills`. [[lines 744-4073](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/settings-reference.md?plain=1#L4057-L4073)] [[Source](https://code.claude.com/docs/en/settings-reference#settings-index)]
* `syncClaudeAiSkills` reworded to reflect automatic syncing in signed-in terminal sessions rather than requiring `CLAUDE_CODE_SYNC_SKILLS` in non-interactive mode.
* The `skipLfs` marketplace-source field is now a no-op, since LFS content is never downloaded on clone/update as of v2.1.274. [[line 4480](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/settings-reference.md?plain=1#L4480)] [[Source](https://code.claude.com/docs/en/settings-reference#marketplace-source-types)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `syncClaudeAiPlugins` to the table of keys where a stricter `false` value is honored across scopes. [[line 698](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/settings.md?plain=1#L698)] [[Source](https://code.claude.com/docs/en/settings#exceptions-to-managed-settings-precedence)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)] / [slash-commands](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/slash-commands.md)

* Major rewrite of "Skills synced from claude.ai": terminal sessions signed in with claude.ai now sync skills automatically at startup and resync every ~10 minutes, replacing the old `CLAUDE_CODE_SYNC_SKILLS` + non-interactive-only workflow. Lists the specific sessions where syncing doesn't happen (API-key auth, no feature-flag fetching, bare/safe mode, plugin-lockdown policy). [[line 185](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/skills.md?plain=1#L185)] [[Source](https://code.claude.com/docs/en/skills#where-synced-skills-load)]
* Documents the new `syncClaudeAiSkills: false` opt-out and that skills already synced move to `~/.claude/skills/.trash/`. [[line 189](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/skills.md?plain=1#L189)] [[Source](https://code.claude.com/docs/en/skills#where-synced-skills-load)]

#### [worktrees](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/worktrees.md) [[Source](https://code.claude.com/docs/en/worktrees)]

* Added a fourth case that blocks worktree creation: a repository git config setting that points Git LFS at an untrusted external program (`lfs.customtransfer.*`, `lfs.standalonetransferagent`), with a new `Git was not run` error and fix guidance. [[line 309](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/claude-code/worktrees.md?plain=1#L309)] [[Source](https://code.claude.com/docs/en/worktrees#worktree-creation-fails-on-a-symlinked-path)]

-----

## API changes

### Changed documents

#### [manage-claude/compliance-api](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/api/manage-claude/compliance-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-api)]

* Compliance API coverage now includes Claude in Chrome sessions alongside Cowork, Claude Code, Claude Science, and Claude for Microsoft 365. [[lines 9-58](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/api/manage-claude/compliance-api.md?plain=1#L9-L58)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-api#compliance-api)]

#### [manage-claude/compliance-faq](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/api/manage-claude/compliance-faq.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-faq)]

* Added Claude in Chrome to the local-session FAQ answer and noted its coverage is in beta, alongside Claude Science and Claude for Microsoft 365. [[lines 71-75](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/api/manage-claude/compliance-faq.md?plain=1#L71-L75)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-faq#data-coverage-and-retention)]

#### [manage-claude/compliance-sessions](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/api/manage-claude/compliance-sessions.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-sessions)]

* Added Claude in Chrome as a new local-session product surface (`claude_in_chrome`), including its row in the product/endpoint table and its `product_surface` value in the API reference. [[lines 9-123](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/api/manage-claude/compliance-sessions.md?plain=1#L27-L123)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-sessions#compliance-sessions)]

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* Added a September 18, 2026 entry announcing Claude in Chrome coverage in the Compliance API's local session endpoints. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/2ea274ea98ab85fc4f6cf1c4a29a80961770177d/docs-md/api/release-notes/overview.md?plain=1#L15)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#september-18-2026)]
