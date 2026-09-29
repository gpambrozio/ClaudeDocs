# [Claude docs changes for Sept, 29th 2026](https://github.com/gpambrozio/ClaudeDocs/tree/b77c81e4fd2be3ebe745177b94d483a6074e9b1d) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/b77c81e4fd2be3ebe745177b94d483a6074e9b1d)]

## Executive Summary
- Claude Code can now start artifacts from Slides, Design, or Docs templates (`/slides`, `/design`, and a Claude Docs connector).
- Ultracode is now an independent toggle: `/effort ultracode off`, a `Tab` toggle in the `/effort` slider, and it no longer forces `xhigh` effort.
- Managed settings now fail closed on unreadable restrictive keys and repair `permissions`, `autoMode`, `worktree`, and `attribution` blocks per field.
- New Access Transparency log (beta) lets Compliance API customers cryptographically verify that their access events were not altered.
- Five new global-config settings were documented (`claudeInChromeDefaultEnabled`, `copyFullResponse`, `defaultToAgentsView`, `leftArrowOpensAgents`, `prStatusFooterEnabled`), and the API reference and SDK docs now cover Claude Sonnet 5.5 and the `between_tools` thinking config.

## New Claude Code versions

No new version files today.

-----

## Claude Code changes

Most of the ~180 changed Claude Code pages also had Markdown table padding and heading formatting normalized; those changes are not listed below.

### New Documents

None.

### Changed documents

#### [agent-sdk/modifying-system-prompts](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/agent-sdk/modifying-system-prompts.md) [[Source](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts)]

* Clarified that the system prompt cache differs across sessions when auto memory locations differ, while CLAUDE.md and environment details (working directory, platform, shell, OS version) are delivered in the conversation and don't affect the cache.
* `excludeDynamicSections` now moves per-user context (including the auto memory location or section) into the first user message; the tradeoffs note was rewritten accordingly.

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Updated the `effortLevel: "ultracode"` description to match the new ultracode behavior.

#### [agent-view](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* The `leftArrowOpensAgents` setting now only turns off the shortcut for foreground sessions and links to its reference entry.

#### [artifacts](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/artifacts.md) [[Source](https://code.claude.com/docs/en/artifacts)]

