# [Claude docs changes for August 11th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/30eed30caf72c432795b0b6db137564a6fe9b56d) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/30eed30caf72c432795b0b6db137564a6fe9b56d)]

## Executive Summary
- Cross-session messaging can now start a conversation with a session on another machine, not just reply to one, and picks up your Claude Code on the web sessions based on cloud access instead of a Remote Control connection
- Two new weekly "What's new" digests landed: Week 30 covers the Claude Opus 5 launch, the Desktop iOS Simulator pane, and the Claude Security plugin; Week 32 covers cross-session messaging, self-hosted environments, and auto mode becoming the default permission mode on August 14
- Claude Code v2.1.227 fixes feature flags wrongly prompting Max users about usage credits, a Bash failure under `claude-code-action` with `allowed_non_write_users`, and `/tui` restoring a rewound conversation
- Structured outputs on Amazon Bedrock are no longer natively GA for Claude Opus 5 and Claude Opus 4.8, while mid-conversation system messages (and their cache-safe updates) now extend to Claude Sonnet 5
- CMEK documentation for Claude Managed Agents is substantially clarified: memory stores and dreams are disabled under CMEK, and vault credentials and user-profile fields are called out as Anthropic-managed encryption

## New Claude Code versions

### [2.1.227](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/versions/2.1.227.md)

#### Existing feature improvements

* Improved slash-command menu: blue now marks only the selected row, matched characters are bolded instead of recolored, and emoji or accented names keep their glyphs
* Improved performance: fewer event-loop stalls on file-not-found suggestions and at-mention size checks

#### Major bug fixes

* Fixed feature flags being evaluated without the user's subscription tier when a session started with an expired login token, which could wrongly prompt Max plan users to enable usage credits for Fable
* Fixed every Bash command failing under `claude-code-action` with `allowed_non_write_users` on GitHub-hosted runners
* Fixed `/tui` bringing back a conversation that had been rewound to before its first message

-----

## Claude Code changes

### New Documents

#### [2026-w30](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/whats-new/2026-w30.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w30)]

The Week 30 (July 20–24) digest: Claude Opus 5 becomes the default Opus model with a 1M-token context window; Claude Code Desktop on macOS gets a public-beta iOS Simulator pane that streams a live device screen next to the conversation; the Claude Security plugin runs a multi-agent vulnerability scan and writes reviewed findings to a report directory. Also covers `/code-review` moving to a background subagent, emoji-shortcode autocomplete, background-by-default forked skills, a 20-subagent concurrency default, and tighter Bash permission checks.

#### [2026-w32](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/whats-new/2026-w32.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w32)]

The Week 32 (August 3–7) digest: cross-session messaging lets Claude Code sessions message each other; self-hosted environments (public beta) run cloud sessions on your own infrastructure; auto mode becomes the default permission mode for new sessions on Pro, Max, and Team plans starting August 14. Also covers VS Code's Focus view, zip-archive plugin distribution, `/review` becoming an alias of `/code-review`, worktree-isolated `/fork`, and removal of the 200-subagent-per-session cap and the Ultraplan research preview.

### Changed documents

#### [context-window](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/context-window.md) [[Source](https://code.claude.com/docs/en/context-window)]