* New section on starting an artifact from a Claude Slides, Claude Design, or Claude Docs template. Templates are in beta, on by default for Pro, Max, and Team, and enabled by an Owner on Enterprise. [[line 258](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/artifacts.md?plain=1#L258)] [[Source](https://code.claude.com/docs/en/artifacts#start-from-a-slides-design-or-docs-template)]
* New `/slides` command for making a slide deck from a brief. [[line 266](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/artifacts.md?plain=1#L266)] [[Source](https://code.claude.com/docs/en/artifacts#make-a-slide-deck)]
* New section on writing documents with the `claude.ai Claude Docs` connector, and how to turn it off with `deniedMcpServers` or the `/mcp` toggle. [[line 286](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/artifacts.md?plain=1#L286)] [[Source](https://code.claude.com/docs/en/artifacts#write-a-document-with-claude-docs)]

#### [auto-mode-config](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/auto-mode-config.md) [[Source](https://code.claude.com/docs/en/auto-mode-config)]

* Explained that the bracketed text in a block message, such as `[Data Exfiltration]`, is the name of the matched classifier rule.

#### [authentication](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/authentication.md) [[Source](https://code.claude.com/docs/en/authentication)]

* Documented staying signed in to multiple accounts by giving each its own `CLAUDE_CONFIG_DIR`, with a shell alias example. [[line 29](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/authentication.md?plain=1#L29)] [[Source](https://code.claude.com/docs/en/authentication#log-in-to-claude-code)]
* On v2.1.212+, every login path applies `forceLoginMethod`, and the login screen pre-selects the forced method; the paths differ only on `forceLoginOrgUUID`.
* Trimmed version-history notes and detailed `apiKeyHelper` refresh text (now points to the settings reference).

#### [cloud-environments](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/cloud-environments.md) [[Source](https://code.claude.com/docs/en/cloud-environments)]

* `OTEL_*` environment variables are not exposed to commands Claude runs, because Claude Code uses them for its own telemetry export.
* Clarified that no server-managed setting adds domains to an environment's allowed-domains list, and that Claude Tag sessions have their own hook behavior.

#### [desktop-ios-simulator](https://github.com/gpambrozo/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/desktop-ios-simulator.md) [[Source](https://code.claude.com/docs/en/desktop-ios-simulator)]

* The simulator pane now works with Xcode 26.x or Xcode 27; the "fails with Xcode 27" troubleshooting section was replaced by a section on choosing which Xcode the pane uses via `xcode-select -s`. [[line 18](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/desktop-ios-simulator.md?plain=1#L18)] [[Source](https://code.claude.com/docs/en/desktop-ios-simulator#requirements)]
* Booted devices also appear in Device Hub on Xcode 27.

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* `The response stream was malformed` now also covers damaged stream events, which are retried silently when they arrive before any content.
* Removed the "Error during compaction: Conversation too long" section and the detailed cross-session endpoint refusal reasons.
* Expanded the Remote Control "Workspace not trusted" entry: `claude rc` now asks whether to trust the directory (v2.1.284+) and exits with code 1 if declined.
* Background-session missing-directory message now applies only when the directory was removed during startup.
* Clarified `--settings` file size limit history and the download-failure text (automatic updater no longer mentioned).

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Documented WorktreeRemove behavior for hook-created worktrees: with no hook Claude Code falls back to `git worktree remove --force`; exit 0 counts as removed; a non-zero exit fails if the directory still exists; branches are never deleted automatically. [[line 2940](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/hooks.md?plain=1#L2940)] [[Source](https://code.claude.com/docs/en/hooks#worktreeremove)]
* Prompt hooks now use the model Claude Code uses for background functionality by default, rather than Haiku.

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Prompt hooks no longer described as defaulting to Haiku.

#### [iam](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/iam.md) [[Source](https://code.claude.com/docs/en/iam)]

* Same multi-account `CLAUDE_CONFIG_DIR` guidance and `forceLoginMethod` login-path changes as in the authentication page.

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* Documented the **Ultracode** switch under the Effort row, and that feedback reports are saved locally under `~/.claude/feedback-bundles/` and not sent on third-party providers.
* Added the VS Code sessions-list filters (see vs-code).

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* In the `EffortSlider` context, Left and Right can now be rebound; only Enter and Escape are fixed.

#### [managed-mcp](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/managed-mcp.md) [[Source](https://code.claude.com/docs/en/managed-mcp)]

* `OTEL_LOG_TOOL_DETAILS=1` also adds MCP server and tool names to cost and token metric attribution.

#### [managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/managed-settings.md) [[Source](https://code.claude.com/docs/en/managed-settings)]

* Claude Tag sessions run in cloud environments but don't receive server-managed settings.
* HKCU registry is never applied beneath a present admin document. [[line 333](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/managed-settings.md?plain=1#L333)] [[Source](https://code.claude.com/docs/en/managed-settings#keys-that-fail-closed)]
* New fail-closed rules: an unreadable single-restrictive-value key (e.g. `allowManagedPermissionRulesOnly`, `disableAutoMode`) enforces the restrictive value, with exceptions for `null`, `disableAllHooks`, and quoted booleans. [[lines 338-345](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/managed-settings.md?plain=1#L338-L345)] [[Source](https://code.claude.com/docs/en/managed-settings#keys-that-fail-closed)]
* `permissions`, `autoMode`, `worktree`, and `attribution` blocks are repaired per field; `allow` grants are withheld when `deny`/`ask` lists are unreadable. Requires v2.1.282+.

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Simplified cache-entry discard rules: **Disable** and **Clear authentication** discard a server's cache entry; **Reconnect** does on connected or failed servers.
* Reworked the OAuth redirect URI / `--callback-port` instructions, including using `callbackPort` alone with dynamic client registration.
* Anthropic-provided connector `claude.ai Claude Docs` appears in `/mcp` with no setup. [[line 1087](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/mcp.md?plain=1#L1087)] [[Source](https://code.claude.com/docs/en/mcp#use-mcp-servers-from-claudeai)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* On Enterprise plans, a default saved with `/model` is also recorded on the claude.ai account and can drive the Default option (v2.1.280+).
* Ultracode is now independent of effort level: `/effort ultracode off`, a `Tab`-toggled **Ultracode** switch in the `/effort` slider, and it stays on at levels other than `xhigh`. The `/model` picker route was removed. Requires v2.1.284+. [[lines 598-602](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/model-config.md?plain=1#L598-L602)] [[Source](https://code.claude.com/docs/en/model-config#adjust-effort-level)]
* Claude Tag sessions don't receive server-managed settings.

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* New section on exporting telemetry from cloud sessions and Claude Tag, via server-managed settings `env` or environment variables, with network and credential constraints and attribution options. [[line 488](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/monitoring-usage.md?plain=1#L488)] [[Source](https://code.claude.com/docs/en/monitoring-usage#telemetry-from-cloud-sessions-and-claude-tag)]
* Repository attributes are derived identically only when HTTPS and SSH remotes name the same host and path; `vcs.repository.url.full` can be declared otherwise.
* Name-redaction rules for `agent.name`, `skill.name`, `plugin.name`, and `mcp_server.name` were reworded, and cost/token counters and API events now carry real names when `OTEL_LOG_TOOL_DETAILS=1`.

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* The outside-working-directory read prompt now has four options, including a new "Yes, but ask again next time".

#### [prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/prompt-caching.md) [[Source](https://code.claude.com/docs/en/prompt-caching)]

* Deferred tools now keep the first request's tool list for the whole conversation; upfront loading applies when tool search is below its `auto` threshold, disabled, or unavailable. [[line 107](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/prompt-caching.md?plain=1#L107)] [[Source](https://code.claude.com/docs/en/prompt-caching#connecting-or-removing-an-mcp-server)]
* Cache scope explanation updated: the system prompt embeds auto memory paths and the conversation opens with a working-directory announcement.

#### [self-hosted-environments-configuration](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/self-hosted-environments-configuration.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration)]

* New section on turning off the built-in Claude Code Remote MCP server with server-level deny rules (three possible server names). [[line 254](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L254)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration#turn-off-built-in-session-tools)]
* Spawn hook idempotency should key on the order ID, not the session ID; added a symptom to check.

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* New global-config setting `claudeInChromeDefaultEnabled` to start interactive sessions with Chrome integration on. [[line 5980](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/settings-reference.md?plain=1#L5980)] [[Source](https://code.claude.com/docs/en/settings-reference#claudeinchromedefaultenabled)]
* New `copyFullResponse` setting to make `/copy` skip the picker. [[line 5999](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/settings-reference.md?plain=1#L5999)] [[Source](https://code.claude.com/docs/en/settings-reference#copyfullresponse)]
* New `defaultToAgentsView` setting to open agent view when running `claude` with no arguments. [[line 6035](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/settings-reference.md?plain=1#L6035)] [[Source](https://code.claude.com/docs/en/settings-reference#defaulttoagentsview)]
* New `leftArrowOpensAgents` entry (default `true`). [[line 6103](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/settings-reference.md?plain=1#L6103)] [[Source](https://code.claude.com/docs/en/settings-reference#leftarrowopensagents)]
* New `prStatusFooterEnabled` setting for the PR badge in the prompt footer. [[line 6131](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/settings-reference.md?plain=1#L6131)] [[Source](https://code.claude.com/docs/en/settings-reference#prstatusfooterenabled)]
* `ultracode` setting text updated: sessions start with ultracode on without forcing `xhigh`, and `/effort ultracode off` overrides for one session.
* `wslInheritsWindowsSettings` now reads quoted booleans and `null`, and `/etc/claude-code` is read only when no Windows admin document is present.

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* New **Ultracode** switch under the Effort row when dynamic workflows are enabled.
* New "Filter the sessions list" section: an **Active** toggle and a status filter (Needs input, Working, Completed, Open, Closed), which persist across reloads. Requires v2.1.271+. [[line 290](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/vs-code.md?plain=1#L290)] [[Source](https://code.claude.com/docs/en/vs-code#filter-the-sessions-list)]
* Feedback reports are saved as a local archive; nothing is sent on third-party providers.

#### [workflows](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/claude-code/workflows.md) [[Source](https://code.claude.com/docs/en/workflows)]

* Ultracode now described as automatic workflow orchestration at whichever effort level the session runs at; `--effort ultracode` also sets `xhigh`.
* Turn it on from the `/effort` slider toggle and off with `/effort ultracode off`; turning workflows off also makes ultracode unavailable.

-----

## API changes

### New Documents

#### [manage-claude/access-transparency-log](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/api/manage-claude/access-transparency-log.md) [[Source](https://platform.claude.com/docs/en/manage-claude/access-transparency-log)]

New beta guide on verifying Access Transparency events with an append-only, signed transparency log read through the Compliance API. It explains signed checkpoints, Merkle inclusion and consistency proofs, and the C2SP tlog-tiles format, so you can check on your own infrastructure that no event was removed or altered. The log is created when the first event is recorded after enablement, and until then its endpoints return 404.

#### [release-notes/system-prompts/claude-sonnet-5-5](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/api/release-notes/system-prompts/claude-sonnet-5-5.md) [[Source](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-sonnet-5-5)]

New page with the Claude Sonnet 5.5 system prompt used on claude.ai and the mobile apps, starting with the September 28, 2026 version.

#### [release-notes/system-prompts/claude-sonnet-5](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/api/release-notes/system-prompts/claude-sonnet-5.md) [[Source](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-sonnet-5)]

New page with the Claude Sonnet 5 system prompt (June 30, 2026 version).

### Changed documents

#### [api/beta](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* `claude-sonnet-5-5` added to the model lists for Messages, batches, token counting, and Managed Agents (`BetaManagedAgentsModel`).
* New `BetaThinkingConfigBetweenTools` thinking config (`type: "between_tools"`) in Messages requests.
* `stream` docs now recommend `messages.stream()` in the TypeScript, Python, and Ruby SDKs.
* The session events list `types` filter is now a typed enum of event types.
* The same changes were propagated to the per-endpoint beta, CLI, and per-language SDK reference pages.

#### [api/beta/organization/analytics/retrieve_summaries](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/api/api/beta/organization/analytics/retrieve_summaries.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/analytics/retrieve_summaries)]

* Response now uses a `data` / `next_page` envelope (`summaries` is deprecated), with new `limit` and `page` parameters.
* Added Cowork and optional per-product (chat, Claude Code, Claude Design, Office agent, Claude Science) active-user counts.

#### [api/compliance/activities/list](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/api/api/compliance/activities/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/activities/list)]

* Two new activity types: `claude_plugin_downloaded` and `platform_organization_created`.
* Artifact `title` is deprecated and no longer populated; a `token_jti` field was added to token minted events.

#### [manage-claude/access-transparency](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/api/manage-claude/access-transparency.md) [[Source](https://platform.claude.com/docs/en/manage-claude/access-transparency)]

* Events are now tamper-evident through the transparency log, with new `workspace_uuid` and `transparency_log_leaf_index` fields and a new FAQ entry.

#### [manage-claude/compliance-activity-feed](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/api/manage-claude/compliance-activity-feed.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed)]

* Clarified that `user_actor` can also cover processes Anthropic runs on a user's behalf.

#### [manage-claude/compliance-faq](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/api/manage-claude/compliance-faq.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-faq)]

* No Compliance API endpoint lists Cowork scheduled tasks or Claude Code routines.

#### [manage-claude/compliance-sessions](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/api/manage-claude/compliance-sessions.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-sessions)]

* Cloud Claude Code routines are listed among the cloud sessions that aren't remote sessions.

#### [models/sonnet-5-5/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/api/models/sonnet-5-5/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide)]

* `between_tools` thinking examples now use typed SDK classes in C#, Go, Java, PHP, and Ruby instead of raw JSON workarounds.

#### [models/sonnet-5-5/overview](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/api/models/sonnet-5-5/overview.md) [[Source](https://platform.claude.com/docs/en/models/sonnet-5-5/overview)]

* Added an announcement link plus System prompt and System card resource cards.

#### [models/sonnet-5/overview](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/api/models/sonnet-5/overview.md) [[Source](https://platform.claude.com/docs/en/models/sonnet-5/overview)]

* Sonnet 5 is now presented as a legacy model: the overview and what's-new sections were removed, and a System prompt card was added.

#### [build-with-claude/prompt-engineering/prompting-claude-sonnet-5](https://github.com/gpambrozio/ClaudeDocs/blob/b77c81e4fd2be3ebe745177b94d483a6074e9b1d/docs-md/api/build-with-claude/prompt-engineering/prompting-claude-sonnet-5.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5)]

* Removed the migration-from-Sonnet-4.6 references and links to the what's-new page.

#### SDK and CLI version bumps

* The Java SDK examples moved from 2.65.0 to 2.66.0 (`cli-sdks-libraries/sdks/java`, `get-started`, `agents-and-tools/mcp-connector`, and the Bedrock, Foundry, Vertex, and Claude Platform on AWS pages) and the `ant` CLI from 1.35.0 to 1.36.0 (`cli-sdks-libraries/cli/quickstart`, `managed-agents/quickstart`, `managed-agents/self-hosted-sandboxes`).