* Documented new proactive-compaction rules: `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` now holds any native-1M model (e.g., Sonnet 5, Fable 5) to the 200K boundary, and sessions on an unrecognized model ID (such as an LLM gateway alias) compact at an assumed window, configurable via `CLAUDE_CODE_MAX_CONTEXT_TOKENS` and `CLAUDE_CODE_DISABLE_UNKNOWN_MODEL_WINDOW_ENFORCEMENT`. [[lines 111-123](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/context-window.md?plain=1#L111-L123)] [[Source](https://code.claude.com/docs/en/context-window#set-the-auto-compact-window)]

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* `/usage-credits` now documented as opening specific pages: **Settings > Usage** for Pro/Max, **Admin settings > Usage** for Team/Enterprise billing admins. [[lines 45-47](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/costs.md?plain=1#L45-L47)] [[Source](https://code.claude.com/docs/en/costs#add-usage-credits-to-your-subscription)]

#### [cross-session-messaging](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/cross-session-messaging.md) [[Source](https://code.claude.com/docs/en/cross-session-messaging)]

* Claude can now start a conversation with a session on another of your machines, not just reply to one, as of v2.1.225; before that it could only reply. [[lines 68-79](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/cross-session-messaging.md?plain=1#L68-L79)] [[Source](https://code.claude.com/docs/en/cross-session-messaging#message-sessions-on-other-machines)]
* The session listing now separates "your cloud sessions" (shown when this session has cloud access) from "your Remote Control sessions on other machines" (shown while connected to Remote Control), replacing the earlier reply-only Remote Control category. [[lines 60-63](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/cross-session-messaging.md?plain=1#L60-L63)] [[Source](https://code.claude.com/docs/en/cross-session-messaging#see-which-sessions-claude-can-reach)]
* A `-p` (non-interactive) session held message is no longer stuck forever: it now expires against the `dialogExpiry` deadline and reports the expiry to the sender, as of v2.1.225. [[line 131](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/cross-session-messaging.md?plain=1#L131)] [[Source](https://code.claude.com/docs/en/cross-session-messaging#non-interactive-sessions)]

#### [desktop-ios-simulator](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/desktop-ios-simulator.md) [[Source](https://code.claude.com/docs/en/desktop-ios-simulator)]

* The iOS Simulator pane is now available on the Enterprise plan, in addition to Pro, Max, and Team; it was previously excluded on Enterprise. [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/desktop-ios-simulator.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/desktop-ios-simulator)]

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* New "See where fast mode spend appears" section documents where Pro/Max, Team/Enterprise, and Claude Console users each see fast mode spend. [[lines 56-66](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/fast-mode.md?plain=1#L56-L66)] [[Source](https://code.claude.com/docs/en/fast-mode#see-where-fast-mode-spend-appears)]
* Documents the "Paid Console organization" requirement: Console Evaluation-plan accounts see `/fast` refuse with a message to purchase credits. [[line 98](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/fast-mode.md?plain=1#L98)] [[Source](https://code.claude.com/docs/en/fast-mode#requirements)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* New `elicitation_url_dialog` Notification type, for when an MCP server asks you to open a browser URL. [[line 275](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/hooks.md?plain=1#L275)] [[Source](https://code.claude.com/docs/en/hooks#matcher-patterns)]
* Documents the exact timing behind notification hooks: `permission_prompt`, `elicitation_dialog`, and `elicitation_url_dialog` fire only after about 6 seconds without terminal input, and `idle_prompt` fires about 60 seconds after Claude finishes responding; use `PermissionRequest` instead for an immediate signal. [[lines 1921-1925](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/hooks.md?plain=1#L1921-L1925)] [[Source](https://code.claude.com/docs/en/hooks#notification)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* In auto mode (and plan mode while the classifier reviews commands), the classifier now also reviews each `SendMessage` send between agents before delivery, as of v2.1.222. [[line 155](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/permission-modes.md?plain=1#L155)] [[Source](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode)]

#### [plugin-dependencies](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/plugin-dependencies.md) [[Source](https://code.claude.com/docs/en/plugin-dependencies)]

* Clarifies that version constraints resolve against git tags on the plugin's own repository for `github`, `url`, and `git-subdir` sources, not always the marketplace repository, and that a plugin with no matching tag now fails install instead of silently falling back. [[line 99](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/plugin-dependencies.md?plain=1#L99)] [[Source](https://code.claude.com/docs/en/plugin-dependencies#tag-plugin-releases-for-version-resolution)]
* `archive`-sourced plugin dependencies now follow the same load-time constraint check as `npm` ones. [[line 123](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/plugin-dependencies.md?plain=1#L123)] [[Source](https://code.claude.com/docs/en/plugin-dependencies#tag-plugin-releases-for-version-resolution)]

#### [llm-gateway-protocol](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/llm-gateway-protocol.md) [[Source](https://code.claude.com/docs/en/llm-gateway-protocol)]

* When a gateway omits token-counting endpoints, Claude Code now falls back to counting context usage through the inference/messages endpoint instead of a local estimate. [[lines 40](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/llm-gateway-protocol.md?plain=1#L40), [108](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/llm-gateway-protocol.md?plain=1#L108)]

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* New `oidc.use_proxy` option (v2.1.227+) routes the gateway's own IdP requests (discovery, JWKS, token, userinfo) through the configured forward proxy, with a new "IdP requests through a forward proxy" section explaining the `CONNECT`-to-IP requirement. [[lines 74-81](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L74-L81)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#oidc)]

#### [claude-apps-gateway-spend-limits](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/claude-apps-gateway-spend-limits.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-spend-limits)]

* A running gateway now serves a protocol description at `<public_url>/protocol` listing the usage-limit response headers and the blocked-429 shape, as of v2.1.227. [[line 46](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/claude-code/claude-apps-gateway-spend-limits.md?plain=1#L46)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-spend-limits#how-enforcement-works)]

-----

## API changes

### Changed documents

#### [claude-in-amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/api/build-with-claude/claude-in-amazon-bedrock.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)]

* Structured outputs moved from the "features supported" list to "features not supported" for Claude Code on Amazon Bedrock. [[line 207](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/api/build-with-claude/claude-in-amazon-bedrock.md?plain=1#L207)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)]

#### [structured-outputs](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/api/build-with-claude/structured-outputs.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

* On Amazon Bedrock, structured outputs are no longer listed as natively GA for Claude Opus 5 and Claude Opus 4.8; the supported list now covers only Opus 4.6, Sonnet 4.6, Sonnet 4.5, Opus 4.5, and Haiku 4.5. [[line 549](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/api/build-with-claude/structured-outputs.md?plain=1#L549)] [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

#### [mid-conversation-system-messages](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/api/build-with-claude/mid-conversation-system-messages.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages)]

* Mid-conversation system messages now support Claude Sonnet 5, which was previously excluded. [[line 21](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/api/build-with-claude/mid-conversation-system-messages.md?plain=1#L21)] [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages)]

#### [prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* Claude Sonnet 5 now supports cache-safe mid-conversation system message updates, matching the change above. [[line 345](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L345)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

#### [cmek](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/api/manage-claude/cmek.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

* Claude Managed Agents data (configurations, environments, webhooks, sessions/events) is now called out as covered by CMEK on Claude Platform. [[line 65](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/api/manage-claude/cmek.md?plain=1#L65)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]
* Managed Agents memory stores and dreams are disabled under CMEK and return `invalid_request_error` (HTTP 400); previously the whole Managed Agents beta was described as disabled as a unit. [[line 86](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/api/manage-claude/cmek.md?plain=1#L86)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]
* New callouts that Managed Agents vault credentials and user-profile `name`/`external_id`/`metadata` fields are stored under Anthropic-managed encryption, not the customer key. [[lines 106-107](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/api/manage-claude/cmek.md?plain=1#L106-L107)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

#### [managed-agents/quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/api/managed-agents/quickstart.md) [[Source](https://platform.claude.com/docs/en/managed-agents/quickstart)]

* New "Build a complete app" section links three full quickstart apps that pair Managed Agents with a chat framework: Vercel's Chat SDK, assistant-ui, and CopilotKit (AG-UI). [[lines 238-262](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/api/managed-agents/quickstart.md?plain=1#L238-L262)] [[Source](https://platform.claude.com/docs/en/managed-agents/quickstart)]
* The featured "Next steps" quickstart link swapped from the Chat SDK quickstart to a new Knowledge wiki quickstart. [[line 288](https://github.com/gpambrozio/ClaudeDocs/blob/30eed30caf72c432795b0b6db137564a6fe9b56d/docs-md/api/managed-agents/quickstart.md?plain=1#L288)] [[Source](https://platform.claude.com/docs/en/managed-agents/quickstart)]
